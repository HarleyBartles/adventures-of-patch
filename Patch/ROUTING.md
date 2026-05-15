# Patch Routing

This file defines how work enters Patch's project-local actor surface.

## Default route

For Adventures of Patch project work, the workspace route is:

```text
Will -> Patch
```

There is no Chris-like intermediary for Adventures of Patch.

Patch is the sole current project-local agent for this repo.

## Lane selection

Bind Patch to one lane per task.

### `Patch / project-director`

Use for:

- planning and issue shaping;
- frame-busting and story/world decisions;
- asset-fit decisions;
- source and playbook gate checks;
- verification and completion judgement;
- creating execution-ready dispatch or work packets.

### `Patch / execution`

Use for:

- repo-local file creation or update;
- binary asset landing;
- source zip landing;
- index updates;
- issue mutation when part of execution;
- commit and push;
- remote verification and worker return.

## No separate domain executors

Do not route to separate Adventures asset, deck, canon, image, receipt, or publication actors. They do not exist yet.

If a future boundary appears, create a planning issue before introducing a new actor.

## Required route disclosure

Any Patch worker return must disclose:

- actor binding used;
- repo root;
- lane label;
- issue number if issue-backed;
- whether tracked repo mutation occurred;
- publication and verification state if mutation occurred.

## Will workspace binding

Will is expected to track `HarleyBartles/adventures-of-patch` as a top-level submodule in `will-workspace`.

The submodule add operation should clone/hydrate the repo into Will's governed workspace. Do not assume a pre-existing local checkout is present.

## Source routing

For source/package questions:

1. Start with repo indexes.
2. Use `assets/source-zips/INDEX.md` for source package discovery.
3. Use `assets/hero-patch/INDEX.md` for Patch visual canon.
4. Treat uploaded/project-source zips as bounded evidence only when repo-indexed or user-scoped.

## Stop conditions

Stop instead of continuing if:

- the active lane is unclear;
- the task would mutate outside Adventures without an explicit Will route;
- required source indexes cannot be read;
- repo mutation cannot be committed, pushed, or verified;
- the task would promote generated assets to canon without acceptance evidence.
