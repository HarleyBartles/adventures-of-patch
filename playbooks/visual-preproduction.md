# Visual preproduction playbook

This playbook defines the pre-deck visual preproduction workflow for Adventures of Patch issues that are frame-ready but not asset-ready.

Visual preproduction creates or verifies reusable visual references before the end-to-end PPTX production playbook starts. It is the stage where the deck world, cast, locations, prop grammar, continuity objects, interaction patterns, and visual style become repeatable enough that later body-slide image generation does not need to invent the core asset language from scratch.

## Scope

Use this playbook after an issue is frame-ready and before `playbooks/end-to-end-pptx-production.md` when the issue is not yet asset-ready.

Use this playbook for Patch-in-world proofs, world or theme visual-language sheets, character class and individual character sheets, environment class and location sheets, prop class and hero prop sheets, interaction/handoff/scale/style sheets, anti-pattern sheets, and readiness reports.

This playbook may generate or edit preproduction reference images. It must not generate deck body-slide scene images. Body-slide image generation belongs inside the production playbook after deck planning and image planning.

Asset sheet deliverables produced through this playbook must also follow `playbooks/asset-sheet-production-contract.md`: generate and QA source images first, then deterministically compile the final asset sheet into the approved blank asset-sheet template, then package the compiled PNG, all approved source images, and the sidecar/spec together.

For character asset sheets, including Patch variants and non-Patch characters, the hero/main source image must be a full-body character shot on a plain white background before compilation. Alternate views may use close-ups, in-world shots, pose studies, detail shots, or other lane-appropriate support images after QA acceptance.

## Primary skill route

Use `adventures-visual-preproduction` as the primary orchestration skill for this playbook.

Compose with:

- `visual-intent-gate` after the lane and stage semantics are clear;
- `adventures-visual-bible-interpreter` when a mature visual bible exists or a provisional asset-class bible must be created;
- `adventures-patch-image-preflight` as the Patch identity and interaction subcheck when Patch appears;
- `adventures-image-qa` after Harley asks to continue from a generated or edited candidate;
- `adventures-asset-sheet-canoniser` after QA acceptance, when sheet-format, landing, or promotion guidance is needed.

`adventures-image-qa` is the single authoritative acceptance gate. Visual preproduction owns the stage, bible/preflight packet, prompt contract, and generation cadence. Image QA owns the decision.

For sheet-format, final-layout, package-shape, and repo/source-package landing questions, defer to `playbooks/asset-sheet-production-contract.md` as the canonical contract.

## Asset discovery

Before generating or editing preproduction images, inspect repo truth and discover relevant assets from stable index entry points.

For asset-sensitive work:

1. start at the first-level `assets` index;
2. follow the index mesh to identify relevant asset families;
3. identify matching source/import packages from the current source-package index when package or integrity fallback inspection is needed;
4. enumerate each relevant package from its own index, manifest, or directory listing;
5. inspect or consider every task-relevant style, contact, anti-pattern, interaction, guide, character, environment, prop, and continuity-object file;
6. record skipped files with reasons.

Do not hard-code second-level asset-family paths, legacy source-zip names, or a fixed count of visual sheets. Source packages are mirrors/source evidence, not independent canon; use the repo index first, then the Slides registry for visual inspection when pixels are needed, and use source packages only for package/integrity fallback when the Slides route is blocked.

## Mandatory style-system inspection

Style-system inspection is mandatory for visual preproduction that will generate or edit Adventures of Patch images, especially Patch-bearing work.

Locate the current style-system asset family through the asset index mesh and inspect the Slides registry for pixel-backed references when needed. Source package discovery remains for package/integrity fallback, not as the default visual truth. Do not encode or depend on a particular style zip filename. Whatever the current style-system package is called, it must be discovered, enumerated, and considered before generation is authorized when the fallback route is actually needed.

If the current style-system package cannot be located, enumerated, or inspected when required, stop with a blocker or mark reduced confidence according to the run mode. Do not proceed as though Patch-only references are sufficient.

## Visual bible and preflight packet

Every generated or edited visual-preproduction image must pass visual asset preflight before generation is authorized. This preflight is not Patch-specific. It applies to Patch images, non-Patch character sheets, environments, props, continuity objects, style references, and interaction sheets.

Visual asset preflight converts inspected assets and current visual bible guidance into prompt governance. It is not enough to say that assets were located or viewed. The assistant must extract and apply:

- positive rendering constraints from the approved style system, bibles, and task-relevant references;
- hard negative constraints from anti-pattern sheets, style guides, bibles, and prior failures;
- lane-specific composition constraints;
- prop, character, environment, and continuity-object constraints;
- physical-logic constraints for held, touched, stamped, carried, occluded, or transformed objects;
- text and label constraints;
- project-exposure constraints that keep repo/session machinery out of audience-facing visuals.

The preflight packet must include source issue and frame basis, selected lane, first-level asset index inspection, relevant asset/source packages, mandatory style-system package, task-specific packages, mature bible interpretation or minimal provisional bible, positive constraints, hard negatives, generated prompt contract, Patch sub-preflight when Patch appears, selected QA lane, and known risk notes.

For asset-sheet lanes, the preflight packet must also identify the intended source images/views, the deterministic compile target, the guidance/sidecar basis, and any character hero-shot requirement from `playbooks/asset-sheet-production-contract.md`.

If the packet is incomplete, block generation. If the packet is complete and Harley has not explicitly forbidden generation, generate one governed candidate and then stop at the natural generation boundary for Harley review.

## Prompt-governance discipline

Visual preproduction must reduce predictable generation failures before QA. Prompt contracts must use the hierarchy and quarantine rules from `adventures-image-preflight`.

For Patch-bearing prompts:

- start with Patch identity, not the scene;
- do not call Patch a robot, cute robot, mascot, toy, or bot;
- include the whole-character Patch lock: long-sleeved teal hoodie, hood framing off-white face panel, black oval eyes with tiny white shine highlights, dark trousers, teal shoes, distinct dark crossbody strap, dark/black bag flap with white `>` mark, and correct slim dark hood antennae with small dark round tips;
- state the selected lane and artifact type before adding decorative scene detail;
- keep text minimal and functional;
- quarantine operator context: do not render QA notes, issue comments, candidate numbers, repo/process references, sidebars, or checklists;
- translate failed QA into concise prompt constraints, not pasted QA prose.

If a prior candidate had correct Patch features, the next prompt must preserve those features while repairing the specific failure. Do not let one repaired feature regress another.

## Bible-first asset-class workflow

Any reusable asset class must be guided by a visual bible before image generation begins. The bible may be minimal and provisional at first, but it must be sufficient to steer the first generation and QA loop.

A minimal provisional bible should define asset class name and function, intended tone and visual direction, positive prompt constraints, negative prompt constraints and anti-drift rules, material/palette/prop/motif vocabulary, text/signage posture, what belongs in the class, what does not belong in the class, immediate QA hard gates, and known uncertainty.

The asset-class workflow is:

```text
minimal bible -> Pass A asset class overview -> update bible from accepted learning
-> Pass B asset family sheets -> update and lock bible
```

Do not wait until after image generation to invent the bible from results. Generation should be guided by the bible; accepted results can refine and validate it.

Update the provisional bible after accepted Pass A imagery and again after accepted Pass B member sheets. Failed imagery may add anti-pattern guidance only when the failure is durable, repeated, or semantically important. At the end of the asset family pass, lock the bible or explicitly leave it provisional with unresolved questions.

## Dual-pass asset-class workflow

Any reusable asset class must be produced through a required two-pass workflow. Do not ask image generation to create an asset class overview and all related member asset sheets in one instruction unless Harley explicitly overrides this rule for a narrow exception.

Asset sheet production inside either pass is governed by `playbooks/asset-sheet-production-contract.md`. Image generation creates focused source images or views only; it does not create the final sheet layout. The final sheet must be compiled deterministically into the approved template and delivered as a package containing the compiled asset-sheet PNG, every approved source image used in it, and a markdown or JSON sidecar/spec.

### Pass A: asset class overview

Create and QA one asset-class overview sheet first. The overview sheet defines the reusable class and establishes visual language, palette, materials, motifs, design boundaries, what belongs inside the family, what does not belong inside the family, the intended member assets or locations for Pass B, and enough reusable structure for member sheets to anchor to it.

Pass A must be accepted by `adventures-image-qa` and approved for the stage before Pass B begins. If Pass A fails, repair or regenerate Pass A rather than moving on to member sheets.

### Pass B: asset family expansion

Only after Pass A is accepted, generate the concrete member sheets for the family.

Each member sheet should stay anchored to the accepted Pass A overview and current bible, focus on one concrete member asset/location/character/prop/motif, avoid re-solving the whole class, be QA'd in the correct sheet lane, and be checked for family coherence against the accepted overview and current bible.

For environment classes, Pass A is the environment asset class overview and Pass B is the set of location sheets. For character classes, Pass A is the class/cast overview and Pass B is the individual character sheets. For prop classes, Pass A is the prop family overview and Pass B is the individual prop or continuity-object sheets.

This rule prevents the generator from collapsing class definition and family expansion into an omnibus poster with mixed lanes, characters, slogans, process panels, or unrelated notes.

## Patch-first proof

For any new Patch-bearing theme, world, or major environment, begin with a Patch-in-world interaction or scale proof.

The proof should show canonical Patch in the proposed world, Patch interacting with the core hook or workflow model, Patch receiving/carrying/updating/handing off the continuity object, clearly non-Patch people/agents/systems/gates, and enough environment/prop context to prove that the world can hold Patch without visual or semantic drift.

Do not begin with the final environment class sheet, character class sheet, prop sheet, or omnibus poster unless Harley explicitly asks for that lane. Do not continue into the broader asset package if the Patch-first proof fails Patch canon, world fit, non-Patch distinction, or interaction grammar.

## Patch sub-preflight

When Patch appears, compose with `adventures-patch-image-preflight` for Patch identity, singularity, non-Patch distinction, and Patch interaction grammar.

Patch sub-preflight does not replace the mandatory general visual asset preflight. It must not be used as a shortcut around style-system inspection, non-Patch asset inspection, environment/prop constraints, physical-logic checks, or prompt contract shaping.

## Semi-autonomous generation and QA cadence

Visual preproduction is a generation-bearing stage by default when Harley asks to run visual preproduction or image preflight for a frame-ready, asset-not-ready issue. It is not an analysis-only stage unless Harley explicitly says so.

The default cadence is semi-autonomous:

```text
plan candidate/package -> visual asset preflight -> generate or edit candidate -> stop for Harley review/nudge
-> on continue: run adventures-image-qa
-> if edit_required or regenerate_required and the repair packet target is known and well defined, edit/regenerate immediately
-> stop again after the next generated candidate
```

Generation is a natural and expected stop point. The image tool returns a visible candidate, and that pause gives Harley an insertion point to inspect the image and add visual direction before QA. Stopping after generation is not a process failure.

After Harley says to continue from a generated or edited candidate, resume at QA for the latest candidate. Do not restart planning, ask whether QA is desired, or skip QA.

Failed QA with a clear, well-defined repair target still proceeds directly into one edit/regeneration without a separate confirmation. The next stopping point is after that next generated candidate appears.

Continuing through multiple generated candidates without a Harley review insertion point is not the default. It requires explicit authorization for a fully autonomous run in that specific stage.

Only candidates accepted by `adventures-image-qa` in the correct lane may count toward asset-ready references after the stage approval rules are satisfied. Generated-only, unreviewed, weak, rejected, or reference-source-only images do not count.

## Fresh-start discipline

Long image-edit chains are a workflow smell. Edits are appropriate for local, surgical defects in an otherwise correct candidate. They are not appropriate when a candidate lineage repeatedly reinforces wrong lane, wrong style, character contamination, operator-context bleed, omnibus-poster behaviour, or another structural failure.

Use fresh generation from the current bible and accepted references when:

- the candidate fails lane or package structure;
- style direction has drifted;
- characters contaminate an environment-only or prop-only pass;
- operator/process/context material appears in the image;
- repeated repairs strengthen the same bad pattern;
- two repair passes fail with the same family of failure.

A fresh start should use the minimal/current bible and accepted references, not the contaminated image lineage.

## Repo-comment threshold

Do not post per-candidate QA comments to GitHub during an active visual-preproduction loop. Failed-candidate QA, repair prompts, regenerated attempts, and provisional acceptances are working loop state, not durable project state.

Persist to GitHub only when one of these thresholds is met:

- Harley has approved a QA-pass candidate or package;
- a hard blocker requires durable project tracking;
- Harley explicitly asks to preserve a planning decision;
- a final stage readiness report is complete.

Do not persist false-green risk by posting a repo comment before Harley approval. The issue should record durable outcomes, blockers, and approved state, not every candidate attempt.

## Lane selection

Select one primary lane before generating or editing.

Supported visual-preproduction lanes include Patch interaction or scale proof, world/theme class sheet, environment class sheet, location sheet, cast/character class sheet, individual character sheet, prop class sheet, hero prop or continuity-object sheet, interaction/handoff sheet, and style/anti-pattern sheet.

Reject or regenerate candidates that drift into omnibus posters, session-status artifacts, deck body-slide art, or multi-product asset bundles unless that lane was explicitly requested.

For asset-sheet lanes, use the approved template/package contract rather than generated full-sheet art as the default final-output path.

## Asset-ready standard

An issue is asset-ready only when the required visual references for its deck world have been created or verified and accepted in the correct QA lanes.

Asset-ready normally requires some subset of world/theme style or asset-class sheet, cast/character class sheet, individual recurring-character sheets, environment class sheet, location sheets, prop asset-class sheet, individual hero prop/continuity-object sheets, interaction/handoff/scale sheets, anti-pattern references, and readiness report.

For any item that introduces a reusable asset class, apply the bible-first dual-pass workflow before counting the family asset-ready: minimal/current bible, Pass A accepted overview, bible update, Pass B member sheets, family-coherence QA, and bible lock or explicit provisional status.

A compiled asset sheet counts only after the approved source images have passed image QA, the final sheet has been deterministically compiled into the approved template, the final sheet/lane compliance check has passed, and the required package sidecar/spec exists.

The exact subset depends on the issue. Do not force optional existing assets into a deck merely because they exist. Do require assets that the frame actually needs to make the story repeatable.

## Stop conditions

Stop or mark blocked when:

- frame-ready state is missing;
- required asset families cannot be discovered from indexes;
- mandatory style-system inspection cannot be completed;
- mandatory visual asset preflight cannot produce a prompt contract;
- required mature bible cannot be discovered or a minimal provisional bible cannot be created for a new asset class;
- Patch-bearing work cannot preserve canonical Patch;
- non-Patch characters or agents become Patch clones;
- the continuity object or key prop cannot be represented coherently;
- generated candidates fail QA and cannot be repaired without a new direction;
- image generation or image QA is unavailable;
- an asset-sheet package lacks the approved compiled template sheet, approved source images, required sidecar/spec, or character full-body plain-white hero source image when applicable;
- the task tries to generate deck body-slide art before the production playbook stage.

Expected pauses after generated candidates are not blockers and not process failures. They are the review insertion point in the default semi-autonomous cadence.

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
- Visual bible status:
- Patch-first proof status:
- Dual-pass asset-class status:
- Generation/review cadence status:
- Fresh-start / edit-chain status:
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

For asset-sheet package work, also record the `playbooks/asset-sheet-production-contract.md` compliance basis: approved source image filenames, compiled sheet PNG, sidecar/spec, skipped candidates if relevant, and character hero-shot confirmation when applicable.

## Boundaries

Do not generate body-slide art. Do not treat preproduction references as substitute slide art in proof/full/final runs unless Harley explicitly approves storyboard mode. Do not call a generated asset canonical because it was generated or QA-accepted; canonisation, repo landing, receipts, and promotion are downstream workflows.
