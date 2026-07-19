#!/usr/bin/env python3
"""Refresh the deterministic agent surfaces used by this repository."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Sequence


ROOT = Path(__file__).resolve().parents[1]


def run(script: Path, args: Sequence[str]) -> None:
    result = subprocess.run([sys.executable, str(script), *args], cwd=ROOT)
    if result.returncode:
        raise RuntimeError(f"{script.name} failed with exit code {result.returncode}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate without writing")
    args = parser.parse_args(argv)
    check_args = ("--check",) if args.check else ()
    run(ROOT / "scripts" / "install_agent_skills.py", check_args)
    run(ROOT / "scripts" / "generate_index_mesh.py", check_args)
    mode = "checked" if args.check else "refreshed"
    print(f"OK {mode} agent surfaces: derived skills, index mesh")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
