# V34 preregistration: symbolic grade-18 cut of the V32 curve

Date: 2026-08-27

V32 found a proper dimension-one ideal on the normalized ordered-`a1`,
`rho=0` support

```text
a1=48; keep ell2,cs1,rs2,aa0,ee1,ec3; kill every other source coordinate.
```

V33 showed that one sigma-scaled rational point of this curve fails at grade
18 only in `Tg18_6`.  V34 asks the stronger symbolic question: append the
restriction of the actual-total `Tg18_6` polynomial to the complete V32
standard basis and decide the resulting ideal over exact Q and independently
over F65521.

Registered outcomes:

- `UNIT_IDEAL=1`: the entire six-coordinate V32 curve is removed at grade 18.
- `UNIT_IDEAL=0, DIM=0`: some grade-18 points remain, but only a finite
  algebraic scheme on this support.
- `UNIT_IDEAL=0, DIM>=1`: a positive-dimensional part remains.

All outcomes concern this support and the literal rows through grade 18 only.
They do not decide the full ordered-`T-a1` chart.  The known `aa0=0` branch is
a mandatory negative control for membership of `Tg18_6` in the old ideal:
after `ell2=l`, it evaluates to `41472/l`, with `l^5=243/2`.
