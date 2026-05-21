# output-zips index

Local output package root for Patch-generated zip artifacts.

## Files in this directory

- `INDEX.md` - this file; root mesh entry for output package locations.

## Subdirectories

- `asset-contact-sheets/` - contact-sheet zip outputs for repo asset inspection. See `asset-contact-sheets/INDEX.md`.

## Notes for agents

- `output-zips/` should stay zip-only plus index mesh docs.
- Build staging for contact-sheet runs belongs under `scratch/contact-sheet-builds/` or another ignored local staging root.
- Do not leave loose generated contact sheets, copied asset sheets, or manifest/evidence files under `output-zips/`.
