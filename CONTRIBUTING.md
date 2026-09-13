# Contributing

This file is the repo's contributor entry point.

## Pre-contribution reading

- Read root [`AGENTS.md`](./AGENTS.md) for source-of-truth and publication rules.
- Read [`.agents/doctrine/repo-runbook-policy.md`](./.agents/doctrine/repo-runbook-policy.md) for this repo's mapping to the cross-repo runbook standard.
- Read [`.agents/runbooks/code-style.md`](./.agents/runbooks/code-style.md) for code and writing conventions.

## Workflow routing

Invoke `/using-superpowers-plus`; it selects the portable workflow owner. The
selected owner reads the matching repo-local runbook for Adventures paths,
commands, custody, and exceptions.

## Repo-specific contribution notes

- Preserve `.agents/plugins/marketplace-source` as a gitlink. Change portable
  skills in their canonical marketplace repository, then refresh this repo.
- Keep project-owned skills under `.agents/skills/adventures-*/` and list them
  exactly in `.agents/plugins/marketplace.json` under `repo.local_skills`.
- Regenerate navigation with `py -3 tools/run.py ci --apply`; never hand-edit
  generated `INDEX.md` files.
- Keep Patch character canon, image acceptance, and presentation readiness under
  their Adventures-specific doctrine and runbooks.
- The local PR base is `main`; publication details are in
  `.agents/runbooks/pr.md`.
