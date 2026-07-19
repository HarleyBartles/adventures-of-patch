# Plugin marketplace routing

Use this routing file before changing the repo-local plugin manifest, pinned
marketplace source, or derived skill refresh contract.

- `marketplace.json` is the repo-owned provider manifest.
- `marketplace-source/` is a pinned gitlink boundary; do not edit its contents
  from this repository.
- `INDEX.md` is generated navigation.
- Refresh derived skills with the scripts in `../../scripts/`, then regenerate
  the full index mesh.

Do not store proposals, inventories, or ordinary project documentation in this
directory. Keep durable policy in `.agents/doctrine/` and current procedures in
`.agents/runbooks/`.
