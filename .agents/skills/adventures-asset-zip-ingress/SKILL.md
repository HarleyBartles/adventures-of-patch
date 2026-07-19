---
name: adventures-asset-zip-ingress
description: Use when an incoming asset zip must be inspected, classified, and safely landed into the Adventures repository with publication evidence
metadata:
  source_id: adventures-asset-zip-ingress
  status: active-local
  scope: Bounded incoming asset package inspection and landing
  use_when: an approved or explicitly scoped zip is present in assets/source-zips/incoming/
  do_not_use_when: no source authority exists, visual QA is required, or the task is ordinary asset editing
---

# Adventures asset zip ingress

Incoming zips are evidence and input, never canon. The canonical drop zone is
`assets/source-zips/incoming/`; preserved source packages belong under
`assets/source-zips/` after inspection and classification.

## Required reads

- root `INDEX.md` and `AGENTS.md`;
- `assets/INDEX.md`, `assets/source-zips/INDEX.md`, and the incoming directory
  guide;
- the relevant issue or receipt;
- `playbooks/asset-package-landing.md`;
- `.agents/contracts/worker-return-contract.md`.

## Workflow

1. Confirm source authority and enumerate incoming zips; stop on multiple
   unscoped payloads.
2. Inspect the selected archive without promoting its contents to canon.
3. Classify each file against the repository asset taxonomy and resolve target
   paths before mutation.
4. Rebuild a repo-shaped source package when the incoming archive is not the
   canonical taxonomy package.
5. Update affected indexes with the mesh generator and validate package shape.
6. Commit, push, verify the exact PR head, then remove the ingress payload and
   scratch extraction only after publication proof exists.

## Stop conditions

Stop for unclear authority, unreadable contents, taxonomy ambiguity, path
conflicts, multiple unscoped zips, publication failure, or any cleanup that
would precede remote proof.

## Required return

Record ingress path, cleanup status, retained/deleted inputs, target paths,
package/index evidence, publication proof, and blockers in
`.agents/contracts/worker-return-contract.md`.
