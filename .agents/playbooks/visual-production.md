# Visual production playbook

## When

Use when an Adventures idea must become a coherent, inspectable visual adventure ready for reuse in the requested downstream artifact.

## Required capabilities

- project identity, canon, and source truth.
- readiness classification.
- authored visual composition and story-preserving translation.
- raster generation, editing, inspection, and truthful handoff.
- authority and canon protection.

## Optional capabilities

- None.

## Required repository-owned skills

- `adventures-project-doctrine` supplies project identity and source truth.

## Optional repository-owned skills

- None.

## Composition

Orient on live briefs, issues, and direct canonical sources. Classify readiness, resolve human-owned framing decisions, establish visual direction and the smallest useful bible, produce and inspect governed candidates, preserve provenance and rejected/omitted reasoning, obtain approvals, and land only requested accepted surfaces. Begin repo asset discovery in ``build/TAXONOMY.md`, relevant package `manifests/manifest.json` files, package guides, sidecars, and canonical directories under `build/`, `style/`, `published/`, or `workbench/`; Patch references are under `build/canon/patch/`. Repo-owned outputs land in the relevant governed asset family. Apply/check mechanical surfaces through `py -3 tools/run.py ci`. Evidence includes source/readiness, references used and skipped, bible/preflight, candidate inspection, package/sidecar provenance, approvals, landing, downstream readiness, and blockers. Generation is not acceptance; selection is not canonisation. Do not let the requested delivery format retroactively dictate the frame or visual system.

## Doctrine and contracts

- `.agents/doctrine/adventures-project-doctrine.md`
- `.agents/contracts/adventure-readiness.md`
- `.agents/contracts/visual-preproduction.md`
- `.agents/contracts/visual-bible.md`
- `.agents/contracts/asset-sheet-production.md`
- `.agents/contracts/adventures.visual_sidecar.adjacent.v1.schema.json`
- `.agents/contracts/image-sidecar-provenance.schema.json`

## Local commands and paths

See the composition and paths above.

## Evidence contract

Evidence is specific to the touched concern and names the source, decision, validation, and remaining uncertainty.

## Prohibited combinations

- Do not claim a capability ran when its output was not inspected.

## Runbook routing

- `.agents/runbooks/design.md` routes here when this concern applies.
- `.agents/runbooks/planning.md` routes here when this concern applies.
- `.agents/runbooks/implementing.md` routes here when this concern applies.
- `.agents/runbooks/code-review.md` routes here when this concern applies.
