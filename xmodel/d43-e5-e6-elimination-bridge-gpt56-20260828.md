# D43 E5/E6 elimination bridge

**Status:** exact algebraic lemma; independent hostile review pending.  This
bridges only the displayed E5/E6/unit equations.  It does not prove any other
upstream template equation, NF-presentation equivalence, all-depth
compatibility, a Keller map, or JC2.

## Setup

Work in the characteristic-zero coefficient algebra containing

```text
r^2 = 3,
a1 = 3+r,       a2 = 3-r,       b = 4,
A1^3 = a1,      A2^3 = a2,
S_M = 7^12/2^6,
```

and localize at `W1*W2`.  Put

```text
C = 243*S_M^3*(a1-a2)^4,
U = A1*W1^4,
V = A2*W2^4.
```

The two literal E5 equations used by `cases/r1_q0_gate.py` are

```text
4*(a1-b)*HM + C*a1^2*U = 0,
4*(a2-b)*HM + C*a2^2*V = 0.                  (E5)
```

The E6 cube tie and nonzero-scale chart are

```text
2^24*HM^3 - 7^48*s1F^3 = 0,
s1F*tSAT - 1 = 0.                            (E6+)
```

All denominators below are units.  Indeed `a1*a2=6`,
`(a1-b)*(a2-b)=-2`, `a1-a2=2r`, and `A_i^3=a_i`; the base is
characteristic zero.

## Elimination of HM

Solving either E5 row for `HM` and equating gives

```text
a1^2*(a2-b)*U - a2^2*(a1-b)*V = 0.
```

Using `r^2=3`, this is a nonzero unit multiple of

```text
E := (9+5*r)*A1*W1^4 + (9-5*r)*A2*W2^4 = 0.       (1)
```

Explicitly,

```text
a1^2*(a2-b) = -6*(5+3*r),
a2^2*(a1-b) =  6*(3*r-5),
```

and multiplication by `r` turns the resulting relation into (1).

Conversely, (1) makes the two displayed formulas

```text
HM = -C*a1^2*A1*W1^4 / (4*(a1-b)),
HM = -C*a2^2*A2*W2^4 / (4*(a2-b))
```

equal.  Defining `HM` by either formula therefore reconstructs both literal
E5 equations.  Since `W1,W2` are units, the reconstructed `HM` is a unit.

Thus, after localization at `W1*W2`, the existential projection of the two
E5 equations from `(HM,W1,W2)` to `(W1,W2)` is exactly the single relation
`E=0`.  E5 fixes only the fourth-power ratio; it does not fix the common W
scale.

## E6 adds no W equation

For every reconstructed `HM`, the explicit choice

```text
s1F = (2^8/7^16)*HM
```

satisfies E6.  It is nonzero, so `tSAT=s1F^-1` satisfies the saturation row.
The other two E6 choices differ by cube roots of unity, already available
after adjoining `zeta_42` if all branches are retained.

Consequently the existential projection of `(E5,E6+)` to the localized W
plane is still exactly

```text
E=0,   W1*W2 != 0.                              (2)
```

There is no separate degree-16 extension obtained by independently adjoining
two pinned W fourth roots: `W1,W2` remain solve coordinates, and the raw J
rows must determine their common scale.

## Solver contract

For a finite D43 candidate whose intended claim includes these template ties,
the exact solver may use either of two equivalent forms:

1. retain `HM,s1F,tSAT` and impose the two literal E5 rows, E6, and the unit
   rows; or
2. impose (2), then reconstruct `HM,s1F,tSAT` by the formulas above and replay
   every literal E5/E6/unit equation.

The second form is smaller and should be used for the 22-support elimination,
provided the reconstruction replay is a mandatory promotion gate.  This
lemma says nothing about template equations other than E5/E6 and units.
