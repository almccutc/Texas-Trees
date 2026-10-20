"""Fetch auditable CC0/CC BY candidates; never activate unreviewed images."""
import json
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlencode

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'inaturalist'
SESSION = requests.Session()
SESSION.headers['User-Agent'] = 'TexasPlants-image-curation/1.0'
SESSION.mount('https://', HTTPAdapter(max_retries=Retry(
    total=4, backoff_factor=1, status_forcelist=(429, 500, 502, 503, 504))))


def api(endpoint, **params):
    for attempt in range(4):
        time.sleep(1.1)
        response = SESSION.get('https://api.inaturalist.org/v1/' + endpoint,
                               params=params, timeout=60)
        if response.status_code == 429 or response.status_code >= 500:
            time.sleep(5 * (attempt + 1))
            continue
        response.raise_for_status()
        return response.json()
    raise RuntimeError('iNaturalist unavailable')


def collect(target):
    slug = target['plant_name'].lower().replace(' ', '_')
    path = DATA / (slug + '.json')
    if path.exists():
        return json.loads(path.read_text())
    name = target['scientific_name']
    search_name = name.replace(' var. ', ' ')
    taxa = api('taxa', q=search_name, per_page=20)['results']
    taxa.sort(key=lambda t: 1 if t['rank'] in ('complex', 'genus') else 0)
    taxon = next((t for t in taxa if t['name'] == search_name), None)
    if taxon is None:
        taxon = next((t for t in taxa if t.get('matched_term') == name), None)
    if taxon is None:
        # Keep ambiguity explicit rather than silently substitute another species.
        result = dict(target=target, error='Exact taxon unavailable', taxa=taxa)
        path.write_text(json.dumps(result, indent=2))
        return result
    photos = {}
    searches = ['', 'bark', 'leaf'] if target['model'] == 'Trees' else ['']
    for term in searches:
        params = dict(taxon_id=taxon['id'], photo_license='cc0,cc-by',
                      quality_grade='research', photos='true', per_page=20,
                      order_by='votes', order='desc')
        if term:
            params.update(q=term, search_on='description')
        observations = api('observations', **params)['results']
        for obs in observations:
            for photo in obs['photos']:
                if photo.get('license_code') not in ('cc0', 'cc-by'):
                    continue
                if photo['id'] in photos:
                    if term and term not in photos[photo['id']]['search_terms']:
                        photos[photo['id']]['search_terms'].append(term)
                    continue
                photos[photo['id']] = dict(photo, observation_id=obs['id'],
                    observation_url=obs['uri'], taxon=obs['taxon']['name'],
                    taxon_id=obs['taxon']['id'], description=obs.get('description'),
                    place_guess=obs.get('place_guess'), search_terms=[term or 'general'])
    result = dict(target=target, taxon_id=taxon['id'], taxon_rank=taxon['rank'], accepted_name=taxon['name'], photos=list(photos.values()))
    path.write_text(json.dumps(result, indent=2))
    return result


def sheets(result):
    if 'photos' not in result:
        return
    slug = result['target']['plant_name'].lower().replace(' ', '_')
    # Prioritize explicitly described bark and leaf observations for inspection.
    photos = sorted(result['photos'], key=lambda p: (
        0 if 'bark' in p['search_terms'] else 1 if 'leaf' in p['search_terms'] else 2))
    selected = photos[:result.get('preview_limit', 80)]
    def download(photo):
        thumb = DATA / 'thumbnails' / (str(photo['id']) + '.jpg')
        thumb.parent.mkdir(exist_ok=True)
        if not thumb.exists():
            try:
                response = requests.get(photo['url'].replace('/square.', '/small.'), timeout=30)
                response.raise_for_status()
                thumb.write_bytes(response.content)
            except requests.RequestException:
                pass
    with ThreadPoolExecutor(max_workers=6) as pool:
        list(pool.map(download, selected))
    for page in range((len(selected) + 39) // 40):
        output = DATA / f'{slug}_sheet_{page}.jpg'
        if output.exists():
            continue
        canvas = Image.new('RGB', (1200, 1100), 'white')
        draw = ImageDraw.Draw(canvas)
        draw.text((10, 5), result['target']['plant_name'] + ' | ' +
                  result['target']['scientific_name'], fill='black')
        for i, photo in enumerate(selected[page * 40:(page + 1) * 40]):
            x, y = (i % 8) * 150, (i // 8) * 210 + 30
            thumb = DATA / 'thumbnails' / (str(photo['id']) + '.jpg')
            thumb.parent.mkdir(exist_ok=True)
            try:
                with Image.open(thumb) as im:
                    im.thumbnail((146, 172))
                    canvas.paste(im, (x, y))
                draw.text((x, y + 174), str(photo['id']), fill='black')
                draw.text((x, y + 187), ','.join(photo['search_terms']), fill='black')
            except Exception as exc:
                draw.text((x, y), str(exc)[:20], fill='red')
        canvas.save(output)


if __name__ == '__main__':
    targets = json.loads((DATA / 'targets.json').read_text())
    seen = set()
    for target in targets:
        if target['plant_name'] in seen:
            continue
        seen.add(target['plant_name'])
        result = collect(target)
        print(target['plant_name'], len(result.get('photos', [])), result.get('error', ''), flush=True)
        sheets(result)
