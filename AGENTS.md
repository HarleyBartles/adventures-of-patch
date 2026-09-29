# Agent navigation for Adventures of Patch

This repository is the canonical source of truth for the Presentation Planner / Adventures of Patch project.

## Repository purpose

The Adventures of Patch repo produces reusable visual adventures and the assets, stories, learning frames, and doctrine that feed them. It is the canonical source for Patch visual canon, adventure frames, style bibles, and the lifecycle runbooks and topical playbooks that compose project capabilities with doctrine and contracts.

## Source-of-truth split

- The repository tree, live issue/PR evidence, repo-tracked manifests and asset guides, and direct canonical sources are authoritative.
- Linear issues and chat reports coordinate work but do not override committed repo state.
- GitHub pull requests are the publication proof for repo-backed work.
- Scratch files and session artifacts belong in the off-repo scratch workspace and are not durable.
- Uploaded zips, chat attachments, scratch files, memory, and marketplace caches are context until the repo explicitly adopts them.

## Build and test commands

- `py -3 tools/run.py ci --check` - validate deployed standards, composition, asset sidecars, and repository routing.
- `py -3 tools/run.py ci --apply` - deploy selected standards, apply mechanical surfaces, and validate.

## Routing pointers

### Canonical topic routers

#### Publication proof

Pull-request publication proof is recorded in the [PR runbook](.agents/runbooks/pr.md).

#### PR instructions

Follow the [PR instructions](.agents/runbooks/pr.md) for publication and remote-state verification.

- [Repository purpose](AGENTS.md)
- [Source-of-truth split](AGENTS.md)
- [Publication proof](.agents/runbooks/pr.md)
- [Build and test commands](AGENTS.md)
- [Testing instructions](.agents/playbooks/testing.md)
- [Code style guidelines](.agents/playbooks/code-style.md)
- [Review guidelines](.agents/runbooks/code-review.md)
- [PR instructions](.agents/runbooks/pr.md)
- [Contributing](CONTRIBUTING.md)
- [Security considerations](.agents/playbooks/security.md)
- [Pull-request rule](.devin/rules/pr.md)
- [Maintenance responsibility](AGENTS.md)

### Conditional rule triggers

- [.devin/rules/pr.md](.devin/rules/pr.md) - pull-request workflow and publication proof
- [.devin/rules/tools.md](.devin/rules/tools.md) - working in `tools/`

### Doctrine and stage runbooks

- [Adventures project doctrine](.agents/doctrine/adventures-project-doctrine.md)
- [Non-repo locations policy](.agents/doctrine/non-repo-locations-policy.md)
- [Repository doctrine](.agents/playbooks/repo-doctrine.md)
- [Repo runbook policy](.agents/doctrine/repo-runbook-policy.md)
- [Runbooks router](.agents/runbooks/AGENTS.md)
- [Lifecycle runbooks](.agents/runbooks/AGENTS.md)
- [Topical playbooks](.agents/playbooks/AGENTS.md)

## Maintenance responsibility

This router is maintained by Harley Bartles. Keep it aligned with `.agents/doctrine/`, `.agents/runbooks/`, `.agents/playbooks/`, and `.devin/rules/*.md`. Update direct routing links when canonical homes move.
