# AS gauge growth at p=3, depth five: exact minimum seven

**Producer verdict: THE EXACT EQUAL-CAP MINIMUM AT `(p,n)=(3,5)` IS
SEVEN.**

- Date: 2026-08-24
- Arithmetic: exact integers reduced coefficientwise modulo `3^5=243`
- Support grammar: total-degree simplices only
- Upper-bound engines: integer-only Python and independent Singular
- Lower-bound input: hostile-review-confirmed depth-four minimum seven
- Required hostile review of this new depth-five point: not yet run

## 1. Verdict and lower-bound provenance

The point below proves `B_(3,5)(7,7)` is nonempty.  Conversely, reduction
modulo `3^4=81` sends every point of `B_(3,5)(D,D)` to a point of
`B_(3,4)(D,D)` without increasing either the map cap or the canonical gauge
cap.  The frozen depth-four producer and its different-model hostile review
prove

```text
B_(3,4)(D,D) is empty for D<=6,
B_(3,4)(7,7) is nonempty.
```

Therefore

```text
min {D : B_(3,5)(D,D) is nonempty} = 7.                 (1)
```

This sharply falsifies the proposed value
`(n-1)(p-1)+1=9`.  It does not assert that the cap remains seven at depth
six or at any later depth.

Lower-bound sources in the charged tree:

- `xmodel/as-gauge-growth-p3-depth4-gate-20260824.md`;
- `xmodel/as-gauge-growth-p3-depth4-review-grok-20260824.md`;
- `cases/as_gauge_growth_p3_depth4_20260824/`.

## 2. Exact base-three gauge digits

Work in `(Z/243Z)[x,y]`.  Put

```text
b = x^5,
c = 2x^2y,
d = xy^2 + x^5 + 2x^7,
e = 2x + xy + 2x^2 + x^4y + 2x^5,

f = y+y^2+2xy+y^3+2xy^2+xy^3+x^3y^2+2x^4y+x^6y+x^7,

g = x+x^2+2xy^2+2x^2y+2xy^3+x^2y^2+2x^2y^3
      +x^4y+x^5+2x^2y^4+2x^7,

h = y+y^2+2xy+y^4+2xy^4+xy^5+2x^5y+2x^6y.
```

Define the identity-branch gauge

```text
A = x + 9c + 27e + 81g,
B = y + 3b + 9d + 27f + 81h.                           (2)
```

Reduced modulo 243, its full supports are

```text
A = 162x^7 +162x^2y^4 +135x^5 +108x^4y +162x^2y^3
      +81x^2y^2 +162xy^3 +180x^2y +162xy^2 +135x^2
      +27xy +136x,

B = 45x^7 +189x^6y +162x^5y +81xy^5 +12x^5 +54x^4y
      +27x^3y^2 +162xy^4 +27xy^3 +81y^4 +63xy^2
      +27y^3 +216xy +108y^2 +109y.
```

Thus `deg A=deg B=7`, `A=x mod 3`, and `B=y mod 3`.

## 3. Exact bounded map

Let

```text
S_5(A)=1+3A^2+9A^4+27A^6+81A^8,
P=A-A^3,
Q=B S_5(A).
```

The exact reduced supports are

```text
P = 162x^6y +162x^2y^4 +135x^5 +54x^4y +162x^2y^3
      +81x^4 +162x^3y +81x^2y^2 +162xy^3 +80x^3
      +180x^2y +162xy^2 +135x^2 +27xy +136x,

Q = 81x^7 +216x^6y +162x^5y +81x^3y^3 +81xy^5 +12x^5
      +63x^4y +81x^3y^2 +81x^2y^3 +162xy^4 +27xy^3
      +81y^4 +165x^2y +63xy^2 +27y^3 +216xy
      +108y^2 +109y.
```

Hence `deg P=deg Q=7` and

```text
(P,Q)=(x-x^3,y) mod 3.
```

## 4. Orientation and the two determinant checks

For `D(A)=1-3A^2`, the exact truncated-geometric identity is

```text
D(A)S_5(A)=1 mod 243.
```

Therefore `B=QD(A)` and the point has the frozen orientation
`C_3 o (A,B)=(P,Q)`.  The two replay engines independently verify both

```text
det J(A,B)=1 mod 243,
det J(P,Q)=1 mod 243.                                  (3)
```

The second equality is checked by direct differentiation, not merely
inferred from the first.

## 5. What changed relative to the cap-eight motif

The earlier clean cap-eight survivor used the cyclotomic carry
`(1-y)(1+y+y^2)=1-y^3`.  It remains a useful structural control, but it is
not minimal.  Cap seven survives on a different first-digit component:
`a=0`, `b=x^5`.  The nonzero Frobenius-horizontal term `b` opens a carry
channel that the clean `a=b=0` component lacks.  This is why the clean
component's final high bracket obstruction did not give a global cap-seven
lower bound.

The present gauge is a finite bounded witness.  Its many lower coefficients
record carry absorption; no simplicity or uniqueness is claimed.

## 6. Replay

From the case directory run

```sh
python3 replay_n5_d7_minimum.py
Singular -q audit_n5_d7_minimum.sing
shasum -a 256 -c MANIFEST_n5_d7_minimum.sha256
```

The Python producer reconstructs every product and derivative using only
integer dictionary arithmetic.  Singular independently computes in
`(Z/243Z)[x,y]`.  Both assert the displayed supports, all four degrees, the
truncated inverse, orientation, and both determinants.

## 7. Refusal scope

This result makes no claim of:

- survival at depth six or any later depth;
- compatibility of bounded points across depths;
- a polynomial or Tate-algebra lift;
- failure of any polar-conductor no-lift theorem;
- an `A_infinity` identification;
- any implication for the plane Jacobian conjecture.

Equation (1) is an exact statement only about the frozen finite system at
`p=3,n=5`.
