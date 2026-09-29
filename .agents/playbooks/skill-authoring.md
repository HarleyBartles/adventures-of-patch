# Skill authoring playbook

## When

Use when creating, changing, reclassifying, or retiring an Adventures-local skill. Portable skill authoring belongs in the marketplace source repository.

## Required capabilities

- a capability for skill qualification, authoring, and verification.
- a capability for repository placement and composition.

## Optional capabilities

- None.

## Required repository-owned skills

- None.
## Optional repository-owned skills

- None.

## Composition

Local skills live under `.agents/skills/` and their exact names are declared in `.agents/plugins/marketplace.json` under `repo.local_skills`. Use the canonical repository check after edits. Keep reusable cross-project workflows and engineering capabilities in their source repository. Adventures skills encode project truth, readiness, canon, visual preproduction, and image acceptance. Do not create a local skill for a portable capability or deterministic procedure; do not edit marketplace-derived projections as authored source.

## Doctrine and contracts

- `.agents/doctrine/skill-authoring-policy.md`
- `.agents/doctrine/adventures-project-doctrine.md`

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
