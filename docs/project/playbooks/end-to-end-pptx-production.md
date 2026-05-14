# End-to-end PPTX production playbook

This playbook is the canonical orchestration guide for turning an Adventures of Patch GitHub issue into a finished presentation package.

The playbook owns the process flow, required evidence, production gates, stop conditions, downgrade rules, artifact expectations, and failure reporting. It does not prescribe a fixed skill invocation script. The assistant is responsible for selecting appropriate currently available skills and tools to satisfy the work described here.

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

## Skill and tool selection

This playbook describes required work and gates, not a fixed skill invocation script.

At each stage, select appropriate currently installed skills and available tools based on the work being performed. A stage may require multiple skills, no skill, or a future skill not named in this document.

Do not treat any skill as exclusive for a stage. Repo/source discipline, artifact validity, Patch canon, visual intent, and QA obligations remain active whenever the work depends on them.

If installed skills are unavailable, stale, renamed, or superseded, follow the playbook's required evidence, outputs, and stop conditions using the best available tools. Do not skip a gate because a named skill is unavailable, and do not claim progress merely because any particular skill or tool was invoked.

## Hard preflight: repo access proof

Before any issue-to-PPTX production work may proceed beyond mandatory artifact-handoff preparation, prove live access to the canonical GitHub repo and fetch the named source issue.

Repo access is a state established by evidence, not by one preferred tool route. If a file, issue, comment, PR, commit, or repository metadata has already been retrieved from `HarleyBartles/adventures-of-patch` in the current run, repo access for that route is proven and must be carried forward. Do not later treat repo access as unavailable merely because a different GitHub search/index/tool route fails.

Required proof for `HarleyBartles/adventures-of-patch`:

1. Identify every currently available GitHub-capable route, including any route that has already successfully fetched repo material in the current run.
2. Prefer direct known-path and known-issue reads over broad search.
3. Prove repository identity with a successful repository metadata, file, or issue fetch from `HarleyBartles/adventures-of-patch`.
4. Fetch `INDEX.md` from `main`.
5. Fetch `AGENTS.md` from `main`.
6. Fetch `docs/project/INDEX.md` from `main`.
7. Fetch this playbook from `main` unless this file is already the active source being read from the repo.
8. Fetch the named issue and relevant issue comments when comments may contain decisions.

A broad search or index miss is not evidence that repo access is unavailable. A failure in one route is route-specific, not a global repo-access failure. If any direct repo read succeeds, do not claim repo access is unavailable. If a known-path read fails after repo access is proven, report the specific failed path and either use another available direct-read route or stop at that path gate.

If the source issue or required repo playbook surfaces cannot be fetched through any available GitHub-capable route, valid outputs are limited to a blocked status, a tooling/access diagnostic, or a user-approved plan-only fallback. Uploaded zips, receipt packages, previous decks, local scratch files, old assets, and memory must not be used as substitutes for the named issue or repo playbook in an end-to-end production run.

No PPTX, storyboard, draft, proof artifact, sidecar, receipt, or QA result may be presented as valid for a source issue when the repo gate was skipped.

## Default interpretation of end-to-end run requests

When the user asks to run an issue-to-PPTX proof, end-to-end pass, production pass, proof pass, rerun, or playbook run, interpret that as a staged playbook execution request.

Do not treat the request as an immediate image-generation request or immediate PPTX-build request, even when the final package will eventually need images and a PPTX.

Default behaviour:

1. Start at the playbook entry point.
2. Complete the hard repo access preflight and fetch the source issue.
3. Read repo navigation surfaces and the source issue.
4. Produce the issue brief.
5. Establish or verify the deck frame/analogy/world before deck planning. If the issue or comments do not already contain a strong frame, resolve the frame interactively with Harley and record the result on the issue before continuing.
6. Produce the deck plan, image plan, and Patch/image readiness assessment in order.
7. Invoke image generation only when the playbook reaches the image-generation stage, the image plan is complete, Patch references have been inspected through repo text plus available project-source Patch asset files, and no blocker exists.
8. If image generation is available, treat that as capability, not permission to jump ahead.
9. If image generation is unavailable at the image-generation stage, stop at the image gate and report the blocker.
10. If image generation is available and the image gate is satisfied, proceed without asking the user to restate the whole command, unless the image plan materially changed, the prompt set is uncertain, or a safety/tooling blocker appears.
11. After image generation, inspect outputs before using them in a PPTX.

Useful shorthand meanings:

- "Run the #3 proof pass" means run the whole staged playbook in order, including frame resolution when needed and image generation only at the correct stage.
- "Run the #3 proof pass but stop before image generation" means stop after image planning and Patch/image readiness.
- "Generate the images for #3" means run the image stage only, still requiring image plan, visual-intent gating, Patch preflight, and repo/project-source Patch references.

The user should not need to write a long gated instruction every time. The playbook is responsible for the default routing.

## Important trigger boundary

A user request for an end-to-end proof, production pass, or PPTX package may trigger artifact tooling because a PPTX is eventually required. That artifact trigger does not authorize skipping the playbook. After any mandatory artifact-handoff/tool preparation, return to this playbook and run the hard repo access preflight before any deck artifact is built or reported.

Artifact-handoff completion is not evidence of deck progress. Do not answer with a success link or completed-artifact claim unless every required playbook stage for the stated output mode has actually completed.

A user request for a deck with images may also look like an image-generation request. That does not authorize image generation before the image-generation stage. Treat image generation as one stage inside the playbook, not the whole task.

## Source and connector routing

Do not claim that a required tool or connector is unavailable until the relevant available routes have actually been inspected or tested.

For this project, source-of-truth repo work may use any live GitHub-capable route that can fetch canonical material from `HarleyBartles/adventures-of-patch`. Direct API-style reads are preferred for known repo paths, issues, comments, writes, and metadata when available, but they are not the only possible proof of access. GitHub search/index routes are useful for discovery, but a failure there does not erase successful direct repo access.

### GitHub repo and issue work

Use connector discovery before claiming GitHub is unavailable:

- Check currently available GitHub-capable routes when there is any doubt about GitHub availability.
- Preserve any already-successful repo read from another GitHub-capable route as proof of access for that route.
- Use direct-read routes for known paths and known issue numbers rather than broad search.
- Do not require a broad search/index route to succeed before using known repo paths or known issue numbers.

Required access proof before a repo-blocker claim:

1. Identify all currently available GitHub-capable routes and any route that already succeeded in this run.
2. Attempt a direct repo metadata, file, or issue read for `HarleyBartles/adventures-of-patch`.
3. If any direct read succeeds, do not claim repo access is unavailable.
4. If a specific file fetch fails, report the specific path failure, not generic connector absence.
5. If one GitHub route fails, try another available direct-read route before reporting a repo gate blocker.
6. If no GitHub-capable route can fetch repo metadata, known paths, or the named issue, report the actual tool results and stop at the repo gate.

Claims of tool sparsity, missing connector access, or unavailable repo access are red only after this multi-route discovery/test sequence has failed.

### Repo file reads

Use GitHub known-path fetches before broad search. Required repo reads for this playbook should normally be fetched from `HarleyBartles/adventures-of-patch` on `main`:

1. `INDEX.md`
2. `AGENTS.md`
3. `docs/project/INDEX.md`
4. `docs/project/playbooks/end-to-end-pptx-production.md`
5. Relevant directory `INDEX.md` files.
6. Relevant asset guides, deck docs, receipts, or issue-linked files.

Use repo search only when the path is unknown or the index mesh points to a file that cannot be found by direct fetch. Search/index failure must be reported as a search/index failure, not as repo unavailability.

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

If the issue or comments already contain a green frame, carry it into deck planning and cite the source. If the frame is missing, weak, corporate, or merely a UI metaphor, resolve the frame before deck planning. Frame resolution is complete when Harley and the assistant have agreed on a strong frame and the source issue records the frame, mapping, visual world, analogy boundaries, and deck-planning implications.

Do not mark deck planning green when the body slides are just Patch performing abstract engineering tasks or standing beside process diagrams.

### Patch visual references

For Patch visual work, inspect repo text references and image-capable visual references where available:

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

Use image generation only after:

- issue ingestion is complete;
- a strong frame is already present or frame resolution is complete;
- deck plan is complete;
- image plan is complete;
- visual intent has been established;
- Patch preflight has inspected repo Patch references and available project-source Patch asset files;
- prompt pack satisfies Patch style requirements, including v1.3 eye canon.

If image generation is not available at this stage, stop at the image gate and report that image generation is the blocker. Do not generate images before this stage merely because the final deliverable includes images.

### PPTX and artifact work

For slide/PPTX work, follow the currently available artifact workflow for creating or modifying a `.pptx`. Do not use PPTX tooling before accepted image status is explicit unless the user has explicitly approved storyboard or draft mode.

For PDF sidecars, follow the currently available document/PDF artifact workflow. Do not mark the package final if the sidecar is missing.

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

Required work:

- Fetch the issue from `HarleyBartles/adventures-of-patch` using a live GitHub-capable route.
- Fetch relevant issue comments if they may contain decisions.
- Extract issue source, issue type, core principle, target audience, narrative premise, slide beats, frame/analogy state, asset/image implications, risks, and acceptance criteria.
- Preserve gaps and uncertainty.

Gate 1: issue fetched and production brief created.

Stop if the issue cannot be fetched after multi-route GitHub connector discovery/testing, the issue is ambiguous and no safe default exists, or the issue lacks enough material to plan and the gap cannot be resolved without user input.

### Stage 2: Frame / analogy / world grounding

Required work:

- Determine whether the ingested issue already has a green frame.
- If the frame is missing, weak, merely corporate, or only a thin UI/process metaphor, resolve the frame interactively with Harley.
- Decide the deck's frame/analogy/world.
- Record the green frame, mapping, visual world, analogy boundaries, and implications for deck planning on the source issue.

Gate 2: strong frame is present and recorded.

Stop if no strong frame exists and Harley has not approved one. Do not proceed to green deck planning with an unframed issue unless Harley explicitly waives the frame requirement.

### Stage 3: Deck doctrine and deck plan

Required work:

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

Required work:

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

Required work:

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

Required work:

- Generate images according to the image plan.
- Inspect results before using them in a deck.
- Reject images that violate Patch canon or the deck's visual intent.

Gate 6: accepted image set exists.

Reject Patch images if Patch becomes glossy 3D, generic robot, plush, or photoreal; the bag is missing; the bag symbol is wrong; strap continuity fails; antennae are missing; hoodie is not teal; eyes have white sclera, visible irises, coloured pupils, or alternate eye style; proportions drift; in-world text is unreadable/misleading; or the image does not support the slide concept.

Stop if generated images fail canon and cannot be repaired in the current pass, generation repeatedly produces non-canonical style, or the user needs to choose between alternative directions.

Do not use rejected images in a final candidate deck.

### Stage 7: PPTX build

Required work:

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

Required work:

- Create a presenter sidecar, preferably PDF.
- Explain target audience, purpose, core principle, selected frame/analogy/world, narrative arc, themes, lessons, slide-by-slide guide, discussion prompts, practical application, assumptions, boundaries, and asset/receipt/canonisation notes.

Gate 8: sidecar exists for final candidate or finished package.

Stop before final status if sidecar is missing, sidecar is only a transcript rather than a presenter guide, or sidecar omits audience, lesson, selected frame, slide guide, or practical application.

### Stage 9: Presentation QA

Required work:

- Review issue alignment, frame strength, doctrine, Patch story, visual-first quality, image-led slide quality, text hierarchy, notes, sidecar, practical transfer, receipt/canonisation, and repo/source grounding.
- Use green/amber/red status.

Gate 9: QA report produced.

Final status rules:

- Green: package satisfies doctrine and issue acceptance criteria.
- Amber: usable draft/final candidate with known missing or weak pieces.
- Red: mandatory gate failed, frame is missing/weak for a non-waived deck, Patch canon failed, production phase skipped without approval, or significant redesign required.

Do not mark green because a deck merely looks polished.

### Stage 10: Receipt and canonisation follow-up

Required work:

- Create or plan a presentation image receipt for finished PPTX files using generated/embedded images.
- Identify reusable asset candidates.
- Open, perform, or recommend follow-up canonisation work for accepted reusable environments, props, characters, visual grammar, contact sheets, style guides, anti-patterns, interaction guides, or receipts.

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

### Follow-ups

<any suggested process, repo-doc, receipt, or canonisation follow-ups>
```

## Red conditions from previous proof failures

Past issue-to-PPTX proof failures on issue #3 should be treated as red because:

1. A run continued after image generation was unavailable/unbound instead of stopping at the image generation gate.
2. Later generated images did not follow canonical Patch style and drifted into glossy 3D mascot imagery.
3. Patch bag symbol and style constraints were violated.
4. Repo-grounded Patch reference inspection was not sufficiently enforced before generation.
5. Results were described too permissively as amber/storyboard rather than as failed proof work with invalid images.
6. A run claimed tool sparsity before discovering/testing live GitHub-capable repo access.
7. Unframed or weakly framed decks drifted into bland corporate process diagrams; future runs must establish a strong frame before green deck planning.
8. A later attempted production run treated search/index failure as repo unavailability and produced an artifact without fetching the source issue; future runs must stop at the hard repo preflight instead.
9. Any future run that has already retrieved repo material must preserve that successful route as access proof instead of narrowing to a different connector and declaring repo access lost.

Future passes must stop at the relevant gate and report the blocker rather than silently producing false-green or near-green artifacts.

## Repair policy

Prefer the smallest honest repair:

- If GitHub access appears unavailable, identify all GitHub-capable routes, preserve any route that already succeeded in the current run, and test direct repo metadata/file/issue reads before claiming a repo blocker.
- If source issue is weak, repair the issue or ask for clarification.
- If the issue lacks a strong frame, resolve the frame and record it before deck planning.
- If deck plan violates doctrine, repair the plan before image work.
- If image generation is unavailable at the image-generation stage, stop and report the image-generation blocker.
- If Patch references are missing or uninspected, stop and inspect repo/project-source references or land missing references.
- If images fail Patch canon, including v1.3 eye canon, reject/regenerate before PPTX build.
- If PPTX lacks notes or sidecar, keep it draft/amber or red depending on scope.
- If final package lacks receipt/canonisation status, do not mark finished.
