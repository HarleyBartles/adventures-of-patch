# Code style runbook

This is the repository-specific overlay for implementation and documentation
style. It does not replace language-specific skills or portable workflow
guidance.

## When

Use when code, scripts, documentation, sidecars, or agent-facing surfaces change.

## Required skills

- `unslop-profiles` supplies the relevant implementation or writing profile.
- `writing-with-clarity` owns human-facing prose quality.
- `repo-worker-base` owns generated/source custody boundaries.

## Composition

Select the profile for the changed artifact, apply clarity to reader-facing
text, and bind both to the repository-specific conventions below.

## Doctrine and contracts

- `.agents/doctrine/mesh-policy.md`
- `.agents/contracts/adventures.visual_sidecar.adjacent.v1.schema.json`

## Local commands and paths

Use `py -3` for Windows-facing Python commands and the repo normalizers for
sidecar JSON.

## Evidence contract

Evidence includes focused lint/format/schema checks and explains any generated
surface changes.

## Prohibited combinations

- Do not use writing style guidance to change factual or canon meaning.
- Do not hand-edit generator-owned navigation or installed projections.

## Python and scripts

- Use `py -3` in Windows-facing commands and repository documentation.
- Repository mutation scripts use `tools/shared_checkout.py` for the repo's
  shared-checkout boundary.
- Repository hook source lives under `.githooks/`; `.git/hooks/` is not authored
  source custody.
- Keep generated navigation and installed skills under their owning generators;
  do not hand-edit their output.

## Documentation

- Keep root and scoped `AGENTS.md` files as routing surfaces, runbooks as
  repo-specific operational overlays, and doctrine as durable policy.
- Use descriptive Markdown links and repository-relative paths in tracked docs.
- Preserve Patch as the project character; never use Patch as an agent, actor,
  owner, or execution-lane label.

## Data and assets

- Preserve deterministic JSON formatting through the repository normalizers.
- Keep image sidecars adjacent to their governed assets and conformant with the
  sidecar schema and provenance rules.
