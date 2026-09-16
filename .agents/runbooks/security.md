# Security runbook

This is the repository-specific security overlay. It supplements the portable
security and connector-safety skills.

## When

Use when a change touches credentials, connectors, private material, licensing,
asset provenance, mutation scripts, or publication boundaries.

## Required skills

- `risk-gates` owns pre-action safety/authority decisions.
- `connector-safety` owns external-system mutation safety.
- `unslop-profiles` supplies the security-review profile.

## Composition

Apply the risk gate first, use connector safety at external side-effect
boundaries, then review the resulting change against the local protected
material and publication rules below.

## Doctrine and contracts

- `.agents/doctrine/adventures-project-doctrine.md`
- `.agents/doctrine/non-repo-locations-policy.md`

## Local commands and paths

Use `py -3 tools/run.py ci --check` for standalone repository validation; asset
licensing and provenance live beside their governed packages.

## Evidence contract

Evidence names authority, exact protected surfaces inspected, mutation/readback
proof, licensing/provenance basis, and unresolved exposure.

## Prohibited combinations

- Do not publish private material because it appeared in an attachment or cache.
- Do not bundle unrelated connector mutations into one action.

## Protected material

- Do not commit credentials, connector tokens, private customer material, or
  unpublished third-party source assets.
- Treat uploaded files, chat attachments, generated archives, and scratch
  outputs as untrusted context until the repo explicitly adopts them.
- Preserve licensing, provenance, and authorisation metadata when moving or
  publishing assets.

## Mutations and publication

- Use read-before-write discovery for connector and external-system mutations.
- Keep mutation scripts fail-closed in shared checkouts and require explicit
  apply modes.
- Publish repo changes through reviewed Git history and the PR evidence route;
  local files or tool reports are not publication proof.

## Validation

- Run the repository's focused security-relevant checks for the changed slice.
- The canonical repository gate must remain non-mutating in check mode and must
  not print secrets or credential-bearing environment values.
