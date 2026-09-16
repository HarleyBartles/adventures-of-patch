# Testing runbook

This is the repository-specific command and check map for validation.

## When

Use when selecting or running validation for any repository change.

## Required skills

- `test-driven-development` owns behavior-change test order.
- `verification-before-completion` owns evidence freshness and claims.
- `repo-worker-base` owns staged-gate and CI boundaries.

## Composition

Use focused tests while iterating, the normal hook for the complete staged
product, and standalone full validation only for diagnosis or explicit parity.

## Doctrine and contracts

- `.agents/contracts/repo-standards-commands.json`
- `.agents/contracts/adventures.visual_sidecar.adjacent.v1.schema.json`
- `.agents/contracts/image-sidecar-provenance.schema.json`

## Local commands and paths

- Tracked hook entrypoint: `.githooks/pre-commit`.
- Local hook binding: `git config core.hooksPath .githooks`.
- See the canonical capability map below.

## Evidence contract

Evidence records command, scope, state/SHA, environment, result, and the claim
the result supports.

## Prohibited combinations

- Do not use apply-mode output as a substitute for a check result.
- Do not rerun the complete gate ceremonially around an unchanged hooked commit.

## Canonical capabilities

- Apply mechanical surfaces: `py -3 tools/run.py ci --apply`.
- Check the committed or otherwise explicitly selected tree:
  `py -3 tools/run.py ci --check`.
- The consumer command vectors are declared in
  `.agents/contracts/repo-standards-commands.json`.
- The active tracked hook delegates to the canonical staged-snapshot hook
  shipped by `repo-standards`; `.git/hooks/pre-commit` is a compatibility copy
  for the current portable validator, not the repository custody surface.

## Repository-specific checks

The canonical check validates refreshed skill provenance, generated index mesh,
agent routing and local skill custody, repo-standard surfaces, image sidecars,
sidecar normalization, and whitespace/diff integrity.
