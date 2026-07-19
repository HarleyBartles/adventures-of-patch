# Mesh Policy

Status: active policy
Owner: Adventures of Patch repository tooling
Scope: authored routing, generated navigation, documentation custody, and
agent-surface discoverability
Nearest router: `.agents/AGENTS.md`

This is the binding contract for the repository's agent and documentation
surfaces. It follows the shared repo pattern while preserving this repo's
local custody rules.

## Surface roles

### `AGENTS.md`

`AGENTS.md` files are thin scoped routers. They tell agents what to read and
when, point to canonical doctrine, and state only the local delta needed for
the governed subtree.

- Root `AGENTS.md` supplies repository identity and the main route.
- Scoped `AGENTS.md` files inherit root law and point outward to doctrine,
  guides, playbooks, scripts, and human context.
- Doctrine must not be duplicated in routers.
- A router carrying substantial doctrine must be split: move the rule to a
  canonical policy and leave a read-when pointer.

### `INDEX.md`

`INDEX.md` files are generated navigation and coverage surfaces. They answer
what exists, where it lives, and how to return to the parent scope.

- They must not contain operative law.
- They must be produced by the repository mesh generator, never hand-edited.
- Stale indexes are repaired by whole-mesh regeneration.
- Skill roots and generated plugin roots are leaves unless the generator's
  policy explicitly says otherwise.
- The pinned marketplace submodule is a gitlink boundary; the parent mesh may
  link to it but must not descend into it.

### `README.md`

README files are human-facing orientation and usage surfaces. They may explain
where agent law lives, but they are not agent routers or the sole home of
operative rules.

## `.agents` custody

`.agents/` is the tracked home for agent-facing infrastructure.

- `.agents/doctrine/` contains binding policies, contracts, and invariants.
- `.agents/docs/` contains non-binding agent reference material when needed.
- `.agents/guides/` contains the four stage overlays: design, planning,
  implementation, and code review.
- `.agents/plugins/` contains plugin posture and the pinned marketplace
  source boundary.
- `.agents/skills/` contains marketplace-derived skills plus protected local
  `adventures-*` skills.
- `.agents/superpowers/plans/` is the only tracked Superpowers artifact home;
  other execution material must remain ignored or external.

Ordinary project work belongs in the repository's project, asset, docs, and
playbook homes rather than being hidden under `.agents/`.

## Link and discovery direction

- Routers point outward to doctrine, guides, scripts, playbooks, and READMEs.
- Doctrine and guidance must not link back to `AGENTS.md` as their authority.
- Generated indexes may list any surface for navigation.
- Every active doctrine, guide, runbook, and skill lane must be reachable from
  an applicable router.
- Adding, moving, or retiring a policy requires repairing the nearest router
  and regenerating affected indexes in the same change.

## Generator and validation contract

The repository-owned mesh generator is the only writer for generated indexes.
It must:

- derive the repository root through Git;
- discover current in-scope files rather than maintain a hard-coded inventory;
- respect tracked and ignored boundaries;
- reject or skip links and reparse points safely;
- treat gitlinks and vendored/generated skill roots as explicit boundaries;
- produce stable ordering, links, and LF-normalized text;
- support write and `--check` modes with identical expected output;
- validate local links and remove stale generated indexes during full
  regeneration.

The generator must refuse shared-checkout writes by default and require an
explicit `--allow-shared-checkout` override, while always rejecting submodule
mutation. Check mode remains read-only.

## Self-healing and completion

When a worker finds stale authored routing, repair the canonical router and
target policy together. When it finds stale generated navigation, repair the
generator or source boundary and regenerate the whole mesh.

A mesh-affecting change is complete only when:

- policy and guidance are reachable from routers;
- generated indexes are current and link-valid;
- the generator's check mode passes;
- marketplace gitlinks remain leaves;
- local skill custody and marketplace provenance remain distinct;
- `git diff --check` passes for the touched content;
- final branch and remote proof are reported accurately.
