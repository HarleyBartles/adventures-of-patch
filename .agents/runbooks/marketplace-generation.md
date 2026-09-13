# Marketplace generation runbook

This repo consumes portable plugins from the
`.agents/plugins/marketplace-source` submodule and keeps project-specific skills
locally.

## Source custody

- Portable skills are authored and reviewed in the marketplace source repo.
  This repo records their source commit through the submodule gitlink.
- Project-owned skills remain under `.agents/skills/adventures-*/` and are
  declared exactly in `.agents/plugins/marketplace.json` under
  `repo.local_skills`.
- Do not edit marketplace-derived installed skills in this repo. Change the
  source package, advance the gitlink, and refresh instead.

## Refresh and validation

- Preview a refresh with
  `py -3 .agents/skills/refreshing-installed-skills/scripts/refresh_installed_skills.py --check`.
- Apply through `py -3 tools/run.py ci --apply`, which refreshes subscribed
  plugins and regenerates the mesh.
- Validate with `py -3 tools/run.py ci --check` when a standalone complete gate
  is required; normal commits use the staged-snapshot pre-commit hook.
- A refresh is incomplete if an installed skill routes to a package that is not
  subscribed in `.agents/plugins/marketplace.json`.
