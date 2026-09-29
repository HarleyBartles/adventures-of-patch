# Marketplace source and standards playbook

## When

Use when advancing the marketplace-source gitlink, changing local skill ownership, or adopting/updating selected standards. Ambient marketplace plugins are not subscribed or projected into this repository.

## Required capabilities

- a capability for repository-owned plugin and standard source management.
- a capability for validating repository standard adoption.

## Optional capabilities

- None.

## Required repository-owned skills

- None.
## Optional repository-owned skills

- None.

## Composition

The source gitlink is `.agents/plugins/marketplace-source`; selected standards are declared in `.agents/contracts/operating-standards.json` and deployed into `.agents/standards/`. Repository-owned skills remain under `.agents/skills/` and are declared exactly in `.agents/plugins/marketplace.json`. Advance the gitlink, deploy selected standards, update composition and consumer runner as one coherent migration, then run `py -3 tools/run.py ci --apply` and `--check`. Do not create plugin subscriptions for ambient plugins, edit marketplace-derived projections as source, or reintroduce generated navigation indexes.

## Doctrine and contracts

- `.agents/contracts/operating-standards.json`
- `.agents/contracts/repo-standards-commands.json`
- `.agents/doctrine/skill-authoring-policy.md`

## Local commands and paths

See the composition and paths above.

## Evidence contract

Evidence is specific to the touched concern and names the source, decision, validation, and remaining uncertainty.

## Prohibited combinations

- Do not claim a capability ran when its output was not inspected.

## Runbook routing

- `.agents/runbooks/implementing.md` routes here when this concern applies.
- `.agents/runbooks/code-review.md` routes here when this concern applies.
- `.agents/runbooks/pr.md` routes here when this concern applies.
