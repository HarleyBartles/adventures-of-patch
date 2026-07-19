# Skill Authoring Policy

Status: active policy
Owner: Adventures of Patch repository
Scope: repo-local skill classification, authoring, review, custody, and refresh
Nearest router: `.agents/AGENTS.md`

This policy governs repository-local skills before any `adventures-*` skill is
created or migrated. It adapts the marketplace skill standards to this repo's
local custody and identity rules.

## Authority and custody

- Generic authoring technique comes from the installed `writing-skills` skill.
- Marketplace frontmatter and projection rules are upstream references, not
  local source custody.
- Repo-local skills are authored under `.agents/skills/adventures-*/`.
- Marketplace-derived skills are projections refreshed from the pinned
  `.agents/plugins/marketplace-source` submodule.
- The deterministic installer must preserve repo-local `adventures-*` skills
  and must never overwrite or prune them.
- Do not add `agents/openai.yaml` to a repo-only skill unless the skill is
  explicitly being prepared for marketplace projection.

## Surface classification

Use the smallest surface that owns the decision.

| Surface | Use it for | Do not use it for |
| --- | --- | --- |
| Skill | A triggerable, reusable technique, pattern, tool capability, or reference guide that addresses recurring agent judgment | One-off solutions, project law, or a deterministic procedure only |
| Doctrine/policy | Durable invariants, authority, source truth, protected boundaries, and must/must-not rules | A task recipe or a triggerable capability |
| Stage guide | Repo-specific, non-binding overlay for design, planning, implementation, or review | Replacing the generic workflow or storing durable law |
| Runbook/playbook | A repeatable procedure with known inputs, paths, commands, outputs, and stop conditions | Judgment that should compose as a skill |
| Reference/contract | Schemas, factual lookup, acceptance criteria, or operating details read on demand | Routing or broad workflow control |
| Script/tool | Mechanical checking, transformation, generation, or enforcement | Instructions that require agent judgment |
| README | Human orientation and usage context | Agent law or read-when routing |
| INDEX.md | Generated navigation and coverage | Operative law or manually maintained inventory |

Project-specific conventions belong in doctrine, guides, or `AGENTS.md` unless
they also provide a recurring, triggerable capability with an owned decision.
The `adventures-` prefix signals local custody; it does not make a document a
skill.

## Skill qualification test

Retain a candidate as a skill only when all of these are true:

1. A human request or observable symptom reliably triggers it.
2. It owns a decision or capability with a clear boundary.
3. The same judgment recurs across multiple Adventures tasks.
4. The behavior is not already owned by a generic skill, local guide,
   doctrine, playbook, reference, or script.
5. A baseline scenario demonstrates a meaningful failure without it.
6. The guidance can be kept compact, with heavy material moved to
   `references/`.

If these tests fail, retire the candidate, merge it into the owning surface,
or convert it to a runbook, policy, reference, or script.

## Required skill shape

Every repo-local skill must have a directory matching its name and a UTF-8
`SKILL.md` with:

- `name`, matching the directory and using lowercase letters, numbers, and
  hyphens;
- a concise `description` beginning with `Use when...`, describing triggers
  rather than summarizing the workflow;
- `metadata` containing stable local identity, status, scope, `use_when`, and
  `do_not_use_when` fields;
- an overview and owned decision;
- hard boundaries and stop conditions;
- a minimal workflow or decision pattern;
- progressive references for detailed operating contracts.

Keep the control plane under 500 words where practical. Do not bind a local
skill to a retired agent identity. Patch may be referenced as the project
character and visual canon, but not as an agent owner or execution actor.

## Authoring gate

Skill authoring is documentation TDD:

1. Write a pressure or application scenario without the candidate skill.
2. Run it and record the baseline failure or ambiguity.
3. Retire or reclassify the candidate if no meaningful failure appears.
4. Write the smallest skill that addresses the observed failure.
5. Run the same scenario with the skill and verify compliance.
6. Identify rationalizations or new ambiguity, revise the skill, and rerun.
7. Verify frontmatter, links, word count, mesh discoverability, and refresh
   preservation before moving to another skill.

Do not bulk-copy marketplace skills, author several untested skills together,
or treat an attractive upstream skill as evidence of local usefulness.

## Review and disposition record

Every assessed candidate must record:

- source and revision;
- local use case and named reader;
- disposition: retain, adapt, merge, reclassify, or retire;
- overlapping canonical surface;
- stale paths, actor names, or authority claims;
- baseline scenario and result;
- final local path or retirement reason.

Marketplace retirement is not capability retirement. A capability is retained
only when the local evidence and qualification test support it.
