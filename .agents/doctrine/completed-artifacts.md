## Scope

Completed planning-artifact custody truth for this repository.

## Doctrine

Completed plans, specifications, roadmaps, checkpoints, and similar execution artifacts are not retained in the tracked repository. Git history is the immutable record. A completed artifact is not an authority: do not use it as a source of canonical command sequences, a template for current implementation, or an authoritative example of repo conventions. Completion does not create a durable exception for an artifact type.

When a completed artifact leaves the tracked tree, an optional disposable convenience copy may live at `<main-checkout>/../_agent-scratch/<repo-name>/completed/<artifact-type>/` with no manifest, retention promise, or evidentiary role.

A successor artifact or current authority must exist before a completed item is retired. Mark it completed-awaiting-retirement while the successor is being verified, then remove the completed artifact from the tracked tree. Abandon unfinished work explicitly with a concise disposition for its owner. Promote enduring architecture decisions to the declared ADR home and operating rules to `.agents/doctrine/`, `.agents/contracts/`, or `.agents/playbooks/` before removal.

## Ownership

A suitable custody capability owns classification and promotion-before-removal. The `.agents/playbooks/completed-artifact-custody.md` playbook composes this doctrine with the applicable lifecycle runbook. Current conventions live in `.agents/doctrine/`, `.agents/contracts/`, `.agents/runbooks/`, `.agents/playbooks/`, and active plans and specifications.
