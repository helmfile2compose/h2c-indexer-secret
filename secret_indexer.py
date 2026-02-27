"""Secret indexer — populates ctx.secrets."""

from dekube import ConverterResult, IndexerConverter  # pylint: disable=import-error  # h2c resolves at runtime


class SecretIndexer(IndexerConverter):  # pylint: disable=too-few-public-methods  # contract: one class, one method
    """Index Secret manifests by name for volume/env resolution."""
    name = "secret"
    kinds = ["Secret"]

    def convert(self, _kind, manifests, ctx):
        """Index Secret manifests into ctx.secrets."""
        for m in manifests:
            meta = m.get("metadata") or {}
            name = meta.get("name", "")
            if name:
                ctx.secrets[name] = m
        return ConverterResult()
