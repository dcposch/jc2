# D7--D9 q1-free divisor-repair hostile review

This case independently reconstructs the branch-P characteristic modes through
weight nine by a direct generalized-binomial expansion.  It does not import
the producer's recurrence engine.  A separate exact `Q[X]` engine verifies
four literal raw `D0=...=D8=0` fixtures, three of them outside q1, and their
weight-nine obstructions.

Verdict: `REPAIR`.  The producer's q1-scoped theorem is true, but q1 is not a
hypothesis: the reviewed reduced prefix, the branch condition
`c2=0 or A|V0`, squarefreeness, and characteristic zero already imply
`D1=...=D9=0 => A|T` at field points.

Replay:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B verify_d7_d9_q1_free.py --check
shasum -a 256 -c SOURCE.sha256
shasum -a 256 -c EVIDENCE.sha256
```

The replay is standard-library only and takes under one second locally.

