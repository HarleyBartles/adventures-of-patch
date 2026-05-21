---
name: patch-asset-zip-ingress
description: repo-resident Patch execution capability for ingesting asset zips into HarleyBartles/adventures-of-patch. use when Patch is bound to execution and must inspect a zip of accepted or candidate assets, classify contents, route files to the repo asset taxonomy, rebuild source packages where appropriate, update indexes, publish changes, clean the canonical ingress lane, and return evidence.
---

# Patch asset zip ingress

This is a repo-resident Patch skill surface, not a ChatGPT-native installed skill unless explicitly packaged for installation later.

## Canonical ingress root

- Canonical local drop zone: `Patch/INGRESS/asset-zips/`
- Incoming zip payloads are input evidence, not canon.
- Repo-preserved source packages belong under `assets/source-zips/` only after inspection, classification, or rebuild.
- The ingress directory itself must remain discoverable in repo through a tracked doc surface such as `README.md` or `INDEX.md`, but incoming zip payloads must not be tracked.

## Trigger

Use when Patch is bound to `Patch / execution` and receives a zip or package of visual assets, markdown sidecars, receipt evidence, or source files that may need to be landed into `HarleyBartles/adventures-of-patch`.

This skill handles package or import work only; repo-canonical image inspection should default to `assets/view-surfaces/google-slides-registry.json`.

## Required reads

1. Root `INDEX.md`.
2. `AGENTS.md`.
3. `Patch/README.md`.
4. `Patch/GOVERNANCE.md`.
5. `Patch/ROUTING.md`.
6. `Patch/CONTRACTS/WORKER_RETURN_CONTRACT.md`.
7. `playbooks/asset-package-landing.md`.
8. Relevant issue or receipt.
9. `assets/INDEX.md` and `assets/source-zips/INDEX.md`.
10. `Patch/INGRESS/asset-zips/` and its tracked doc surface.
11. Target asset directory indexes.

## Workflow

1. Confirm source authority: issue, receipt, user approval, or explicit bounded intake scope.
2. Discover zip payloads only from `Patch/INGRESS/asset-zips/` unless the dispatch explicitly overrides the ingress root.
3. Process one zip per ingress run unless the dispatch explicitly authorizes a batch.
4. Stop if multiple unscoped zips are present in the ingress folder.
5. Inspect the selected zip contents without promoting them to canon.
6. Classify each file by repo taxonomy.
7. Decide target paths for individual assets, sidecars, receipts, and source packages.
8. Rebuild repo-shaped source zips when the incoming zip is not already the canonical taxonomy package.
9. Update all relevant `INDEX.md` files and playbook/doc surfaces.
10. Commit and push to `main`.
11. Verify remote `origin/main` contains the expected paths.
12. Delete the ingress zip and any scratch extraction folders only after the landed repo files are committed, pushed, and remote-verified.
13. Return using `Patch/CONTRACTS/WORKER_RETURN_CONTRACT.md`.

## Stop conditions

Stop if approval is unclear, contents cannot be inspected, taxonomy is ambiguous, target paths conflict unexpectedly, package contents disagree with index claims, multiple unscoped zips are present, publication fails, cleanup would remove a zip before publication proof exists, or an index would point at files that were not actually landed.

## Required return fields

- `ingress_zip_path`
- `cleanup_status`
- `retained_inputs`
- `deleted_inputs`

## Return contract

Use `../../../Patch/CONTRACTS/WORKER_RETURN_CONTRACT.md` for the final worker return shape and publication evidence.
