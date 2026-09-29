# Repository-owned skills routing

Repository-owned skills live under `.agents/skills/adventures-*/` and are listed exactly in `.agents/plugins/marketplace.json`. The pinned `.agents/plugins/marketplace-source` supplies implementations for selected standards; ambient plugins are not subscribed or projected into this repository.

Edit repository-owned skill sources in place. For standard or skill ownership changes, use `.agents/playbooks/marketplace-generation.md` and validate with `py -3 tools/run.py ci --check`. Navigation uses direct repository links and canonical homes.
