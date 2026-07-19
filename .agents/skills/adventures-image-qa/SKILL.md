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

## Overview

Generation proves only that pixels exist. This skill owns the single acceptance
decision for Adventures images; orchestration skills may plan or generate, but
they may not accept their own output.

## Select one lane

| Lane | Accepted result |
| --- | --- |
| `patch_scene` | `accepted_scene_art` for Patch body-slide or scene art |
| `patch_preproduction_reference` | `accepted_preproduction_reference` |
| `non_patch_preproduction_reference` | `accepted_preproduction_reference` |
| `asset_sheet_lane_compliance` | accepted compiled-sheet/package compliance |
| `anti_pattern_reference` | `accepted_antipattern_reference` |
| `deck_package_image_review` | package consistency after per-image QA |

Read `playbooks/image-qa-contract.md` and
`playbooks/asset-sheet-production-contract.md` when the candidate is a sheet.
Record the image identifier, intended use, source issue/package, references
considered, Patch presence, lane, decision, exact failures, repair guidance,
and whether it counts toward `asset_ready` or scene inventory readiness.

## Acceptance gates

Reject or block when the candidate fails lane fit, Patch canon, non-Patch
distinction, world/frame fit, physical logic, text discipline, continuity,
template/package contract, or downstream usefulness. For Patch, enforce the
current repo-indexed canon: clean editorial vector style, teal hoodie and
antennae, off-white face panel, black oval eyes with small white highlights,
dark trousers, teal shoes, teal crossbody bag, and visible `>` mark. Reject
generic robots, screen-face bots, human substitutions, clones, glossy/plush/
photoreal/anime drift, and alternate eye styles.

For compiled sheets, require QA-accepted source images, the approved template,
compiled PNG, required sidecar/spec, correct hero-shot rule for character
sheets, and no one-shot generated sheet replacing deterministic compilation.

## Loop and stop conditions

After generation, stop for Harley review. On continuation, QA the latest
candidate; do not restart planning or ask whether QA is needed. Return one of
`accepted_scene_art`, `accepted_preproduction_reference`,
`accepted_antipattern_reference`, `edit_required`, `regenerate_required`, or
`blocked`. If the repair is clear, give concise prompt constraints that
preserve passed features, then stop after the next candidate.

Keep candidate-level decisions in the active loop. Do not post per-candidate
GitHub updates or promote an unreviewed/rejected image into a deck, package,
receipt, or canon surface.
