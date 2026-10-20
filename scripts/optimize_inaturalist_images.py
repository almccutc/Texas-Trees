"""Create smaller WebP delivery copies, preserving downloaded source images."""
import argparse
import hashlib
import json
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageOps

DATA = Path(__file__).resolve().parents[1] / 'data' / 'inaturalist'


def optimize(rows, max_size=960, quality=80):
    if max_size < 1 or not 1 <= quality <= 100:
        raise ValueError('Positive max size and quality between 1 and 100 required')
    for row in rows:
        original_key = row.get('original_s3_key', row['s3_key'])
        original_path = DATA / 'images' / original_key
        original_blob = original_path.read_bytes()
        original_digest = hashlib.sha256(original_blob).hexdigest()
        expected_digest = row.get('original_sha256', row['sha256'])
        if original_digest != expected_digest:
            raise ValueError(f'Source checksum changed: {original_key}')
        with Image.open(original_path) as original:
            original_dimensions = list(original.size)
            im = ImageOps.exif_transpose(original).convert('RGB')
            im.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
            encoded = BytesIO()
            im.save(encoded, format='WEBP', quality=quality, method=6)
            blob = encoded.getvalue()
            dimensions = list(im.size)
        digest = hashlib.sha256(blob).hexdigest()
        key = str(Path(original_key).with_suffix('')) + f'_w{max_size}_q{quality}_{digest[:12]}.webp'
        path = DATA / 'images' / key
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(blob)
        original_source = row.get('original_source', row['source'])
        changes = f'resized to maximum {max_size}px and converted to WebP (quality {quality}); no crop'
        same_image = row['s3_key'] == key and row['sha256'] == digest
        row.update(original_s3_key=original_key, original_sha256=original_digest,
                   original_image_dimensions=original_dimensions, original_source=original_source,
                   original_bytes=len(original_blob), image_bytes=len(blob),
                   image_dimensions=dimensions, s3_key=key, sha256=digest,
                   image_url='https://texasplants.s3.us-east-2.amazonaws.com/' + key,
                   source=original_source.removesuffix('unmodified image') + changes,
                   image_processing=dict(format='webp', max_size=max_size, quality=quality, crop=False),
                   uploaded=row.get('uploaded', False) if same_image else False)
    return rows


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-size', type=int, default=960)
    parser.add_argument('--quality', type=int, default=80)
    args = parser.parse_args()
    manifest = DATA / 'manifest.json'
    rows = optimize(json.loads(manifest.read_text()), args.max_size, args.quality)
    manifest.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + '\n')
    before = sum(r['original_bytes'] for r in rows)
    after = sum(r['image_bytes'] for r in rows)
    print(f'{len(rows)} images: {before / 1048576:.1f} MiB -> {after / 1048576:.1f} MiB ({100 * (1 - after / before):.1f}% smaller)')
    print(f'Median image: {sorted(r["image_bytes"] for r in rows)[len(rows) // 2] / 1024:.0f} KiB')
