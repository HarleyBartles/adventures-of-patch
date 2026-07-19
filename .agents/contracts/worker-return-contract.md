# Repository worker return contract

Use this contract for tracked repository mutation and asset/source-package
work. It makes execution state, publication proof, and unresolved risk easy to
verify without binding the work to a named agent or actor.

```yaml
status: "GREEN | AMBER | RED | BLOCKED"
status_reason: "<brief reason>"
worker_lane: "planning | execution | review"
repo: "HarleyBartles/adventures-of-patch"
issue_tracking:
  issue_numbers_addressed: ["<issue or not_applicable>"]
  issue_verification_state: "open | verified_pending_closure | blocked | not_applicable"
repo_publication:
  branch: "<branch | not_applicable>"
  tracked_repo_mutation: true
  committed: true
  pushed_branch: true
  branch_head_verified: true
  pr_opened_or_updated: true
  pr_or_merge_verified: true
  working_tree_clean: true
  green_allowed: true
  green_blocker_if_false: "<exact blocker or not_applicable>"
  commits: ["<commit hash or none>"]
changed_surfaces:
  - path: "<repo-relative path>"
    why: "<why it changed>"
source_and_package_basis:
  repo_indexes_read: ["<path>"]
  source_packages_used: ["<package or none>"]
  local_or_uploaded_inputs: ["<input and status or none>"]
  canonisation_state: "canonical | accepted_pending_landing | provisional | import_evidence | not_applicable"
validation:
  checks_run: ["<command>"]
  results: "<brief result>"
  skipped_validations: []
blockers_and_deferred_work:
  blockers: ["<blocker or none>"]
  deferred_work: ["<deferred item or none>"]
false_green_risks_checked: ["<risk checked>"]
```

Use `GREEN` only when the requested work is complete and remote publication
proof exists when mutation occurred. Use `AMBER` for incomplete or review-
pending work, `RED` for an invalid claimed result, and `BLOCKED` for a hard
tool, source, permission, or policy blocker.
