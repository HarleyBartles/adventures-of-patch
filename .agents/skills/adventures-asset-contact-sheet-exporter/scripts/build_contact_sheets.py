from __future__ import annotations

import argparse
import json
import math
import sys
import textwrap
import zipfile
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageOps


REQUEST_TYPE = "asset_contact_sheet_export"
PROJECT = "adventures-of-patch"
SOURCE_REPO = "HarleyBartles/adventures-of-patch"
FIXED_ZIP_DATE_TIME = (1980, 1, 1, 0, 0, 0)


@dataclass
class InputRecord:
    family_id: str
    record_type: str
    source_path: str
    resolved_path: Path
    sheet_name: str | None = None
    sheet_index: int | None = None
    panel_index: int | None = None
    panel_slot: int | None = None
    visible_label: str | None = None


@dataclass
class FamilyResult:
    family_id: str
    reason: str
    source_contact_sheet_generated: bool = False
    source_contact_sheet_reason: str | None = None
    source_records: list[InputRecord] = field(default_factory=list)
    asset_sheet_records: list[InputRecord] = field(default_factory=list)
    reference_sheet_records: list[InputRecord] = field(default_factory=list)
    rendered_source_contact_sheets: list[str] = field(default_factory=list)
    included_existing_assets: list[str] = field(default_factory=list)
    skipped: list[dict[str, Any]] = field(default_factory=list)
    sheet_files: list[str] = field(default_factory=list)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[4]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dump_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")


def slugify(value: str) -> str:
    chars: list[str] = []
    previous_dash = False
    for char in value.lower():
        if char.isalnum():
            chars.append(char)
            previous_dash = False
        else:
            if not previous_dash:
                chars.append("-")
                previous_dash = True
    slug = "".join(chars).strip("-")
    return slug or "sheet"


def short_repo_path(path: str, limit: int = 48) -> str:
    if len(path) <= limit:
        return path
    parts = Path(path).parts
    if len(parts) <= 2:
        return path[: max(0, limit - 3)] + "..."
    tail = Path(*parts[-2:]).as_posix()
    return f".../{tail}" if len(tail) + 4 <= limit else path[: max(0, limit - 3)] + "..."


def resolve_repo_relative_path(raw_path: str, root: Path) -> Path:
    candidate = Path(raw_path)
    if candidate.is_absolute():
        raise ValueError(f"absolute paths are not allowed: {raw_path}")
    resolved = (root / candidate).resolve(strict=False)
    if not resolved.is_relative_to(root):
        raise ValueError(f"path traversal is not allowed: {raw_path}")
    return resolved


def repo_relative_string(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def is_png_file(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() == ".png"


def normalize_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [str(item).strip() for item in value if str(item).strip()]


def resolved_family_paths(family: dict[str, Any]) -> dict[str, list[str]]:
    source_png_paths = normalize_list(family.get("source_png_paths"))
    legacy_png_paths = normalize_list(family.get("png_paths"))
    if not source_png_paths:
        source_png_paths = legacy_png_paths
    compiled_asset_sheet_paths = normalize_list(family.get("compiled_asset_sheet_paths"))
    legacy_asset_sheet_paths = normalize_list(family.get("asset_sheet_paths"))
    if not compiled_asset_sheet_paths:
        compiled_asset_sheet_paths = legacy_asset_sheet_paths
    reference_sheet_paths = normalize_list(family.get("reference_sheet_paths"))
    in_flight_image_paths = normalize_list(family.get("in_flight_image_paths"))
    in_flight_reference_paths = normalize_list(family.get("in_flight_reference_paths"))
    selectors = normalize_list(family.get("selectors"))
    requested_optional_paths_or_names = normalize_list(family.get("requested_optional_paths_or_names"))
    return {
        "source_png_paths": source_png_paths,
        "compiled_asset_sheet_paths": compiled_asset_sheet_paths,
        "reference_sheet_paths": reference_sheet_paths,
        "in_flight_image_paths": in_flight_image_paths,
        "in_flight_reference_paths": in_flight_reference_paths,
        "selectors": selectors,
        "requested_optional_paths_or_names": requested_optional_paths_or_names,
    }


def classify_record_type(repo_rel_path: str, requested_type: str | None = None) -> str:
    path = repo_rel_path.replace("\\", "/")
    if requested_type in {"in_flight_image", "in_flight_reference"}:
        return requested_type
    if path == "assets/in-flight" or path.startswith("assets/in-flight/"):
        return "in_flight_image"
    if "compiled_asset_sheets/" in path:
        return "asset_sheet"
    if "reference_sheets/" in path:
        return "reference_sheet"
    return requested_type or "source_png"


def safe_add_record(
    family_id: str,
    raw_path: str,
    root: Path,
    requested_type: str | None,
    skipped: list[dict[str, Any]],
    seen: set[str],
) -> InputRecord | None:
    try:
        resolved = resolve_repo_relative_path(raw_path, root)
    except Exception as exc:
        skipped.append(
            {
                "family_id": family_id,
                "input": raw_path,
                "kind": "path",
                "reason": str(exc),
            }
        )
        return None

    repo_rel = repo_relative_string(resolved, root)
    if repo_rel in seen:
        skipped.append(
            {
                "family_id": family_id,
                "input": raw_path,
                "kind": "duplicate",
                "reason": "duplicate input path",
            }
        )
        return None

    if not resolved.exists():
        skipped.append(
            {
                "family_id": family_id,
                "input": raw_path,
                "kind": "missing",
                "reason": "file does not exist",
            }
        )
        return None
    if not resolved.is_file():
        skipped.append(
            {
                "family_id": family_id,
                "input": raw_path,
                "kind": "unreadable",
                "reason": "path exists but is not a file",
            }
        )
        return None
    if resolved.suffix.lower() != ".png":
        skipped.append(
            {
                "family_id": family_id,
                "input": raw_path,
                "kind": "non_png",
                "reason": "file is not a PNG",
            }
        )
        return None
    try:
        with Image.open(resolved) as img:
            img.verify()
    except Exception as exc:
        skipped.append(
            {
                "family_id": family_id,
                "input": raw_path,
                "kind": "unreadable",
                "reason": f"image could not be opened: {exc}",
            }
        )
        return None

    seen.add(repo_rel)
    record_type = classify_record_type(repo_rel, requested_type)
    return InputRecord(family_id=family_id, record_type=record_type, source_path=repo_rel, resolved_path=resolved)


def collect_selector_records(
    family_id: str,
    selectors: list[Any],
    root: Path,
    skipped: list[dict[str, Any]],
    seen: set[str],
) -> list[InputRecord]:
    records: list[InputRecord] = []
    for selector in selectors:
        if not isinstance(selector, str) or not selector.strip():
            skipped.append(
                {
                    "family_id": family_id,
                    "input": selector,
                    "kind": "selector",
                    "reason": "selector must be a non-empty string",
                }
            )
            continue

        if Path(selector).is_absolute():
            skipped.append(
                {
                    "family_id": family_id,
                    "input": selector,
                    "kind": "selector",
                    "reason": "absolute selectors are not allowed",
                }
            )
            continue

        try:
            resolved = resolve_repo_relative_path(selector, root)
        except Exception as exc:
            skipped.append(
                {
                    "family_id": family_id,
                    "input": selector,
                    "kind": "selector",
                    "reason": str(exc),
                }
            )
            continue

        if resolved.is_dir():
            for child in sorted(resolved.iterdir()):
                if child.is_file() and child.suffix.lower() == ".png":
                    record = safe_add_record(
                        family_id,
                        repo_relative_string(child, root),
                        root,
                        None,
                        skipped,
                        seen,
                    )
                    if record is not None:
                        records.append(record)
            continue

        record = safe_add_record(family_id, selector, root, None, skipped, seen)
        if record is not None:
            records.append(record)

    return records


def collect_family_records(
    family_id: str,
    source_png_paths: list[str],
    compiled_asset_sheet_paths: list[str],
    reference_sheet_paths: list[str],
    in_flight_image_paths: list[str],
    in_flight_reference_paths: list[str],
    selectors: list[str],
    requested_optional_paths_or_names: list[str],
    root: Path,
    skipped: list[dict[str, Any]],
) -> tuple[list[InputRecord], list[InputRecord], list[InputRecord], list[InputRecord], list[InputRecord]]:
    source_records: list[InputRecord] = []
    asset_sheet_records: list[InputRecord] = []
    reference_sheet_records: list[InputRecord] = []
    in_flight_image_records: list[InputRecord] = []
    in_flight_reference_records: list[InputRecord] = []
    seen: set[str] = set()

    def route_record(record: InputRecord | None) -> None:
        if record is None:
            return
        if record.record_type == "source_png":
            source_records.append(record)
        elif record.record_type == "asset_sheet":
            asset_sheet_records.append(record)
        elif record.record_type == "reference_sheet":
            reference_sheet_records.append(record)
        elif record.record_type == "in_flight_image":
            in_flight_image_records.append(record)
        elif record.record_type == "in_flight_reference":
            in_flight_reference_records.append(record)
        else:
            source_records.append(record)

    for raw_path in source_png_paths:
        route_record(safe_add_record(family_id, raw_path, root, "source_png", skipped, seen))

    for record in collect_selector_records(family_id, selectors, root, skipped, seen):
        route_record(record)

    for raw_path in compiled_asset_sheet_paths:
        route_record(safe_add_record(family_id, raw_path, root, "asset_sheet", skipped, seen))

    for raw_path in reference_sheet_paths:
        route_record(safe_add_record(family_id, raw_path, root, "reference_sheet", skipped, seen))

    for raw_path in in_flight_image_paths:
        route_record(safe_add_record(family_id, raw_path, root, "in_flight_image", skipped, seen))

    for raw_path in in_flight_reference_paths:
        route_record(safe_add_record(family_id, raw_path, root, "in_flight_reference", skipped, seen))

    if requested_optional_paths_or_names:
        resolved_set = (
            {record.source_path for record in source_records}
            | {record.source_path for record in asset_sheet_records}
            | {record.source_path for record in reference_sheet_records}
            | {record.source_path for record in in_flight_image_records}
            | {record.source_path for record in in_flight_reference_records}
        )
        for raw_name in requested_optional_paths_or_names:
            if raw_name in resolved_set:
                continue
            skipped.append(
                {
                    "family_id": family_id,
                    "input": raw_name,
                    "kind": "missing_optional_reference",
                    "reason": "not repo-tracked or not found through inspected selectors",
                    "status": "not_found",
                }
            )

    return (
        sorted(source_records, key=lambda item: item.source_path),
        sorted(asset_sheet_records, key=lambda item: item.source_path),
        sorted(reference_sheet_records, key=lambda item: item.source_path),
        sorted(in_flight_image_records, key=lambda item: item.source_path),
        sorted(in_flight_reference_records, key=lambda item: item.source_path),
    )


def load_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    try:
        if bold:
            return ImageFont.truetype("DejaVuSans-Bold.ttf", size=size)
        return ImageFont.truetype("DejaVuSans.ttf", size=size)
    except Exception:
        return ImageFont.load_default()


def wrap_label(label: str, font: ImageFont.ImageFont, width: int, max_lines: int = 2) -> list[str]:
    words = label.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        bbox = font.getbbox(candidate)
        if bbox[2] - bbox[0] <= width:
            current = candidate
            continue
        if current:
            lines.append(current)
        current = word
    if current:
        lines.append(current)
    if not lines:
        lines = [label]
    if len(lines) > max_lines:
        trimmed = lines[: max_lines - 1]
        last = " ".join(lines[max_lines - 1 :])
        while font.getbbox(last + "…")[2] - font.getbbox(last + "…")[0] > width and len(last) > 1:
            last = last[:-1]
        lines = trimmed + [last.rstrip() + "…"]
    return lines


def render_contact_sheet(
    family_id: str,
    request_id: str,
    reason: str,
    records: list[InputRecord],
    output_path: Path,
    sheet_number: int,
    total_sheets: int,
) -> list[dict[str, Any]]:
    columns = min(3, max(1, len(records)))
    rows = math.ceil(len(records) / columns)

    margin = 30
    gap = 20
    title_height = 96
    cell_w = 360
    cell_h = 330
    thumb_w = 320
    thumb_h = 200
    label_h = 76

    sheet_w = margin * 2 + columns * cell_w + (columns - 1) * gap
    sheet_h = margin + title_height + rows * cell_h + (rows - 1) * gap + margin

    canvas = Image.new("RGB", (sheet_w, sheet_h), "white")
    draw = ImageDraw.Draw(canvas)
    title_font = load_font(28, bold=True)
    subtitle_font = load_font(16)
    label_font = load_font(15)

    title = f"{family_id} | page {sheet_number}/{total_sheets}"
    subtitle = f"request {request_id} | {reason}"
    draw.text((margin, margin), title, fill="#111111", font=title_font)
    draw.text((margin, margin + 38), subtitle, fill="#444444", font=subtitle_font)
    draw.line((margin, margin + title_height - 16, sheet_w - margin, margin + title_height - 16), fill="#DDDDDD", width=2)

    manifest_panels: list[dict[str, Any]] = []
    for index, record in enumerate(records):
        row = index // columns
        col = index % columns
        x0 = margin + col * (cell_w + gap)
        y0 = margin + title_height + row * (cell_h + gap)

        cell_rect = [x0, y0, x0 + cell_w, y0 + cell_h]
        draw.rounded_rectangle(cell_rect, radius=18, outline="#C8C8C8", width=2, fill="#FAFAFA")

        with Image.open(record.resolved_path) as source:
            image = source.convert("RGBA")
            thumb = ImageOps.contain(image, (thumb_w, thumb_h))
            thumb_bg = Image.new("RGBA", (thumb_w, thumb_h), (255, 255, 255, 255))
            paste_x = (thumb_w - thumb.width) // 2
            paste_y = (thumb_h - thumb.height) // 2
            thumb_bg.alpha_composite(thumb, (paste_x, paste_y))
            thumb_rgb = thumb_bg.convert("RGB")

        thumb_x = x0 + (cell_w - thumb_w) // 2
        thumb_y = y0 + 18
        canvas.paste(thumb_rgb, (thumb_x, thumb_y))
        draw.rectangle(
            [thumb_x, thumb_y, thumb_x + thumb_w - 1, thumb_y + thumb_h - 1],
            outline="#BBBBBB",
            width=1,
        )

        label = f"{index + 1}. [{record.record_type}] {Path(record.source_path).name}"
        label_lines = wrap_label(label, label_font, thumb_w - 10, max_lines=2)
        text_y = thumb_y + thumb_h + 10
        for line in label_lines:
            bbox = label_font.getbbox(line)
            line_h = bbox[3] - bbox[1]
            draw.text((thumb_x + 5, text_y), line, fill="#222222", font=label_font)
            text_y += line_h + 2

        manifest_panels.append(
            {
                "panel_index": len(manifest_panels) + 1,
                "sheet_file": output_path.name,
                "sheet_index": sheet_number,
                "panel_slot": index + 1,
                "record_type": record.record_type,
                "source_path": record.source_path,
                "visible_label": label,
            }
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path)
    return manifest_panels


def copy_included_asset(source_path: Path, destination_path: Path) -> None:
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    destination_path.write_bytes(source_path.read_bytes())


def write_deterministic_zip(zip_path: Path, files: list[Path], root: Path) -> None:
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w") as archive:
        for file_path in sorted(files, key=lambda item: item.as_posix()):
            arcname = file_path.relative_to(root).as_posix()
            info = zipfile.ZipInfo(arcname, date_time=FIXED_ZIP_DATE_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            with file_path.open("rb") as handle:
                archive.writestr(info, handle.read())


def build_staging_dir(staging_root: Path, request_id: str) -> Path:
    run_name = slugify(request_id)
    run_dir = staging_root / run_name
    if run_dir.exists():
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
        run_dir = staging_root / f"{run_name}--{timestamp}"
    return run_dir


def validate_dispatch(dispatch: dict[str, Any]) -> None:
    required = [
        "request_type",
        "project",
        "source_repo",
        "request_id",
        "issue",
        "purpose",
        "families",
        "output",
    ]
    missing = [field for field in required if field not in dispatch]
    if missing:
        raise ValueError(f"dispatch missing required fields: {', '.join(missing)}")
    if dispatch["request_type"] != REQUEST_TYPE:
        raise ValueError(f"unsupported request_type: {dispatch['request_type']}")
    if dispatch["project"] != PROJECT:
        raise ValueError(f"unsupported project: {dispatch['project']}")
    if dispatch["source_repo"] != SOURCE_REPO:
        raise ValueError(f"unsupported source_repo: {dispatch['source_repo']}")
    if not isinstance(dispatch["families"], list) or not dispatch["families"]:
        raise ValueError("families must be a non-empty list")


def build_contact_sheets(dispatch_path: Path, output_root: Path) -> dict[str, Any]:
    root = repo_root()
    dispatch = load_json(dispatch_path)
    validate_dispatch(dispatch)

    staging_root = root / "scratch" / "contact-sheet-builds"
    run_dir = build_staging_dir(staging_root, str(dispatch["request_id"]))
    contact_sheets_dir = run_dir / "contact-sheets"
    included_assets_dir = run_dir / "included-assets"
    manifests_dir = run_dir / "manifests"
    sheets_written: list[Path] = []
    included_assets_written: list[Path] = []
    skipped: list[dict[str, Any]] = []
    family_results: list[dict[str, Any]] = []
    all_panels: list[dict[str, Any]] = []
    all_included_assets: list[dict[str, Any]] = []
    unresolved: list[dict[str, Any]] = []
    compiled_assets_included: list[dict[str, Any]] = []
    reference_sheets_included: list[dict[str, Any]] = []
    in_flight_full_size_included: list[dict[str, Any]] = []

    for family in dispatch["families"]:
        if not isinstance(family, dict):
            skipped.append(
                {
                    "family_id": None,
                    "input": family,
                    "kind": "family",
                    "reason": "family entry must be an object",
                }
            )
            continue

        family_id = str(family.get("family_id", "")).strip()
        reason = str(family.get("reason", "")).strip()
        family_paths = resolved_family_paths(family)
        source_png_paths = family_paths["source_png_paths"]
        compiled_asset_sheet_paths = family_paths["compiled_asset_sheet_paths"]
        reference_sheet_paths = family_paths["reference_sheet_paths"]
        in_flight_image_paths = family_paths["in_flight_image_paths"]
        in_flight_reference_paths = family_paths["in_flight_reference_paths"]
        selectors = family_paths["selectors"]
        requested_optional_paths_or_names = family_paths["requested_optional_paths_or_names"]
        if not family_id:
            skipped.append(
                {
                    "family_id": None,
                    "input": family,
                    "kind": "family",
                    "reason": "family_id is required",
                }
            )
            continue

        family_skipped: list[dict[str, Any]] = []
        source_records, asset_sheet_records, reference_sheet_records, in_flight_image_records, in_flight_reference_records = collect_family_records(
            family_id,
            source_png_paths,
            compiled_asset_sheet_paths,
            reference_sheet_paths,
            in_flight_image_paths,
            in_flight_reference_paths,
            selectors,
            requested_optional_paths_or_names,
            root,
            family_skipped,
        )

        contact_sheet_records = sorted(source_records, key=lambda item: item.source_path)
        source_contact_sheet_generated = bool(contact_sheet_records)
        source_contact_sheet_reason: str | None = None
        if not source_records:
            if asset_sheet_records and reference_sheet_records:
                source_contact_sheet_reason = "full_size_asset_sheets_only_no_source_images"
            elif asset_sheet_records:
                source_contact_sheet_reason = "compiled_asset_sheet_only_no_source_images"
            elif reference_sheet_records:
                source_contact_sheet_reason = "reference_sheet_only_no_source_images"
            elif in_flight_image_records or in_flight_reference_records:
                source_contact_sheet_reason = "in_flight_full_size_only_no_source_images"
            else:
                source_contact_sheet_reason = "no_source_images_or_asset_sheets_resolved"

        family_sheet_files: list[str] = []
        family_panels: list[dict[str, Any]] = []
        if contact_sheet_records:
            max_per_sheet = 12
            total_sheets = math.ceil(len(contact_sheet_records) / max_per_sheet)
            for sheet_number in range(1, total_sheets + 1):
                start = (sheet_number - 1) * max_per_sheet
                end = start + max_per_sheet
                page_records = contact_sheet_records[start:end]
                sheet_suffix = f"__{sheet_number:02d}" if total_sheets > 1 else ""
                sheet_name = f"{slugify(family_id)}{sheet_suffix}.png"
                sheet_path = contact_sheets_dir / sheet_name
                page_panels = render_contact_sheet(
                    family_id=family_id,
                    request_id=str(dispatch["request_id"]),
                    reason=reason or "no reason provided",
                    records=page_records,
                    output_path=sheet_path,
                    sheet_number=sheet_number,
                    total_sheets=total_sheets,
                )
                family_sheet_files.append(sheet_path.relative_to(run_dir).as_posix())
                family_panels.extend(page_panels)
                sheets_written.append(sheet_path)

        family_included_assets: list[dict[str, Any]] = []
        for record in asset_sheet_records:
            included_relative = Path("included-assets") / slugify(family_id) / Path(record.source_path).name
            included_path = run_dir / included_relative
            copy_included_asset(record.resolved_path, included_path)
            included_assets_written.append(included_path)
            entry = {
                "family_id": family_id,
                "zip_path": included_relative.as_posix(),
                "source_path": record.source_path,
                "record_type": record.record_type,
            }
            family_included_assets.append(entry)
            all_included_assets.append(entry)
            compiled_assets_included.append(entry)

        family_reference_assets: list[dict[str, Any]] = []
        for record in reference_sheet_records:
            included_relative = Path("included-assets") / slugify(family_id) / Path(record.source_path).name
            included_path = run_dir / included_relative
            copy_included_asset(record.resolved_path, included_path)
            included_assets_written.append(included_path)
            entry = {
                "family_id": family_id,
                "zip_path": included_relative.as_posix(),
                "source_path": record.source_path,
                "record_type": record.record_type,
            }
            family_reference_assets.append(entry)
            all_included_assets.append(entry)
            reference_sheets_included.append(entry)

        family_in_flight_assets: list[dict[str, Any]] = []
        for record in sorted(in_flight_image_records + in_flight_reference_records, key=lambda item: item.source_path):
            included_relative = Path("included-assets") / slugify(family_id) / "in-flight" / Path(record.source_path).name
            included_path = run_dir / included_relative
            copy_included_asset(record.resolved_path, included_path)
            included_assets_written.append(included_path)
            entry = {
                "family_id": family_id,
                "zip_path": included_relative.as_posix(),
                "source_path": record.source_path,
                "record_type": record.record_type,
            }
            family_in_flight_assets.append(entry)
            all_included_assets.append(entry)
            in_flight_full_size_included.append(entry)

        if not source_records and not asset_sheet_records and not reference_sheet_records and not in_flight_image_records and not in_flight_reference_records:
            unresolved.append(
                {
                    "family_id": family_id,
                    "reason": "no valid source PNGs, compiled asset sheets, reference sheets, or in-flight assets were resolved for this family",
                    "requested_source_png_paths": source_png_paths,
                    "requested_compiled_asset_sheet_paths": compiled_asset_sheet_paths,
                    "requested_reference_sheet_paths": reference_sheet_paths,
                    "requested_in_flight_image_paths": in_flight_image_paths,
                    "requested_in_flight_reference_paths": in_flight_reference_paths,
                    "selectors": selectors,
                    "requested_optional_paths_or_names": requested_optional_paths_or_names,
                }
            )

        if family_skipped:
            skipped.extend(family_skipped)

        all_panels.extend(
            [
                {
                    **panel,
                    "family_id": family_id,
                }
                for panel in family_panels
            ]
        )
        family_results.append(
            {
                "family_id": family_id,
                "reason": reason,
                "source_contact_sheet_generated": source_contact_sheet_generated,
                "source_contact_sheet_reason": source_contact_sheet_reason,
                "rendered_source_contact_sheets": family_sheet_files,
                "included_existing_assets": [entry["zip_path"] for entry in family_included_assets + family_reference_assets + family_in_flight_assets],
                "included_compiled_asset_sheets": [entry["zip_path"] for entry in family_included_assets],
                "included_reference_sheets": [entry["zip_path"] for entry in family_reference_assets],
                "included_in_flight_assets": [entry["zip_path"] for entry in family_in_flight_assets],
                "included_in_flight_references": [entry["zip_path"] for entry in family_in_flight_assets],
                "source_records": [
                    {
                        "source_path": record.source_path,
                        "record_type": record.record_type,
                    }
                    for record in source_records
                ],
                "asset_sheet_records": [
                    {
                        "source_path": record.source_path,
                        "record_type": record.record_type,
                    }
                    for record in asset_sheet_records
                ],
                "reference_sheet_records": [
                    {
                        "source_path": record.source_path,
                        "record_type": record.record_type,
                    }
                    for record in reference_sheet_records
                ],
                "in_flight_image_records": [
                    {
                        "source_path": record.source_path,
                        "record_type": record.record_type,
                    }
                    for record in in_flight_image_records
                ],
                "in_flight_reference_records": [
                    {
                        "source_path": record.source_path,
                        "record_type": record.record_type,
                    }
                    for record in in_flight_reference_records
                ],
                "panels": family_panels,
                "skipped": family_skipped,
            }
        )

    request_json = dispatch
    request_json.setdefault("schema_version", 2)
    manifest = {
        "request": request_json,
        "output": {
            "root": run_dir.relative_to(root).as_posix(),
            "contact_sheet_per_family": True,
            "zip_all_outputs": True,
            "include_manifest": True,
        },
        "taxonomy": {
            "in_flight_assets_are_non_canonical": True,
            "in_flight_record_types": ["in_flight_image", "in_flight_reference"],
        },
        "stats": {
            "families_requested": len(dispatch["families"]),
            "families_rendered": len([item for item in family_results if item["rendered_source_contact_sheets"]]),
            "source_contact_sheets_rendered": len(sheets_written),
            "included_existing_assets": len(all_included_assets),
            "included_compiled_asset_sheets": len(compiled_assets_included),
            "included_reference_sheets": len(reference_sheets_included),
            "included_in_flight_assets": len(in_flight_full_size_included),
            "included_in_flight_references": len(in_flight_full_size_included),
            "in_flight_contact_sheet_panels": 0,
            "compiled_asset_sheet_only_families": len([item for item in family_results if item["source_contact_sheet_reason"] == "compiled_asset_sheet_only_no_source_images"]),
            "reference_sheet_only_families": len([item for item in family_results if item["source_contact_sheet_reason"] == "reference_sheet_only_no_source_images"]),
            "in_flight_full_size_only_families": len([item for item in family_results if item["source_contact_sheet_reason"] == "in_flight_full_size_only_no_source_images"]),
            "skipped_count": len(skipped),
            "unresolved_count": len(unresolved),
        },
        "families": family_results,
        "rendered_source_contact_sheets": all_panels,
        "included_existing_assets": all_included_assets,
        "included_compiled_asset_sheets": compiled_assets_included,
        "included_reference_sheets": reference_sheets_included,
        "included_in_flight_assets": in_flight_full_size_included,
        "included_in_flight_references": in_flight_full_size_included,
    }
    if unresolved:
        manifest["unresolved"] = unresolved

    zip_name = f"{slugify(str(dispatch['request_id']))}.zip"
    output_zip = output_root / zip_name
    request_path = manifests_dir / "request.json"
    manifest_path = manifests_dir / "manifest.json"
    skipped_path = manifests_dir / "skipped.json"
    evidence_path = run_dir / "evidence.json"
    unresolved_path = manifests_dir / "unresolved.json"

    request_path.parent.mkdir(parents=True, exist_ok=True)
    dump_json(request_path, request_json)
    dump_json(manifest_path, manifest)
    dump_json(skipped_path, skipped)
    if unresolved:
        dump_json(unresolved_path, unresolved)

    evidence = {
        "command": f"python {Path(__file__).as_posix()} --dispatch {dispatch_path.as_posix()} --output-root {output_root.as_posix()}",
        "request_id": str(dispatch["request_id"]),
        "issue": dispatch["issue"],
        "staging_root": run_dir.relative_to(root).as_posix(),
        "zip": output_zip.relative_to(root).as_posix(),
        "contact_sheets": [path.relative_to(root).as_posix() for path in sheets_written],
        "included_assets": [path.relative_to(root).as_posix() for path in included_assets_written],
        "manifest": manifest_path.relative_to(root).as_posix(),
        "skipped": skipped_path.relative_to(root).as_posix(),
        "request": request_path.relative_to(root).as_posix(),
        "unresolved": unresolved_path.relative_to(root).as_posix() if unresolved else None,
        "found_count": len(all_panels) + len(all_included_assets),
        "source_contact_sheet_count": len(sheets_written),
        "included_existing_asset_count": len(included_assets_written),
        "in_flight_contact_sheet_panels": 0,
        "in_flight_full_size_inclusions": len(in_flight_full_size_included),
        "compiled_asset_sheet_only_family_count": len([item for item in family_results if item["source_contact_sheet_reason"] == "compiled_asset_sheet_only_no_source_images"]),
        "reference_sheet_only_family_count": len([item for item in family_results if item["source_contact_sheet_reason"] == "reference_sheet_only_no_source_images"]),
        "in_flight_full_size_only_family_count": len([item for item in family_results if item["source_contact_sheet_reason"] == "in_flight_full_size_only_no_source_images"]),
        "skipped_count": len(skipped),
        "families_rendered": len([item for item in family_results if item["rendered_source_contact_sheets"]]),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "taxonomy": {
            "in_flight_assets_are_non_canonical": True,
            "in_flight_record_types": ["in_flight_image", "in_flight_reference"],
        },
    }
    dump_json(evidence_path, evidence)

    files_to_zip: list[Path] = [request_path, manifest_path, skipped_path, evidence_path] + sheets_written + included_assets_written
    if unresolved:
        files_to_zip.append(unresolved_path)
    write_deterministic_zip(output_zip, files_to_zip, run_dir)

    return {
        "run_dir": run_dir,
        "output_zip": output_zip,
        "request_path": request_path,
        "manifest_path": manifest_path,
        "skipped_path": skipped_path,
        "evidence_path": evidence_path,
        "unresolved_path": unresolved_path if unresolved else None,
        "contact_sheets": sheets_written,
        "included_assets": included_assets_written,
        "skipped": skipped,
        "source_contact_sheet_count": len(sheets_written),
        "included_existing_asset_count": len(included_assets_written),
        "in_flight_contact_sheet_panels": 0,
        "in_flight_full_size_inclusions": len(in_flight_full_size_included),
        "compiled_asset_sheet_only_family_count": len([item for item in family_results if item["source_contact_sheet_reason"] == "compiled_asset_sheet_only_no_source_images"]),
        "reference_sheet_only_family_count": len([item for item in family_results if item["source_contact_sheet_reason"] == "reference_sheet_only_no_source_images"]),
        "in_flight_full_size_only_family_count": len([item for item in family_results if item["source_contact_sheet_reason"] == "in_flight_full_size_only_no_source_images"]),
        "families_rendered": len([item for item in family_results if item["rendered_source_contact_sheets"]]),
        "unresolved": unresolved,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build deterministic PNG contact sheets from a dispatch JSON file.")
    parser.add_argument("--dispatch", required=True, help="path to a dispatch JSON file")
    parser.add_argument(
        "--output-root",
        required=True,
        help="output root under the repository, for example output-zips",
    )
    args = parser.parse_args(argv)

    root = repo_root()
    dispatch_path = Path(args.dispatch)
    if not dispatch_path.is_absolute():
        dispatch_path = (root / dispatch_path).resolve(strict=False)
    output_root = Path(args.output_root)
    if not output_root.is_absolute():
        output_root = (root / output_root).resolve(strict=False)

    if not dispatch_path.exists():
        print(f"dispatch file does not exist: {dispatch_path}", file=sys.stderr)
        return 2
    if not dispatch_path.is_file():
        print(f"dispatch path is not a file: {dispatch_path}", file=sys.stderr)
        return 2
    if not dispatch_path.is_relative_to(root):
        print(f"dispatch path must be inside the repository: {dispatch_path}", file=sys.stderr)
        return 2
    if not output_root.is_relative_to(root):
        print(f"output root must be inside the repository: {output_root}", file=sys.stderr)
        return 2

    try:
        result = build_contact_sheets(dispatch_path, output_root)
    except Exception as exc:  # pragma: no cover - CLI boundary
        print(str(exc), file=sys.stderr)
        return 1

    run_dir = result["run_dir"]
    evidence = load_json(result["evidence_path"])
    print(f"staging_root: {run_dir.relative_to(root).as_posix()}")
    print(f"zip: {result['output_zip'].relative_to(root).as_posix()}")
    print(f"contact_sheets: {len(result['contact_sheets'])}")
    for sheet in result["contact_sheets"]:
        print(f"sheet: {sheet.relative_to(root).as_posix()}")
    print(f"included_assets: {len(result['included_assets'])}")
    for asset in result["included_assets"]:
        print(f"included: {asset.relative_to(root).as_posix()}")
    print(f"manifest: {result['manifest_path'].relative_to(root).as_posix()}")
    print(f"skipped: {result['skipped_path'].relative_to(root).as_posix()}")
    print(f"found_count: {evidence['found_count']}")
    print(f"skipped_count: {evidence['skipped_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
