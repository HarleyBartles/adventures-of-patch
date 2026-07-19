---
name: adventures-project-readiness
description: Use when an Adventures of Patch idea, issue, or deck request must be classified before framing, visual preparation, or PPTX production
metadata:
  source_id: adventures-project-readiness
  status: active-local
  scope: Adventures project readiness routing
  use_when: issue or idea may be seed-ready, frame-ready, asset-ready, or playbook-ready
  do_not_use_when: generic repository work has no Adventures production or readiness boundary
---

# Adventures project readiness

## Overview

An Adventures idea is not production-ready merely because it has a good theme.
Use the readiness ladder to prevent the production playbook from inventing a
frame, lesson, cast, world, visual language, or asset package while working.

## Owned decision

Classify the current source as exactly one of:

| State | Meaning | Next owner |
| --- | --- | --- |
| `seed-ready` | useful topic or adventure idea, but core teaching/frame decisions are open | `adventures-frame-buster` |
| `frame-ready` | world, lesson, anti-pattern, positive pattern, Patch role, mappings, continuity, and audience application are green | `adventures-visual-preproduction` |
| `asset-ready` | reusable visual language and required references are QA-accepted and packaged | end-to-end PPTX playbook |
| `playbook-ready` | frame-ready and asset-ready; production may begin without inventing missing foundations | end-to-end PPTX playbook |

## Required handoff

Read `playbooks/pre-playbook-adventure-readiness.md` and return a compact
readiness record containing:

- source issue or brief and evidence location;
- current state and the failed gate, if any;
- frame basis or the route to obtain one;
- asset basis, QA status, and provisional/canonical status;
- next owner, blocker, and stop condition.

Route framing to `adventures-frame-buster`. Route visual requirements,
reference discovery, and candidate planning to
`adventures-visual-preproduction`. Route every generated or edited image
acceptance decision to `adventures-image-qa`.

## Hard boundaries

- Do not build a deck, generate body-slide images, or call an issue green when
  a required readiness state is absent.
- Do not silently invent a frame, canon, actor identity, or approval.
- Patch is the project character and visual canon, never an agent or execution
  owner.
- A reference, asset sheet, contact sheet, source zip, or thumbnail is not
  body-slide art without explicit storyboard-mode approval.

## Common mistake

“The issue is clear enough” is not a readiness result. Name the state, show the
evidence, and route the missing gate.
