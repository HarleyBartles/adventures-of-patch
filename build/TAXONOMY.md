# Asset Taxonomy Contract

This document defines the active asset-information model for `build/`, `style/`, `published/`, and `workbench/`.

## Core rule

Path, lane, and manifest carry taxonomy. Filenames are local identifiers inside a lane.

- Path tells you the layer, domain, family, and package.
- Lane tells you whether a PNG is a `source_images/`, `compiled_asset_sheets/`, `reference_sheets/`, or other allowed artifact kind.
- Manifest tells you the semantic identity, package completeness, and provenance.
- Filename should not repeat the full package taxonomy just to make the path feel safer.

## Repository layers

- `published/` - finished, licensable CC BY-ND output (`adventures/`, `fairytales/`).
- `build/` - reusable assets that feed published output.
- `style/` - style bibles, pattern guides, and image-generation drivers.
- `workbench/` - active, repo-tracked experiments and drafts; no licence granted.

## Canonical build family shape

Build families live directly under `build/<domain>/<family>/`. The old `asset_packs/` pass-through is gone. Each package is a direct child of its family.

```text
build/<domain>/<family>/
  INDEX.md
  README.md optional
  <pack_id>/
    INDEX.md
    README.md optional
    source_images/
      INDEX.md
      <local_name>__vN.png
    compiled_asset_sheets/
      sheet__vN.png
    reference_sheets/
      overview__vN.png
      <local_reference_name>__vN.png
    manifests/
      manifest.json
```

A single-pack family whose pack would share the family name is collapsed so the package lanes live directly at the family root:

```text
build/environments/identity-emporium/
  INDEX.md
  README.md
  reference_sheets/
    overview__v1.png
  manifests/
    manifest.json
```

## Canonical style shape

Style lives in `style/` as first-class source.

```text
style/patch/
  style-bible.md
  reference_sheets/
    approved_style__v1.png
    style_drift_risks__v1_0.png

style/patterns/
  style-guide.md
  reference_sheets/
    approved_patterns__v1.png
    general_drift_risks__v1.png
```

## Allowed package lanes

- `source_images/`
- `compiled_asset_sheets/`
- `reference_sheets/`
- `manifests/`

`workbench/` is not a build lane and does not become canonical by path alone.

## Filename rules

- `source_images/` filenames are local inputs, such as `hero__v1.png` or `side_view__v1.png`.
- `compiled_asset_sheets/` filenames are local compiled-sheet labels, normally `sheet__vN.png`.
- `reference_sheets/` filenames are local sheet labels, such as `overview__v1.png` or `front_exterior__vN.png`.
- `workbench/` filenames are local working-reference labels; they remain in `workbench/` until promoted.
- Filenames must not repeat the package taxonomy in full just to encode what the path already says.
- Over-encoded names such as `asset_sheet__character__stakeholders__data_architect_product_trio__v1.png` are not acceptable active filenames.

## Manifest contract

Every active package must have `manifests/manifest.json`.

Minimum fields:

- `domain`
- `family`
- `package_id`
- `package_type`
- `status`
- `artifact_lanes`
- `files`
- `provenance_notes`

Lane completeness is recorded in the manifest.

- Missing source images are provenance/completeness state.
- Missing compiled sheets are provenance/completeness state.
- Reference-only families can be represented as reference packs with missing source/compiled lanes recorded explicitly.

Recommended `artifact_lanes` values:

- `present`
- `absent_not_required`
- `absent_missing_legacy_inputs`
- `absent_not_reconstructed`

## Index rules

- Every visible directory should have an `INDEX.md`.
- Indexes list only direct children that really exist.
- Parent indexes must point to existing child indexes.
- If a file moved, update the index mesh in the same batch.

## Validator

Repo-tracked validation lives in `tools/run.py`:

- `py -3 tools/run.py ci --check`
- `py -3 tools/run.py ci --apply`

The `repo-standards` and `generating-agent-mesh` skills validate surface presence, index consistency, and `git diff --check`.

The taxonomy should be mechanically checkable:

- every build family root has its packages directly beneath it;
- every package has `manifests/manifest.json`;
- every manifest path exists;
- `source_images/` contains only local source images;
- `compiled_asset_sheets/` contains only local compiled sheets;
- `reference_sheets/` contains only local reference sheets;
- `workbench/` contents are working references, not canonical package contents;
- no active filename is over-encoded with redundant package taxonomy;
- no stale moved path remains in indexes, manifests, registry, docs, or sample dispatches;
- no UTF-8 BOM exists in touched Markdown or JSON files;
- PNG count and bytes remain unchanged across the restructure.

## Workbench

`workbench/` stores active experiments and drafts that are not yet canonical. Material promoted from `workbench/` should move into `build/` or `style/` through a custody workflow. Material discarded from `workbench/` should be deleted, not archived.

## Operating rule

When a taxonomy migration changes a PNG path, update all affected indexes, manifests, docs, registry entries, and sample dispatches in the same batch.
