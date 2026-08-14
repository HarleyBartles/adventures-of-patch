---
description: "Working in tools/ - load tooling doctrine and the implementation runbook"
trigger: glob
globs:
  - "tools/**"
---
## Scope

`tools/**`

When working in this scope:

- MUST READ `.agents/doctrine/repo-runbook-policy.md`
- MUST READ `.agents/runbooks/implementing.md`
- MUST INVOKE `/repo-worker-base`

The canonical validation command is `py -3 tools/run.py ci --check`.

This file is a conditional rule trigger. It does not contain the doctrine; it only tells the runtime when to load the doctrine and runbook from `.agents/`.
