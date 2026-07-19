# Pre-playbook adventure readiness playbook

This playbook defines the required planning state before an Adventures of Patch issue may enter the end-to-end PPTX production playbook.

The production playbook should remain strict and staged. It should not privately invent a frame, teaching model, cast, world, or visual language while building a deck. If a source issue is thin, the production playbook stops and routes outward to this readiness process.

## Scope

Use this playbook before running `playbooks/end-to-end-pptx-production.md` on an adventure-plan issue, deck-plan issue, proof run, production pass, or similar issue-to-PPTX request when the issue is not already known to be playbook-ready.

A seed issue may still be valuable and in scope for future Adventures of Patch decks even when it is not production-ready. The purpose of this pre-playbook pass is to mature the issue, not to reject it as an idea.

## Readiness ladder

### Seed-ready

The issue contains a useful topic, theme, agent-work problem, or adventure idea.

Seed-ready is not enough for PPTX production. Most thin adventure issues start here.

### Frame-ready

The framing family has produced a green result. Frame-ready means the issue has:

- a theme/world;
- a real-world autonomous-agent model;
- an anti-pattern;
- a positive pattern;
- Patch's role;
- cast-to-function mapping;
- environment/location-to-domain mapping;
- prop/tool/state mapping;
- a continuity object or state transition;
- ordered story progression;
- concrete recommendations the target audience can apply.

Frame-ready is story and teaching readiness. It is not visual production readiness.

### Asset-ready

Visual preproduction has created or verified the assets required to make the deck's world repeatable.

Asset-ready normally requires:

- world/theme style or asset-class sheet;
- cast/character class sheet where useful;
- individual sheets for recurring major characters;
- environment class sheet where useful;
- location sheets for recurring major places or command domains;
- prop asset-class sheet tied to the world/theme;
- individual hero prop or continuity-object sheet where needed;
- interaction sheet when recurring handoffs, scale, or staged relationships matter;
- readiness report identifying provisional versus repo-tracked/canonical status.

Asset preproduction may use image generation, but it must not generate body-slide scene images. Body-slide image generation belongs inside the production playbook after deck and image planning.

Generated or edited preproduction images are only candidates until accepted by `adventures-image-qa` in the correct lane. Unreviewed, rejected, weak, or generated-only sheets do not count toward asset-ready.

For new Patch-bearing worlds, visual preproduction must normally begin with a Patch-in-world interaction or scale proof. This proof must show canonical Patch inhabiting the theme, interacting with the core hook and relevant non-Patch people, agents, systems, gates, or props. If that proof fails Patch canon, world fit, or interaction grammar, do not continue into the broader asset package.

### Playbook-ready

The issue is both frame-ready and asset-ready. The end-to-end PPTX production playbook may start.

Playbook-ready means production can begin from issue ingestion without deck planning or image planning having to invent the core story, teaching model, cast, locations, prop grammar, or reusable visual language.

## Framing family route

Use `adventures-project-readiness` as the umbrella router for the framing and
readiness family. A green readiness result means the frame is green, not merely
that a single theme sounds appealing.

Expected composition:

- `adventures-theme-buster` tests whether the world/theme is scene-generating, bounded, and non-decorative.
- `adventures-lesson-buster` tests the real-world autonomous-agent lesson, anti-pattern, positive pattern, and audience applicability.
- `adventures-story-buster` tests Patch's agency, stakes, continuity, and ordered story progression.
- `adventures-cast-domain-mapper` maps cast members to real-world functions.
- `adventures-environment-domain-mapper` maps environments and locations to real-world command or workflow domains.
- `adventures-prop-state-mapper` maps props, tools-as-props, continuity objects, and state transitions.
- `adventures-frame-greenlight` aggregates the family result and emits the visual preproduction order.

## Lesson sharpness tests

Do not mark an adventure green if the lesson collapses to generic advice such as:

- write better prompts;
- be clearer;
- add more context;
- communicate better;
- use AI carefully.

A green Adventures deck must teach a concrete, applicable autonomous-agent operating improvement for engineers, product people, QA people, team leads, or similar users.

The positive pattern should be something the audience can apply in real workflows, such as a decision rule, delegation architecture, checklist, source-truth discipline, review loop, control model, tool-use boundary, or evidence contract.

## Visual preproduction route

After frame-ready, run `playbooks/visual-preproduction.md` before the production playbook.

Visual preproduction consumes the frame-greenlight output and produces the asset package needed for consistent later body-slide image generation. `adventures-visual-preproduction` owns the local orchestration skill route.

Use `playbooks/image-qa-contract.md` as the canonical image QA contract. `adventures-image-qa` is the single authoritative image QA skill. Visual preproduction owns candidate planning and generation loops, but `adventures-image-qa` owns acceptance.

Only QA-accepted candidates may count as asset-ready references.

## Production playbook gate

The end-to-end PPTX production playbook should stop when an issue is not playbook-ready:

- If frame-ready is missing, remain in `adventures-project-readiness` and run
  its frame gate before routing onward.
- If frame-ready exists but asset-ready is missing, route to `playbooks/visual-preproduction.md`.
- If either state is absent, do not build a deck, generate body-slide images, or treat the issue as a completed proof run.

Preproduction compiled asset sheets are references for later generation. They must not be used as substitute body-slide art in proof/full/final-candidate runs unless Harley explicitly approves a separate storyboard mode.

## Standard readiness output

Use this compact readiness report when handing a matured issue to production:

```markdown
## Adventure readiness

- Issue:
- Seed state:
- Frame-ready: yes/no
- Asset-ready: yes/no
- Playbook-ready: yes/no

### Frame basis
- Theme/world:
- Real-world model:
- Anti-pattern:
- Positive pattern:
- Patch role:
- Cast/function map:
- Environment/domain map:
- Prop/state map:
- Continuity object/state transition:
- Concrete audience recommendations:

### Asset basis
- Existing reusable assets:
- New asset class sheets:
- Character sheets:
- Environment/location sheets:
- Prop/continuity sheets:
- Interaction/style/anti-pattern sheets:
- Image QA decisions and lanes:
- Provisional vs repo-tracked status:

### Production handoff
- Ready for end-to-end PPTX playbook: yes/no
- Blockers:
- Required next action:
```
