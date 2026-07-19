# Agent navigation for Adventures of Patch

This repository is the canonical source of truth for the Presentation Planner / Adventures of Patch project.

## First read for agents

When beginning project work from this repo, read these in order:

1. `INDEX.md` - root directory index and top-level navigation surface.
2. `README.md` - short project orientation.
3. `docs/project/INDEX.md` - first-class project index and current source map.
4. The relevant GitHub issue, if the user named one.
5. Any repo-tracked asset guides, receipts, deck plans, or source files linked from the index mesh, project index, or issue.

For agent-workspace policy, skill authoring, or mesh work, also read:

- `.agents/AGENTS.md`
- `.agents/doctrine/adventures-project-doctrine.md` for Adventures identity,
  source truth, readiness, and publication invariants;
- `.agents/doctrine/mesh-policy.md`
- `.agents/doctrine/skill-authoring-policy.md`

For Adventures readiness or visual work, also read:

- `.agents/guides/design-guide.md` or `.agents/guides/planning-guide.md`;
- `playbooks/pre-playbook-adventure-readiness.md`;
- `playbooks/visual-preproduction.md`;
- `playbooks/image-qa-contract.md` when an image candidate is involved.

For tracked repo mutation or source-package work, read:

- `.agents/guides/implementing-guide.md`;
- `repo-worker-base` and the matching publication/review guidance.

For issue-to-PPTX production, also read:

- `playbooks/end-to-end-pptx-production.md`

When navigating into a directory, also read that directory's `INDEX.md` and `AGENTS.md` if present before relying on broad search or assumptions.

Use any live GitHub-capable route that can fetch canonical material from this repo. Prefer the live GitHub API connector for known repo paths, issues, and writes when available, but do not treat it as the only possible proof of access. Treat code-search/index access as useful but potentially lagging.

## Patch character surface

Patch is the constant project character and visual canon. Patch has no agent
identity, actor lane, execution authority, or repository ownership role.

Patch visual canon remains under `assets/canon/patch/` and its explicit
`reference_sheets/` subdirectory. Repo-canonical image inspection uses the
current indexed visual-inspection route; source zips stay in the
package/import/integrity lane.

## Source-of-truth rules

The repo is canonical. Do not treat uploaded project-source zips, chat attachments, or local scratch files as active project truth unless the repo points to them or the user explicitly scopes the task to that artifact.

For marketplace skill refreshes, use `.agents/plugins/marketplace.json` and the pinned `.agents/plugins/marketplace-source` gitlink. The retired `adventures-pack` must not be reintroduced. Marketplace-derived skills are projections; repo-local `adventures-*` skills are local custody and must be preserved by refresh tooling.

Repo files, repo issues, repo-tracked receipts, and repo-tracked asset documentation are authoritative project state.

If a required guide or asset is missing from the repo, report it as a blocker or repo hygiene gap. Do not silently substitute memory or uploaded zips.

## Bound connector action gate

When a turn, skill step, or playbook stage clearly becomes an external connector action, refresh the named connector namespace at that boundary before selecting actions or reporting action availability. Use `playbooks/bound-connector-action-gate.md` for the full gate. Do not treat earlier sparse connector listings as final evidence.

## Issue-to-PPTX repo gate

For issue-to-PPTX, proof-pass, production-pass, or finished-package work, prove repo access and fetch the named source issue before producing any deck artifact.

Repo access is a state established by evidence, not by one preferred tool route. If an assistant has already retrieved a file, issue, comment, PR, commit, or repository metadata from `HarleyBartles/adventures-of-patch` in the current run, repo access for that route is proven and must be carried forward. A later failure in a different GitHub search/index/tool route must not erase that proof.

A search or index miss is not proof that repo access is unavailable. Check all currently available GitHub-capable routes and prefer direct known-path or known-issue reads over broad search. If any direct repo read succeeds for `HarleyBartles/adventures-of-patch`, do not claim repo access is unavailable.

If the source issue or required repo playbook surfaces cannot be fetched through any available GitHub-capable route, valid outputs are limited to a blocked status, a tooling/access diagnostic, or a user-approved plan-only fallback. Do not create a PPTX, storyboard, draft, or proof artifact from uploaded zips, receipt packages, old deck assets, memory, or inferred structure.

Any artifact produced after a skipped repo gate is not valid for issue progress, QA, receipt, asset canonisation, or closure.

## Directory index mesh

Every in-scope directory should contain a generated `INDEX.md` file listing
direct files and pointing to child directory indexes. Skill roots and gitlink
boundaries are intentional leaves: link to their entrypoint or repository
boundary without descending or creating nested indexes. Navigate through that
mesh before relying on broad search.

## Patch rules

Patch is the constant protagonist for Adventures of Patch presentations unless Harley explicitly excludes him.

Before planning or generating images featuring Patch, inspect `assets/canon/patch/INDEX.md` and the current repo-tracked Patch visual references:

- `assets/canon/patch/asset__hero__patch_style_bible.md`
- `assets/canon/patch/reference_sheets/approved_style__v1.png`
- `assets/canon/patch/reference_sheets/general_drift_risks__v1.png`
- `assets/canon/patch/reference_sheets/scene_behaviour__v1.png`

If required visual references cannot be inspected with the available tools, report the gap rather than silently substituting memory or uploaded zips.

Any rendered Patch visual must preserve the canonical Patch style: clean editorial vector style, thick rounded outlines, soft shading, teal hoodie, hoodie antennae, compact rounded proportions, black oval eyes with small white shine highlights only, dark pants, teal shoes with white soles, and teal crossbody bag with visible `>` symbol and consistent strap placement.

Patch canon reference sheets use local filenames inside `assets/canon/patch/reference_sheets/`; the path tells you they are canon references, and the filename only labels the sheet locally.

Do not drift into generic robot, glossy 3D mascot, plush realism, photorealism, unrelated asset-family styles, or alternate eye styles such as white sclera, irises, anime eyes, human eyes, doll eyes, or large expressive mascot eyes.

## Presentation production pipeline

For an adventure-plan issue intended to become a finished presentation package, follow `playbooks/end-to-end-pptx-production.md`.

The short version:

1. issue ingestion;
2. frame/analogy grounding when no strong frame exists;
3. deck doctrine;
4. deck planning;
5. image planning;
6. visual intent and Patch preflight;
7. repo/view-surface Patch reference inspection;
8. image generation or explicit blocked status;
9. PPTX build;
10. presenter sidecar;
11. presentation QA;
12. receipt and asset-canonisation follow-up.

Do not skip a required production gate. If image generation, Patch references, sidecar creation, or QA cannot be completed, stop and report the blocker rather than downgrading the package silently.

Mandatory artifact-handoff preparation for a PPTX request is not production progress. After any artifact handoff/tool preparation, resume the playbook at the repo-access proof gate. Do not report a completed artifact unless every required playbook stage for the claimed output mode actually completed.

## Finished deck expectations

A finished deck package includes:

- a PPTX;
- plain text-only title page with month date;
- a strong frame/analogy/world that makes the lesson physically happen through Patch's adventure;
- visual-first Patch-led body slides, preferably full-slide or near-full-slide images;
- sparse visible slide text, with short concept-bearing text preferably embedded in-world inside images where it helps the scene carry meaning;
- speaker notes sufficient for another presenter;
- plain text-only end card focused on takeaways and applying the learning today;
- presenter sidecar, preferably PDF;
- image receipt and canonisation follow-up when generated images or reusable assets are involved.

## Issue discipline

Use GitHub issues as durable work packets. Do not close or mark work complete without evidence. Comment with red/amber/green status when a proof run or production pass exposes failures.
