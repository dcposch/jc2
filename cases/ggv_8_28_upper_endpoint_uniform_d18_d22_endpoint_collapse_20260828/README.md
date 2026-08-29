# Uniform full-mode endpoint collapse through D22

This packet continues the frozen uniform branch-P characteristic cascade
from D17 through the literal upper endpoint.  Standard-library exact rational
arithmetic proves

```text
D18: c18=0, P18 in (A^2)
D19:          P19 in (A^2)
D20: c20=0, P20 in (A^2)
D21:          P21 in (A^2)
```

where every defect and numerator is serialized in `RESULT.json`.  The full
weight-22 characteristic coefficient has the corrected shape

```text
g22 = P22/A^2 + H22,
```

with `H22` polynomial.  It is not purely `A^-2`.  Nevertheless, because no
raw `G22` exists, the complete raw endpoint row is `D22=-L22(g22)`, and every
term of this polynomial is divisible by `A=X^4-1`.  The eighteen literal
endpoint generators require the whole polynomial identity `D22(X)=1`.
Thus the uniform field-valued endpoint stratum is empty.

The checker pins the authoritative 303-variable/513-generator source,
replays the frozen D16/D17 producer, certifies the exact raw G18--G21 windows,
and exercises live D18--D22 mutations.  The D22 mutation has

```text
D22 = 12*X - 96*X^5 + 84*X^9
    = (X^4-1)*(-12*X+84*X^5),
```

after every D4--D21 literal row has vanished.  All mutations are checked
against every serialized generator and include scaling regressions.

Replay:

```text
python3 -B verify_uniform_d18_d22.py --check
shasum -a 256 -c SOURCE.sha256
shasum -a 256 -c EVIDENCE.sha256
```

This is a field-point emptiness result for the pinned uniform branch-P
fixture.  It is not a scheme-theoretic unit certificate or, by itself, a
proof of JC2.  No CAS, AWS, or `jc2-lean` state is used.
