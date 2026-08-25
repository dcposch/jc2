# Preregistration: finite unloaded-overlap formal-IFT exclusion

Date: 2026-08-25  
Status: **FROZEN BEFORE CAS**

Let `X` be the exact six-row approximate-cubic source and let its raw
special-fibre overlap be

```text
A3: w=x1=x3=x5=0,
```

with finite coordinates `(c,d2,d4)`.  This producer tests the following
formal-local argument, independently of global saturation.

1. Restrict the special-fibre Jacobian to `A3`.  The tangent columns
   `(c,d2,d4)` must vanish, while the six-by-three normal block in
   `(x1,x3,x5)` must have rank three at every geometric point.  Certify the
   latter by a unit ideal of all three-by-three minors.  Since `A3` is a
   smooth threefold contained in the special fibre, the equal-dimension
   regular-local argument then makes the entire special-fibre local germ
   equal to `A3` at every finite point.
2. Append the `w`-derivative column to that normal block.  All four-by-four
   minors must vanish at `d2=d4=0`, and their common zero set must have no
   point on either `D(d2)` or `D(d4)`, certified by two inverse-variable unit
   ideals.  Thus any formal branch not contained in `w=0`, including a
   ramified branch, can specialize only to `(d2,d4)=(0,0)`.  The separate
   first-order tangent producer records the intermediate false candidate
   `(4,2)` and its nonzero `e7` residual.
3. At `(d2,d4)=(0,0)`, the `(e1,e3,e5)` Jacobian in ordered variables
   `(x5,x3,x1)` must be the triangular matrix

   ```text
   [  4/9      0     0 ]
   [-20/27    4/9    0 ]
   [ 40/81   -4/9   4/9]
   ```

   with determinant `64/729`, uniformly in finite `c`.
4. Source ideal-membership checks must justify the formal solution estimates

   ```text
   x1 in w*(d2,d4),
   x3,x5 in w*(d2,d4)^2.
   ```

   After substituting the unique formal solution and dividing `e2,e4` by
   `w`, their linear parts in `(d2,d4)` must be

   ```text
   G2_lin = (4/9)*d4,
   G4_lin = (4/9)*d2-(16/27)*d4,
   ```

   whose determinant is `-16/81`.  The second formal IFT then forces
   `d2=d4=0`, and the exact sheet
   `d2=d4=x1=x3=x5=0` is the unique formal source germ.

Acceptance requires two independent AWS engine/order lanes, literal source
pins, all ideal/unit/matrix identities, no diagnostics, and fail-closed
replay.  The intended conclusion is only: no finite point of this overlap is
a landing of the selected `D(w*x5*(x3-2*x5))` open.  Projective/coefficient
infinity, Taylor/terminal reconstruction, other leaves, maximum twelve,
Keller pairs, and JC2 remain charged.
