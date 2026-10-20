"""Expand a species search when the initial photos do not show the needed part."""
import json
import sys
from find_inaturalist_images import DATA, api, collect, sheets

for name in sys.argv[1:]:
    slug = name.lower().replace(' ', '_')
    path = DATA / (slug + '.json')
    data = json.loads(path.read_text())
    target = data['target']
    if data.get('error') or name in ('Willow Oak', 'Blackjack Oak', 'Overcup Oak'):
        path.unlink()
        data = collect(target)
    if 'photos' not in data:
        print(name, data.get('error'), flush=True)
        continue
    photos = {p['id']: p for p in data['photos']}
    observations = api('observations', taxon_id=data['taxon_id'],
                       photo_license='cc0,cc-by', quality_grade='research',
                       photos='true', per_page=100, order_by='votes', order='desc')['results']
    for obs in observations:
        if data['taxon_id'] not in obs['taxon'].get('ancestor_ids', []) + [obs['taxon']['id']]:
            continue
        for photo in obs['photos']:
            if photo.get('license_code') not in ('cc0', 'cc-by') or photo['id'] in photos:
                continue
            photos[photo['id']] = dict(photo, observation_id=obs['id'],
                observation_url=obs['uri'], taxon=obs['taxon']['name'],
                taxon_id=obs['taxon']['id'], description=obs.get('description'),
                place_guess=obs.get('place_guess'), search_terms=['expanded'])
    data['photos'] = list(photos.values())
    path.write_text(json.dumps(data, indent=2))
    # Preview general/expanded photos independently from part-specific searches.
    preview = dict(data)
    preview['target'] = dict(target, plant_name=name + ' expanded')
    preview['photos'] = [p for p in data['photos'] if p['search_terms'] == ['general'] or 'expanded' in p['search_terms']]
    preview['preview_limit'] = 240
    print(name, len(preview['photos']), flush=True)
    sheets(preview)
