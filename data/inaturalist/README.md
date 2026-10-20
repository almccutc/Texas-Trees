The targets are the 107 commented seed records (41 species). Only photographs
whose own iNaturalist license is CC0 or CC BY are eligible. Observation licenses
are not used as evidence of photo permissions. Candidates are research-grade
observations; selections are visually checked for the requested plant part.

Current status: all 107 images (25 CC0, 82 CC BY) are uploaded to `texasplants`
and verified through public GETs with matching SHA-256 checksums. Photo licenses
and research-grade identifications were rechecked before upload. All 107 seed
entries are enabled locally with the uploaded URLs and complete photo credits.
`publish_receipt.json` records the completed batch. The live database update is
still pending server/database access or deployment. No Git push or deployment
has been performed. `s3-upload-policy.json` grants upload/read permissions only
for the curated WebP filenames in the four existing destination folders.
Six optimization/activation regression checks pass; repeated seeding was also
checked using an in-memory ORM test double, with no duplicate additions.

`selections.json` records the chosen photo IDs. `manifest.json` contains the
prepared seed values, original attribution, photo/observation links, license,
download URL, verification date, image dimensions, SHA-256, and S3 object key.
Downloaded images are in the ignored `images/` folder, arranged to match S3.
Copy that folder with the manifest if running the upload on a different machine.
The source downloads are iNaturalist's large renditions. Delivery copies are
WebP at quality 80 with a maximum dimension of 960 pixels, without upscaling or
cropping. The manifest retains source checksums and paths, records the conversion
in each credit, and uses content-specific object names for immutable caching.
Total delivery size is 17.1 MiB, reduced from 58.5 MiB (70.8% smaller).
County fields remain empty because these searches do not establish county ranges.

Name resolution: iNaturalist treats Pistacia texana as Pistacia mexicana;
Tilia americana var. caroliniana is searched as Tilia americana caroliniana.
Winecup's original Callirhoe involuta is corrected to Callirhoe involucrata.
Willow oak uses species 119983, not the similarly named species complex 1550127.

Install tooling with `python -m pip install -r requirements-curation.txt`.
From the repository root:

    python scripts/find_inaturalist_images.py
    python scripts/prepare_inaturalist_images.py
    python scripts/publish_inaturalist_images.py --prepare-seeds
    python scripts/publish_inaturalist_images.py --activate
    python seed_database.py

Publishing uses the configured AWS environment, profile, or IAM role and can
load the project's ignored `.env`. It uploads to bucket `texasplants` in
`us-east-2`, refuses to overwrite a different object, verifies the publicly
accessible bytes, and then activates only verified uploads in the seed file.
It does not modify bucket policies or ACLs. Run the final database step on the
configured server (for this project, `docker compose exec texas-tree-quiz python
seed_database.py`) after deploying the updated seed file. The project deploy
workflow also runs that step after a push to main; no push was performed here.

`--prepare-seeds` fills the commented rows for review while keeping them
disabled. `--activate` enables them only after successful public S3 verification.

Open `gallery.html` locally to review the photographs, credits, and license links.
Rebuild it with `python scripts/preview_inaturalist_images.py` after updates.
Preparation now creates optimized delivery copies automatically. To regenerate
them from the preserved downloads without fetching again, run
`python scripts/optimize_inaturalist_images.py`, then refresh the prepared seeds
and gallery. Originals stay in the ignored `images/` folder alongside WebP copies.
