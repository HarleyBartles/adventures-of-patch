---
name: adventures-project-readiness
description: Use when an Adventures of Patch idea, issue, or deck request must be classified before framing, visual preparation, or PPTX production
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
| `frame-ready` | The frame contract is green. | `adventures-visual-preproduction` |
| `asset-ready` | Required visual references are accepted and packaged. | End-to-end PPTX runbook |
| `runbook-ready` | Frame and asset readiness are green. | End-to-end PPTX runbook |

## Local contract

Read `.agents/runbooks/pre-runbook-adventure-readiness.md` for the repository's
frame evidence, readiness record, and production boundary. Route visual
requirements to `adventures-visual-preproduction` and image acceptance to
`adventures-image-qa`.

## Boundary

Do not advance to a later owner when the required state or evidence is absent.
Do not invent readiness evidence or approval.
