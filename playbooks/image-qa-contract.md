# Canonical image QA contract

This playbook defines the project-level image QA contract for Adventures of Patch.

Use this playbook whenever generated or edited images may become preproduction references, body-slide art, anti-pattern references, package evidence, or reusable assets.

Asset-sheet QA must also apply `playbooks/asset-sheet-production-contract.md`. Source images and final compiled sheets are different QA moments: generated source images must be accepted before compile, and the final compiled asset sheet must then be checked against the approved template/package contract.

## Canonical image QA authority

`adventures-image-qa` is the single authoritative image QA skill.

Retired or legacy image QA skills, including Patch-specific QA wrappers, must route to `adventures-image-qa` and must not independently accept generated images.

Other skills may orchestrate image work, but they do not own acceptance:

- `adventures-visual-preproduction` owns preproduction generation loops.
- `adventures-deck-image-planner` owns image plans and inventories.
- `adventures-pptx-builder` owns build gating.
- `adventures-presentation-qa` owns package/stage QA.
- `adventures-asset-sheet-canoniser` owns canonisation and landing posture after image QA.

## Core rule

Never trust image generation.

Every generated or edited image is a candidate until `adventures-image-qa` accepts it in the correct lane.

A successful generation call proves only that an image was produced. It does not prove Patch canon, asset usefulness, slide readiness, asset-sheet template compliance, or package validity.

For asset sheets, do not treat an attractive one-shot generated full-sheet image as satisfying the final asset-sheet deliverable. The accepted path is QA-accepted source images followed by deterministic compile into the approved template and final package review.

## Semi-autonomous generation / QA loop

Use this loop for every generated or edited image that may be used downstream:

```text
plan candidate -> generate or edit candidate -> stop for Harley review/nudge
-> on continue: run adventures-image-qa
-> if edit_required or regenerate_required and the repair target is known and well defined, edit/regenerate immediately
-> stop again after the next generated candidate
```

Generation is an expected stop point. The image tool naturally returns a visible candidate, and that pause gives Harley an insertion point to add visual direction before QA. Stopping after generation is not a process failure.

The next user prompt to continue after generation should resume at QA for the latest candidate. It should not restart planning, ask whether to QA, or skip QA.

Failed QA with a clear and well-defined repair target still continues into the next edit/regeneration without a separate confirmation. The next stopping point is after that next generated candidate appears.

A weak, non-compliant, unreviewed, or rejected image must not enter decks, asset packages, receipts, or canon surfaces as an accepted image.

## Working-loop state vs durable repo state

Candidate-level QA decisions inside a visual-preproduction loop are working loop state, not durable repo state.

Do not post per-candidate QA comments to GitHub during the loop. Keep failed-candidate QA, repair prompts, regenerated attempts, and provisional decisions inside the active loop.

Persist to GitHub only when one of these thresholds is reached:

- Harley has approved a QA-pass candidate or package;
- a hard blocker requires durable project tracking;
- Harley explicitly asks to preserve a planning decision;
- a final stage readiness report is complete.

Do not persist false-green risk by posting an issue comment before Harley approval.

## QA lanes

### patch_scene

Use for body-slide or scene art featuring Patch.

Accepted output: `accepted_scene_art`.

This lane is required before proof, full, final-candidate, or finished PPTX builds can use the image as body-slide art.

### patch_preproduction_reference

Use for asset sheets, interaction sheets, style sheets, character sheets, environment sheets, prop sheets, or location sheets where Patch appears.

Accepted output: `accepted_preproduction_reference`.

This lane makes the image usable as a reference for later generation. It does not make the image body-slide art.

For Patch-bearing asset sheets, apply the source-image and compiled-sheet checks from `playbooks/asset-sheet-production-contract.md` after Patch canon and non-Patch distinction checks.

### non_patch_preproduction_reference

Use for preproduction references where Patch does not appear.

Accepted output: `accepted_preproduction_reference`.

This lane still checks style, lane fit, function mapping, text discipline, physical logic, and canon confusion.

For non-Patch asset sheets, apply the same source-image, template compile, package sidecar, and character hero-shot checks when the sheet is a character sheet.

### asset_sheet_lane_compliance

Use when the image is intended as an asset sheet. Check whether it matches its declared lane:

- world or theme class sheet;
- environment class sheet;
- location sheet;
- cast or character class sheet;
- individual character sheet;
- prop class sheet;
- hero prop or continuity-object sheet;
- interaction or scale sheet;
- anti-pattern or style sheet.

Reject omnibus posters unless the requested lane explicitly calls for one.

For final compiled asset sheets, this lane must verify compliance with `playbooks/asset-sheet-production-contract.md`: approved blank template layout, compiled asset-sheet PNG, all used source images previously QA-accepted, sidecar/spec present, shadow placeholders covered where needed, guidance text contained in the right panel, alternate views in the bottom rail, unused alternate slots left empty rather than squeezed, and no durable inclusion of HTML/scratch/helper intermediates unless explicitly promoted.

For character asset sheets, the main/hero source image must be a full-body character shot on a plain white background. A compiled character sheet lacking that source image is not accepted.

### anti_pattern_reference

Use for images that intentionally show rejected examples.

Accepted output: `accepted_antipattern_reference`.

Non-canonical examples are allowed only when they are clearly marked as rejected anti-patterns and cannot be mistaken for canon.

### deck_package_image_review

Use for reviewing a full set of generated or embedded deck images against an accepted inventory, mode, and source issue.

This lane does not replace slide-level image QA. It verifies package-level consistency after per-image QA has already happened.

## Patch-bearing image rules

Any lane containing Patch must enforce current repo-indexed Patch canon.

Patch must remain the singular hero and visual anchor:

- clean editorial vector style;
- compact rounded proportions;
- teal hoodie with hood antennae;
- off-white face panel;
- black oval eyes with small white shine highlights only;
- dark pants;
- teal shoes with white soles;
- teal crossbody bag with visible `>` symbol;
- visible strap crossing the torso when the torso is visible;
- no generic robot Patch;
- no screen-face bot Patch;
- no human-boy Patch;
- no glossy mascot, plush, photoreal, anime, or chibi Patch;
- no Patch clones or Patch-shaped support teams.

Other agents, bots, humans, systems, specialists, gates, reviewers, and operators must be visually distinct from Patch. They must not borrow Patch's hoodie, antennae, bag, `>` symbol, off-white face panel, full silhouette, or teal identity as their main read.

## Patch-first world proof

For any new Patch-bearing theme or environment, visual preproduction must first prove that canonical Patch can inhabit the world.

The first generated asset should normally be a Patch-in-world interaction or scale proof sheet. It should show:

- canonical Patch in the proposed theme/world;
- Patch interacting with the core hook of the world;
- Patch interacting with one or two key roles, systems, gates, desks, or handoffs;
- Patch carrying or receiving the continuity object;
- non-Patch agents or people clearly distinct from Patch.

Do not continue to the broader asset package if this proof fails Patch canon, world fit, or interaction grammar.

## Preproduction asset readiness

Generated asset sheets are candidates, not accepted assets.

Preproduction assets count toward `asset_ready` only when:

- the correct lane has been selected;
- `adventures-image-qa` has accepted the generated source images in the correct lane;
- Patch-bearing candidates have passed Patch canon and non-Patch distinction checks;
- the source images are useful as future generation references;
- final asset sheets have been deterministically compiled into the approved template when a compiled sheet is being delivered;
- final compiled sheets pass lane/layout compliance and package-shape checks;
- the package includes the compiled PNG, every approved source image used, and a markdown or JSON sidecar/spec;
- character sheets include a full-body plain-white hero/main source image;
- the asset is recorded as provisional, accepted, or repo-tracked according to its evidence state;
- any required Harley approval threshold for the stage has been met.

Rejected, weak, unreviewed, generated-only asset sheets, one-shot generated full-sheet layouts, or template-noncompliant compiled sheets must not make an issue asset-ready.

## Body-slide image readiness

Body-slide scene images for proof, full, final-candidate, or finished packages must be accepted through the `patch_scene` lane when Patch appears or the relevant non-Patch scene lane when Patch does not appear.

PPTX build is not permitted for proof/full/final mode until the accepted generated scene-image inventory is complete for every body slide.

Preproduction references, asset sheets, source zips, contact sheets, anti-pattern sheets, interaction guides, old proof images, and thumbnails are not body-slide art unless Harley explicitly approves storyboard mode.

## Required QA output

Every image QA decision should record enough working-loop state for the caller to continue:

- image or candidate identifier;
- intended use;
- lane;
- source issue or package;
- reference assets considered;
- whether Patch appears;
- Patch preflight basis when Patch appears;
- decision: `accepted_scene_art`, `accepted_preproduction_reference`, `accepted_antipattern_reference`, `edit_required`, `regenerate_required`, or `blocked`;
- exact failures when not accepted;
- regeneration or edit instruction;
- whether the result may count toward `asset_ready`, scene inventory readiness, or neither.

For asset-sheet source-image QA, record whether the image is accepted as a source image/view only. For final compiled-sheet QA, record the compiled PNG path/name, source-image filenames, sidecar/spec status, template compliance, character hero-shot status when applicable, and skipped/omitted candidates if relevant.

During an active loop, this output is for the caller, not an automatic GitHub issue comment. If the repair target is clear and well defined, the caller may continue to one edit/regeneration, then stop after the next generated candidate.

## Repair-prompt hygiene

When returning `edit_required` or `regenerate_required`, provide repair guidance as prompt constraints, not prose to
paste into the next image prompt.

The caller should translate failures into:

- concise positive visual constraints;
- hard negatives only for the exact failure mode;
- preserve clauses for features that were correct;
- text-budget and operator-context quarantine reminders when relevant.

Do not encourage the caller to include QA reports, candidate numbers, pass/fail labels, issue comments, repo/process
notes, sidebars, or checklists in a generation prompt. If a generated image includes operator-context material, mark it
`edit_required` or `regenerate_required` and require removal.

For Patch drift, repair instructions should prefer whole-character constraints over isolated attribute lists. Avoid
terms that trigger bad generator priors for Patch, especially `robot`, `cute robot`, `mascot`, `toy`, or `bot`.

## Failure posture

Mark the image Red or blocked when:

- Patch is non-canonical;
- Patch is replaced by a human boy, generic robot, bot mascot, or other wrong identity;
- Patch is multiplied or support agents are Patch clones;
- the image uses the wrong lane and becomes an omnibus poster instead of the requested sheet;
- an asset sheet uses generated full-sheet layout as a substitute for the approved deterministic template/package path;
- a final compiled asset sheet uses unaccepted source images, lacks the compiled PNG/source images/sidecar package basis, or violates the approved template layout;
- a character sheet lacks a full-body plain-white hero/main source image;
- in-world text is misleading, overlong, or contaminates canon;
- the image accidentally canonises legacy or rejected material;
- the image is too cluttered or unclear to function as a reference or slide image;
- the image cannot be repaired without a new generation pass.

Do not mark Green because an image is attractive, polished, or plausible. Green requires lane fitness and downstream usefulness.

## Stop and continuation posture

Expected stop points:

- after each generated or edited candidate, so Harley can inspect the visible result;
- after a QA-pass candidate/package is ready for Harley approval;
- at a hard blocker;
- at a creative-choice fork.

After a user says to continue from a generated candidate:

- resume at QA for the latest candidate;
- do not restart planning;
- do not skip QA;
- do not ask whether QA is desired.

After a QA decision:

- `edit_required` with clear, well-defined repair: perform the edit/regeneration, then stop after the next generated candidate.
- `regenerate_required` with clear, well-defined repair: perform one regeneration, then stop after the next generated candidate.
- accepted candidate/package: stop for Harley approval when the owning stage requires it.
- `blocked`: stop and record the blocker when durable project tracking is required.
- creative-choice fork: stop and ask Harley to choose.

Continuing through multiple generated candidates without Harley's review insertion point is not the default. It requires explicit authorization for a fully autonomous run in that specific stage.
