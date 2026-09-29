# Code review runbook

## When

Use for self-review, requested review, or review-feedback handling on a concrete repository change.

## Required capabilities

- a capability for initiating and conducting review.
- a capability for evaluating feedback and verifying corrections.

## Optional capabilities

- None.

## Required repository-owned skills

- `adventures-project-doctrine` is the repository-owned capability for this project concern.

## Optional repository-owned skills

- None.

## Composition

Review the exact change and intended published head, apply repository-specific red flags, evaluate findings before repair, and require current validation before a readiness claim. Raise a human review flag when the same concrete agent mistake appears across roughly two or three independent agents or attempts; route to profile maintenance only when that evidence exists.

## Doctrine and contracts

- `.agents/doctrine/adventures-project-doctrine.md`
- `.agents/contracts/operating-standards.json`
- `.agents/contracts/unslop.json`

## Local commands and paths

Review entrypoint: `REVIEW.md`. Complete check: `py -3 tools/run.py ci --check`.

## Evidence contract

Evidence names the exact source and state, decisions, validation tied to that state, and remaining uncertainty or blockers.

## Prohibited combinations

- Do not use review output as validation evidence.
- Do not call generated-image output accepted without inspecting the actual image against its authored direction, intended use, and project canon.
- Do not describe Patch as an agent or actor rather than the project character.
- Do not report local validation without matching the claim to the exact reviewed or published head.
- Do not make a runbook duplicate doctrine or generic capability ownership.

## Unslop profile routing

When the same concrete agent mistake recurs across roughly two or three independent agents or attempts, invoke `$unslop-profiles` and route to `.agents/playbooks/unslop-profile-maintenance.md`. Do not infer repetition from duplicate reports of one attempt.

## Playbook routing

- `.agents/playbooks/unslop-profile-maintenance.md` when the same concrete mistake recurs across roughly two or three independent agents or attempts.
- `.agents/playbooks/code-style.md` for changed code or documentation.
- `.agents/playbooks/testing.md` for validation evidence.
- `.agents/playbooks/security.md` when protected material, provenance, or mutations are in scope.
- `.agents/playbooks/repo-doctrine.md` when a finding concerns a durable repository invariant.
