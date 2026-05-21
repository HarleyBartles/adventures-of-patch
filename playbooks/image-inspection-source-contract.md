# Image inspection source contract

This contract defines how GPT should visually inspect repo-canonical image assets.

## Source truth

Repo image files are canonical source truth. Asset-family indexes describe what images exist and what they are for.

Repo-indexed contact-sheet dispatch/intake packages built by the Patch contact-sheet exporter are the default visual inspection surface for repo-canonical images. They are inspection packages, not source truth.

Source zips, project-source zips, source-package mirrors, and receipt packages are not the default image-inspection truth for GPT.

## Default inspection route

When GPT needs to inspect a repo-canonical image:

1. Start from `assets/INDEX.md`.
2. Read the relevant asset-family `INDEX.md`.
3. Discover the current repo-indexed contact-sheet dispatch or intake package through the repo index mesh.
4. Open the rendered contact-sheet PNGs or included full-size references from that package.
5. Visually inspect the rendered image surface.

If the needed contact-sheet package is missing or stale, use the Patch contact-sheet exporter and the repo index mesh to produce or refresh the package, then inspect the resulting contact-sheet PNGs. Do not promote the package itself to canon.

## Contact-sheet package contract

- Contact sheets are built from bounded, repo-relative dispatches.
- One package may cover one or more asset families, but the dispatch must name the explicit files or bounded selectors.
- The package records the rendered contact-sheet PNGs, included full-size references, manifests, and evidence.
- The package is an inspection input, not a canonical asset surface.

## Source zips and project sources

Source zips remain valid for bounded package work only:

- import or transfer bundle review;
- source package rebuild checks;
- receipt/evidence package handling;
- package integrity checks;
- explicit user-scoped zip inspection;
- contact-sheet package support when the dispatch needs full-size source or in-flight inclusion.

Do not inspect source zips or project-source visual packages as the ordinary way to view repo PNGs.

For now, project sources should contain only asset sheet template package(s), unless Harley explicitly changes that policy.

For template packages only, the repo template PNG plus its JSON sidecar and the matching project-source PNG plus spec must both be discoverable and reconciled through the index mesh before the package is treated as ready.

## False-green checks

A run is not green if it claims image inspection was complete because a source zip existed, a package was listed, a repo path was known, or a project-source package name matched.

A run may claim visual inspection only when GPT inspected a rendered image surface from a repo-indexed contact-sheet package.

If the required package is blocked, report the exact blocker and either stop or mark reduced confidence before using any package fallback.
