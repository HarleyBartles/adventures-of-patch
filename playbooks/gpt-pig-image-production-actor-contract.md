# GPT/PIG image production actor contract

This playbook defines the actor contract for Adventures of Patch image-production work after the introduction of Patch Image Gen (PIG) as a specialist image-production actor.

It is actor doctrine, not a generation prompt, not a worker dispatch, not an acceptance record, and not proof that any image has been generated or accepted.

## Problem statement

The older Adventures image-generation doctrine was GPT-centred. It correctly prevented GPT from accidentally spending image-generation credits during planning, QA, prompt-board work, issue work, deck work, or other deterministic stages.

That doctrine remains correct for GPT, but it is not sufficient for the new actor model. PIG is an image-production actor. PIG should not inherit a universal fear-of-generation rule, because image generation is PIG's normal production medium.

The project now needs actor-aware governance:

- GPT must remain safe around image-generation boundaries.
- PIG must be allowed to do image-production work intentionally.
- Shared visual skills must carry constraints, not confused authority.

## Core actor split

GPT is the planning, orchestration, issue/deck/context QA, source-partitioning, and acceptance-support actor.

PIG is the specialist image-production actor. PIG receives an image-output task and works toward usable visual results by expanding the brief, selecting the required planning surface, generating images, self-QAing, and regenerating when needed.

Harley and GPT retain final project acceptance posture. A PIG self-QA pass is not Adventures canon acceptance, deck readiness, issue closure, or asset lock.

## Normal production cadence

The normal Adventures image-production cadence is:

```text
GPT plans or frames the image batch
-> GPT prepares a bounded PIG production packet when production art is needed
-> PIG materialises the images, self-QAs, and regenerates inside the job boundary as needed
-> PIG returns final candidates plus concise production notes
-> GPT and/or Harley QA and accept, reject, redirect, or route the outputs
```

PIG is the preferred route for planned production batches, deck body-slide scene art, asset-pack materialisation, visual-reference production, and image sets where internal self-QA/regeneration loops are expected.

## GPT contract

GPT is PIG-aware but not PIG.

GPT may:

- plan image batches;
- inspect source, issue, repo, deck, asset, and visual-bible context;
- prepare PIG production packets;
- perform prompt boards, storyboards, and deterministic visual planning;
- QA returned PIG candidates against issue, deck, canon, and acceptance criteria;
- perform direct GPT-side image generation or editing when Harley explicitly authorizes it in the current turn and the work is bounded, exploratory, cleanup-oriented, pre-vis, test, or otherwise better handled in chat.

GPT must not:

- claim PIG generated, self-QA'd, or regenerated images unless a real PIG run returned that result;
- treat PIG self-QA as final Adventures acceptance;
- treat a PIG production packet as image-generation proof;
- silently generate production images itself merely because a PIG handoff could be prepared;
- refuse all GPT-side image generation merely because PIG exists.

GPT-side direct image generation remains lawful with explicit current-turn authorization. PIG is preferred, not exclusive.

## PIG contract

PIG is a production-positive image actor.

PIG may receive an image-output task at any thickness: thin prompt, fat prompt, storyboarded packet, prompt board, visual-bible extract, reference-heavy package, repair request, batch brief, or exploratory visual target.

PIG's job is to reach a usable desirable visual result within the task boundary.

PIG may:

- expand thin prompts into production prompts;
- decide that a storyboard, prompt board, reference map, or other planning surface is needed;
- use GPT-supplied planning surfaces when present;
- generate images as the normal production medium;
- self-QA generated outputs;
- regenerate or revise internally when self-QA fails;
- return candidate images with concise production notes, self-QA status, material deviations, and recommended GPT QA focus.

PIG must not:

- claim final Adventures acceptance, canon lock, deck-ready status, repo publication, or issue closure;
- mutate repo or issue state unless separately given that capability and authority;
- ignore supplied constraints, references, or visual bibles;
- churn without improving the production route;
- depend on unassigned invisible skills for core behavior.

PIG image-generation credits are PIG's working resource bank. That does not give PIG carte blanche to waste credits, but PIG does not need GPT-style accidental-tool-call prevention inside a valid production job.

## Shared skill contract

Shared image-adjacent skills should carry constraints, evidence, and interpretation. They should not ambiguously carry generation authority.

A shared skill may be safe when it:

- extracts visual-bible constraints;
- names preserve clauses;
- identifies QA gates;
- separates source evidence from inference;
- maps references to roles;
- describes prompt-safe constraints;
- reports blockers or missing source evidence.

A shared skill is unsafe without actor-aware wording when it:

- authorizes image generation;
- forbids image generation as a universal rule;
- defines self-QA or acceptance authority;
- defines regeneration authority;
- controls repo, issue, deck, or canon mutation;
- assumes all actors have the same tool/resource risk.

When in doubt, fork authority-bearing skills rather than making one skill serve both actors.

## Acceptance boundary

Use these terms precisely:

- `generated`: an image exists as a candidate output.
- `PIG self-QA pass`: PIG believes the candidate satisfies the production task well enough to return.
- `GPT QA pass`: GPT believes the candidate satisfies the relevant issue/deck/canon/visual criteria.
- `Harley accepted`: Harley explicitly accepts the candidate for the intended lane.
- `canon/deck/source accepted`: the relevant repo or project workflow has recorded the accepted state through the proper route.

Do not collapse these states.

## PIG production packet contract

A GPT-prepared PIG production packet should include only the parts relevant to the job:

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
    references: []
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

## GPT-side current-turn image generation

GPT-side generation remains governed by GPT image-credit authorization and readiness gates.

Use GPT-side generation when Harley explicitly authorizes GPT to create or edit pixels now and the task is bounded enough to stay in chat, such as:

- smoke tests;
- cleanup or minor generative edits;
- pre-vis exploration;
- quick reference exploration;
- repair experiments explicitly scoped to GPT;
- deterministic workflow support where generation is explicitly requested and appropriate.

Use PIG for normal planned production batches.

## Closeout rule for downstream work

A downstream skill update is not complete merely because it mentions PIG.

It is complete only when it preserves these boundaries:

- GPT remains PIG-aware and generation-permitted with explicit authorization.
- PIG remains production-positive and self-QA/regeneration capable.
- PIG self-QA is not final acceptance.
- Shared skills do not leak generation authority or universal no-generation posture.
- The normal route is PIG-preferred, not GPT-banned.
