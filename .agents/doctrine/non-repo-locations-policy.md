# Non-repo locations policy

Status: active policy
Owner: Adventures of Patch repository
Scope: repository identity used by portable worktree and scratch helpers

Portable worktree and scratch layout belongs to `using-git-worktrees`,
`subagent-workspace`, and `repo-standards`. The Adventures-specific repository
slug is `adventures-of-patch`.

Canonical external roots therefore resolve beneath:

- `../_agent-worktrees/adventures-of-patch/` for linked worktrees; and
- `../_agent-scratch/adventures-of-patch/` for disposable scratch.

No canonical Adventures source or durable project asset lives solely in either
external root.
