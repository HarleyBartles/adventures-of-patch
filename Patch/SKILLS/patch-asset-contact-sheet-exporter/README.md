# Patch asset contact-sheet exporter

Repo-resident Patch execution capability for bounded export of deterministic PNG contact sheets plus full compiled asset-sheet and in-flight visual-reference inclusion.

## Purpose

Given a structured dispatch JSON that names explicit repo-relative source PNGs, optional compiled asset-sheet PNGs, and optional in-flight working references, the exporter:

- resolves the requested files from the repository root;
- rejects unsafe, absolute, missing, unreadable, or non-PNG inputs;
- renders deterministic contact-sheet PNGs from source-image families only;
- includes compiled asset-sheet PNGs in full under `included-assets/`;
- includes all resolved in-flight PNGs in full under `included-assets/<family>/in-flight/`;
- writes `request.json`, `manifest.json`, `skipped.json`, `evidence.json`, and `unresolved.json` when needed;
- packages the rendered sheets, included assets, and manifests into one `asset-contact-sheets.zip`.

This capability is for local repo work and GPT visual intake. It does not generate images and does not canonicalise assets; the rendered contact-sheet zip is an inspection package, not canon.

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
      "source_png_paths": [
        "assets/example/path/image-a.png"
      ],
      "compiled_asset_sheet_paths": [
        "assets/example/path/compiled-sheet.png"
      ],
      "reference_sheet_paths": [
        "assets/example/path/reference-sheet.png"
      ],
      "in_flight_image_paths": [
        "assets/in-flight/working-panel.png"
      ],
      "in_flight_reference_paths": [
        "assets/in-flight/storyboard-diagram.png"
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

`source_png_paths` must be exact repo-relative paths first. `compiled_asset_sheet_paths` are compiled PNG sheets to include in full, not contact-sheet panels. `asset_sheet_paths` remains a legacy alias for `compiled_asset_sheet_paths`. `reference_sheet_paths` are full-size reference PNGs. `in_flight_image_paths` and `in_flight_reference_paths` are both full-size in-flight inclusions that stay visibly in-flight in the manifest. `png_paths` remains a legacy alias for `source_png_paths` only. `selectors` are deliberately limited in this pass and must not trigger vague whole-tree discovery.

## Real CLI

Run from the repo root:

```bash
python Patch/SKILLS/patch-asset-contact-sheet-exporter/scripts/build_contact_sheets.py \
  --dispatch Patch/SKILLS/patch-asset-contact-sheet-exporter/examples/sample-dispatch.json \
  --output-root output-zips
```

The command writes staging under `scratch/contact-sheet-builds/` and emits the final zip directly into `output-zips/`.

## Output shape

```text
scratch/contact-sheet-builds/<request-id-or-timestamp>/
  contact-sheets/
    <family-slug>.png
  included-assets/
    <family-slug>/
      <compiled-sheet>.png
      in-flight/
        <in-flight-image-or-reference>.png
  manifests/
    request.json
    manifest.json
    skipped.json
    unresolved.json
  evidence.json

output-zips/<request-id>.zip
```

The staging folder lives under `scratch/` so `output-zips/` stays a disposable emitted-artifact folder. The final zip includes the contact sheets, full asset sheets, full reference sheets, full in-flight inclusions, and manifest files, plus the evidence file for the run.

## Manifest model

- `rendered_source_contact_sheets` lists the generated contact-sheet panels and their repo-relative PNGs. In-flight PNGs do not appear here.
- `included_existing_assets` lists the full compiled asset sheets copied into the zip under `included-assets/`.
- Each family records whether a source contact sheet was generated and, if not, why.
- Families with only asset sheets record `source_contact_sheet_generated: false` and `source_contact_sheet_reason: asset_sheet_only_no_source_images`.
- In-flight records preserve their lane with `record_type: in_flight_image` or `record_type: in_flight_reference`, but both are copied full-size under `included-assets/<family>/in-flight/`.
- The manifest keeps `included_in_flight_assets` as the authoritative full-size in-flight list. `included_in_flight_references` remains a compatibility alias when present.

## Safety rules

- Resolve inputs from the repository root only.
- Reject absolute paths and path traversal.
- Do not modify source PNGs.
- Record every skipped input with a reason.
- Keep the output deterministic by using stable ordering and fixed layout rules.
- Do not create a contact sheet out of compiled asset sheets or in-flight assets.
- Do not scan the whole repository for vague selectors.
- Keep build staging in `scratch/contact-sheet-builds/` or another ignored local staging root.
- Keep `output-zips/` disposable and gitignored; only emitted zip packages belong there during local use.

## Notes

Selectors are intentionally bounded in this first pass. If a dispatch needs broader lookup semantics, extend the selector logic deliberately rather than falling back to a repo-wide scan.
Asset-sheet-only families are valid and should still be represented in the zip, but only as included full sheets.
