# Provenance: visual and media assets

This is a thin surface. It lists asset categories and what must be filled in before the repository is treated as publication-ready.

## Asset categories

- `build/adventures/` - adventure-specific asset packs
- `build/canon/` - canonical Patch style, role kits, and reference sheets
- `build/characters/` - character asset packs
- `build/environments/` - environment reference sheets
- `build/templates/` - asset sheet templates
- `style/patch/` - Patch style bible and reference sheets
- `style/patterns/` - general visual pattern and style reference sheets
- `published/adventures/` - finished presentation packages and deck artifacts
- `published/fairytales/` - one-page fairytale pages and scenes
- `workbench/` - active experiments and drafts; no licence is granted unless a specific written exception says otherwise

The accepted Heist Crew character references are first-class reusable assets at
`build/characters/heist-crew/`. Their adjacent sidecars preserve the provenance
actually known for each image; unknown generator or prompt details remain
unknown rather than being reconstructed. The promoted visual assets may use
the repository's established CC BY-ND 4.0 visual-asset licence, while the
characters, names, distinctive designs, world, stories, and branding remain
reserved under `LICENSING.md`.

The permission for `HarleyBartles/portfolio` to create and publish the six
specifically documented Heist Crew assent-marker derivatives is a bounded
exception recorded in `LICENSING.md` and the Override Heist assent-marker
bible. It does not license the rest of the workbench or broaden the source
assets' licence.

## To be filled in for each item

For each asset, image, zip, or deck:

- title or identifier
- file path
- author or generation tool (for example, image model, DALL-E, Midjourney, hand-drawn)
- license or terms of use
- any third-party source material embedded in the asset
- whether the asset is original project work, AI-generated, or derived from a third-party base

## Notes

- AI-generated images should record the model and prompt provenance if possible.
- PowerPoint files should record any embedded fonts, templates, or media that are not original.
- The old `assets/`, `fairytales/`, `decks/`, `assets/source-zips/`, `assets/evidence/receipts/`, and `assets/in-flight/` paths were removed or restructured into the four layers above during the repo-shape cleanup.
