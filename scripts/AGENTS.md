# scripts directory guidance

This directory holds repo-tracked validation and maintenance helpers.

When working in `scripts/`, start with:

1. `../INDEX.md`
2. `../AGENTS.md`
3. this file
4. `INDEX.md`
5. the relevant helper or script source

Prefer deterministic repo validation helpers over ad hoc shell logic when they already exist.

For mesh work, read `.agents/doctrine/mesh-policy.md` before editing the
generator or generated indexes. `generate_index_mesh.py` is the portable
owner; `generate_index_mesh.ps1` and `generate_index_mesh.sh` are equivalent
entrypoints. Use `--check` for validation and do not hand-edit `INDEX.md`.
