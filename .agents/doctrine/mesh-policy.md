# Mesh policy

Status: active policy
Owner: Adventures of Patch repository tooling
Scope: Adventures-specific mesh and installed-skill custody

Portable mesh generation and validation behavior belongs to
`generating-agent-mesh` and `repo-worker-base`. This policy contains only the
repository delta.

## Local boundaries

- `.agents/plugins/marketplace-source` is a gitlink and a mesh leaf. The parent
  mesh may link to it but must not descend into it.
- Marketplace-derived installed skill directories are mesh leaves.
- Project-owned skills use the `adventures-*` prefix and must survive portable
  skill refreshes.
- Exact local skill names are declared in
  `.agents/plugins/marketplace.json` under `repo.local_skills`.
- Ordinary project work belongs in existing project, asset, documentation,
  runbook, or script homes rather than hidden under `.agents/`.

The local complete validation capability is `py -3 tools/run.py ci --check`.
