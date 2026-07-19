---
name: adventures-asset-directory-source-packager
description: Use when an approved asset directory under assets must be discovered, packaged as a flat source zip, and published with evidence
metadata:
  source_id: adventures-asset-directory-source-packager
  status: active-local
  scope: Repo-local asset source packaging
  use_when: an existing assets directory needs bounded discovery, flat packaging, index updates, and publication proof
  do_not_use_when: visual inspection, image generation, image acceptance, or ambiguous asset placement is required
---

# Adventures asset directory source packager

This skill owns source-package publication for an already-authorized asset
directory. It does not own visual QA or canonisation.

## Required reads

- root `INDEX.md` and `AGENTS.md`;
- `playbooks/asset-package-landing.md`;
- `assets/INDEX.md` and `assets/source-zips/INDEX.md`;
- the target asset-family and directory indexes;
- `.agents/contracts/worker-return-contract.md`.

## Workflow

1. Confirm the target exists inside `assets/` and the source authority is
   explicit.
2. Discover the directory through the mesh and inspect its direct contents.
3. Stop on nested directories unless the authority explicitly allows them.
4. Update the target and parent navigation through the mesh generator.
5. Create a flat zip named after the containing folder and land it under the
   discovered source-zips home.
6. Validate archive shape, index links, commit, push, and verify the exact PR
   head before returning evidence.

## Stop conditions

Stop when approval, target mapping, package contents, index claims, or
publication proof is ambiguous. Do not call a zip canonical merely because it
exists; canonisation remains an explicit project decision.

## Output

Return target path, source authority, zip path, archive listing, changed
indexes, commit/branch/PR proof, working-tree state, and unresolved risks via
`.agents/contracts/worker-return-contract.md`.
