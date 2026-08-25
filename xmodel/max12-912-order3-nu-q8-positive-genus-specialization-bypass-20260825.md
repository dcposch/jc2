# Selected-Q8 positive-genus specialization bypass

Date: 2026-08-25  
Status: **COORDINATOR CONDITIONAL LEMMA; `g(H)>0`, cross-characteristic
review, and hostile review of this composition pending**

## 1. Purpose

The live degree-one/all-eight computation is sufficient but may not be
necessary.  A positive geometric genus for the forced mod-127 plane curve
`H` would already exclude trajectories on every characteristic-zero
selected component meeting a corrected-Q8 contact, even if the eight
contacts lie on eight singleton components.

This note states the exact conditional chain.  It does not assert that the
pending genus computation or cross-characteristic review has passed.

## 2. One H-supported marked contact is enough

Consume the following exact inputs only after their stated review gates:

1. the reviewed theorem that some mod-127 selected-source component maps
   dominantly and separably to the geometrically integral curve `H`;
2. the hostile-reviewed rational-contact residual obstruction, with its
   repaired bound `I(H,R)<=37,010`, which puts at least one of the full
   contacts with `v=26,58,67` on an `H`-supported source component `C`;
3. the cross-characteristic full-contact bridge, which gives the arithmetic
   completed source `R[[w]]` and attaches the corresponding reviewed
   characteristic-zero selected branch `Y` to that same full special point.

At the marked point the full special source has completed local ring
`k[[w]]`, hence one local irreducible component in every dimension.  The
scheme-theoretic closure of `Y` contains the point.  Its one-dimensional
special-fibre component is therefore dense in `C`.

The map from the normalization of the projective closure of `C` to the
normalization of `H` is generically finite and separable.  At the marked
source point the completed local ring is `k[[w]]`, so the pullback of `dw`
is nonzero.  A generically inseparable extension of one-variable function
fields in characteristic 127 would kill every pulled-back differential from
the smaller field, including `dw`.  No claim that `w` is a uniformizer on the
possibly singular plane model is needed.
Consequently Riemann--Hurwitz gives

```text
g(H)>0  ==>  g(C)>0.                                  (1)
```

No source degree-one or all-contact statement is used here.

## 3. Positive genus cannot specialize from a rational generic curve

Suppose the characteristic-zero component `Y` admitted a nonconstant map
from `P1`.  After normalizing/projectivizing and making a finite field/DVR
extension, Riemann--Hurwitz makes its smooth projective normalization a
genus-zero curve with a rational point, hence `P1`.

Take a regular proper model of this normalized generic curve dominating the
projective closure used above.  A regular proper model of `P1` over a DVR is
obtained, after resolving the birational map to `P1_R`, through blowups and
contractions of vertical rational curves.  Every irreducible special-fibre
component therefore has rational normalization.  Its image onto `C` would
give a dominant map from a rational curve to the normalization of `C`, which
is impossible when (1) holds.  Equivalently, this is the standard genus
inequality for the residue function field of a residually transcendental
divisorial valuation.

Thus

```text
g(H)>0  ==>  the attached characteristic-zero component Y
             admits no nonconstant map from P1.        (2)
```

Properization and resolution are load-bearing.  A statement about an affine
closure alone is not enough.

## 4. Primitivity propagates the obstruction to all eight contacts

The reviewed Galois-primitivity theorem says that the eight selected local
branches are grouped by characteristic-zero geometric components in exactly
one of two ways:

```text
one component containing all eight contacts, or
eight singleton components.
```

In the first case, (2) applies to the common component.  In the singleton
case, transitivity of the Galois action makes the eight components conjugate;
their smooth projective normalizations have the same genus.  Hence if the
one component attached above has positive genus, all eight singleton
components do.  In either partition no selected component meeting a Q8
contact admits a nonconstant map from `P1`.

The reviewed infinity/passport registration supplies exactly such a
nonconstant map from the trajectory source `P1_x` to the normalization of
its selected coefficient component.  Therefore a proved `g(H)>0` would
exclude an actual trajectory on every selected component meeting a
corrected-Q8 contact, including the currently open singleton alternative.

## 5. Computational genus targets and scope

The pinned support of `H` has Newton hull

```text
(0,3), (1,0), (21,0), (21,1), (0,190)
```

with 1,890 interior lattice points.  Toric nondegeneracy would therefore
give genus 1,890, but the `w=0` face is degenerate and this shortcut cannot be
asserted.  An exact normalization/function-field genus, a certified regular
differential, or any rigorous lower bound `g(H)>=1` is sufficient.

This route classifies only characteristic-zero selected components meeting
the eight Q8 contacts.  Components disjoint from the contacts, other
`(9,12)` strata, Taylor realization, the rest of maximum twelve, a
counterexample, and JC2 remain open.  All substantive genus computation is
AWS-only.
