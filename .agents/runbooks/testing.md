# Testing runbook

This is the repository-specific command and check map for validation.

## Canonical capabilities

- Apply mechanical surfaces: `py -3 tools/run.py ci --apply`.
- Check the committed or otherwise explicitly selected tree:
  `py -3 tools/run.py ci --check`.
- The consumer command vectors are declared in
  `.agents/contracts/repo-standards-commands.json`.

## Repository-specific checks

The canonical check validates refreshed skill provenance, generated index mesh,
agent routing and local skill custody, repo-standard surfaces, image sidecars,
sidecar normalization, and whitespace/diff integrity.
