---
name: adventures-project-readiness
description: Use when an Adventures of Patch idea, issue, or artifact request must be classified before framing, visual preparation, or downstream production
metadata:
  source_id: adventures-project-readiness
  status: active-local
  scope: Adventures project readiness routing
  use_when: issue or idea may be seed-ready, frame-ready, asset-ready, or runbook-ready, or its frame may be weak
  do_not_use_when: generic repository work has no Adventures production or readiness boundary
---

# Adventures project readiness

## Owned decision

Classify the current source as exactly one of:

| State | Meaning | Next owner |
| --- | --- | --- |
| `seed-ready` | Core teaching or frame decisions remain open. | Frame gate in the readiness runbook. |
| `frame-ready` | The frame contract is green. | `directing-visual-stories` through the visual-production runbook |
| `asset-ready` | Required visual references are accepted and packaged. | Requested downstream workflow |
| `runbook-ready` | Frame and asset readiness are green. | Requested downstream workflow |

## Local contract

Read `.agents/contracts/adventure-readiness.md` for the repository's
frame evidence, readiness record, and production boundary. Route visual
requirements to `directing-visual-stories`; the visual-production
runbook owns the wider production and review sequence.

## Boundary

Do not advance to a later owner when the required state or evidence is absent.
Do not invent readiness evidence or approval.
