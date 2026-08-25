# TD6 fixed-A3 q2 `H=0` source-DAG certificate (V60)

Status: **exact fraction-field source identity on
`H=0, D(U V P3 QH)`; not a whole-`H` theorem.**

The raw center stratum is `H=C-3U^2=0`, hence `C=3U^2`.  Define

```text
P3 = V^4 - 32 V^2 U^3 + 128 U^6,
QH = V^4 +  8 V^2 U^3 -  64 U^6.
```

V60 preserves arbitrary-degree original rows and uses an edge-only proof DAG:
the unique current N13 row 13 is reduced through exactly the previous rows
`('X-1',0)` and `('X-1',14)`, and those edges are replayed against original
first rows.  The genuine P12 is reduced directly through 28 original first
rows.  Its 2,885 terms, 1,640 multiplier terms, beta tail, and multiplier
objects agree exactly with the reviewed V44 objects.  The exact composition
has residual `-k/50`.

The full emitted denominator radical is `U*V*P3*QH`.  The factor `QH` is new:
it occurs in the row-13 first multipliers and in the row-14 previous-to-first
edge.  Therefore this package explicitly rejects any inference that the old
`U*V*P3` open covered the whole `H=0` divisor.  Direct source-DAG rebuilds on
`V=0`, `P3=0`, and `QH=0`, including their intersections away from the
already separate `U=0` stratum, remain required.

## Exact controls

- transport rank: `3470/3602`;
- first, previous/pole, current ranks: `38/132`, `38/94`, `25/56`;
- current source rows used: `[13]`;
- previous source rows used: `[('X-1',0), ('X-1',14)]`;
- one-edge omission is an exact negative control;
- P12 without N13 is an exact negative control;
- coefficient denominators and their factorizations are recorded line by
  line, rather than inferred from a digest.

Strict scope: fixed source-typed A3 center, q2-beta source, `H=0`, and
`U*V*P3*QH != 0`.  No whole-`H`, full-A3, full-TD6, SP-2, landing, or JC2
claim.

## AWS custody

- Host: r6d `100.26.198.153`.
- Run: `/home/ubuntu/runs/td6_v60_h_raw_r6d_20260825T1231Z`.
- UTC: `2026-08-25T12:29:27Z`--`2026-08-25T12:57:19Z`.
- Exit code: `0`.
- Elapsed: `27:52.03`; maximum RSS: `674212` KiB.
- Source archive SHA256:
  `78dae78e0aca67bb6ab81ab234fba52c8116b98614de141db04f4c669db967e5`.
- Stdout SHA256:
  `d029a06d35a16265cbcb6e473b89006d1fe55d993466793a8224c573b95f89cd`.
- DAG SHA256:
  `9516116934a1b3cbde7894f2eeb8010e45b0c1dc4bfd1192ba2e04dd36148ddb`.
- Denominator ledger SHA256:
  `259605ae41d2743d7f4280d4f7879d6c16b915a5ce0117a974366e9cc594b385`.

