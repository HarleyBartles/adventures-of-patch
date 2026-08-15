# Agent navigation for Adventures of Patch

This repository is the canonical source of truth for the Presentation Planner / Adventures of Patch project.

## Repository purpose

The Adventures of Patch repo produces reusable presentation packages and the asset, story, and doctrine that feed them. It is the canonical source for Patch visual canon, adventure frames, style bibles, and the generated mesh that routes workers through design, planning, implementation, review, and publication.

## Source-of-truth split

- The repository tree, live issue/PR evidence, repo-tracked manifests and asset guides, and indexed project sources are authoritative.
- Linear issues and chat reports coordinate work but do not override committed repo state.
- GitHub pull requests are the publication proof for repo-backed work.
- Scratch files and session artifacts belong in the off-repo scratch workspace and are not durable.
- Uploaded zips, chat attachments, scratch files, memory, and marketplace caches are context until the repo explicitly adopts them.

## Build and test commands

- `py -3 tools/run.py ci --check` - validate the committed mechanical surfaces, mesh, and repo-standards.
- `py -3 tools/run.py ci --apply` - regenerate mechanical surfaces and validate.

## Routing pointers

### Canonical topic routers

- [Repository purpose](AGENTS.md)
- [Source-of-truth split](AGENTS.md)
- [Publication proof](.agents/runbooks/pr.md)
- [Build and test commands](AGENTS.md)
- [Testing instructions](.agents/runbooks/testing.md)
- [Code style guidelines](.agents/runbooks/code-style.md)
- [Review guidelines](.agents/runbooks/code-review.md)
- [PR instructions](.agents/runbooks/pr.md)
- [Contributing](CONTRIBUTING.md)
- [Security considerations](.agents/runbooks/security.md)
- [Routing pointers](.devin/rules/INDEX.md)
- [Maintenance responsibility](AGENTS.md)

### Conditional rule triggers

- [.devin/rules/pr.md](.devin/rules/pr.md) - pull-request workflow and publication proof
- [.devin/rules/tools.md](.devin/rules/tools.md) - working in `tools/`
- [.devin/rules/completed-plans.md](.devin/rules/completed-plans.md) - completed plans and specs

### Doctrine and stage runbooks

- [Adventures project doctrine](.agents/doctrine/adventures-project-doctrine.md)
- [Non-repo locations policy](.agents/doctrine/non-repo-locations-policy.md)
- [Mesh policy](.agents/doctrine/mesh-policy.md)
- [Repo runbook policy](.agents/doctrine/repo-runbook-policy.md)
- [Runbooks router](.agents/runbooks/AGENTS.md)
- [Repository mesh index](INDEX.md)

## Maintenance responsibility

This router is maintained by Harley Bartles. Keep it aligned with `.agents/doctrine/`, `.agents/runbooks/`, and `.devin/rules/*.md`. Regenerate the index mesh with `py -3 tools/run.py ci --apply` after moving or adding canonical homes.
