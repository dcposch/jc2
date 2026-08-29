# V36 preregistration: grade-19 unit obstruction on the V34 orbit

Date: 2026-08-27

V34 is the normalized six-coordinate ordered-`a1`, `rho=0` degree-five
scheme through grade 18.  V35 found that its rational sigma-orbit
representative has all grade-19 rows zero except

```text
Tg19_7 = -7077888.
```

V36 tests the stronger scheme-theoretic statement.  It freezes all seven
V35 rows in exact Q and F65521, verifies their modular shadow and sigma
homogeneity, and requires that no sigma-weight-19 source variable occurs.
It then normalizes `a1=48`, restricts `Tg19_7` to the V34 six-coordinate
support, and independently asks Singular in each field for:

1. a nonzero normal form modulo the V34 grade-18 standard basis; and
2. the unit ideal after adjoining that grade-19 row.

Both conditions, together with absence of a weight-19 receiver, eliminate
the entire V34 degree-five scheme at grade 19.  This does not eliminate
ordered-`T-a1` solutions outside the V32/V34 six-coordinate support.
