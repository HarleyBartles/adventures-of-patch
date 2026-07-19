# Adventures Marketplace Skill Retirement Inventory

Status: assessed against the marketplace submodule at revision
`44571abcc1c369d62e316b4694a89c7c2c1bd3bd`.

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
custody decision, not a claim that every capability is discarded: retained
capabilities are proposed for later repository-local adaptation in the
companion proposal.

## Marketplace entries

| Skill | Marketplace source | Retirement decision | Validity note |
| --- | --- | --- | --- |
| `adventures-asset-sheet-compiler` | `sources/first_party/skills/adventures-asset-sheet-compiler` | Retire from pack; local candidate | Relevant to the repo's asset-sheet templates and production contract; adapt bundled `/home/oai/skills` examples to portable repo-derived paths. |
| `adventures-bootstrap` | `sources/first_party/skills/adventures-bootstrap` | Retire from pack; local candidate | Relevant as a project bootstrap router; remove assumptions that Patch is an agent identity. |
| `adventures-frame-buster` | `sources/first_party/skills/adventures-frame-buster` | Retire from pack; local candidate | Relevant to frame-readiness and storyboard gates; retain Patch as character, not actor. |
| `adventures-github-operations` | `sources/first_party/skills/adventures-github-operations` | Retire from pack; local candidate | Relevant as an Adventures-specific layer over generic GitHub proof; align with this repo's live workflows. |
| `adventures-image-qa` | `sources/first_party/skills/adventures-image-qa` | Retire from pack; local candidate | Relevant to visual QA and existing image QA playbooks; adapt actor-boundary language. |
| `adventures-project-doctrine` | `sources/first_party/skills/adventures-project-doctrine` | Retire from pack; local candidate | Relevant project doctrine; split durable project law from retired Patch governance. |
| `adventures-storyboard-preflight` | `sources/first_party/skills/adventures-storyboard-preflight` | Retire from pack; local candidate | Relevant to storyboard and prompt-board preparation; update downstream actor/tool names to current repo surfaces. |
| `adventures-visual-bible-creator` | `sources/first_party/skills/adventures-visual-bible-creator` | Retire from pack; local candidate | Relevant to the repo's visual-bible creation playbook and Patch canon. |
| `adventures-visual-bible-interpreter` | `sources/first_party/skills/adventures-visual-bible-interpreter` | Retire from pack; local candidate | Relevant to interpreting the visual bible; keep interpretation separate from generation authority. |
| `adventures-visual-preproduction` | `sources/first_party/skills/adventures-visual-preproduction` | Retire from pack; local candidate | Relevant to the existing visual-preproduction playbook and source-first readiness checks. |

## Proof of local exclusion

The local manifest no longer configures `adventures-pack`. The deterministic
installer's reserved prefix remains `adventures-`, so even if the plugin is
examined again in a future assessment checkout, those names cannot become
marketplace-derived output.

Current derived output is recorded in
`.agents/skills/.provenance.json`; it contains `using-linear` from
`repo-worker-pack`, no `don-logan-boundary`, and no `adventures-*` directories.
