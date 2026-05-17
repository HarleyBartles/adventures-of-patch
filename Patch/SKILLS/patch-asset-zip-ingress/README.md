# Patch asset zip ingress

Planned Patch execution capability for ingesting asset zips into `HarleyBartles/adventures-of-patch`.

## Purpose

Given an incoming zip of accepted or candidate assets, Patch should inspect the package, classify contents against the repo taxonomy, route files to the correct repo locations, rebuild canonical source packages where appropriate, update index mesh files, publish changes, and return evidence.

This skill is for package handling and import/rebuild work, not the default GPT visual-inspection route for repo-canonical images.

## Current status

Planned capability surface. This folder defines the intended on-disk skill tree shape before implementation.

## Required behaviour

- Do not treat an uploaded zip as canon merely because it exists.
- Identify source decision, issue, receipt, or user approval before promoting assets.
- Classify contents before writing them into `assets/**`.
- Rebuild repo-shaped source packages to match the on-disk taxonomy when needed.
- Update `assets/INDEX.md`, target asset directory indexes, and `assets/source-zips/INDEX.md`.
- Commit, push, and verify before returning green.

## Related project playbook

See root `playbooks/asset-package-landing.md` for the project/domain workflow.
