# Genuine q1-compatible branch-P prefix: D7 split and D9 repair

This packet independently continues the reviewed general branch-P prefix

```text
F1=A^2 V0,
F2=(V0^2+A^2 Z)/4,
F3=(V0 Z+A T)/8
```

on the prioritized q1 locus `V0=A'R0+2AR0'`, `deg R0<=4`.  It uses exact
`fractions.Fraction` arithmetic and the coefficient recurrence
`F*y'=e*F'*y`; all ten characteristic modes born at weights
`2,4,...,20` are retained.

The first change from the frozen `V0=1` slice is D7.  If
`C=gcd(A,V0)=gcd(A,R0)`, `A=CB`, `V0=CV1`, and `T=BU`, the exact c2-zero
D7 condition is

```text
C | U*(64F4-Z^2-2UV1).
```

The packet freezes the exact D8 successor and a live raw-window mutation
with `C=X-1` that has `A` not dividing `T` yet satisfies every direct row
`D0..D8=0`.  D9 then repairs the escape on every q1/c2 branch: at field
points, `D1=...=D9=0` forces `A|T`.  `TARGET.json` freezes both rootwise
D9 certificates and the next square-defect target.

Replay:

```bash
cd cases/ggv_8_28_upper_endpoint_q1_prefix_d7_d8_target_20260828
python3 -B verify_q1_prefix_target.py --check
shasum -a 256 -c SOURCE.sha256
shasum -a 256 -c EVIDENCE.sha256
```

Maximum scope: exact characteristic polynomiality through D9 for the
reviewed general prefix, direct raw-window replay of the frozen fixture
through D8, its exact D9 first residual, and the field-point theorem
`A|T` on the full q1/c2 cover.  This is not an endpoint proof.  The q1
restriction itself requires its reviewed D23 licensing row and is not
implied by `D1..D22`.  The old 513-row JSON hardcodes `V0=1` and is
deliberately not used as general-prefix evidence.
