# assets index

Reusable visual assets, canonical asset docs, source packages, receipt packages, and machine-readable GPT view-surface registries.

## Files in this directory

- `TAXONOMY.md` - durable asset taxonomy contract and migration posture.

No other direct asset files are expected at this level. Navigate into subdirectories.

## Subdirectories

- `adventures/` - adventure-specific asset families and preproduction sheet sets. See `adventures/INDEX.md`.
- `canon/` - global canonical Patch and style roots. See `canon/INDEX.md`.
- `characters/` - character asset families. See `characters/INDEX.md`.
- `evidence/` - receipt, import, transfer, and legacy evidence. See `evidence/INDEX.md`.
- `environments/` - environment/location asset families. See `environments/INDEX.md`.
- `canon/patch/` - canonical Patch visual references. See `canon/patch/INDEX.md`.
- `source-zips/` - committed source/import zip packages. See `source-zips/INDEX.md`.
- `view-surfaces/` - machine-readable durable GPT view-surface registry for repo-canonical images. See `view-surfaces/INDEX.md`.

## Notes for agents

Patch references in `canon/patch/reference_sheets/` are canonical for Patch image planning and generation.

Many character and environment families place non-source PNGs in local `reference_sheets/` subdirectories to make the artifact class obvious at the path level.

Non-Patch character and environment families are optional. Do not force them into a deck just because they exist.

Repo image files remain canonical source truth. When GPT needs a durable visual inspection surface for a repo image, use `view-surfaces/google-slides-registry.json`. Do not add Google Slides links or per-image view pointers to ordinary asset-family indexes unless Harley explicitly requests a human-facing report.

## Taxonomy posture

The current repo uses the live roots listed above. The taxonomy contract in `TAXONOMY.md` defines the live package lanes and the migration order before any future batch begins.

Current active package lanes:

- `assets/canon/patch/role-kits/asset_packs/` for Patch role kits.
- `assets/characters/<family>/asset_packs/` for character-family packs.
- `assets/adventures/<family>/asset_packs/` for adventure-scoped packs.

Current future-shape targets are documented in the contract only:

- `assets/views/` for the future view-surface root name.
- `assets/packs/issue-*/` for issue-scoped adventure packs.
- `assets/characters/heist-crew/` for the heist crew family.
