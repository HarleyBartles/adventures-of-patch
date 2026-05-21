# Patch Domain Manifest

## Actor

Patch is the sole project-local agent for `HarleyBartles/adventures-of-patch`.

## Repo root

`HarleyBartles/adventures-of-patch`

## Actor root

`Patch/`

## Active lanes

- `Patch / project-director` - planning, issue shaping, source discipline, gate checks, routing decisions, verification, and repo-state judgement.
- `Patch / execution` - repo-local file mutation, binary asset landing, source zip creation, index updates, issue updates, commit/push, and return evidence.

## First-read surfaces

1. `INDEX.md`
2. `AGENTS.md`
3. `Patch/README.md`
4. `Patch/GOVERNANCE.md`
5. `Patch/ROUTING.md`
6. Relevant issue or project playbook

## Key governed surfaces

- `Patch/SKILLS/` - Patch-owned repo-resident executable capabilities.
- `playbooks/` - first-class Adventures project/domain playbooks.
- `assets/canon/patch/` - Patch visual canon.
- `assets/source-zips/` - source/import packages and package discovery index.
- `skills/` - committed project skill packages or source copies when intentionally committed.

## Publication expectation

Tracked repo mutation is not GREEN until committed, pushed to `main`, and remotely verified.

Use `Patch/CONTRACTS/WORKER_RETURN_CONTRACT.md` for returns.
