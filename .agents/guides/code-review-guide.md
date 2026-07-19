# Adventures code-review guide

This is the repository-specific overlay for review work. It does not replace
`repo-worker-base`, `requesting-code-review`, `receiving-code-review`, or
`verification-before-completion`.

## Review order

1. Review the exact branch head and draft PR, not a stale local summary.
2. Check scope against the plan and disposition record.
3. Check that doctrine, guides, skills, playbooks, and scripts each remain in
   their smallest canonical surface.
4. For skills, verify frontmatter, trigger-only descriptions, local metadata,
   stop conditions, references, pressure scenario evidence, and no stale Patch
   actor identity.
5. Run `python scripts/generate_index_mesh.py --check`, the repository skill
   checks, and `git diff --check` on the final head.

## Review red flags

- marketplace-derived output overwrote `adventures-*` local custody;
- a generated index was hand-edited or descends into a gitlink/skill root;
- a guide duplicates doctrine or generic workflow ownership;
- a deterministic compiler is presented as a judgment skill;
- a generated image is called accepted without the image-QA lane;
- Patch is described as an agent or actor rather than a character;
- local validation is reported without matching remote branch and PR proof.

Return blockers with file paths and evidence. Keep this draft PR open for the
end-of-slice review; do not merge it as part of the implementation pass.
