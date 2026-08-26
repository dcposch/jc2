# V80A deployment erratum

The immutable V80A source archive
`baf57130b9a7f95387a19695c30c4a800d7eb2cbb22cca24875bac4119bb207a`
and its 22 AWS shard outputs are deployment-negative evidence only.  Every
shard exited 1 before importing the frozen transport source.  The hard-coded
parent pin was

```text
fb138b0f59a611bab365f37c0302418eda485318beec3f6b21237a95fdc41198
```

whereas both the V80A source manifest and a literal SHA-256 computation give

```text
fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198
```

The mismatch is the single hexadecimal digit at zero-based position 10
(`a` versus `e`).  No V80A shard reached transport construction, and no
mathematical or dead-stretch conclusion may be consumed from it.  V80B
changes that pin, renames the producer/case surface, and preserves all other
source-audit logic.
