# assets/in-flight index

Live directory listing for current working visual references.

## Purpose

This lane holds repo-tracked images that are still in flight: accepted-but-not-yet-canonised references, storyboard diagrams, trial renders, and other visual-preproduction assets.

These files are non-canonical working references. They may be included in visual-intake zips, but they are not source-image packs or canonical asset sheets by default.

## Files in this directory

event_official_at_sports_ceremony.png

## Subdirectories

None.

## Non-canon warning

In-flight images are working references only. Do not treat this lane as canonical source art, compiled asset-sheet output, or a promoted asset package unless a separate canonisation workflow says otherwise.

## How GPT and Patch should request these

Use `in_flight_image_paths` for full-size in-flight PNG inclusions.

Use `in_flight_reference_paths` for full-size in-flight inclusions such as storyboard diagrams or detail references that GPT needs to inspect at native resolution.

If a dispatch also uses source images, compiled sheets, or reference sheets, keep those lanes explicit so in-flight assets stay visibly separate in the manifest and evidence.
