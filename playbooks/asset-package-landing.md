# Asset package landing playbook

Use this project playbook when approved visual assets, markdown sidecars, receipt packages, or source zips need to be landed in `HarleyBartles/adventures-of-patch`.

Patch may execute this workflow through `Patch / execution`, but the project workflow belongs in root `/playbooks/`. Patch-specific executable helpers belong under `Patch/SKILLS/`.

## Preflight

1. Read root `INDEX.md`, `AGENTS.md`, and `playbooks/INDEX.md`.
2. If Patch executes the work, read `Patch/README.md`, `Patch/GOVERNANCE.md`, `Patch/ROUTING.md`, and `Patch/CONTRACTS/WORKER_RETURN_CONTRACT.md`.
3. Read the relevant issue and comments.
4. Read the relevant asset directory `INDEX.md` files.
5. Read `assets/source-zips/INDEX.md` when a zip package is involved.
6. Confirm target paths do not collide with existing files unless replacement is explicitly intended.

## Landing workflow

1. Classify each input file by repo taxonomy.
2. Copy accepted individual assets into the target `assets/**` directory.
3. Copy markdown sidecars beside the relevant image sheets or documentation.
4. Copy repo-tracked source packages into `assets/source-zips/` when appropriate.
5. Update the target asset directory `INDEX.md`.
6. Update `assets/INDEX.md` if a new asset directory is introduced.
7. Update `assets/source-zips/INDEX.md` for committed source packages.
8. Update issue or receipt surfaces required by the task.
9. Commit and push to `main`.
10. Verify remote `origin/main` contains the expected paths.
11. Return with publication evidence.

## Taxonomy hints

Useful categories include:

- Patch visual canon;
- style-system sheet;
- character class sheet;
- individual character sheet;
- environment class sheet;
- location sheet;
- prop sheet;
- interaction guide;
- anti-pattern sheet;
- receipt or evidence package;
- deck-specific provisional asset.

## First smoke case

Issue #20 identifies the first smoke case: inspect the approved style-system assets already added to the repo, classify them, repair the index mesh, and publish a verified return.

## Stop conditions

Stop and return blocked or amber if source files are missing, approval is unclear, target paths are ambiguous, the package contents disagree with the intended index entry, publication fails, or an index would point at files that were not actually landed.
