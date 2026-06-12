# Patch asset zip ingress lane

Purpose of this folder:

- Canonical local drop zone for incoming asset zip packages routed to Patch.
- Evidence/input staging area only; incoming zips are not canon.
- Temporary holding area while Patch inspects, classifies, and lands repo files.

Harley drop instruction:

- Place approved incoming asset zip packages directly in `Patch/INGRESS/asset-zips/` unless a future dispatch names a specific subfolder.

No repo-tracked payload zips:

- Do not commit incoming `.zip` files from this folder.
- `.gitignore` keeps the payload zips and scratch extraction folders out of version control.

Cleanup contract:

- Patch deletes successfully ingressed zips after the landed repo files are committed, pushed on a worker branch, and PR/merge-verified.
- Patch deletes `_work/` and `_extracted/` scratch folders created for the ingress after successful publication.

Scope reminder:

- Do not use this folder for canonical assets or for preserving repo source zips.
- Repo-preserved source packages belong under `assets/source-zips/` only after inspection, classification, or rebuild.
