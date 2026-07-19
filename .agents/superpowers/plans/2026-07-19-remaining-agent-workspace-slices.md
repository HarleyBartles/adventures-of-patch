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
- Asset-sheet compilation and canonisation remain runbook/script concerns;
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

## Skill authoring evidence

The retained skills were assessed as four distinct local decisions, not as a
bulk marketplace transplant:

| Skill | Pressure scenario | Observed RED ambiguity | Local control and validation |
| --- | --- | --- | --- |
| `adventures-project-doctrine` | A repo-backed task needs a project invariant before implementation. | The no-skill agent selected an obsolete project-owner route instead of a local doctrine router. | Thin router into `.agents/doctrine/`; frontmatter, route table, composition contract, and character-only boundary were checked. |
| `adventures-project-readiness` | A thin issue requests a finished deck with a theme but no frame, mappings, continuity, or accepted assets. | The no-skill agent stopped generically but did not name the repository's four-state readiness result or owner. | Four-state readiness ladder, frame gate, handoff record, and production stop conditions were checked against the readiness runbook. |
| `adventures-visual-preproduction` | A frame-ready issue needs reusable visual language and a governed reference candidate containing Patch and other agents. | The no-skill agent named generic inspection risks but did not route candidate acceptance to the local QA skill or define the preproduction boundary. | Visual-preproduction route, candidate boundary, Patch/non-Patch constraints, and handoff to `adventures-image-qa` were checked. |
| `adventures-image-qa` | A generated Patch image is proposed for immediate deck use and canonisation. | The no-skill agent correctly held the candidate but could not select an Adventures QA lane or return the local outcome vocabulary. | Lane table, acceptance gates, explicit outcomes, Harley stop, and no-promotion boundary were checked against the image-QA runbook. |

Disposition: retain all four as repository-local skills. The doctrine skill is
a router; readiness and visual preproduction own judgment boundaries; image
QA owns acceptance. Deterministic compilation, packaging, and indexing remain
runbook/script concerns. No generated image was created for this assessment.

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
