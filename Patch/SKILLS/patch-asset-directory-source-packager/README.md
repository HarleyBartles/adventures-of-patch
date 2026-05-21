# Patch asset directory source packager

Repo-resident Patch execution capability for publishing an existing asset directory under `assets/`.

## Purpose

Given an approved or otherwise source-authorized asset directory already present in the repo, Patch can:

- discover the directory through the repo index mesh;
- inspect the directory contents;
- update or create the directory `INDEX.md` so it lists every direct file;
- update the parent asset-family `INDEX.md` when the directory is new;
- create a flat source zip named after the containing folder;
- land that zip in `assets/source-zips/`;
- update `assets/source-zips/INDEX.md`;
- commit, push, and return publication evidence.

## Trigger

Use when Patch is bound to `Patch / execution` and receives an existing asset directory under `assets/` that needs to be discovered, indexed, flat-zipped, added to `assets/source-zips/`, and published.

This skill handles source/package publishing only; repo-canonical image inspection should default to repo-indexed contact-sheet dispatch/intake packages built by the Patch contact-sheet exporter.

## Required reads

- `INDEX.md`
- `AGENTS.md`
- `Patch/README.md`
- `Patch/GOVERNANCE.md`
- `Patch/ROUTING.md`
- `Patch/CONTRACTS/WORKER_RETURN_CONTRACT.md`
- `Patch/SKILLS/INDEX.md`
- `playbooks/asset-package-landing.md`
- `assets/INDEX.md`
- `assets/source-zips/INDEX.md`
- The target asset-family `INDEX.md`
- The target asset-directory `INDEX.md`, if it already exists

## Workflow

1. Read the root and asset indexes first.
2. Confirm the target path is inside `assets/` and exists locally.
3. Inspect the target directory contents directly.
4. Reject nested directories unless explicitly allowed.
5. Create or update the target directory `INDEX.md`.
6. Update the parent asset-family `INDEX.md` if needed.
7. Update `assets/INDEX.md` only for a new top-level asset family.
8. Create a flat zip named after the containing folder.
9. Land the zip in `assets/source-zips/`.
10. Update `assets/source-zips/INDEX.md`.
11. Validate index entries and archive shape.
12. Commit and push to `origin/main`.
13. Verify remote `origin/main` contains the committed paths.
14. Return using the worker return contract.

## Validation

- The target directory index lists only real files.
- The parent asset-family index includes the target directory when needed.
- `assets/source-zips/INDEX.md` lists the landed source zip.
- The zip root contains only files.
- Remote `origin/main` shows the committed path set after push.

## Stop conditions

Stop if the target path is outside `assets/`, the directory does not exist, approval is unclear, nested directories are present and not explicitly allowed, target paths conflict unexpectedly, the package contents disagree with the intended index entry, publication fails, or an index would point at files that were not actually landed.

## Return contract

Use `../../../Patch/CONTRACTS/WORKER_RETURN_CONTRACT.md` for the final worker return shape and publication evidence.

## Related playbook

See `../../../playbooks/asset-package-landing.md` for the repo workflow this skill implements.
