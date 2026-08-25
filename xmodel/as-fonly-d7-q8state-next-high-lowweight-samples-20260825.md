# AS F-only `D=7`: 66 predecessor-state samples all die by Q7 or high carry

**Status: PRODUCER EXACT AT SAMPLED-CANONICAL SCOPE; PROVISIONAL PENDING
DIFFERENT-MODEL REVIEW.**

The preceding exhaustive theorem fixed both the Q9 point `t=e17` and the
zero Q8 restored vector.  This successor probes the two omitted affine axes
separately:

- at fixed Q9 `e17`, zero and both scalar multiples of all 19 canonical Q8
  solution-kernel basis vectors (39 states);
- on the exact 13-dimensional Q9 Kuranishi zero locus, the base point and
  both scalar multiples of all 13 free basis directions, with a canonical
  full-system Q8 section at each point (27 states).

All 66 canonical Q8 states pass their 22 source rows.  The next Q7 affine
system has rank nine throughout.  Four states in each family are
incompatible already at Q7:

```text
Q8-kernel family: samples 31,32,35,36;
Q9-locus family:  samples 13,14,17,18.
```

For each of the remaining 58 states the Q7 system is compatible with a
nine-dimensional fibre.  A separate AWS lane exhausts all `3^9=19,683`
points of each such fibre, exact-divides every prior integer carry, and
compares the recursively derived rows `R12..R9` with the literal determinant
divided by 243.  Every fibre has high-row zero count zero.

Moreover, all 58 fibres have the same exact one-nonzero-coefficient
presentation SHA-256
`12d8487739c38e0c5508ac6438067fbce3d51aa7dc223e18f47192961084b5b0`
and ordered high-row stream SHA-256
`6e4df88330f8a9ee169d3ec105ba08c655f13ae6d5c6a50dbb53f375a1265c10`
as the frozen base calculation, where the sole coefficient is the constant
`R10=x^10`.  Thus every sampled predecessor state either dies at Q7 or has
the same degree-ten cap obstruction on every Q7/Q6 continuation.

The source-frozen run used 66 parallel Box02 lanes under tag
`as_q8state_next_high_samples_20260825T031215Z`.  It ran from 03:12:48Z to
03:13:26Z with return code zero; all 66 state sentinels and the aggregate
sentinel are present, and every stderr file is empty.  The aggregate JSON
has SHA-256 `3d42d327476b0fdaba635588b332af2ab2ed415a17cd758a2a38cbdf2495ee8f`.

This does **not** exhaust either the `3^19` Q8 solution kernel or the
`3^13` Q9 Kuranishi locus, nor combinations of their directions.  The
sample counts are not rates.  The six Q9 Frobenius spectators remain pinned
zero.  No full fixed-cap/all-depth, counterexample, or JC2 claim follows.
