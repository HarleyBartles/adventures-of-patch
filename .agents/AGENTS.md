# Agent workspace routing

Read the applicable doctrine before changing agent-facing surfaces:

- `.agents/playbooks/repo-doctrine.md` for direct routing, discoverability,
  and surface custody;
- `.agents/doctrine/adventures-project-doctrine.md` for Adventures identity,
  source truth, readiness, resource, and publication invariants;
- `.agents/doctrine/skill-authoring-policy.md` before creating, migrating,
  reviewing, or retiring any repo-local skill;
- `.agents/runbooks/AGENTS.md` for stage runbook routing;
- `.agents/plugins/marketplace.json` for repository-owned skill custody and
  `.agents/contracts/operating-standards.json` plus `.agents/standards/provenance.json`
  for selected standard sources and deployed-resource provenance.

`.agents/` is agent-facing infrastructure. Keep ordinary project work in its
canonical project homes. The pinned marketplace source is a gitlink boundary;
local `adventures-*` skills are repository-owned custody. Ambient plugins are
not subscribed or projected into this checkout.
