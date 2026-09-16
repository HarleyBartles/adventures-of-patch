# Code review runbook

This is the repository-specific overlay for Adventures review concerns.

## When

Use for self-review, requested review, or review-feedback handling on a concrete
Adventures repository change.

## Required skills

- `requesting-code-review` owns review initiation.
- `receiving-code-review` owns feedback evaluation.
- `verification-before-completion` owns evidence-backed readiness claims.
- `unslop-profiles` supplies the applicable code-review profile.

## Composition

Review the exact change and published head, apply the repo-specific red flags
below, evaluate findings before repair, and require current validation before a
readiness claim.

## Doctrine and contracts

- `.agents/doctrine/adventures-project-doctrine.md`
- `.agents/doctrine/mesh-policy.md`

## Local commands and paths

The local complete check is `py -3 tools/run.py ci --check`. Review entrypoint:
`REVIEW.md`.

## Evidence contract

Evidence includes findings with paths, accepted/rejected disposition, fixes,
validation tied to the reviewed head, and accurate PR state.

## Prohibited combinations

- Do not use review output as validation evidence.
- Do not treat generated-image output as self-validating; inspect the actual
  image against its intended use and project canon.

## Review red flags

- marketplace-derived output overwrote `adventures-*` local custody;
- a generated index was hand-edited or descends into a gitlink/skill root;
- a runbook duplicates doctrine or generic workflow ownership;
- a deterministic compiler is presented as a judgment skill;
- a generated image is called accepted without direct inspection against the
  authored direction, intended use, and project canon;
- Patch is described as an agent or actor rather than a character;
- local validation is reported without matching remote branch and PR proof.

The local complete check command is `py -3 tools/run.py ci --check`.
