# Visual bible interpretation playbook

This playbook defines how Adventures visual bibles are discovered and converted into image-generation, image-QA, and repair constraints.

Use this playbook whenever a visual-preproduction, image-preflight, or image-QA task involves a subject, style system, character, environment, prop, or asset class that has a repo-indexed visual bible or style guide.

## Core rule

Visual bibles are source doctrine. Skills must not reconstruct visual canon from memory.

A visual-bible interpretation step should discover the relevant bible through the repo index mesh, inspect matching project-source visuals when needed, and produce grounded prompt/QA blocks. It must not rely on hard-coded second-level paths, fixed source-zip names, versioned filenames, or bundled copies of visual canon.

## Discovery route

For every visual-bible interpretation task:

1. Start from the source issue, image task, candidate, or visual-preproduction lane.
2. Start repo discovery from stable first-level indexes, normally `assets/INDEX.md`.
3. Follow the asset index mesh to discover the relevant asset family and bible/style guide.
4. Follow the source-package index to discover current matching source/project-source packages when visual backing is needed.
5. Enumerate relevant package files from the package index, manifest, or directory listing.
6. Consider matching contact sheets, style guides, anti-pattern sheets, interaction sheets, and asset sheets.
7. Distinguish repo text evidence, visual evidence, inference, and uncertainty.

If the relevant bible cannot be located through the index mesh, block or mark reduced confidence according to the owning playbook. Do not substitute stale path memory.

## Interpretation packet

A visual-bible interpretation packet should include:

- source issue/task;
- lane or asset class;
- bible discovered through repo indexes;
- visual backing inspected, if any;
- evidence basis: repo text, visual package, inference, uncertainty;
- positive prompt block;
- negative prompt block;
- sensitive-detail micro-specs;
- QA hard gates;
- repair blocks relevant to the current failure;
- preserve clauses;
- extrapolation rules;
- prompt-safe next constraints;
- do-not-include block;
- status: green, amber text-only, blocked missing bible, or blocked missing visual evidence.

## Patch lane

Patch is the first implemented lane because Patch has a repo-indexed style bible.

For Patch-bearing generation or QA, use the current Patch style bible's extractable sections when present:

- prompt-positive canon block;
- prompt-negative canon block;
- sensitive-detail micro-specs;
- QA hard-gate checklist;
- feature-specific repair blocks;
- extrapolation rules.

When the Patch bible and visual source package disagree, report the discrepancy. Repo text remains canonical, but visual evidence should be used to catch ambiguity in wording and prevent overbroad repair rules.

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

## Extrapolation discipline

A bible-backed prompt may extrapolate only where the bible permits variation: pose, action, setting, small props, lighting, and composition.

Do not extrapolate identity-critical features unless the repo bible explicitly allows it. If a required scene would alter a canonical feature, stop and ask for a canon decision rather than silently inventing a variant.

## Skill composition

- Visual-bible interpretation extracts canon blocks and repair constraints.
- Image preflight turns those blocks into prompt contracts.
- Image QA uses those blocks as hard gates and repair sources.
- Visual preproduction orchestrates the loop and decides when bible interpretation is required.

No one skill should own both canon extraction and generated-image acceptance.