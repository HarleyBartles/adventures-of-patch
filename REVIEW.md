# Review entry point

This file is the repo's review entry point. Code-review agents discover it automatically.

## Pre-review reading

- Read root [`AGENTS.md`](./AGENTS.md) for source-of-truth and publication rules.
- Read [`.agents/doctrine/repo-runbook-policy.md`](./.agents/doctrine/repo-runbook-policy.md) for this repo's mapping to the cross-repo runbook standard.
- Read [`.agents/runbooks/code-review.md`](./.agents/runbooks/code-review.md) for Adventures-specific review concerns.

## Workflow routing

Invoke `/using-superpowers-plus`; it selects the portable review owner. The
owner reads `.agents/runbooks/code-review.md` for Adventures-specific concerns.

## First-class review concerns

- Repository-owned `adventures-*` skills stay declared in `repo.local_skills`;
  selected standards and their deployed resources must match the pinned gitlink.
- Generated mesh indexes are retired; navigate through direct canonical links
  and tracked manifests, and do not descend into the marketplace-source gitlink.
- Doctrine, runbooks, skills, and scripts must retain distinct ownership; local
  overlays must not duplicate portable workflow instructions.
- Patch is the project character, never an agent, actor, owner, or execution
  lane.
- Generated images and downstream artifacts require the applicable project
  readiness, direct inspection, and selection evidence before acceptance claims.
- Review conclusions must match the exact published PR head and current
  validation evidence.
