# Adventures of Patch

Adventures of Patch is a repository for developing short, visual adventures
that explain agentic workflows. The current practical outputs are PowerPoint
presentations used as mini talks for colleagues and peers at work, and one-page
fairytale images that land a single principle.

## What this project does

Agentic workflows can be difficult to explain as process diagrams or abstract
terminology. This project turns those ideas into a small story: Patch enters a
world, encounters a problem, and makes the workflow visible through what he
does next. The result is intended to be memorable enough to discuss in a
short workplace presentation.

This is a working development repository, not an application or an agent
runtime. Some material is exploratory, some is reusable project canon, and
some work eventually becomes a finished deck. The repository describes the
project as it is now: evolving, presentation-led, and grounded in real
explanations for real audiences.

## What gets developed here

- adventure ideas and narrative frames for explaining workflow concepts;
- Patch's visual canon, environments, props, and supporting assets;
- deck plans, presentation structure, and presenter material;
- one-page fairytales that land a concise agentic or operational principle;
- PowerPoint/PPTX presentations and the supporting review or receipt material
  needed when a package is ready to use.

## The usual journey

1. Start with an agentic-workflow idea that needs explaining.
2. Turn the lesson into a bounded Patch adventure with visible stakes and
   choices.
3. Develop the visual language, assets, and story continuity needed to make
   the lesson happen on the slide.
4. Build and review the presentation, adding presenter notes or a sidecar when
   useful.
5. Use the finished deck as a short presentation with colleagues and peers,
   then carry the learning into the next adventure.

## Repository map

- [`docs/adventures/`](docs/adventures/) contains adventure concepts and
  narrative frames.
- [`docs/principles/`](docs/principles/) contains working principles expressed
  through Patch stories.
- [`assets/canon/patch/`](assets/canon/patch/) holds reusable Patch canon and
  related visual source material.
- [`assets/evidence/receipts/`](assets/evidence/receipts/) holds evidence and
  receipt packages produced from asset or deck work.
- [`decks/`](decks/) is the home for committed presentation artifacts and deck
  working folders.
- [`fairytales/`](fairytales/) is the home for one-page fairytale artifacts and
  their source scenes.
- [`scripts/`](scripts/) contains deterministic maintenance and validation
  helpers.
- [`.agents/`](.agents/) contains project doctrine, runbooks, local skills, and
  other agent-facing infrastructure.
- [`scratch/`](scratch/) is local working space, not a source of project truth.

## Patch's role

Patch is the recurring project character and visual through-line unless a
particular presentation explicitly excludes him. He is not an agent, owner,
or authority figure. His job is to give abstract workflow ideas a consistent
character, setting, and point of view that people can follow.

## Finding your way around

Start with the generated [repository index](INDEX.md) for the current map of
the tree. The [project index](docs/project/INDEX.md) points to project-specific
sources and guidance. [`AGENTS.md`](AGENTS.md) explains the repository rules
for contributors and automated work.

The repository is the canonical project source. Scratch files, uploaded source
packages, generated projections, and old presentation material are not
automatically current just because they exist locally; follow the indexed repo
paths to find the active source.
