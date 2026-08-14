# Pull request runbook

Use this runbook for pull-request workflow and publication proof in this repo.

## Before you begin

- Read root [`AGENTS.md`](../../AGENTS.md).
- Read [`CONTRIBUTING.md`](../../CONTRIBUTING.md) and [`REVIEW.md`](../../REVIEW.md).
- Invoke `/repo-worker-base`.

## When to use

- Preparing a branch for review.
- Creating or updating a PR.
- Providing publication proof for repo work.

## Draft PR policy

- Open pull requests as **draft**.
- Keep a PR in draft while iterating and running local validation.
- Flip to ready for review only after self-review is complete and `py -3 tools/run.py ci --check` passes.
- The PR body must include publication proof.

## Repo-specific guidance

- Work in an isolated worktree on a task branch.
- Run `py -3 tools/run.py ci --check` before pushing or flipping a PR to ready.
- Commit focused changes. Do not commit generated artifacts unless the generator produced them.
- Push the branch and open a **draft** PR into `main` unless direct-main work is explicitly authorized.
- A valid repo-work return must include one of:
  1. an open PR URL with branch name and full head SHA;
  2. a verified direct-main commit SHA;
  3. a concrete publication blocker.

## Pre-commit hook

This repo installs a `pre-commit` hook via `repo-standards` that runs
`py -3 tools/run.py ci --apply --allow-shared-checkout` and stages generated
surfaces. If the hook is not installed, run `py -3 tools/run.py ci --apply` and
then `py -3 tools/run.py ci --check` before committing.

## Routing to skills

- `/repo-worker-base` for worktree, branch, and publication boundaries.
- `/using-github-mcp` for PR evidence and GitHub proof.
- `/verification-before-completion` before claiming the PR is green.
- `/requesting-code-review` when the branch is ready for human review.
