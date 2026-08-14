# Completing plans and specs

Use this runbook when a plan and its associated spec(s) are delivered in the
same PR as the implementation. Close out the artifacts in the completing PR so
that when it merges the plan, spec, and related files move to the generated,
indexed archive and `.agents/plans/` / `.agents/specs/` stay focused on in-flight
work.

## When to archive

Archive a plan and its related artifacts as part of the same PR that completes
the work, so that when the PR merges the artifacts it completes are closed out.

Archive once:

- the implementation is complete and the PR is ready for final review;
- the spec is fully realized in the implementation;
- the plan is marked completed: every top-level checkbox (`- [ ]`) is checked
  (`- [x]`), or the plan records the implementation PR.

Do not archive a plan before its implementation is ready for final review or
while it has unresolved review findings.

## What to archive

Move the complete work slice together:

1. **The plan file** — `plan-name.md` from `.agents/plans/` to
   `.agents/plans/completed/`.
2. **The spec file** — if the plan lists a spec, move that file from
   `.agents/specs/` to `.agents/specs/completed/`.
3. **Any explicitly referenced `.agents/` artifact** the plan names (roadmaps,
   research, design files, or other plans/specs).

If a referenced file does not exist, note the missing file in the PR body rather
than leaving it in the active tree.

## How to archive

```bash
# 1. Move the plan and spec together
git mv .agents/plans/<plan-name>.md .agents/plans/completed/
git mv .agents/specs/<spec-name>.md .agents/specs/completed/    # if there is one

# 2. Move any related .agents/ artifacts the plan references

# 3. Regenerate the index mesh
py -3 .agents/skills/generating-agent-mesh/scripts/generate_index_mesh.py --apply

# 4. Verify the tree passes CI before committing
py -3 tools/run.py ci --check

# 5. Commit the archive and publish
git add -A
git commit -m "archive: complete <plan-name>"
git push origin <pr-branch>
```

## Mesh behavior

The `generating-agent-mesh` skill discovers `.agents/plans/completed/` and
`.agents/specs/completed/` automatically and writes `INDEX.md` files for both.
The parent `.agents/plans/INDEX.md` and `.agents/specs/INDEX.md` list only
in-flight files and a single `completed/` directory link, so agents reviewing
current plans/specs no longer load the full historical index.
