# Asset Taxonomy Contract

This document defines the active asset-information model for `assets/`.

## Core rule

Path, lane, and manifest carry taxonomy. Filenames are local identifiers inside a lane.

- Path tells you the domain, family, and package.
- Lane tells you whether a PNG is a `source_images/`, `compiled_asset_sheets/`, `reference_sheets/`, or other allowed artifact kind.
- Manifest tells you the semantic identity, package completeness, and provenance.
- Filename should not repeat the full package taxonomy just to make the path feel safer.

## Canonical repository shapes

### Working in-flight lane

`assets/in-flight/` is a repo-tracked working lane for current visual references that are not yet canonical asset-pack contents.

```text
assets/in-flight/
  INDEX.md
  <working_reference>.png
```

This lane is separate from reusable asset packs and canon roots.

- In-flight images are repo-tracked visual evidence and working references, not final canonical asset-pack contents.
- In-flight images may be included in a repo-indexed visual inspection package when requested.
- In-flight images may also be included full-size when the dispatch marks them as storyboard, diagram, or full-size reference.
- Manifest and evidence output must label them as `in_flight_image` or `in_flight_reference`, not `source_image`, `asset_sheet`, `compiled_asset_sheet`, or canon reference.
- If an in-flight image later becomes reusable or canonical, promote it through a separate asset-pack or canonisation workflow.

### Reusable asset families

Reusable families live under `asset_packs/`.

```text
assets/<domain>/<family>/
  INDEX.md
  README.md optional
  asset_packs/
    INDEX.md
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

The same package kind must use the same lane structure across the repo.

### Canon roots

Canon roots are explicit exceptions, not reusable family packages.

```text
assets/canon/patch/
  INDEX.md
  asset__hero__patch_style_bible.md
  reference_sheets/
    approved_style__v1.png
    general_drift_risks__v1.png
    scene_behaviour__v1.png
    style_drift_risks__v1_0.png
    style_drift_risks__v1_1.png
  role-kits/
    asset_packs/

assets/canon/style/
  INDEX.md
  reference_sheets/
    approved_patterns__v1.png
    environment_drift_risks__v1.png
    general_drift_risks__v1.png
    props_drift_risks__v1.png
```

Canon roots may remain outside `asset_packs/` when they are explicitly documented as canon roots. They still use local filenames.

## Allowed package lanes

- `source_images/`
- `compiled_asset_sheets/`
- `reference_sheets/`
- `manifests/`

The working `in-flight/` lane is not an `asset_packs/` lane and does not become canonical by path alone.

No active package should use `reference_sheets/` at the family root as a substitute for `asset_packs/`.

## Filename rules

- `source_images/` filenames are local inputs, such as `hero__v1.png` or `side_view__v1.png`.
- `compiled_asset_sheets/` filenames are local compiled-sheet labels, normally `sheet__vN.png`.
- `reference_sheets/` filenames are local sheet labels, such as `overview__v1.png` or `front_exterior__v1.png`.
- `in-flight/` filenames are local working-reference labels; they remain lane-qualified as in-flight until promoted elsewhere.
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

Repo-tracked validation lives at:

- `scripts/validate_asset_taxonomy.py`

The validator must check:

- every reusable family root has `asset_packs/`, unless it is an explicit canon root;
- every package has `manifests/manifest.json`;
- every manifest path exists;
- `source_images/` contains only local source images;
- `compiled_asset_sheets/` contains only local compiled sheets;
- `reference_sheets/` contains only local reference sheets;
- `in-flight/` contents are working references, not canonical package contents;
- no active filename is over-encoded with redundant package taxonomy;
- no stale moved path remains in indexes, manifests, registry, docs, or sample dispatches;
- no UTF-8 BOM exists in touched Markdown or JSON files;
- PNG count remains unchanged;
- PNG bytes remain unchanged.

The validator should report:

- families checked
- asset packs checked
- packages missing manifests
- manifest missing paths
- over-encoded PNG filenames
- lane mismatches
- stale references
- BOM files
- PNG counts

## Source zips and evidence

- `assets/source-zips/` stores canonical ingested input zips and one-time backfill bundles.
- `assets/evidence/` stores receipts, imports, transfers, and legacy provenance.

These lanes are separate from reusable asset packages.

## Operating rule

When a taxonomy migration changes a PNG path, update all affected indexes, manifests, docs, registry entries, and sample dispatches in the same batch.
