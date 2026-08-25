# TD6 q2 row-13 source-lift reuse checkpoint

The completed V56 current-row shard provides an exact reusable source lift
for `('X0',13)`, the unique row in the generic staged N13 left-null support.
The run is rc0, source-closed, and replays the row through exactly the raw
previous ancestors `('X-1',0)` and `('X-1',14)` plus the original first rows.

This materially narrows the generic source-lift problem: the remaining 39
current-row shards are irrelevant to N13 itself.  Genuine P12 is row 12 and
already has the independently reviewed V43 direct-first certificate.

The result is held at custody tier, not promoted to a `D(U H B3)` unit
theorem.  Shard mode hashes the complete row-13 lift but exits before emitting
its individual multipliers and denominator ledgers.  V59/V60 must supply that
denominator audit and the explicit singleton-weight/P12 composition.  This
checkpoint therefore licenses reuse and background review, but no generic
open, fixed-A3 family, TD6, SP-2, landing, or JC2 conclusion.

Frozen case:
`cases/td6_c1_c2_c3_q2_row13_reuse_custody_aws_20260825/`.

Key custody hashes:

- source archive: `afb1bbab4572893eb1c5b96faa82832fbfd55508142e9085711952c964cdcc2a`;
- stdout: `f5911fda0e8e64720d4e2e9a3eb40a3188526d323c9e7ed46beb8c69efc5b112`;
- raw row: `ec21f21a48f771929134e861cc981b730de81622b7645905318bcfb5ca3b1652`;
- complete lift: `95906283f5ec65f70ef4e9b666de1210d93f2f0980ed35f7ab8440e238ebc139`.
