# TD6 fixed-A3 q2-beta: exact zero current rows 36--39

Status: **PRODUCER-EXACT NARROW AWS SUPPLEMENT**

Date: 2026-08-25

Within the fixed source-typed normalized A3 section and post-transport chart,
four one-row V56B jobs prove that current original equations `('X0',36)`
through `('X0',39)` are exactly zero polynomials.  This is a source-shape
fact, not an incompatibility.

The pinned canonical serializer sends an empty dictionary to
`('dict', ())`.  Its exact SHA256 is

```text
84315a814615731cc801bec5a1747c2ad15d6a4262aae78bbeb0847f694495b1.
```

Every AWS row emitted that raw-polynomial digest, the same empty-lift digest
`d78fca8e...`, `current_shard_original_row_replay=true`, and terminal PASS.
All four exited zero.  Their stdout SHA256 values are, in row order,

```text
36  90efcd98c1a14660f1f2afaf66d7973d537282553acdbc893683a7078cfb9172
37  88283e566a071fa2cfe6ce76cfa14ed202cd68d6b8d599e969e9f5988ce7557f
38  cda14fcdd06924e63d179724a8467d673a53a75ae3ab02945418669d88c0e9b2
39  7c567546c67b42ee9e7b86470da41186060b9c75cc4c6b513309a018b26b7a4b
```

The portable verifier pins canonical parent source SHA
`3cc0fc3b...` and shard producer source SHA `589ea51f...`, recomputes the
empty-dictionary digest, and checks every row, custody marker, negative scope
line, and terminal PASS.  Independent r6d replay tag
`td6_v56b_zero_rows_verify_r6d_20260825T1120Z` exited zero; verifier stdout
SHA256 is `7a715a60282802553d5830613b050a795f99c31c5eff8e03efd827104b1907d9`
and stderr is empty.

Scope is strictly rows 36--39 of the fixed-A3 q2-beta post-transport current
family.  This proves no nonzero compatibility or obstruction, no 40-row
completeness, no source-ideal unit, no full fixed-A3 result, and no whole-TD6,
SP-2, or JC2 statement.
