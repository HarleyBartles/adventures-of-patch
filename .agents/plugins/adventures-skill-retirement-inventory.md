# Adventures Marketplace Skill Retirement Inventory

Status: assessed against the retired marketplace pack originally present at
revision `44571abcc1c369d62e316b4694a89c7c2c1bd3bd`; latest marketplace main is
`70a7bb0f8181f81f2a063ddce4458dea1a2debcb`.

Source:

- Plugin: `codex-marketplace/plugins/adventures-pack`
- Skills: `codex-marketplace/plugins/adventures-pack/skills`
- Bundle manifest: `codex-marketplace/plugins/adventures-pack/references/bundle-manifest.json`

## Decision

Retire the entire `adventures-pack` plugin from this repository's configured
marketplace providers. Its two non-local entries are handled elsewhere:

- `using-linear` is already installed from `repo-worker-pack`.
- `don-logan-boundary` is planned for retirement and is intentionally not
  installed.

All ten `adventures-*` entries are retired from marketplace custody. This is a
custody decision, not a claim that every capability is discarded: the retained
local skills and reclassifications are recorded in the companion disposition.

## Marketplace entries

| Skill | Marketplace source | Retirement decision | Validity note |
| --- | --- | --- | --- |
| `adventures-asset-sheet-compiler` | `sources/first_party/skills/adventures-asset-sheet-compiler` | Retire; reclassify to playbook/script | Deterministic template compilation is governed by the asset-sheet production contract. |
| `adventures-bootstrap` | `sources/first_party/skills/adventures-bootstrap` | Retire | The repository router, stage guides, and generic work-mode routing already own session entry. |
| `adventures-frame-buster` | `sources/first_party/skills/adventures-frame-buster` | Retire | Its frame gate is absorbed by the local `adventures-project-readiness` router. |
| `adventures-github-operations` | `sources/first_party/skills/adventures-github-operations` | Retire | Generic GitHub proof already owns this capability. |
| `adventures-image-qa` | `sources/first_party/skills/adventures-image-qa` | Retire from pack; retain locally | Owns the single visual acceptance decision and composes the image-QA contract. |
| `adventures-project-doctrine` | `sources/first_party/skills/adventures-project-doctrine` | Retire from pack; retain locally | The local skill is a thin triggerable router; durable project law belongs in `.agents/doctrine/adventures-project-doctrine.md`. |
| `adventures-storyboard-preflight` | `sources/first_party/skills/adventures-storyboard-preflight` | Retire; merge into local routes | Its readiness packet is owned by project readiness and visual preproduction. |
| `adventures-visual-bible-creator` | `sources/first_party/skills/adventures-visual-bible-creator` | Retire; merge into local route | Bible creation is part of visual preproduction orchestration. |
| `adventures-visual-bible-interpreter` | `sources/first_party/skills/adventures-visual-bible-interpreter` | Retire; merge into local route | Bible interpretation is supporting preproduction judgment, not a separate owner. |
| `adventures-visual-preproduction` | `sources/first_party/skills/adventures-visual-preproduction` | Retire from pack; retain locally | Owns image requirements, prompt governance, and asset readiness before production. |

## Proof of local exclusion

The local manifest no longer configures `adventures-pack`. The deterministic
installer's reserved prefix remains `adventures-`, so even if the plugin is
examined again in a future assessment checkout, those names cannot become
marketplace-derived output.

Current derived output is recorded in
`.agents/skills/.provenance.json`; it contains `using-linear` from
`repo-worker-pack`, no `don-logan-boundary`, and no marketplace-derived
`adventures-*` directories. Local `adventures-*` skills are repository-owned
and preserved separately.
