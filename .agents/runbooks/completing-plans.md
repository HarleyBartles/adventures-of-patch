# Completing plans and specs

## When

Use when implementation has completed an active plan, spec, roadmap,
checkpoint, or related planning artifact.

## Required skills

- `cleanup-custody` owns classification and promotion-before-removal.
- `verification-before-completion` proves the implementation and durable
  replacements before removal.
- `generating-agent-mesh` owns navigation repair after tracked removals.

## Composition

Verify completion, classify each artifact with `cleanup-custody`, promote
enduring decisions into current doctrine/runbooks or the repo's ADR home,
remove completed artifacts from Git, regenerate the mesh, and validate the
resulting tree.

## Doctrine and contracts

- `.agents/doctrine/completed-artifacts.md`
- `.agents/doctrine/mesh-policy.md`

## Local commands and paths

- Active plans/specs: `.agents/plans/`, `.agents/specs/`.
- Remove completed tracked artifacts with Git-aware edits.
- Regenerate/validate with `py -3 tools/run.py ci --apply`; normal commits use
  the staged apply/check hook.

## Evidence contract

Evidence includes the completed implementation/PR, removed artifact paths,
promoted durable destinations, optional scratch-copy disclosure, regenerated
mesh result, and current validation proof.

## Prohibited combinations

- Do not move completed artifacts into a tracked `completed/` archive.
- Do not remove an artifact before promoting enduring decisions or proving the
  implementation complete.
- Do not describe an optional scratch copy as durable or evidentiary.
