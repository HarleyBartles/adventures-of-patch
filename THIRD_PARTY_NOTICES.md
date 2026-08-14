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
- **Pinning:** The submodule is tracked by git; the current checkout is recorded in `.gitmodules` and the working tree. The installed snapshot is also recorded in `.agents/skills/.provenance.json`.
- **License:** governed by the upstream repository; see `.agents/plugins/marketplace-source/LICENSE`
- **Status:** repo-boundary

The skills installed under `.agents/skills/` are copied from this marketplace source, except the four `adventures-*` local skills. Their provenance and licensing are governed by the upstream repository and the per-plugin `SOURCE.md`, `references/bundle-manifest.json`, and `references/source-map.md` files in the submodule. The snapshot installed here is recorded in `.agents/skills/.provenance.json`.

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

### The Elements of Style (1918)

- **Path:** `.agents/skills/writing-with-clarity/assets/authority/reference-source/elements-of-style-1918/`
- **Source:** Project Gutenberg EBook #37134, https://www.gutenberg.org/ebooks/37134
- **License:** public domain
- **Authority record:** `.agents/skills/writing-with-clarity/assets/authority/CITATIONS.md`
- **Status:** verified

## Material needing audit before public release

### Visual and media assets

- **Paths:** `assets/`, `fairytales/`, `decks/`
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
4. Record skill provenance in `docs/project/provenance-skills.md`.

## Current status

This is a proper audit surface rather than an empty scaffold. The repository boundary and verified items are recorded. The visual and media asset audit and the per-skill marketplace summary remain thin surfaces for the next review pass.
