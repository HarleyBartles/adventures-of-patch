# Introducing Patch one-pager implementation plan

**Goal:** Produce and publish desktop and mobile one-pager PNGs introducing Patch, with deterministic text overlay, full sidecars, and the Adventures of Patch licence footer.

**Execution Strategy:** `manual`

## Global Constraints

- Output is a single PNG in both 16:9 and 9:16, text added with Pillow.
- Background is the same cream `#f7f4ec` as the Goldilocks fairytale page.
- Brand is "Adventures of Patch", not "PATCH FAIRYTALES".
- All sidecars and provenance created at asset creation time.
- `py -3 tools/run.py ci --check` passes before PR.

## Task 1: Generate source bases

- Use the OpenAI image generation MCP to create `source_images/page_base_desktop__v1.png` (2400x1344) and `source_images/page_base_mobile__v1.png` (1088x1920) on a cream background with Patch and no explanatory text.
- Fill sidecars for both source bases.

## Task 2: Build the deterministic composition script

- Create `tools/build_introducing_patch.py`.
- Overlay the brand label, title, subtitle, three info cards, and licence footer on desktop and mobile.
- Save `page__v1.png` and `page__v1-mobile.png`.

## Task 3: Sidecars and manifest

- Fill sidecars for the two finished pages.
- Create `manifests/manifest.json`.

## Task 4: Validation and PR

- Run `py -3 tools/run.py ci --check`.
- Commit, push, and open a PR.
- Move this plan and the spec to `completed/` in the same PR.
