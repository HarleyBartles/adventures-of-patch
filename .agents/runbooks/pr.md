# PR instructions and publication proof runbook

## When

Use when publishing repository work or verifying a pull request and its review state.

## Required capabilities

- a capability for safe source publication.
- a capability for verifying remote pull request state.

## Optional capabilities

- None.

## Required repository-owned skills

- `adventures-project-doctrine` is the repository-owned capability for this project concern.

## Optional repository-owned skills

- None.

## Composition

Commit completed implementation through the tracked hook, push the intended branch, open or update the requested pull request, and verify its exact head, base, draft/review state, and checks.

## Doctrine and contracts

- `.agents/doctrine/adventures-project-doctrine.md`
- `.agents/doctrine/completed-artifacts.md`

## Local commands and paths

Publication instructions and proof are also linked from `CONTRIBUTING.md`; local validation alone is not publication proof.

## Evidence contract

Evidence names the exact source and state, decisions, validation tied to that state, and remaining uncertainty or blockers.

## Prohibited combinations

- Do not claim review, validation, readiness, or publication without the evidence that proves it.

## Playbook routing

- `.agents/playbooks/testing.md` when that concern applies.
- `.agents/playbooks/security.md` when that concern applies.
- `.agents/playbooks/marketplace-generation.md` when that concern applies.
- `.agents/playbooks/completed-artifact-custody.md` when publication completes a tracked plan.
