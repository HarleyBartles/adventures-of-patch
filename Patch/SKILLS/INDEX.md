# Patch skills index

Patch skills are repo-resident, Patch-owned executable capabilities for `HarleyBartles/adventures-of-patch`.

These are not the same thing as ChatGPT-native installed skills unless explicitly packaged and installed as such. They are on-disk capability surfaces that Patch can use when bound to `Patch / execution`.

## Files in this directory

None.

## Subdirectories

- `patch-asset-zip-ingress/` - planned Patch capability for ingesting asset zips, classifying contents, routing assets to repo taxonomy locations, rebuilding canonical source packages, updating indexes, publishing, and returning evidence.
- `patch-asset-directory-source-packager/` - repo-resident Patch capability for publishing an existing asset directory into a flat source zip with index updates and publication proof.

## Rules

- Project/domain playbooks live in root `/playbooks/`.
- Patch actor governance lives in `/Patch/`.
- Patch executable capabilities live in `/Patch/SKILLS/`.
- Do not use Patch skills to bypass repo-first source discipline or publication-proof requirements.
