# Third-party and upstream licensing notices

This file is the repository-level audit surface for material that is not cleanly covered by the project-authored MIT or CC BY-ND defaults described in `LICENSING.md`.

The rule is simple: third-party, vendored, adapted, or upstream-derived material keeps the licence and attribution obligations that actually apply to it. The repository does not relicense material merely because it is checked in here.

## Known repository boundary

- `.agents/plugins/marketplace-source` is a git submodule pointing to `HarleyBartles/agent-asset-marketplace`. Treat that repository boundary and the material exposed through it according to its own licensing and notices rather than the defaults in this repository.

## Audit required before public release

An on-disk licensing pass should inventory the tracked tree and record, at minimum:

- vendored software or source copied from elsewhere;
- upstream-derived or adapted source files;
- fonts, templates, icons, images, audio, media, or other assets not wholly authored for this repository;
- examples or snippets carrying upstream copyright/licence requirements;
- submodules and generated projections that preserve upstream licensing;
- any file or subtree whose existing licence is more specific than the repository defaults.

For each discovered item, preserve the applicable upstream licence text, copyright notice, attribution, source/provenance, and any required NOTICE material. Prefer SPDX/REUSE-compatible file or subtree metadata where practical.

Do not classify uncertain provenance as project-authored merely to make the audit pass. Record uncertainty explicitly and resolve it before treating the repository as publication-ready.

## Current status

This file is a scaffold, not a completed provenance audit. The full-tree audit and machine-readable classification remain an on-disk task before the repository is made public.
