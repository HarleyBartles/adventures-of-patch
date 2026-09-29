# Agent asset and standards provenance

## Repository-owned skills

These skills are authored and maintained in this repository, listed exactly in `.agents/plugins/marketplace.json` under `repo.local_skills`, and are not marketplace projections:

- `adventures-project-doctrine`
- `adventures-project-readiness`
- `directing-visual-stories`
- `generating-images`

## Selected marketplace standards

The pinned `.agents/plugins/marketplace-source` gitlink supplies implementation resources for the standards declared in `.agents/contracts/operating-standards.json`. Deployed resource paths, source paths, checksums, and the source revision are recorded in `.agents/standards/provenance.json`. The upstream repository and its notices govern those source resources.

Marketplace plugins are ambient and are not subscribed to or copied into `.agents/skills/`. There is no installed-plugin skill snapshot in this repository.
