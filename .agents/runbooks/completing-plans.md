# Completing plans and specs

Use this runbook when a plan and its associated spec(s) are delivered in the
same PR as the implementation. Close out the artifacts in the completing PR so
that `.agents/plans/` and `.agents/specs/` stay focused on in-flight work while
Git history preserves the completed state.

## When to remove

Remove a plan and its related artifacts as part of the same PR that completes
the work, so that when the PR merges the artifacts it completes are closed out.

Remove them once:

- the implementation is complete and the PR is ready for final review;
- the spec is fully realized in the implementation;
- the plan is marked completed: every top-level checkbox (`- [ ]`) is checked
  (`- [x]`), or the plan records the implementation PR.

Do not remove a plan before its implementation is ready for final review or
while it has unresolved review findings.

## What to remove

Remove the complete work slice together:

1. **The plan file** from `.agents/plans/`.
2. **The spec file** from `.agents/specs/`, if the plan lists one.
3. **Any explicitly referenced `.agents/` artifact** the plan names (roadmaps,
   research, design files, or other plans/specs).

If a referenced file does not exist, note the missing file in the PR body.

Before removal, promote enduring architecture decisions to ADRs and operating
rules to current doctrine or runbooks. A convenience copy may be placed in the
central disposable `_agent-scratch/<repo-name>/completed/` store, but it is not
evidence and has no retention promise.

## How to remove

```bash
# 1. Remove the completed plan and spec together
git rm .agents/plans/<plan-name>.md
git rm .agents/specs/<spec-name>.md    # if there is one

# 2. Remove any related completed .agents/ artifacts the plan references

# 3. Regenerate the index mesh
py -3 .agents/skills/generating-agent-mesh/scripts/generate_index_mesh.py --apply

# 4. Verify the tree passes CI before committing
py -3 tools/run.py ci --check

# 5. Commit the closeout and publish
git add -A
git commit -m "docs: close out <plan-name>"
git push origin <pr-branch>
```

## Evidence behavior

The completing commit and Git history preserve the final artifact state. Do not
recreate tracked `completed/` folders or indexes as a compatibility archive.
