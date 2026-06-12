# Repo-Resident Visual Sidecar Proof

Status: AMBER for PATCH-21.
Date: 2026-06-12.

This proof shows the repo-resident image-sidecar mesh and the limited pixel-inspected subset available in this worker shell. It does not promote any in-flight asset to canon.

## What Landed

- `assets/visual-sidecars/schema.v0.1.json`.
- `assets/visual-sidecars/index.v0.1.json`.
- `assets/visual-sidecars/inspected_subset.v0.1.json`.
- 40 shard JSON files under `assets/visual-sidecars/shards/`.
- 5 pixel-inspected records and 168 metadata-only records.

## What Was Inspected

The following five tracked images were visually inspected and recorded with actual observed facts:

- `assets/canon/patch/reference_sheets/approved_style__v1.png`.
- `assets/templates/asset-sheets/template_asset_sheet_3hero_6alt_v4.png`.
- `assets/adventures/Tournament/asset_packs/patch-bit-bot-tournament-kit/source_images/patch_hero__v1.png`.
- `assets/environments/mission-control/asset_packs/mission-control/reference_sheets/overview__v1.png`.
- `assets/in-flight/issue_48_override_heist_style_framework_v0_3/style-sheets/Patch Approved Silhouette.png`.

## AMBER Reason

Full semantic sidecars for all 173 tracked images could not be completed in this worker shell. The branch therefore carries a real schema/index/mesh plus a representative pixel-inspected subset, and it remains honest about the 168 records that are metadata-only.

## Proposed Child Slices

- Source images by package root.
- Compiled asset sheets as a separate pass.
- Reference sheets as a separate pass.
- In-flight working references as a separate pass.
- Template inventory as a separate pass.

## Validation

- `git ls-files` inventory count: 173 tracked images.
- every shard record maps to a real tracked image path.
- no image binaries changed.
- `scripts/validate_asset_taxonomy.py --json` still passes.

## Conclusion

The branch now demonstrates the intended repo-sidecar routing layer, but it should be read as AMBER because semantic inspection coverage is partial rather than complete.
