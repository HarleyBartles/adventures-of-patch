# Skill authoring and mesh policy

Status: approved first-slice implementation plan

## Objective

Establish the repository-local contracts that govern skill authoring and the
agent/documentation mesh before any `adventures-*` skill is authored.

## Scope

- Add `.agents/doctrine/skill-authoring-policy.md`.
- Add `.agents/doctrine/mesh-policy.md`.
- Add thin `.agents/AGENTS.md` and `.agents/doctrine/AGENTS.md` routing.
- Add the minimum root routing pointers needed to make the policies
  discoverable.
- Preserve marketplace-derived skill custody and the `adventures-*` local
  prefix boundary.

## Exclusions

- No `adventures-*` skill authoring or migration.
- No Patch identity cleanup.
- No line-ending normalization; existing churn is outside this slice.
- No marketplace plugin reintroduction.
- No manual repair of the whole existing `INDEX.md` tree.

## Acceptance

- The skill policy distinguishes skills from doctrine, guides, runbooks,
  references, scripts, READMEs, and generated indexes.
- The skill policy requires a baseline failure before a new skill is retained
  and requires RED/GREEN/REFACTOR verification.
- The mesh policy defines authored routers, generated indexes, human READMEs,
  canonical `.agents` custody, submodule boundaries, and self-healing.
- New policies are reachable from the root and `.agents` routing surfaces.
- No policy duplicates generic marketplace mechanics where this repository has
  a local rule.
- Existing unrelated working-tree churn is preserved and reported.

## Later follow-up

- Add the deterministic mesh generator and wrappers.
- Regenerate the complete index mesh.
- Add the required `.agents/guides/` stage guides.
- Reassess and author only the surviving local Adventures skills.
