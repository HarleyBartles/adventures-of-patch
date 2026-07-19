# Adventures of Patch

Canonical repository for the Presentation Planner / Adventures of Patch project.

This project develops presentation narratives through Patch's adventures as a
character and visual through-line. Patch is the constant protagonist unless
explicitly excluded. Supporting characters, environments, props, and visual
systems may be reused, ignored, extended, or newly created for each
presentation.

## Source discipline

The repository is canonical project truth. Do not rely on memory when asset availability, Patch continuity, visual planning, actor routing, or playbook status matters. Inspect the current repo files first.

## Visual resource discipline

Before any visual-production decision that could touch image credits, read `playbooks/image-generation-resource-discipline.md`. Deterministic workflows such as QA, prompt boards, contact sheets, asset-sheet compilation, receipts, repo work, and policy discussion are credit-conservation work, not image-generation authorization.

## Connector action gate

When work reaches an external connector action, refresh the named connector at that boundary before choosing actions or reporting action availability. See `docs/project/connector-action-gate-note.md` and `playbooks/bound-connector-action-gate.md`.

## Agent workspace

Agent-facing infrastructure lives under `.agents/`. Local Adventures skills
live under `.agents/skills/adventures-*/`; repository contracts live under
`.agents/contracts/`; stage overlays live under `.agents/guides/`.

## Repository layout

- `.agents/` - agent workspace infrastructure, doctrine, guides, contracts, and local skills.
- `playbooks/` - first-class project/domain playbooks for Adventures workflows.
- `assets/source-zips/` - canonical uploaded asset packages and reusable source/import bundles; not the default visual-inspection route.
- `assets/canon/patch/` - reusable visual assets, source packages, receipts, and Patch canon. See `assets/INDEX.md`.
- `assets/evidence/receipts/` - receipt packages and evidence bundles derived from decks or asset work.
- `docs/adventures/` - Patch adventure concepts and deck narrative frames.
- `docs/principles/` - software-agent working principles expressed through Patch stories.
- `docs/project/` - project indexes, bootstrap notes, and workflow guidance.
- `decks/` - presentation artifacts or deck working folders when committed.
- `.agents/skills/` - packaged marketplace projections and repository-local skills.
- `scratch/` - local working area, ignored by git except for `.gitkeep`.

## Core rule

Repo-canonical image inspection should default to repo-indexed visual
inspection packages. Source zips remain useful for package/import/receipt/
integrity work, not as the ordinary source of visual truth. For template work,
the repo template PNG+JSON sidecar and matching project-source PNG/spec are
both required and must be discoverable through the index mesh.

Patch is the through-line. Existing non-Patch assets are optional. New presentation-specific asset generation is expected and first-class. Reusable results should later be canonicalised into asset sheets, style guides, contact sheets, anti-pattern sheets, interaction guides, environment sheets, or receipt packages.
