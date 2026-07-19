# Scripts

This directory contains deterministic repository hygiene and agent-surface
tooling. Prefer these entrypoints over ad hoc shell commands.

## Agent-surface commands

- `refresh_agent_surfaces.{py,ps1,sh}` refreshes derived skills and the index
  mesh; use `--check` or `-Check` for read-only validation.
- `validate_agent_mesh.{py,ps1,sh}` checks authored routes, local skill
  custody, retired route names, and forbidden legacy homes; use
  `--changed-from origin/main` for scoped PR validation.
- `ci-preflight.{ps1,sh}` runs the same refresh, mesh, skill, validator, and
  test checks used by the repository workflow.
- `generate_index_mesh.{py,ps1,sh}` owns generated `INDEX.md` navigation.
- `install_agent_skills.{py,ps1,sh}` refreshes marketplace-derived skills.

## Conventions

- Python files are the portable implementation surface.
- PowerShell and Bash files are equivalent thin entrypoints.
- Check modes must validate the write-mode contract without mutating files.
- All mutating commands must run from the intended linked worktree.
