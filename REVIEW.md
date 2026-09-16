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

- Marketplace refreshes must preserve every `adventures-*` local skill and keep
  each installed portable skill backed by a subscribed plugin.
- Generated `INDEX.md` files must come from the mesh generator and must not
  descend into the marketplace-source gitlink or installed-skill internals.
- Doctrine, runbooks, skills, and scripts must retain distinct ownership; local
  overlays must not duplicate portable workflow instructions.
- Patch is the project character, never an agent, actor, owner, or execution
  lane.
- Generated images and downstream artifacts require the applicable project
  readiness, direct inspection, and selection evidence before acceptance claims.
- Review conclusions must match the exact published PR head and current
  validation evidence.
