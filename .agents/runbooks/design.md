# Design runbook

## When

Use when a request needs shaping before requirements are settled.

## Required capabilities

- a capability for clarifying intent and exploring design alternatives.
- a capability for project readiness and source-truth assessment.

## Optional capabilities

- None.

## Required repository-owned skills

- `adventures-project-doctrine` is the repository-owned capability for this project concern.
- `adventures-project-readiness` is the repository-owned capability for this project concern.

## Optional repository-owned skills

- None.

## Composition

Clarify the requested outcome, inspect live source truth and canon, resolve human-owned design decisions, and record the evidence and constraints needed by planning. Do not move to planning while material design decisions remain open.

## Doctrine and contracts

- `.agents/doctrine/adventures-project-doctrine.md`
- `.agents/contracts/adventure-readiness.md`

## Local commands and paths

Read `README.md` and direct canonical sources under `docs/`, `build/`, `style/`, `published/`, and `workbench/`; use `py -3 tools/run.py ci --check` when standalone validation is needed.

## Evidence contract

Evidence names the exact source and state, decisions, validation tied to that state, and remaining uncertainty or blockers.

## Prohibited combinations

- Do not claim review, validation, readiness, or publication without the evidence that proves it.

## Playbook routing

- `.agents/playbooks/visual-production.md` when that concern applies.
- `.agents/playbooks/repo-doctrine.md` when project truth or canon shapes the design.
- `.agents/playbooks/code-style.md` when that concern applies.
