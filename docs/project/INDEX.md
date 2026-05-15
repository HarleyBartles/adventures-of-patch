# Adventures of Patch project index

This index is the first-class navigation surface for repo-grounded project work inside `docs/project/`.

## Canonical repository

- Repo: `HarleyBartles/adventures-of-patch`
- Default branch: `main`
- Purpose: canonical project state for Presentation Planner / Adventures of Patch decks, issues, assets, receipts, skills, actor governance, and workflow notes.

Use the live GitHub API connector for known paths and issue operations when available. Do not rely on uploaded project-source zips as active truth unless the repo points to them or the user explicitly scopes work to them.

## Files in this directory

- `INDEX.md` - this file; first-class project index and current source map for agents.

## Subdirectories

- `playbooks/` - operational playbooks for composing project skills into complete jobs. See `playbooks/INDEX.md`.

## Required first reads

For a fresh agent session or repo-sensitive task:

1. `INDEX.md` at the repository root.
2. `AGENTS.md`.
3. `README.md`.
4. `docs/project/INDEX.md`.
5. The named issue, deck, receipt, or asset guide relevant to the task.
6. For Patch actor-governed work, `Patch/README.md`, `Patch/GOVERNANCE.md`, and `Patch/ROUTING.md`.
7. For issue-to-PPTX production, `docs/project/playbooks/end-to-end-pptx-production.md`.

## Current repo layout

- `README.md` - project orientation.
- `AGENTS.md` - agent navigation, source discipline, Patch actor routing, visual Patch rules, and production gates.
- `INDEX.md` - root directory index and top-level navigation surface.
- `Patch/` - Patch project-local actor surface, with project-director and execution lanes.
- `docs/adventures/future-patch-adventures.md` - seed list of future Patch adventure concepts.
- `docs/project/` - project indexes, workflow notes, doctrine summaries, playbooks, and bootstrap/navigation material.
- `docs/project/playbooks/end-to-end-pptx-production.md` - canonical orchestration playbook for issue-to-finished-presentation-package work.
- `assets/patch/` - canonical Patch visual guidance and asset surfaces.
- `assets/source-zips/` - committed source packages or legacy/import bundles. These are not automatically active canon unless indexed or documented.
- `assets/receipts/` - committed receipt packages and evidence bundles.
- `decks/` - deck artifacts or deck working folders when committed.
- `skills/` - packaged or source copies of project-specific skills when intentionally committed.
- `scratch/` - local working area; not canonical.

## Patch actor surface

Patch is the sole project-local agent for Adventures of Patch.

Current local lanes:

- `Patch / project-director` - planning, issue shaping, source discipline, gate checks, routing decisions, verification, and repo-state judgement.
- `Patch / execution` - repo-local file mutation, binary asset landing, source zip creation, index updates, issue updates, commit/push, and return evidence.

The default workspace route is `Will -> Patch`.

No separate Adventures asset, deck, image, canon, receipt, or publication executors exist unless a future issue creates one for a real boundary.

## Directory index mesh

Every visible directory should contain an `INDEX.md` file listing direct files and pointing to child directory indexes. Agents should navigate through this mesh before relying on broad search results.

## Adventure issues

Adventure-plan issues are durable presentation seeds. Use issue ingestion before deck planning.

Smallest proof target selected for pipeline testing:

- Issue #3: `Adventure plan: Patch at the Checkpoint of Intent`

Patch actor instantiation and binary asset landing route:

- Issue #20: `Planning: instantiate Patch as Adventures repo-local agent and binary asset landing worker`

Known proof-run result:

- The first proof pass should be treated as failed/red because it skipped mandatory image generation and produced non-canonical Patch imagery. Future passes must stop at blocked image generation or missing Patch references rather than silently downgrading to storyboard/fallback output.

## Patch visual canon

Patch is the constant protagonist unless explicitly excluded.

Current canonical Patch references in repo:

- `assets/patch/patch_style_guide_v1.3.md` - current Patch visual design guide, including style, palette, hoodie, antennae, bag, strap, eye canon, expression, pose, and prompt guidance. v1.3 hardens Patch eye canon: black oval eyes with small white shine highlights only.
- `assets/patch/patch_contact_sheet_v1.1.png` - Patch contact sheet.
- `assets/patch/patch_anti_patterns_v1.1.png` - Patch anti-pattern sheet.
- `assets/patch/patch_interaction_guide_v1.1.png` - Patch interaction guide.

Patch generation must preserve the style guide requirements: clean editorial vector style, thick rounded outlines, soft shading, teal hoodie, two hoodie antennae, compact rounded proportions, black oval eyes with small white shine highlights only, dark pants, teal shoes with white soles, and teal crossbody bag with visible `>` symbol and consistent strap placement.

Do not drift into generic robot, glossy 3D mascot, plush realism, photorealism, unrelated asset-family styles, or alternate eye styles such as white sclera, irises, anime eyes, human eyes, doll eyes, or large expressive mascot eyes.

## Presentation production pipeline

For end-to-end deck work from an issue, read and follow:

- `docs/project/playbooks/end-to-end-pptx-production.md`

The short version:

1. Ingest the issue into a production brief.
2. Establish a strong frame/analogy/world with `frame-buster` when one is missing or weak.
3. Apply deck doctrine.
4. Create a deck plan.
5. Create an image plan and prompt pack.
6. Run visual-intent gate and Patch image preflight.
7. Inspect repo-tracked Patch references and available project-source Patch assets.
8. Generate images, or stop and report a blocker.
9. Build the PPTX only after required image status is explicit.
10. Create presenter sidecar, preferably PDF.
11. Run presentation QA.
12. Create presentation image receipt and asset-canonisation follow-ups where needed.

Do not skip required gates. Do not call a package finished without notes, sidecar, QA, and receipt/canonisation status.

## Finished deck contract summary

A finished Adventures of Patch presentation package should include:

- PPTX deck;
- plain text-only title slide with month date;
- a strong frame/analogy/world that makes the lesson physically happen through Patch's adventure;
- visual-first Patch-led body slides, preferably full-slide or near-full-slide images;
- sparse visible slide text, with short concept-bearing text preferably embedded in-world inside images where it helps the scene carry meaning;
- speaker notes on every substantive body slide;
- plain text-only end card focused on takeaways and applying the learning today;
- presenter sidecar document, preferably PDF;
- receipt/evidence package for generated or embedded images;
- follow-up canonisation issues for accepted reusable assets.

## Repo hygiene gaps to resolve

- Update stale docs or skills that still refer to uploaded project sources as canonical.
- Add labels for local issue taxonomy if desired.
- Add deck/asset/receipt folders as concrete artifacts are committed.

## Agent warning

If you cannot inspect the repo source needed for a claim or generation task, say so. Do not invent repo contents. Do not treat a polished artifact as green if a mandatory production phase failed.
