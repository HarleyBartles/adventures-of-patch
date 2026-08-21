# Goldilocks mobile portrait page implementation plan

> **For agentic workers:** Use `/executing-plans` or manual execution. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a deterministic 1080 x 1920 portrait PNG mobile variant of the Goldilocks fairytale page using Pillow and the three approved source scenes.

**Architecture:** A single deterministic build script composes the source scenes, drawn text, and a lesson bar into a portrait canvas. The resulting image is sidecar-tracked and added to the package manifest.

**Tech Stack:** Python, Pillow, repo font fallback (`C:\Windows\Fonts\arial.ttf` / `arialbd.ttf`), `tools/generate_image_sidecar.py`, `tools/normalize_image_sidecars.py`, `tools/run.py ci --check`.

**Execution Strategy:** `manual` — the work is a single focused image build with one script.

## Global Constraints

- No image generation; only Pillow-style deterministic composition.
- Preserve all original wording.
- Maintain Patch canon and the same three source scenes.
- Pass `py -3 tools/run.py ci --check` before commit.

---

### Task 1: Create the deterministic build script

**Files:**
- Create: `tools/build_fairytale_mobile_page.py`

**Interfaces:**
- Consumes: `published/fairytales/goldilocks/scene__too_much__v1.png`, `scene__not_enough__v1.png`, `scene__just_right__v1.png`
- Produces: `published/fairytales/goldilocks/page__right_amount_of_guidance__v1-mobile.png`

- [ ] **Step 1:** Create `tools/build_fairytale_mobile_page.py` that loads the three source scenes.
- [ ] **Step 2:** Build a 1080 x 1920 canvas with the sampled color palette and header text.
- [ ] **Step 3:** Draw three stacked rows: image left (60% width), label + caption right (40% width).
- [ ] **Step 4:** Draw the "THE LESSON" bar at the bottom.
- [ ] **Step 5:** Save the PNG.

### Task 2: Generate sidecar and update manifest

**Files:**
- Modify: `published/fairytales/goldilocks/manifest.json`
- Create: `published/fairytales/goldilocks/page__right_amount_of_guidance__v1-mobile-sidecar.json`

- [ ] **Step 1:** Run `py -3 tools/generate_image_sidecar.py published/fairytales/goldilocks/page__right_amount_of_guidance__v1-mobile.png`.
- [ ] **Step 2:** Fill the generated sidecar semantic fields (project, purpose, summary, etc.).
- [ ] **Step 3:** Add `finished_page_mobile` to `manifest.json`.

### Task 3: Validate and commit

**Files:**
- Run: `py -3 tools/run.py ci --check`

- [ ] **Step 1:** Run `tools/run.py ci --check`.
- [ ] **Step 2:** Stage new/modified files.
- [ ] **Step 3:** Commit and push to a PR.
