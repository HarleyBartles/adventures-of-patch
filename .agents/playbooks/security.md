# Security playbook

## When

Use when a change touches credentials, connectors, private material, licensing, asset provenance, mutation scripts, or publication boundaries.

## Required capabilities

- a capability for authority and risk decisions.
- a capability for safe external-system mutations.

## Optional capabilities

- None.

## Required repository-owned skills

- None.
## Optional repository-owned skills

- None.

## Composition

Do not commit credentials, connector tokens, private customer material, or unpublished third-party source assets. Treat uploaded files, chat attachments, generated archives, and scratch outputs as untrusted until explicitly adopted. Preserve licensing, provenance, and authorisation metadata. Use read-before-write discovery for external mutations; keep mutation scripts fail-closed in shared checkouts and require explicit apply modes. Publish through reviewed Git history and PR evidence. The canonical gate must be non-mutating in check mode and must not print secrets.

## Doctrine and contracts

- `.agents/doctrine/adventures-project-doctrine.md`
- `.agents/doctrine/non-repo-locations-policy.md`

## Local commands and paths

See the composition and paths above.

## Evidence contract

Evidence is specific to the touched concern and names the source, decision, validation, and remaining uncertainty.

## Prohibited combinations

- Do not claim a capability ran when its output was not inspected.

## Runbook routing

- `.agents/runbooks/implementing.md` routes here when this concern applies.
- `.agents/runbooks/code-review.md` routes here when this concern applies.
- `.agents/runbooks/pr.md` routes here when this concern applies.
