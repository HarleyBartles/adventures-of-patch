# Patch Worker Return Contract

Patch worker returns must make execution state, publication proof, and unresolved risk easy to verify.

This contract applies whenever Patch performs project-local work in `HarleyBartles/adventures-of-patch`.

## Publication gate

For tracked repo mutation, GREEN is blocked until publication proof exists.

If `tracked_repo_mutation` is `true`, then `green_allowed` must be `false` unless the return records:

- local changes complete;
- commit SHA or exact no-op classification;
- push to a worker branch;
- worker branch head verification;
- PR opened into `main`;
- PR or merge verification;
- working tree cleanliness or exact remaining dirty state.

A generated file, local package, report, or ledger is evidence only. It does not certify completion without publication proof.

## Required return shape

```yaml
status: "GREEN | AMBER | RED | BLOCKED"
status_reason: "<brief reason>"
actor_and_lane:
  actor_binding: "Patch / project-director | Patch / execution"
  repo: "HarleyBartles/adventures-of-patch"
  domain_boundaries_honored: true
issue_tracking:
  issue_numbers_addressed:
    - "<issue number or not_applicable>"
  issue_backing_state: "issue-backed | not_applicable"
  issue_verification_state: "open | verified_pending_closure | blocked | follow-up-needed | not_applicable"
repo_publication:
  branch: "<worker branch name | not_applicable>"
  tracked_repo_mutation: true
  local_changes_complete: "true | false | not_applicable"
  committed: "true | false | not_applicable"
  pushed_worker_branch: "true | false | not_applicable"
  worker_branch_head_verified: "true | false | not_applicable"
  pr_opened_into_main: "true | false | not_applicable"
  pr_or_merge_verified: "true | false | not_applicable"
  working_tree_clean: "true | false | not_applicable"
  green_allowed: "true | false"
  green_blocker_if_false: "<exact blocker or not_applicable>"
  commits:
    - "<commit hash or none>"
changed_surfaces:
  - path: "<repo-relative path>"
    why: "<why it changed>"
source_and_package_basis:
  repo_indexes_read:
    - "<path>"
  source_packages_used:
    - "<package filename or none>"
  local_or_uploaded_inputs:
    - "<input and status or none>"
  canonisation_state: "canonical | accepted_pending_landing | provisional | import_evidence | not_applicable"
validation:
  checks_run:
    - "<check or command>"
  results: "<brief result>"
  skipped_validations:
    - check: "<check>"
      reason: "<why skipped>"
blockers_and_deferred_work:
  blockers:
    - "<blocker or none>"
  deferred_work:
    - "<deferred item or none>"
false_green_risks_checked:
  - "<risk checked>"
```

## Required source/package fields

For asset or source-zip work, returns must record:

- whether the asset was user-approved;
- whether the asset was already repo-tracked;
- target asset directory;
- target source zip filename when applicable;
- `assets/source-zips/INDEX.md` update status;
- relevant asset directory `INDEX.md` update status;
- any discrepancy between repo text and package contents.

For visual-inspection doctrine work, returns should also note whether the repo-indexed contact-sheet route or a package fallback was used.

For asset sheet package work, returns must also record:

- rendered asset-sheet PNG path;
- approved source image paths used in the sheet;
- sidecar/spec path and whether it records title, type, status, source/QA, guidance bullets, source-image filenames, and QA decisions;
- confirmation that the approved blank asset sheet template was used for deterministic compile;
- for character asset sheets, confirmation that the main/hero source image is a full-body character shot on a plain white background;
- whether compile intermediates such as HTML, scratch manifests, or helper scripts were omitted or explicitly promoted.

## Status guidance

Use `GREEN` only when the requested work is complete and publication proof is present when required.

Use `AMBER` when the work is useful but incomplete, partially verified, downgraded, or waiting for review.

Use `RED` when the attempted result is invalid for its claimed purpose.

Use `BLOCKED` when a hard tool, source, permission, or policy blocker prevents completion.
