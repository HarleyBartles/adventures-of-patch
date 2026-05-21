# Visual bible interpretation playbook

This playbook defines how Adventures visual bibles are discovered and converted into image-generation, image-QA, and repair constraints.

Use this playbook whenever a visual-preproduction, image-preflight, or image-QA task involves a subject, style system, character, environment, prop, or asset class that has a repo-indexed visual bible or style guide. Also use it when creating a minimal provisional bible before generating a new reusable asset class.

## Core rule

Visual bibles are source doctrine. Skills must not reconstruct visual canon from memory.

A visual-bible interpretation step should discover the relevant bible through the repo index mesh, inspect a repo-indexed contact-sheet dispatch/intake package when pixels are needed, and produce grounded prompt/QA blocks. It must not rely on hard-coded second-level paths, fixed source-zip names, versioned filenames, bundled copies of visual canon, or obsolete inspection routes.

## Bible-first preproduction

A reusable visual asset class should have a bible before image generation begins, even if the bible is minimal and provisional.

A minimal provisional bible is enough when it defines:

- the asset class or subject;
- intended tone, function, and visual direction;
- positive prompt constraints;
- negative prompt constraints and anti-drift rules;
- text/signage posture;
- what belongs in the class;
- what does not belong in the class;
- immediate QA hard gates;
- known uncertainty.

The bible may be short at first. It should be updated during generation and QA when durable learning emerges. At the end of the asset-family pass, update and lock the bible based on accepted imagery. Locked bibles become the durable source for future prompt construction, image QA, repair packets, asset expansion, and deck-image planning.

Do not wait until after image generation to invent the bible from results. Generation should be guided by the bible; accepted results can then refine and validate it.

## Discovery route

For every visual-bible interpretation task:

1. Start from the source issue, image task, candidate, or visual-preproduction lane.
2. Start repo discovery from stable first-level indexes, normally `assets/INDEX.md`.
3. Follow the asset index mesh to discover the relevant asset family and bible/style guide.
4. Read or build the relevant contact-sheet dispatch/intake package from the repo index mesh when rendered pixels are needed.
5. Follow the source-package index only when package, transfer, or integrity fallback inspection is needed.
6. Enumerate relevant package files from the package index, manifest, or directory listing when using a fallback package.
7. Consider matching contact sheets, style guides, anti-pattern sheets, interaction sheets, and asset sheets.
8. Distinguish repo text evidence, visual evidence, inference, and uncertainty.

If the relevant mature bible cannot be located through the index mesh but the task is creating a new asset class, create a minimal provisional bible as a preproduction artifact instead of substituting stale path memory. If the task requires an existing canonical bible and it cannot be found, block or mark reduced confidence according to the owning playbook.

## Interpretation packet

A visual-bible interpretation packet should include:

- source issue/task;
- lane or asset class;
- bible discovered through repo indexes, or provisional bible created for this class;
- visual backing inspected, if any;
- evidence basis: repo text, visual package, accepted generated reference, inference, uncertainty;
- bible state: provisional, updated, or locked;
- positive prompt block;
- negative prompt block;
- sensitive-detail micro-specs;
- QA hard gates;
- repair blocks relevant to the current failure;
- preserve clauses;
- extrapolation rules;
- prompt-safe next constraints;
- do-not-include block;
- status: green, amber text-only, provisional, blocked missing bible, or blocked missing visual evidence.

## Patch lane

Patch is the first implemented mature lane because Patch has a repo-indexed style bible.

For Patch-bearing generation or QA, use the current Patch style bible's extractable sections when present:

- prompt-positive canon block;
- prompt-negative canon block;
- sensitive-detail micro-specs;
- QA hard-gate checklist;
- feature-specific repair blocks;
- extrapolation rules.

When the Patch bible and visual source package disagree, report the discrepancy. Repo text remains canonical, but visual evidence should be used to catch ambiguity in wording and prevent overbroad repair rules.

## Provisional asset-class bible lane

For a new environment, character class, prop class, costume/gear family, interaction motif, or world/theme class without a mature bible, create a minimal provisional bible before Pass A generation.

The provisional bible should be updated after accepted Pass A overview imagery and again after accepted Pass B member sheets. At the end of the family pass, lock the bible or explicitly leave it provisional with unresolved questions.

Accepted generated images can refine a provisional bible, but failed images should only become anti-pattern guidance when the failure is durable, repeated, or semantically important. Do not overfit the bible to one accidental generation error.

## Repair packet use

When image QA fails and a relevant bible exists, the next prompt or edit instruction should be built from a bible-backed repair packet, not freeform QA prose.

The repair packet should identify:

- exact failed hard gate;
- source canon block used;
- what passed and must be preserved;
- what failed and must change;
- positive repair constraints;
- exact negatives for this failure mode;
- whether edit or regeneration is viable;
- prompt hygiene reminders.

Do not paste QA prose, candidate numbers, pass/fail labels, issue comments, repo paths, process notes, sidebars, or checklists into an image prompt.

## Fresh-start discipline

Long image-edit chains are a workflow smell. Edits are appropriate for local, surgical defects in an otherwise correctly structured candidate. They are not appropriate when the candidate lineage repeatedly reinforces a wrong style, wrong lane, operator-context bleed, character contamination, or omnibus-poster behaviour.

Use a fresh generation from the current bible and accepted references when:

- the candidate fails lane or package structure;
- style direction has drifted;
- characters contaminate an environment-only or prop-only pass;
- operator/process/context material appears in the image;
- repeated repairs strengthen the same bad pattern;
- two repair passes fail with the same family of failure.

A fresh start should use the minimal/current bible and accepted references, not the contaminated image lineage.

## Extrapolation discipline

A bible-backed prompt may extrapolate only where the bible permits variation: pose, action, setting, small props, lighting, and composition.

Do not extrapolate identity-critical features unless the repo bible explicitly allows it. If a required scene would alter a canonical feature, stop and ask for a canon decision rather than silently inventing a variant.

## Skill composition

- Visual-bible interpretation extracts canon blocks and repair constraints.
- Image preflight turns those blocks into prompt contracts.
- Image QA uses those blocks as hard gates and repair sources.
- Visual preproduction orchestrates the loop and decides when bible interpretation is required.

No one skill should own both canon extraction and generated-image acceptance.
