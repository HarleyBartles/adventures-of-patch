---
description: "Pull-request workflow and publication proof"
trigger: glob
globs:
  - "gh pr*"
  - "tools/run.py ci*"
  - ".agents/runbooks/pr.md"
  - ".github/workflows/ci.yml"
---
## Scope

This rule fires when creating, updating, or publishing a pull request.

For the canonical doctrine, read `.agents/runbooks/pr.md` `## Publication proof` and root `AGENTS.md` `## Source-of-truth split`.

For the step-by-step runbook, read `.agents/runbooks/pr.md`.

This file is a conditional rule trigger. It does not contain the doctrine; it only tells the runtime when to load the doctrine and runbook.
