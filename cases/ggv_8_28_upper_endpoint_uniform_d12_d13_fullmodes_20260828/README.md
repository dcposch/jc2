# Uniform full-mode cascade through D13

This exact desk packet continues the frozen uniform D8--D11 cascade by two
rows.  On characteristic-zero field points, define

```text
Delta6=F6-Q/2-R*Z/8-V^2/256.
```

Then D12 forces `A|Delta6`, with no mode kill.  Writing `Delta6=A*S`,
D13 forces `A|S`, again with no mode kill.  Therefore

```text
F6=Q/2+R*Z/8+V^2/256+A^2*T.
```

The full nine-mode schedule is retained.  In particular `c12` is replayed
as the exact additive `G12[X^0]` gauge, while `c14,c16,c18,c20` remain live
forced rational continuation coordinates.

Replay:

```text
python3 -B verify_uniform_d12_d13.py --check
shasum -a 256 -c SOURCE.sha256
shasum -a 256 -c EVIDENCE.sha256
```

Only Python standard-library rational arithmetic is used.  This is a
field-radical prefix result, not endpoint emptiness or a JC2 conclusion.
