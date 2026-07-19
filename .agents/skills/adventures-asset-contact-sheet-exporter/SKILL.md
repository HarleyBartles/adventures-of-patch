---
name: adventures-asset-contact-sheet-exporter
description: Use when repo-canonical visual inspection needs deterministic contact sheets from an explicit Adventures asset dispatch
metadata:
  source_id: adventures-asset-contact-sheet-exporter
  status: active-local
  scope: Deterministic visual inspection package creation
  use_when: bounded repo-relative PNG families must be rendered for inspection without changing canon
  do_not_use_when: image generation, image acceptance, or asset canonisation is required
---

# Adventures asset contact-sheet exporter

This is a deterministic inspection capability, not an image-generation or
canonisation skill. It consumes an explicit dispatch, resolves safe
repo-relative PNG paths, renders stable contact sheets, includes selected full
reference assets, and emits manifests and a zip package.

## Use

Read the dispatch and CLI contract in `README.md`. Run from the repository
root:

```bash
python .agents/skills/adventures-asset-contact-sheet-exporter/scripts/build_contact_sheets.py \
  --dispatch .agents/skills/adventures-asset-contact-sheet-exporter/examples/sample-dispatch.json \
  --output-root output-zips
```

## Boundaries

- Inputs must be explicit repo-relative paths; reject absolute paths, traversal,
  missing files, unreadable files, and non-PNG inputs.
- Do not scan the whole repository for vague selectors.
- Do not modify source images or declare anything canonical.
- Do not compile asset sheets or accept generated images; route those decisions
  to `adventures-image-qa` and the asset-sheet production contract.
- Keep staging under ignored `scratch/contact-sheet-builds/` and emitted zips
  disposable unless a separate package-landing decision promotes one.

Record skipped or unresolved inputs in the generated manifests. Stable ordering
and deterministic layout are part of the output contract.
