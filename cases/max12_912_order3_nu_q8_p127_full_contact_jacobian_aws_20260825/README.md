# Full corrected-Q8 contact Jacobian over `F_127[v]/(Q8bar)`

This AWS-only gate works in the finite étale algebra

```text
A = F_127[v]/(Q8bar(v)).
```

It imports the pinned approximate-cubic quotient compiler and reconstructs
the full corrected contact section.  The three odd tangent coordinates are
solved inside `A` from the same divided rows; the six divided source rows,
the `v`-definition row, and the localization row are then evaluated at the
section.  The full relative `8 x 8` Jacobian is taken with respect to
`(c,d2,d4,x1,x3,x5,inv,v)` at fixed `w=0`.

Acceptance requires every row to vanish in `A`, every displayed contact
denominator to be a unit, the full determinant to be a unit (`gcd=1` with
`Q8bar` and nonzero norm), and the old wrong-`x1` slice to fail.  This is a
full-source boundary-local statement, deliberately distinct from the plane
projection condition `H_v != 0`.  It does not prove that the interpolated
plane curve lifts to a global quotient component or that any characteristic-
zero components cannot merge.

All substantive execution is AWS-only.

