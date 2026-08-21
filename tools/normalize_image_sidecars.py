#!/usr/bin/env python3
"""Normalize image sidecar JSON formatting for deterministic CI.

`--check` fails if any *-sidecar.json is not formatted with:
  - 2-space indentation
  - ensure_ascii=False
  - LF line endings
  - no trailing whitespace
  - a single trailing newline

`--apply` rewrites any non-conforming sidecars in place.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def normalize(data: dict) -> str:
    """Return the canonical JSON text for a sidecar."""
    text = json.dumps(data, indent=2, ensure_ascii=False)
    lines = [line.rstrip() for line in text.split("\n")]
    return "\n".join(lines) + "\n"


def iter_sidecars(root: Path):
    """Yield all *-sidecar.json paths under root, excluding agent skills."""
    for path in root.rglob("*-sidecar.json"):
        if ".agents/skills" in path.as_posix():
            continue
        if not path.is_file():
            continue
        yield path


def check_and_apply(root: Path, apply: bool) -> int:
    changed = 0
    for path in iter_sidecars(root):
        raw = path.read_bytes()
        try:
            data = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError as exc:
            print(f"error: {path}: {exc}", file=sys.stderr)
            return 1
        expected = normalize(data).encode("utf-8")
        if raw != expected:
            changed += 1
            if apply:
                path.write_bytes(expected)
                print(f"normalized: {path}")
            else:
                print(f"would change: {path}")
    if not apply:
        if changed:
            print(f"error: {changed} sidecar(s) need normalization; run `ci --apply`", file=sys.stderr)
            return 1
        print(f"OK: all {sum(1 for _ in iter_sidecars(root))} sidecar(s) are normalized")
    else:
        print(f"OK: normalized {changed} sidecar(s)")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Normalize image sidecar JSON.")
    parser.add_argument("--apply", action="store_true", help="rewrite sidecars in place")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent,
                        help="repo root to search from")
    args = parser.parse_args(argv)
    return check_and_apply(args.root, apply=args.apply)


if __name__ == "__main__":
    raise SystemExit(main())
