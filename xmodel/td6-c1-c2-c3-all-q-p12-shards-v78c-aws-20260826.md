# TD6 V78C dual-host all-q P12 shard result

Producer verdict: **exact PASS; hostile review pending**.

The frozen case
`cases/td6_c1_c2_c3_all_q_p12_shards_v78c_aws_20260826/` contains 44
proof-carrying AWS runs: one run on Box02 and one on r6d for each licensed q
coefficient `q_e`, `e=2,...,14,16,...,24`.  Coefficient `q_15` is excluded
because it is the lower target-shear gauge.

Every run returned `rc=0`, a standalone PASS marker, exact source-row replay,
direct-q-prime and source-row omission controls, varying multiplier/lambda
terms, and denominator support.  The 22 output rows assemble independently on
both hosts to the same byte string:

```text
ALL_Q_P12_COLUMNS.UNION.tsv
SHA256 e14ff29cf5ca4301640215f10c3f0911df169cfac03b79624b6e18d088f360ef
```

The first-stage conormal map is zero on all 22 basis directions.  The genuine
P12 reduced sensitivity is nonzero for every direction `q2,...,q14` and exact
zero for every licensed direction `q16,...,q24`.  All directions nevertheless
have 14 active lambda-prime rows.  Therefore the high-jet zero values are
exact original-row syzygies, not an omission of coefficient variation.  The
only denominator radicals are

```text
U,
H = C-3U^2,
B3 = 4C^2U^2-4CV^2U+24CU^4+V^4-20V^2U^3+20U^6.
```

The q2 row agrees with V32 (`raw 816da33c...`, remainder `1acfd5c0...`).
The q3 row agrees with corrected and hostile-reviewed V77R (`raw 70d253cd...`,
remainder `3dd07bb5...`).  This gives a sharp degree-14 cutoff for this P12
adjoint/source-support tensor.

The scope is deliberately narrow: exact first-order/source-support evidence
on the already-empty fixed source-typed A3 generic open
`D(U*(C-3U^2)*B3)`.  It does not prove a nonlinear q-neighborhood, a q-family,
that q16--q24 vanish in other current rows, a full TD6 result, SP-2, or JC2.
The simultaneous V78B runs are still a separate reconciliation gate.

Source archive SHA256:
`b566a57ea50c3f4d24c091f006fe321aa9bb813368049773ee89b347d1284be4`.
Frozen manifest and report hashes are recorded in the case FREEZE file.
