#!/usr/bin/env python3
"""Minimal CI runner for the Adventures of Patch repo."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

import shared_checkout


ROOT = Path(__file__).resolve().parent.parent
SCRIPT_NAME = "tools/run"


def _run(cmd: list[str]) -> None:
    print("+ " + " ".join(cmd))
    subprocess.run(cmd, cwd=ROOT, check=True)


def _python() -> list[str]:
    return [sys.executable, "-3"] if sys.executable.endswith("py.exe") else [sys.executable]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Adventures of Patch CI runner.")
    parser.add_argument("target", choices=["ci"], help="target to run")
    parser.add_argument("--check", action="store_true", help="non-mutating validation (default)")
    parser.add_argument("--apply", action="store_true", help="apply and regenerate surfaces")
    parser.add_argument(
        "--allow-shared-checkout",
        action="store_true",
        dest="allow_shared",
        help="allow writes in a shared/main checkout",
    )
    args = parser.parse_args(argv)

    if not args.check and not args.apply:
        args.check = True
    if args.apply and args.check:
        print("error: --apply and --check are mutually exclusive", file=sys.stderr)
        return 1
    if args.allow_shared and not args.apply:
        print("error: --allow-shared-checkout requires --apply", file=sys.stderr)
        return 1

    if args.apply:
        if not shared_checkout.approve_mutation(ROOT, SCRIPT_NAME, args.allow_shared):
            return 1

    allow = ["--allow-shared-checkout"] if args.allow_shared else []
    mode = "apply" if args.apply else "check"

    print(f"[tools/run] === ci ({mode})")

    # Refresh marketplace skills and check they are current.
    refresh_cmd = [
        sys.executable,
        ".agents/skills/refreshing-installed-skills/scripts/refresh_installed_skills.py",
        f"--{mode}",
        *allow,
    ]
    _run(refresh_cmd)

    # Regenerate or check the repository index mesh.
    mesh_cmd = [
        sys.executable,
        ".agents/skills/generating-agent-mesh/scripts/generate_index_mesh.py",
        f"--{mode}",
        *allow,
    ]
    _run(mesh_cmd)

    # Validate the agent mesh (local links, doctrine routing, local skill custody).
    _run(
        [
            sys.executable,
            ".agents/skills/generating-agent-mesh/scripts/validate_agent_mesh.py",
            "--check",
        ]
    )

    # Validate repo-standards surface manifest.
    _run(
        [
            sys.executable,
            ".agents/skills/repo-standards/scripts/repo_standards.py",
            "--check",
        ]
    )

    # Validate image sidecars.
    _run(
        [
            sys.executable,
            "tools/validate_image_sidecars.py",
        ]
    )

    # Normalize/check image sidecar JSON formatting.
    norm_cmd = [
        sys.executable,
        "tools/normalize_image_sidecars.py",
    ]
    if args.apply:
        norm_cmd.append("--apply")
    _run(norm_cmd)

    # Check for whitespace/diff issues.
    _run(["git", "diff", "--check", "--", ".", ":(exclude).agents/skills"])

    print(f"[tools/run] ci ({mode}) passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
