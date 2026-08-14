# The Sorcerer’s Apprentice — Delegation Without Boundaries

This directory is the custody surface for the approved Patch Fairytales Sorcerer’s Apprentice visual set.

The image bytes are intentionally not part of this scaffold. Each adjacent sidecar records the exact expected filename, SHA-256, byte size, dimensions, semantic role, and accepted visual constraints so an on-disk custody agent can place and verify the approved PNGs without renaming ambiguity.

## Expected approved image files

- `scene__runaway_recursive_delegation__v1.png`
- `scene__five_worker_handoff__v1.png`
- `detail__delegation_instruction_closeup__v1.png`
- `detail__delegation_instruction_circle__v1.png`
- `prop__delegation_policy__v1.png`
- `page__delegation_without_boundaries__v1.png`

Each image has an adjacent `-sidecar.json` already scaffolded in this directory.

## Custody handoff

The on-disk custody pass should:

1. place the six approved image bytes at the exact filenames above;
2. verify each image against the SHA-256, byte size, and dimensions recorded in its adjacent sidecar;
3. update sidecar custody state only after matching bytes are present;
4. add the normal package manifest/provenance surface if required by current Fairytales custody conventions;
5. regenerate the repository index mesh rather than hand-editing `INDEX.md`.

Until the PNG bytes are present and verified, the sidecars are scaffolding and do not by themselves prove repo custody of the images.
