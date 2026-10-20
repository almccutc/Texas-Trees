"""Upload reviewed images to texasplants, verify public access, then activate seeds.

Run on the configured server: python scripts/publish_inaturalist_images.py
Use --activate after successful uploads to fill the commented seed records.
AWS credentials use boto3's normal chain (environment, profile, or IAM role).
"""
import argparse
import ast
import hashlib
import json
import mimetypes
import re
from pathlib import Path

import requests

from find_inaturalist_images import DATA, ROOT, SESSION, api

BUCKET = 'texasplants'
REGION = 'us-east-2'
FIELDS = ('plant_name', 'image_type', 'image_url', 'scientific_name',
          'plant_type', 'source', 'location_counties')


def activate(rows, prepare_only=False):
    approved = {(r['model'], r['plant_name'], r['image_type']): r for r in rows
                if (r.get('uploaded') or prepare_only) and r.get('reviewed') and r['license_code'] in ('cc0', 'cc-by')}
    path = ROOT / 'seed_database.py'
    lines = []
    count = 0
    for line in path.read_text().splitlines():
        match = re.match(r'(\s*)#\s*((?:Trees|Flowers)\(.*\)),?$', line)
        if match:
            call = ast.parse(match[2], mode='eval').body
            values = [ast.literal_eval(a) for a in call.args]
            row = approved.get((call.func.id, values[0], values[1]))
            if row:
                args = ', '.join(repr(row[field]) for field in FIELDS)
                comment = '# ' if prepare_only else ''
                line = f'{match[1]}{comment}{call.func.id}({args}),'
                count += 1
        # The last existing flower lacks a comma before the commented entries.
        if line.lstrip().startswith(('Trees(', 'Flowers(')) and line.rstrip().endswith(')'):
            line += ','
        lines.append(line)
    content = '\n'.join(lines) + '\n'
    ast.parse(content)
    path.write_text(content)
    if prepare_only:
        print(f'Filled {count} commented seed records; uploads are required before activation.')
    else:
        print(f'Activated {count} seed records. Run seed_database.py against the configured database.')


def publish(activate_seeds=False):
    from dotenv import load_dotenv
    load_dotenv(ROOT / '.env', override=False)
    import boto3
    from botocore.exceptions import ClientError
    s3 = boto3.client('s3', region_name=REGION)
    if not s3._request_signer._credentials:
        raise RuntimeError('AWS credentials unavailable; configure .env, an AWS profile, or an IAM role.')
    manifest = DATA / 'manifest.json'
    rows = json.loads(manifest.read_text())
    obs_cache = {}
    for row in rows:
        if not row.get('reviewed') or row.get('license_code') not in ('cc0', 'cc-by'):
            raise ValueError('Unreviewed or disallowed photo in manifest')
        path = DATA / 'images' / row['s3_key']
        blob = path.read_bytes()
        if hashlib.sha256(blob).hexdigest() != row['sha256']:
            raise ValueError(f"Image bytes changed: {path}")
        obs_id = row['observation_id']
        if obs_id not in obs_cache:
            obs_cache[obs_id] = api('observations/' + str(obs_id))['results'][0]
        obs = obs_cache[obs_id]
        photo = next(p for p in obs['photos'] if p['id'] == row['photo_id'])
        if photo.get('license_code') != row['license_code'] or photo.get('attribution', '') != row['attribution']:
            raise ValueError('Photo license/attribution changed; rerun preparation')
        if obs['quality_grade'] != 'research' or row['taxon_id'] not in obs['taxon'].get('ancestor_ids', []) + [obs['taxon']['id']]:
            raise ValueError('Photo identification changed; review again')
        try:
            s3.put_object(Bucket=BUCKET, Key=row['s3_key'], Body=blob,
                          ContentType=mimetypes.guess_type(path.name)[0],
                          CacheControl='public, max-age=31536000, immutable',
                          Metadata={'sha256': row['sha256'], 'license': row['license_code'],
                                    'source': row['photo_url'], 'license-url': row['license_url']},
                          IfNoneMatch='*')
        except ClientError as exc:
            if exc.response['Error']['Code'] not in ('PreconditionFailed', '412'):
                raise
            existing = s3.head_object(Bucket=BUCKET, Key=row['s3_key'])
            if existing.get('Metadata', {}).get('sha256') != row['sha256']:
                raise ValueError('S3 key already exists with different content; refusing overwrite') from exc
        # A successful PUT alone does not guarantee the quiz can load the image.
        response = SESSION.get(row['image_url'], timeout=60)
        response.raise_for_status()
        if hashlib.sha256(response.content).hexdigest() != row['sha256']:
            raise ValueError('Public image checksum does not match')
        row['uploaded'] = True
        manifest.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + '\n')
        print('Uploaded and verified:', row['s3_key'], flush=True)
    if activate_seeds:
        activate(rows)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--activate', action='store_true')
    parser.add_argument('--prepare-seeds', action='store_true', help='Fill commented entries locally without uploading or activating')
    args = parser.parse_args()
    if args.prepare_seeds:
        activate(json.loads((DATA / 'manifest.json').read_text()), prepare_only=True)
    else:
        publish(args.activate)
