# Code style runbook

This is the repository-specific overlay for implementation and documentation
style. It does not replace language-specific skills or portable workflow
guidance.

## Python and scripts

- Use `py -3` in Windows-facing commands and repository documentation.
- Repository mutation scripts use `tools/shared_checkout.py` for the repo's
  shared-checkout boundary.
- Keep generated navigation and installed skills under their owning generators;
  do not hand-edit their output.

## Documentation

- Keep root and scoped `AGENTS.md` files as routing surfaces, runbooks as
  repo-specific operational overlays, and doctrine as durable policy.
- Use descriptive Markdown links and repository-relative paths in tracked docs.
- Preserve Patch as the project character; never use Patch as an agent, actor,
  owner, or execution-lane label.

## Data and assets

- Preserve deterministic JSON formatting through the repository normalizers.
- Keep image sidecars adjacent to their governed assets and conformant with the
  sidecar schema and provenance rules.
