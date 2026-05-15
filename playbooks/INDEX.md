# Playbooks index

Root-level playbooks are first-class Adventures of Patch project/domain operating doctrine.

Use this directory for project workflows that coordinate issues, assets, decks, receipts, skills, QA, and publication gates across the repo. Do not bury project/domain playbooks inside `Patch/`; Patch-specific executable capabilities live under `Patch/SKILLS/`.

## Files in this directory

- `pre-playbook-adventure-readiness.md` - required planning-readiness workflow before issue-to-PPTX production; matures seed issues through frame-ready and asset-ready states.
- `image-qa-contract.md` - canonical multi-lane image QA contract; generated images are candidates until accepted by `adventures-image-qa`.
- `end-to-end-pptx-production.md` - canonical orchestration guide for turning a playbook-ready Adventures of Patch issue into a finished presentation package.
- `asset-package-landing.md` - project/domain workflow for landing approved visual assets, markdown sidecars, source zips, and related indexes.

## Subdirectories

None.

## Notes for agents

- Skills own local runtime behaviour.
- Playbooks own project orchestration across skills, production gates, stop conditions, and failure reporting.
- Pre-playbook readiness is separate from PPTX production. Production should stop if frame-ready or asset-ready state is missing.
- `adventures-image-qa` is the canonical image QA authority; generated image candidates must be QA-accepted in the correct lane before they count as preproduction references or scene art.
- Patch actor governance lives under `Patch/`.
- Patch repo-resident executable skills live under `Patch/SKILLS/`.
