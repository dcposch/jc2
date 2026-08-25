# Preregistration — B9 complete fixed-D12 next digit modulo 729

Date: 2026-08-25

Consume the exact B9 `Z/243` parent replay at source SHA-256
`f1b50bb2c3e21369da205ebcf1ba028eede20c89d5ad863253fdfec4d6d28c5d`.
For its literal integer pair `(P5,Q5)`, introduce every monomial of total
degree at most twelve in each fresh order-243 output digit `(R,S)`.  Retain
all determinant monomials of total degree at most 22 and solve exactly over
`F_3`

```text
(det J(P5,Q5)-1)/243 + L_G(R,S) = 0 mod 3.
```

The compiler must include all 182 columns (including zero/spectator columns),
all 276 rows, exact affine rank and consistency, and an original-row left-null
certificate if inconsistent.  If consistent, reconstruct one integer pair
and literally verify every determinant coefficient modulo 729, both total and
partial `y`-degree caps, and reduction to B9.  The uncorrected parent is the
mandatory negative control.

This is one next-digit gate over one displayed `Z/243` point.  It is not the
complete earlier fibre, an all-depth branch, a characteristic-zero map, a
counterexample, a maximum-twelve theorem, or JC2.
