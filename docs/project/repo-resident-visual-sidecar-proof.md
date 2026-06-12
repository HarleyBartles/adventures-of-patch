# Repo-Resident Visual Sidecar Proof

Status: repo-backed proof note for PATCH-21.
Date: 2026-06-12.

This note proves that the repo's tracked visual surfaces are carried by repo-resident sidecars or lane metadata. It does not promote any in-flight asset to canon.

## Sidecar Schema

The repo uses a small set of lane-specific sidecar shapes:

| Lane | Tracked visual surface | Required sidecar or index surface |
|---|---|---|
| Reusable asset packs | `assets/<domain>/<family>/asset_packs/<pack>/` | `manifests/manifest.json`, plus `INDEX.md` and usually `README.md` |
| Template asset sheets | `assets/templates/asset-sheets/` | Sibling JSON sidecars recorded beside each template PNG |
| Canon roots | `assets/canon/patch/reference_sheets/`, `assets/canon/style/reference_sheets/` | Canon root markdown plus the reference-sheet index mesh |
| In-flight working references | `assets/in-flight/` | Subtree `INDEX.md` and `README.md`, plus child `INDEX.md` files for each working folder |

The sidecar contract differs by lane, but the common rule is the same: the visual surface is never left floating without repo-resident metadata.

## Repository Proof

The current repository state contains:

- 173 tracked raster images across `assets/`.
- 18 reusable asset packs with `manifests/manifest.json`.
- 130 tracked images inside those reusable asset packs.
- 8 template PNGs with 8 matching JSON sidecars.
- 5 Patch canon reference PNGs.
- 4 style canon reference PNGs.
- 26 in-flight PNGs in the active style-framework working subtree.

Those counts are enough to show that the repo's tracked visual content is not relying on loose, untracked, or outside-repo sidecar state.

## Pack Coverage

The 18 reusable packs all resolve to repo-resident manifest-backed package roots:

- `assets/adventures/Tournament/asset_packs/judges-officials-acceptance-authority` - 7 images.
- `assets/adventures/Tournament/asset_packs/long-course-route-check-booth` - 5 images.
- `assets/adventures/Tournament/asset_packs/patch-bit-bot-tournament-kit` - 10 images.
- `assets/adventures/Tournament/asset_packs/tournament-trial-environments` - 13 images.
- `assets/canon/patch/role-kits/asset_packs/chef-role-kit` - 8 images.
- `assets/canon/patch/role-kits/asset_packs/cowboy-role-kit` - 8 images.
- `assets/canon/patch/role-kits/asset_packs/detective-role-kit` - 8 images.
- `assets/canon/patch/role-kits/asset_packs/mechanic-role-kit` - 8 images.
- `assets/characters/bit-bot/asset_packs/bit-and-bot` - 8 images.
- `assets/characters/bit-bot/asset_packs/bot-role-kit` - 13 images.
- `assets/characters/bouncers/asset_packs/bouncer-family` - 9 images.
- `assets/characters/mission-control-team/asset_packs/mission-control-team` - 6 images.
- `assets/characters/other-agents/asset_packs/other-agents` - 1 image.
- `assets/characters/shopkeeper/asset_packs/shopkeeper` - 1 image.
- `assets/characters/stakeholders/asset_packs/data-architect-product-trio` - 10 images.
- `assets/environments/club-db/asset_packs/club-db` - 5 images.
- `assets/environments/identity-emporium/asset_packs/identity-emporium` - 4 images.
- `assets/environments/mission-control/asset_packs/mission-control` - 6 images.

All 18 packs were checked by `scripts/validate_asset_taxonomy.py` against the repo's manifest contract.

## Template Sidecars

The asset-sheet template lane is also repo-resident and sidecar-driven:

- `assets/templates/asset-sheets/template_asset_sheet_1location_3view_v1.png`
- `assets/templates/asset-sheets/template_asset_sheet_1location_3view_v1.json`
- `assets/templates/asset-sheets/template_asset_sheet_1location_6view_v1.png`
- `assets/templates/asset-sheets/template_asset_sheet_1location_6view_v1.json`
- `assets/templates/asset-sheets/template_asset_sheet_3hero_6alt_v4.png`
- `assets/templates/asset-sheets/template_asset_sheet_3hero_6alt_v4.json`
- `assets/templates/asset-sheets/template_asset_sheet_4column_12equal_v1.png`
- `assets/templates/asset-sheets/template_asset_sheet_4column_12equal_v1.json`
- `assets/templates/asset-sheets/template_asset_sheet_4up_equal_header_v1.png`
- `assets/templates/asset-sheets/template_asset_sheet_4up_equal_header_v1.json`
- `assets/templates/asset-sheets/template_asset_sheet_process_sequence_6panel_v1.png`
- `assets/templates/asset-sheets/template_asset_sheet_process_sequence_6panel_v1.json`
- `assets/templates/asset-sheets/template_asset_sheet_prop_pack_12grid_v1.png`
- `assets/templates/asset-sheets/template_asset_sheet_prop_pack_12grid_v1.json`
- `assets/templates/asset-sheets/template_asset_sheet_world_overview_v1.png`
- `assets/templates/asset-sheets/template_asset_sheet_world_overview_v1.json`

Each JSON sidecar records the compile contract for the matching template PNG.

## Canon Root Proof

The explicit canon roots also carry their own repo-local documentation:

- `assets/canon/patch/asset__hero__patch_style_bible.md`
- `assets/canon/patch/reference_sheets/approved_style__v1.png`
- `assets/canon/patch/reference_sheets/general_drift_risks__v1.png`
- `assets/canon/patch/reference_sheets/scene_behaviour__v1.png`
- `assets/canon/patch/reference_sheets/style_drift_risks__v1_0.png`
- `assets/canon/patch/reference_sheets/style_drift_risks__v1_1.png`
- `assets/canon/style/asset__style__approved_styleguide.md`
- `assets/canon/style/reference_sheets/approved_patterns__v1.png`
- `assets/canon/style/reference_sheets/environment_drift_risks__v1.png`
- `assets/canon/style/reference_sheets/general_drift_risks__v1.png`
- `assets/canon/style/reference_sheets/props_drift_risks__v1.png`

These lanes do not use package manifests because they are explicit canon roots rather than reusable asset packs.

## Validation

Validation command run:

```bash
python scripts/validate_asset_taxonomy.py --json
```

Result:

- reusable package manifests present on every checked asset pack root;
- no missing manifest paths or lane mismatches;
- no over-encoded filenames;
- one stale absolute-path reference was corrected in `assets/in-flight/issue_48_override_heist_style_framework_v0_3/style-sheets/INDEX.md`.

## Conclusion

The repo already proves the visual-sidecar model in three different ways:

1. reusable packs use `manifests/manifest.json`;
2. templates use sibling JSON compile sidecars;
3. canon and in-flight lanes keep their own repo-resident documentation and index surfaces.

That is enough to show that the tracked repo images are not orphaned from their sidecar metadata.
