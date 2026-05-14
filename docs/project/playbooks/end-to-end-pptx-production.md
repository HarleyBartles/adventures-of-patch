# End-to-end PPTX production playbook

This playbook is the canonical orchestration guide for turning an Adventures of Patch GitHub issue into a finished presentation package.

Skills own local contracts. This playbook owns the cross-skill sequence, production gates, stop conditions, downgrade rules, tool-routing expectations, skill-invocation expectations, and failure reporting.

## Scope

Use this playbook when the user asks to take an adventure-plan issue, deck-plan issue, or related GitHub issue through to a delivered presentation package.

A finished package normally includes:

- PPTX deck;
- plain text-only title slide with month date;
- a strong frame/analogy/world that makes the issue's lesson physically happen through Patch's adventure;
- visual-first Patch-led body slides, preferably full-slide or near-full-slide images;
- speaker notes for every substantive body slide;
- plain text-only end card focused on takeaways and applying the learning today;
- presenter sidecar document, preferably PDF;
- presentation image receipt when generated or embedded images are used;
- follow-up asset canonisation issues where reusable assets emerge.

## Hard preflight: repo access proof

Before any issue-to-PPTX production work may proceed beyond mandatory artifact-handoff preparation, the assistant must prove live GitHub API access to the canonical repo and fetch the named source issue.

Required proof for `HarleyBartles/adventures-of-patch`:

1. Discover GitHub tools through `api_tool.list_resources`.
2. Call `get_repo` for `HarleyBartles/adventures-of-patch`.
3. Fetch `INDEX.md` from `main`.
4. Fetch `AGENTS.md` from `main`.
5. Fetch `docs/project/INDEX.md` from `main`.
6. Fetch `docs/project/playbooks/end-to-end-pptx-production.md` from `main` unless this file is already the active source being read.
7. Fetch the named issue with `fetch_issue`.

A broad search or index miss is not evidence that repo access is unavailable. If `get_repo` succeeds, the assistant must not claim repo access is unavailable. If a known-path read fails after repo access is proven, report the specific path failure and stop at that gate.

If the source issue or required repo playbook surfaces cannot be fetched, valid outputs are limited to a blocked status, a tooling/access diagnostic, or a user-approved plan-only fallback. Uploaded zips, receipt packages, previous decks, local scratch files, old assets, and memory must not be used as substitutes for the named issue or repo playbook in an end-to-end production run.

No PPTX, storyboard, draft, proof artifact, sidecar, receipt, or QA result may be presented as valid for a source issue when the repo gate was skipped.

## Default interpretation of end-to-end run requests

When the user asks to run an issue-to-PPTX proof, end-to-end pass, production pass, proof pass, rerun, or playbook run, interpret that as a staged playbook execution request.

Do not treat the request as an immediate image-generation request or immediate PPTX-build request, even when the final package will eventually need images and a PPTX.

Default behaviour:

1. Start at the playbook entry point.
2. Complete the hard repo access preflight and fetch the source issue.
3. Read repo navigation surfaces and the source issue.
4. Produce the issue brief.
5. Establish or verify the deck frame/analogy/world before deck planning. If the issue or comments do not already contain a strong frame, run `frame-buster` interactively with Harley and land the resulting planning comment on the issue before continuing.
6. Produce the deck plan, image plan, and Patch/image readiness assessment in order.
7. Invoke image generation only when the playbook reaches Stage 6, the image plan is complete, Patch references have been inspected through repo text plus available project-source Patch asset files, and no blocker exists.
8. If the image generation tool is available, treat that as capability, not permission to jump ahead.
9. If image generation is unavailable at Stage 6, stop at the image gate and report the blocker.
10. If image generation is available and the Stage 6 gate is satisfied, proceed without asking the user to restate the whole command, unless the image plan materially changed, the prompt set is uncertain, or a safety/tooling blocker appears.
11. After image generation, inspect outputs before using them in a PPTX.

Useful shorthand meanings:

- "Run the #3 proof pass" means run the whole staged playbook in order, including frame-buster when needed and image generation only at the correct stage.
- "Run the #3 proof pass but stop before image generation" means stop after image planning and Patch/image readiness.
- "Generate the images for #3" means run the image stage only, still requiring image plan, visual-intent gate, Patch preflight, and repo/project-source Patch references.

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
- Stage 2, frame/analogy/world grounding: `frame-buster` when the issue lacks a green frame or contains only a weak/provisional one.
- Stage 3, finished-deck contract: `adventures-of-patch-deck-doctrine`.
- Stage 3, deck planning: `adventures-of-patch-deck-planner`.
- Stage 4, image planning: `patch-deck-image-planner`.
- Stage 5, visual intent gate: `visual-intent-gate`.
- Stage 5, Patch preflight: `patch-image-preflight`.
- Stage 6, image generation: `image_gen` tool only after the Stage 6 gate is reached and Patch preflight has passed.
- Stage 6, image acceptance/rejection: `patch-image-preflight` post-generation review rules.
- Stage 7, PPTX build: `adventures-of-patch-pptx-builder`, composing with the installed `slides` artifact skill.
- Stage 8, presenter sidecar: installed document/PDF artifact skills as appropriate.
- Stage 9, presentation QA: `adventures-of-patch-presentation-qa`.
- Stage 10, image receipt: `presentation-image-receipt`.
- Stage 10, receipt package ingestion if needed: `receipt-zip-ingressor`.
- Stage 10, reusable asset canonisation if needed: `asset-sheet-canoniser`.

### Important trigger boundary

A user request for an end-to-end proof, production pass, or PPTX package may trigger artifact tooling because a PPTX is eventually required. That artifact trigger does not authorize skipping the playbook. After any mandatory artifact-handoff/tool preparation, return to this playbook and run the hard repo access preflight before any deck artifact is built or reported.

Artifact-handoff completion is not evidence of deck progress. Do not answer with a success link or completed-artifact claim unless every required playbook stage for the stated output mode has actually completed.

A user request for a deck with images may also look like an image-generation request. That does not authorize calling `image_gen` before Stage 6. Treat image generation as one stage inside the playbook, not the whole task.

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

### Frame / analogy / world grounding

Every Adventures of Patch deck needs a named frame/analogy/world unless Harley explicitly waives that requirement.

A green frame must:

- map cleanly to the issue's core principle;
- create physical stakes or a lived situation for Patch;
- give Patch an active role, not a mascot role;
- generate most body-slide scenes naturally;
- avoid importing misleading source-domain authority;
- identify where the analogy stops helping;
- provide visual language for environments, props, obstacles, success, failure, and handoff.

If the issue or comments already contain a green frame, carry it into deck planning and cite the source. If the frame is missing, weak, corporate, or merely a UI metaphor, run `frame-buster` before deck planning. `frame-buster` is green when Harley and the assistant decide on a strong frame and a planning comment has been landed on the source issue.

Do not mark deck planning green when the body slides are just Patch performing abstract engineering tasks or standing beside process diagrams.

### Patch visual references

For Patch visual work, use GitHub `fetch_file` for text references and image-capable inspection where available for visual references:

1. `assets/patch/INDEX.md`
2. `assets/patch/patch_style_guide_v1.3.md`
3. `assets/patch/patch_contact_sheet_v1.1.png`
4. `assets/patch/patch_anti_patterns_v1.1.png`
5. `assets/patch/patch_interaction_guide_v1.1.png`

ChatGPT project sources are also the expected home for an inspectable Patch asset package when this project provides one, especially `patch_assets.zip`. That project-source package may contain the same Patch visual surfaces in a form the assistant can inspect directly:

- `patch_style_guide_v1.3.md` or the latest project-source Patch style guide available;
- `patch_contact_sheet_v1.1.png`;
- `patch_anti_patterns_v1.1.png`;
- `patch_interaction_guide_v1.1.png`.

Use the project-source Patch asset package as the tool-accessible visual reference home for contact sheets, anti-pattern sheets, interaction guides, and style guides when GitHub confirms the repo paths but the connector cannot materialize PNGs for visual inspection. It is an inspectable mirror/input for Patch preflight, not a replacement for repo truth. If repo metadata/text and project-source files disagree, report the discrepancy and do not silently prefer either source.

If the tool cannot visually inspect PNG files from GitHub, report that exact limitation, then check whether the project-source Patch asset package is available and inspectable. Do not substitute arbitrary uploaded zips or memory. If neither GitHub visual inspection nor project-source Patch assets are available, use the written style guide as the minimum text basis and mark confidence or blocking status according to the requested output mode.

Patch prompts and image reviews must enforce v1.3 eye canon: black oval eyes with small white shine highlights only. Reject white sclera, visible irises, anime eyes, human eyes, doll eyes, coloured pupils, large expressive mascot eyes, or alternate creative eye styles.

### Slide image and text posture

Body slides should normally be full-slide or near-full-slide image-led scenes. The image should carry the emotional, narrative, and conceptual load.

Preferred visible text hierarchy:

1. No visible slide text beyond the image when the scene is self-explanatory with presenter notes.
2. Short in-world text embedded in the image when it helps the scene carry meaning: signs, stamps, mission cards, warning labels, dossiers, route markers, dashboards, receipts, or brief checklists.
3. Short PPTX overlay captions only when exact readable wording is required or generated in-world text is unreliable.

Avoid heavy explanatory text in images and avoid dense PPTX overlays. If a slide needs a paragraph to explain itself, repair the frame, image plan, or presenter notes instead of treating the slide as green.

### Image generation

Use the `image_gen` tool only at Stage 6, after:

- issue ingestion is complete;
- frame-buster is green or a strong frame is already present;
- deck plan is complete;
- image plan is complete;
- visual intent has been established;
- Patch preflight has inspected repo Patch references and available project-source Patch asset files;
- prompt pack satisfies Patch style requirements, including v1.3 eye canon.

If `image_gen` is not available at Stage 6, stop at the image gate and report that image generation is the blocker. Do not call `image_gen` before Stage 6 merely because the final deliverable includes images.

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
- Extract issue source, issue type, core principle, target audience, narrative premise, slide beats, frame/analogy state, asset/image implications, risks, and acceptance criteria.
- Preserve gaps and uncertainty.

Gate 1: issue fetched and production brief created.

Stop if the issue cannot be fetched after GitHub connector discovery/testing, the issue is ambiguous and no safe default exists, or the issue lacks enough material to plan and the gap cannot be resolved without user input.

### Stage 2: Frame / analogy / world grounding

Skill: `frame-buster` when needed.

Required actions:

- Determine whether the ingested issue already has a green frame.
- If the frame is missing, weak, merely corporate, or only a thin UI/process metaphor, run `frame-buster` interactively with Harley.
- Decide the deck's frame/analogy/world.
- Land a planning comment on the source issue describing the green frame, mapping, visual world, analogy boundaries, and implications for deck planning.

Gate 2: strong frame is present and recorded.

Stop if no strong frame exists and Harley has not approved one. Do not proceed to green deck planning with an unframed issue unless Harley explicitly waives the frame requirement.

### Stage 3: Deck doctrine and deck plan

Skills: `adventures-of-patch-deck-doctrine`, then `adventures-of-patch-deck-planner`

Required actions:

- Apply the finished-deck contract.
- Carry the green frame into the narrative arc and slide plan.
- Add a plain text-only title slide with month date.
- Add a plain text-only end card focused on takeaways and applying the learning today.
- Plan visual-first Patch-led body slides generated by the selected frame/world.
- Plan speaker-note intent for every substantive body slide.
- Plan presenter sidecar content.
- Identify asset and canonisation candidates.

Gate 3: deck plan satisfies doctrine before image planning.

Stop if the body lacks a Patch adventure spine, title/end requirements are missing, practical transfer is missing, the frame is missing/weak, the plan depends on dense slide text, or notes/sidecar obligations are absent.

### Stage 4: Image planning

Skill: `patch-deck-image-planner`

Required actions:

- Exclude title and end cards from image generation by default.
- Produce shot list for body slides from the selected frame/world.
- Prefer full-slide or near-full-slide image-led scenes.
- Plan short in-world image text where it helps the scene carry meaning.
- Reserve PPTX overlays for short fallback captions or exact-readable support only.
- Produce prompt pack, in-world text requirements, continuity constraints, generation order, and reusable asset candidates.
- Mark all new visual material provisional until accepted and canonicalised.

Gate 4: image plan maps to the deck plan and respects doctrine.

Stop if title/end cards receive image prompts without override, Patch is decorative rather than active, Patch continuity requirements are missing, prompt pack relies on uninspected Patch canon/reference assets, the image plan ignores the frame, or image/PPTX text is too dense.

### Stage 5: Visual intent and Patch preflight

Skills: `visual-intent-gate`, `patch-image-preflight`

Required actions:

- Confirm that image generation/editing is the current playbook stage, not the first action.
- Inspect repo Patch references and available project-source Patch asset files before generating Patch images.
- Incorporate Patch style guide, contact sheet, anti-pattern sheet, and interaction guide constraints into prompts when those project-source assets are available.

Patch prompt requirements:

- clean editorial vector style;
- thick rounded outlines;
- soft shading;
- teal hoodie;
- hoodie antennae;
- compact rounded proportions;
- black oval eyes with small white shine highlights only;
- expressive simple face without alternate eye anatomy;
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
- no `X` bag symbol unless explicitly documented as canonical change;
- no white sclera, irises, anime eyes, human eyes, doll eyes, coloured pupils, large expressive mascot eyes, or creative alternate eye styles.

Gate 5: image generation is available, playbook-authorized, and Patch preflight is complete.

Stop if image generation is not available at this stage, Patch references cannot be inspected sufficiently for the requested confidence level through either repo or project-source assets, or prompts cannot satisfy Patch identity constraints.

Do not build the PPTX after this gate fails unless the user explicitly accepts storyboard/draft downgrade.

### Stage 6: Image generation and image acceptance

Tool: `image_gen`, when available and when Stage 6 has been reached.

Required actions:

- Generate images according to the image plan.
- Inspect results before using them in a deck.
- Reject images that violate Patch canon or the deck's visual intent.

Gate 6: accepted image set exists.

Reject Patch images if Patch becomes glossy 3D, generic robot, plush, or photoreal; the bag is missing; the bag symbol is wrong; strap continuity fails; antennae are missing; hoodie is not teal; eyes have white sclera, visible irises, coloured pupils, or alternate eye style; proportions drift; in-world text is unreadable/misleading; or the image does not support the slide concept.

Stop if generated images fail canon and cannot be repaired in the current pass, generation repeatedly produces non-canonical style, or the user needs to choose between alternative directions.

Do not use rejected images in a final candidate deck.

### Stage 7: PPTX build

Skill: `adventures-of-patch-pptx-builder`, composing with the installed slides artifact workflow.

Required actions:

- Build only after image status is explicit.
- Use accepted images for visual-first body slides.
- Prefer full-slide or near-full-slide image-led layouts.
- Keep visible slide text sparse.
- Prefer short in-world image text where it carries the scene meaning.
- Use PPTX overlays only as short fallback captions or exact-readable support.
- Add presenter notes to every substantive body slide.
- Include plain title and end cards.
- Label the build mode accurately.

Gate 7: PPTX built in the correct mode.

Stop or downgrade only with explicit user approval if accepted images are missing, notes are absent, title/end cards violate doctrine, the deck requires dense visible text to work, or it falls back to corporate infographic/bullet layouts instead of image-led Patch scenes.

### Stage 8: Presenter sidecar

Artifact workflows: document/PDF tooling as appropriate.

Required actions:

- Create a presenter sidecar, preferably PDF.
- Explain target audience, purpose, core principle, selected frame/analogy/world, narrative arc, themes, lessons, slide-by-slide guide, discussion prompts, practical application, assumptions, boundaries, and asset/receipt/canonisation notes.

Gate 8: sidecar exists for final candidate or finished package.

Stop before final status if sidecar is missing, sidecar is only a transcript rather than a presenter guide, or sidecar omits audience, lesson, selected frame, slide guide, or practical application.

### Stage 9: Presentation QA

Skill: `adventures-of-patch-presentation-qa`

Required actions:

- Review issue alignment, frame strength, doctrine, Patch story, visual-first quality, image-led slide quality, text hierarchy, notes, sidecar, practical transfer, receipt/canonisation, and repo/source grounding.
- Use green/amber/red status.

Gate 9: QA report produced.

Final status rules:

- Green: package satisfies doctrine and issue acceptance criteria.
- Amber: usable draft/final candidate with known missing or weak pieces.
- Red: mandatory gate failed, frame is missing/weak for a non-waived deck, Patch canon failed, production phase skipped without approval, or significant redesign required.

Do not mark green because a deck merely looks polished.

### Stage 10: Receipt and canonisation follow-up

Skills: `presentation-image-receipt`, `receipt-zip-ingressor`, `asset-sheet-canoniser`, plus GitHub issue workflows.

Required actions:

- Create or plan a presentation image receipt for finished PPTX files using generated/embedded images.
- Identify reusable asset candidates.
- Open or recommend follow-up canonisation issues for accepted reusable environments, props, characters, visual grammar, contact sheets, style guides, anti-patterns, interaction guides, or receipts.

Gate 10: receipt/canonisation status recorded.

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
7. Subsequent proof attempts exposed that unframed or weakly framed decks drift into bland corporate process diagrams; future runs must establish a strong frame before green deck planning.
8. A later attempted production run treated search/index failure as repo unavailability and produced an artifact without fetching the source issue; future runs must stop at the hard repo preflight instead.

Future passes must stop at the relevant gate and report the blocker rather than silently producing false-green or near-green artifacts.

## Repair policy

Prefer the smallest honest repair:

- If GitHub access appears unavailable, discover `/GitHub` tools through `api_tool.list_resources` and test `get_repo` before claiming a repo blocker.
- If source issue is weak, repair the issue or ask for clarification.
- If the issue lacks a strong frame, run `frame-buster` and land the planning comment before deck planning.
- If deck plan violates doctrine, repair the plan before image work.
- If image generation is unavailable at Stage 6, stop and report the image-generation blocker.
- If Patch references are missing or uninspected, stop and inspect repo/project-source references or land missing references.
- If images fail Patch canon, including v1.3 eye canon, reject/regenerate before PPTX build.
- If PPTX lacks notes or sidecar, keep it draft/amber or red depending on scope.
- If final package lacks receipt/canonisation status, do not mark finished.
