# End-to-end PPTX production playbook

This playbook is the canonical orchestration guide for turning an Adventures of Patch GitHub issue into a finished presentation package.

Before any image-generation decision inside this playbook, read `playbooks/image-generation-resource-discipline.md`. The deterministic stages in this playbook are credit-conservation infrastructure, not automatic spend triggers.

It owns process flow, required evidence, production gates, stop conditions, downgrade rules, artifact expectations, and failure reporting. It does not prescribe a fixed skill invocation script. At each stage, select currently available skills and tools that satisfy the required evidence and gates.

## Scope

Use this playbook when the user asks to take an adventure-plan issue, deck-plan issue, or related GitHub issue through to a delivered presentation package.

A finished package normally includes:

- PPTX deck;
- plain text-only title slide with month date;
- strong frame/analogy/world that makes the lesson physically happen through Patch's adventure;
- visual-first Patch-led body slides, preferably full-slide or near-full-slide accepted generated scene images;
- speaker notes for every substantive body slide;
- plain text-only end card focused on takeaways and applying the learning today;
- presenter sidecar document, preferably PDF;
- presentation image receipt when generated or embedded images are used;
- follow-up asset canonisation issues where reusable assets emerge.

## Proof-run semantics

A proof run is a full live run of this end-to-end production playbook.

"Proof" describes the purpose of the run: proving whether the playbook, skills, tools, assets, and artifact pipeline can complete correctly from source issue to package. It does not describe a weaker output mode.

A proof run must execute the same required stages as a full production run:

1. repo access proof;
2. issue ingestion;
3. frame verification or frame-buster resolution;
4. deck planning;
5. image planning;
6. visual intent gate;
7. Patch image preflight where Patch appears;
8. image generation;
9. post-generation Patch image QA and accepted/rejected image inventory;
10. PPTX build from accepted generated scene images;
11. presenter sidecar;
12. presentation QA;
13. receipt and canonisation follow-up.

If a proof run fails at any mandatory gate, the proof result is Red or Amber with exact evidence. The assistant must stop at the failed gate unless this playbook explicitly allows continuation and Harley explicitly approves the mode change.

A proof run must not be downgraded to storyboard, draft, placeholder, asset-sheet deck, or plan-only mode merely because a gate is difficult, unavailable, or inconvenient. Storyboard and draft modes are separate requested modes, not implicit proof-run fallbacks.

## Skill and tool selection

Use appropriate currently installed skills and available tools at each stage. A stage may require multiple skills, no skill, or a future skill not named here.

Do not skip a gate because a named skill is unavailable. If a skill is unavailable, stale, renamed, or superseded, still satisfy the playbook's required evidence, outputs, and stop conditions with the best available route.

Expected compositions include:

- `adventures-bootstrap` at fresh project start when available;
- `adventures-repo` and `github-issue-management` for repo and issue discipline;
- `adventures-issue-ingestor` for issue briefs;
- `adventures-frame-buster` when the frame is missing or weak;
- `adventures-deck-doctrine` and `adventures-deck-planner` for deck planning;
- `adventures-deck-image-planner` for shot lists, prompt packs, and the image inventory skeleton;
- `visual-intent-gate` before generation/editing;
- `adventures-patch-image-preflight` before generating Patch images;
- `adventures-patch-image-qa` after generation and before slides;
- `adventures-pptx-builder` for PPTX assembly;
- `adventures-presentation-qa` for package/stage QA;
- `adventures-receipt-gen` for embedded-image receipt packages.

### Required discovery before unavailability claims

Before claiming that a required skill, artifact route, image route, repo connector, or source package is unavailable, record the discovery attempt in the run-state ledger.

For external app connectors, refresh the named connector namespace at the action boundary before selecting actions or reporting availability. Treat earlier sparse connector listings as provisional until that refresh happens.

For skills:

- attempt skill catalogue lookup for each required Adventures skill;
- read `SKILL.md` for visible skills;
- record exact absence or read failure if a skill is missing.

For GitHub/repo:

- identify all currently available GitHub-capable routes;
- prefer direct known-path and known-issue reads over search;
- preserve any successful route as proof of repo access for the current run.

For image generation:

- image generation availability must be established by the actual image-generation route at the image stage, not by inference, tool sparsity language, artifact-tool behaviour, or prior failures in unrelated tools;
- valid image-stage outcomes are: image generation invoked and outputs produced; image generation invoked and failed with the exact tool failure recorded; or no image-generation route visible after actual tool discovery, with the discovery result recorded.

Do not use phrases such as "tool sparsity", "unavailable", "not visible", or "unbound" unless the actual discovery or tool call supports that statement.

## Hard preflight: repo access proof

Before any issue-to-PPTX production work may proceed beyond mandatory artifact-handoff preparation, prove live access to the canonical GitHub repo and fetch the named source issue.

Repo access is a state established by evidence, not by one preferred tool route. A successful file, issue, comment, PR, commit, or repository metadata fetch from `HarleyBartles/adventures-of-patch` proves repo access for that route and must be carried forward. A later failure in another route is route-specific and does not erase proof.

Required proof:

1. Identify currently available GitHub-capable routes, including any route already successful in the current run.
2. Prefer direct known-path and known-issue reads over broad search.
3. Fetch or otherwise prove repository identity for `HarleyBartles/adventures-of-patch`.
4. Fetch `INDEX.md` from `main`.
5. Fetch `AGENTS.md` from `main`.
6. Fetch `docs/project/INDEX.md` from `main`.
7. Fetch `assets/INDEX.md` and `assets/source-zips/INDEX.md` when project-source or zipped asset inspection may be needed.
8. Fetch this playbook from `main` unless this file is already the active source being read from the repo.
9. Fetch the named issue and relevant issue comments when comments may contain decisions.

A broad search or index miss is not repo unavailability. If the source issue or required playbook cannot be fetched through any available GitHub-capable route, valid outputs are limited to a blocked status, tooling/access diagnostic, or user-approved plan-only fallback.

No PPTX, storyboard, draft, proof artifact, sidecar, receipt, or QA result may be presented as valid for a source issue when the repo gate was skipped.

## Run-state ledger and mode-switch continuity

Every playbook run must maintain an explicit run-state ledger. The ledger prevents mode switches from resetting source truth or silently changing run mode.

Create the ledger immediately after hard preflight and carry it forward through chat reasoning, artifact handoff, image generation, local file/container work, zip inspection, PPTX building, sidecar creation, QA, and receipt work.

Minimum ledger fields:

- `repo_access`: green, red, or blocked;
- `proven_repo_route`;
- `repo_identity`;
- `fetched_repo_surfaces`;
- `source_issue`;
- `current_stage`;
- `frame_state`;
- `artifact_mode`;
- `proof_run`: yes/no, with proof meaning full live run;
- `downgrade_approval`: none, or Harley approval quote/comment ID plus approved mode;
- `local_sources_allowed`: repo-indexed package names and limited purpose;
- `image_generation_route`: available, unavailable, failed, or not yet tested, with evidence;
- `image_qa_route`: available, unavailable, failed, or not yet tested, with evidence;
- `accepted_scene_image_inventory`: missing, partial, complete, or not applicable;
- `blocked_or_open_items`.

Before any mode switch, re-check the ledger. If the ledger is lost or contradicted, stop and reconstruct it from repo evidence before continuing. Do not fall back to uploaded zips, receipts, memory, old assets, or substitute visuals while the ledger is missing.

Project-source zips may be used only after the ledger records repo proof, the current repo-tracked source package name from `assets/source-zips/INDEX.md`, and the specific non-visual reason for local inspection. Identify the current zip package in the repo index only when package, import, or integrity work actually needs it; do not treat the matching zip as the default visual truth for repo-canonical images.

Patch visual source packages are never a substitute for issue, playbook, deck, image generation, image QA, or repo truth. They are inspection mirrors for package/integrity fallback only when repo text and paths are already confirmed and the repo-indexed contact-sheet route is blocked or explicitly unavailable.

A production artifact is invalid if the ledger is absent, contradicts claimed status, loses repo-green state during a mode switch, or shows a proof/full run without the accepted scene-image inventory required for PPTX build.

## Default interpretation of run requests

When the user asks to run an issue-to-PPTX proof, end-to-end pass, production pass, proof pass, rerun, or playbook run, interpret that as staged playbook execution.

Do not treat the request as immediate image generation or immediate PPTX build, even when the final package will need images and a PPTX.

Default behaviour:

1. Start at the playbook entry point.
2. Complete hard repo access preflight and fetch the source issue.
3. Create the run-state ledger.
4. Read repo navigation surfaces and source issue.
5. Produce the issue brief.
6. Establish or verify the deck frame/analogy/world before deck planning. If no green frame exists, resolve the frame interactively with Harley and record the result on the issue.
7. Produce deck plan, image plan, and Patch/image readiness assessment in order.
8. Invoke image generation only at the image-generation stage when the image plan is complete, Patch references have been inspected through repo text plus any required repo-indexed contact-sheet intake package, and no blocker exists.
9. Run post-generation image QA on outputs. Weak/non-compliant images go back for edit or full regeneration.
10. Repeat the image generation -> image QA loop until every body-slide image is accepted, or stop Red/blocked.
11. Build PPTX only after the accepted generated scene-image inventory is complete for every body slide.
12. Create sidecar, QA report, receipt, and canonisation status.

Useful shorthand meanings:

- "Run the #3 proof pass" means run the whole staged playbook in order as a full live run, including image generation, image QA, PPTX build, sidecar, QA, and receipt/canonisation status.
- "Run the #3 proof pass but stop before image generation" means stop after image planning and Patch/image readiness; this is not a completed proof run.
- "Generate the images for #3" means run the image stage only, still requiring image plan, visual-intent gating, Patch preflight, generation, and Patch image QA.

## Important trigger boundary

A user request for a PPTX package may trigger artifact tooling because a PPTX is eventually required. Artifact preparation does not authorize skipping the playbook. After any mandatory artifact handoff/tool preparation, return to this playbook and continue from the ledger.

A user request for a deck with images may look like an image-generation request. That does not authorize generation before the image-generation stage. Treat image generation as one stage inside the playbook.

## Downgrade approval rule

A proof/full/final-art run may downgrade to storyboard or draft only when all are true:

- the blocking gate is reported before the downgrade;
- Harley explicitly approves the downgrade in the current conversation or through a cited issue comment;
- the ledger records the approval quote or comment ID;
- every output and issue comment labels the artifact with the downgraded mode;
- the artifact is not described as a completed proof/full run.

Absent this approval, continuing after a failed mandatory gate is Red, not Amber.

A failed proof can produce notes, diagnostics, and scratch artifacts, but those scratch artifacts are not the proof output and must not be dressed up as one.

## Image evidence and QA contract

For proof, full, final-candidate, or finished-package runs, body-slide visual requirements are satisfied only by a complete accepted generated scene-image inventory produced after post-generation QA.

The image stage is a mandatory loop:

```text
generate image -> run Patch image QA -> accept / edit_required / regenerate_required / blocked -> repeat until every body-slide image is accepted -> only then enter PPTX build
```

The loop runs as many times as needed. A weak or non-compliant image is edited, regenerated, or reported as blocked. It does not enter slides.

An accepted generated scene-image inventory must list, for each body slide:

- slide number and deck-plan beat;
- generated image file/path or generation ID;
- generation prompt or prompt reference;
- source/reference assets used as guidance;
- whether Patch appears;
- Patch preflight basis when Patch appears;
- post-generation QA decision: `accepted`, `edit_required`, `regenerate_required`, or `blocked`;
- rejection/repair reason when not accepted;
- next action;
- whether the image is final, draft, or storyboard.

Only rows marked `accepted` can unlock PPTX build for proof/full/final runs.

Reference assets, source zips, asset-class sheets, contact sheets, style sheets, anti-pattern sheets, interaction sheets, location sheets, package thumbnails, and old deck images are not accepted generated scene images. They may be used only as generation references unless Harley explicitly approves storyboard mode.

A successful image-generation call proves tool availability only. It does not prove Patch image acceptance. Every generated Patch image must still pass post-generation QA.

## Source and local material routing

Do not begin an issue-to-PPTX run from uploaded zips, local scratch files, or prior generated artifacts.

Allowed local/project-source uses after repo proof:

- inspecting the current repo-indexed Patch source package to view Patch PNG references after repo paths and style-guide truth are confirmed;
- inspecting repo-indexed environment, character, style, or receipt packages as generation references;
- reading an artifact just produced in the current run for QA or receipt generation.

Disallowed uses:

- using source zips, receipt zips, old decks, memory, or source-package contents as a replacement for issue #3, issue comments, playbook, deck plan, image plan, image generation, image QA, or generated scene images;
- treating local unzip work as evidence that repo access is unavailable;
- continuing artifact production after the ledger is lost or contradicted;
- using asset sheets, contact sheets, style sheets, anti-pattern sheets, location sheets, or package thumbnails as body-slide art in a proof/full/final run unless Harley explicitly approves separate storyboard mode.

## Frame / analogy / world grounding

Every Adventures of Patch deck needs a named frame/analogy/world unless Harley explicitly waives that requirement.

A green frame must:

- map cleanly to the issue's core principle;
- create physical stakes or a lived situation for Patch;
- give Patch an active role, not a mascot role;
- generate body-slide scenes naturally;
- avoid importing misleading source-domain authority;
- identify where the analogy stops helping;
- provide visual language for environments, props, obstacles, success, failure, and handoff.

If the issue or comments already contain a green frame, carry it into deck planning and cite the source. If the frame is missing, weak, corporate, or merely a UI/process metaphor, resolve it before deck planning and record the result on the issue.

Do not mark deck planning green when the body slides are Patch beside abstract diagrams or corporate process panels.

## Patch visual references

For Patch visual work, inspect repo text references and image-capable visual references where available:

1. `assets/canon/patch/INDEX.md`;
2. repo-indexed Patch style guide;
3. repo-indexed Patch contact sheet;
4. repo-indexed Patch anti-pattern sheet;
5. repo-indexed Patch interaction guide;
6. repo-indexed contact-sheet dispatch/intake packages built from current Patch references when rendered visual inspection is needed.
7. `assets/source-zips/INDEX.md` only when package, import, or integrity fallback inspection is explicitly needed.

Use the project-source Patch package only as a package or integrity aid when the ledger records that GitHub confirmed the repo paths but the repo-indexed contact-sheet route is blocked. If repo metadata/text and project-source files disagree, report the discrepancy and do not silently prefer either source.

Patch prompts and image QA must enforce current repo-indexed eye canon unless superseded by a newer repo-indexed style guide: black oval eyes with small white shine highlights only. Reject white sclera, visible irises, anime eyes, human eyes, doll eyes, coloured pupils, large expressive mascot eyes, or alternate eye styles.

## Slide image and text posture

Body slides should normally be full-slide or near-full-slide image-led scenes. The image should carry the emotional, narrative, and conceptual load.

Preferred visible text hierarchy:

1. no visible slide text beyond the image when the scene is self-explanatory with presenter notes;
2. short in-world text embedded in the image when it helps the scene carry meaning;
3. short PPTX overlay captions only when exact readable wording is required or generated in-world text is unreliable.

Avoid heavy explanatory text in images and dense PPTX overlays. If a slide needs a paragraph to explain itself, repair the frame, image plan, generated image, or presenter notes instead of treating the slide as green.

## Image generation and QA gates

Use image generation only after:

- issue ingestion is complete;
- a strong frame is already present or frame resolution is complete;
- deck plan is complete;
- image plan is complete;
- visual intent has been established;
- Patch preflight has inspected repo Patch references and any required repo-indexed contact-sheet intake package;
- prompt pack satisfies Patch style requirements, including current repo-indexed eye canon.
- the current turn satisfies `playbooks/image-generation-resource-discipline.md`, including the credit-spend justification object.

At the image-generation stage, invoke the image-generation route, report exact route failure, or record exact route absence after discovery. Do not infer unavailability.

After generation, run `adventures-patch-image-qa` or equivalent post-generation QA. Reject, edit, or regenerate any image that fails Patch identity, scene fit, frame fit, slide mapping, or text posture.

Reject Patch images if Patch becomes a dog, animal, glossy 3D, generic robot, plush, or photoreal; the bag is missing; the bag symbol is wrong; strap continuity fails; antennae are missing; hoodie is not teal; eyes have white sclera, visible irises, coloured pupils, or alternate eye style; proportions drift; Patch is multiplied; supporting agents become Patch clones; in-world text is unreadable/misleading; or the image does not support the slide concept.

Stop Red/blocked if generated images fail canon and cannot be repaired, generation repeatedly produces non-canonical style, image generation is not actually invoked, or Harley must choose between alternative directions.

Do not use rejected, weak, unreviewed, or reference/source images in a proof/full/final-candidate deck.

## PPTX and artifact work

For slide/PPTX work, follow the currently available artifact workflow for creating or modifying a `.pptx`.

For proof/full/final-candidate/finished runs, PPTX build is not permitted until the accepted generated scene-image inventory exists for every body slide.

Do not use PPTX tooling before accepted generated scene-image status is explicit unless Harley has explicitly approved a separate storyboard or draft mode.

For PDF sidecars, follow the currently available document/PDF artifact workflow. Do not mark the package final if the sidecar is missing.

## Output modes

Use explicit output-mode labels.

### Plan-only

No artifact generation. Produces briefs, plans, prompts, or QA recommendations.

### Storyboard

A prototype deck with placeholders or non-final visual treatment. Allowed only if the user requests storyboard/prototype mode or explicitly accepts a downgrade after a production gate is blocked. Storyboard is not proof-run completion.

### Draft

A deck with real structure and possibly real images, but known missing or weak pieces. Draft is not proof-run completion unless draft was the requested mode from the start.

### Final candidate

All required artifacts exist and the package is ready for QA, but QA has not yet marked it green.

### Finished package

PPTX, notes, sidecar, image receipt status, canonisation status, and QA are complete or explicitly accepted with known deviations.

Do not silently change modes. If a requested proof/full/final-art path becomes blocked, stop and report the failed gate. Continue as storyboard/draft only after explicit Harley approval.

## Production sequence

### Stage 1: Issue ingestion

Required work:

- fetch the issue and relevant comments from `HarleyBartles/adventures-of-patch`;
- extract issue source/type, core principle, target audience, narrative premise, slide beats, frame state, asset/image implications, risks, and acceptance criteria;
- preserve gaps and uncertainty;
- update the ledger.

Gate 1: issue fetched and production brief created.

Stop if the issue cannot be fetched, is ambiguous with no safe default, or lacks enough material to plan without user input.

### Stage 2: Frame / analogy / world grounding

Required work:

- determine whether the issue/comments already contain a green frame;
- resolve missing/weak frames interactively with Harley;
- record the green frame, mapping, visual world, analogy boundaries, and planning implications on the source issue;
- update the ledger.

Gate 2: strong frame is present and recorded.

Stop if no strong frame exists and Harley has not approved or waived one.

### Stage 3: Deck doctrine and deck plan

Required work:

- apply finished-deck contract;
- carry the green frame into the narrative arc and slide plan;
- include plain text-only title slide with month date;
- include plain text-only end card focused on practical application;
- plan visual-first Patch-led body slides;
- plan speaker-note intent for every substantive body slide;
- plan presenter sidecar content;
- identify asset/canonisation candidates;
- update the ledger.

Gate 3: deck plan satisfies doctrine before image planning.

Stop if the body lacks a Patch adventure spine, title/end requirements, practical transfer, strong frame, notes/sidecar obligations, or relies on dense slide text.

### Stage 4: Image planning

Required work:

- exclude title and end cards from image generation by default;
- produce body-slide shot list from the selected frame/world;
- plan full-slide or near-full-slide scenes;
- plan short in-world text where useful;
- produce prompt pack, continuity constraints, generation order, reusable asset candidates, and slide-by-slide image inventory skeleton;
- update the ledger.

The image inventory skeleton must include:

| Slide | Required scene image | Reference assets | Patch present? | Generation status | QA status |
|---|---|---|---|---|---|

Gate 4: image plan maps to the deck plan and respects doctrine.

Stop if title/end cards receive prompts without override, Patch is decorative, Patch continuity is missing, prompt pack relies on uninspected references, the frame is ignored, image/PPTX text is too dense, or the inventory skeleton is missing.

### Stage 5: Visual intent and Patch preflight

Required work:

- confirm image generation/editing is the current playbook stage;
- re-check ledger before local zip extraction or image tool use;
- inspect repo Patch references and the repo-indexed contact-sheet intake package when needed;
- incorporate style guide, contact sheet, anti-pattern sheet, and interaction guide into prompts when available;
- record image-generation route status.

Gate 5: generation is playbook-authorized and Patch preflight is complete.

Stop if image generation is unavailable, Patch references cannot be inspected sufficiently, prompts cannot satisfy Patch identity, or availability has been inferred rather than tested/discovered.

### Stage 6: Image generation

Required work:

- re-check ledger;
- invoke image-generation route or record exact failure/absence;
- generate images according to the image plan;
- record generated image IDs/paths and prompts;
- update the inventory generation status.

Gate 6: generated image candidates exist for required body slides, or exact generation failure is recorded.

Stop if image generation is not actually invoked, fails without recoverable route, or generation repeatedly cannot produce usable candidates.

### Stage 7: Post-generation Patch image QA and repair loop

Required work:

- run `adventures-patch-image-qa` or equivalent post-generation QA on every generated body-slide image before PPTX build;
- decide per image: `accepted`, `edit_required`, `regenerate_required`, or `blocked`;
- send weak/non-compliant images back for edit or full regeneration;
- repeat generation -> image QA until every required body-slide image is accepted, or stop blocked/Red;
- complete the accepted generated scene-image inventory;
- update the ledger.

Gate 7: complete accepted generated scene-image inventory exists for every body slide.

Stop if any image is pending, weak, rejected, unreviewed, source/reference-only, or blocked.

### Stage 8: PPTX build

Required work:

- re-check ledger;
- build only after accepted generated scene-image inventory is complete, unless Harley explicitly approved separate storyboard/draft mode;
- use accepted generated scene images for visual-first body slides;
- prefer full-slide or near-full-slide layouts;
- keep visible slide text sparse;
- add presenter notes to every substantive body slide;
- include plain title and end cards;
- label build mode accurately;
- update ledger with artifact path, mode, and validity.

Gate 8: PPTX built in the correct mode.

Stop if accepted image inventory is missing, partial, pending, rejected, or made from reference/source assets rather than generated scenes.

### Stage 9: Presenter sidecar

Required work:

- create presenter sidecar, preferably PDF;
- explain target audience, purpose, core principle, selected frame, narrative arc, lessons, slide-by-slide guide, discussion prompts, practical application, assumptions, boundaries, and asset/receipt/canonisation notes;
- update ledger.

Gate 9: sidecar exists for final candidate or finished package.

Stop before final status if sidecar is missing or not a usable presenter guide.

### Stage 10: Presentation QA

Required work:

- review issue alignment, frame strength, doctrine, Patch story, accepted generated scene-image inventory, image-led quality, text hierarchy, notes, sidecar, practical transfer, receipt/canonisation, and repo/source grounding;
- use green/amber/red status;
- include ledger in QA basis or artifact manifest.

Gate 10: QA report produced.

Final status rules:

- Green: package satisfies doctrine, issue acceptance criteria, accepted generated scene-image inventory, Patch canon, notes, sidecar, QA, and receipt/canonisation status.
- Amber: usable explicitly scoped draft/storyboard/final candidate with known missing or weak pieces that were not silently skipped.
- Red: mandatory gate failed, frame is missing/weak, Patch canon failed, generated scene-image inventory is missing, source/reference assets were substituted without explicit approval, image QA was bypassed, production phase was skipped without approval, ledger was lost/contradicted, or significant redesign is required.

Do not mark green because a deck merely looks polished.

### Stage 11: Receipt and canonisation follow-up

Required work:

- create or plan presentation image receipt for finished PPTX files using generated/embedded images;
- identify reusable asset candidates;
- open, perform, or recommend follow-up canonisation work;
- update ledger.

Gate 11: receipt/canonisation status recorded.

Stop before finished status if embedded/generated images are used and receipt status is unknown, or reusable assets emerged but no canonisation follow-up is recorded or explicitly deferred.

## Failure reporting

When a production pass fails or is downgraded, comment on the source issue unless Harley asks not to.

Use this template:

```markdown
## Production pass status: Red | Amber | Green

### Stage reached

<stage name and number>

### Gate result

<which gate passed or failed>

### Run-state ledger

<repo route, source issue, fetched surfaces, frame state, artifact mode, proof_run, downgrade_approval, local sources allowed, image_generation_route, image_qa_route, accepted_scene_image_inventory, current blocker>

### Proof-run validity

- Full playbook run attempted: yes/no
- Stage reached:
- Mandatory gate failed:
- Accepted generated scene-image inventory exists: yes/no
- Post-generation Patch image QA completed: yes/no
- Reference assets used as substitute art: yes/no
- Downgrade explicitly approved by Harley: yes/no + quote/comment ID
- PPTX build permitted by playbook: yes/no
- Sidecar produced: yes/no
- QA produced: yes/no
- Receipt produced: yes/no
- Result: Red / Amber / Green
- If Amber or Red, exact repair required:

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

Treat these as Red unless Harley explicitly scoped the run differently beforehand:

1. Continuing after image generation is unavailable/unbound instead of stopping at the image gate.
2. Skipping actual image-generation invocation at the image stage and substituting asset/source/reference sheets for body-slide art.
3. Bypassing post-generation Patch image QA before PPTX build.
4. Using generated images that do not follow canonical Patch style, including dog/animal Patch, glossy 3D mascot Patch, generic robot Patch, duplicate Patch, Patch-like support teams, missing bag/antennae, wrong eyes, or wrong bag symbol.
5. Describing invalid images, storyboard, draft, asset-sheet deck, or partial run as a completed proof.
6. Claiming tool sparsity before discovering/testing live GitHub-capable repo access or image-generation routes.
7. Treating search/index failure as repo unavailability after a direct repo route succeeded.
8. Losing repo-green ledger state during artifact generation, local file work, image work, or zip inspection.
9. Inspecting project-source zips by hard-coded legacy filename rather than repo-indexed package discovery.
10. Marking a polished but weakly framed or corporate-diagram deck as green.

Future passes must stop at the relevant gate and report the blocker rather than silently producing false-green, near-green, or substitute artifacts.

## Repair policy

Prefer the smallest honest repair:

- If GitHub access appears unavailable, identify all GitHub-capable routes, preserve any route that already succeeded, and test direct repo metadata/file/issue reads before claiming a repo blocker.
- If repo access was green earlier but appears absent after a mode switch, stop and reconstruct the ledger.
- If project-source zip inspection is needed, read `assets/source-zips/INDEX.md`, record the repo-indexed package name, and inspect the project-source filename for package, import, or integrity reasons only.
- If the issue lacks a strong frame, resolve and record the frame before deck planning.
- If deck plan violates doctrine, repair the plan before image work.
- If image generation has not been tested at the image stage, test/invoke the image route or record exact absence.
- If Patch references are missing or uninspected, stop and inspect repo or contact-sheet references, or land missing references.
- If generated images fail Patch canon or scene fit, run the edit/regeneration loop through post-generation QA.
- If the accepted generated scene-image inventory is missing or incomplete, stop before PPTX build.
- If PPTX lacks notes or sidecar, keep it draft/amber or red depending on scope.
- If final package lacks receipt/canonisation status, do not mark finished.
