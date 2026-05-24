# GPT to PIG image production handoff

This playbook defines the GPT-side handoff route for Adventures image-production work that should normally be materialised by Patch Image Gen (PIG).

It consumes `playbooks/gpt-pig-image-production-actor-contract.md` and does not replace the GPT-side image-generation resource discipline. GPT remains allowed to generate or edit images directly when Harley explicitly authorizes bounded GPT-side image work in the current turn.

## Purpose

GPT needs a repeatable way to decide when to keep work in planning mode, when to hand off image production to PIG, and when direct GPT-side image generation is lawful.

The handoff should prevent three failure modes:

- GPT over-generates production images because a plan or prompt is ready;
- GPT over-refuses lawful image work because PIG exists;
- GPT gives PIG vague or unbounded tasks that create unnecessary churn or acceptance confusion.

## Route decision

Classify the current visual request before selecting a route:

```yaml
gpt_visual_route:
  plan_only: false
  pig_handoff: false
  gpt_side_generation: false
  deterministic_pixel_work: false
  blocked_or_unclear: false
```

Use `plan_only` when the user asks for:

- visual strategy;
- prompt text;
- storyboard or prompt-board planning;
- deck/image planning;
- QA or critique;
- issue comments or doctrine;
- confidence estimates or next-step reasoning.

Use `pig_handoff` when the user asks GPT to prepare or route planned Adventures production image work, especially:

- planned batches;
- deck body-slide scene art;
- reusable asset-pack images;
- visual-reference materialisation;
- style/reference exploration where PIG self-QA and regeneration are expected;
- prompt sets intended to become actual images outside the current GPT response.

Use `gpt_side_generation` only when Harley explicitly authorizes GPT-side visible pixel mutation in the current turn and the work is bounded enough for chat-side generation or editing, such as:

- smoke tests;
- cleanup or minor generative edits;
- pre-vis exploration;
- quick reference exploration;
- repair experiments explicitly scoped to GPT;
- deterministic workflow support where generation is explicitly requested and appropriate.

Use `deterministic_pixel_work` when the request can be satisfied without image generation, such as:

- contact sheets;
- crops;
- annotations;
- asset-sheet compilation;
- template rendering;
- file packaging or receipts.

Use `blocked_or_unclear` when the route cannot be selected without missing authority, missing sources, or a real ambiguity that changes the actor or output.

## Normal handoff cadence

The normal handoff cadence is:

```text
GPT confirms image-production need
-> GPT gathers current issue/deck/frame/asset/style constraints
-> GPT prepares bounded PIG production packet
-> PIG materialises images and self-QAs/regenerates inside the job boundary
-> PIG returns candidates and concise notes
-> GPT/Harley QA, accept, reject, redirect, or route outputs
```

A handoff packet is not proof that PIG generated anything. A PIG self-QA pass is not final Adventures acceptance.

## Required handoff packet

Use the actor-contract playbook's packet shape. Include only relevant fields, but do not omit the boundaries.

```yaml
pig_production_packet:
  role: "Patch Image Gen (PIG)"
  task: "<image-output task>"
  context:
    adventure_or_issue: "<id or null>"
    deck_or_asset_context: "<summary or null>"
    audience_or_use: "<slide, asset pack, pre-vis, style reference, repair, etc.>"
  inputs:
    prompt_or_brief: "<thin or fat prompt>"
    references:
      - path_or_surface: "<reference>"
        role: "<style | geometry | character | prop | world | negative | support>"
    visual_bible_extracts: []
    storyboard_or_prompt_board: null
  output_requirements:
    image_count: "<number or bounded range>"
    aspect_ratio: "<ratio or task-defined>"
    separate_files: true
    combined_grid_allowed: false
  must_preserve: []
  must_avoid: []
  production_authority:
    may_expand_prompt: true
    may_create_internal_planning_surfaces: true
    may_generate_images: true
    may_self_qa: true
    may_regenerate_until_self_qa_pass_or_blocked: true
  return_contract:
    include_final_candidates: true
    include_concise_production_notes: true
    include_self_qa_status: true
    include_material_deviations_or_blockers: true
    include_recommended_gpt_qa_focus: true
  boundaries:
    final_acceptance_authority: "GPT/Harley/project workflow, not PIG"
    repo_or_issue_mutation: false
```

## Minimum packet requirements

A PIG handoff packet must always include:

- target task;
- intended use;
- output count or bounded range;
- aspect ratio or task-defined ratio;
- separate-vs-combined image requirement;
- must-preserve constraints;
- must-avoid constraints;
- production authority block;
- return contract;
- explicit final-acceptance boundary.

When available, include:

- issue number or deck context;
- frame/lesson/story state;
- visual bible extract;
- reference images or asset sheets with roles;
- storyboard or prompt board;
- QA focus areas;
- known failure modes.

Do not invent repo evidence or claim references were inspected if they were not.

## GPT-side direct generation boundary

PIG is preferred for normal production batches, but GPT is not banned from image generation.

If Harley explicitly asks GPT to generate or edit images now, apply GPT-side current-turn image authorization and the relevant image preflight/readiness workflow. Do not redirect to PIG merely because PIG exists when Harley intentionally scoped the work to GPT-side generation.

If a planned production batch is underway and Harley has not explicitly asked GPT to generate directly, prefer PIG handoff.

## Acceptance and reporting language

Use precise state labels:

- `handoff_prepared`: GPT prepared the packet.
- `pig_run_returned`: PIG returned generated candidates.
- `pig_self_qa_pass`: PIG marked returned candidates as production-usable.
- `gpt_qa_pass`: GPT judged candidates against issue/deck/canon criteria.
- `harley_accepted`: Harley explicitly accepted the outputs.
- `repo_accepted`: the correct repo/project workflow recorded the accepted state.

Do not say `done`, `accepted`, `deck-ready`, `asset-ready`, or `canon` merely because the PIG packet exists or PIG self-QA passed.

## When to update issues

Issue comments may record:

- that a PIG handoff packet was prepared;
- that a PIG run returned candidates;
- GPT QA results;
- Harley acceptance;
- blockers or required next action.

Do not post a PIG production packet to an issue as an executable instruction unless Harley explicitly asks to record it there. Handoffs are normally task packets, not durable issue comments.

## Closeout rule

A GPT-side handoff/routing update is complete when GPT has a durable route to:

- prefer PIG for normal production batches;
- still permit GPT-side generation with explicit current-turn authorization;
- prepare bounded PIG production packets;
- keep PIG self-QA separate from final acceptance;
- avoid claiming PIG execution before a real PIG run returns results.
