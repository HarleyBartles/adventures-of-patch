#!/usr/bin/env python3
"""Validate Adventures agent-surface custody and route integrity."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
RETIRED_TOKENS = (
    "adventures-frame-buster",
    "adventures-patch-image-preflight",
    "adventures-patch-image-qa",
    "adventures-deck-image-planner",
    "adventures-receipt-gen",
    "adventures-image-preflight",
    "adventures-asset-sheet-compiler",
    "adventures-asset-sheet-canoniser",
    "image-generation-resource-discipline",
    "Patch Image Gen",
)
FORBIDDEN_HOMES = ("Patch/", "docs/superpowers/plans/")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def operational_roots() -> tuple[Path, ...]:
    return (
        ROOT / "AGENTS.md",
        ROOT / "README.md",
        ROOT / ".agents" / "AGENTS.md",
        ROOT / ".agents" / "doctrine",
        ROOT / ".agents" / "guides",
        ROOT / ".agents" / "plugins",
        ROOT / ".agents" / "runbooks",
        ROOT / ".agents" / "skills",
        ROOT / "scripts",
    )


def iter_files(roots: Iterable[Path]) -> Iterable[Path]:
    for root in roots:
        if root.is_file():
            yield root
            continue
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or path.name == "INDEX.md":
                continue
            relative = path.relative_to(ROOT).as_posix()
            if relative.startswith("scripts/tests/"):
                continue
            if relative.startswith(".agents/plugins/marketplace-source/"):
                continue
            if relative.startswith(".agents/skills/") and not relative.startswith(
                ".agents/skills/adventures-"
            ):
                continue
            if path.suffix.lower() in {".md", ".json", ".py", ".ps1", ".sh"}:
                yield path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def local_link_findings(path: Path, text: str) -> list[str]:
    findings: list[str] = []
    for target in LINK_RE.findall(text):
        target = target.strip().strip("<>").split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:", "data:")):
            continue
        if "{" in target or "}" in target:
            continue
        if re.match(r"^[A-Za-z]:[\\/]", target):
            continue
        candidate = (path.parent / target).resolve()
        try:
            candidate.relative_to(ROOT.resolve())
        except ValueError:
            continue
        if not candidate.exists():
            findings.append(f"{path.relative_to(ROOT)} -> missing local link {target}")
    return findings


def route_findings(files: Iterable[Path]) -> list[str]:
    findings: list[str] = []
    for path in files:
        if path.resolve() == (ROOT / "scripts" / "validate_agent_mesh.py").resolve():
            continue
        text = read_text(path)
        for token in RETIRED_TOKENS:
            if token.lower() in text.lower():
                findings.append(f"{path.relative_to(ROOT)} contains retired route {token}")
    return findings


def skill_findings() -> list[str]:
    findings: list[str] = []
    skills_root = ROOT / ".agents" / "skills"
    local_dirs = sorted(p for p in skills_root.glob("adventures-*") if p.is_dir())
    for path in local_dirs:
        if not (path / "SKILL.md").is_file():
            findings.append(f"{path.relative_to(ROOT)} is missing SKILL.md")
    provenance_path = skills_root / ".provenance.json"
    if provenance_path.is_file():
        data = json.loads(read_text(provenance_path))
        copied = data.get("copied_skills", [])
        expected = {str(name) for name in copied}
        actual = {
            path.name
            for path in skills_root.iterdir()
            if path.is_dir() and not path.name.startswith("adventures-")
        }
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        if missing:
            findings.append(f".provenance.json projected skills are missing: {', '.join(missing)}")
        if extra:
            findings.append(f".agents/skills contains unprovenanced projections: {', '.join(extra)}")
        for name in sorted(expected):
            if not (skills_root / name / "SKILL.md").is_file():
                findings.append(f".agents/skills/{name} is missing SKILL.md")
        for name in copied:
            if str(name).startswith("adventures-"):
                findings.append(f".provenance.json claims local skill is marketplace-derived: {name}")
        if data.get("local_skill_prefixes") != ["adventures-"]:
            findings.append(".provenance.json has an unexpected local skill prefix policy")
    else:
        findings.append(".agents/skills/.provenance.json is missing")
    return findings


def plugin_findings() -> list[str]:
    findings: list[str] = []
    root = ROOT / ".agents" / "plugins"
    allowed_files = {"AGENTS.md", "INDEX.md", "marketplace.json"}
    for path in root.iterdir():
        if path.is_file() and path.name not in allowed_files:
            findings.append(f".agents/plugins contains unclassified file {path.name}")
        if path.is_dir() and path.name != "marketplace-source":
            findings.append(f".agents/plugins contains unclassified directory {path.name}")
    return findings


def doctrine_findings() -> list[str]:
    findings: list[str] = []
    router_text = "\n".join(
        read_text(path)
        for path in (ROOT / ".agents" / "AGENTS.md", ROOT / "AGENTS.md")
        if path.is_file()
    )
    for path in (ROOT / ".agents" / "doctrine").glob("*.md"):
        if path.name in {"AGENTS.md", "INDEX.md"}:
            continue
        if path.name not in router_text:
            findings.append(f"{path.relative_to(ROOT)} is not reachable from the agent routers")
    return findings


def git_changed_paths(ref: str) -> list[tuple[str, str]]:
    result = subprocess.run(
        ["git", "diff", "--name-status", f"{ref}...HEAD"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or f"could not inspect {ref}")
    changed: list[tuple[str, str]] = []
    for line in result.stdout.splitlines():
        status, _, path = line.partition("\t")
        if path:
            changed.append((status, path.replace("\\", "/")))
    return changed


def changed_home_findings(ref: str | None) -> list[str]:
    if not ref:
        return []
    findings: list[str] = []
    for status, path in git_changed_paths(ref):
        if status.startswith("D"):
            continue
        if any(path.startswith(home) for home in FORBIDDEN_HOMES):
            findings.append(f"changed path remains in forbidden legacy home: {status} {path}")
    return findings


def collect_findings(changed_from: str | None = None) -> list[str]:
    files = tuple(iter_files(operational_roots()))
    findings: list[str] = []
    for path in files:
        findings.extend(local_link_findings(path, read_text(path)))
    findings.extend(route_findings(files))
    findings.extend(skill_findings())
    findings.extend(plugin_findings())
    findings.extend(doctrine_findings())
    findings.extend(changed_home_findings(changed_from))
    return sorted(set(findings))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="explicit validation mode")
    parser.add_argument("--changed-from", help="only apply legacy-home checks to this diff base")
    args = parser.parse_args(argv)
    findings = collect_findings(args.changed_from)
    if findings:
        print("Agent mesh findings:")
        print("\n".join(f"- {finding}" for finding in findings))
        return 1
    scope = f" changed from {args.changed_from}" if args.changed_from else ""
    print(f"OK agent mesh: no findings{scope}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
