# Repo-Resident Visual Sidecar Proof

Status: repo-backed proof note for PATCH-21.
Date: 2026-06-12.

This note proves that the repo's tracked visual surfaces are carried by a repo-resident image-sidecar mesh. It does not promote any in-flight asset to canon.

## Sidecar Schema

The repo uses a small set of lane-specific sidecar shapes:

| Lane | Tracked visual surface | Sidecar or index surface |
|---|---|---|
| Reusable asset packs | `assets/<domain>/<family>/asset_packs/<pack>/` | `manifests/manifest.json`, plus package indexes and readmes |
| Template asset sheets | `assets/templates/asset-sheets/` | Sibling JSON compile sidecars beside each template PNG |
| Canon roots | `assets/canon/patch/reference_sheets/`, `assets/canon/style/reference_sheets/` | Canon root markdown plus the reference-sheet index mesh |
| In-flight working references | `assets/in-flight/` | Subtree `INDEX.md` and `README.md`, plus child `INDEX.md` files for each working folder |
| Repo image selection mesh | `assets/visual-sidecars/` | `schema.v0.1.json`, `index.v0.1.json`, and sharded records keyed by tracked image path |

The sidecar contract differs by lane, but the common rule is the same: the visual surface is never left floating without repo-resident metadata. The new repo image-selection mesh is the durable routing layer PATCH-21 asked for.

## Repository Proof

The current repository state contains:

- 173 tracked image files discovered from `git ls-files` across `*.png`, `*.jpg`, and `*.jpeg`.
- 172 tracked PNGs and 1 tracked JPEG.
- `assets/visual-sidecars/schema.v0.1.json`.
- `assets/visual-sidecars/index.v0.1.json`.
- 40 shard JSON records under `assets/visual-sidecars/shards/`.

Those files show that the repo's tracked visual content is no longer relying on loose, unindexed metadata. It has a dedicated, repo-resident selection/routing layer that maps image path to machine-legible sidecar record.

## Shard Coverage

The shard mesh covers the tracked image inventory by source directory. Representative shard families include:

- `assets/adventures/Tournament/asset_packs/judges-officials-acceptance-authority/source_images` -> `assets/visual-sidecars/shards/shard__assets_adventures_tournament_asset_packs_judges_officials_acceptance_authority_source_images__v0_1.json`
- `assets/canon/patch/reference_sheets` -> `assets/visual-sidecars/shards/shard__assets_canon_patch_reference_sheets__v0_1.json`
- `assets/canon/patch/role-kits/asset_packs/cowboy-role-kit/source_images` -> `assets/visual-sidecars/shards/shard__assets_canon_patch_role_kits_asset_packs_cowboy_role_kit_source_images__v0_1.json`
- `assets/characters/bit-bot/asset_packs/bot-role-kit/source_images` -> `assets/visual-sidecars/shards/shard__assets_characters_bit_bot_asset_packs_bot_role_kit_source_images__v0_1.json`
- `assets/environments/mission-control/asset_packs/mission-control/reference_sheets` -> `assets/visual-sidecars/shards/shard__assets_environments_mission_control_asset_packs_mission_control_reference_sheets__v0_1.json`
- `assets/in-flight/issue_48_override_heist_style_framework_v0_3/style-sheets` -> `assets/visual-sidecars/shards/shard__assets_in_flight_issue_48_override_heist_style_framework_v0_3_style_sheets__v0_1.json`
- `assets/templates/asset-sheets` -> `assets/visual-sidecars/shards/shard__assets_templates_asset_sheets__v0_1.json`

## Validation

Validation command run:

```bash
python scripts/validate_asset_taxonomy.py --json
```

Result:

- `git ls-files` inventory counted 173 tracked image files;
- `assets/visual-sidecars/` was generated from that inventory;
- each shard maps to real tracked image paths;
- no image binaries were changed;
- `scripts/validate_asset_taxonomy.py --json` still passes after the sidecar mesh was added;
- semantic pixel inspection remains unavailable in this worker shell, so visual-facts fields are honestly marked metadata-only.

## Conclusion

PATCH-21 is now satisfied at the level the PR comment asked for: the repo has a discoverable image-sidecar selection mesh keyed by tracked image path, with a schema, a global index, and shard files that future GPT work can use for routing and text constraint selection without pretending the sidecars are visual canon.
