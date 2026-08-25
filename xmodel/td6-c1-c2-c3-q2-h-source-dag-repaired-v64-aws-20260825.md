# TD6 fixed-A3 q2 H-divisor repaired source-DAG checkpoint

V64 fulfills the load-bearing ancestry repair requested by the V60 hostile
review.  On the fixed source-typed A3 section and the raw divisor `H=0`, the
unique N13 current row 13 now traces through exactly previous row
`('X-1',14)` and original first rows.  The cached quadratic previous row
`('X-1',0)` remains an exact positive control but is explicitly not an N13
edge.

The repaired source replay also pins genuine P12 with counts
`2885/28/1640`, verifies its direct original-first-row ancestry, and
composes it with N13 to give the exact residual `-k/50`.  Three omission
controls detect loss of the previous-14 edge, current row 13, or the live
N13 correction.  The denominator ledger's radical support is exactly

```text
U, V,
P3 = V^4 - 32 V^2 U^3 + 128 U^6,
QH = V^4 + 8 V^2 U^3 - 64 U^6.
```

Therefore the producer-exact scope is only
`H=0, D(U*V*P3*QH)` inside the fixed A3 q2-beta section.  The four factor
strata remain direct source-rebuild obligations.  No whole-H, whole-A3,
TD6, SP-2, landing, or JC2 inference is made.

Frozen case:
`cases/td6_c1_c2_c3_q2_h_source_dag_repaired_v64_aws_20260825/`.

Custody hashes:

- source archive:
  `1a2e4f6766ffe5b15b963dd6ac86c02d538eb3e6d45b27d4a5a99e3c87a7aac6`;
- r6d stdout:
  `14775e9ad4adfb0a20512823be01bdd48da711e30b8ac7796e094841f41edd06`;
- proof DAG:
  `ef721416a7aac4f97167003801bfe94033e0b6627942d4ba9269c5565d9a962e`;
- denominator ledger:
  `259605ae41d2743d7f4280d4f7879d6c16b915a5ce0117a974366e9cc594b385`;
- V60 nonmutating ancestry erratum:
  `3443fcc6d6f332190a7569dab6ed6631e850174deb2e88b67dc4f4fe3bc4c069`.
