# `.agents/runbooks` Guidance

This directory holds the repo's stage-based and project runbooks. Use them as
the entry point for each kind of work.

## Read when

- Use `design.md` for design and shaping work.
- Use `planning.md` for multi-step planning work.
- Use `implementing.md` for implementation work.
- Use `code-style.md` for conventions and style.
- Use `code-review.md` for review work.
- Use `pr.md` for pull-request workflow and publication proof.
- Use `testing.md` for test commands and TDD workflow.
- Use `security.md` for security posture and review.
- Use `skill-authoring.md` for creating or editing skills.
- Use `marketplace-generation.md` for marketplace refresh and plugin work.
- Use `completing-plans.md` for plan closeout and archive.
- Use the additional project runbooks for Adventures-specific workflows:
  - `pre-runbook-adventure-readiness.md`
  - `visual-preproduction.md`
  - `end-to-end-pptx-production.md`
  - `image-qa-contract.md`
  - `image-inspection-source-contract.md`
  - `asset-sheet-production-contract.md`
  - `visual-bible-creation.md`
  - `visual-bible-interpretation.md`
  - `bound-connector-action-gate.md`

## Working rules

- Keep each runbook focused on a single stage or concern.
- Do not repeat doctrine; point to `.agents/doctrine/*.md`.
- If a runbook moves or a new one is added, update this router and the mesh in
the same change.
