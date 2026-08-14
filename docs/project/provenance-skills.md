# Provenance: installed skills

This is a thin surface. It records the marketplace-derived skills installed in this repository and notes what still needs to be filled in for a complete audit.

## Marketplace-derived skills

Installed from the agent-asset-marketplace submodule via the plugins listed in `.agents/plugins/marketplace.json`.

- `repo-worker-pack`
- `superpowers-plus`
- `mcp-usage-pack`

The exact list of installed skills and the source commit are in `.agents/skills/.provenance.json`.

## To be filled in

For each installed skill in `.agents/skills/`, record:

- skill name
- source plugin and upstream repository
- `content_mode` (verbatim or adapted)
- `source_author`
- `source_license`
- `source_repo`
- `source_path` inside the marketplace submodule
- whether any adaptation was done in this repository

The canonical source for this data is the per-plugin `references/bundle-manifest.json` and `SOURCE.md` under `.agents/plugins/marketplace-source/codex-marketplace/plugins/`.

## Local skills

The following skills are owned by this repository and are not marketplace-derived:

- `adventures-image-qa`
- `adventures-project-doctrine`
- `adventures-project-readiness`
- `adventures-visual-preproduction`
