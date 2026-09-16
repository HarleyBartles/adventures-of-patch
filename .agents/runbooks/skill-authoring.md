# Skill authoring runbook

This runbook covers project-owned Adventures skills. Portable skill authoring
belongs in the marketplace source repository.

## When

Use when creating, changing, reclassifying, or retiring an Adventures-local skill.

## Required skills

- `writing-skills` owns skill qualification, authoring, and verification.
- `repo-standards` owns repository placement and runbook composition rules.
- `generating-agent-mesh` owns generated navigation.

## Composition

Use `writing-skills` as capability owner, bind custody through local doctrine,
then regenerate and validate the repository mesh.

## Doctrine and contracts

- `.agents/doctrine/skill-authoring-policy.md`
- `.agents/doctrine/mesh-policy.md`

## Local commands and paths

Local skills live under `.agents/skills/` and are declared in
`.agents/plugins/marketplace.json`. Apply/check through `tools/run.py ci`.

## Evidence contract

Evidence includes qualification basis, exact owner/custody, tested behavior,
frontmatter/link validation, refresh preservation, and mesh result.

## Prohibited combinations

- Do not create a local skill for portable capability or deterministic procedure.
- Do not edit marketplace-derived projections as source.

## Local custody

- Local skills use the `adventures-*` prefix and live under `.agents/skills/`.
- Add every local skill's exact directory/frontmatter name to
  `.agents/plugins/marketplace.json` under `repo.local_skills` so refreshes do
  not prune it.
- Keep reusable cross-project workflow, writing, review, or engineering skills
  in the marketplace source rather than creating a repo-local duplicate.

## Local content boundary

- Adventures skills may encode project source-truth, readiness, canon, visual
  preproduction, and image-acceptance rules.
- Refresh local skill installation and mesh state with
  `py -3 tools/run.py ci --apply`; validate with
  `py -3 tools/run.py ci --check` when a standalone complete gate is required.
