# Code style playbook

## When

Use when code, scripts, documentation, sidecars, or agent-facing surfaces change.

## Required capabilities

- a suitable coding or writing capability for the changed artifact.
- repository guidance for generated and source custody.

## Optional capabilities

- None.

## Required repository-owned skills

- None.
## Optional repository-owned skills

- None.

## Composition

Use `py -3` for Windows-facing Python commands and repository normalizers for sidecar JSON. Repository mutation scripts use `tools/shared_checkout.py`. Keep root and scoped `AGENTS.md` files as routing surfaces, playbooks as topical compositions, and doctrine as durable policy. Preserve Patch as the project character, never as an agent, actor, owner, or execution-lane label. Preserve deterministic JSON formatting and keep image sidecars adjacent to governed assets.

## Doctrine and contracts

- `.agents/doctrine/adventures-project-doctrine.md`
- `.agents/contracts/adventures.visual_sidecar.adjacent.v1.schema.json`

## Local commands and paths

See the composition and paths above.

## Evidence contract

Evidence is specific to the touched concern and names the source, decision, validation, and remaining uncertainty.

## Prohibited combinations

- Do not claim a capability ran when its output was not inspected.

## Runbook routing

- `.agents/runbooks/design.md` routes here when this concern applies.
- `.agents/runbooks/implementing.md` routes here when this concern applies.
- `.agents/runbooks/code-review.md` routes here when this concern applies.
