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

## Prompt-governance discipline

Visual preproduction must reduce predictable generation failures before QA. Prompt contracts must use the hierarchy
and quarantine rules from `adventures-image-preflight`.

For Patch-bearing prompts:

- start with Patch identity, not the scene;
- do not call Patch a robot, cute robot, mascot, toy, or bot;
- include the whole-character Patch lock: long-sleeved teal hoodie, hood framing off-white face panel, black oval eyes
  with tiny white shine highlights, dark trousers, teal shoes, distinct dark crossbody strap, dark/black bag flap with
  white `>` mark, and correct slim dark hood antennae with small dark round tips;
- state the selected lane and artifact type before adding decorative scene detail;
- keep text minimal and functional;
- quarantine operator context: do not render QA notes, issue comments, candidate numbers, repo/process references,
  sidebars, or checklists;
- translate failed QA into concise prompt constraints, not pasted QA prose.

If a prior candidate had correct Patch features, the next prompt must preserve those features while repairing the
specific failure. Do not let one repaired feature regress another.

## Dual-pass asset-class workflow

Any reusable asset class must be produced through a required two-pass workflow. Do not ask image generation to create
an asset class overview and all related member asset sheets in one instruction unless Harley explicitly overrides this
rule for a narrow exception.

### Pass A: asset class overview

Create and QA one asset-class overview sheet first.

The overview sheet defines the reusable class and establishes:

- visual language, palette, materials, motifs, and design boundaries;
- what belongs inside the asset family;
- what does not belong inside the asset family;
- the intended member assets or locations to be produced in Pass B;
- enough reusable structure that member sheets can anchor to it.

Pass A must be accepted by `adventures-image-qa` and approved for the stage before Pass B begins. If Pass A fails, repair
or regenerate Pass A rather than moving on to member sheets.

### Pass B: asset family expansion

Only after Pass A is accepted, generate the concrete member sheets for the family.

Each member sheet should:

- stay anchored to the accepted Pass A overview;
- focus on one concrete member asset, location, character, prop, or motif;
- avoid re-solving the whole class;
- be QA'd in the correct sheet lane;
- be checked for family coherence against the accepted overview.

For environment classes, Pass A is the environment asset class overview and Pass B is the set of location sheets. For
character classes, Pass A is the class/cast overview and Pass B is the individual character sheets. For prop classes,
Pass A is the prop family overview and Pass B is the individual prop or continuity-object sheets.

This rule prevents the generator from collapsing class definition and family expansion into an omnibus poster with
mixed lanes, characters, slogans, process panels, or unrelated notes.

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
plan candidate/package -> visual asset preflight -> generate or edit candidate -> run adventures-image-qa
-> if edit_required or regenerate_required and repair is clear, edit/regenerate immediately
-> repeat until QA-pass ready for Harley approval, hard blocker, or creative-choice fork
```

Use `playbooks/image-qa-contract.md` for canonical lane definitions and acceptance posture.

Only candidates accepted by `adventures-image-qa` in the correct lane may count toward asset-ready references after the
stage approval rules are satisfied. Generated-only, unreviewed, weak, rejected, or reference-source-only images do not
count.

## Non-terminal image generation and failed QA

Image generation, image editing, and ordinary failed QA are non-terminal substeps of this playbook.

When a candidate image is generated or edited, the assistant must not stop, summarize, or wait for Harley as though the
run is complete. The generated image is a candidate only. The next required action is to resume the playbook loop and
run `adventures-image-qa` in the selected lane.

If QA returns `edit_required` or `regenerate_required` and the repair is clear, the assistant must continue directly to
edit/regeneration and then QA again. Harley should not have to prompt `continue`, `proceed`, or `continue to QA` for
ordinary repair loops.

If the platform image-generation tool returns control in a way that prevents the assistant from continuing in the same
visible response, the assistant's next message must resume at QA. Do not treat the image tool boundary as a
user-confirmation gate. If that QA fails with a clear repair, continue the loop rather than pausing for confirmation.

Required continuation state after every generation, edit, or failed QA:

- source issue;
- selected lane;
- candidate image identifier or path if available;
- preflight and source-discovery basis;
- intended use;
- QA skill to invoke;
- known risk notes from the generation brief;
- repair instruction when QA failed.

The visual-preproduction run is not complete until it reaches one of these states:

- QA-pass candidate or package ready for Harley approval;
- hard blocker;
- creative-choice fork requiring Harley.

Generate is not a handoff. Generate is a candidate-producing substep. QA is not a repo-persistence trigger. Harley
approval or blocker state is the handoff.

## Repo-comment threshold

Do not post per-candidate QA comments to GitHub during an active autonomous visual-preproduction loop. Failed-candidate
QA, repair prompts, regenerated attempts, and provisional acceptances are working loop state, not durable project
state.

Persist to GitHub only when one of these thresholds is met:

- Harley has approved a QA-pass candidate or package;
- a hard blocker requires durable project tracking;
- Harley explicitly asks to preserve a planning decision;
- a final stage readiness report is complete.

Do not persist false-green risk by posting a repo comment before Harley approval. The issue should record durable
outcomes, blockers, and approved state, not every candidate attempt.

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

For any item that introduces a reusable asset class, apply the dual-pass workflow before counting the family asset-ready:
Pass A accepted overview first, then Pass B member sheets and family-coherence QA.

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

Stopping after generation, edit, or ordinary failed QA with a clear repair is a playbook violation, not a valid stop
condition.

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
- Dual-pass asset-class status:
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