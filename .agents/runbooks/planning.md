# Planning runbook

## When

Use after design and specification requirements are settled and an executable implementation plan is required.

## Required capabilities

- a capability for executable plan construction.
- a capability for evaluating readiness and handoff.

## Optional capabilities

- None.

## Required repository-owned skills

- `adventures-project-doctrine` is the repository-owned capability for this project concern.

## Optional repository-owned skills

- None.

## Composition

Bind the plan to the approved source/spec, readiness, repository custody, validation, and handoff evidence. Do not use a plan to settle unresolved design or canon decisions.

## Doctrine and contracts

- `.agents/doctrine/adventures-project-doctrine.md`
- `.agents/doctrine/completed-artifacts.md`
- `.agents/contracts/adventure-readiness.md`

## Local commands and paths

Active plans live in `.agents/plans/`; associated specifications live in `.agents/specs/`.

## Evidence contract

Evidence names the exact source and state, decisions, validation tied to that state, and remaining uncertainty or blockers.

## Prohibited combinations

- Do not claim review, validation, readiness, or publication without the evidence that proves it.

## Playbook routing

- `.agents/playbooks/testing.md` when that concern applies.
- `.agents/playbooks/visual-production.md` when that concern applies.
