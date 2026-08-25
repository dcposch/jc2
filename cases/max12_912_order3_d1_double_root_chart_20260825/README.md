# D1 double-root chart checkpoint

This is the first exact package for the sole projective point left by the
squarefree order-20 theorem.  It is deliberately separate from the global
slope compiler.

The moving common cubic has the étale axis/cusp coordinates

```text
p=-3*a^2,  c=2*a^3+h,
K=(z-a)^2*(z+2*a)+h,
Delta=-27*h*(4*a^3+h).
```

The Jacobian at `(a,h)=(1,0)` is `-6`, so `a` is the discriminant-axis
coordinate and `h` is transverse.  Every degree-at-most-two normal polynomial
is represented, without a slice, by its Hermite data
`(P(a),P'(a),P(-2*a))`; this is applied separately to `Q` and `R`.

At the normalized centre, put `L=z-1`, `U=L+3`,
`K0=L^2*U`, and `N=L*U`.  Then `N^2=K0*U`.  The exact singular leading
cancellation

```text
Q1=q*N,  R2=q^2/3
```

makes the weight-`3 beta` pure `f^(4/3)` tail polynomial.  The V3 structural
check proves that, after arbitrary next corrections `Q2,R3`, the next pure
common numerator modulo `K0` is

```text
(q^4/243)*(5*L^2+18*L+15).
```

It is nonzero and nonconstant, so neither a row-3 numerator (a multiple of
`K0`) nor a scalar row-6 numerator removes it.  This is an exact successor
obstruction for the displayed nilpotent ray, not yet a classification of all
tropical rays: interactions with the weight-six `kbar` layer and arbitrary
target coincidences remain to be folded into one theorem.

Independently, `compile_double_root_exact.py` substitutes all six normal
directions into the full eight charged ordinary tails, with no normal-degree
truncation.  Box03's `dp` standard basis completed with 101 elements and
vector-space dimension 125.  Together with the reviewed reduced-support
theorem this gives a finite-colength exceptional-fibre local algebra, but no
finite loaded-Rees determinacy bound is inferred yet.  The independent r6d
`lp` basis was still running at freeze time.

The failed Python/Sympy and V2 Singular attempts are documented in
`PREREGISTRATION.md`; neither is evidence.  V3 is accepted only because both
hosts returned rc 0, empty stderr, and exactly one fail-closed PASS marker.
