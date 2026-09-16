# Visual production runbook

## When

Use when an Adventures idea must become a coherent, inspectable visual
adventure: framed, art-directed, evidenced, generated or assembled, inspected,
and ready for reuse in whatever downstream artifact the request names.

## Required skills

- `adventures-project-doctrine` supplies project identity, canon, and source truth.
- `adventures-project-readiness` owns seed/frame/asset readiness decisions.
- `brainstorming` owns unresolved concept and frame shaping.
- `directing-visual-stories` owns authored composition, viewing contract,
  visual rhetoric, and story-preserving translation.
- `generating-images` owns raster generation, editing, inspection, iteration,
  and truthful asset handoff from an authored direction.
- `risk-gates` protects canon, authority, and human-owned creative choices.
- `verification-before-completion` owns final readiness and landing claims.

## Composition

1. **Orient** — bind the live brief/issue to project doctrine and repo truth.
2. **Frame** — classify readiness; use `brainstorming` for unresolved world,
   lesson, story, mapping, or audience decisions; pass the frame contract.
3. **Art direction** — run `directing-visual-stories`; discover current canon
   and references, build a bounded moodboard/reference set, and author the
   audience change, viewing contract, composition, and visual language without
   promoting inspiration into canon.
4. **Visual system** — create or interpret the smallest useful visual bible,
   identify required asset families, and produce lane-specific preflight packets.
5. **Proof** — for a new Patch-bearing world, prove canonical Patch can inhabit
   and interact with it while other roles remain distinct.
6. **Produce and review** — hand the authored image contract to
   `generating-images`; generate or edit one governed candidate at a time,
   inspect the actual image and its hard delivery properties, preserve accepted
   features, and stop at human review points. Repair one material defect at a
   time; start fresh after structural failure.
7. **Build reusable sheets when useful** — generate focused source images,
   review them, then compile the accepted sources deterministically into the
   approved template. Image generation does not create the final sheet layout.
8. **Package and land** — retain
   provenance and rejected/omitted reasoning, obtain required approval, and
   land only the accepted reusable surfaces the request actually needs.
9. **Close** — verify frame/asset state, package/index/sidecar evidence, canon
   posture, downstream readiness, and remaining blockers without assuming a
   particular output format.

## Doctrine and contracts

- `.agents/doctrine/adventures-project-doctrine.md`
- `.agents/contracts/adventure-readiness.md`
- `.agents/contracts/visual-preproduction.md`
- `.agents/contracts/visual-bible.md`
- `.agents/contracts/asset-sheet-production.md`
- `.agents/contracts/adventures.visual_sidecar.adjacent.v1.schema.json`
- `.agents/contracts/image-sidecar-provenance.schema.json`

## Local commands and paths

- Start discovery at `assets/INDEX.md` and follow generated indexes.
- Patch canon starts at `assets/canon/patch/INDEX.md`.
- Repo-owned reusable outputs land in the relevant governed asset family; source
  zips are retained only under their explicit package/receipt role.
- Apply/check repository mechanical surfaces through `py -3 tools/run.py ci`.

## Evidence contract

The visual-production record names:

- live source/brief and readiness history;
- frame basis and unresolved human decisions;
- moodboard/reference inventory with used/skipped rationale;
- bible/preflight versions and uncertainty;
- candidate identifiers, intended use, inspection evidence, human review
  points, and repair decisions;
- accepted reusable assets, deterministic package outputs, sidecars/provenance,
  and omitted/rejected candidates where relevant;
- canon status, landing/index proof, downstream readiness, blockers, and next owner.

## Prohibited combinations

- Do not collapse framing, art direction, generation, inspection, and
  canonisation into one model judgment.
- Do not treat moodboards, uploads, source zips, thumbnails, or generated-only
  candidates as repo canon.
- Do not let a requested delivery format retroactively dictate the frame or
  visual system.
- Do not present a specific downstream format as the default goal
  of Adventures visual production.
