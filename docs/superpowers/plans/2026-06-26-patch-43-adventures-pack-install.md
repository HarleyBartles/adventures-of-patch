# PATCH-43 Adventures Pack Install Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Install the Adventures project plugin from the Asset Marketplace repo through a pinned repo-local marketplace entry, with an audit lock file and compact repo guidance, without vendoring generated skills into `.agents/skills`.

**Architecture:** The Adventures repo becomes a consumer of the Asset Marketplace `adventures-pack` plugin through `.agents/plugins/marketplace.json`, pointing to `HarleyBartles/agent-asset-marketplace` at the reviewed commit `2ae5f3a33670c212a8e09345302c5b47bbc0d873` via `git-subdir`. The repo also records a lock file with the plugin identity, source location, pinned SHA, plugin version, and exact bundled skill set. Repo guidance stays compact in `AGENTS.md` so workers use the pinned plugin path instead of treating `.agents/skills` as canonical.

**Tech Stack:** GitHub contents API, local git worktree, JSON metadata, Markdown guidance, Codex plugin install surface.

## Global Constraints

- Keep scope to PATCH-43 only.
- Do not vendor-copy generated skills into `.agents/skills` as the primary solution.
- Do not edit Asset Marketplace source from the Adventures repo.
- Do not use a floating `main` ref where a pinned SHA is available.
- Treat the plugin's bundled `skills/` as the installable skill set; do not invent extra dependency semantics.
- If Codex cannot install from a pinned `git-subdir` marketplace entry in this runtime, stop and report the exact limitation, then propose the smallest fallback.
- Repo guidance should say: use the pinned repo plugin; do not local-vendor skills unless explicitly repairing the plugin path.

---

### Task 1: Add the repo-local plugin registration and lock file

**Files:**
- Create: `.agents/plugins/marketplace.json`
- Create: `.agents/plugins/adventures-pack.lock.json`

**Interfaces:**
- Consumes: Asset Marketplace plugin metadata at commit `2ae5f3a33670c212a8e09345302c5b47bbc0d873`, bundle manifest, source map, and the repo's guidance surfaces.
- Produces: repo-local plugin source registration and an audit receipt for the Adventures pack install.

- [ ] **Step 1: Create the marketplace entry**

```json
{
  "name": "adventures-repo-plugins",
  "interface": {
    "displayName": "Adventures Repo Plugins"
  },
  "plugins": [
    {
      "name": "adventures-pack",
      "source": {
        "source": "git-subdir",
        "url": "https://github.com/HarleyBartles/agent-asset-marketplace.git",
        "path": "./codex-marketplace/plugins/adventures-pack",
        "sha": "2ae5f3a33670c212a8e09345302c5b47bbc0d873"
      },
      "policy": {
        "installation": "INSTALLED_BY_DEFAULT",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

- [ ] **Step 2: Create the audit lock file**

```json
{
  "plugin": "adventures-pack",
  "source_repo": "https://github.com/HarleyBartles/agent-asset-marketplace.git",
  "source_path": "codex-marketplace/plugins/adventures-pack",
  "source_sha": "2ae5f3a33670c212a8e09345302c5b47bbc0d873",
  "plugin_version": "1.0.0",
  "expected_skills": [
    "adventures-project-doctrine",
    "adventures-bootstrap",
    "adventures-github-operations",
    "adventures-visual-preproduction",
    "adventures-storyboard-preflight",
    "adventures-visual-bible-creator",
    "adventures-visual-bible-interpreter",
    "adventures-image-qa",
    "adventures-asset-sheet-compiler",
    "adventures-project-readiness",
    "don-logan-boundary",
    "linear"
  ],
  "updated_at": "2026-06-26"
}
```

- [ ] **Step 3: Run a structural sanity check**

Run:

```powershell
Get-Content .agents/plugins/marketplace.json | ConvertFrom-Json | Out-Null
Get-Content .agents/plugins/adventures-pack.lock.json | ConvertFrom-Json | Out-Null
```

Expected: both files parse as JSON and the pinned SHA matches `2ae5f3a33670c212a8e09345302c5b47bbc0d873`.

### Task 2: Update repo guidance to point workers at the pinned plugin

**Files:**
- Modify: `AGENTS.md`

**Interfaces:**
- Consumes: the new plugin marketplace entry and lock file.
- Produces: a compact repo guidance note that tells workers to use the pinned repo plugin instead of treating `.agents/skills` as canonical for this pack.

- [ ] **Step 1: Add a short guidance block**

Insert this text in the repo guidance surface near the source-of-truth rules:

```markdown
For Adventures plugin installs, use `.agents/plugins/marketplace.json` and the pinned `adventures-pack` source entry. Do not treat `.agents/skills` as canonical for this bundle unless the issue explicitly documents a fallback.
```

- [ ] **Step 2: Keep the guidance compact**

Run:

```powershell
Select-String -Path AGENTS.md -Pattern 'adventures-pack|\\.agents/plugins/marketplace.json|\\.agents/skills'
```

Expected: one compact guidance hit, with no new long-form doctrine added around plugin semantics.

### Task 3: Smoke-test the install surface and close the plan branch cleanly

**Files:**
- None expected if the install surface succeeds
- If the runtime cannot see the repo-local marketplace entry, record the exact blocker in the plan branch notes and stop

**Interfaces:**
- Consumes: the committed repo-local marketplace entry and lock file.
- Produces: either a visible `adventures-pack` install result or a precise blocker statement that names the missing runtime capability.

- [ ] **Step 1: Ask the runtime to install the plugin from the repo-local marketplace entry**

Use the available Codex plugin install surface to request `adventures-pack` after the marketplace file exists. Confirm the returned snapshot exposes:

1. plugin name `adventures-pack`
2. version `1.0.0`
3. source repo `https://github.com/HarleyBartles/agent-asset-marketplace.git`
4. source path `codex-marketplace/plugins/adventures-pack`
5. pinned SHA `2ae5f3a33670c212a8e09345302c5b47bbc0d873`

- [ ] **Step 2: If install cannot be proven, record the exact limitation**

If the runtime cannot consume the pinned `git-subdir` marketplace entry, stop after capturing the exact tool or connector limitation. Do not substitute a floating ref, a local-vendored skill copy, or a guessed fallback path.

- [ ] **Step 3: Verify the worktree is ready for plan commit**

Run:

```powershell
git status --short
```

Expected: only the intended plan files and repo-guidance edits are staged or ready to stage, with no unrelated worktree drift.

## Self-Review

- Spec coverage: the plan covers the pinned marketplace entry, the lock file, the repo guidance update, and a runtime smoke test or precise blocker report.
- Placeholder scan: no TBD, TODO, or vague dependency wording remains in the plan.
- Type consistency: the pinned SHA, plugin version, source path, and expected skill list match the Asset Marketplace source metadata read during preflight.
