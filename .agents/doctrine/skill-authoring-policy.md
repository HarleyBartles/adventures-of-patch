# Skill authoring policy

Status: active policy
Owner: Adventures of Patch repository
Scope: repo-local skill custody and identity

Portable skill qualification, authoring, testing, and deployment behavior
belongs to `writing-skills`. This policy contains only the repository delta.

## Local custody

- Repo-local skill names use the `adventures-*` prefix and live under
  `.agents/skills/`.
- List each local skill's exact directory/frontmatter name in
  `.agents/plugins/marketplace.json` under `repo.local_skills`.
- Marketplace-derived skills are installed projections of the pinned
  `.agents/plugins/marketplace-source` gitlink; do not author them here.
- A local skill may own recurring Adventures judgment about project readiness,
  canon, visual preproduction, or image acceptance. Project facts and detailed
  contracts remain in doctrine and runbooks.
- Patch may appear only as the project character and visual canon, never as an
  agent owner, actor, or execution lane.
- Do not add `agents/openai.yaml` to a repo-only skill unless it is explicitly
  being prepared for marketplace projection.
