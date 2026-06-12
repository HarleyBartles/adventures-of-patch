# assets/visual-sidecars index

Repo-resident image-sidecar selection and routing layer.

## Files in this directory

- `INDEX.md`
- `schema.v0.1.json`
- `index.v0.1.json`

## Subdirectories

- `shards/`

## Notes for agents

This lane is a text-first selection mesh for tracked repo images. Use `index.v0.1.json` to find the shard, then the shard JSON to read the record for a tracked image path.

Tracked image inventory: 173 files (172 png, 1 jpeg/jpg, 0 webp, 0 gif, 0 svg).

Inspection mode for this pass: metadata-only.
