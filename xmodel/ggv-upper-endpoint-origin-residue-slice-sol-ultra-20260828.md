# Exact origin-residue exclusion on the symmetric deep slice

Date: 2026-08-28  
Author: Sol Ultra / coordinator  
Status: **EXACT PROVISIONAL FIXED-SLICE THEOREM; GENERALIZATION REFUTED**

## 1. Result

On the `lambda=0`, `c2!=0`, exact-`D=0` branch, fix

```text
A=X^4-1,  Q=e=F8=0,  r=0.                            (1)
```

Every literal q7/q9/q11/q13 solution (q5 and q15 are automatic here) that
makes the complete characteristic coefficient `G15` polynomial has

```text
D22[X0]=0.                                             (2)
```

The raw endpoint requires `D22[X0]=1`, so this entire fixed slice is empty.
The proof is an exact residue identity, not a sampled rank computation.

This does **not** generalize to arbitrary `Q`.  An independently found exact
`Q=X` mutation has legal q7--q15 primitives and legal `G11,G15`, with nonzero
origin pairing; after a quadratic scalar extension it reaches origin target
one.  That mutation is not yet a full endpoint survivor because the other
`G` windows, the four-root endpoint equations, and remaining raw rows have
not been imposed.

## 2. Complete q parameterization on the slice

Let

```text
T5(d)=(5A'd+2Ad')/2.
```

All literal solutions may be written

```text
f   =4T5(a0+a1 X+a2 X^2),              F7=A f,
F9  =4T5(b0+b2 X^2+b3 X^3+b4 X^4),
F11 =4T5(A(k0+k2 X^2))/A,
F13 =4T5(A^2 ell13)/A^2.                              (3)
```

The missing `X` coefficients in the q9 and q11 primitives are forced by the
raw constant floors of `F9` and `F11`; the displayed polynomials have exactly
the authoritative windows.  Equations `(3)` make q7--q13 exact by the
reviewed primitive theorem, while q15 vanishes because `(1)` and `r=0` kill
every term of its reviewed formula.

## 3. Characteristic residue and endpoint identity

Let `c2,c4,c6,c8` be the relevant even characteristic modes.  A direct
fractional-series reconstruction gives the complete coefficients

```text
G11=(3/2)A^2F11+(5/4)c2*A*F9+c4*F7,

G15=(5/4)c2*A*F13+c4*F11
     +(1/A)((3/4)c6*F9+(1/2)c8*f).                    (4)
```

Modes `c10,c12,c14` have no contribution at these weights because
`F5=F3=F1=0`; later modes are unborn.  Divide the pole numerator in `(4)` by
`A`, and write `R` for its remainder.  Exact symbolic division gives

```text
R[X1]=10(3c6*b2+2c8*a2),

5*D22[X0]+6*F7[X0]*R[X1]=0.                           (5)
```

Polynomiality of `G15` forces `R=0`, so `(5)` proves `(2)`.  The cancellation
of the `c4` terms is the expected functional-dependence cancellation; the
load-bearing condition is the `X` coefficient of the negative-power mode.

## 4. Frozen checker

```text
cases/ggv_8_28_upper_endpoint_origin_residue_slice_20260828/
  verify_origin_residue_slice.py
```

SHA-256:

```text
de371953d4bc22da7cfc39c4e94221097eac7612b7b4a8b44afe0fd14ecb76e0
```

Expected marker:

```text
PASS_EXACT_ORIGIN_RESIDUE_SLICE_EXCLUSION
```

The checker pins the authoritative recurrence implementation, independently
rebuilds the fractional characteristic through weight 15 in a symbolic
Laurent-in-`A` ring, verifies all raw floors and q parameterizations, performs
the exact division, and proves `(5)` as a polynomial identity.

No general-`Q`, full endpoint, other-lambda/D/`c2`, Keller, or JC2 result is
claimed.  The live target is the arbitrary-`Q` odd fiber intersected with all
remaining `G` windows and the 15-coordinate four-root endpoint system.
