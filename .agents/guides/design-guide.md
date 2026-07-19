# Adventures design guide

This is the repository-specific overlay for design work. It does not replace
`repo-worker-base`, `brainstorming`, or `risk-gates`.

## Route

1. Read the root `AGENTS.md`, `README.md`, `docs/project/INDEX.md`, and the
   relevant project playbook.
2. For an adventure or deck, establish the teaching problem and a concrete
   frame/world before visual styling. Use `adventures-project-readiness` and
   `adventures-frame-buster` when the issue is not already green.
3. For Patch-bearing work, inspect `assets/canon/patch/INDEX.md` and the
   repo-tracked Patch references before choosing visual direction.
4. Record the decision in the canonical issue, plan, or project document; do
   not make a chat-only frame or visual bible authoritative.

## Local boundaries

- Use `playbooks/pre-playbook-adventure-readiness.md` for readiness contracts.
- Use `playbooks/visual-preproduction.md` for reusable visual language and
  image requirements.
- Do not generate images during deterministic design, QA, or policy work.
- Patch is a character and visual canon, not an agent, actor lane, or owner.
- Do not turn a doctrine rule, one-off frame, or deterministic asset procedure
  into a new skill.

## Design output

A useful design handoff names the audience problem, frame/world, lesson,
anti-pattern, positive pattern, Patch role when applicable, visual risks, and
the next readiness gate. If those are unresolved, return amber or blocked.
