# Adventures of Patch

Adventures of Patch is a repository for developing short, visual adventures that explain agentic workflows. The current practical outputs are PowerPoint presentations used as mini talks for colleagues and peers at work, and one-page fairytale images that land a single principle.

## What this project does

Agentic workflows can be difficult to explain as process diagrams or abstract terminology. This project turns those ideas into a small story: Patch enters a world, encounters a problem, and makes the workflow visible through what he does next. The result is intended to be memorable enough to discuss in a short workplace presentation.

This is a working development repository, not an application or an agent runtime. Some material is exploratory, some is reusable project canon, and some work eventually becomes a finished deck. The repository describes the project as it is now: evolving, presentation-led, and grounded in real explanations for real audiences.

## What gets developed here

- adventure ideas and narrative frames for explaining workflow concepts;
- Patch's visual canon, environments, props, and supporting assets;
- deck plans, presentation structure, and presenter material;
- one-page fairytales that land a concise agentic or operational principle;
- PowerPoint/PPTX presentations and the supporting review or receipt material needed when a package is ready to use.

## The usual journey

1. Start with an agentic-workflow idea that needs explaining.
2. Turn the lesson into a bounded Patch adventure with visible stakes and choices.
3. Develop the visual language, assets, and story continuity needed to make the lesson happen on the slide.
4. Build and review the presentation, adding presenter notes or a sidecar when useful.
5. Use the finished deck as a short presentation with colleagues and peers, then carry the learning into the next adventure.

## Repository map

The top-level layers are organised by licence and maturity:

- [`published/adventures/`](published/adventures/) is the home for committed presentation artifacts and deck working folders.
- [`published/fairytales/`](published/fairytales/) is the home for one-page fairytale artifacts and their source scenes.
- [`build/`](build/) contains reusable assets that feed the published layer: characters, environments, props, canon, role-kits, and templates.
- [`style/`](style/) contains the text and visual style bibles and reference sheets that drive image generation.
- [`workbench/`](workbench/) is the repo-tracked working lane for active experiments and drafts.
- [`docs/project/`](docs/project/) points to project-specific sources, provenance, and guidance.
- [`.agents/`](.agents/) contains project doctrine, runbooks, local skills, and other agent-facing infrastructure.
- [`tools/`](tools/) contains deterministic maintenance and validation helpers.

Scratch files, uploaded source packages, generated projections, and old presentation material are not automatically current just because they exist locally; follow the indexed repo paths to find the active source.

## Patch's role

Patch is the recurring project character and visual through-line unless a particular presentation explicitly excludes him. He is not an agent, owner, or authority figure. His job is to give abstract workflow ideas a consistent character, setting, and point of view that people can follow.

## Finding your way around

Start with the generated [repository index](INDEX.md) for the current map of the tree. The [project index](docs/project/INDEX.md) points to project-specific sources and guidance. [`AGENTS.md`](AGENTS.md) explains the repository rules for contributors and automated work. [`build/TAXONOMY.md`](build/TAXONOMY.md) defines the current asset taxonomy.

## Licensing

This is a mixed-licence repository rather than a single-licence project.

- Original project-authored software is intended to be MIT-licensed where the project has the rights needed to grant MIT and no more specific notice applies.
- Original visual and media assets are intended to be CC BY-ND 4.0 where the project has the rights needed to grant that licence and no more specific notice applies. In practical terms, the supplied licensed assets may be used and redistributed in their licensed form with attribution, but adapted versions may not be publicly shared under that licence.
- Patch, Bit, Bot, the Heist Crew, other original Adventures of Patch characters, their distinctive designs and identities, and Adventures of Patch world/branding rights are not offered as an open character universe. The asset licence does not grant a general right to publish new or adapted character depictions, derivative characters, or new Adventures of Patch stories without separate permission.
- `HarleyBartles/portfolio` has one narrow, recorded exception for the specifically documented derivative Heist Crew assent-marker images; it does not relicense the source assets or create a general adaptation right.
- Third-party, vendored, adapted, or upstream-derived material keeps its own applicable licence and attribution requirements.

Private experimentation is not the boundary this policy is trying to police; the practical reservation is around publishing and distributing transformative Adventures of Patch character/world material.

See [`LICENSE`](LICENSE), [`LICENSING.md`](LICENSING.md), and [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) for the licensing map and current audit posture.
