# Adventures planning guide

This is the repository-specific overlay for planning work. It does not replace
`repo-worker-base`, `writing-plans`, or `risk-gates`.

## Route

1. Start from the live repository mesh and, when named, the live GitHub issue.
2. Keep implementation plans under `.agents/superpowers/plans/`; do not add
   new plans under `docs/superpowers/plans/`.
3. For issue-to-PPTX work, classify the issue as seed-ready, frame-ready,
   asset-ready, or runbook-ready using
   `.agents/runbooks/pre-runbook-adventure-readiness.md`.
4. Use the frame gate in `adventures-project-readiness`, route visual
   preparation to `adventures-visual-preproduction`, and acceptance to
   `adventures-image-qa`.

## Plan contents

Plans must state the source of truth, target worktree and branch, scope,
non-goals, custody boundaries, readiness gates, validation commands, and
publication evidence.

## Stop conditions

Stop before production if the frame is weak, Patch references cannot be
inspected, asset readiness is unproven, the issue source is unavailable, or a
required decision belongs to Harley. Do not invent a frame, asset canon, actor
identity, or acceptance result to make a plan appear green.
