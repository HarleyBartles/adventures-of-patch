---
name: adventures-visual-preproduction
description: Use when a frame-ready Adventures of Patch project needs reusable visual language, image requirements, prompt governance, or asset readiness before PPTX production
metadata:
  source_id: adventures-visual-preproduction
  status: active-local
  scope: Adventures visual preproduction and image requirements
  use_when: frame is green but the world, cast, locations, props, continuity, or prompt contract is not repeatable
  do_not_use_when: task is body-slide production, final package QA, or generic image work outside Adventures
---

# Adventures visual preproduction

## Overview

Visual preproduction makes a frame-ready Adventures world repeatable before
body-slide production. It owns the requirements and candidate-planning lane;
`adventures-image-qa` owns acceptance.

## Required route

Read, in order:

1. `playbooks/visual-preproduction.md`;
2. the relevant `assets/` indexes and current visual-bible/style references;
3. `assets/canon/patch/INDEX.md` and current Patch references when Patch appears;
4. `playbooks/asset-sheet-production-contract.md` for sheet work.

Discover assets through the index mesh. Do not hard-code source-zip names,
fixed sheet counts, or bundled paths. Record relevant references, skipped files,
positive constraints, hard negatives, lane, composition, text posture, physical
logic, continuity requirements, and the selected QA lane in the preflight
packet.

## Image requirements

Every candidate needs a stated artifact lane and intended downstream use. For
Patch-bearing prompts, preserve the current canonical character: clean
editorial vector style, teal hoodie and antennae, off-white face panel, black
oval eyes with small white highlights, dark trousers, teal shoes, and teal
crossbody bag with visible `>` mark. Keep other people, agents, systems, and
props visually distinct.

Keep operator context out of audience-facing images: no issue comments, QA
labels, candidate numbers, repo paths, process checklists, or hidden notes.
Translate known failures into concise prompt constraints and preserve features
that already passed.

## Stage boundary

Preproduction may plan and, when explicitly authorized, generate one governed
reference candidate at a time. It must not generate body-slide scene images or
call a final deck green. For asset classes, use the required
`minimal bible -> overview -> accepted learning -> member sheets` sequence and
deterministic template compilation.

Stop at generation for Harley review. On continuation, send the latest
candidate to `adventures-image-qa`; do not skip acceptance or restart planning.

## Hard boundaries

- Deterministic prep, QA, indexing, and policy work does not spend image
  credits.
- A generated candidate is not an accepted asset.
- An asset sheet is not body-slide art.
- Patch is a character and canon reference, never an agent or actor identity.
