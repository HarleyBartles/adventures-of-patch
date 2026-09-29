# Implementation runbook

## When

Use when an approved plan or bounded repository change is ready for implementation.

## Required capabilities

- a capability for executing an approved plan.
- a capability for behavior validation and repository hygiene.

## Optional capabilities

- None.

## Required repository-owned skills

- `adventures-project-doctrine` is the repository-owned capability for this project concern.

## Optional repository-owned skills

- None.

## Composition

Select a suitable execution method, keep work within approved scope, preserve source custody, and validate the changed state before completion or publication. Apply mechanical surfaces with `py -3 tools/run.py ci --apply`; the normal commit hook runs the complete staged-snapshot gate.

## Doctrine and contracts

- `.agents/doctrine/adventures-project-doctrine.md`
- `.agents/contracts/repo-standards-commands.json`

## Local commands and paths

Agent infrastructure belongs under `.agents/`; project work belongs in established canonical homes. Plans and specs live under `.agents/plans/` and `.agents/specs/`. Local skills are declared in `.agents/plugins/marketplace.json`.

## Evidence contract

Evidence names the exact source and state, decisions, validation tied to that state, and remaining uncertainty or blockers.

## Prohibited combinations

- Do not claim review, validation, readiness, or publication without the evidence that proves it.

## Playbook routing

- `.agents/playbooks/code-style.md` when that concern applies.
- `.agents/playbooks/testing.md` when that concern applies.
- `.agents/playbooks/security.md` when that concern applies.
- `.agents/playbooks/skill-authoring.md` when that concern applies.
- `.agents/playbooks/marketplace-generation.md` when that concern applies.
- `.agents/playbooks/visual-production.md` when that concern applies.
- `.agents/playbooks/completed-artifact-custody.md` when completing a tracked plan or specification.
- `.agents/playbooks/repo-doctrine.md` when durable repository policy constrains implementation.
