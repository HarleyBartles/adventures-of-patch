# Agent workspace routing

Read the applicable doctrine before changing agent-facing surfaces:

- `.agents/doctrine/mesh-policy.md` for routing, generated navigation,
  discoverability, and surface custody;
- `.agents/doctrine/adventures-project-doctrine.md` for Adventures identity,
  source truth, readiness, resource, and publication invariants;
- `.agents/doctrine/skill-authoring-policy.md` before creating, migrating,
  reviewing, or retiring any repo-local skill;
- `.agents/runbooks/AGENTS.md` for stage runbook routing;
- `.agents/plugins/marketplace.json` and `.agents/skills/.provenance.json` for
  marketplace-derived skill custody.

`.agents/` is agent-facing infrastructure. Keep ordinary project work in its
canonical project homes. The pinned marketplace source is a gitlink boundary;
local `adventures-*` skills are repository-owned custody and must survive
marketplace refresh.
