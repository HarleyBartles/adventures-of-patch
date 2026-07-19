# Plugin and Skill Refresh Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers-plus:executing-plans` to implement this plan task-by-task with verification checkpoints.

**Goal:** Install a deterministic repository-local skill set from the latest marketplace submodule, retire `adventures-*` from marketplace custody, and leave an evidence-backed proposal for the repo-local Adventures skill set.

**Architecture:** Follow the portfolio installer pattern with a nested marketplace git submodule, a manifest-driven Python refresh command, thin PowerShell and shell launchers, and `.agents/skills/.provenance.json`. The configured providers are `repo-worker-pack` and `superpowers-plus`; the reserved local prefix is `adventures-`. The retired `adventures-pack` is inspected for the inventory only, not installed. Marketplace skills with identical content from multiple providers are materialized once and recorded with all providers.

**Tech Stack:** Git submodules, Python 3 standard library, PowerShell, Bash, JSON, Markdown.

**Execution status:** Complete for the plugin refresh slice. Local
`adventures-*` skill authoring was intentionally deferred here and is covered
by the continuation plan at
`.agents/superpowers/plans/2026-07-19-remaining-agent-workspace-slices.md`.

## Global Constraints

- Work only on plugin and skill surfaces in this slice.
- Preserve the existing unrelated CRLF-only dirty state; do not normalize the wider repository in this slice.
- Do not create or move the local `adventures-*` skills yet; produce the assessment and proposal, because local skill authoring requires a later bounded pass.
- Do not import any marketplace skill whose name starts with `adventures-`.
- Derive paths from the Git repository root; do not encode `Z:\` in runtime tooling.
- The marketplace source must be clean and the parent gitlink must equal the source checkout `HEAD` before refresh.
- The installer must support write mode and `--check` mode, and write deterministic UTF-8/LF output.

---

### Task 1: Add the latest marketplace source and manifest

**Files:**
- Create: `.gitmodules`
- Create: `.agents/plugins/marketplace-source` as a gitlink to the marketplace repository
- Modify: `.agents/plugins/marketplace.json`
- Replace: `.agents/plugins/adventures-pack.lock.json` with current refresh provenance if the new installer makes it obsolete

**Steps:**

- [x] Fetch `origin/main` in the main checkout and record the current `HEAD`, remote main SHA, and pre-existing dirty state before mutation.
- [x] Add `https://github.com/HarleyBartles/agent-asset-marketplace.git` at `.agents/plugins/marketplace-source`.
- [x] Fetch the marketplace submodule's `origin/main`, check out that exact latest main revision, and stage the gitlink.
- [x] Configure the local manifest with `repo-worker-pack` and `superpowers-plus`, exact source paths/versions, and `local_skill_prefixes: ["adventures-"]`.
- [x] Retire `adventures-pack` from this repository's configured provider set; retain the marketplace source submodule for the generic providers.

**Checks:**

```powershell
git -C .agents/plugins/marketplace-source status --short --branch
git -C .agents/plugins/marketplace-source rev-parse HEAD
git submodule status -- .agents/plugins/marketplace-source
python -c "import json; json.load(open('.agents/plugins/marketplace.json', encoding='utf-8'))"
```

### Task 2: Add deterministic skill refresh tooling

**Files:**
- Create: `scripts/install_agent_skills.py`
- Create: `scripts/install_agent_skills.ps1`
- Create: `scripts/install_agent_skills.sh`

**Steps:**

- [x] Adapt the portfolio installer pattern to this repo's manifest and source path.
- [x] Load the reserved local prefixes from the manifest and preserve tracked local skill directories matching them.
- [x] Enumerate configured plugin skill directories, excluding reserved `adventures-*` names.
- [x] Accept duplicate marketplace skill names only when their complete trees match; materialize one deterministic copy and record all providers in provenance.
- [x] Reject missing plugins, version mismatches, source/gitlink mismatches, links/reparse points, path escapes, reserved output names, untracked local skills, and configured providers with no eligible skills.
- [x] Remove any dependency on Portfolio-only linked-worktree scripts so the command can validate this repository's authorized main checkout.
- [x] Preserve `AGENTS.md`, `INDEX.md`, `.provenance.json`, and tracked local skills while pruning stale marketplace-derived entries.
- [x] Make `--check` read-only and make write mode idempotent.

**Checks:**

```powershell
python scripts/install_agent_skills.py --help
python scripts/install_agent_skills.py --check
```

### Task 3: Refresh derived skills and write the Adventures assessment

**Files:**
- Create/update: `.agents/skills/*` marketplace-derived skill directories
- Create/update: `.agents/skills/.provenance.json`
- Create: `.agents/plugins/adventures-skill-retirement-inventory.md`
- Create: `.agents/plugins/adventures-local-skill-proposal.md`

**Steps:**

- [x] Run the installer in write mode from the repository root.
- [x] Confirm the derived output contains generic repo-worker and Superpowers skills, including the canonical `using-linear`, with no `adventures-*` directories and no `don-logan-boundary`.
- [x] Inventory all `adventures-*` directories present in the latest marketplace pack, recording source path, current role, retirement-from-marketplace decision, and local assessment.
- [x] Propose the local `adventures-*` skill set, including adapted candidates from the 10 marketplace skills and renamed candidates for the existing `Patch/SKILLS` capabilities.
- [x] Mark local skill authoring as deferred to a later bounded pass; do not copy unreviewed marketplace skills into local custody in this slice.

**Checks:**

```powershell
python scripts/install_agent_skills.py --check
Get-ChildItem .agents/skills -Directory | Where-Object Name -like 'adventures-*'
git diff --check -- .agents/plugins .agents/skills scripts .gitmodules
```

### Task 4: Verify deterministic convergence and hand off

**Steps:**

- [x] Run the installer a second time and prove the derived tree is unchanged.
- [x] Run `--check` after the second refresh.
- [x] Compare the inventory against the live marketplace submodule at the recorded gitlink SHA.
- [x] Review the staged diff to ensure no guides, mesh-wide cleanup, Patch identity cleanup, or unrelated project files entered this slice.
- [ ] Commit the plugin/skill slice and report the exact source SHA, derived skill inventory, retirement inventory, local proposal, validation output, and remaining follow-up.

**Checks:**

```powershell
git diff --quiet -- .agents/skills
python scripts/install_agent_skills.py --check
git status --short --branch
git diff --cached --check
```

**Handoff confidence:** 9/10 after the live submodule and generated provenance checks pass.
