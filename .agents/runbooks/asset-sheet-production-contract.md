# Asset sheet production contract

This contract defines the canonical final-layout rule for Adventures of Patch asset sheets.

## Scope

Use this contract whenever a reusable visual asset sheet is produced or updated, including asset class overviews, individual character sheets, Patch costume variant sheets, environment/location sheets, prop sheets, hero prop or continuity-object sheets, interaction sheets, style sheets, and anti-pattern sheets.

This contract does not authorize body-slide scene art. It governs preproduction asset-sheet packaging and final sheet layout.

## Required production shape

Asset sheet production is always source-image first and deterministic-sheet second:

```text
plan asset sheet -> generate focused source images -> stop for Harley review -> QA accepted source images -> deterministic compile into approved asset-sheet template -> final sheet/lane compliance QA -> Harley approval -> zip package -> repo/source-package landing when requested
```

Do not ask image generation to create the final sheet layout. Image generation creates the source images only. The final compiled asset sheet must be built by deterministic compile into the approved blank asset-sheet template.

## Approved template rule

Use the current approved blank asset sheet template as the final layout for every asset sheet. The approved template is the one Harley placed as a first-class project-source/library template package after approving `template_final_asset_sheet_blank_v3.png`. Project sources are reserved for asset-sheet template package(s) only for now unless Harley changes that policy.

For template packages, the repo PNG and JSON sidecar are required source truth, and the matching project-source PNG plus spec are also required and must be discoverable through the index mesh. Do not treat either side as sufficient on its own.

Before deterministic compile, read the repo JSON sidecar first, then use the matching project-source PNG and spec filenames recorded there. Do not compile from the repo PNG alone or from session memory.

The template structure is:

- hard-text header: `ASSET SHEET`;
- shadow placeholder fields for asset title, type, status, version, and source/QA;
- left main image area;
- right `GUIDANCE` panel for bullet-pointed design guidance;
- bottom `ALTERNATE VIEWS` rail with six-slot rhythm;
- only two visible required alternate placeholders in the blank template;
- unused optional alternate slots left as empty space, not squeezed or resized.

Actual sheet compile may cover shadow placeholder text with opaque white text boxes. Shadow text is fallback structure only. It is not permission to leave example prose, process notes, or operator context in the final sheet.

## Character hero-shot rule

For all character asset sheets, including Patch costume variants and non-Patch characters, the main/hero source image must be a full-body character shot on a plain white background.

Alternate views may include close-ups, pose variants, character-in-world shots, detail shots, prop handoffs, expression/gesture studies, or environmental context, as long as they remain QA-accepted and lane-appropriate.

A character sheet is not ready to compile if it lacks the full-body plain-white hero shot.

## Source image requirements

Every image used in the final asset sheet must have an accepted Adventures image QA decision in the correct lane before compile.

Source images should be saved as durable package contents. Do not use unreviewed, rejected, weak, or reference-only images in the compiled asset sheet.

For Patch-bearing source images, enforce current Patch canon and Patch preflight. For non-Patch source images, enforce style-system fit, identity continuity, function, and lane discipline.

## Guidance panel requirements

Guidance content should be rendered by deterministic compile from a spec or sidecar, not generated into the source image.

Use short wrapped bullets. Typical bullets cover:

- identity-critical features;
- allowed variation;
- do-not-change rules;
- source image and QA basis;
- known anti-drift notes;
- intended downstream use.

If guidance overflows the panel, the compiler must reduce text within a safe range or fail loudly. Do not silently draw outside the panel.

## Final package contract

The final deliverable for an asset sheet is a zip package containing:

- the compiled asset-sheet PNG;
- every approved source image used in that sheet;
- a markdown or JSON sidecar/spec recording title, asset type, status, version/source/QA text, guidance bullets, source-image filenames, QA decisions, and any skipped/omitted candidate images with reasons when relevant.

The final canonical artifact is the compiled asset-sheet PNG. HTML files, scratch manifests, and temporary compile scripts are intermediates unless Harley explicitly promotes them as durable source.

## Landing posture

When landing in the repo, place the compiled asset sheet and approved source images in the relevant asset directory. Place the zip package in `assets/source-zips/` only when the package is intended as a repo-tracked source/import package or integrity receipt. Update the relevant asset directory index and `assets/source-zips/INDEX.md` when applicable.

Do not call the sheet canonical solely because the zip exists. Canonical status requires repo/source-package/index evidence and any required Harley approval threshold.
