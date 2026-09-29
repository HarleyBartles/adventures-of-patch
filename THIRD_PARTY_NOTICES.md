# Third-party and upstream licensing notices

This file is the repository-level audit surface for material that is not cleanly covered by the project-authored MIT or CC BY-ND defaults described in `LICENSING.md`.

The rule is simple: third-party, vendored, adapted, or upstream-derived material keeps the licence and attribution obligations that actually apply to it. The repository does not relicense material merely because it is checked in here.

## Status key

- `verified`: provenance and licence are recorded to a defensible baseline.
- `needs-review`: the item is known but the audit is not complete; fill in the linked thin surface before publication.
- `repo-boundary`: the item lives in a submodule and is governed by its own repository notices.

## Repository boundaries

### Agent asset marketplace

- **Path:** `.agents/plugins/marketplace-source`
- **Source:** https://github.com/HarleyBartles/agent-asset-marketplace
- **Pinning:** The submodule is tracked by git. Its exact source revision and deployed standard resources are recorded in `.agents/standards/provenance.json`.
- **License:** governed by the upstream repository; see `.agents/plugins/marketplace-source/LICENSE`
- **Status:** repo-boundary

Selected Agent Operating Model standard resources are deployed from this pinned source into `.agents/standards/`. Their provenance and content hashes are recorded in `.agents/standards/provenance.json`. Marketplace plugins are ambient and are not copied into this repository. Repository-owned skills under `.agents/skills/adventures-*/` are authored here.

For a repo-local summary, see `docs/project/provenance-skills.md`.

## Verified upstream material

### PyYAML

- **Package:** `pyyaml`
- **Version:** 6.0.3
- **Declared in:** `requirements.txt`
- **Source:** https://pyyaml.org/
- **License:** MIT
- **License text:** `LICENSES/PyYAML.txt`
- **Status:** verified

## Material needing audit before public release

### Visual and media assets

- **Paths:** `build/`, `style/`, `published/`, `workbench/`
- **Status:** needs-review
- **Notes:** Individual image, zip, and PPTX provenance must be confirmed. See `docs/project/provenance-assets.md`.

### Python dependencies beyond PyYAML

- **Path:** `requirements.txt`
- **Status:** needs-review
- **Notes:** If more dependencies are added, record them in `docs/project/provenance-dependencies.md`.

## How to update this audit

1. Do not classify uncertain provenance as first-party.
2. Record new dependencies in `docs/project/provenance-dependencies.md` and copy the license text to `LICENSES/`.
3. Record asset provenance in `docs/project/provenance-assets.md` and update this file to `verified`.
4. Record repository-owned skill and selected standards provenance in `docs/project/provenance-skills.md`.

## Current status

This is a proper audit surface rather than an empty scaffold. The repository boundary and verified items are recorded. The visual and media asset audit remains a thin surface for the next review pass.
