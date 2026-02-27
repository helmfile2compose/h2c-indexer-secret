# dekube-indexer-secret

Secret indexer for [dekube](https://dekube.io) — indexes Secret manifests into `ctx.secrets` for volume/env resolution.

**The Guardian** — one of the Eight Monks, the founding extensions of the helmfile2compose distribution.

> Heresy level: 0/10 — a faithful scribe, nothing more.

## Type

`IndexerConverter` (priority 50)

## Kinds

- `Secret`

## Install

Via [dekube-manager](https://github.com/dekubeio/dekube-manager):

```sh
python3 dekube-manager.py secret-indexer
```

Or listed in `distribution.json` — installed automatically when building a distribution.
