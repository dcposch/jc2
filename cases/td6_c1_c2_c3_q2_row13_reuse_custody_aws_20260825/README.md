# TD6 generic row-13 source-lift reuse custody

Status: **exact rc0 source-row lift, frozen for reuse; not by itself a
generic-open or family theorem.**

This package preserves the completed V56 shard for the unique current row in
the staged N13 left-null support on the fixed source-typed A3 q2-beta chart.
The exact producer reports:

```text
N13_equals_k_beta_over_25=true
N13_left_null_support=1
current_shard_indices=[13]
current_shard_row[0]_key=('X0', 13)
current_shard_previous_ancestor_keys=[('X-1', 0), ('X-1', 14)]
current_shard_original_row_replay=true
TD6-A3-Q2-SOURCE-ROW-SHARD-V56 PASS
```

The raw row digest is
`ec21f21a48f771929134e861cc981b730de81622b7645905318bcfb5ca3b1652`;
the complete lifted record digest is
`95906283f5ec65f70ef4e9b666de1210d93f2f0980ed35f7ab8440e238ebc139`.
The record contains the raw row, 94- and 56-variable remainders, first-only
relation, composed first relation, and raw-previous relation.  The producer
replays that record against the original first and previous rows before
hashing it.

## Reuse boundary

The singleton support means the full 40-row V56 union is not logically needed
to lift N13: row 13 is the only current dependency edge.  Row 12 is the
genuine P12 edge and belongs to the separately reviewed V43 first-stage
certificate, not to the N13 source ancestry.  Omitting row 13 or substituting
row 12 therefore cannot reproduce the reported singleton N13 dependency.

This custody package intentionally does **not** yet claim a source-replayed
unit on `D(U H B3)`.  V56 shard mode returns immediately after the row replay
and does not emit the individual source multipliers or their coefficient and
termwise denominator ledgers.  A theorem-level composition must additionally
pin the singleton left-null weight, genuine V43 P12 source relation, and exact
row-13 denominator support.  V59/V60 are the independent live producers for
those missing composition fields.  No denominator radical is inferred from a
digest alone.

## AWS custody

- Host: r6d, `100.26.198.153`.
- Run: `/home/ubuntu/runs/td6_v56b_current40_r6d_20260825T1028Z_s13`.
- UTC: `2026-08-25T10:28:49Z` to `2026-08-25T11:19:56Z`.
- Exit code: `0`.
- Maximum RSS: `867852` KiB.
- Source archive SHA256:
  `afb1bbab4572893eb1c5b96faa82832fbfd55508142e9085711952c964cdcc2a`.
- Stdout SHA256:
  `f5911fda0e8e64720d4e2e9a3eb40a3188526d323c9e7ed46beb8c69efc5b112`.
- Stderr SHA256:
  `176bbe36763c77537f2e6ce72f75da6397d395607536e7eb7cf2c28aff1d4cfc`.

Strict scope: fixed A3 center chart and q2-beta source, one generic current
row.  No full-A3, TD6, SP-2, landing, or JC2 conclusion.
