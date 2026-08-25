# Preregistration — normalized `(9,12)` common-cubic gate

Consume the complete normalized mod-`3^11` family over the displayed B9
mod-243 parent.  Reimpose every determinant coefficient and require, without
division by three,

```text
P9 = P_(0,9) H^3,   Q12 = Q_(0,12) H^4,
H = y^3 + h1*x*y^2 + h2*x^2*y + h3*x^3,
h1,h2,h3 = 0 mod 3.
```

The two displayed leading coefficients are required to be units.  The monic
normalization is integral because the residue common cubic is `y^3`.
All products use 64-bit modular gates reduced after each multiplication.
SAT requires literal determinant and common-cubic replay; UNSAT requires a
checked certificate.  This is one fixed-parent finite-depth necessary locus.
