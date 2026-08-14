# Non-repo locations policy

This policy covers canonical locations outside the repo tree that agents use
for isolated work and scratch artifacts.

## Worktrees

Isolated branch worktrees live in `../_agent-worktrees/adventures-of-patch/<date>-<branch-name>/`,
a sibling of the repo folder. Worktree payloads live entirely outside the repo
tree. On Windows this is typically `Z:\_agent-worktrees\adventures-of-patch\<date>-<branch-name>\`.

Rules:

- Use worktrees only for isolated branch checkouts and temporary local issue lanes.
- Do not store canonical source, generated outputs, or long-lived repo assets in worktrees.

## Scratch files

Scratch files (temporary scripts, commit message temp files, inspection scripts,
debug output, subagent inputs and outputs) go in
`../_agent-scratch/adventures-of-patch/<branch>/<plan-basename>/`, not in the
repo tree. The scratch directory is a sibling of the repo folder. On Windows the
canonical path is `Z:\_agent-scratch\adventures-of-patch\<branch>\<plan-basename>\`.

Rules:

- The top level of `_agent-scratch` must contain only folders named after repositories.
- Inside the `adventures-of-patch/` folder, create subfolders named after the worktree branch.
- Plan- or task-scoped scratch lives inside the branch folder.
- Scratch contents are not durable. Do not put anything in scratch that needs to survive beyond the work it supports.
- Do not commit scratch files into the repo.
- Do not leave scratch files in the repo working tree. If a scratch file ends up in the repo tree, remove it before committing.
- Use the `subagent-workspace` skill to resolve the off-repo scratch path for subagent tasks.
