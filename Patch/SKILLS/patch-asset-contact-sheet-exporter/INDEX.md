# patch-asset-contact-sheet-exporter index

Repo-resident Patch execution capability for deterministic PNG contact-sheet exports from source images plus full compiled, reference, and in-flight asset inclusion from bounded dispatch JSON.

## Files in this directory

- `README.md` - capability overview, dispatch contract, and real CLI invocation.
- `examples/sample-dispatch.json` - small repo-tracked sample dispatch using source-image plus compiled-sheet inputs.
- `examples/asset-sheet-only-dispatch.json` - sample dispatch proving asset-sheet-only inclusion without a fake contact sheet.
- `examples/in-flight-visual-intake-dispatch.json` - sample dispatch proving source-image contact sheets plus full-size in-flight inclusion handling.
- `scripts/build_contact_sheets.py` - deterministic exporter that renders source-image contact sheets, includes compiled/reference/in-flight assets full-size, writes manifests/evidence, and packages a zip.

## Subdirectories

- `examples/` - sample dispatches for local smoke tests.
- `scripts/` - executable exporter scripts for the capability.

## Related project playbook

- `../../../../playbooks/asset-package-landing.md` - closest repo-local packaging discipline reference for output shape and publication hygiene.

Build staging lives under `scratch/contact-sheet-builds/`, while `output-zips/` is the disposable emitted-artifact folder for local zip outputs.
