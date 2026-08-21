# Introducing Patch one-pager design

## Problem

There is no canonical one-page introduction to Patch. New visitors who land on the portfolio site have no lightweight, self-contained page that explains who Patch is, what he represents, and how the Adventures of Patch stories work before they encounter a specific adventure or fairytale.

## Constraints

- Output is a single PNG page, delivered in both 16:9 landscape and 9:16 portrait.
- Must sit cleanly on the portfolio site with the same cream background used for the Goldilocks fairytale page.
- Text is added deterministically with Pillow, not baked into generated images.
- Generated images may only contain "in-universe" text (e.g. small marks on a prop), not explanatory prose.
- The design is an infographic-style character card, not a full scene.
- Sidecars and provenance must be created and maintained at asset creation time.
- The footer must include the Adventures of Patch brand and a short licence notice.

## Outputs

- `published/misc/introducing-patch/source_images/hero__v1.png`
- `published/misc/introducing-patch/page__v1.png` (2400 x 1350)
- `published/misc/introducing-patch/page__v1-mobile.png` (1080 x 1920)
- Adjacent sidecars for all three PNGs.
- `published/misc/introducing-patch/manifests/manifest.json`
- `tools/build_introducing_patch.py` deterministic layout builder.

## Brand

- Top brand label: "ADVENTURES OF PATCH" in teal.
- Page title: "Introducing Patch".
- Subtitle: "An autonomous software agent who makes workflows easy to follow."

## Visual design

### Source hero image

- One generated source image of Patch on the cream `#f7f4ec` background.
- Patch is shown in a friendly, mid-shot pose, slightly turned toward the viewer.
- He may carry or stand near a small prop cluster: his crossbody bag, a route card, and a folded plan or document.
- Only in-universe marks are allowed in the image (e.g. a small `>` on a document or the bag, if it reads naturally).
- The background is clean and untextured, matching the published page background so the pasted image blends seamlessly.

### Landscape page (2400 x 1350)

- Background `#f7f4ec`.
- Top-left: "ADVENTURES OF PATCH" in teal, 24 pt bold.
- Below it: "Introducing Patch" in dark, 56 pt bold.
- Below that: subtitle in dark, 32 pt regular.
- Patch placed slightly left of centre, taking up the left half of the page.
- Three rounded info cards to the right of Patch, stacked vertically with 20 px gaps:
  1. **What I am** — "A friendly autonomous software agent."
  2. **What I do** — "Turn agentic workflow ideas into small, followable stories."
  3. **How I learn** — "One clear next step at a time."
- Cards have a subtle dark outline, white fill, rounded corners, and 24 pt bold labels with 22 pt regular body text.
- Footer at the bottom-right in small dark text:
  - "Adventures of Patch and Patch and related characters are reserved."
  - "Images are CC BY-ND 4.0: free to share and inspect, not to modify or derive without permission."

### Portrait page (1080 x 1920)

- Same background and header.
- Patch centred near the top.
- The three info cards stacked vertically beneath Patch.
- Same footer at the bottom.

## Typography

- Fallback: `C:\Windows\Fonts\arial.ttf` and `arialbd.ttf`.
- Brand label: bold, 24 pt, teal `#0e8d84`.
- Title: bold, 56 pt, dark `#1d2b3a`.
- Subtitle: regular, 32 pt, dark.
- Card labels: bold, 24 pt, dark.
- Card body: regular, 22 pt, dark.
- Footer: regular, 16 pt, dark.

## Colors

- Background: `#f7f4ec`
- Dark text: `#1d2b3a`
- Teal: `#0e8d84`
- Card fill: `#ffffff`
- Card outline: `#1d2b3a`

## Image generation

- Use the repo MCP image-generation tool with the canonical Patch prompt from `style/patch/style-bible.md`.
- Prompt summary: clean editorial vector style, teal hoodie, hood up, off-white face panel, black oval eyes with small white shine highlights, dark trousers, teal shoes with white soles, teal crossbody bag with dark strap and white `>` mark. Pose is friendly and mid-shot, cream/off-white background, small route card and document props.
- The image must be saved as a source asset with an adjacent sidecar recording the exact prompt, generator, model, and pixel-inspected details.

## Sidecars

Each generated and composed PNG gets an `adventures.visual_sidecar.adjacent.v1` sidecar:
- `project`: "Adventures of Patch"
- `character`: "Patch"
- `asset_role`: `source_image` for `hero__v1.png`, `published_one_pager` for the finished pages.
- `acceptance_state`: `approved` once accepted.
- `inspection_mode`: `pixel_inspection`.
- `provenance`: exact prompt, model, generator, and `prompt_retained: true`.
- `summary`, `observed_visual_facts`, `positive_constraints`, `negative_constraints`, `sidecar_usage`.

## Deterministic build

`tools/build_introducing_patch.py`:
1. Load `published/misc/introducing-patch/source_images/hero__v1.png`.
2. Create 2400 x 1350 and 1080 x 1920 canvases.
3. Paste Patch into each layout.
4. Draw all text and rounded cards with Pillow.
5. Add the footer.
6. Save the two finished PNGs.
7. Generate sidecars for all three PNGs.
8. Update `manifest.json`.

## Validation

- `py -3 tools/run.py ci --check` passes.
- All sidecars validate.
- The two finished pages are normalised and diff-checked.
