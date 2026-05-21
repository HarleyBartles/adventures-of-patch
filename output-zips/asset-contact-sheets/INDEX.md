# output-zips/asset-contact-sheets index

Zip output location for the Patch asset contact-sheet exporter.

## Files in this directory

None tracked by design beyond this index file. Generated zip packages land here as local output artifacts.

## Output convention

- One zip per request ID, named `<request-id>.zip`.
- The zip contains `contact-sheets/`, `included-assets/`, `manifests/`, and `evidence.json`.
- Build staging stays under `scratch/contact-sheet-builds/<request-id-or-timestamp>/`.

## Typical command

```bash
python Patch/SKILLS/patch-asset-contact-sheet-exporter/scripts/build_contact_sheets.py \
  --dispatch Patch/SKILLS/patch-asset-contact-sheet-exporter/examples/sample-dispatch.json \
  --output-root output-zips/asset-contact-sheets
```

## Notes for agents

- Keep this directory free of loose build staging.
- Do not copy source PNGs or compiled asset sheets here outside the final zip.
- Use the repo indexes and manifests for source-path provenance.
