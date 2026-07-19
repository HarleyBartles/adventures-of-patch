# Agent Workspace Policy Design for Adventures of Patch

Status: design approved; implementation plan handoff pending.

## Goal

Bring `Z:\adventures-of-patch` into the same agent-workspace shape used by
`Z:\portfolio`, while preserving the repository's project content and Patch's
role as the character and visual canon rather than an agent identity.

The result must provide a deterministic marketplace refresh, explicit custody
for repository-local skills, a tracked agent mesh, a single home for agent
operational material, and a line-ending policy that does not create recurring
checkout churn.

## Non-goals

- Do not redesign the Adventures project, its presentation pipeline, or Patch's
  character canon.
- Do not import `adventures-*` skills as marketplace-derived output.
- Do not hard-code `adventures-pack` as a special case in the refresh tool.
- Do not preserve Patch as a project-local agent, actor lane, or governance
  identity.
- Do not treat the marketplace source checkout as repository-authored skill
  custody.
- Do not erase unrelated repository content while repairing the agent surface.

## Governing layout

The portfolio policy is the structural reference:

- `AGENTS.md` files are thin routing surfaces.
- `INDEX.md` files are generated navigation and coverage surfaces.
- `.agents/doctrine/` contains durable agent-facing policy and contracts.
- `.agents/docs/` contains agent-facing guidance that is not doctrine.
- `.agents/guides/` contains workflow entrypoints where needed.
- `.agents/plugins/` contains the plugin manifest, lock/provenance metadata,
  and the initialized marketplace source submodule.
- `.agents/skills/` contains repository-local skills and marketplace-derived
  skills, with generated provenance identifying the latter.
- `.agents/guides/` is a required workflow surface containing the portfolio
  pattern's `AGENTS.md`, `INDEX.md`, `design-guide.md`, `planning-guide.md`,
  `implementing-guide.md`, and `code-review-guide.md`. The four stage guides
  must be adapted to Adventures-specific paths, policies, and validation while
  preserving their design, planning, implementation, and review handoffs.
- `.agents/superpowers/plans/` is the only tracked superpowers content.
- `README.md` files remain human-facing.
- Project documentation, runbooks, source assets, and Patch character canon
  remain repository work outside `.agents/`.

Any existing Patch actor-governance, actor-routing, or worker-identity material
must be classified and moved into the appropriate `.agents/` doctrine/guidance
home or removed when it has no continuing purpose. Character, visual, and
story material about Patch remains in project-owned locations such as
`assets/canon/patch/` and the Adventures project documentation.

## Marketplace source and refresh contract

Add the marketplace repository as the nested Git submodule
`.agents/plugins/marketplace-source`, following the portfolio submodule
configuration and tracking the latest validated `main` commit. The local
manifest records the source coordinates and the default plugin set; the
submodule gitlink records the exact source revision used for a refresh.

Add a deterministic `scripts/install_agent_skills.py` entrypoint, with the
PowerShell and shell wrappers used by the sister repositories where practical.
The installer must support a write mode and `--check` mode, derive paths from
the repository root, validate that the submodule is initialized and pinned, and
write stable UTF-8/LF output.

The refresh algorithm is provider-agnostic:

1. Read the local marketplace manifest and resolve its configured default
   plugins from the initialized marketplace source.
2. Enumerate each configured plugin's declared skill directories.
3. Exclude any skill whose name matches the configured local prefix
   `adventures-` from marketplace-derived output.
4. Import every remaining eligible skill, including non-Adventures dependency
   skills exposed by an otherwise Adventures-related plugin.
5. Preserve repository-local skills and never overwrite them from the
   marketplace source.
6. Detect and fail on conflicting marketplace skill names, reserved output
   names, missing providers, or invalid source coordinates.
7. Prune only stale marketplace-derived output; never prune local
   `adventures-*` skills or hand-authored navigation files.
8. Write deterministic `.provenance.json` describing the source revision,
   configured providers, and each derived skill.

The algorithm must not contain an `adventures-pack` branch. Its behavior for
that provider follows the general rule:

- if the provider still contains non-`adventures-*` skills, those skills are
  imported;
- if it contains no eligible skills, it produces no vendored output and
  `--check` reports the provider as empty/stale so the local manifest can be
  repaired when the marketplace worker removes the plugin;
- if the provider is removed upstream, the local manifest must remove it and
  the next refresh must converge cleanly.

The local manifest must make the reserved prefix explicit, while retaining the
portfolio-style default plugin and per-plugin source metadata. A duplicate
skill supplied by multiple providers is acceptable only when the content and
source contract are equivalent; otherwise refresh fails rather than selecting
an implicit winner.

## Local skill assessment and custody

Assess every `adventures-*` skill currently supplied by the Adventures project
pack against this repository's live project docs, runbooks, asset paths, and
workflow boundaries. The assessment must record one of:

- retain and adapt as a repository-local skill;
- retain with a narrowly documented scope change; or
- reject as obsolete, duplicated, or not valid for this repository.

Retained skills become authored sources under
`Z:\adventures-of-patch\.agents\skills\adventures-*`. They must be adapted
to the new agent-workspace layout, current canonical asset paths, and the
removal of Patch as an agent identity. They may still describe Patch as the
project character when that is relevant to visual or presentation work.

Existing repo-local Patch capability skills must be classified in the same
pass. Relevant executable guidance moves into `.agents\skills\` with stable
`adventures-*` local names where appropriate; project-specific production
contracts remain in project runbooks or asset documentation. No local skill
may rely on a vanished `Patch/` agent governance surface.

Non-local skills such as `using-linear` or `don-logan-boundary` remain
marketplace-derived when they are present in the configured plugin set. They
are not copied into local Adventures custody merely because the provider once
also contained `adventures-*` skills.

## Mesh and documentation repair

Move the operative agent routing currently carried by the root and Patch
surfaces into a thin root `AGENTS.md` plus scoped `.agents/AGENTS.md` and
`.agents/*/AGENTS.md` routers. Place durable policy in `.agents/doctrine/` and
keep project-specific production law in the existing project documentation
homes.

Add or adapt the portfolio-style index generator so every visible directory
has a generated `INDEX.md`, with the marketplace submodule treated as a
gitlink boundary. Regenerate the complete mesh; do not hand-edit generated
indexes. Update the human-facing root README only for orientation and links,
not as a replacement for agent routing.

The `.agents/guides/` router and index must explicitly expose all four stage
guides. A repository is not considered aligned if the directory exists but
one of the four guides is missing or still points at Portfolio-only paths.

Repair stale paths discovered during the mesh pass, including existing
references to the retired `assets/hero-patch/` layout where the live canonical
path is `assets/canon/patch/`. Update affected workflows and validation docs
only where the live repository proves the old path is invalid.

## Line-ending policy

Add or repair the repository's `.gitattributes` policy so text and generated
agent surfaces are normalized consistently as LF in Git. Ensure the refresh
and mesh tools write LF explicitly. Normalize the currently semantic-empty
CRLF churn as part of the implementation, preserving file content and any
unrelated user changes.

Validation must include `git diff --check`, `git ls-files --eol`, and a
semantic comparison confirming that normalization did not alter project
content.

## Validation and handoff

The implementation is complete only when all of the following are proven:

- the main checkout is fast-forwarded to the requested `origin/main` before
  mutation and the marketplace submodule points at the intended latest main;
- skill refresh write mode is deterministic and a second run is a no-op;
- `--check` passes on the resulting tree;
- local `adventures-*` skills are tracked separately from marketplace-derived
  skills and are never overwritten or pruned;
- non-local skills from a surviving Adventures-related provider are imported;
- an empty or removed provider is diagnosed and converges after manifest repair;
- provenance identifies the exact source revision and derived skill set;
- `.agents/guides/` contains the four required stage guides, its router and
  index are current, and each guide points at live Adventures policy surfaces;
- the full agent/index mesh regenerates cleanly and has no stale retired paths;
- no active agent identity named Patch remains, while Patch character/canon
  remains discoverable;
- line-ending checks are clean; and
- relevant repository validation scripts and workflows pass.

Because this is a shared main checkout and the user has authorized publication
when the changes are correct, the final commit/push may go directly to `main`
only after the exact final tree, validation output, and remote head are
verified.

## Open implementation decisions

These are implementation details, not unresolved product choices:

- whether the PowerShell and shell wrappers delegate to the Python entrypoint
  or contain thin platform-specific launch logic;
- the exact subset of current `adventures-*` skills retained after live
  relevance review;
- the final names and locations of migrated doctrine documents after each
  existing Patch surface is classified; and
- the precise generated-index exclusions required by the initialized
  submodule and other non-project boundaries.

The design deliberately leaves those choices to the implementation plan while
holding the custody, source, and validation contracts fixed.
