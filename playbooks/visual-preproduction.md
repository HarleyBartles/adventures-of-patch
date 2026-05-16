# Visual preproduction playbook

This playbook defines the pre-deck visual preproduction workflow for Adventures of Patch issues that are frame-ready
but not asset-ready.

Visual preproduction creates or verifies reusable visual references before the end-to-end PPTX production playbook
starts. It is the stage where the deck world, cast, locations, prop grammar, continuity objects, interaction patterns,
and visual style become repeatable enough that later body-slide image generation does not need to invent the core
asset language from scratch.

## Scope

Use this playbook after an issue is frame-ready and before `playbooks/end-to-end-pptx-production.md` when the issue is
not yet asset-ready.

Use this playbook for:

- Patch-in-world interaction or scale proofs;
- world or theme visual-language sheets;
- character class sheets and individual character sheets;
- environment class sheets and location sheets;
- prop class sheets and hero prop or continuity-object sheets;
- interaction, handoff, scale, style, or anti-pattern sheets;
- readiness reports that decide whether an issue has become asset-ready.

This playbook may generate or edit preproduction reference images. It must not generate deck body-slide scene images.
Body-slide image generation belongs inside the production playbook after deck planning and image planning.

## Primary skill route

Use `adventures-visual-preproduction` as the primary orchestration skill for this playbook.

Compose with:

- `visual-intent-gate` only after the visual-preproduction lane and stage semantics are clear;
- `adventures-patch-image-preflight` as the Patch identity and interaction subcheck when Patch appears;
- `adventures-image-qa` after every generated or edited candidate;
- `adventures-asset-sheet-canoniser` only after QA acceptance, when sheet-format, landing, or promotion guidance is
  needed.

`adventures-image-qa` is the single authoritative acceptance gate. Visual preproduction owns the pre-generation
asset preflight and generation loop; `adventures-image-qa` owns the decision.

## Asset discovery

Before generating or editing preproduction images, inspect repo truth and discover relevant assets from stable index
entry points.

For asset-sensitive work:

1. start at the first-level `assets` index;
2. follow the index mesh to identify relevant asset families;
3. identify matching source/import packages from the current source-package index when visual package inspection is
   needed;
4. enumerate each relevant package from its own index, manifest, or directory listing;
5. inspect or consider every task-relevant style, contact, anti-pattern, interaction, guide, character, environment,
   prop, and continuity-object file;
6. record skipped files with reasons.

Do not hard-code second-level asset-family paths, legacy source-zip names, or a fixed count of visual sheets. Source
packages are mirrors/source evidence, not independent canon; use the repo index first, then the matching package for
visual inspection when needed.

## Mandatory style-system inspection

Style-system inspection is mandatory for visual preproduction that will generate or edit Adventures of Patch images,
especially Patch-bearing work.

Locate the current style-system asset family and matching source package through the asset/source-package index mesh.
Do not encode or depend on a particular style zip filename. Whatever the current style-system package is called, it
must be discovered, enumerated, and considered before generation is authorized.

If the current style-system package cannot be located, enumerated, or inspected when required, stop with a blocker or
mark reduced confidence according to the run mode. Do not proceed as though Patch-only references are sufficient.

## Mandatory visual asset preflight

Every generated or edited visual-preproduction image must pass visual asset preflight before generation is authorized.
This preflight is not Patch-specific. It applies to Patch images, non-Patch character sheets, environments, props,
continuity objects, style references, and interaction sheets.

Visual asset preflight converts inspected assets into prompt governance. It is not enough to say that assets were
located or viewed. The assistant must extract and apply:

- positive rendering constraints from the approved style-system and task-relevant references;
- hard negative constraints from anti-pattern sheets, style guides, and prior failures;
- lane-specific composition constraints;
- prop, character, environment, and continuity-object constraints;
- physical-logic constraints for held, touched, stamped, carried, occluded, or transformed objects;
- text and label constraints;
- project-exposure constraints that keep repo/session machinery out of audience-facing visuals.

The preflight packet must include:

- source issue and frame basis;
- selected visual-preproduction lane;
- first-level asset index inspection;
- relevant asset families and source packages discovered through the index mesh;
- mandatory style-system package discovered, enumerated, and considered;
- task-specific packages discovered, enumerated, and considered;
- positive visual constraints extracted;
- hard negative visual constraints extracted;
- generated prompt contract shaped from those constraints;
- Patch sub-preflight result when Patch appears;
- selected `adventures-image-qa` lane;
- known risk notes to carry into QA.

If the packet is incomplete, block generation. If the packet is complete and Harley has not explicitly forbidden
generation, generate one governed candidate and continue to QA.

## Patch-first proof

For any new Patch-bearing theme, world, or major environment, begin with a Patch-in-world interaction or scale proof.

The proof should show:

- canonical Patch in the proposed world;
- Patch interacting with the core hook or workflow model;
- Patch receiving, carrying, updating, or handing off the continuity object;
- one or more clearly non-Patch people, agents, systems, desks, gates, or handoff points;
- enough environment and prop context to prove that the world can hold Patch without visual or semantic drift.

Do not begin with the final environment class sheet, character class sheet, prop sheet, or omnibus poster unless Harley
explicitly asks for that lane. Do not continue into the broader asset package if the Patch-first proof fails Patch
canon, world fit, non-Patch distinction, or interaction grammar.

## Patch sub-preflight

When Patch appears, compose with `adventures-patch-image-preflight` for Patch identity, singularity, non-Patch
distinction, and Patch interaction grammar.

Patch sub-preflight does not replace the mandatory visual asset preflight. It must not be used as a shortcut around
style-system inspection, non-Patch asset inspection, environment/prop constraints, physical-logic checks, or prompt
contract shaping.

## Image generation and QA loop

Visual preproduction is a generation-bearing stage by default when Harley asks to run visual preproduction or image
preflight for a frame-ready, asset-not-ready issue. It is not an analysis-only stage unless Harley explicitly says so.

The required loop is:

```text
plan candidate -> visual asset preflight -> generate or edit candidate -> run adventures-image-qa -> accept / edit_required / regenerate_required / blocked -> repeat until accepted or blocked
```

Use `playbooks/image-qa-contract.md` for canonical lane definitions and acceptance posture.

Only candidates accepted by `adventures-image-qa` in the correct lane may count toward asset-ready references.
Generated-only, unreviewed, weak, rejected, or reference-source-only images do not count.

## Non-terminal image generation

Image generation and image editing are non-terminal substeps of this playbook.

When a candidate image is generated or edited, the assistant must not stop, summarize, or wait for Harley as though the
run is complete. The generated image is a candidate only. The next required action is to resume the playbook loop and
run `adventures-image-qa` in the selected lane.

If the platform image-generation tool returns control in a way that prevents the assistant from continuing in the same
visible response, the assistant's next message must resume at QA. Do not treat the image tool boundary as a
user-confirmation gate.

Required continuation state after every generation or edit:

- source issue;
- selected lane;
- candidate image identifier or path if available;
- preflight and source-discovery basis;
- intended use;
- QA skill to invoke;
- known risk notes from the generation brief.

The visual-preproduction run is not complete until the candidate has a QA decision:
`accepted_preproduction_reference`, `edit_required`, `regenerate_required`, or `blocked`.

Generate is not a handoff. Generate is a candidate-producing substep. QA is the handoff.

## Lane selection

Select one primary lane before generating or editing.

Supported visual-preproduction lanes include:

- Patch interaction or scale proof;
- world or theme class sheet;
- environment class sheet;
- location sheet;
- cast or character class sheet;
- individual character sheet;
- prop class sheet;
- hero prop or continuity-object sheet;
- interaction or handoff sheet;
- style or anti-pattern sheet.

Reject or regenerate candidates that drift into omnibus posters, session-status artifacts, deck body-slide art, or
multi-product asset bundles unless that lane was explicitly requested.

## Asset-ready standard

An issue is asset-ready only when the required visual references for its deck world have been created or verified and
accepted in the correct QA lanes.

Asset-ready normally requires some subset of:

- world/theme style or asset-class sheet;
- cast/character class sheet where useful;
- individual sheets for recurring major characters;
- environment class sheet where useful;
- location sheets for recurring major places or command domains;
- prop asset-class sheet tied to the world/theme;
- individual hero prop or continuity-object sheet where needed;
- interaction, handoff, or scale sheet when recurring relationships matter;
- style or anti-pattern references where drift risk is high;
- readiness report identifying provisional, accepted, and repo-tracked status.

The exact subset depends on the issue. Do not force optional existing assets into a deck merely because they exist.
Do require assets that the frame actually needs to make the story repeatable.

## Stop conditions

Stop or mark blocked when:

- frame-ready state is missing;
- required asset families cannot be discovered from indexes;
- mandatory style-system inspection cannot be completed;
- mandatory visual asset preflight cannot produce a prompt contract;
- Patch-bearing work cannot preserve canonical Patch;
- non-Patch characters or agents become Patch clones;
- the continuity object or key prop cannot be represented coherently;
- generated candidates fail QA and cannot be repaired without a new direction;
- image generation or image QA is unavailable;
- the task tries to generate deck body-slide art before the production playbook stage.

Stopping after generation or edit without a QA decision is a playbook violation, not a valid stop condition.

## Output contract

Use this report shape when returning visual-preproduction status:

```markdown
## Visual preproduction report

- Issue:
- Frame-ready source:
- Selected lane:
- Asset discovery:
- Mandatory style-system inspection:
- Visual asset preflight:
- Patch-first proof status:
- Existing reusable assets:
- Generated or edited candidates:
- Image QA decisions:
- Accepted preproduction references:
- Remaining required assets:
- Provisional vs repo-tracked status:
- Asset-ready: yes/no
- Playbook-ready: yes/no
- Blockers:
- Required next action:
```

## Boundaries

Do not generate body-slide art. Do not treat preproduction references as substitute slide art in proof/full/final runs
unless Harley explicitly approves storyboard mode. Do not call a generated asset canonical because it was generated or
QA-accepted; canonisation, repo landing, receipts, and promotion are downstream workflows.