# Playbooks index

Root-level playbooks are first-class Adventures of Patch project/domain operating doctrine.

Use this directory for project workflows that coordinate issues, assets, decks, receipts, skills, QA, and publication gates across the repo. Do not bury project/domain playbooks inside Patch; Patch-specific executable capabilities live under Patch/SKILLS.

## Files in this directory

- pre-playbook-adventure-readiness.md - required planning-readiness workflow before issue-to-PPTX production; matures seed issues through frame-ready and asset-ready states.
- visual-preproduction.md - canonical pre-deck visual preproduction workflow for generating, editing, QA-ing, and reporting reusable asset references before PPTX production.
- visual-bible-creation.md - canonical workflow for creating, updating, normalising, and locking standardized visual bibles with composable prompt, QA, repair, and extrapolation blocks.
- visual-bible-interpretation.md - canonical workflow for discovering repo-indexed visual bibles and converting them into prompt, QA, and repair constraints.
- image-inspection-source-contract.md - canonical contract for GPT visual inspection through repo-indexed contact-sheet dispatch/intake packages.
- image-qa-contract.md - canonical multi-lane image QA contract; generated images are candidates until accepted by adventures-image-qa.
- asset-sheet-production-contract.md - canonical final-layout and zip-package contract for source-image-first, template-compiled asset sheets.
- bound-connector-action-gate.md - connector-agnostic gate requiring namespace refresh at the external app action boundary before reporting tool availability.
- end-to-end-pptx-production.md - canonical orchestration guide for turning a playbook-ready Adventures of Patch issue into a finished presentation package.
- asset-package-landing.md - project/domain workflow for landing approved visual assets, markdown sidecars, source zips, and related indexes.

## Subdirectories

None.

## Notes for agents

- Skills own local runtime behaviour.
- Playbooks own project orchestration across skills, production gates, stop conditions, and failure reporting.
- External app connector stages must use bound-connector-action-gate.md before selecting actions or reporting tool absence.
- Pre-playbook readiness is separate from PPTX production. Production should stop if frame-ready or asset-ready state is missing.
- Visual preproduction is separate from PPTX production and must not generate body-slide scene art.
- Visual bible creation authors or updates standardized bibles before generation, after accepted overview references, and when locking accepted asset families.
- Visual bible interpretation converts repo-indexed canon into prompt, QA, and repair constraints without hard-coding brittle paths or source-package visual truth assumptions.
- Image inspection should default to repo-indexed contact-sheet intake documented in `image-inspection-source-contract.md`.
- Asset sheets must follow the source-image-first, deterministic-template compile contract before landing or being counted asset-ready.
- adventures-image-qa is the canonical image QA authority; generated images must be QA-accepted in the correct lane before they count as preproduction references or scene art.
- Patch actor governance lives under Patch.
- Patch repo-resident executable skills live under Patch/SKILLS.
