# Visual bible creation playbook

This playbook defines how Adventures visual bibles are created, updated, normalised, and locked for reusable asset classes.

Use this playbook when a visual-preproduction task needs a new minimal provisional bible before image generation, when accepted Pass A imagery should update a bible, when accepted Pass B family sheets should lock a bible, or when an older bible needs to be normalised into the Patch v1.4 operational shape.

## Primary skill route

Use `adventures-visual-bible-creator` as the primary skill for authoring bible content.

Compose with:

- `adventures-visual-bible-interpreter` after a bible exists and must be converted into prompt, QA, repair, and extrapolation packets;
- `adventures-visual-preproduction` when the bible is part of a preproduction image-generation loop;
- `adventures-image-preflight` when the bible blocks must be turned into a concrete prompt contract;
- `adventures-image-qa` when a generated image candidate must be accepted, repaired, regenerated, or blocked.

The creator writes or updates the bible. The interpreter reads a repo-indexed or provisional bible and extracts operational constraints. Image QA accepts or rejects generated images. Do not collapse those responsibilities into one step.

## Source discipline

Start from repo truth. For asset-sensitive work, begin at `assets/INDEX.md` and follow the index mesh to discover existing asset-family docs, bibles, style guides, source zips, receipts, and accepted references.

Use accepted generated images and Harley-approved uploaded images as visual evidence only for the scoped bible task. Do not treat unaccepted candidates, project-source zips, or session handoff notes as canon unless repo evidence or Harley explicitly scopes them as evidence.

Always partition evidence into:

- repo text;
- repo-indexed visual/source package evidence;
- accepted generated reference evidence;
- user-supplied visual evidence for this task;
- inference;
- uncertainty.

## Standard bible states

Use these states consistently:

- `minimal_provisional` - enough to steer first Pass A generation and QA;
- `updated_provisional` - refined from an accepted Pass A overview or intermediate accepted references;
- `locked` - refined from accepted Pass B family assets and ready to act as durable visual source doctrine;
- `blocked_missing_bible` - an expected existing bible cannot be discovered;
- `amber_text_only` - text evidence exists but required visual evidence could not be inspected.

A bible can be generation-ready while still provisional. Do not call it locked until accepted family imagery and any required landing/canonisation evidence supports that state.

## Required bible shape

Use the Patch style bible v1.4 as the operational house pattern. Do not copy Patch canon into other assets; copy the structure and degree of mechanical extractability.

A standard bible should normally include:

```markdown
# <Asset Name> Visual Design Guide vX.X

## Version note
## Evidence basis
## Asset overview
## Function and narrative role
## Visual style
## Palette
## Materials / construction / environment language
## Anatomy / layout / location system
## Text and signage posture
## Belongs in this asset family
## Does not belong in this asset family
## Allowed variation
## Do's and Don'ts
## Extractable Prompt and QA Blocks
### Prompt-positive canon block
### Prompt-negative canon block
### Sensitive detail micro-specs
### QA hard-gate checklist
### Feature-specific repair blocks
### Extrapolation rules
### Prompt guidance for image generation
## Reference note
```

Adjust headings to the lane. Environment bibles should emphasise layout, materials, palette, signage, location system, and contamination risks. Character bibles should emphasise identity-critical anatomy, wardrobe, face, props, scale, expression, and pose. Prop bibles should emphasise object states, handling, continuity semantics, labels, and success/failure variants.

## Minimal provisional bible

Before Pass A image generation for a new reusable asset class, create a minimal provisional bible that includes at least:

- asset name and lane;
- source issue/task;
- bible state;
- evidence basis;
- intended tone, function, and visual direction;
- positive prompt block;
- negative prompt block;
- text/signage posture where relevant;
- what belongs and what does not belong;
- QA hard gates;
- known uncertainty.

If images are not available, mark the bible as concept/repo-text/inference based. If accepted images are available, extract durable palette, materials, motifs, layout rules, hard negatives, and likely repair constraints from them.

## Updating and locking

After an accepted Pass A overview, update the bible from durable learning in the accepted image. Preserve prior constraints unless Harley or repo evidence explicitly changes them.

After accepted Pass B member sheets, update and lock the bible, or explicitly leave it provisional with unresolved questions.

Do not canonise accidental text, malformed objects, distorted anatomy, one-off decoration, image-generator glitches, or composition accidents. Failed imagery should become anti-pattern guidance only when the failure is repeated, durable, or semantically important.

## Prompt and repair hygiene

Image-facing blocks must be prompt-safe. Do not paste QA prose, candidate numbers, repo paths, issue comments, status labels, process notes, sidebars, or checklists into prompt-positive, prompt-negative, or repair blocks.

Repair blocks should preserve passed features, repair only the failed feature, state positive visual constraints, and include only the negatives needed for that failure mode.

## Output contract

A bible creation/update pass should return either the bible itself or a concise creator report:

```markdown
## Bible creator report

- Source issue/task:
- Asset/lane:
- Input evidence:
- Existing bible:
- Target bible state:
- Gaps found:
- Recommended updates:
- Status:
```

## Boundaries

Do not generate images. Do not run image QA. Do not claim asset-ready. Do not land repo files unless Harley explicitly asks for durable repo updates or the active playbook requires a repo landing step.