# asset_class__hero__patch_approved_style.png chunk package

This folder contains plain-text chunks for the canonical Patch contact-sheet PNG.

Reconstruction rule: concatenate the files in `chunks/` in lexical order, decode the resulting base64 text, and treat the decoded bytes as the PNG image.

## Files in this directory

- `INDEX.md` - package description and reconstruction note.
- `manifest.json` - provenance and chunk layout metadata.

## Subdirectories

- `chunks/` - ordered base64 text slices for the PNG image.
