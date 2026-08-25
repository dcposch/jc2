# TD6 fixed-A3 q2 `V=H=0` source-unit checkpoint

V62D gives an exact original-row unit identity on the rational edge
`V=H=0,D(U)` of the fixed source-typed A3 q2-beta section.  After transport,
the first stage has rank `38/132`; the previous/pole stage has rank `37/94`
and exactly two nonzero dependencies, at `('X-1',11)` and `('X-1',13)`.
Their exact Bezout combination is lifted back to the raw previous equations,
divided once by the original first pivots, and has remainder `1`.  The final
certificate uses 13 original first rows and 12 original previous rows and
replays the unit exactly while preserving arbitrary source-row degree.

The construction uses no current row, N13, or P12.  Independent omission of
one used first edge and one used previous edge breaks the identity.  Complete
source-coefficient and first/previous-pivot denominator ledgers both have
radical support exactly `{U}`.  Therefore the result certifies emptiness only
on `V=H=0,D(U)` for arbitrary beta.  It does not itself cover `U=0`; the
separately frozen direct whole-`U=0` source theorem is a later composition
leaf.  No whole-H, whole-A3, TD6, SP-2, landing, or JC2 inference is made.

The portable source archive was independently replayed on Box02 and r6d,
both with exit code zero.  The three proof artifacts agree byte-for-byte; the
stdout differs only in absolute artifact paths.

Frozen case:
`cases/td6_c1_c2_c3_q2_v_h_zero_source_unit_v62d_aws_20260825/`.

Custody hashes:

- source archive:
  `6d568ff6e77dc764c2ddae6b5be1c6b8baa75e47e364ac15f83d6e4aaaa52e42`;
- Box02 stdout:
  `50a143c637b0344b2ea8dc7d4f67ae85c4afe497b6d3fecb59a1d94665980a76`;
- r6d stdout:
  `db4e566e4dfb51d6bffe66fc271fb3e19d9b7b4c5c5b1d7657d1789a305dd1bf`;
- exact unit certificate:
  `6d672e839c84b518909ea70161761f929d249fa4251fa5852bde9f896c1572a1`;
- source denominator ledger:
  `02d29ba2f0112a5f2d83b1973d86e4350ae04203df1496a9f598c599c8d8426a`;
- pivot denominator ledger:
  `bacdf7a6869cb50f118c4a77fa646815963f9782be5bf0f387dc676361f8b034`.
