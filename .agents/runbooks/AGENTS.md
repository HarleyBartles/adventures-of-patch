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
- Use `testing.md` for the local validation command map.
- Use `security.md` for security posture and review.
- Use `skill-authoring.md` for creating or editing skills.
- Use `marketplace-generation.md` for marketplace refresh and plugin work.
- Use `completing-plans.md` to compose completion custody, durable promotion,
  removal, mesh regeneration, and validation.
- Use the additional project runbooks for Adventures-specific workflows:
  - `visual-production.md`

## Working rules

- Keep each runbook focused on a single stage or concern.
- Do not repeat doctrine; point to `.agents/doctrine/*.md`.
- If a runbook moves or a new one is added, update this router and the mesh in
the same change.
