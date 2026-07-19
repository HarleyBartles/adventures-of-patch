#!/usr/bin/env python3
"""Generate or validate the repository-wide INDEX.md mesh."""

from __future__ import annotations

import argparse
import os
import re
import stat
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path


INDEX_NAME = "INDEX.md"
EXCLUDED_DIR_NAMES = {".git", "__pycache__", ".pytest_cache"}
EXCLUDED_FILE_NAMES = {".git"}
LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

ROOT: Path | None = None
TRACKED_FILES: set[str] = set()
TRACKED_DIRS: set[str] = set()
GITLINKS: set[str] = set()


@dataclass(frozen=True)
class IndexTarget:
    directory: Path
    content: str


def git_output(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def unignored_files(root: Path) -> set[str]:
    candidates: list[str] = []
    for directory, dirnames, filenames in os.walk(root, topdown=True, followlinks=False):
        current = Path(directory)
        dirnames[:] = [
            name
            for name in dirnames
            if name not in EXCLUDED_DIR_NAMES
            and not is_reparse_or_link(current / name)
            and not is_gitlink(current / name)
            and not is_skill_root(current / name)
        ]
        for name in filenames:
            path = current / name
            if name not in EXCLUDED_FILE_NAMES and not is_reparse_or_link(path):
                candidates.append(path.relative_to(root).as_posix())
    if not candidates:
        return set()
    result = subprocess.run(
        ["git", "-C", str(root), "check-ignore", "-z", "--stdin"],
        input=("\0".join(candidates) + "\0").encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode not in {0, 1}:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace").strip())
    ignored = {
        item
        for item in result.stdout.decode("utf-8", errors="replace").split("\0")
        if item
    }
    return set(candidates) - ignored


def discover_root(start: Path | None = None) -> Path:
    probe = (start or Path.cwd()).resolve()
    superproject = git_output(probe, "rev-parse", "--show-superproject-working-tree")
    if superproject:
        raise RuntimeError(f"Refusing to run inside submodule {superproject}")
    return Path(git_output(probe, "rev-parse", "--show-toplevel")).resolve()


def configure(root: Path) -> None:
    global ROOT, TRACKED_FILES, TRACKED_DIRS, GITLINKS
    ROOT = root.resolve()
    TRACKED_FILES = {
        item for item in git_output(ROOT, "ls-files", "-z").split("\0") if item
    }
    GITLINKS = set()
    raw = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "--stage", "-z"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if raw.returncode != 0:
        raise RuntimeError(raw.stderr.decode("utf-8", errors="replace").strip())
    for record in raw.stdout.decode("utf-8", errors="replace").split("\0"):
        if not record:
            continue
        metadata, relative = record.split("\t", 1)
        if metadata.split(" ", 1)[0] == "160000":
            GITLINKS.add(relative)

    TRACKED_FILES.update(unignored_files(ROOT))

    TRACKED_DIRS = {"."}
    for relative in TRACKED_FILES | GITLINKS:
        path = Path(relative)
        for index in range(len(path.parts)):
            TRACKED_DIRS.add(Path(*path.parts[:index]).as_posix() or ".")


def repo_root() -> Path:
    if ROOT is None:
        configure(discover_root())
    assert ROOT is not None
    return ROOT


def relative(path: Path) -> str:
    root = repo_root()
    return path.relative_to(root).as_posix() or "."


def is_reparse_or_link(path: Path) -> bool:
    try:
        metadata = path.lstat()
    except FileNotFoundError:
        return False
    if stat.S_ISLNK(metadata.st_mode):
        return True
    flag = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    return bool(getattr(metadata, "st_file_attributes", 0) & flag)


def is_gitlink(path: Path) -> bool:
    current = path
    root = repo_root()
    while True:
        try:
            key = current.relative_to(root).as_posix()
        except ValueError:
            return False
        if key in GITLINKS:
            return True
        if current == root:
            return False
        current = current.parent


def is_skill_root(path: Path) -> bool:
    return (path / "SKILL.md").is_file() or (path / "overlay.yaml").is_file()


def has_tracked_content(path: Path) -> bool:
    root = repo_root()
    key = relative(path)
    prefix = "" if key == "." else key + "/"
    return any(item == key or item.startswith(prefix) for item in TRACKED_FILES | GITLINKS)


def should_index(path: Path) -> bool:
    root = repo_root()
    if path == root:
        return True
    if is_reparse_or_link(path) or is_gitlink(path) or is_skill_root(path):
        return False
    ancestor = path.parent
    while ancestor != root:
        if is_skill_root(ancestor) or is_gitlink(ancestor):
            return False
        ancestor = ancestor.parent
    if any(part in EXCLUDED_DIR_NAMES for part in path.relative_to(root).parts):
        return False
    return relative(path) in TRACKED_DIRS and has_tracked_content(path)


def should_descend(path: Path) -> bool:
    return should_index(path)


def relative_link(current: Path, target: Path, label: str | None = None) -> str:
    target_text = os.path.relpath(target, start=current).replace(os.sep, "/")
    return f"[{label or target.name}]({target_text})"


def directory_link(current: Path, child: Path) -> str:
    if is_gitlink(child):
        return relative_link(current, child, child.name) + "/"
    if is_skill_root(child):
        return relative_link(current, child / "SKILL.md", child.name)
    return relative_link(current, child / INDEX_NAME, child.name)


def index_title(path: Path) -> str:
    return "Repository Root" if path == repo_root() else f"`{relative(path)}` Index"


def render_index(path: Path) -> str:
    directories: list[Path] = []
    files: list[Path] = []
    for entry in sorted(path.iterdir(), key=lambda item: (not item.is_dir(), item.name.casefold(), item.name)):
        if entry.name.casefold() == INDEX_NAME.casefold() or is_reparse_or_link(entry):
            continue
        if entry.is_dir():
            if entry.name in EXCLUDED_DIR_NAMES or not has_tracked_content(entry):
                continue
            if is_gitlink(entry) or is_skill_root(entry) or should_descend(entry):
                directories.append(entry)
            continue
        if entry.name not in EXCLUDED_FILE_NAMES and relative(entry) in TRACKED_FILES:
            files.append(entry)

    lines = [f"# {index_title(path)}", "", "> Generated by `scripts/generate_index_mesh.py`. Do not hand-edit.", ""]
    lines.extend(["## Location", f"- Repo path: `{relative(path)}`"])
    if path != repo_root():
        lines.append(f"- Up: {relative_link(path, path.parent / INDEX_NAME, 'parent index')}")
    lines.append("")

    if directories:
        lines.append("## Directories")
        lines.extend(f"- {directory_link(path, child)}" for child in directories)
        lines.append("")
    if files:
        lines.append("## Files")
        lines.extend(f"- {relative_link(path, child)}" for child in files)
        lines.append("")
    if not directories and not files:
        lines.extend(["No child entries.", ""])
    return "\n".join(lines).rstrip() + "\n"


def walk_targets() -> list[IndexTarget]:
    root = repo_root()
    targets: list[IndexTarget] = []
    for directory in [root, *(root / item for item in sorted(TRACKED_DIRS) if item != ".")]:
        if directory.exists() and should_index(directory):
            targets.append(IndexTarget(directory, render_index(directory)))
    return sorted(targets, key=lambda item: relative(item.directory))


def existing_index_paths() -> set[Path]:
    root = repo_root()
    paths: set[Path] = set()
    for directory, dirnames, filenames in os.walk(root, topdown=True, followlinks=False):
        current = Path(directory)
        dirnames[:] = [name for name in dirnames if should_descend(current / name)]
        index_names = [name for name in filenames if name.casefold() == INDEX_NAME.casefold()]
        if index_names and should_index(current):
            paths.add(current / index_names[0])
    return paths


def index_path(directory: Path) -> Path:
    canonical = directory / INDEX_NAME
    if canonical.exists():
        return canonical
    for entry in directory.iterdir():
        if entry.name.casefold() == INDEX_NAME.casefold():
            return entry
    return canonical


def resolve_link_target(index_path: Path, target: str) -> Path | None:
    if target.startswith(("http://", "https://", "mailto:")):
        return None
    clean = target.split("#", 1)[0]
    if not clean:
        return None
    candidate = (index_path.parent / clean.rstrip("/")).resolve()
    if not candidate.is_relative_to(repo_root()):
        return None
    return candidate


def validate_links(index_path: Path, content: str) -> list[str]:
    failures: list[str] = []
    for _label, target in LINK_PATTERN.findall(content):
        resolved = resolve_link_target(index_path, target)
        if resolved is None:
            continue
        if not resolved.exists():
            failures.append(f"broken-link: {relative(index_path)} -> {target}")
    return failures


def assert_write_safe(allow_shared_checkout: bool) -> None:
    root = repo_root()
    superproject = git_output(root, "rev-parse", "--show-superproject-working-tree")
    if superproject:
        raise RuntimeError(f"Refusing write from submodule {superproject}")
    git_dir = Path(git_output(root, "rev-parse", "--absolute-git-dir")).resolve()
    common_dir = Path(git_output(root, "rev-parse", "--path-format=absolute", "--git-common-dir")).resolve()
    if git_dir == common_dir and not allow_shared_checkout:
        raise RuntimeError("Mesh writes require a linked worktree; pass --allow-shared-checkout to override")


def write_atomic(path: Path, content: str) -> None:
    if is_reparse_or_link(path):
        raise RuntimeError(f"Refusing to replace link or reparse point: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", newline="\n", delete=False, dir=path.parent) as handle:
        handle.write(content)
        temporary = Path(handle.name)
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate or validate the repository-wide INDEX.md mesh")
    parser.add_argument("--check", action="store_true", help="validate without writing")
    parser.add_argument(
        "--allow-shared-checkout",
        action="store_true",
        help="allow write mode from the main/shared checkout",
    )
    args = parser.parse_args()

    configure(discover_root())
    targets = walk_targets()
    expected = {index_path(target.directory) for target in targets}
    actual = existing_index_paths()
    mismatches: list[str] = []

    if args.check:
        for target in targets:
            path = index_path(target.directory)
            if not path.exists():
                mismatches.append(f"missing: {relative(path)}")
                continue
            raw = path.read_bytes()
            if b"\r" in raw:
                mismatches.append(f"stale: {relative(path)} (must use LF)")
                continue
            current = raw.decode("utf-8")
            if current != target.content:
                mismatches.append(f"stale: {relative(path)}")
            mismatches.extend(validate_links(path, target.content))
        mismatches.extend(f"unexpected: {relative(path)}" for path in sorted(actual - expected))
        if mismatches:
            raise RuntimeError("INDEX mesh is stale or inconsistent:\n" + "\n".join(mismatches))
        print(f"OK index mesh: {len(targets)} indexes current")
        return 0

    assert_write_safe(args.allow_shared_checkout)
    for target in targets:
        write_atomic(index_path(target.directory), target.content)

    for path in sorted(actual - expected):
        if is_reparse_or_link(path):
            raise RuntimeError(f"Refusing to remove link or reparse point: {path}")
        path.unlink()

    for target in targets:
        path = index_path(target.directory)
        mismatches.extend(validate_links(path, target.content))
    if mismatches:
        raise RuntimeError("INDEX mesh produced broken links:\n" + "\n".join(mismatches))
    print(f"Wrote index mesh: {len(targets)} files")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, OSError, UnicodeError) as exc:
        print(f"ERROR: {exc}", file=__import__("sys").stderr)
        raise SystemExit(1)
