# Pull request local overlay

Portable commit, draft lifecycle, review sequencing, and publication handoff
belong to the selected skills. This file contains only Adventures repository
configuration.

## PR instructions

- Base branch: `main`.
- Apply capability: `py -3 tools/run.py ci --apply`.
- Check capability: `py -3 tools/run.py ci --check`.
- Consumer command declaration:
  `.agents/contracts/repo-standards-commands.json`.
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
