# Marketplace generation runbook

This repo consumes portable plugins from the
`.agents/plugins/marketplace-source` submodule and keeps project-specific skills
locally.

## When

Use when advancing the marketplace gitlink, changing subscriptions, or
refreshing installed skill projections.

## Required skills

- `refreshing-installed-skills` owns deterministic projection refresh.
- `repo-standards` owns repository shape and subscription contracts.
- `generating-agent-mesh` owns generated navigation.

## Composition

Verify source custody, advance the gitlink/subscription manifest, refresh
installed skills, regenerate the mesh, then validate subscription/provenance
agreement.

## Doctrine and contracts

- `.agents/doctrine/mesh-policy.md`
- `.agents/doctrine/skill-authoring-policy.md`

## Local commands and paths

The source gitlink is `.agents/plugins/marketplace-source`; subscriptions are in
`.agents/plugins/marketplace.json`; apply/check through `tools/run.py ci`.

## Evidence contract

Evidence includes old/new gitlink SHA, subscribed plugins, installed/local skill
counts, provenance manifest, orphan handling, mesh result, and validation.

## Prohibited combinations

- Do not author portable skills in the consumer projection.
- Do not prune declared local skills or accept dangling skill routes.

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
