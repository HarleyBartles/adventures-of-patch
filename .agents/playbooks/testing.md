# Testing playbook

## When

Use when selecting or running validation for any repository change.

## Required capabilities

- a capability for focused behavior checks when appropriate.
- a capability for evidence-backed validation and completion claims.

## Optional capabilities

- None.

## Required repository-owned skills

- None.
## Optional repository-owned skills

- None.

## Composition

Apply mechanical surfaces with `py -3 tools/run.py ci --apply`; check with `py -3 tools/run.py ci --check`. The tracked hook runs the complete staged-snapshot gate. Consumer command vectors are declared in `.agents/contracts/repo-standards-commands.json`. Record command, scope, state/SHA, environment, result, and the claim the result supports. Do not use apply-mode output as a substitute for a check result or rerun the complete gate ceremonially around an unchanged hooked commit. The canonical check validates selected standards, repository routing and composition, image sidecars, normalization, and whitespace integrity.

## Doctrine and contracts

- `.agents/contracts/repo-standards-commands.json`
- `.agents/contracts/adventures.visual_sidecar.adjacent.v1.schema.json`
- `.agents/contracts/image-sidecar-provenance.schema.json`

## Local commands and paths

See the composition and paths above.

## Evidence contract

Evidence is specific to the touched concern and names the source, decision, validation, and remaining uncertainty.

## Prohibited combinations

- Do not claim a capability ran when its output was not inspected.

## Runbook routing

- `.agents/runbooks/planning.md` routes here when this concern applies.
- `.agents/runbooks/implementing.md` routes here when this concern applies.
- `.agents/runbooks/code-review.md` routes here when this concern applies.
- `.agents/runbooks/pr.md` routes here when this concern applies.
