#!/usr/bin/env python3
"""Validate image sidecars for schema, provenance, and path/metadata consistency."""

import argparse
import hashlib
import json
import mimetypes
import os
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / ".agents/contracts/image-sidecar-provenance.schema.json"
IMAGE_LANES = ("build", "style", "published", "workbench")


def _png_dimensions(path: Path) -> tuple[int, int]:
    with open(path, "rb") as f:
        # PNG signature is 8 bytes, then IHDR chunk
        sig = f.read(8)
        if sig != b"\x89PNG\r\n\x1a\n":
            raise ValueError(f"{path} is not a PNG")
        length = struct.unpack(">I", f.read(4))[0]
        chunk_type = f.read(4)
        if chunk_type != b"IHDR":
            raise ValueError(f"{path} has no IHDR chunk")
        if length != 13:
            raise ValueError(f"{path} has unexpected IHDR length")
        width, height = struct.unpack(">II", f.read(8))
        return width, height


def _expected_mime(filename: str) -> str:
    return mimetypes.guess_type(filename, strict=False)[0] or "image/png"


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate(sidecar_path: Path, schema: dict) -> list[str]:
    errors = []
    data = load_json(sidecar_path)
    image = data.get("image", {})
    provenance = image.get("provenance")

    if not provenance:
        errors.append(f"{sidecar_path}: missing image.provenance")
        return errors

    for key in schema.get("required", []):
        if provenance.get(key) is None and key in ("generator", "model"):
            errors.append(f"{sidecar_path}: image.provenance.{key} is required")
        elif key == "prompt_retained" and "prompt_retained" not in provenance:
            errors.append(f"{sidecar_path}: image.provenance.prompt_retained is required")

    if not provenance.get("prompt_retained") and not provenance.get("prompt_unretained_note"):
        errors.append(f"{sidecar_path}: prompt_unretained_note is required when prompt_retained is false")

    repo_image = ROOT / image.get("repo_image_path", "")
    repo_sidecar = ROOT / image.get("repo_sidecar_path", "")

    if not repo_image.exists():
        errors.append(f"{sidecar_path}: repo_image_path does not resolve: {image.get('repo_image_path')}")
    if not repo_sidecar.exists():
        errors.append(f"{sidecar_path}: repo_sidecar_path does not resolve: {image.get('repo_sidecar_path')}")

    actual = repo_image
    if not actual.exists():
        return errors

    if "sha256" in image and _sha256(actual) != image["sha256"]:
        errors.append(f"{sidecar_path}: sha256 mismatch")
    if "byte_size" in image and os.path.getsize(actual) != image["byte_size"]:
        errors.append(f"{sidecar_path}: byte_size mismatch")
    if "dimensions" in image:
        try:
            width, height = _png_dimensions(actual)
            if image["dimensions"].get("width") != width or image["dimensions"].get("height") != height:
                errors.append(f"{sidecar_path}: dimensions mismatch")
        except (OSError, ValueError) as e:
            errors.append(f"{sidecar_path}: cannot read dimensions: {e}")
    if "mime_type" in image and _expected_mime(actual.name) != image["mime_type"]:
        errors.append(f"{sidecar_path}: mime_type mismatch")

    return errors


def find_sidecars() -> list[Path]:
    sidecars = []
    for lane in IMAGE_LANES:
        sidecars.extend(sorted((ROOT / lane).rglob("*-sidecar.json")))
    return sidecars


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate image sidecars.")
    parser.add_argument("paths", nargs="*", help="optional sidecar paths to validate; if omitted, scans all lanes")
    args = parser.parse_args(argv)

    schema = load_json(SCHEMA)
    sidecars = [Path(p) for p in args.paths] if args.paths else find_sidecars()
    sidecars = [p.resolve() if p.is_absolute() else (ROOT / p) for p in sidecars]

    errors = []
    for sidecar_path in sidecars:
        if not sidecar_path.exists():
            errors.append(f"{sidecar_path}: file not found")
            continue
        errors.extend(validate(sidecar_path, schema))

    if not sidecars:
        print("warning: no sidecars found")

    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        return 1

    print(f"OK: {len(sidecars)} sidecar(s) validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
