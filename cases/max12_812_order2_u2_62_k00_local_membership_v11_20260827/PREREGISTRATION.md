# Preregistration: exact K00 local-ring membership V11

Date: 2026-08-27

Status: **FROZEN LOCAL STANDARD-BASIS TEST; NO RESULT AT REGISTRATION.**

V8 proves that unloaded `r7` is not in the global polynomial ideal generated
by `r1,...,r6` on `D(C6)`.  V9 proves compatible multiplier jets through
transverse degree 7 at the normalized K00 germ.  V11 directly asks the
distinct local question

```text
r7 in (r1,...,r6) Q[d0,...,d5]_(d0,...,d5) ?
```

after the registered faithfully flat weighted normalization `C6=1`.

The exact-Q AWS lane uses Singular's negative degree reverse local ordering
`ds` and `liftstd`.  Before touching the charged rows it must pass two toy
controls in the same ring:

```text
d1 in ((1+d0)*d1) locally, but not globally;
d2 not in ((1+d0)*d1) locally.
```

The positive toy must return and replay the local unit identity with unit
`1+d0`.  This freezes the intended semantics: Singular is computing in the
localization at the maximal ideal, not silently reusing global membership.

For the charged ideal, `liftstd(I,T)` must replay `G=I*T`.  If the local
normal form of `r7` is zero, `lift(G,r7,U)` must provide a diagonal unit and
the producer must save/replay

```text
r7*U = I*(T*H),  U(0) != 0.
```

This unit-denominator identity is the exact certificate of local membership.
If the normal form is nonzero, save its lowest transverse homogeneous piece
and hash; the next cumulative Macaulay cutoff must independently reproduce
that obstruction degree.

A zero normal form would explain arbitrarily long compatible unloaded jets
while remaining consistent with V8 global nonmembership.  A nonzero normal
form would identify a finite local obstruction.  Neither outcome addresses
mixed `Lambda`/loads/targets, the `Lambda^19` Jacobian target, the full K00
closure-first incidence, Taylor realization, or JC2.
