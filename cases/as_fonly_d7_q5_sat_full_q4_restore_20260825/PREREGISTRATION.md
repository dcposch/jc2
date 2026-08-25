# Constructive full-Q4 restoration of replayed Q5 SAT models

Consume exact Boolector SAT models of the complete 197-row aligned Q5
formula which also pass the source-pinned `[x^2 y^2]` Q4 Cartier row.  Run
the reviewed nested-integer Q5 replay first.  Then solve all five degree-four
rows constructively by adjoining homogeneous degree-five fourth-digit
polynomials `(H5,J5)` with coefficient 81.

For a replayed pre-restoration row `g=(g0,...,g4)` over F3, use the fixed
section

```text
H5 = 0,
J5 = g0*y^5 - g1*x*y^4 + g3*x^3*y^2 - g4*x^4*y.
```

Its divergence has row `-g` exactly when the unique Cartier coordinate
`g2` is zero.  The replay must reconstruct the full integer polynomials,
verify all five degree-four determinant coefficients modulo 243, verify the
recursive/divergence and literal determinant rows agree, and emit the full
map support.  The zero-restoration negative control must fail whenever the
pre-restoration row is nonzero.

Strict scope: this restores the complete displayed Q4 row only for the exact
input models.  It does not restore Q3 through Q0, prove a complete map modulo
243, give an all-depth lift, or imply JC2.  All substantive execution is
AWS-only.

