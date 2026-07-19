# Proposed Repository-Local Adventures Skills

Status: proposal only. No `adventures-*` skill is imported or authored by the
plugin refresh slice.

## Proposed local set from the retired marketplace pack

Retain the following ten names as repository-local candidates after a bounded
adaptation pass. Keep the `adventures-` prefix so local custody is explicit and
the marketplace installer will preserve them:

- `adventures-project-doctrine`
- `adventures-bootstrap`
- `adventures-github-operations`
- `adventures-visual-preproduction`
- `adventures-storyboard-preflight`
- `adventures-visual-bible-creator`
- `adventures-visual-bible-interpreter`
- `adventures-image-qa`
- `adventures-asset-sheet-compiler`
- `adventures-frame-buster`

These are all relevant to the current Adventures project surface, but they are
not automatically valid as-is. The adaptation pass must:

- remove Patch as an agent, actor lane, or governance identity while retaining
  Patch as the character and visual canon;
- replace stale checkout-specific or `/home/oai/skills` paths with repo-derived
  paths and current project playbooks;
- reconcile each skill with the live `assets/canon/patch/`, `playbooks/`, and
  `docs/project/` surfaces; and
- preserve explicit boundaries between planning, generation, editing, QA, and
  acceptance.

## Proposed local names for existing Patch capabilities

The three existing repo-local capabilities under `Patch/SKILLS/` should be
reviewed for migration into the same local namespace:

| Existing capability | Proposed local skill | Rationale |
| --- | --- | --- |
| `Patch/SKILLS/patch-asset-contact-sheet-exporter` | `adventures-asset-contact-sheet-exporter` | Asset inspection/export is project capability; the name should no longer imply an agent owner. |
| `Patch/SKILLS/patch-asset-directory-source-packager` | `adventures-asset-directory-source-packager` | Source packaging is repo-local production work, not Patch agent governance. |
| `Patch/SKILLS/patch-asset-zip-ingress` | `adventures-asset-zip-ingress` | Zip ingress remains a project workflow while the `Patch/` agent surface is retired. |

## Acceptance gate for the later local-authoring pass

Create a candidate skill only after checking its source against the live repo,
writing the skill with the repository-local path contract, and verifying that
it does not claim a retired agent identity or stale actor surface. The later
pass should then install the local candidates beside the marketplace-derived
skills and prove that refresh preserves them.
