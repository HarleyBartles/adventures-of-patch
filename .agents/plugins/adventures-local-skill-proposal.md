# Adventures local skill disposition

Status: assessed for repository-local reimplementation

The marketplace pack is retired from this repository's provider configuration.
This record separates useful recurring judgment from project law, deterministic
procedures, and generic capability already owned elsewhere.

## Retained local skills

| Retired marketplace candidate | Local disposition | Reason and canonical owner |
| --- | --- | --- |
| `adventures-project-doctrine` | Retain/adapt as `adventures-project-doctrine` | Thin triggerable router into the smallest applicable `.agents/doctrine/` surface; the durable rules remain in doctrine. |
| `adventures-frame-buster` | Retain/adapt as `adventures-frame-buster` | Owns the recurring frame/world/lesson gate before deck planning; composes the existing readiness playbook. |
| `adventures-visual-preproduction` | Retain/adapt as `adventures-visual-preproduction` | Owns image requirements, visual-bible interpretation, prompt governance, and preproduction readiness. |
| `adventures-image-qa` | Retain/adapt as `adventures-image-qa` | Owns the single acceptance decision for generated and edited images. |

## New local umbrella skill

| Local skill | Basis | Reason |
| --- | --- | --- |
| `adventures-project-readiness` | `adventures-project-doctrine` plus the readiness boundary | Owns the seed-ready → frame-ready → asset-ready → playbook-ready decision and routes to the stage owner. Durable law remains in `.agents/doctrine/` and the playbook remains the detailed contract. |

## Reclassified or retired candidates

| Candidate | Disposition | Reason |
| --- | --- | --- |
| `adventures-bootstrap` | Retire | The repository router, stage guides, and generic `work-mode-router` already establish the session route; an Adventures-specific bootstrap adds no recurring decision. |
| `adventures-github-operations` | Retire | Generic GitHub proof is already owned by `github-operations`; this repo's exceptions belong in the guides and playbooks. |
| `adventures-storyboard-preflight` | Merge into `adventures-project-readiness` and `adventures-visual-preproduction` | It is a stage-specific readiness packet, not a separate reusable decision boundary. |
| `adventures-visual-bible-creator` | Merge into `adventures-visual-preproduction` | Bible creation is part of preproduction orchestration and must follow the live asset mesh. |
| `adventures-visual-bible-interpreter` | Merge into `adventures-visual-preproduction` | Interpretation is a supporting step, not a separate triggerable owner. |
| `adventures-asset-sheet-compiler` | Reclassify to playbook/script | Compilation is deterministic and governed by `asset-sheet-production-contract.md`. |
| `adventures-asset-sheet-canoniser` | Reclassify to playbook | Landing/canonisation is a publication and custody decision, not an image-generation skill. |

## Existing asset capabilities

The useful capabilities formerly under `Patch/SKILLS/` now live under
`.agents/skills` as:

- `adventures-asset-contact-sheet-exporter`;
- `adventures-asset-directory-source-packager`;
- `adventures-asset-zip-ingress`.

They are repo capabilities, not Patch agent capabilities. Their paths,
frontmatter, and return contracts must be portable and must not bind to a
retired actor identity.

## Marketplace retirement inventory

The full ten-entry retirement record remains in
`adventures-skill-retirement-inventory.md`. `using-linear` remains supplied by
`repo-worker-pack`; `don-logan-boundary` remains intentionally absent.
