# Released artifacts

Keep the versioned release archives and their metadata here. They are
historical snapshots; use the campaign's current `AUDIT.md` for corrections
and the scope of mathematical claims.

- `jc72108-paper1-artifact-v1.tar.gz`: Paper 1's original reproduction package,
  including the former `lean/` project and its Python generator.
- `jc72108-theory-bundle-v1.tar.gz`: the original theory bundle.
- `ZENODO-METADATA.md` and `ZENODO-METADATA-BUNDLE.md`: release metadata.

The unpacked theory bundle was removed after verifying that all 302 files
exactly matched the archive, with no extra files. When an old citation needs
that snapshot, extract it from the repository root:

```sh
tar -xzf dist/jc72108-theory-bundle-v1.tar.gz -C dist
```

The extracted directory is Git-ignored. Current formalization source lives in
[`jc2-lean/`](../jc2-lean/README.md), including the migrated
[`cascade-certificate/`](../jc2-lean/cascade-certificate/README.md) worked example.
