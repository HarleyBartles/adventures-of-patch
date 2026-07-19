# Remaining agent-workspace slices

Status: approved continuation for draft PR #73

## Objective

Finish the repository-local agent workspace cleanup and refresh from the
merged upstream marketplace main.

## Decisions

- The four canonical stage overlays live in `.agents/guides/`.
- The retained local skill set is:
  - `adventures-project-readiness`
  - `adventures-visual-preproduction`
  - `adventures-image-qa`
- `adventures-bootstrap` and `adventures-github-operations` are retired.
- `adventures-project-doctrine` remains a thin triggerable router into
  repository doctrine; durable law remains in `.agents/doctrine/`.
- The frame gate is absorbed by `adventures-project-readiness`.
- Storyboard preflight and visual-bible interpretation/creation are composed
  into readiness and visual preproduction rather than separate skills.
- Asset-sheet compilation and canonisation remain playbook/script concerns;
  deterministic packaging is not a judgment skill.
- The stale contact-sheet, asset-directory packaging, and asset-zip ingress
  capabilities are removed.
- Patch remains the character and visual canon only; Patch actor governance,
  actor lanes, and actor-bound return contracts are retired.
- The marketplace submodule moves to merged upstream main and refreshes the
  marketplace-derived projection.

## Skill authoring gate

For each retained skill, record a pressure scenario and baseline ambiguity,
author the smallest control plane, run structural/application checks, and
record the disposition and validation in the skill or plan. Do not bulk-copy
the retired marketplace pack.

## Exclusions

- No line-ending normalization.
- No marketplace submodule movement before the upstream removal is merged.
- No image-generation calls or asset mutation.
- No PR merge; publish all commits to draft PR #73.

## Acceptance

- Four guides are reachable from `.agents/AGENTS.md`.
- Every retained local skill has valid frontmatter, clear triggers, local
  custody metadata, boundaries, stop conditions, and a live-repo reference.
- Retired candidates and reclassifications are recorded.
- No operative Patch agent identity remains in active routing or skill docs.
- The mesh generator and all validation checks pass on the final head.
