# h2c-indexer-secret

Secret indexer for [helmfile2compose](https://github.com/helmfile2compose/helmfile2compose) — indexes Secret manifests into `ctx.secrets` for volume/env resolution.

**The Guardian** — one of the Seven Bishops, the founding extensions of the helmfile2compose distribution.

> Heresy level: 0/10 — a faithful scribe, nothing more.

## Type

`IndexerConverter` (priority 50)

## Kinds

- `Secret`

## Install

Via [h2c-manager](https://github.com/helmfile2compose/h2c-manager):

```sh
python3 h2c-manager.py secret-indexer
```

Or listed in `distribution.json` — installed automatically when building a distribution.
