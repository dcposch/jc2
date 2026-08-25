# TD6 V56B exact zero current rows 36--39

Frozen status: **producer-exact narrow AWS supplement**.

Four independent one-row V56B jobs on Box03 exited zero for current original
rows `('X0',36)` through `('X0',39)`.  Each emitted the raw-polynomial digest

```text
84315a814615731cc801bec5a1747c2ad15d6a4262aae78bbeb0847f694495b1
```

The pinned canonical serializer represents an empty dictionary as
`('dict', ())`; hashing that exact representation gives the same digest.
Thus these are exactly zero source equations, not merely four equations with
equal unknown content.  Their lifted-relation digest is also identical and
every original-row replay and terminal shard check passed.

The portable `verify_zero_rows.py` recomputes the empty-dictionary digest,
pins the canonical parent and shard producer sources, checks the immutable
archive/source custody, and verifies every required marker and negative scope
line in all four AWS outputs.

The verifier was replayed independently on r6d under tag
`td6_v56b_zero_rows_verify_r6d_20260825T1120Z`.  It exited zero with stdout
SHA256 `7a715a60282802553d5830613b050a795f99c31c5eff8e03efd827104b1907d9`
and empty stderr.

This package proves only that rows 36--39 vanish in the fixed source-typed A3
q2-beta post-transport current family.  It supplies no nonzero compatibility,
no row-level obstruction, no 40-row completeness, no source-ideal unit, no
fixed-A3 theorem, no whole-TD6 theorem, and no SP-2 or JC2 conclusion.
