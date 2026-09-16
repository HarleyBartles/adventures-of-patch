# Planning runbook

This is the repository-specific overlay for Adventures planning custody.

## When

Use after design/spec requirements are settled and an executable Adventures
implementation plan is required.

## Required skills

- `writing-plans` owns executable plan construction.
- `adventures-project-readiness` supplies readiness state for visual-production work.
- `handoff-gates` owns plan-readiness evaluation.

## Composition

Run `writing-plans` as the stage owner, bind the plan to current readiness and
repo custody, then apply the plan-readiness gate before execution handoff.

## Doctrine and contracts

- `.agents/doctrine/adventures-project-doctrine.md`
- `.agents/doctrine/completed-artifacts.md`
- `.agents/contracts/adventure-readiness.md`

## Local commands and paths

Active plans live in `.agents/plans/`; associated specs live in
`.agents/specs/`. Use `py -3 tools/run.py ci --check` only when standalone
complete validation is required.

## Evidence contract

Evidence identifies the approved source/spec, readiness state, exact plan path,
named execution lane, validation commands, and plan-readiness result.

## Prohibited combinations

- Do not use a plan to settle unresolved design or canon decisions.
- Do not retain completed plans/specs as tracked archives.

## Local custody and gates

- Implementation plans live under `.agents/plans/`; associated specifications
  live under `.agents/specs/`.
- Visual-production work uses the seed-ready, frame-ready, asset-ready, and
  runbook-ready classifications defined in
  `.agents/contracts/adventure-readiness.md`.
- Patch canon, visual-preproduction, and image-acceptance requirements come
  from the corresponding Adventures skills and project runbooks.
