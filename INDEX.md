# Repository index

This is the root navigation index for `HarleyBartles/adventures-of-patch`.

Use this file first when spelunking the repo through a GitHub API connector. Each directory should have its own `INDEX.md` that lists the files directly inside it and points to child directory indexes.

## Top-level files

- `AGENTS.md` - agent navigation, source discipline, Patch rules, and production gates.
- `README.md` - short project orientation.
- `.gitignore` - local and generated-file ignore rules.

## Top-level directories

- `Patch/` - Patch project-local actor surface, with project-director and execution lanes. See `Patch/README.md`.
- `assets/` - reusable visual assets, source packages, receipts, and Patch canon. See `assets/INDEX.md`.
- `decks/` - committed presentation artifacts and deck working folders. See `decks/INDEX.md`.
- `docs/` - project documentation, adventure concepts, principles, and workflow notes. See `docs/INDEX.md`.
- `playbooks/` - first-class Adventures project/domain playbooks. See `playbooks/INDEX.md`.
- `scratch/` - local working area, not canonical. See `scratch/INDEX.md`.
- `skills/` - project-specific ChatGPT skill packages or source copies when intentionally committed. See `skills/INDEX.md`.

## Canonical navigation rules

- The repo is canonical project truth.
- Uploaded zips or chat attachments are not active canon unless committed here or explicitly scoped by the user.
- For Patch actor-governed work, start with `Patch/README.md`, `Patch/GOVERNANCE.md`, and `Patch/ROUTING.md`.
- For Patch-owned executable capabilities, start with `Patch/SKILLS/INDEX.md`.
- For project/domain playbooks, start with `playbooks/INDEX.md`.
- For Patch image work, start with `assets/hero-patch/INDEX.md` and inspect the style guide before planning or generating images.
- For issue-to-deck or issue-to-PPTX work, start from the GitHub issue, then use the production pipeline described in `AGENTS.md` and `playbooks/INDEX.md`.
