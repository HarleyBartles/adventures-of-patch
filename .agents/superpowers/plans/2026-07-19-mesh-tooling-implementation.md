# Mesh tooling implementation

Status: approved continuation slice for draft PR #73

## Objective

Replace the stale hand-maintained index mesh with deterministic, Git-derived
generation and validation while preserving agent-surface custody boundaries.

## Scope

- Add `scripts/generate_index_mesh.py` as the portable implementation.
- Add real PowerShell and Bash wrappers with matching `--check` behavior.
- Add focused tests for generated shape, stale detection, links, ignored paths,
  reparse points, gitlinks, skill roots, LF output, and worktree safety.
- Regenerate all in-scope repository `INDEX.md` files.
- Keep `.agents/plugins/marketplace-source` a gitlink leaf.
- Keep `.agents/skills` as a skill-root leaf while indexing its direct skills.
- Update mesh routing surfaces when generated navigation exposes the new
  policies.

## Exclusions

- No line-ending policy or broad text renormalization beyond generator-owned
  LF output.
- No Patch identity migration.
- No Adventures skill authoring or disposition changes.
- No marketplace refresh or plugin changes.

## Safety

- Derive the repo root and checkout state through Git, not script-parent
  inference.
- Reject submodule execution.
- Refuse shared-checkout writes unless `--allow-shared-checkout` is explicit.
- Keep `--check` read-only.
- Use atomic writes and refuse links/reparse points in generated targets.

## Acceptance

- Write mode and check mode agree on the same expected mesh.
- Repeated generation is stable.
- Generated indexes contain navigation only and no operative policy.
- Gitlinks and skill roots are not descended into.
- Local authored `adventures-*` skills remain visible and are not pruned.
- Link validation passes for generated local links.
- Focused tests and `git diff --check` pass.
