# Code review runbook

This is the repository-specific overlay for Adventures review concerns.

## Review red flags

- marketplace-derived output overwrote `adventures-*` local custody;
- a generated index was hand-edited or descends into a gitlink/skill root;
- a runbook duplicates doctrine or generic workflow ownership;
- a deterministic compiler is presented as a judgment skill;
- a generated image is called accepted without the image-QA lane;
- Patch is described as an agent or actor rather than a character;
- local validation is reported without matching remote branch and PR proof.

The local complete check command is `py -3 tools/run.py ci --check`.
