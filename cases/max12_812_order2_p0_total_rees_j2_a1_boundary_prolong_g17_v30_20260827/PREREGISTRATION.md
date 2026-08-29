# V30 preregistration: prolong the rational ordered-a1 boundary ray to grade 17

Date: 2026-08-27

V28's normalized grade-16 obstruction factors as

`(1 - 48*t^5)/(384*t^4)`

along the sparse grade-15 family.  Undoing the weighted normalization gives
the rational sigma-homogeneous ray

```text
a1=48*u^5, aa0=48*u^6, cs1=8*u^3,
ec3=384*u^8, rs2=-32*u^4,
```

with `rho=0` and all other registered coordinates zero.  Direct exact-Q
substitution kills all 49 rows through grade 16.  Since each row is
sigma-homogeneous, it suffices to set `u=1` and use the rational point
`(a1,aa0,cs1,ec3,rs2)=(48,48,8,384,-32)`.

V30 reconstructs the seven actual-total rows to grade 17, bridges grades
10--15 to V23R1 and grade 16 to V28 byte-for-byte as polynomials, and solves
the seven affine equations for every new weight-17 coordinate.  Emit an exact
extension on consistency or a rational dual combination equal to one on
inconsistency.  Run independently over Q and F_65521 on AWS, with 400 GiB
virtual-memory and 30-minute compiler/engine caps.  This is a finite-prefix
prolongation only, not a formal arc or JC2 conclusion.

