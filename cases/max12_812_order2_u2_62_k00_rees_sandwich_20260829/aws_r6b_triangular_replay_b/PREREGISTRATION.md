# K00-REES-SANDWICH triangular-coordinate replay

- Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`.
- Registered lane: `K00-REES-SANDWICH-TRIANGULAR-REPLAY-B-R6B-20260829`.
- Registered host: campaign r6b, instance `i-0f089e64c378f5da3`.
- Source: original frozen unloaded prelude SHA-256
  `5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a`.
- Charged producer result: clean V2 output/result manifest
  `V2_RESULTS.sha256`, SHA-256
  `b4ecb6c3f02c4167610398b2b51e89e5d978121a7d37b4a282a87d8aeb9eb72e`,
  reports candidate theorem `J^5 subset I` with witness `f5^4 notin I`.
- V1 remains wholly quarantined and is not an input.
- Replay attempt A, packet hash
  `10fbaeb91137b3bd1b035de912edd847b21a461e9a8184ed5e04022fcad9c8c4`,
  was correctly rejected by the generic diagnostic firewall because `IN` is
  a reserved Singular name.  Its frozen rejection manifest has SHA-256
  `b4a3fad463e7ff843bf764867eba9af773e4ed39a733ed89105b4e1690114a5d`.
  No line from attempt A is mathematical input.  Attempt B changes only that
  identifier to the unreserved `transformedRows` and starts in a new remote
  directory/process.

## Independent presentation

Use the exact triangular automorphism

```text
d0=e0+2S+S^2,
d1=(e1+(1+S)T)/8,
d2=e2+S+16T^2,
d3=T, d4=S, d5=e5+2T.
```

Carry the four literal `f` generators and all seven literal rows together
through this map and require that the first four images are exactly
`e0,e1,e2,e5`.  A mutation replacing `16T^2` by `15T^2` must be detected.
Build a fresh exact-Q `liftstd` basis of the transformed seven-row ideal,
replay every basis column into the original transformed rows, and reduce all
56 canonical generators of `(e0,e1,e2,e5)^5`.  Every remainder must vanish.
Independently reduce `e5^4`; its exact normal form must be nonzero and is
serialized.  These two endpoints establish 5 as the least exponent without
using the V2 standard basis, reductions, witness file, or fifth-power lifts.

The lane also reruns the corrected source-bundled initial-ideal strictness
check in a separate process.  Before evidence, the same generic validator
must reject the planted undefined-symbol/fake-PASS regression with status 41.

## Caps and typing

- Negative control: 30 wall/CPU seconds, 256 MiB aggregate RSS.
- Triangular replay: 1,800 wall/CPU seconds, 32 GiB aggregate RSS.
- Initial strictness replay: 120 wall/CPU seconds, 1 GiB aggregate RSS.
- `CAPRUN/v1`, closed stdin, 0.10-second RSS sampling, five-second TERM grace.
- Exact characteristic zero only.  Any cap, generic Singular diagnostic,
  explicit failure marker, lifecycle error, missing unique PASS endpoint, or
  failed mutation is `NO VERDICT`.

No quartic elimination is recomputed.  No loaded, cell, arc, closure, map, or
JC2 claim is made.
