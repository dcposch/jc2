# V32 preregistration: exact six-coordinate grade-17 support solve

Date: 2026-08-27

V31 finds that the grade-17 obstruction at the rational grade-16 point can be
canceled to first order, with `a1=48` fixed, using only the coordinates

```text
aa0, cs1, ec3, ell2, ee1, rs2.
```

V32 restricts all 56 ordered-`a1`, `rho=0` actual-total rows through grade 17
to precisely this support, computes a complete reduced standard basis, and
decides whether the restricted ideal is the unit ideal.  Run over exact `Q`
and independently over `F_65521` on AWS.  Export the full reduced basis and
normal form of one.

`UNIT_IDEAL=0` only proves that this restricted algebraic prefix is nonempty;
it does not produce a characteristic-zero point or a formal branch.
`UNIT_IDEAL=1` kills only this six-coordinate support.

