# End-to-end PPTX production playbook

This playbook is the canonical orchestration guide for turning an Adventures of Patch GitHub issue into a finished presentation package.

Skills own local contracts. This playbook owns the cross-skill sequence, production gates, stop conditions, downgrade rules, tool-routing expectations, skill-invocation expectations, and failure reporting.

## Scope

Use this playbook when the user asks to take an adventure-plan issue, deck-plan issue, or related GitHub issue through to a delivered presentation package.

A finished package normally includes:

- PPTX deck;
- plain text-only title slide with month date;
- visual-first Patch-led body slides;
- speaker notes for every substantive body slide;
- plain text-only end card focused on takeaways and applying the learning today;
- presenter sidecar document, preferably PDF;
- presentation image receipt when generated or embedded images are used;
- follow-up asset canonisation issues where reusable assets emerge.

## Default interpretation of end-to-end run requests

When the user asks to run an issue-to-PPTX proof, end-to-end pass, production pass, proof pass, rerun, or playbook run, interpret that as a staged playbook execution request.

Do not treat the request as an immediate image-generation request or immediate PPTX-build request, even when the final package will eventually need images and a PPTX.

Default behaviour:

1. Start at the playbook entry point.
2. Read repo navigation surfaces and the source issue.
3. Produce the issue brief, deck plan, image plan, and Patch/image readiness assessment in order.
4. Invoke image generation only when the playbook reaches Stage 5, the image plan is complete, repo Patch references have been inspected, and no blocker exists.
5. If the image generation tool is available, treat that as capability, not permission to jump ahead.
6. If image generation is unavailable at Stage 5, stop at the image gate and report the blocker.
7. If image generation is available and the Stage 5 gate is satisfied, proceed without asking the user to restate the whole command, unless the image plan materially changed, the prompt set is uncertain, or a safety/tooling blocker appears.
8. After image generation, inspect outputs before using them in a PPTX.

Useful shorthand meanings:

- "Run the #3 proof pass" means run the whole staged playbook in order, including image generation only at the correct stage.
- "Run the #3 proof pass but stop before image generation" means stop after image planning and Patch/image readiness.
- "Generate the images for #3" means run the image stage only, still requiring image plan, visual-intent gate, Patch preflight, and repo Patch references.

The user should not need to write a long gated instruction every time. The playbook is responsible for the default routing.

## Required skill invocation map

When running this playbook, invoke or apply the following skills at the listed points. Do not rely on general reasoning alone when a skill is named here and available.

### Entry and repo grounding

- `presentation-planner-bootstrap`: use as the project-context/session binding read when the session has not already been bootstrapped.
- `github-issue-management`: apply for generic GitHub issue mechanics, duplicate checks, comments, updates, closure, and verification discipline.
- `adventures-of-patch-repo`: apply for local repo doctrine, index-mesh navigation, issue shapes, repo-first source discipline, and failure/downgrade reporting expectations.

These skills do not replace this playbook. They prepare the agent to use the playbook correctly.

### Stage skills

- Stage 1, issue ingestion: `adventures-of-patch-issue-ingestor`.
- Stage 2, finished-deck contract: `adventures-of-patch-deck-doctrine`.
- Stage 2, deck planning: `adventures-of-patch-deck-planner`.
- Stage 3, image planning: `patch-deck-image-planner`.
- Stage 4, visual intent gate: `visual-intent-gate`.
- Stage 4, Patch preflight: `patch-image-preflight`.
- Stage 5, image generation: `image_gen` tool only after the Stage 5 gate is reached and Patch preflight has passed.
- Stage 5, image acceptance/rejection: `patch-image-preflight` post-generation review rules.
- Stage 6, PPTX build: `adventures-of-patch-pptx-builder`, composing with the installed `slides` artifact skill.
- Stage 7, presenter sidecar: installed document/PDF artifact skills as appropriate.
- Stage 8, presentation QA: `adventures-of-patch-presentation-qa`.
- Stage 9, image receipt: `presentation-image-receipt`.
- Stage 9, receipt package ingestion if needed: `receipt-zip-ingressor`.
- Stage 9, reusable asset canonisation if needed: `asset-sheet-canoniser`.

### Important trigger boundary

A user request for an end-to-end proof, production pass, or PPTX package may trigger artifact tooling because a PPTX is eventually required. That artifact trigger does not authorize skipping the playbook. After any mandatory artifact-handoff/tool preparation, return to this playbook and run stages in order.

A user request for a deck with images may also look like an image-generation request. That does not authorize calling `image_gen` before Stage 5. Treat image generation as one stage inside the playbook, not the whole task.

## Tool routing and connector discovery

Do not claim that a required tool or connector is unavailable until the appropriate tool namespace has actually been inspected or tested.

For this project, the preferred source-of-truth tool for repo work is the live GitHub API connector exposed through `api_tool`.

### GitHub repo and issue work

Use `api_tool.list_resources` before claiming GitHub is unavailable:

- Call `api_tool.list_resources` with path `/GitHub`, `only_tools: true`, and `refetch_tools: true` when there is any doubt about GitHub availability.
- Then use the discovered `/GitHub/...` tool paths rather than guessing names.

Expected GitHub API tools include, when available:

- `get_repo` to prove repo access and permissions.
- `fetch_file` for known repo paths.
- `fetch_issue` for a known issue number.
- `fetch_issue_comments` when issue comments may contain decisions.
- `search` for repo file search only after known-path index reads have been attempted.
- `add_comment_to_issue` for production pass status comments.
- `create_issue`, `update_issue`, `create_file`, `update_file`, and related write tools when repo updates are part of the requested work.

Required access proof before a repo-blocker claim:

1. Discover GitHub tools with `api_tool.list_resources`.
2. Call `get_repo` for `HarleyBartles/adventures-of-patch`.
3. If `get_repo` succeeds, do not claim repo access is unavailable.
4. If a specific file fetch fails, report the specific path failure, not generic connector absence.
5. If GitHub tools are absent or `get_repo` fails, report the actual tool result and stop at the repo gate.

Claims of tool sparsity, missing connector access, or unavailable repo access are red only after this discovery/test sequence has failed.

### Repo file reads

Use GitHub known-path fetches before broad search. Required repo reads for this playbook should normally be fetched with `fetch_file` from `HarleyBartles/adventures-of-patch` on `main`:

1. `INDEX.md`
2. `AGENTS.md`
3. `docs/project/INDEX.md`
4. `docs/project/playbooks/end-to-end-pptx-production.md`
5. Relevant directory `INDEX.md` files.
6. Relevant asset guides, deck docs, receipts, or issue-linked files.

Use repo search only when the path is unknown or the index mesh points to a file that cannot be found by direct fetch.

### Patch visual references

For Patch visual work, use GitHub `fetch_file` for text references and image-capable inspection where available for visual references:

1. `assets/patch/INDEX.md`
2. `assets/patch/patch_style_guide_v1.2.md`
3. `assets/patch/patch_contact_sheet_v1.1.png`
4. `assets/patch/patch_anti_patterns_v1.1.png`
5. `assets/patch/patch_interaction_guide_v1.1.png`

If the tool cannot visually inspect PNG files from GitHub, report that exact limitation and use the written style guide as the minimum text basis. Do not substitute uploaded zips or memory unless the user explicitly scopes the task to them.

### Image generation

Use the `image_gen` tool only at Stage 5, after:

- issue ingestion is complete;
- deck plan is complete;
- image plan is complete;
- visual intent has been established;
- Patch preflight has inspected repo Patch references;
- prompt pack satisfies Patch style requirements.

If `image_gen` is not available at Stage 5, stop at the image gate and report that image generation is the blocker. Do not call `image_gen` before Stage 5 merely because the final deliverable includes images.

### PPTX and artifact work

For slide/PPTX work, follow the installed slides artifact instructions before creating or modifying a `.pptx`. Do not use PPTX tooling before accepted image status is explicit unless the user has explicitly approved storyboard or draft mode.

For PDF sidecars, follow the installed PDF/document artifact instructions. Do not mark the package final if the sidecar is missing.

## Output modes

Use explicit output-mode labels.

### Plan-only

No artifact generation. Produces briefs, plans, prompts, or QA recommendations.

### Storyboard

A prototype deck with placeholders or non-final visual treatment. Allowed only if the user requests storyboard/prototype mode or explicitly accepts a downgrade after a production gate is blocked.

### Draft

A deck with real structure and possibly real images, but known missing or weak pieces. Drafts are not final and must clearly list missing gates.

### Final candidate

All required artifacts exist and the package is ready for QA, but QA has not yet marked it green.

### Finished package

PPTX, notes, sidecar, image receipt status, and canonisation status are complete, and presentation QA is green or explicitly accepted by the user with known deviations.

Do not silently change modes. If a requested final-art or proof-run path becomes blocked, stop and ask whether to continue as storyboard/draft.

## Production sequence

### Stage 1: Issue ingestion

Skill: `adventures-of-patch-issue-ingestor`

Required actions:

- Fetch the issue from `HarleyBartles/adventures-of-patch` using the live GitHub API connector.
- Extract issue source, issue type, core principle, target audience, narrative premise, slide beats, asset/image implications, risks, and acceptance criteria.
- Preserve gaps and uncertainty.

Gate 1: issue fetched and production brief created.

Stop if the issue cannot be fetched after GitHub connector discovery/testing, the issue is ambiguous and no safe default exists, or the issue lacks enough material to plan and the gap cannot be resolved without user input.

### Stage 2: Deck doctrine and deck plan

Skills: `adventures-of-patch-deck-doctrine`, then `adventures-of-patch-deck-planner`

Required actions:

- Apply the finished-deck contract.
- Add a plain text-only title slide with month date.
- Add a plain text-only end card focused on takeaways and applying the learning today.
- Plan visual-first Patch-led body slides.
- Plan speaker-note intent for every substantive body slide.
- Plan presenter sidecar content.
- Identify asset and canonisation candidates.

Gate 2: deck plan satisfies doctrine before image planning.

Stop if the body lacks a Patch adventure spine, title/end requirements are missing, practical transfer is missing, the plan depends on dense slide text, or notes/sidecar obligations are absent.

### Stage 3: Image planning

Skill: `patch-deck-image-planner`

Required actions:

- Exclude title and end cards from image generation by default.
- Produce shot list for body slides.
- Produce prompt pack, in-world text requirements, continuity constraints, generation order, and reusable asset candidates.
- Mark all new visual material provisional until accepted and canonicalised.

Gate 3: image plan maps to the deck plan and respects doctrine.

Stop if title/end cards receive image prompts without override, Patch is decorative rather than active, Patch continuity requirements are missing, prompt pack relies on uninspected repo canon, or in-world text is too dense/purposeless.

### Stage 4: Visual intent and Patch preflight

Skills: `visual-intent-gate`, `patch-image-preflight`

Required actions:

- Confirm that image generation/editing is the current playbook stage, not the first action.
- Inspect repo Patch references before generating Patch images.
- Incorporate Patch style guide constraints into prompts.

Patch prompt requirements:

- clean editorial vector style;
- thick rounded outlines;
- soft shading;
- teal hoodie;
- hoodie antennae;
- compact rounded proportions;
- expressive simple face;
- dark pants;
- teal shoes with white soles;
- teal crossbody bag with visible `>` symbol;
- strap crossing torso from shoulder to opposite hip;
- bag-side continuity in sequences, comparisons, and panels.

Patch prompt negative constraints:

- no generic robot;
- no glossy 3D mascot;
- no plush realism;
- no photorealism;
- no unrelated asset-family style;
- no missing bag;
- no missing antennae;
- no changed hoodie colour;
- no `X` bag symbol unless explicitly documented as canonical change.

Gate 4: image generation is available, playbook-authorized, and Patch preflight is complete.

Stop if image generation is not available at this stage, repo Patch references cannot be inspected sufficiently for the requested confidence level, or prompts cannot satisfy Patch identity constraints.

Do not build the PPTX after this gate fails unless the user explicitly accepts storyboard/draft downgrade.

### Stage 5: Image generation and image acceptance

Tool: `image_gen`, when available and when Stage 5 has been reached.

Required actions:

- Generate images according to the image plan.
- Inspect results before using them in a deck.
- Reject images that violate Patch canon or the deck's visual intent.

Gate 5: accepted image set exists.

Reject Patch images if Patch becomes glossy 3D, generic robot, plush, or photoreal; the bag is missing; the bag symbol is wrong; strap continuity fails; antennae are missing; hoodie is not teal; proportions drift; in-world text is unreadable/misleading; or the image does not support the slide concept.

Stop if generated images fail canon and cannot be repaired in the current pass, generation repeatedly produces non-canonical style, or the user needs to choose between alternative directions.

Do not use rejected images in a final candidate deck.

### Stage 6: PPTX build

Skill: `adventures-of-patch-pptx-builder`, composing with the installed slides artifact workflow.

Required actions:

- Build only after image status is explicit.
- Use accepted images for visual-first body slides.
- Keep visible slide text sparse.
- Add presenter notes to every substantive body slide.
- Include plain title and end cards.
- Label the build mode accurately.

Gate 6: PPTX built in the correct mode.

Stop or downgrade only with explicit user approval if accepted images are missing, notes are absent, title/end cards violate doctrine, or the deck requires dense visible text to work.

### Stage 7: Presenter sidecar

Artifact workflows: document/PDF tooling as appropriate.

Required actions:

- Create a presenter sidecar, preferably PDF.
- Explain target audience, purpose, core principle, narrative arc, themes, lessons, slide-by-slide guide, discussion prompts, practical application, assumptions, boundaries, and asset/receipt/canonisation notes.

Gate 7: sidecar exists for final candidate or finished package.

Stop before final status if sidecar is missing, sidecar is only a transcript rather than a presenter guide, or sidecar omits audience, lesson, slide guide, or practical application.

### Stage 8: Presentation QA

Skill: `adventures-of-patch-presentation-qa`

Required actions:

- Review issue alignment, doctrine, Patch story, visual-first quality, notes, sidecar, practical transfer, receipt/canonisation, and repo/source grounding.
- Use green/amber/red status.

Gate 8: QA report produced.

Final status rules:

- Green: package satisfies doctrine and issue acceptance criteria.
- Amber: usable draft/final candidate with known missing or weak pieces.
- Red: mandatory gate failed, Patch canon failed, production phase skipped without approval, or significant redesign required.

Do not mark green because a deck merely looks polished.

### Stage 9: Receipt and canonisation follow-up

Skills: `presentation-image-receipt`, `receipt-zip-ingressor`, `asset-sheet-canoniser`, plus GitHub issue workflows.

Required actions:

- Create or plan a presentation image receipt for finished PPTX files using generated/embedded images.
- Identify reusable asset candidates.
- Open or recommend follow-up canonisation issues for accepted reusable environments, props, characters, visual grammar, contact sheets, style guides, anti-patterns, interaction guides, or receipts.

Gate 9: receipt/canonisation status recorded.

Stop before finished status if embedded/generated images are used and receipt status is unknown, or reusable assets emerged but no canonisation follow-up is recorded or explicitly deferred.

## Failure reporting

When a production pass fails or is downgraded, comment on the source issue unless the user asks not to.

Use this template:

```markdown
## Production pass status: Red | Amber | Green

### Stage reached

<stage name and number>

### Gate result

<which gate passed or failed>

### What was attempted

<short summary>

### Source evidence inspected

<repo files, issue, asset indexes, style guides, receipts, artifacts>

### Artifacts produced

<links or filenames, with validity status>

### Failure / downgrade reason

<clear explanation>

### Required next action

<smallest next repair or decision>

### Skill or repo-doc follow-ups

<any suggested updates>
```

## Red conditions from the first proof failure

The first issue-to-PPTX proof pass on issue #3 should be treated as red because:

1. The run continued after image generation was unavailable/unbound instead of stopping at the image generation gate.
2. The later generated images did not follow canonical Patch style and drifted into glossy 3D mascot imagery.
3. Patch bag symbol and style constraints were violated.
4. The run did not sufficiently enforce repo-grounded Patch reference inspection before generation.
5. The result was described too permissively as amber/storyboard rather than as a failed proof with invalid images.
6. The run claimed tool sparsity before discovering/testing the GitHub live API connector.

Future passes must stop at the relevant gate and report the blocker rather than silently producing false-green or near-green artifacts.

## Repair policy

Prefer the smallest honest repair:

- If GitHub access appears unavailable, discover `/GitHub` tools through `api_tool.list_resources` and test `get_repo` before claiming a repo blocker.
- If source issue is weak, repair the issue or ask for clarification.
- If deck plan violates doctrine, repair the plan before image work.
- If image generation is unavailable at Stage 5, stop and report the image-generation blocker.
- If Patch references are missing or uninspected, stop and inspect/land references.
- If images fail Patch canon, reject/regenerate before PPTX build.
- If PPTX lacks notes or sidecar, keep it draft/amber or red depending on scope.
- If final package lacks receipt/canonisation status, do not mark finished.
