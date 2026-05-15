# Asset Package Landing Playbook

Use this playbook when Patch is explicitly bound to `Patch / execution` to land approved visual assets, markdown sidecars, receipt packages, or source zips in `HarleyBartles/adventures-of-patch`.

## Purpose

Close the binary asset landing gap: ChatGPT sessions can generate or assemble PNGs, sidecars, and zips, but Patch's on-disk execution lane must perform governed repo-local landing, index updates, commit, push, and verification.

## Inputs

A valid landing packet should include:

- issue number or source decision;
- approved asset files or package paths;
- target asset family and target repo directory;
- intended source zip filename when a package is being committed;
- sidecar markdown when text doctrine accompanies generated sheets;
- acceptance status: accepted, provisional, import evidence, or rejected.

Do not treat an uploaded package as canon merely because it exists. The user decision, repo issue, receipt, or index must explain why it is being landed.

## Preflight

1. Read `../README.md`, `../GOVERNANCE.md`, `../ROUTING.md`, and `../CONTRACTS/WORKER_RETURN_CONTRACT.md`.
2. Read repo root `INDEX.md`, `AGENTS.md`, and the relevant issue.
3. Read the relevant asset directory `INDEX.md` files.
4. Read `assets/source-zips/INDEX.md` when a zip package is involved.
5. Confirm the target paths do not collide with existing files unless replacement is explicitly intended.
6. Check large-file and binary handling before writing unusually large files.

## Landing steps

1. Copy approved individual assets into the target `assets/**` directory.
2. Copy markdown sidecars beside the corresponding image sheets or into the target documentation location.
3. Copy bundled source zips into `assets/source-zips/` when the zip is meant to be a repo-tracked source/import package.
4. Update the target asset directory `INDEX.md`.
5. Update `assets/INDEX.md` if a new asset directory is introduced.
6. Update `assets/source-zips/INDEX.md` for any committed source zip.
7. Update any issue comment or receipt surface required by the task.
8. Commit and push to `main`.
9. Verify remote `origin/main` contains the expected commit and paths.
10. Return using `Patch/CONTRACTS/WORKER_RETURN_CONTRACT.md`.

## First test case

Issue #20 identifies the first intended test case: the approved Adventures of Patch style-system package from the ChatGPT session that created:

- approved style patterns sheet;
- style anti-patterns sheet;
- general style guide markdown sidecar;
- bundled source zip.

The package should be landed only once the execution environment has the actual PNG/markdown/zip payloads available on disk.

## Canon and source discipline

- Accepted assets become repo-tracked project state only after landing, index update, commit, push, and verification.
- Source zips are package evidence, not automatically active canon.
- Generated image text is not authoritative doctrine; markdown sidecars and repo text should carry exact rules.
- Patch visual canon remains under `assets/patch/`.
- General style-system sheets should not overwrite canonical Patch identity rules.

## Stop conditions

Stop and return `BLOCKED` or `AMBER` if:

- required source files are missing from disk;
- user approval is unclear;
- target paths are ambiguous;
- files exceed safe repo storage expectations;
- the zip contents disagree with the intended index entry;
- commit, push, or remote verification fails;
- index entries would point to files that were not actually landed.
