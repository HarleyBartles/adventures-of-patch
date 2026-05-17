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
- If a repo image changes blob SHA or source commit, the previous view surface is stale for the new revision until GPT creates or records a new canonical view slide.

## GPT operating procedure

When GPT needs to inspect a repo-canonical image:

1. Start from `assets/INDEX.md` and the relevant asset-family index.
2. Read `assets/view-surfaces/google-slides-registry.json`.
3. Look up the image by repo-relative path.
4. If the registry entry is present, status is `canonical`, and the recorded source fingerprint still matches the repo image, use the recorded Google Slides `presentation_id` and `slide_object_id` to render a slide thumbnail for visual inspection.
5. If the entry is missing, blocked, or stale, GPT may create or update the durable Google Slides view surface when the connected Google Drive/Slides tools are available.
6. After creating or updating a view slide, GPT must update `google-slides-registry.json` and commit the registry change so future sessions can find the same durable view surface.

## View-surface creation rules

- Prefer one durable Google Slides presentation per asset family.
- Use one slide per repo image revision.
- Insert the repo image into the slide at a readable size and preserve the image content.
- Record the source repo path, source commit SHA, source blob SHA, presentation ID, slide object ID, and image object ID if available.
- Do not treat a slide thumbnail URL as durable; use the presentation ID and slide object ID as the durable handle.
- Do not add human-facing slide links to ordinary asset indexes unless Harley explicitly asks for a human report.
