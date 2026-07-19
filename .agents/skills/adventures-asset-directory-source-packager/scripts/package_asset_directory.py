from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[4]


def _validate_target_dir(target_dir: Path) -> list[Path]:
    if not target_dir.exists():
        raise FileNotFoundError(f"target directory does not exist: {target_dir}")
    if not target_dir.is_dir():
        raise NotADirectoryError(f"target path is not a directory: {target_dir}")
    nested_dirs = sorted(p for p in target_dir.iterdir() if p.is_dir())
    if nested_dirs:
        nested = "\n".join(str(p) for p in nested_dirs)
        raise RuntimeError(
            "nested directories are not allowed for this packaging workflow:\n" + nested
        )
    files = sorted(p for p in target_dir.iterdir() if p.is_file())
    if not files:
        raise RuntimeError(f"no files found in target directory: {target_dir}")
    return files


def package_asset_directory(target_dir: Path, source_zips_dir: Path) -> Path:
    files = _validate_target_dir(target_dir)
    source_zips_dir.mkdir(parents=True, exist_ok=True)
    zip_path = source_zips_dir / f"{target_dir.name}.zip"

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for file_path in files:
            archive.write(file_path, arcname=file_path.name)

    return zip_path


def list_zip_members(zip_path: Path) -> list[str]:
    with zipfile.ZipFile(zip_path) as archive:
        return archive.namelist()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Create a flat source zip from a target asset directory."
    )
    parser.add_argument("target_dir", help="asset directory path under assets/")
    parser.add_argument(
        "--source-zips-dir",
        help="source-zips directory path",
        default=str(_repo_root() / "assets" / "source-zips"),
    )
    args = parser.parse_args(argv)

    repo_root = _repo_root()
    target_dir = Path(args.target_dir).resolve()
    source_zips_dir = Path(args.source_zips_dir).resolve()

    assets_root = (repo_root / "assets").resolve()
    if assets_root not in target_dir.parents:
        print(f"target path must be inside assets/: {target_dir}", file=sys.stderr)
        return 2

    try:
        zip_path = package_asset_directory(target_dir, source_zips_dir)
    except Exception as exc:  # pragma: no cover - simple CLI wrapper
        print(str(exc), file=sys.stderr)
        return 1

    members = list_zip_members(zip_path)
    print(str(zip_path))
    for member in members:
        print(member)

    if any("/" in member or "\\" in member for member in members):
        print("zip contains nested paths; expected a flat archive", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
