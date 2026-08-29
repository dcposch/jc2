# Exact evidence index

## Production output

- terminal archive: `db522621095ca392e65280fe18044924d8566de3e1f30acd0b9e419e0798419d`;
- result JSON: `acf609052e4271573487d46e804f5651031d7632c710d114a271664ae199f83a`;
- verdict: `71b96178d8ac463e8ecc3fb7801d784cadd0ec1d4fa3c98b974ccaf7e5acac51`;
- Singular stdout: `899850c3d388e20ca9507ed42fbd616da11ed4e973945c759f0d005e5234c600`;
- empty Singular stderr: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
- transcript-gate JSON: `a14e1841374755245f4575b18dd258eadcc89aa7c96a8e1d67c142fdeac5852f`;
- endpoint semantic-plant values: `da3763d3b557e2e7db1f157a2e7eb68ecd8ded8d541211c318c4502b766993a4`;
- bordered semantic-plant values: `169bfd6619141bafcc9dadeda322d1eebd80dc90c20594163e96c46f5d372656`;
- terminal manifest: `9bf0b079ed2372d3e388d44d142d371a8cd3eb1770a6d1e9a645db6e1ad34aa0`;
- telemetry: `3da586e70c78d60519466f6c080b3a67f08c689f8c977865df1d1b73777fd81a`.

## Local lightweight replay

The fetched archive hash, complete terminal manifest, source manifest, original
artifact hashes, plant values, and required markers were replayed locally without
CAS computation.

- terminal-manifest replay transcript:
  `0b7553a3e8a1c7afe0669cb88a2f4b294883233e93db7ccd391d11bcf6e93ca9`;
- semantic postcheck transcript:
  `d063165311a0b1ba74a55c2eab7adb9b0f67b841400bb60a022a3774d6aaf3a1`;
- source-manifest replay transcript:
  `815b83ad1285b253d81b9c0b6fd1e5ae997fd9f70a71d97f36bb1ba37aa8e6ff`.

The terminal archive contains nine harmless AppleDouble metadata members emitted
when the immutable macOS source archive was unpacked by GNU tar. They are covered
by the terminal manifest and were explicitly materialized for the local complete
manifest replay; no mathematical source or output hash depends on them.
