# TD6 fixed-A3 q2 `H=0` source-DAG checkpoint

V60 supplies the missing original-row ancestry for the q2-beta obstruction on
the raw center divisor `H=C-3U^2=0`.  It replays the singleton N13 dependency
through current row 13, previous rows 0 and 14, and original first rows;
independently, it replays the genuine P12 directly through 28 first rows.  The
exact scalar composition has residual `-k/50`.

The complete denominator ledger changes the scope materially.  Its radical
is

```text
U * V * P3 * QH,
P3 = V^4 - 32 V^2 U^3 + 128 U^6,
QH = V^4 +  8 V^2 U^3 -  64 U^6.
```

`QH` was absent from the earlier staged denominator account but appears in
the source lift of row 13 and the row-14 previous edge.  The exact theorem is
therefore only the fraction-field obstruction on
`H=0, D(U V P3 QH)`.  There is no whole-`H` conclusion.  Fresh source-DAG
rebuilds on `V=0`, `P3=0`, and `QH=0`, plus intersections, are charged.

Frozen case:
`cases/td6_c1_c2_c3_q2_h_source_dag_v60_aws_20260825/`.

Key hashes:

- source archive: `78dae78e0aca67bb6ab81ab234fba52c8116b98614de141db04f4c669db967e5`;
- stdout: `d029a06d35a16265cbcb6e473b89006d1fe55d993466793a8224c573b95f89cd`;
- proof DAG: `9516116934a1b3cbde7894f2eeb8010e45b0c1dc4bfd1192ba2e04dd36148ddb`;
- denominator ledger: `259605ae41d2743d7f4280d4f7879d6c16b915a5ce0117a974366e9cc594b385`.

Strict scope: fixed source-typed A3 q2-beta section on the stated open.  No
full-A3, TD6, SP-2, landing, or JC2 claim.
