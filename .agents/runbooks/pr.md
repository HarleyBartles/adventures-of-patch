# Pull request local overlay

Portable commit, draft lifecycle, review sequencing, and publication handoff
belong to the selected skills. This file contains only Adventures repository
configuration.

## When

Use when publishing or checking repo-backed work through GitHub.

## Required skills

- `publishing-source` owns the publication decision and lifecycle.
- `using-github-mcp` owns GitHub/CLI surface selection and readback.
- `verification-before-completion` owns validation claims.

## Composition

Use `publishing-source` as owner, bind it to the local base/commands below, use
`using-github-mcp` for mutation and exact readback, and verify before readiness.

## Doctrine and contracts

- `.agents/doctrine/adventures-project-doctrine.md`
- `.agents/contracts/repo-standards-commands.json`

## Local commands and paths

See `## PR instructions` below.

## Evidence contract

Evidence includes PR URL, base/head branches, full remote head SHA, draft/state,
current validation proof, and any hosted-check boundary.

## Prohibited combinations

- Do not treat a local commit or branch as publication proof.
- Do not bypass draft-aware CI or infer GitHub state from a worker report.

## PR instructions

- Base branch: `main`.
- Apply capability: `py -3 tools/run.py ci --apply`.
- Check capability: `py -3 tools/run.py ci --check`.
- Consumer command declaration:
  `.agents/contracts/repo-standards-commands.json`.
- Tracked commit gate: `.githooks/pre-commit`, activated with
  `git config --worktree core.hooksPath .githooks` after enabling
  `extensions.worktreeConfig` once for the repository.
- Hosted workflow: `.github/workflows/ci.yml`.
- The hosted `build-and-test` and `repo-hygiene` jobs run for `main` pushes and
  non-draft pull requests; `ready_for_review` is an enabled PR activity.

## Publication proof surface

Repo-backed publication proof is the GitHub pull request targeting `main`, or a
verified commit on `main` when direct-main publication was explicitly
authorized. Local branches, worktrees, files, and validation output are not the
publication surface.

## Exceptions

None.
