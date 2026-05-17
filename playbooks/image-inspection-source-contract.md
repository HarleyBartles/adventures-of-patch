# Image inspection source contract

This contract defines how GPT should visually inspect repo-canonical image assets.

## Source truth

Repo image files are canonical source truth. Asset-family indexes describe what images exist and what they are for.

Google Slides view surfaces are GPT's durable visual inspection surface for repo-canonical images. They are derived views, not source truth.

Source zips, project-source zips, source-package mirrors, and receipt packages are not the default image-inspection truth for GPT.

## Default inspection route

When GPT needs to inspect a repo-canonical image:

1. Start from `assets/INDEX.md`.
2. Read the relevant asset-family `INDEX.md`.
3. Read `assets/view-surfaces/google-slides-registry.json`.
4. Look up the repo-relative image path.
5. Use the recorded `presentation_id` and `slide_object_id` to render the Google Slides thumbnail or equivalent view surface.
6. Visually inspect the rendered slide image.

If the registry entry is missing, stale, blocked, or inconsistent with the repo image fingerprint, GPT should use the deterministic Slides view-surface deck workflow to create or update the deck and registry when the Google Drive/Slides and GitHub tools are available.

## Deck contract

- One image per slide.
- One stable deck per asset folder for folders with 1-10 images.
- Folders with more than 10 images split into stable numbered deck chunks with at most 10 image slides per deck.
- Deck names include the numeric suffix from creation, for example `AOP View Surface - Hero Patch -1`.
- The durable handle is `presentation_id` plus `slide_object_id`, not a transient thumbnail URL.

## Source zips and project sources

Source zips remain valid for bounded package work only:

- import or transfer bundle review;
- source package rebuild checks;
- receipt/evidence package handling;
- package integrity checks;
- explicit user-scoped zip inspection;
- emergency fallback when the Slides view-surface route is blocked and the reduced-confidence state is stated.

Do not inspect source zips or project-source visual packages as the ordinary way to view repo PNGs.

For now, project sources should contain only asset sheet template package(s), unless Harley explicitly changes that policy.

## False-green checks

A run is not green if it claims image inspection was complete because a source zip existed, a package was listed, a repo path was known, or a project-source package name matched.

A run may claim visual inspection only when GPT inspected a rendered image surface, normally through the Slides registry route.

If the Slides route is blocked, report the exact blocker and either stop or mark reduced confidence before using any package fallback.
