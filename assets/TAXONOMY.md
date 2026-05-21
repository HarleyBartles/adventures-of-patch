# Asset Taxonomy Contract

This contract defines the target asset taxonomy for Adventures of Patch and the rules that govern future migration batches.

The repo's current folder layout remains in place until a migration batch explicitly moves paths. This document locks the destination shape, the boundary rules, and the order of operations so later moves can be staged safely.

## Purpose

- Separate reusable canon from adventure-scoped packs.
- Separate canonical repo images from derived inspection surfaces.
- Separate canonical input zips from ad hoc mirror-generation workflows.
- Give Patch and GPT a deterministic contract for where new assets belong.
- Preserve rollbackability by keeping the taxonomy explicit before any moves begin.

## Current migration posture

- This is a docs-first contract stage.
- No asset files are moved by this document.
- Current roots remain live until a later batch migrates them.
- `source-zips` remains first-class, but only as a canonical input-zip and one-time backfill storage lane organized by asset taxonomy category.
- `png_chunks` has been retired and is no longer an operating root.
- `assets/canon/patch/reference_sheets/` is the live home for Patch canon reference, interaction, and anti-pattern sheets.
- `assets/canon/style/reference_sheets/` is the live home for the style-system pattern and anti-pattern sheets.
- `assets/canon/patch/role-kits/asset_packs/` is the live home for Patch role-kit packages.
- `assets/characters/<family>/asset_packs/` is the live home for character-family packages.
- `assets/adventures/<family>/asset_packs/` is the live home for adventure-scoped packages.
- `assets/views/` is the future name for the current view-surface registry root, but the on-disk path is not renamed in this dispatch.
- `assets/evidence/receipts/` is the live evidence lane for receipt bundles and migrated receipt packages.
- `assets/packs/issue-*` remains the future home for issue-scoped adventure packs.

## Asset sheet, source image, and in-flight reference distinction

The repo uses these terms with specific meaning:

- `asset_sheet` - a compiled or rendered PNG sheet that presents an approved asset family, character set, prop pack, environment pack, role kit, or visual kit.
- `source_images` - approved individual PNG images used to construct a compiled asset sheet or completed asset pack.
- `in_flight_references` - accepted, candidate, or reviewed images for an adventure or asset pack that have not yet been compiled into a completed asset sheet or promoted into an approved `source_images` set.
- `view_surfaces` - derived GPT inspection surfaces, such as Google Slides registry entries or other visual mirrors of repo-canonical images.

Contract rules:

- Source images are the panel inputs for generated contact sheets.
- Compiled asset sheets are included full-size in visual-intake zips when requested.
- Compiled asset sheets are never used as contact-sheet panels.
- In-flight references may be included full-size for GPT visual grounding, but they remain distinct from completed `source_images` until promoted.
- View surfaces are not canonical image truth.
- Registry or path changes for view surfaces happen only when the underlying repo paths move.

Contact-sheet decision table:

- source images + compiled asset sheet -> generate a contact sheet from source images only, and include the compiled asset sheet separately in full.
- source images only -> generate a contact sheet from source images.
- compiled asset sheet only -> include the asset sheet in full; do not generate a fake contact sheet made from asset sheets.
- in-flight references -> include full-size or as an explicitly in-flight visual packet when needed; do not silently classify as completed `source_images`.
- neither source images nor asset sheet resolves -> record unresolved/skipped with reason; do not invent paths.

## Canonical roots

Target taxonomy roots:

- `assets/canon/`
- `assets/worlds/`
- `assets/characters/`
- `assets/environments/`
- `assets/props/`
- `assets/packs/`
- `assets/templates/`
- `assets/views/`
- `assets/source-zips/`
- `assets/evidence/`

## Root boundary rules

- `assets/canon/patch/` is global Patch visual canon.
- `assets/canon/patch/reference_sheets/` is the live Patch canon reference-sheet lane for approved style, anti-pattern, and interaction PNGs.
- `assets/canon/patch/role-kits/asset_packs/` is the active home for Patch role-kit packages.
- `assets/canon/style/` is global Adventures style canon.
- `assets/canon/style/reference_sheets/` is the live style-system reference-sheet lane for patterns and anti-patterns.
- `assets/characters/<family>/asset_packs/` is the active home for current asset-pack families.
- `assets/environments/<family>/asset_packs/` is the active home for environment-pack families.
- `assets/adventures/<family>/asset_packs/` is the active home for adventure-scoped packs.
- `assets/worlds/` holds reusable world bibles, style frames, and setting grammar.
- `assets/characters/` holds reusable non-Patch character families and individual characters.
- `assets/characters/heist-crew/` is the target path for the heist crew family.
- `assets/environments/` holds reusable locations and location families.
- `assets/props/` holds reusable props, continuity objects, and stateful hero props.
- `assets/packs/` holds issue-scoped adventure packs, planning, bibles, manifests, and accepted or rejected references.
- `assets/templates/` holds deterministic templates, layout specs, and pack-manifest templates.
- `assets/views/` holds derived GPT view-surface registry material, not canonical repo assets.
- `assets/views/` and the current live `assets/view-surfaces/` registry are derived inspection surfaces, not canonical assets.
- `assets/source-zips/` holds canonical ingested input zips and one-time backfill zips, organized by category folders.
- `assets/evidence/` holds receipts, imports, transfers, and legacy provenance that is not the canonical input zip.

## Naming rules

- Use short, human-readable folder names.
- Keep Patch role kits under `assets/canon/patch/role-kits/asset_packs/`.
- Keep issue packs under `assets/packs/issue-*`.
- Prefer family names that match the real reusable concept, not legacy class prefixes.
- Preserve the `heist-crew` name exactly.
- Do not introduce new first-class roots for ad hoc package generation.

## Index rules

- Every visible folder must have an `INDEX.md`.
- Indexes list only direct children that really exist.
- Parent indexes must point to existing child indexes.
- No index may point to a path that does not exist yet.
- Future-shape paths belong in contract text until the migration batch creates them.
- If a registry or index points at a moved image, it must be updated in the same batch as the move.

## Canonical asset-pack zip contract

GPT-produced asset packs must use a deterministic zip layout so Patch can validate and ingest them without guessing.

```text
asset-pack.zip
  manifest.json
  README.md
  asset/
    INDEX.md
    bible.md                  # optional when applicable
    sheet.png                 # required for asset-sheet packages
    sheet_spec.json           # required when deterministically compiled
    sidecar.md or sidecar.json
  source_images/
    ...accepted source images used in the sheet...
  accepted/
    ...accepted references, if distinct from source_images...
  rejected/
    ...only when explicitly included for evidence...
  evidence/
    ...receipts, import notes, provenance, or QA notes when needed...
```

Minimum manifest fields:

- `pack_id`
- `pack_type`
- `target_asset_root`
- `source_issue`
- `created_by`
- `created_at`
- `asset_status`
- `intended_repo_paths`
- `included_files`
- `source_images`
- `asset_sheet`
- `qa_status`
- `template_version`
- `extraction_instructions`
- `do_not_promote_without`

Required pack types:

- `character-family`
- `individual-character`
- `environment-family`
- `location`
- `prop-family`
- `stateful-hero-prop`
- `world-style`
- `adventure-pack`
- `visual-bible-pack`
- `template-pack`

For completed packs, the manifest should identify the compiled asset sheet separately from the source image set. For asset-sheet-only packs, the manifest should make it explicit that the pack is represented only by the full compiled sheet and has no contact-sheetable source-image set yet. In-flight reference packets should remain labeled as in-flight until promoted.

## Source-zips policy

- `assets/source-zips/` remains first-class.
- It stores canonical ingested input zips and one-time cleanup/backfill zips.
- It is not an ad hoc mirror-generation lane.
- Patch must not routinely regenerate mirror zips after extraction.
- The original input zip is preserved and catalogued after validation and extraction.
- Existing tracked zip files may still reflect legacy mirror semantics until their migration batch reclassifies them.
- Do not delete unique evidence without provenance review.

## Patch ingest/catalogue flow

Patch execution for a canonical asset pack zip should follow this order:

1. Receive the canonical asset-pack zip.
2. Validate the manifest and zip shape.
3. Classify the pack type and target root.
4. Extract the files into the repo taxonomy.
5. Preserve the original input zip in the correct `assets/source-zips/` category.
6. Update the affected indexes.
7. Update `assets/views/google-slides-registry.json` only when repo images are present and a view surface is being created or refreshed.
8. Return the changed paths, the stored zip path, validation results, and publication proof.

## Evidence policy

- `assets/evidence/` is the home for receipts, imports, transfers, and legacy provenance that is not itself the canonical input zip.
- `assets/evidence/receipts/` is the live root for receipt packages.
- Receipt content should remain distinguishable from canonical input zips.
- The extra `assembly/` tree in `hero-patch.zip` is not protected by default; keep it only if dependency evidence proves it is still needed.

## View-surface registry policy

- `assets/view-surfaces/` is the current live registry root.
- `assets/views/` is the future target name.
- Repo images remain canonical source truth.
- Google Slides entries are derived inspection surfaces.
- Registry path updates must happen in the same migration batch as any image path move.
- Do not update registry paths for unmoved files.
- Do not leave the registry pointing at old image paths after a move.

## png_chunks retirement policy

- `assets/png_chunks/` has been retired and removed as a live root.
- Do not create new chunk packages as a normal workflow.
- Do not revive the lane as a first-class operating path.
- If any minimal provenance must survive in the future, preserve only the minimum necessary record under `assets/evidence/legacy/`.

## Reusable vs adventure-specific promotion rules

- Promote to reusable roots only when an asset family is genuinely reusable.
- Keep adventure-scoped planning, accepted/rejected references, and manifests in `assets/packs/issue-*`.
- Reusable assets may be referenced from packs, but packs should not duplicate reusable canon unless a deliberate packaged snapshot is required.
- Do not promote one-off scene art into reusable canon just to simplify navigation.

## Local folder shapes

### Canon

```text
assets/canon/
  patch/
    reference_sheets/
    role-kits/
      asset_packs/
  style/
    reference_sheets/
```

### Characters

```text
assets/characters/
  bit-bot/
    asset_packs/
    reference_sheets/
  mission-control-team/
    reference_sheets/
  stakeholders/
    asset_packs/
  shopkeeper/
    reference_sheets/
  bouncers/
    reference_sheets/
  other-agents/
    reference_sheets/
  heist-crew/
```

### Adventures

```text
assets/adventures/
  Tournament/
    asset_packs/
    source_images/
```

### Environments

```text
assets/environments/
  mission-control/
    reference_sheets/
  identity-emporium/
    reference_sheets/
  override-safehouse/
  tournament-grounds/
  club-db/
    reference_sheets/
```

### Props

```text
assets/props/
  route-cards/
  override-keycard/
  vault-interface/
  medals-podiums-trophies/
  task-packets/
  receipts-and-audit/
  rollback-and-recovery/
```

### Packs

```text
assets/packs/
  issue-37-identity-emporium/
  issue-47-tournament-defaults/
  issue-48-override-heist/
```

### Templates

```text
assets/templates/
  asset-sheets/
  style-bibles/
  pack-manifests/
```

### Views

```text
assets/views/
  INDEX.md
  google-slides-registry.json
  google-slides-registry.schema.json
```

### Source zips

```text
assets/source-zips/
  canon/
  worlds/
  characters/
  environments/
  props/
  packs/
  templates/
  legacy/
```

### Evidence

```text
assets/evidence/
  receipts/
  imports/
  transfers/
  legacy/
```

## Migration batches

- Batch 0: taxonomy contract only, no asset moves.
- Batch 1: GPT-native canonical asset-pack zip skill update plan.
- Batch 2: low-risk pilot move, completed here as `assets/style/` to `assets/canon/style/`.
- Batch 3: evidence and source-zip structure cleanup without deleting unique evidence.
- Batch 4: reusable character and environment family moves in small batches.
- Batch 5: adventure pack migration and scaffolding for issues `#37`, `#47`, and `#48`.
- Batch 6: Patch canon migration last, after path, registry, and skill updates are proven.
- Batch 7: `png_chunks` retirement and old legacy mirror cleanup after reference audit.

## Rollback and validation

- Each batch must be small.
- Each batch must use tracked moves or an equivalent explicit move plan.
- Each batch must run stale-reference sweeps.
- Each batch must validate indexes and registry entries.
- Each batch must be reversible by `git revert`.
- No batch is green if an index points at a missing path.
- No batch is green if a registry still points at a moved image path.
- No batch is green if unique provenance was deleted without review.

## Skill/playbook follow-up requirements

### GPT-native skill follow-up

- Update GPT-native asset-pack-producing skills so their output zips always use the canonical layout.
- Likely affected skills include asset-sheet compilation, visual-bible creation, visual-preproduction, receipt ingestion, repo navigation, and dispatch-prep workflows.

### Repo-resident Patch skill follow-up

- Update Patch asset zip ingress to validate, extract, catalogue, and preserve canonical input zips.
- Update Patch asset directory source packager to become cleanup/backfill-only or retire it if no longer needed.
- Remove or rewrite any Patch workflow text that still treats `source-zips` as an ad hoc mirror lane.
