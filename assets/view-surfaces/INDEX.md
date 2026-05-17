# assets/view-surfaces index

Durable GPT view-surface registry for repo-canonical image assets.

This directory exists so GPT can find a durable visual inspection surface for image files that live canonically in the repo. It is a machine-facing support surface, not a replacement for repo assets.

## Files in this directory

- `google-slides-registry.json` - machine-readable registry mapping repo image assets to canonical Google Slides view surfaces.
- `google-slides-registry.schema.json` - JSON schema and field contract for the registry.

## Subdirectories

None.

## Canonicality rules

- Repo PNGs and other committed image files remain canonical source truth.
- Google Slides entries are derived GPT view surfaces only.
- Asset-family indexes should not contain Google Slides links or per-image view-surface records.
- GPT should use `google-slides-registry.json` as the machine-readable lookup source for durable view surfaces.
- If a repo image changes blob SHA or source commit, GPT should update the existing canonical slide where possible and then refresh the registry entry for the new source fingerprint.
- Retired view-surface entries are exceptions, not BAU. Use them only when a source image is removed from the folder, a deck must be split/merged, or an old view container is being explicitly replaced.

## GPT operating procedure

When GPT needs to inspect a repo-canonical image:

1. Start from `assets/INDEX.md` and the relevant asset-family index.
2. Read `assets/view-surfaces/google-slides-registry.json`.
3. Look up the image by repo-relative path.
4. If the registry entry is present, status is `canonical`, and the recorded source fingerprint still matches the repo image, use the recorded Google Slides `presentation_id` and `slide_object_id` to render a slide thumbnail for visual inspection.
5. If the entry is missing, blocked, or stale, GPT may create or update the durable Google Slides view surface when the connected Google Drive/Slides tools are available.
6. After creating or updating a view slide, GPT must update `google-slides-registry.json` and commit the registry change so future sessions can find the same durable view surface.

## Deck lifecycle rules

- Maintain stable canonical Google Slides deck containers per asset folder.
- All view-surface deck names must assume future growth and include a numeric chunk suffix from creation, even when only one deck currently exists.
- Use the naming pattern `AOP View Surface — <Asset Family Name> -<deck_index>`, for example `AOP View Surface — Hero Patch -1`.
- Use one canonical deck for an asset folder when the folder has 1-10 images; that deck is still named with `-1`.
- If an asset folder has more than 10 images, decompose it into stable numbered deck chunks with at most 10 image slides per deck: `-1`, `-2`, `-3`, and so on.
- Reuse canonical deck containers for a folder. Do not create a fresh deck for every refresh when the existing deck can be updated.
- Use one slide per repo image. Do not compress multiple source images onto one canonical inspection slide.
- When an image changes but remains in the same asset folder, update the existing slide content and registry source fingerprint rather than creating a new deck shell.
- When an image is added to a folder with available deck capacity, add a new slide to the existing canonical deck and add a registry entry.
- When an image is removed from a folder, remove or clear the corresponding slide if the tool surface allows it, and mark or remove the registry entry according to the current evidence need.
- Only create a replacement deck when the existing deck is inaccessible, structurally corrupt, over the 10-image chunk limit, or explicitly superseded.
- Do not leave retired root-level or temporary proof decks as ordinary operating practice. If the tool surface cannot delete, rename, or move them, retire them from repo machine state and state the exact Drive cleanup blocker.

## View-surface creation rules

- Prefer one durable Google Slides presentation per asset family folder, chunked into max-10 image decks only when required.
- Use one slide per repo image revision.
- Insert the repo image into the slide at a readable size and preserve the image content.
- Record the source repo path, source commit SHA, source blob SHA, presentation ID, slide object ID, deck index, slide index, and image object ID if available.
- Do not treat a slide thumbnail URL as durable; use the presentation ID and slide object ID as the durable handle.
- Do not add human-facing slide links to ordinary asset indexes unless Harley explicitly asks for a human report.
