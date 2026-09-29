# Completed artifact custody playbook

## When

Use when an implementation completes an active plan, specification, roadmap, checkpoint, or related planning artifact.

## Required capabilities

- A capability for classifying artifacts and promoting durable decisions before removal.
- A capability for verifying implementation and replacement evidence.

## Optional capabilities

- None.

## Required repository-owned skills

- None.

## Optional repository-owned skills

- None.

## Composition

Verify completion, classify each artifact, promote enduring decisions into current doctrine or contracts, remove completed artifacts from Git, update direct routing, and validate the resulting tree. Do not move completed artifacts into a tracked archive or remove them before proving implementation complete.

## Doctrine and contracts

- `.agents/doctrine/completed-artifacts.md`
- `.agents/doctrine/adventures-project-doctrine.md`

## Local commands and paths

Active plans and specifications live in `.agents/plans/` and `.agents/specs/`. Use `py -3 tools/run.py ci --apply` for mechanical surfaces and the tracked hook for staged apply/check.

## Evidence contract

Evidence names completed implementation, removed paths, promoted durable destinations, current validation, and optional off-repo convenience copies.

## Prohibited combinations

- Do not retain completed plans as tracked archives.
- Do not describe an optional scratch copy as durable evidence.

## Runbook routing

- `.agents/runbooks/implementing.md` routes here when this concern applies.
- `.agents/runbooks/pr.md` routes here when this concern applies.
