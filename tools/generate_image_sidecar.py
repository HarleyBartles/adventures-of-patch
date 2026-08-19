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


def _extract_base_project(image_path: Path) -> str:
    rel = image_path.relative_to(ROOT)
    # Use the second path component if it makes sense, otherwise Adventures of Patch
    if len(rel.parts) > 1:
        return "Adventures of Patch"
    return "Adventures of Patch"


def _extract_tags(image_path: Path) -> list[str]:
    rel = image_path.relative_to(ROOT).as_posix()
    tags = ["asset:image"]
    if "/characters/" in rel:
        tags.append("character")
    if "/environments/" in rel:
        tags.append("environment")
    if "/adventures/" in rel:
        tags.append("adventure")
    if "/canon/" in rel:
        tags.append("canon")
    if "/style/" in rel:
        tags.append("style-reference")
    if "/templates/" in rel:
        tags.append("template")
    if "/workbench/" in rel:
        tags.append("workbench")
    return tags


def generate(image_path: Path, force: bool = False) -> Path | None:
    sidecar_path = image_path.with_name(image_path.stem + "-sidecar.json")
    if sidecar_path.exists() and not force:
        print(f"skip: {sidecar_path}")
        return None
    width, height, mode = _png_info(image_path)
    rel = image_path.relative_to(ROOT)
    data = {
        "schema": "adventures.visual_sidecar.adjacent.v1",
        "project": _extract_base_project(image_path),
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
            "repo_index_tags": _extract_tags(image_path),
        },
    }
    with open(sidecar_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"wrote: {sidecar_path}")
    return sidecar_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate sidecar skeletons for PNG images.")
    parser.add_argument("images", nargs="+", help="PNG image paths")
    parser.add_argument("--force", action="store_true", help="overwrite existing sidecars")
    args = parser.parse_args()
    for image in args.images:
        generate(ROOT / image, force=args.force)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
