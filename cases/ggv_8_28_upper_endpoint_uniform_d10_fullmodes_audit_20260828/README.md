# Uniform full-mode cascade through D11: independent audit and extension

This packet independently replays the provisional full-fixture D8/D9 cascade
from the pinned 513-generator branch-P source, then advances it through D10
and D11 using only exact `fractions.Fraction` arithmetic.

On characteristic-zero field points, after

```text
T=A*V,
F4=V/16+Z^2/64+A^2*R,
c6=0,
```

the exact next defect is

```text
Delta5=F5-R/2-Z*V/64.
```

D10 forces `A|Delta5` and has no additional mode kill.  Writing
`Delta5=A*S`, D11 first forces `A|S` and then forces `c10=0`.  Thus

```text
F5=R/2+Z*V/64+A^2*Q,
c10=0.
```

The packet retains all nine characteristic modes through `c20`.  Two literal
gauge points requiring `c16=+3/8` and `c16=-3/8` are replayed against every
one of the 513 serialized generators, preventing regression to the invalid
five-mode truncation.  A separate literal mutation detects omission of the
`Z*V/64` term.

Replay:

```text
python3 -B verify_uniform_d10.py --check
sha256sum -c SOURCE.sha256
sha256sum -c EVIDENCE.sha256
```

No CAS, AWS, floating point, interpolation, or root evaluation is used.  The
result is a field-radical prefix theorem only, not endpoint emptiness or a
Jacobian-conjecture conclusion.
