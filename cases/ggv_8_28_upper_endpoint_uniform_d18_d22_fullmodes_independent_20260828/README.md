# Independent uniform endpoint audit, D18--D22

This packet independently continues the frozen full-mode D16/D17 upper
branch-P packet through the endpoint.  It proves, for the authoritative
303-variable/513-generator fixture, that

```text
D18: c18=0, R18=A^2*h18
D19: R19=A^2*h19
D20: c20=0, R20=A^2*h20
D21: R21=A^2*h21,
```

and then the nine-mode `g22` has pole order at most two.  Consequently
`D22_raw=-L22(g22)` is divisible by `A=X^4-1` and cannot equal the charged
target `1`.

The checker uses an independent exact Laurent recurrence and an independent
dense `Q[X]` replay of all 513 serialized generators.  It pins and enforces
the literal G18--G21 degree windows, includes row-basis rank certificates,
four first-failure mutation families, and an independent endpoint-sign
diagnostic.

Replay:

```text
python3 -B verify_uniform_d18_d22.py --check
shasum -a 256 -c SOURCE.sha256
shasum -a 256 -c EVIDENCE.sha256
```

This closes only the frozen fixture.  It does not assert that all remaining
JC2 branches have already been transported into it.  No CAS, AWS, or Lean
state is used.
