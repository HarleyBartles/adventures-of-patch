# patch-asset-contact-sheet-exporter index

Repo-resident Patch execution capability for deterministic PNG contact-sheet exports from bounded dispatch JSON.

## Files in this directory

- `README.md` - capability overview, dispatch contract, and real CLI invocation.
- `examples/sample-dispatch.json` - small repo-tracked sample dispatch using existing PNG assets.
- `scripts/build_contact_sheets.py` - deterministic exporter that renders contact sheets, manifests, skipped records, evidence, and a packaged zip.

## Subdirectories

- `examples/` - sample dispatches for local smoke tests.
- `scripts/` - executable exporter scripts for the capability.

## Related project playbook

- `../../../../playbooks/asset-package-landing.md` - closest repo-local packaging discipline reference for output shape and publication hygiene.

