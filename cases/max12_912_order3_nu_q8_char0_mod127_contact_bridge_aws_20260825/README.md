# Corrected-Q8 characteristic-zero/mod-127 contact bridge producer

This fail-closed AWS-only case checks the narrow repaired no-merger items 6
and 7 at the boundary-local tier.  It does not compute or claim a global
component grouping.

`producer.py` loads the hash-pinned reviewed quotient source and frozen
mod-127 full-contact source, emits the exact six divided rows over
`Z_(127)`, checks every scalar denominator, computes the full
characteristic-zero contact in `Q[v]/(Q8)`, reduces all eight coordinates,
and reduces the full relative `8 x 8` determinant to the frozen mod-127
unit.  Its scheme manifest keeps `w=0`: the localizer is
`x5*(x3-2*x5)`, not `w*x5*(x3-2*x5)`.

`independent_replay.py` does not import the producer.  It reruns the frozen
mod-127 endpoint from its own source, directly reduces every exact rational
coefficient recorded by the producer, and compares the coordinates, source
rows, and determinant.

Heavy or uncertain-duration execution is restricted to AWS.  Example:

```sh
sh cases/max12_912_order3_nu_q8_char0_mod127_contact_bridge_aws_20260825/run_remote.sh \
  /home/ubuntu/jc2q8/repo /home/ubuntu/jc2q8/out \
  q8_char0_mod127_contact_bridge_r6d_v1
```

Acceptance requires `runner.rc=0`, both JSON payloads to say `PASS`, exact
source and output hashes, and empty non-timing error streams.  The intended
interpretive successor is the arithmetic formal-IFT statement
`completed local source = R[[w]]`; that statement remains review-charged.
