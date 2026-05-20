# assets index

Reusable visual assets, canonical asset docs, source packages, receipt packages, and machine-readable GPT view-surface registries.

## Files in this directory

- `TAXONOMY.md` - durable asset taxonomy contract and migration posture.

No other direct asset files are expected at this level. Navigate into subdirectories.

## Subdirectories

- `adventures/` - adventure-specific asset families and preproduction sheet sets. See `adventures/INDEX.md`.
- `characters/` - character asset families. See `characters/INDEX.md`.
- `environments/` - environment/location asset families. See `environments/INDEX.md`.
- `hero-patch/` - canonical Patch visual references. See `hero-patch/INDEX.md`.
- `png_chunks/` - self-contained PNG chunk packages derived from canonical assets. See `png_chunks/INDEX.md`.
- `style/` - Adventures of Patch style-system sheets and sidecar guide. See `style/INDEX.md`.
- `receipts/` - receipt packages and evidence bundles. See `receipts/INDEX.md`.
- `source-zips/` - committed source/import zip packages. See `source-zips/INDEX.md`.
- `view-surfaces/` - machine-readable durable GPT view-surface registry for repo-canonical images. See `view-surfaces/INDEX.md`.

## Notes for agents

Patch references in `hero-patch/` are canonical for Patch image planning and generation.

Non-Patch character and environment families are optional. Do not force them into a deck just because they exist.

Repo image files remain canonical source truth. When GPT needs a durable visual inspection surface for a repo image, use `view-surfaces/google-slides-registry.json`. Do not add Google Slides links or per-image view pointers to ordinary asset-family indexes unless Harley explicitly requests a human-facing report.

## Taxonomy posture

The current repo still uses the live roots listed above. The taxonomy contract in `TAXONOMY.md` defines the target shape and the migration order before any asset moves begin.

Current future-shape targets are documented in the contract only:

- `assets/canon/patch/role-kits/` for Patch role kits.
- `assets/views/` for the future view-surface root name.
- `assets/evidence/receipts/` for the future receipts root name.
- `assets/packs/issue-*/` for adventure-scoped packs.
- `assets/characters/heist-crew/` for the heist crew family.
