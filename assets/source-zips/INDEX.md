# assets/source-zips index

Committed source/import zip packages.

This is a first-class asset root for canonical ingested input zips and one-time cleanup/backfill zips, organized by asset taxonomy category. It is not an ad hoc mirror-generation lane.

When GPT needs to inspect a repo-canonical image, use the repo index mesh plus `assets/view-surfaces/google-slides-registry.json` and the recorded Google Slides view surface. Do not use source zips, project-source zips, or package mirrors as the source of image inspection truth unless the Slides route is explicitly blocked and the reduced-confidence fallback is stated.

Use source zips for bounded package tasks only, including:

- canonical input-zip storage after validation and extraction;
- one-time cleanup/backfill zip storage for already-landed assets;
- import or transfer bundle review;
- source package rebuild checks;
- receipt/evidence package handling;
- package integrity checks;
- explicit user-scoped zip inspection;
- emergency fallback when the Slides view-surface route is blocked.

## Files in this directory

- `.gitkeep` - keeps the root visible in a tracked empty-state form if category folders are temporarily empty.
- `INDEX.md` - source-zip catalogue and policy surface.

## Subdirectories

- `canon/` - canonical style and Patch visual reference input/backfill packages. See `canon/INDEX.md`.
- `characters/` - reusable character-family input/backfill packages. See `characters/INDEX.md`.
- `environments/` - reusable environment-family input/backfill packages. See `environments/INDEX.md`.
- `packs/` - reserved for future adventure-pack source bundles. See `packs/INDEX.md`.
- `templates/` - reserved for future template-pack source bundles. See `templates/INDEX.md`.
- `legacy/` - reserved for deferred or legacy source bundles that have not yet been reclassified. See `legacy/INDEX.md`.

## Notes for agents

Source zips are not automatically active canon and are not visual-inspection authority. Repo image files remain canonical source truth, while Google Slides view surfaces are GPT's durable inspection surface for those repo images.

Do not rely on hard-coded legacy flat source-zip filenames. When package inspection is specifically needed, identify the current repo-tracked zip package here and then inspect the matching zip in its category folder for that package task.

Project-source visual packages are no longer expected as the normal GPT image-inspection bridge. For now, project sources should contain only asset sheet template package(s), unless Harley explicitly changes that policy.

For Patch visual work, repo text and `assets/canon/patch/` remain canonical for Patch identity, and GPT visual inspection should route through the view-surface registry when rendered image inspection is needed.

The current tracked zip files are catalogued by asset taxonomy category. Their filenames are preserved because they remain canonical package identifiers until a later package-normalization lane says otherwise.

Receipt evidence that no longer belongs in the source-import lane lives under `assets/evidence/receipts/`.
