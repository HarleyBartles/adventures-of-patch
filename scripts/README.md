# Scripts

This directory contains deterministic repository hygiene and agent-surface
tooling. Prefer these entrypoints over ad hoc shell commands.

## Agent-surface commands

- `refresh_agent_surfaces.{py,ps1,sh}` refreshes derived skills and the index
  mesh; use `--check` or `-Check` for read-only validation. Use
  `--committed-only` when the private marketplace source is unavailable and
  only the committed projection should be checked.
- `validate_agent_mesh.{py,ps1,sh}` checks authored routes, local skill
  custody, retired route names, and forbidden legacy homes; use
  `--changed-from origin/main` for scoped PR validation.
- `ci-preflight.{ps1,sh}` runs the local refresh, mesh, skill, validator, and
  test checks. CI adds `--committed-only` to validate the projection without
  requiring marketplace access.
- `generate_index_mesh.{py,ps1,sh}` owns generated `INDEX.md` navigation.
- `install_agent_skills.{py,ps1,sh}` refreshes marketplace-derived skills.

## Conventions

- Python files are the portable implementation surface.
- PowerShell and Bash files are equivalent thin entrypoints.
- Check modes must validate the write-mode contract without mutating files.
- All mutating commands must run from the intended linked worktree.
