# Contributing

This file is the repo's contributor entry point.

## Pre-contribution reading

- Read root [`AGENTS.md`](./AGENTS.md) for source-of-truth and publication rules.
- Read [`.agents/doctrine/repo-runbook-policy.md`](./.agents/doctrine/repo-runbook-policy.md) for this repo's mapping to the cross-repo runbook standard.
- Read [`.agents/playbooks/code-style.md`](./.agents/playbooks/code-style.md) for code and writing conventions.

## Workflow routing

Invoke `/using-superpowers-plus`; it selects the portable workflow owner. The
selected owner reads the matching repo-local runbook for Adventures paths,
commands, custody, and exceptions.

## Repo-specific contribution notes

- Enable per-worktree Git configuration once with
  `git config extensions.worktreeConfig true`, then activate the tracked gate
  in the checkout with `py -3 .agents/standards/_runtime/repo_standards.py --standard tracked-validation-hook --apply --yes --allow-shared-checkout`; the configured tracked hook lives in `githooks/pre-commit`.
- Preserve `.agents/plugins/marketplace-source` as a gitlink. Change portable
  skills in their canonical marketplace repository, then advance the source gitlink and deploy the selected standards.
- Keep project-owned skills under `.agents/skills/adventures-*/` and list them
  exactly in `.agents/plugins/marketplace.json` under `repo.local_skills`.
- Apply selected standards and validate direct routing with `py -3 tools/run.py ci --apply`; do not generate navigation indexes.
- Keep Patch character canon, image acceptance, and presentation readiness under
  their Adventures-specific doctrine, contracts, and playbooks.
- The local PR base is `main`; publication details are in
  `.agents/runbooks/pr.md`.
