# Image generation resource discipline

This playbook is the Adventures of Patch doctrine for conserving image-generation credits and preventing accidental visual-production churn.

## Problem statement

Image generation credits are scarce production capacity. Deterministic workflows exist to reduce image-generation failures and conserve those credits. Calling image generation during deterministic work defeats the purpose of those workflows and can block visual preproduction, preprod-ready work, and deck production until credits refresh.

## Why this matters

Image generation is not a casual helper in this project. It is a limited production resource. If credits run out, visual preproduction stalls, visual-preprod-ready issues cannot advance, deck-ready issues that need art cannot proceed, and production can be blocked until credits refresh.

The deterministic workflow stack exists to avoid exactly that failure mode. Prompt boards, storyboard diagrams, locked reference sets, QA, deterministic crops and callouts, contact sheets, asset-sheet compilation, template packages, receipts, and package validation all reduce the chance of failed image calls. If GPT fires image generation during those deterministic stages, the project pays the workflow-prep cost and still wastes the credits the workflow was designed to protect.

This is not merely an authorization nicety. It is production-capacity stewardship.

## Operation classes

Before selecting any visual tool, classify the current task by operation class.

```yaml
operation_classes:
  deterministic_no_credit:
    - repo and issue inspection
    - asset request dispatches
    - visual preflight planning
    - prompt boards
    - storyboard diagrams
    - reference selection and locking
    - QA and repair planning
    - deterministic crops and annotations
    - contact-sheet rendering
    - asset-sheet compilation
    - template package creation
    - receipts and package validation
    - repo comments and issue updates
    - policy, doctrine, or skill discussion
  non_credit_pixel_work:
    - PIL layout
    - deterministic template compile
    - deterministic crop
    - deterministic callout or annotation board
    - deterministic contact sheet
    - deterministic package preview rendering
  credit_spending_mutation:
    - generate a new image candidate
    - regenerate a failed candidate
    - generatively edit an existing image
```

Only `credit_spending_mutation` may use image generation or a generative image-editing tool. Visual-adjacent work is not automatically image generation.

## Credit-spend rule

Image generation is allowed only when all of these are true:

```yaml
credit_spend_intent:
  current_turn_requests_new_or_changed_pixels: true
  requested_operation_class: credit_spending_mutation
  deterministic_route_insufficient: true
  deterministic_preparation_complete_or_explicitly_waived: true
  user_authorizes_spending_credit_now: true
  expected_to_advance_production_boundary: true
  max_calls: 1
```

If any field is false, unknown, inferred only from previous turns, or based only on workflow momentum, do not call image generation.

## Deterministic workflows are credit-conservation infrastructure

Treat deterministic tools as the default path when they can satisfy the request. In particular:

- QA is a reasoning decision, not mutation.
- A repair plan is not authority to spend another credit.
- A prompt board or storyboard is a deterministic artifact, not an image-generation call.
- A contact sheet is a deterministic inspection surface, not generated art.
- An asset-sheet compile places accepted source images into an approved template; it must not generate or restyle pixels.
- A repo comment, issue update, policy discussion, or skill update is text/repo work, not visual mutation.

Do not call image generation merely because the conversation includes images, generated candidates, prompts, style references, visual QA, or image-generation policy.

## Expected workflow cadence

For generation-bearing visual preproduction, the safe cadence is:

```text
inspect -> plan -> storyboard/prompt board -> ask/receive current-turn credit-spend authorization -> one image call -> stop -> QA -> accept or repair plan -> wait for next authorization
```

For deterministic asset-sheet work, the safe cadence is:

```text
accepted source images -> choose approved template -> deterministic compile -> inspect rendered sheet -> package -> report
```

The deterministic asset-sheet cadence does not include image generation.

## Anti-examples from observed failures

These requests must not spend image credits:

```text
What does QA say?
```

This is QA-only reasoning.

```text
Proceed with annotated callouts and a new iteration of the prompt board.
```

This is deterministic prompt-board work.

```text
Accepted. Proceed to compilation onto the template please.
```

This is deterministic asset-sheet compilation.

```text
How do I make that a durable rule?
```

This is policy/skill/repo planning.

```text
What is your plan to land it in the next image gen when you later regain authorisation?
```

This is repair planning for a future possible spend.

This request may spend one credit only after readiness checks:

```text
You are authorised for one image gen tool call to regenerate this image.
```

Even then, the call is limited to one and must use the locked prompt/reference/repair plan. If readiness is not established, stop with a blocker rather than spending the credit.

## False-green checks

Do not mark a workflow green if:

- it only added a permission phrase but did not explain credit scarcity;
- it treats deterministic visual work as image generation;
- it lets QA, prompt boards, repair plans, or accepted source images imply mutation authority;
- it has no operation-class classification before image tools;
- it relies on memory rather than repo, system-prompt, or skill surfaces;
- it requires Harley to restate every turn that image generation is scarce;
- it blocks legitimate generation when the workflow actually reaches the visual mutation stage.

## Relationship to skills

- `visual-intent-gate` should classify current-turn credit-spend intent.
- `adventures-image-preflight` should decide whether the requested spend is ready and justified.
- `adventures-storyboard-preflight` should produce deterministic diagrams/prompt boards that reduce later retries.
- `adventures-image-qa` should accept, reject, or plan repairs without spending another credit.
- `adventures-asset-sheet-compiler` should compile accepted images deterministically and never call image generation.
- `skill-validator` should reject visual skills that collapse deterministic/no-credit work into credit-spending mutation.

## Completion posture

Issue #55 owns the implementation of this doctrine across the system prompt, repo policy, skills, validator, and regression tests. The work is not green until the close-out posture on #55 can be answered yes with evidence.
