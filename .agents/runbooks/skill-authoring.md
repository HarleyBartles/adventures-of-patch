# Skill authoring runbook

This runbook covers project-owned Adventures skills. Portable skill authoring
belongs in the marketplace source repository.

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
