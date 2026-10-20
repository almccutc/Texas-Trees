"""Build a local browsable gallery and contact sheets from prepared images."""
import html
import json
from PIL import Image, ImageDraw
from find_inaturalist_images import DATA

rows = json.loads((DATA / 'manifest.json').read_text())
cards = []
for row in rows:
    esc = html.escape
    cards.append(f'''<article data-name="{esc(row['plant_name'].lower())}">
      <h2>{esc(row['plant_name'])} · {esc(row['image_type'])}</h2>
      <p><i>{esc(row['scientific_name'])}</i></p>
      <a href="images/{esc(row['s3_key'])}"><img loading="lazy" src="images/{esc(row['s3_key'])}" alt="{esc(row['plant_name'] + ' ' + row['image_type'])}"></a>
      <p>{esc(row['attribution'])}</p>
      <p><a href="{esc(row['photo_url'])}">iNaturalist photo {row['photo_id']}</a> ·
      <a href="{esc(row['license_url'])}">{esc(row['license_code'].upper())}</a></p>
      <p>{'Uploaded and verified' if row['uploaded'] else 'Prepared locally; S3 upload pending'}</p>
    </article>''')
(DATA / 'gallery.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>Texas plants: selected images</title>
<style>body{font:16px system-ui;margin:2rem;background:#f4f5ef;color:#233326}h1{font-size:2rem}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1rem}article{background:white;border-radius:12px;padding:1rem}h2{font-size:1.05rem}img{width:100%;height:260px;object-fit:contain;background:#eee}a{color:#275c38}input{font:inherit;padding:.6rem;margin-bottom:1rem;width:min(90%,400px)}[hidden]{display:none}</style>
<h1>Texas plants: selected images</h1>
<p>CC0 and CC BY photographs selected for the missing seed records. Click an image to inspect it.</p>
<p>Delivery images use WebP, maximum 960 pixels on the longest side, quality 80. Source downloads are preserved; no cropping is applied.</p>
<p>County distribution fields remain unfilled pending distribution research.</p>
<input aria-label="Filter by plant name" placeholder="Filter by plant name" id="filter">
<main>''' + '\n'.join(cards) + '''</main><script>
document.querySelector('#filter').addEventListener('input',e=>{
for(const card of document.querySelectorAll('article'))card.hidden=!card.dataset.name.includes(e.target.value.toLowerCase());
});</script></html>''')
for start in range(0, len(rows), 12):
    canvas = Image.new('RGB', (1200, 1050), 'white')
    draw = ImageDraw.Draw(canvas)
    for i, row in enumerate(rows[start:start + 12]):
        x, y = (i % 3) * 400, (i // 3) * 260
        with Image.open(DATA / 'images' / row['s3_key']) as im:
            im.thumbnail((390, 225))
            canvas.paste(im, (x, y))
        draw.text((x, y + 227), row['plant_name'] + ' | ' + row['image_type'], fill='black')
        draw.text((x, y + 242), str(row['photo_id']) + ' | ' + row['license_code'], fill='black')
    canvas.save(DATA / f'review_sheet_{start // 12}.jpg')
print(f'Built gallery and contact sheets for {len(rows)} prepared images.')
