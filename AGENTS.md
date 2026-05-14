# Agent navigation for Adventures of Patch

This repository is the canonical source of truth for the Presentation Planner / Adventures of Patch project.

## First read for agents

When beginning project work from this repo, read these in order:

1. `README.md` - short project orientation and repo layout.
2. `docs/project/index.md` - first-class repo index and current source map.
3. The relevant GitHub issue, if the user named one.
4. Any repo-tracked asset guides, receipts, deck plans, or source files linked from the index or issue.

Use the live GitHub API connector for known repo paths, issues, and writes when available. Treat code-search/index access as useful but potentially lagging.

## Source-of-truth rules

The repo is canonical. Do not treat uploaded project-source zips, chat attachments, or local scratch files as active project truth unless the repo points to them or the user explicitly scopes the task to that artifact.

Repo files, repo issues, repo-tracked receipts, and repo-tracked asset documentation are authoritative project state.

If a required guide or asset is missing from the repo, report it as a blocker or repo hygiene gap. Do not silently substitute memory or uploaded zips.

## Patch rules

Patch is the constant protagonist for Adventures of Patch presentations unless Harley explicitly excludes him.

Before planning or generating images featuring Patch, inspect the current repo-tracked Patch visual references. Expected canonical surfaces include:

- Patch style guide;
- Patch contact sheet;
- Patch anti-pattern sheet;
- Patch interaction guide.

If these are not present or discoverable in the repo, do not claim that Patch visual generation is ready. Open or recommend a repo hygiene / asset canonisation issue to land them.

Patch image generation must preserve the canonical Patch style. Do not drift into generic robot, glossy 3D mascot, plush realism, or unrelated asset-family styles.

## Presentation production pipeline

For an adventure-plan issue intended to become a finished presentation package, use the project skill chain:

1. issue ingestion;
2. deck doctrine;
3. deck planning;
4. image planning;
5. visual intent and Patch preflight;
6. image generation or explicit blocked status;
7. PPTX build;
8. presenter sidecar;
9. presentation QA;
10. receipt and asset-canonisation follow-up.

Do not skip a required production gate. If image generation, Patch references, sidecar creation, or QA cannot be completed, stop and report the blocker rather than downgrading the package silently.

## Finished deck expectations

A finished deck package includes:

- a PPTX;
- plain text-only title page with month date;
- visual-first Patch-led body slides;
- speaker notes sufficient for another presenter;
- plain text-only end card focused on takeaways and applying the learning today;
- presenter sidecar, preferably PDF;
- image receipt and canonisation follow-up when generated images or reusable assets are involved.

## Issue discipline

Use GitHub issues as durable work packets. Do not close or mark work complete without evidence. Comment with red/amber/green status when a proof run or production pass exposes failures.
