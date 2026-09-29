# Repository doctrine playbook

## When

Use when a task depends on project identity, source truth, non-repository locations, canon, or durable repository policy.

## Required capabilities

- A capability for locating and applying repository-owned doctrine.
- A capability for distinguishing authoritative source from contextual reports and generated material.

## Optional capabilities

- None.

## Required repository-owned skills

- `adventures-project-doctrine` supplies project identity, source truth, and canon boundaries.

## Optional repository-owned skills

- None.

## Composition

Read the applicable doctrine before choosing a workflow. Resolve repository facts from the live tree and tracked sources; use issue, chat, attachment, and cache material as context unless adopted by the repository. Doctrine states durable constraints and does not orchestrate workflow stages.

## Doctrine and contracts

- `.agents/doctrine/adventures-project-doctrine.md`
- `.agents/doctrine/non-repo-locations-policy.md`
- `.agents/doctrine/completed-artifacts.md`
- `.agents/doctrine/repo-runbook-policy.md`

## Local commands and paths

Doctrine lives under `.agents/doctrine/`; the repository router is `AGENTS.md`. Navigate using direct links and canonical directories.

## Evidence contract

Evidence cites the live authoritative file or tracked source and separates it from contextual claims.

## Prohibited combinations

- Do not turn doctrine into a lifecycle checklist or use it to override user-owned choices.
- Do not treat generated caches or unadopted artifacts as repository truth.

## Runbook routing

- `.agents/runbooks/design.md` routes here when this concern applies.
- `.agents/runbooks/implementing.md` routes here when this concern applies.
- `.agents/runbooks/code-review.md` routes here when this concern applies.
