# Post-collection integrity erratum — round `20260824T0453Z-dd11599`

**Recorded:** `2026-08-24T05:55:47Z`, after blind collection closed.

The sealed packet displayed a 63-character digest for `AUDIT.md`:

```text
a0033b88030fbd73b1f342d64ed99f5568e4385f33d30f37124e69a17dcca32
```

The actual SHA-256 of both the on-disk file at cutoff and
`dd11599b07eb05591b5c006791005eef19457d8e:AUDIT.md` is:

```text
a0033b88030f0bd73b1f342d64ed99f5568e4385f33d30f37124e69a17dcca32
```

The displayed packet value omitted the `0` after `...030f`. The path, clean
basis, file bytes, read scope, and mathematical snapshot were unambiguous and
unchanged. The sealed packet was not edited. This is a provenance-table typo,
not a mathematical delta and not an alternate input version.

Grok detected the mismatch during collection. The atlas, zero-base, and
falsifier reports incorrectly state that every listed digest matched; those
metadata assertions fail for this one row even though each reports reading
the actual `AUDIT.md`. Root did not assert a hash match. The synthesis must
preserve this distinction.
