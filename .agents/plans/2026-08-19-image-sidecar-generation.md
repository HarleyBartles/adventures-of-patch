# Image sidecar generation

> **For agentic workers:** REQUIRED SUB-SKILL: Use `/subagent-driven-development` (recommended) or `/executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate `adventures.visual_sidecar.adjacent.v1` sidecar JSON for all 169 images that currently lack one, folder by folder, starting with a one-image proof.

**Architecture:** A new `tools/generate_image_sidecar.py` script creates a sidecar skeleton with deterministic image metadata (sha256, byte_size, dimensions, mime_type, mode, paths, and provenance). The agent then uses the `read` tool to inspect the actual pixels and writes the descriptive sections (summary, observed_visual_facts, positive_constraints, negative_constraints, sidecar_usage). Each slice is validated by `tools/validate_image_sidecars.py` and the repo's `ci` target before the next slice begins.

**Tech Stack:** Python 3.12, `json`, `hashlib`, `mimetypes`, `pathlib`, `struct`, `tools/validate_image_sidecars.py`, `py -3 tools/run.py ci --check`.

## Global Constraints

- Work in the `sidecar-generation` worktree on the `sidecar-generation` branch.
- Every new sidecar must be valid against `.agents/contracts/image-sidecar-provenance.schema.json` and pass `tools/validate_image_sidecars.py`.
- Every sidecar must use `adventures.visual_sidecar.adjacent.v1` and follow the existing sidecar style.
- Deterministic metadata (sha256, byte_size, dimensions, mime_type, mode) is derived by the generator script; descriptive text is written after pixel inspection.
- Provenance defaults to `generator: "unknown"`, `model: "unknown"`, `prompt_retained: false`, `prompt_unretained_note: "Provenance has not been determined for this image."` if the exact source is not known.
- `py -3 tools/run.py ci --check` must pass before any slice is committed.
- Do not hand-edit marketplace-derived `.agents/skills/*` files.

## Slice roadmap

| # | Slice | Images | Status |
|---|-------|--------|--------|
| 1 | `build/characters/shopkeeper/reference_sheets/` | 1 | ready |
| 2 | `style/patch/reference_sheets/` + `style/patterns/reference_sheets/` | 9 | pending |
| 3 | `build/templates/asset-sheets/` | 8 | pending |
| 4 | `build/environments/` (all subfolders) | 15 | pending |
| 5 | `build/characters/` remaining subfolders | 47 | pending |
| 6 | `build/canon/patch/role-kits/` + `build/canon/patch/` | 32 | pending |
| 7 | `build/adventures/Tournament/` | 34 | pending |
| 8 | `workbench/issue_48_override_heist_style_framework_v0_3/` remaining | 23 | pending |

Total: 169 images. The existing 13 sidecars are not touched.

---

## Phase 1: Proof slice (shopkeeper reference sheet)

### Task 1: Create the sidecar generator

**Files:**
- Create: `tools/generate_image_sidecar.py`

**Interfaces:**
- Consumes: one or more image file paths
- Produces: a `<image>-sidecar.json` skeleton in the same directory as each image

**Code skeleton:**

```python
#!/usr/bin/env python3
"""Generate sidecar skeletons for PNG images."""

import argparse
import hashlib
import json
import mimetypes
import os
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _png_info(path: Path) -> tuple[int, int, str]:
    with open(path, "rb") as f:
        if f.read(8) != b"\x89PNG\r\n\x1a\n":
            raise ValueError(f"{path} is not a PNG")
        f.read(4)  # length
        if f.read(4) != b"IHDR":
            raise ValueError(f"{path} has no IHDR")
        width, height = struct.unpack(">II", f.read(8))
        bit_depth, color_type = struct.unpack(">BB", f.read(2))
    mode_map = {0: "L", 2: "RGB", 3: "P", 4: "LA", 6: "RGBA"}
    return width, height, mode_map.get(color_type, f"unknown:{color_type}")


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def _mime(filename: str) -> str:
    return mimetypes.guess_type(filename, strict=False)[0] or "image/png"


def generate(image_path: Path) -> None:
    sidecar_path = image_path.with_name(image_path.stem + "-sidecar.json")
    if sidecar_path.exists():
        print(f"skip: {sidecar_path}")
        return
    width, height, mode = _png_info(image_path)
    rel = image_path.relative_to(ROOT)
    data = {
        "schema": "adventures.visual_sidecar.adjacent.v1",
        "project": "Adventures of Patch",
        "character": None,
        "sidecar_purpose": "TBD",
        "source_truth_note": "TBD",
        "runtime_use_note": "TBD",
        "do_not_infer_note": "TBD",
        "image": {
            "repo_image_path": str(rel.as_posix()),
            "relative_image_path": image_path.name,
            "repo_sidecar_path": str(rel.with_name(sidecar_path.name).as_posix()),
            "relative_sidecar_path": sidecar_path.name,
            "image_filename": image_path.name,
            "sha256": _sha256(image_path),
            "byte_size": os.path.getsize(image_path),
            "mime_type": _mime(image_path.name),
            "dimensions": {"width": width, "height": height},
            "mode": mode,
            "asset_role": "TBD",
            "acceptance_state": "TBD",
            "inspection_mode": "TBD",
            "confidence": "TBD",
            "provenance": {
                "generator": "unknown",
                "model": "unknown",
                "generated_at": None,
                "prompt_language": None,
                "prompt": None,
                "prompt_retained": False,
                "prompt_unretained_note": "Provenance has not been determined for this image.",
            },
        },
        "summary": "TBD",
        "observed_visual_facts": {"TBD": ["TBD"]},
        "positive_constraints": ["TBD"],
        "negative_constraints": ["TBD"],
        "sidecar_usage": {
            "best_for": ["TBD"],
            "not_sufficient_for": ["TBD"],
            "linear_view_route": None,
            "repo_index_tags": ["TBD"],
        },
    }
    with open(sidecar_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"wrote: {sidecar_path}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="+", help="PNG image paths")
    args = parser.parse_args()
    for image in args.images:
        generate(ROOT / image)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`tools/generate_image_sidecar.py` must:

- Accept a list of image paths on the command line.
- Compute and write the deterministic `image` fields: `repo_image_path`, `repo_sidecar_path`, `image_filename`, `relative_image_path`, `relative_sidecar_path`, `sha256`, `byte_size`, `mime_type`, `dimensions` (width, height), and `mode`.
- Add a `provenance` block with the default unknown values from the Global Constraints.
- Use `adventures.visual_sidecar.adjacent.v1` as the `schema`.
- Leave placeholders for descriptive fields that will be filled in after pixel inspection.
- Skip any image that already has a sidecar (no overwrites).

- [ ] **Step 1: Write `tools/generate_image_sidecar.py`**

- [ ] **Step 2: Test the generator on the proof image**

Run: `py -3 tools/generate_image_sidecar.py build/characters/shopkeeper/reference_sheets/three_view_sheet__v1.png`

Expected: creates `build/characters/shopkeeper/reference_sheets/three_view_sheet__v1-sidecar.json` with valid `image` metadata and a `provenance` block.

- [ ] **Step 3: Validate the generated skeleton**

Run: `py -3 tools/validate_image_sidecars.py build/characters/shopkeeper/reference_sheets/three_view_sheet__v1-sidecar.json`

Expected: `OK: 1 sidecar(s) validated`.

### Task 2: Write the proof sidecar from pixel inspection

**Files:**
- Modify: `build/characters/shopkeeper/reference_sheets/three_view_sheet__v1-sidecar.json`

**Interfaces:**
- Consumes: generated sidecar skeleton, observed image pixels
- Produces: completed sidecar with descriptive fields

- [ ] **Step 1: Inspect the image**

Open `build/characters/shopkeeper/reference_sheets/three_view_sheet__v1.png` with the `read` tool or an image viewer and record the observed visual facts.

- [ ] **Step 2: Fill the descriptive fields**

Complete `summary`, `observed_visual_facts`, `positive_constraints`, `negative_constraints`, `sidecar_usage`, and `repo_index_tags`. Use `published/fairytales/goldilocks/scene__just_right__v1-sidecar.json` as a style reference.

Example of a completed sidecar for a simple reference sheet:

```json
{
  "summary": "Canonical three-view reference sheet for the Identity Emporium shopkeeper. Front, side, and rear views show the shopkeeper's uniform, apron, prop posture, and customer-facing stance.",
  "observed_visual_facts": {
    "composition": [
      "Three-view character reference sheet arranged horizontally: front, side, and rear.",
      "The shopkeeper stands behind a compact counter with a few small props visible.",
      "The figure is posed neutrally, not in an action beat."
    ],
    "character_design": [
      "Canonical shopkeeper apron and cap.",
      "Friendly, approachable body language.",
      "Proportions consistent with the approved style guide."
    ]
  },
  "positive_constraints": [
    "Preserve the three-view layout for reference use.",
    "Keep the shopkeeper apron, cap, and counter props consistent.",
    "Use this image as a canonical shopkeeper reference."
  ],
  "negative_constraints": [
    "Do not add extra story beats or alternate costumes beyond the shown views.",
    "Do not use this single reference as final acceptance for derivative art without image QA."
  ],
  "sidecar_usage": {
    "best_for": [
      "Shopkeeper character reference and continuity.",
      "Prompting new shopkeeper images or scenes."
    ],
    "not_sufficient_for": [
      "Final acceptance of new generated images without image QA.",
      "Detailed prop or environment canon beyond the shown views."
    ],
    "linear_view_route": null,
    "repo_index_tags": [
      "character:shopkeeper",
      "asset:reference-sheet",
      "state:ready-for-qa"
    ]
  }
}
```

- [ ] **Step 3: Validate the completed sidecar**

Run: `py -3 tools/validate_image_sidecars.py build/characters/shopkeeper/reference_sheets/three_view_sheet__v1-sidecar.json`

Expected: `OK: 1 sidecar(s) validated`.

### Task 3: CI, commit, and publish the proof slice

**Files:**
- Create: `tools/generate_image_sidecar.py`
- Modify: `build/characters/shopkeeper/reference_sheets/three_view_sheet__v1-sidecar.json`

- [ ] **Step 1: Run the canonical CI check**

Run: `py -3 tools/run.py ci --check`

Expected: all checks pass, including the new sidecar validator.

- [ ] **Step 2: Commit the proof slice**

```bash
git add -A
git commit -m "Add sidecar generator and proof sidecar for shopkeeper reference sheet."
```

- [ ] **Step 3: Push the branch**

```bash
git push
```

- [ ] **Step 4: Mark slice 1 done in the roadmap**

Update this plan file's slice table to mark `build/characters/shopkeeper/reference_sheets/` as `done`, then amend or follow up with the update so the roadmap stays current.

---

## Next slices (just-in-time)

After the proof slice is approved, write a just-in-time plan for each remaining slice. Each slice reuses `tools/generate_image_sidecar.py` and follows the same generate/inspect/validate/commit pattern. Slices are executed in the same `sidecar-generation` branch and PR until all 169 images have sidecars.
