# Adventures of Patch project index

This index is the first-class navigation surface for repo-grounded project work.

## Canonical repository

- Repo: `HarleyBartles/adventures-of-patch`
- Default branch: `main`
- Purpose: canonical project state for Presentation Planner / Adventures of Patch decks, issues, assets, receipts, skills, and workflow notes.

Use the live GitHub API connector for known paths and issue operations when available. Do not rely on uploaded project-source zips as active truth unless the repo points to them or the user explicitly scopes work to them.

## Required first reads

For a fresh agent session or repo-sensitive task:

1. `INDEX.md`
2. `AGENTS.md`
3. `README.md`
4. This index
5. The named issue, deck, receipt, or asset guide relevant to the task
6. For issue-to-PPTX production, `docs/project/playbooks/end-to-end-pptx-production.md`

## Current repo layout

- `README.md` - project orientation.
- `AGENTS.md` - agent navigation, source discipline, and production gates.
- `INDEX.md` - root directory index and top-level navigation surface.
- `docs/adventures/future-patch-adventures.md` - seed list of future Patch adventure concepts.
- `docs/project/` - project indexes, workflow notes, doctrine summaries, playbooks, and bootstrap/navigation material.
- `docs/project/playbooks/end-to-end-pptx-production.md` - canonical orchestration playbook for issue-to-finished-presentation-package work.
- `assets/patch/` - canonical Patch visual guidance and asset surfaces.
- `assets/source-zips/` - committed source packages or legacy/import bundles. These are not automatically active canon unless indexed or documented.
- `assets/receipts/` - committed receipt packages and evidence bundles.
- `decks/` - deck artifacts or deck working folders when committed.
- `skills/` - packaged or source copies of project-specific skills when intentionally committed.
- `scratch/` - local working area; not canonical.

## Directory index mesh

Every visible directory should contain an `INDEX.md` file listing direct files and pointing to child directory indexes. Agents should navigate through this mesh before relying on broad search results.

## Adventure issues

Adventure-plan issues are durable presentation seeds. Use issue ingestion before deck planning.

Smallest proof target selected for pipeline testing:

- Issue #3: `Adventure plan: Patch at the Checkpoint of Intent`

Known proof-run result:

- The first proof pass should be treated as failed/red because it skipped mandatory image generation and produced non-canonical Patch imagery. Future passes must stop at blocked image generation or missing Patch references rather than silently downgrading to storyboard/fallback output.

## Patch visual canon

Patch is the constant protagonist unless explicitly excluded.

Current canonical Patch references in repo:

- `assets/patch/patch_style_guide_v1.2.md` - current Patch visual design guide, including style, palette, hoodie, antennae, bag, strap, expression, pose, and prompt guidance.
- `assets/patch/patch_contact_sheet_v1.1.png` - Patch contact sheet.
- `assets/patch/patch_anti_patterns_v1.1.png` - Patch anti-pattern sheet.
- `assets/patch/patch_interaction_guide_v1.1.png` - Patch interaction guide.

Patch generation must preserve the style guide requirements: clean editorial vector style, thick rounded outlines, soft shading, teal hoodie, two hoodie antennae, compact rounded proportions, dark pants, teal shoes with white soles, and teal crossbody bag with visible `>` symbol and consistent strap placement.

Do not drift into generic robot, glossy 3D mascot, plush realism, photorealism, or unrelated asset-family styles.

## Presentation production pipeline

For end-to-end deck work from an issue, read and follow:

- `docs/project/playbooks/end-to-end-pptx-production.md`

The short version:

1. Ingest the issue into a production brief.
2. Apply deck doctrine.
3. Create a deck plan.
4. Create an image plan and prompt pack.
5. Run visual-intent gate and Patch image preflight.
6. Inspect repo-tracked Patch references.
7. Generate images, or stop and report a blocker.
8. Build the PPTX only after required image status is explicit.
9. Create presenter sidecar, preferably PDF.
10. Run presentation QA.
11. Create presentation image receipt and asset-canonisation follow-ups where needed.

Do not skip required gates. Do not call a package finished without notes, sidecar, QA, and receipt/canonisation status.

## Finished deck contract summary

A finished Adventures of Patch presentation package should include:

- PPTX deck;
- plain text-only title slide with month date;
- visual-first Patch-led body slides;
- sparse visible slide text, with concept-bearing text preferably in-world;
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
