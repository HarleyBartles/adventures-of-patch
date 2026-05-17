---
name: patch-asset-directory-source-packager
description: repo-resident Patch execution capability for publishing an existing asset directory into a flat source zip in HarleyBartles/adventures-of-patch. use when Patch is bound to execution and must discover an existing assets/ directory, index its files, package the directory contents into a flat zip named after the containing folder, land the zip in assets/source-zips/, update index meshes, publish changes, and return evidence.
---

# Patch asset directory source packager

This is a repo-resident Patch skill surface, not a ChatGPT-native installed skill unless explicitly packaged later.

## Trigger

Use when Patch is bound to `Patch / execution` and receives an existing asset directory under `assets/` that needs to be discovered, indexed, flat-zipped, added to `assets/source-zips/`, and published.

This skill handles source/package publishing only; repo-canonical image inspection should default to `assets/view-surfaces/google-slides-registry.json`.

## Required inputs

- Target asset directory path under `Adventures-of-Patch/assets/`.
- Source authority: user instruction, issue, receipt, or accepted asset package context.
- Whether the asset directory is new or is updating an existing directory.

## Required reads

1. Root `INDEX.md`.
2. `AGENTS.md`.
3. `Patch/README.md`.
4. `Patch/GOVERNANCE.md`.
5. `Patch/ROUTING.md`.
6. `Patch/CONTRACTS/WORKER_RETURN_CONTRACT.md`.
7. `Patch/SKILLS/INDEX.md`.
8. `playbooks/asset-package-landing.md`.
9. `assets/INDEX.md`.
10. `assets/source-zips/INDEX.md`.
11. The target asset-family `INDEX.md`.
12. The target asset-directory `INDEX.md`, if it already exists.

## Workflow

1. Read the root and asset indexes first; do not rely on memory.
2. Confirm the target path is inside `assets/` and exists locally.
3. Inspect the target directory contents directly.
4. Reject nested directories for this packaging workflow unless the source authority explicitly allows them; if nested directories exist, stop and report the exact handling required.
5. Create or update the target directory `INDEX.md` so it lists every file directly inside the directory, including its own `INDEX.md`.
6. Update the parent asset-family `INDEX.md` to include the target directory if it is missing.
7. Update `assets/INDEX.md` only when a new top-level asset family has been introduced.
8. Create a zip named after the containing folder, for example `asset_class__environment__patch_mission_control.zip`.
9. Keep the zip flat: files must appear at the zip root, with no nested containing directory.
10. Include every file in the target directory, including the target directory `INDEX.md`.
11. Land the zip in the repo source-zips area discovered through `assets/INDEX.md` and the index mesh, expected currently as `assets/source-zips/`.
12. Update `assets/source-zips/INDEX.md` to list the new package.
13. Validate that every index entry points to a real file.
14. Validate zip contents by listing the archive and confirming there is no nested root folder.
15. Commit and push to `origin/main`.
16. Verify remote `origin/main` contains the asset directory files, updated indexes, and source zip.
17. Return using `Patch/CONTRACTS/WORKER_RETURN_CONTRACT.md`.

## Validation

- The target directory index lists only real files that exist in the directory.
- The parent asset-family index includes the target directory entry when needed.
- `assets/source-zips/INDEX.md` lists the landed source zip.
- The zip root contains only files, never a wrapper directory.
- Remote `origin/main` shows the committed path set after push.

## Stop conditions

Stop if the target path is outside `assets/`, the directory does not exist, approval is unclear, nested directories are present and not explicitly allowed, target paths conflict unexpectedly, the package contents disagree with the intended index entry, publication fails, or an index would point at files that were not actually landed.

## Return contract

Use `Patch/CONTRACTS/WORKER_RETURN_CONTRACT.md` for the final worker return shape and publication evidence.
