# Selected-Q8 positive-genus trajectory exclusion — repaired V2 successor

Date: 2026-08-25  
Status: **PRODUCER-EXACT V2 COMPOSITION; final hostile review pending**

## 1. Theorem, predecessor, and exact scope

Assume the reviewed cube/Faber and selected-global-quotient reductions place
an **actual** order-three trajectory in the strict leaf

```text
k=mu=0,  nu!=0,
```

and that its selected coefficient component meets a corrected-Q8 contact.
Then no such trajectory exists.

This V2 successor consumes every immutable input and every repair recorded in

```text
xmodel/max12-912-order3-nu-q8-selected-contact-positive-genus-exclusion-repaired-20260825.md
SHA256 b543738ad447777dfca624512d304b7e86ba312c9c5c87c1abf6cea0d2a47039
```

and changes one shorthand that was not explicit enough: the `H`-supported
source component is first chosen as a **geometric** component and placed over
a finite residue-field/unramified-DVR extension.  Only this V2 file is eligible
for final review and consumption.

The firewall is unchanged.  This is not an exclusion of components disjoint
from the corrected-Q8 contacts, every `nu!=0` component, the polynomial core,
`(8,12)`, all `(9,12)`, maximum degree twelve, an arbitrary Keller pair, or
JC2.

## 2. Reviewed inputs retained verbatim

V1's immutable parent table is incorporated without alteration.  In
particular, V2 consumes:

- the reviewed six-row selected quotient and actual-trajectory landing;
- the reviewed geometric mod-127 `H`-component theorem;
- reviewed geometric integrality of `H`;
- the reviewed `40,960>37,010` theorem placing at least one rational full
  contact `q=(0,q_v)`, `q_v in {26,58,67}`, on an `H`-supported source
  component;
- the reviewed arithmetic full-contact bridge and full relative `8 x 8`
  unit;
- the Grok-CONFIRMED exact point count proving `g(Htilde)>0`;
- the reviewed infinity/passport and primitive `8` versus `1+...+1`
  alternatives.

The V1 case manifest

```text
57717e15a2e2064f73f635fadeeac6101765bdee19ebdf46ea234de547d3ae4e
```

pins every one of those reports and reviews.  No generic-length, no-merger,
coordinate-graph, Padé, Taylor, or terminal input is added here.

## 3. Choose the geometric component before descent

Over `Fbar_127`, choose an irreducible `H`-supported source component
`Cbar` through the rational contact `q` supplied by the reviewed residual
theorem.  The full relative `8 x 8` Jacobian is a unit at `q`.  After geometric
base change, the completed full-source local ring is therefore

```text
Fbar_127[[w]],
```

so there is exactly one geometric source branch and exactly one geometric
component through `q`.  In particular, the chosen `Cbar` is unambiguous.

The source equations, `q`, and the plane curve `H` are defined over
`F_127`.  The unique component is Frobenius-stable; equivalently, and all
that is needed below, it has a finite field of definition

```text
k0=F_(127^m).
```

Replace the reviewed splitting DVR by the corresponding finite unramified
complete/Henselian extension `R0`, with residue field `k0` and fraction field
`K0`.  Now write `C` for this geometrically integral `k0`-component.  Its map
to `H_(k0)` remains dominant.  This finite unramified extension is made
**before** any use of geometric integrality or genus for `C`.

## 4. Whole-source attachment over `R0`

Base change the common eight-equation localized source and the reviewed
arithmetic contact section to `R0`.  The determinant remains a unit, so its
arithmetic formal neighborhood is

```text
Spf R0[[w]].                                             (4.1)
```

The symbols `K0[[w]]` and `k0[[w]]` below denote the completed generic and
special **fibre** local rings of (4.1), not an uncompleted localization of
`R0[[w]]`.  Reviewed six-row uniqueness identifies the generic fibre germ
with the selected characteristic-zero component `Y`.

Let `Z` be the scheme-theoretic closure of `Y` in the common source.  Its
ideal in `R0[[w]]` maps to zero in the generic fibre completion `K0[[w]]`.
Since `R0[[w]] -> K0[[w]]` is injective, the ideal is zero.  Thus the special
fibre completion of `Z` is `k0[[w]]`: one reduced multiplicity-one branch.
By Section 3 it is the branch of `C`.  Hence `C` is genuinely a special
component of the horizontal closure, not merely a component of the plane
projection incident at the same point.

The full `8 x 8` unit is also the source of the local parameter `w` at
`q`; no fixed fibre away from `w=0` is used for that assertion.  Together
with the separate plane unit `H_v(q)!=0`, it gives local ramification index
one, hence separability of `Ctilde -> Htilde`.  Separability is an optional
cross-check, not a premise of the genus argument.

## 5. Positive genus of `C`

The Grok-CONFIRMED point count gives

```text
g(Htilde)>0.
```

Normalize projective closures over `k0`.  Dominance gives a finite
nonconstant map `Ctilde -> Htilde_(k0)`.  If the geometrically integral curve
`Ctilde` were geometrically rational, then over an algebraic closure

```text
kbar(Htilde) -> kbar(Ctilde)=kbar(t)
```

would make `Htilde` rational by geometric Lueroth, contradiction.  Therefore

```text
g(Ctilde)>0.                                             (5.1)
```

This does not claim that `k0(C)` itself is `k0`-rational.  The separable
Riemann--Hurwitz check mentioned in Section 4 gives the same inequality but
is unnecessary.

## 6. Finite DVR rationalization and proper valuation contradiction

Assume an actual trajectory lies on `Y`.  The reviewed infinity/passport
input gives a nonconstant map from `P1_x` to the smooth projective
normalization `Ytilde`.  Geometric Lueroth proves only that `Ytilde` is
geometrically rational over `K0`; it need not yet be `P1_(K0)`.

Choose a finite extension `K1/K0` over which `Ytilde` acquires a rational
point and all finite trajectory constants are defined.  Complete a DVR
`R1` above `R0`; let its residue field be `k1`.  Then

```text
Ytilde_(K1) ~= P1_(K1).                                  (6.1)
```

The extension `R1/R0` may be ramified.  Since `C/k0` is geometrically
integral, `C_(k1)` stays integral and (5.1) stays true.

Take the projective closure of the integral horizontal component of
`Z_(R1)` selected by `Y_(K1)` and normalize it.  Properness/lying-over puts
a vertical component `Gamma` above the generic point of `C_(k1)`; equivalently,
the divisorial valuation defined by `C` extends to the common generic
function field.  The center `Gamma` maps dominantly and generically finitely
to `C_(k1)`.  A regular proper arithmetic-surface model may be used to expose
the same valuation, but regularity is not being substituted for the
whole-source attachment of Section 4.

By (6.1) the generic function field is `K1(t)`.  The ruled-residue theorem
for a residually transcendental divisorial valuation of `K1(t)` gives

```text
kappa(Gamma)=ell(s)
```

for the finite relative constant extension `ell/k1`.  Dominance gives
`k1(C) -> kappa(Gamma)`; adjoining `ell` gives
`ell(C) -> ell(s)`.  Geometric Lueroth would force `C` to be rational,
contradicting (5.1).  Hence `Ytilde` is not geometrically rational and cannot
be dominated nontrivially by `P1`.

This proper divisorial-valuation argument is load-bearing.  Semistable
reduction or arithmetic-genus semicontinuity is only an optional remark.

## 7. Primitive alternatives and final conclusion

The reviewed characteristic-zero primitive alternatives are one component
through all eight contacts or eight singleton components.  The all-eight
case is already excluded by the reviewed infinity theorem.  In the singleton
case, Section 6 excludes the component attached at `q`; all eight singleton
components are `Qbar`-isomorphic Galois conjugates and therefore have the
same geometric genus.  None is dominated by `P1`.

This propagation uses only characteristic-zero isomorphism.  It does not say
that all eight specializations are `H`-supported.

Thus neither primitive alternative supports the registered actual
selected-Q8 trajectory.  The sole remaining debt is a fresh hostile review
of this V2 composition at exactly the stated scope.
