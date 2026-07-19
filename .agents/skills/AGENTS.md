# Derived and local skills routing

Use this routing file before inspecting or refreshing `.agents/skills/`.

- Marketplace-derived skills are copied from the pinned source recorded in
  `.provenance.json`.
- Repository-owned skills use the reserved `adventures-*` prefix and must
  survive marketplace refreshes.
- Do not hand-edit marketplace-derived skill content; change source custody and
  refresh it deterministically.
- `INDEX.md` is generated navigation, not an inventory to maintain by hand.

Use `scripts/refresh_agent_surfaces.*` for the combined refresh and
`scripts/validate_agent_mesh.*` for custody, route, and doctrine checks.
