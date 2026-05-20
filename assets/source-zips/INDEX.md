# assets/source-zips index

Committed source/import zip packages.

This is a first-class asset root for canonical ingested input zips and one-time cleanup/backfill zips. It is not an ad hoc mirror-generation lane.

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

- `asset_class__character__bouncers.zip` - bouncer supporting-character asset family mirror.
- `asset_class__character__pmc__patch_mission_control_team.zip` - Patch Mission Control Team character family mirror.
- `asset_class__character__stakeholders.zip` - reusable stakeholder character family mirror.
- `asset_classs__character__other_agents.zip` - other agents character family mirror.
- `asset_class__environment__clubdb.zip` - Club DB environment/location family mirror.
- `asset_class__environment__identity_emporium.zip` - Identity Emporium environment family mirror.
- `asset_class__environment__patch_mission_control.zip` - Patch Mission Control Centre environment family mirror.
- `hero-patch.zip` - canonical Patch visual reference folder mirror.
- `style.zip` - approved style-system folder mirror.
- `receipts.zip` - receipt/evidence folder mirror.

## Subdirectories

None.

## Notes for agents

Source zips are not automatically active canon and are not visual-inspection authority. Repo image files remain canonical source truth, while Google Slides view surfaces are GPT's durable inspection surface for those repo images.

Do not rely on hard-coded legacy project-source filenames. When package inspection is specifically needed, identify the current repo-tracked zip package here and then inspect the matching zip for that package task.

Project-source visual packages are no longer expected as the normal GPT image-inspection bridge. For now, project sources should contain only asset sheet template package(s), unless Harley explicitly changes that policy.

For Patch visual work, repo text and `assets/hero-patch/` remain canonical for Patch identity, and GPT visual inspection should route through the view-surface registry when rendered image inspection is needed.

Legacy zip names that no longer match the current folder basenames were replaced during the rebuild. The previous `asset_class__hero__patch.zip` mirror is now `hero-patch.zip`, and the previous `asset_class__style__style_system.zip` mirror is now `style.zip`.

The current tracked zip files may still reflect earlier mirror semantics. They stay in place until a later migration batch reclassifies or retires them.
