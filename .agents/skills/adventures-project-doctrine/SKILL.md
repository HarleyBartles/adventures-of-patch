---
name: adventures-project-doctrine
description: Use when an Adventures of Patch task needs project identity, source truth, readiness, visual-resource, or publication invariants before choosing a workflow
metadata:
  source_id: adventures-project-doctrine
  status: active-local
  scope: Triggerable routing into Adventures project doctrine
  use_when: task needs a project invariant or source-of-truth decision before execution
  do_not_use_when: task is generic repository work with no Adventures-specific boundary
  use_with: using-superpowers-plus, base-doctrine, matching local runbook
---

# Adventures project doctrine router

This is a routing entrypoint, not a second doctrine store. Read only the
smallest canonical Adventures rule surface needed for the task.

## Route by decision

| Need | Read |
| --- | --- |
| Adventures identity, source truth, readiness, or publication invariants | `.agents/doctrine/adventures-project-doctrine.md` |
| Agent/documentation custody, generated indexes, gitlinks, or mesh safety | `.agents/doctrine/mesh-policy.md` |
| Creating, adapting, assessing, or retiring a local skill | `.agents/doctrine/skill-authoring-policy.md` |
| Design, planning, implementation, or review overlay | matching file under `.agents/runbooks/` |
| Readiness/frame, visual preparation, or image acceptance | `adventures-project-readiness`, `adventures-visual-preproduction`, or `adventures-image-qa` |

## Routing rules

1. Identify the decision that could be wrong.
2. Read the matching doctrine or runbook before acting.
3. Keep the canonical rule's path and evidence in the plan or return.
4. Do not duplicate doctrine in this router or treat it as approval.

## Hard boundaries

- Do not invent project law from memory, marketplace caches, or old Patch actor
  documents.
- Do not load every doctrine file when one route answers the decision.
- Patch is the project character and visual canon, not an agent or actor
  identity.
