---
name: patch-asset-zip-ingress
description: repo-resident Patch execution capability for ingesting asset zips into HarleyBartles/adventures-of-patch. use when Patch is bound to execution and must inspect a zip of accepted or candidate assets, classify contents, route files to the repo asset taxonomy, rebuild source packages where appropriate, update indexes, publish changes, and return evidence.
---

# Patch asset zip ingress

This is a repo-resident Patch skill surface, not a ChatGPT-native installed skill unless explicitly packaged for installation later.

## Trigger

Use when Patch is bound to `Patch / execution` and receives a zip or package of visual assets, markdown sidecars, receipt evidence, or source files that may need to be landed into `HarleyBartles/adventures-of-patch`.

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
10. Target asset directory indexes.

## Workflow

1. Confirm source authority: issue, receipt, user approval, or explicit bounded intake scope.
2. Inspect the zip contents without promoting them to canon.
3. Classify each file by repo taxonomy.
4. Decide target paths for individual assets, sidecars, receipts, and source packages.
5. Rebuild repo-shaped source zips when the incoming zip is not already the canonical taxonomy package.
6. Update all relevant `INDEX.md` files.
7. Commit and push to `main`.
8. Verify remote `origin/main` contains the expected paths.
9. Return using `Patch/CONTRACTS/WORKER_RETURN_CONTRACT.md`.

## Stop conditions

Stop if approval is unclear, contents cannot be inspected, taxonomy is ambiguous, target paths conflict unexpectedly, package contents disagree with index claims, publication fails, or an index would point at files that were not actually landed.
