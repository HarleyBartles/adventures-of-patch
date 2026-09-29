# Repository Runbook and Playbook Policy

This repository follows `repo-standards`. Lifecycle stages are runbooks; available topical workflows are playbooks.

## Standard runbooks

| Standard runbook | Local path | Status |
|---|---|---|
| design.md | `.agents/runbooks/design.md` | required |
| planning.md | `.agents/runbooks/planning.md` | required |
| implementing.md | `.agents/runbooks/implementing.md` | required |
| code-review.md | `.agents/runbooks/code-review.md` | required |
| pr.md | `.agents/runbooks/pr.md` | required |

## Standard playbooks

| Standard playbook | Local path | Status |
|---|---|---|
| code-style.md | `.agents/playbooks/code-style.md` | required |
| testing.md | `.agents/playbooks/testing.md` | required |
| security.md | `.agents/playbooks/security.md` | optional |
| skill-authoring.md | `.agents/playbooks/skill-authoring.md` | optional |
| marketplace-generation.md | `.agents/playbooks/marketplace-generation.md` | optional |
| completed-artifact-custody.md | `.agents/playbooks/completed-artifact-custody.md` | optional |
| repo-doctrine.md | `.agents/playbooks/repo-doctrine.md` | optional |
| unslop-profile-maintenance.md | `.agents/playbooks/unslop-profile-maintenance.md` | optional |

## Additional repository-specific playbooks

- `.agents/playbooks/visual-production.md` - idea-to-visual-adventure production workflow.

## Root contributor and review surfaces

- `REVIEW.md` enters through the code-review runbook.
- `CONTRIBUTING.md` enters through the applicable lifecycle runbook.

## Exceptions

None.
