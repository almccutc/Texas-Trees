"""Download reviewed images and write a provenance manifest (no AWS writes)."""
import hashlib
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import requests
from PIL import Image

from find_inaturalist_images import DATA, SESSION, api
from optimize_inaturalist_images import optimize

LICENSES = {
    'cc-by': ('CC BY 4.0', 'https://creativecommons.org/licenses/by/4.0/'),
    'cc0': ('CC0 1.0', 'https://creativecommons.org/publicdomain/zero/1.0/'),
}


def prepare(species=None):
    choices = json.loads((DATA / 'selections.json').read_text())
    targets = json.loads((DATA / 'targets.json').read_text())
    output = DATA / 'manifest.json'
    previous = json.loads(output.read_text()) if output.exists() else []
    old = {(r['plant_name'], r['image_type']): r for r in previous}
    progress = dict(old)
    rows = []
    observations = {}
    taxa = {}
    for target in targets:
        name, role = target['plant_name'], target['image_type']
        if species and name not in species:
            if (name, role) in old:
                rows.append(old[(name, role)])
            continue
        photo_id = choices.get(name, {}).get(role)
        if not photo_id:
            continue
        slug = name.lower().replace(' ', '_')
        candidates = json.loads((DATA / (slug + '.json')).read_text())
        taxon_id = candidates['taxon_id']
        if taxon_id not in taxa:
            taxa[taxon_id] = api('taxa/' + str(taxon_id))['results'][0]
        taxon = taxa[taxon_id]
        expected = target['scientific_name'].replace(' var. ', ' ')
        expected = {'Pistacia texana': 'Pistacia mexicana'}.get(expected, expected)
        if taxon['rank'] in ('complex', 'genus') or taxon['name'] != expected:
            raise ValueError(f'Incorrect taxon resolution: {name} -> {taxon["name"]} ({taxon["rank"]})')
        cached = next(p for p in candidates['photos'] if p['id'] == photo_id)
        obs_id = cached['observation_id']
        if obs_id not in observations:
            observations[obs_id] = api('observations/' + str(obs_id))['results'][0]
        obs = observations[obs_id]
        photo = next(p for p in obs['photos'] if p['id'] == photo_id)
        code = photo.get('license_code')
        if code not in LICENSES or obs['quality_grade'] != 'research':
            raise ValueError(f'License or identification changed: photo {photo_id}')
        if candidates['taxon_id'] not in obs['taxon'].get('ancestor_ids', []) + [obs['taxon']['id']]:
            raise ValueError(f'Taxon changed: photo {photo_id}')
        license_name, license_url = LICENSES[code]
        url = photo['url'].replace('/square.', '/large.')
        extension = Path(url.split('?')[0]).suffix.lower()
        if extension not in ('.jpg', '.jpeg', '.png'):
            raise ValueError(f'Unsupported image format: {url}')
        prefix = 'texas_trees/' + role if target['model'] == 'Trees' else 'flowers'
        key = f'{prefix}/{slug}_inat_{photo_id}{extension}'
        path = DATA / 'images' / key
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            response = SESSION.get(url, timeout=60)
            response.raise_for_status()
            path.write_bytes(response.content)
        with Image.open(path) as im:
            dimensions = list(im.size)
            im.verify()
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        photo_url = f'https://www.inaturalist.org/photos/{photo_id}'
        attribution = photo.get('attribution', '')
        # For CC0 retain the observer credit, explicitly identified as observer.
        credit = attribution if code == 'cc-by' else f"CC0; observer: {obs['user'].get('name') or obs['user']['login']}"
        source = f'iNaturalist Photo {photo_id}; {credit}; {photo_url}; {license_name}: {license_url}; unmodified image'
        row = dict(target, image_url=f'https://texasplants.s3.us-east-2.amazonaws.com/{key}',
                   source=source, photo_id=photo_id, observation_id=obs_id,
                   observation_url=obs['uri'], photo_url=photo_url,
                   license_code=code, license_url=license_url, attribution=attribution,
                   taxon_id=candidates['taxon_id'], accepted_name=obs['taxon']['name'],
                   downloaded_from=url, image_dimensions=dimensions, s3_key=key,
                   sha256=digest, reviewed=True,
                   license_checked_at=datetime.now(timezone.utc).isoformat(), uploaded=False)
        prior = old.get((name, role), {})
        if prior.get('sha256') == digest and prior.get('s3_key') == key:
            row['uploaded'] = prior.get('uploaded', False)
        rows.append(row)
        # Save progress after every verified photo.
        progress[(name, role)] = row
        output.write_text(json.dumps(list(progress.values()), indent=2, ensure_ascii=False) + '\n')
        print(name, role, photo_id, license_name, dimensions, flush=True)
    rows = optimize(rows)
    for row in rows:
        prior = old.get((row['plant_name'], row['image_type']), {})
        if prior.get('sha256') == row['sha256'] and prior.get('s3_key') == row['s3_key']:
            row['uploaded'] = prior.get('uploaded', False)
    output.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + '\n')
    return rows


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--species', action='append', help='Re-prepare only this species, preserving other records')
    prepare(parser.parse_args().species)
