# AS F-only `D=7`: binary-Wronskian top-row compression

**Status: PRODUCER EXACT; PROVISIONAL PENDING DIFFERENT-MODEL REVIEW.**

## Result

Let `k=F3`, and let `C,D` be binary forms of the same degree seven.  If they
are not both zero and `H=gcd(C,D)`, then

```text
{C,D}=C_x D_y-C_y D_x=0
```

if and only if

```text
C=H A^3,   D=H B^3,
deg(H) in {1,4,7},   deg(A)=deg(B)=(7-deg(H))/3.       (1)
```

The quotients may be zero or constant, so (1) includes the proportional and
one-zero degeneracies.  Equivalently, after removing the homogeneous gcd,
the coprime quotient pair consists of Frobenius cubes.

For the AS top-carry gate, `N12={C7,D7}`.  Thus (1) is an exact
componentwise normal form for every `N12=0` point.  Moreover the six free
degree-six coefficients

```text
c6_0,c6_3,c6_6,d6_0,d6_3,d6_6
```

multiply monomials in `F3[x^3,y^3]`; their gradients vanish.  They therefore
do not occur in

```text
N11={C7,D6}+{C6,D7}.                                (2)
```

The apparent six-variable affine solve at degree eleven is a fixed
compatibility test, with fibre size either `0` or `3^6=729`.

## Proof

On the chart `y=1`, write `C=y^7 c(t)`, `D=y^7 d(t)`, where `t=x/y`.
Direct differentiation gives

```text
{C,D}=7 y^12 (c'd-cd')=y^12(c'd-cd')                (3)
```

in characteristic three.  Write `c=ha`, `d=hb` with `gcd(a,b)=1`.  The
common-factor derivative cancels, so (3) vanishes exactly when
`a'b-ab'=0`.  Then `a|a'` and `b|b'`; degree forces `a'=b'=0`.  Hence
`a,b in F3[t^3]`.

Let the coprime homogeneous quotients have degree `n=7-deg(H)`.  If
`n` were not divisible by three, every homogenization of a polynomial in
`t^3` would share a positive power of `y`, contradicting coprimality.
Thus `3|n`, and perfection of `F3` makes both quotients cubes.  This gives
`deg(H)=1,4,7`.  Conversely, differentiating `H A^3,H B^3` leaves
`A^3 dH,B^3 dH`, whose wedge is zero.  The statement about (2) follows
because derivatives of every polynomial in `x^3,y^3` vanish.

The same proof gives the general perfect-field lemma for characteristic
`p` and common degree `d` with `p` not dividing `d`: the Wronskian vanishes
exactly when the coprime quotients are `p`-th powers, so the gcd degree is
congruent to `d` modulo `p`.

## Replay and scope

`cases/as_fonly_binary_wronskian_char3_20260824/replay.py` verifies the
generic dehomogenization identity coefficientwise, all three generic
degree-seven strata, a nonzero nearby control, and exhaustively checks the
Euclidean converse core on all nonzero pairs of univariate polynomials of
degree at most four over `F3`.

This lemma classifies only the pure top row.  It does not assert that any
stratum meets the earlier accepted-digit equations, passes `N11`, or lifts
through lower rows.  It gives no all-depth, characteristic-zero, no-lift,
counterexample, or JC2 conclusion.
