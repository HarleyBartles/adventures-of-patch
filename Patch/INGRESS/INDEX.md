# Patch ingress index

Canonical tracked ingress surfaces for Patch-routed incoming packages.

## Files in this directory

- `asset-zips/README.md` - canonical drop-zone contract for incoming asset zip packages.
- `asset-zips/INDEX.md` - direct-child index for the canonical asset-zip ingress lane.

## Subdirectories

- `asset-zips/` - canonical local drop zone for incoming asset zip packages. Incoming zip payloads are ignored by git and are not canon.

## Notes for agents

- Use `Patch/INGRESS/asset-zips/` as the known ingress location unless a dispatch explicitly overrides it.
- Do not commit incoming zip payloads.
- Delete successfully ingressed zips only after publication proof exists.
