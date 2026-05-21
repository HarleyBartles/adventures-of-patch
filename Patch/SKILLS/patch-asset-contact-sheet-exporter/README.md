# Patch asset contact-sheet exporter

Repo-resident Patch execution capability for bounded export of deterministic PNG contact sheets.

## Purpose

Given a structured dispatch JSON that names explicit repo-relative PNG asset paths, the exporter:

- resolves the requested files from the repository root;
- rejects unsafe, absolute, missing, unreadable, or non-PNG inputs;
- renders deterministic contact-sheet PNGs with short visible labels;
- writes `request.json`, `manifest.json`, `skipped.json`, and `evidence.json`;
- packages the rendered sheets and manifests into one `asset-contact-sheets.zip`.

This capability is for local repo work and GPT visual intake. It does not generate images and does not canonicalise assets.

## Dispatch contract

The first-version dispatch shape is:

```json
{
  "request_type": "asset_contact_sheet_export",
  "project": "adventures-of-patch",
  "source_repo": "HarleyBartles/adventures-of-patch",
  "request_id": "sample-contact-sheet-request",
  "issue": 50,
  "purpose": "visual inspection for GPT adventure planning",
  "families": [
    {
      "family_id": "example-family",
      "reason": "why GPT needs this family",
      "png_paths": [
        "assets/example/path/image-a.png"
      ],
      "selectors": []
    }
  ],
  "output": {
    "contact_sheet_per_family": true,
    "zip_all_outputs": true,
    "include_manifest": true
  }
}
```

`png_paths` must be exact repo-relative paths first. `selectors` are deliberately limited in this pass and must not trigger vague whole-tree discovery.

## Real CLI

Run from the repo root:

```bash
python Patch/SKILLS/patch-asset-contact-sheet-exporter/scripts/build_contact_sheets.py \
  --dispatch Patch/SKILLS/patch-asset-contact-sheet-exporter/examples/sample-dispatch.json \
  --output-root output-zips/asset-contact-sheets
```

The command writes a run folder under `output-zips/asset-contact-sheets/` and emits a zip with the sheets plus manifests.

## Output shape

```text
output-zips/asset-contact-sheets/<request-id-or-timestamp>/
  contact-sheets/
    <family-slug>.png
  manifests/
    request.json
    manifest.json
    skipped.json
  evidence.json
  asset-contact-sheets.zip
```

The zip includes the contact sheets and manifest files, plus the evidence file for the run.

## Safety rules

- Resolve inputs from the repository root only.
- Reject absolute paths and path traversal.
- Do not modify source PNGs.
- Record every skipped input with a reason.
- Keep the output deterministic by using stable ordering and fixed layout rules.

## Notes

Selectors are intentionally bounded in this first pass. If a dispatch needs broader lookup semantics, extend the selector logic deliberately rather than falling back to a repo-wide scan.

