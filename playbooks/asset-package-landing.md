# Asset package landing playbook

Use this project playbook when approved visual assets, markdown sidecars, receipt packages, or source zips need to be landed in `HarleyBartles/adventures-of-patch`.

Patch may execute this workflow through `Patch / execution`, but the project workflow belongs in root `/playbooks/`. Patch-specific executable helpers belong under `Patch/SKILLS/`.

## Preflight

1. Read root `INDEX.md`, `AGENTS.md`, and `playbooks/INDEX.md`.
2. If Patch executes the work, read `Patch/README.md`, `Patch/GOVERNANCE.md`, `Patch/ROUTING.md`, and `Patch/CONTRACTS/WORKER_RETURN_CONTRACT.md`.
3. Read the relevant issue and comments.
4. Read the relevant asset directory `INDEX.md` files.
5. Read `assets/source-zips/INDEX.md` when a zip package is involved.
6. When an asset sheet package is involved, read `playbooks/asset-sheet-production-contract.md`.
7. Confirm target paths do not collide with existing files unless replacement is explicitly intended.

## Landing workflow

1. Classify each input file by repo taxonomy.
2. Copy accepted individual assets into the target `assets/**` directory.
3. Copy rendered asset-sheet PNGs into the target `assets/**` directory.
4. Copy approved source images used by the rendered sheet beside the sheet or into the appropriate assembly/source folder according to the asset directory convention.
5. Copy markdown or JSON sidecars/specs beside the relevant image sheets or documentation.
6. Copy repo-tracked source packages into `assets/source-zips/` when appropriate.
7. Update the target asset directory `INDEX.md`.
8. Update `assets/INDEX.md` if a new asset directory is introduced.
9. Update `assets/source-zips/INDEX.md` for committed source packages.
10. Update issue or receipt surfaces required by the task.
11. Commit and push to `main`.
12. Verify remote `origin/main` contains the expected paths.
13. Return with publication evidence.

## Asset sheet package rule

A final asset sheet package must contain:

- the rendered asset-sheet PNG compiled into the approved blank template;
- every QA-accepted source image used in that sheet;
- a sidecar/spec recording title, type, status, version/source/QA text, guidance bullets, source-image filenames, QA decisions, and omissions or skipped candidates when relevant.

Do not land generated one-shot sheet images as canonical asset sheets unless Harley explicitly scoped an omnibus experiment. The canonical final sheet layout is deterministic-template compile under `playbooks/asset-sheet-production-contract.md`.

For character asset sheets, verify that the package includes a full-body main/hero source image on a plain white background. Alternate views may include close-ups, in-world shots, prop/detail shots, pose variants, or other lane-appropriate support images.

Compile intermediates such as HTML files, scratch manifests, and helper scripts are not landed by default. Land them only if Harley explicitly promotes them as durable source.

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

Stop and return blocked or amber if source files are missing, approval is unclear, target paths are ambiguous, the package contents disagree with the intended index entry, required asset sheet package contents are missing, publication fails, or an index would point at files that were not actually landed.
