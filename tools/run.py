#!/usr/bin/env python3
"""Canonical validation runner for the Adventures of Patch repository."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import shared_checkout


ROOT = Path(__file__).resolve().parent.parent
SCRIPT_NAME = "tools/run"
MARKETPLACE_DEPLOYMENT = ".agents/plugins/marketplace-source/skills/repo-shape/scripts/deploy_operating_standards.py"
REPO_STANDARDS = ".agents/standards/_runtime/repo_standards.py"


def _run(command: list[str]) -> None:
    print("+ " + " ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)


def _marketplace_command(mode: str, allow_shared: bool = False) -> list[str]:
    command = [sys.executable, MARKETPLACE_DEPLOYMENT, f"--{mode}"]
    if mode == "apply":
        command.append("--yes")
        if allow_shared:
            command.append("--allow-shared-checkout")
    return command


def _standards_command(mode: str, allow_shared: bool = False) -> list[str]:
    command = [sys.executable, REPO_STANDARDS, f"--{mode}"]
    if mode == "apply":
        command.append("--yes")
        if allow_shared:
            command.append("--allow-shared-checkout")
    return command


def _validate_sidecars() -> None:
    _run([sys.executable, "tools/validate_image_sidecars.py"])


def _normalize_sidecars(*, apply: bool) -> None:
    command = [sys.executable, "tools/normalize_image_sidecars.py"]
    if apply:
        command.append("--apply")
    _run(command)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Adventures of Patch repository runner.")
    parser.add_argument("target", choices=["ci"], help="target to run")
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument("--check", action="store_true", help="validate without writing (default)")
    mode_group.add_argument("--apply", action="store_true", help="deploy and apply selected standards")
    parser.add_argument(
        "--allow-shared-checkout",
        action="store_true",
        dest="allow_shared",
        help="allow writes in the shared main checkout",
    )
    args = parser.parse_args(argv)
    applying = args.apply

    if args.allow_shared and not applying:
        parser.error("--allow-shared-checkout requires --apply")
    if applying and not shared_checkout.approve_mutation(ROOT, SCRIPT_NAME, args.allow_shared):
        return 1

    mode = "apply" if applying else "check"
    print(f"[tools/run] === ci ({mode})")

    _run(_marketplace_command(mode, args.allow_shared))
    if applying:
        _run(_standards_command("apply", args.allow_shared))
    _run(_standards_command("check"))

    _validate_sidecars()
    _normalize_sidecars(apply=applying)
    _run(["git", "diff", "--check"])

    print(f"[tools/run] ci ({mode}) passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
