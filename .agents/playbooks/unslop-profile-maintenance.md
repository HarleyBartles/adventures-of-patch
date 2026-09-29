# Unslop profile maintenance playbook

## When

Use during review when the same concrete agent mistake appears across two or three independent agents or attempts, suggesting sloppy behavior is getting through.

## Required capabilities

- A profile discovery and application capability for repository-owned operational guidance.
- A review capability that can distinguish independent evidence from repeated retelling.

## Optional capabilities

- None.

## Required repository-owned skills

- None.

## Optional repository-owned skills

- `adventures-project-doctrine` supplies the project source-truth boundary when a proposed profile touches canon or custody.

## Composition

Record the concrete mistake and the independent agent/attempt evidence in the review discussion. Raise a human review flag when the pattern recurs across roughly two or three independent instances. Decide whether a focused profile would prevent recurrence, link to the durable doctrine or capability that owns the rule, and keep the profile conditional and proportionate. One event is not enough by itself. Do not maintain an automated score, global incident ledger, keyword ban, or profile for already-owned binding policy. Profiles live under `.agents/unslop/` and must follow the adopted Unslop profile structure.

## Doctrine and contracts

- `.agents/contracts/unslop.json`
- `.agents/contracts/operating-standards.json`
- `.agents/doctrine/adventures-project-doctrine.md`

## Local commands and paths

Profiles are consumer-owned Markdown files under `.agents/unslop/`. Validate structure and routing with `py -3 tools/run.py ci --check`.

## Evidence contract

Evidence names the repeated behavior, distinct agents or attempts, why they are independent, the review flag, the owning doctrine/capability, and the decision to create, revise, or defer a profile.

## Prohibited combinations

- Do not treat a profile as binding doctrine or a historical incident log.
- Do not infer repetition from duplicate reports of one underlying attempt.
- Do not automatically create a profile or claim adherence from structural validation.

## Runbook routing

- `.agents/runbooks/code-review.md` routes here when this concern applies.
