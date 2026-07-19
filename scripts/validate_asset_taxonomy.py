#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ASSETS_ROOT = REPO_ROOT / "assets"

LANES = {"source_images", "compiled_asset_sheets", "reference_sheets", "manifests"}
CANON_EXPLICIT_ROOTS = {
    ASSETS_ROOT / "canon" / "patch",
    ASSETS_ROOT / "canon" / "style",
}
CANON_REFERENCE_LANES = {
    ASSETS_ROOT / "canon" / "patch" / "reference_sheets",
    ASSETS_ROOT / "canon" / "style" / "reference_sheets",
}
REUSABLE_FAMILY_ROOTS = {
    ASSETS_ROOT / "characters",
    ASSETS_ROOT / "environments",
    ASSETS_ROOT / "adventures",
    ASSETS_ROOT / "canon" / "patch" / "role-kits",
}
TEXT_EXTENSIONS = {".md", ".json"}
STALE_REFERENCE_EXCLUDE_FILES: set[Path] = set()
LOCAL_REF_RE = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*__v\d+(?:_\d+)?\.png$")
SHEET_RE = re.compile(r"^sheet__v\d+(?:_\d+)?\.png$")
PNG_REF_RE = re.compile(r"(?P<path>(?:[A-Za-z]:[\\/])?(?:assets|Patch|docs|playbooks|skills)[^\"'\s)]+?\.png)")
INDEX_REF_RE = re.compile(r"`([^`]+)`")


def normalize_token(value: str) -> str:
    token = re.sub(r"[^a-z0-9]+", "_", value.lower())
    return token.strip("_")


def list_pngs() -> list[Path]:
    return sorted(path for path in ASSETS_ROOT.rglob("*.png") if path.is_file())


def index_entries(path: Path) -> tuple[list[str], list[str]]:
    files: list[str] = []
    subdirs: list[str] = []
    current: str | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            if stripped == "## Files in this directory":
                current = "files"
            elif stripped == "## Subdirectories":
                current = "subdirs"
            else:
                current = None
            continue
        if current not in {"files", "subdirs"}:
            continue
        for entry in INDEX_REF_RE.findall(line):
            if current == "files":
                files.append(entry)
            elif current == "subdirs":
                subdirs.append(entry)
    return files, subdirs


def package_files(package_root: Path) -> dict[str, list[str]]:
    result = {"source_images": [], "compiled_asset_sheets": [], "reference_sheets": []}
    for lane in result:
        lane_dir = package_root / lane
        if lane_dir.is_dir():
            result[lane] = sorted(p.name for p in lane_dir.glob("*.png"))
    return result


def manifest_path(package_root: Path) -> Path:
    return package_root / "manifests" / "manifest.json"


def package_metadata(package_root: Path) -> tuple[str, str, str]:
    rel = package_root.relative_to(ASSETS_ROOT)
    parts = rel.parts
    if parts[0] == "canon" and parts[1] == "patch" and parts[2] == "role-kits":
        return "canon", "patch", package_root.name
    if parts[0] in {"characters", "environments", "adventures"}:
        return parts[0], package_root.parent.parent.name, package_root.name
    return "", "", package_root.name


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def file_tokens_from_manifest(manifest: dict) -> dict[str, set[str]]:
    tokens: dict[str, set[str]] = {}
    for key in ("domain", "family", "package_id", "package_type", "status"):
        value = manifest.get(key)
        if isinstance(value, str):
            tokens[key] = {normalize_token(value)}
    return tokens


def collect_text_files() -> list[Path]:
    files: list[Path] = []
    skip_names = {".git", ".svn", ".hg"}
    for path in REPO_ROOT.rglob("*"):
        if any(part in skip_names for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS:
            files.append(path)
    return sorted(files)


def has_bom(path: Path) -> bool:
    with path.open("rb") as handle:
        return handle.read(3) == b"\xef\xbb\xbf"


def git_blob_sha(path: Path) -> str | None:
    try:
        output = subprocess.check_output(
            ["git", "ls-files", "-s", "--", str(path.relative_to(REPO_ROOT))],
            cwd=REPO_ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        return None
    if not output:
        return None
    return output.split()[1]


def sha256_bytes(path: Path) -> str:
    import hashlib

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Adventures of Patch asset taxonomy.")
    parser.add_argument("--json", action="store_true", help="Print JSON summary only.")
    args = parser.parse_args()

    pngs = list_pngs()
    png_paths = {path.relative_to(REPO_ROOT).as_posix() for path in pngs}

    families_checked: list[str] = []
    asset_packs_checked = 0
    top_level_reference_sheets_in_reusable_families: list[str] = []
    families_without_asset_packs: list[str] = []
    packages_missing_manifest: list[str] = []
    manifest_missing_paths: list[str] = []
    overencoded_png_filenames: list[str] = []
    lane_mismatches: list[str] = []
    stale_references: list[str] = []
    bom_files: list[str] = []
    semantic_mismatches_after: list[str] = []
    blocked_pngs: list[str] = []
    renamed_or_moved_files: list[str] = []
    syntax_failure_paths: set[str] = set()
    semantic_failure_paths: set[str] = set()

    # Family-root checks.
    family_roots = set()
    for pack_dir in ASSETS_ROOT.rglob("asset_packs"):
        if pack_dir.is_dir():
            family_roots.add(pack_dir.parent)
    family_roots.update(CANON_EXPLICIT_ROOTS)

    for family_root in sorted(family_roots):
        families_checked.append(family_root.relative_to(REPO_ROOT).as_posix())
        if family_root in CANON_EXPLICIT_ROOTS:
            continue
        if not (family_root / "asset_packs").is_dir():
            families_without_asset_packs.append(family_root.relative_to(REPO_ROOT).as_posix())
        if (family_root / "reference_sheets").is_dir():
            top_level_reference_sheets_in_reusable_families.append((family_root / "reference_sheets").relative_to(REPO_ROOT).as_posix())

    # Package checks.
    for asset_packs_dir in ASSETS_ROOT.rglob("asset_packs"):
        if not asset_packs_dir.is_dir():
            continue
        for package_root in sorted(p for p in asset_packs_dir.iterdir() if p.is_dir()):
            asset_packs_checked += 1
            rel_package_root = package_root.relative_to(REPO_ROOT).as_posix()
            domain, family, package_id = package_metadata(package_root)

            allowed_root_entries = {"INDEX.md", "README.md", "source_images", "compiled_asset_sheets", "reference_sheets", "manifests"}
            for child in package_root.iterdir():
                if child.name not in allowed_root_entries:
                    lane_mismatches.append(f"{rel_package_root}: unexpected package-root entry {child.name}")
                    semantic_failure_paths.add(rel_package_root)

            manifest_file = manifest_path(package_root)
            if not manifest_file.is_file():
                packages_missing_manifest.append(rel_package_root)
                semantic_failure_paths.add(rel_package_root)
                continue

            manifest = load_json(manifest_file)
            manifest_domain = normalize_token(str(manifest.get("domain", "")))
            manifest_family = normalize_token(str(manifest.get("family", "")))
            manifest_package_id = normalize_token(str(manifest.get("package_id", "")))

            if domain and manifest_domain and normalize_token(domain) != manifest_domain:
                semantic_mismatches_after.append(
                    f"{rel_package_root}: manifest domain {manifest.get('domain')!r} does not match package path domain {domain!r}"
                )
            if family and manifest_family and normalize_token(family) != manifest_family:
                semantic_mismatches_after.append(
                    f"{rel_package_root}: manifest family {manifest.get('family')!r} does not match package path family {family!r}"
                )
            if package_id and manifest_package_id and normalize_token(package_id) != manifest_package_id:
                semantic_mismatches_after.append(
                    f"{rel_package_root}: manifest package_id {manifest.get('package_id')!r} does not match package path package_id {package_id!r}"
                )

            files_block = manifest.get("files", {})
            lanes_block = manifest.get("artifact_lanes", {})
            for lane in ("source_images", "compiled_asset_sheets", "reference_sheets"):
                lane_dir = package_root / lane
                actual = sorted(p.name for p in lane_dir.glob("*.png")) if lane_dir.is_dir() else []
                expected = sorted(files_block.get(lane, [])) if isinstance(files_block, dict) else []
                if actual != expected:
                    semantic_mismatches_after.append(
                        f"{rel_package_root}: manifest file list for {lane} does not match directory contents"
                    )
                    lane_mismatches.append(f"{rel_package_root}: {lane} manifest mismatch")
                    semantic_failure_paths.add(rel_package_root)
                if lane == "compiled_asset_sheets":
                    for name in actual:
                        if not SHEET_RE.fullmatch(name):
                            overencoded_png_filenames.append(f"{(lane_dir / name).relative_to(REPO_ROOT).as_posix()}: compiled sheet must be sheet__vN.png")
                            syntax_failure_paths.add((lane_dir / name).relative_to(REPO_ROOT).as_posix())
                else:
                    for name in actual:
                        if not LOCAL_REF_RE.fullmatch(name):
                            overencoded_png_filenames.append(f"{(lane_dir / name).relative_to(REPO_ROOT).as_posix()}: filename must be local_name__vN.png")
                            syntax_failure_paths.add((lane_dir / name).relative_to(REPO_ROOT).as_posix())
                        if name.count("__") > 1:
                            overencoded_png_filenames.append(f"{(lane_dir / name).relative_to(REPO_ROOT).as_posix()}: filename is over-encoded")
                            syntax_failure_paths.add((lane_dir / name).relative_to(REPO_ROOT).as_posix())

            for lane in ("source_images", "compiled_asset_sheets", "reference_sheets"):
                lane_state = lanes_block.get(lane)
                lane_dir = package_root / lane
                lane_exists = lane_dir.is_dir()
                lane_has_pngs = any(lane_dir.glob("*.png")) if lane_exists else False
                if lane == "source_images" and lane_state == "present" and not lane_has_pngs:
                    semantic_mismatches_after.append(f"{rel_package_root}: source_images marked present but empty")
                    semantic_failure_paths.add(rel_package_root)
                if lane == "compiled_asset_sheets" and lane_state == "present" and not lane_has_pngs:
                    semantic_mismatches_after.append(f"{rel_package_root}: compiled_asset_sheets marked present but empty")
                    semantic_failure_paths.add(rel_package_root)
                if lane == "reference_sheets" and lane_state == "present" and not lane_has_pngs:
                    semantic_mismatches_after.append(f"{rel_package_root}: reference_sheets marked present but empty")
                    semantic_failure_paths.add(rel_package_root)

            # Manifest path existence checks.
            if isinstance(files_block, dict):
                for lane in ("source_images", "compiled_asset_sheets", "reference_sheets"):
                    lane_dir = package_root / lane
                    for filename in files_block.get(lane, []):
                        if not (lane_dir / filename).is_file():
                            manifest_missing_paths.append(f"{rel_package_root}:{lane}/{filename}")
                            semantic_failure_paths.add(f"{rel_package_root}:{lane}/{filename}")

            # Heuristic over-encoding check on path-local filenames.
            for lane in ("source_images", "compiled_asset_sheets", "reference_sheets"):
                lane_dir = package_root / lane
                if not lane_dir.is_dir():
                    continue
                for png_path in lane_dir.glob("*.png"):
                    rel_png = png_path.relative_to(REPO_ROOT).as_posix()
                    stem = png_path.name[:-4]
                    if lane == "compiled_asset_sheets":
                        if not SHEET_RE.fullmatch(png_path.name):
                            overencoded_png_filenames.append(f"{rel_png}: compiled_asset_sheets must use sheet__vN.png")
                            syntax_failure_paths.add(rel_png)
                    else:
                        if not LOCAL_REF_RE.fullmatch(png_path.name):
                            overencoded_png_filenames.append(f"{rel_png}: filename must use local_name__vN.png")
                            syntax_failure_paths.add(rel_png)
                    if stem.count("__") > 1:
                        overencoded_png_filenames.append(f"{rel_png}: filename contains redundant taxonomy slots")
                        syntax_failure_paths.add(rel_png)

    # Canon root checks.
    for canon_root in CANON_REFERENCE_LANES:
        if not canon_root.is_dir():
            continue
        for png_path in canon_root.glob("*.png"):
            rel_png = png_path.relative_to(REPO_ROOT).as_posix()
            if not LOCAL_REF_RE.fullmatch(png_path.name):
                overencoded_png_filenames.append(f"{rel_png}: canon reference filename must be local_name__vN.png")
                syntax_failure_paths.add(rel_png)
            if png_path.name[:-4].count("__") > 1:
                overencoded_png_filenames.append(f"{rel_png}: canon reference filename is over-encoded")
                syntax_failure_paths.add(rel_png)

    # Stale-reference sweep for text files.
    for text_path in collect_text_files():
        if text_path.is_relative_to(REPO_ROOT / "scratch"):
            continue
        if text_path in STALE_REFERENCE_EXCLUDE_FILES:
            continue
        if has_bom(text_path):
            bom_files.append(text_path.relative_to(REPO_ROOT).as_posix())
        try:
            text = text_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for match in PNG_REF_RE.finditer(text):
            raw = match.group("path").replace("\\", "/")
            raw = raw.rstrip(").,;")
            if raw.startswith("C:/") or raw.startswith("C:\\"):
                raw = raw.split(":/", 1)[-1]
            candidate = Path(raw)
            if not candidate.is_absolute():
                candidate = (REPO_ROOT / raw).resolve()
            if not candidate.exists():
                stale_references.append(f"{text_path.relative_to(REPO_ROOT).as_posix()}: {raw}")

    # PNG byte stability guard: report if any PNG in git is modified in content.
    # This is a best-effort heuristic for the active working tree.
    try:
        diff_output = subprocess.check_output(
            ["git", "diff", "--name-only", "--diff-filter=M", "--", "*.png"],
            cwd=REPO_ROOT,
            text=True,
        ).splitlines()
    except Exception:
        diff_output = []
    if diff_output:
        renamed_or_moved_files.extend(diff_output)

    summary = {
        "families_checked": len(families_checked),
        "asset_packs_checked": asset_packs_checked,
        "top_level_reference_sheets_in_reusable_families": top_level_reference_sheets_in_reusable_families,
        "families_without_asset_packs": families_without_asset_packs,
        "packages_missing_manifest": packages_missing_manifest,
        "manifest_missing_paths": manifest_missing_paths,
        "overencoded_png_filenames": sorted(set(overencoded_png_filenames)),
        "lane_mismatches": sorted(set(lane_mismatches)),
        "stale_references": sorted(set(stale_references)),
        "bom_files": sorted(set(bom_files)),
        "png_count_before": None,
        "png_count_after": len(pngs),
        "total_pngs_checked": len(pngs),
        "syntax_conforming_png_count": len(pngs) - len(syntax_failure_paths),
        "semantic_conforming_png_count": len(pngs) - len(semantic_failure_paths),
        "semantic_mismatches_after": sorted(set(semantic_mismatches_after)),
        "blocked_pngs": sorted(set(blocked_pngs)),
    }

    ok = not any(
        [
            summary["top_level_reference_sheets_in_reusable_families"],
            summary["families_without_asset_packs"],
            summary["packages_missing_manifest"],
            summary["manifest_missing_paths"],
            summary["overencoded_png_filenames"],
            summary["lane_mismatches"],
            summary["stale_references"],
            summary["bom_files"],
            summary["semantic_mismatches_after"],
            summary["blocked_pngs"],
            renamed_or_moved_files,
        ]
    )

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(json.dumps(summary, indent=2))
        print()
        print("Validation:", "passed" if ok else "failed")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
