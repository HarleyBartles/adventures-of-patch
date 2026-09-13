---
name: adventures-image-qa
description: Use when an Adventures of Patch image, asset-sheet source, compiled sheet, or deck image needs an acceptance decision after generation or editing
metadata:
  source_id: adventures-image-qa
  status: active-local
  scope: Adventures image and asset-sheet acceptance
  use_when: generated or edited candidate may enter preproduction, a deck, a receipt, or canon
  do_not_use_when: deterministic preparation has produced no image candidate or generic image review is outside Adventures
---

# Adventures image QA

## Owned decision

Select one acceptance lane and return one decision:

| Lane | Accepted result |
| --- | --- |
| `patch_scene` | `accepted_scene_art` |
| `patch_preproduction_reference` | `accepted_preproduction_reference` |
| `non_patch_preproduction_reference` | `accepted_preproduction_reference` |
| `asset_sheet_lane_compliance` | accepted compiled-sheet/package compliance |
| `anti_pattern_reference` | `accepted_antipattern_reference` |
| `deck_package_image_review` | package consistency after per-image QA |

Non-acceptance results are `edit_required`, `regenerate_required`, or `blocked`.

## Local contract

Read `.agents/runbooks/image-qa-contract.md`; for sheet candidates also read
`.agents/runbooks/asset-sheet-production-contract.md`. Those runbooks own the
evidence fields, Patch canon, acceptance gates, repair cadence, and package
requirements.

## Boundary

Generation is not acceptance. Do not promote a candidate beyond the selected
lane without the runbook evidence.
