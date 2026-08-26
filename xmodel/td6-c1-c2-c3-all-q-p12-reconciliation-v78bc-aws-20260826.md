# TD6 V78B/V78C exact reconciliation supplement

Producer verdict: **PASS**.

The dual simultaneous V78B calculations and the dual-host 44-run V78C shard
atlas agree exactly.  All four independently produced/assembled 23-line
tables have SHA256

```text
e14ff29cf5ca4301640215f10c3f0911df169cfac03b79624b6e18d088f360ef.
```

Both V78B runs returned rc0 with their standalone PASS marker after all 22
source coordinates, direct-q-prime omissions, first conormal, genuine P12,
original-row source lifts, varying multiplier/lambda terms, denominator
checks, and omission controls.  The agreement discharges the preregistered
simultaneous-versus-basis-shard and dual-host reconciliation gate.

Together with V78C, the exact statement is: for the 22 licensed q directions
`q2,...,q14,q16,...,q24` (q15 is gauge), the first conormal map is zero and
the genuine-P12 reduced sensitivity has support exactly through q14; q16--q24
are exact P12 source syzygies.  Denominator radicals are contained in
`U`, `H=C-3U^2`, and `B3`.

Scope remains fixed source-typed A3, generic `D(U*H*B3)`, square-zero
first-order/source-support only.  No nonlinear family, no assertion about all
other current rows, no full TD6, SP-2, or JC2 inference.

Frozen case:
`cases/td6_c1_c2_c3_all_q_p12_reconciliation_v78bc_aws_20260826/`.
