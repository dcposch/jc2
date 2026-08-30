# Rank-four zero-cusp cycle: polynomial-link obstruction to the primitive braid packet

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`rank4_cycle_m0` lane)  
Frozen basis: `f4ce61d422f11c66b1767d69d83a6c4f6f3c2938`  
Lifecycle: **FINAL+VERIFIED EXACT-PACKET NO-GO / GLOBAL CONTROL PASSES / BROADER HORN OPEN**

## 0. Verdict

The primitive `S4` escape packet isolated in the preceding cycle-zero report
cannot be globalized as the complete finite braid packet of a polynomially
parametrized one-place curve

```text
nu:A1 -> B subset A2.                                  (0.1)
```

This also excludes every Hurwitz-equivalent factorization of that packet.
The obstruction is at infinity and is independent of the choice of paths to
the finite critical values.

For the frozen four-braid `beta`, an exact reduced-Burau calculation gives

```text
Delta_beta(t)
 = -t^(-4) (t^2-t+1)^2
     (t^6-4t^5+4t^4-3t^3+4t^2-4t+1).                 (0.2)
```

The last factor has values `-15` and `25` at `t=2` and `t=3`, respectively.
It therefore has a positive real zero in `(2,3)`.  In contrast, the knot at
infinity of an irreducible affine plane curve with one place at infinity is a
toral/graph knot.  The Eisenbud--Neumann splice formula implies that every
nonzero zero of its Alexander polynomial is a root of unity.  Equation (0.2)
is therefore impossible for such a knot at infinity.

This is a strict successor to the earlier braid-local threat map:

```text
abstract S4 coloring of the packet:                  survives;
positive algebraic curve piece in a bidisc:          survives;
global polynomial A1 realization of that packet:    impossible;
all R4-CYCLE-0 polynomial packets:                   not classified. (0.3)
```

The last firewall matters.  Tangential two-point conductor, unibranch affine
singularities, or a different quasipositive factorization can change the
boundary braid and its Alexander polynomial.  The argument below excludes
the displayed packet and its Hurwitz orbit, not every possible realization
of

```text
h=k=1, beta1(B)=n22=1, n4=0, m=0,
(C,Q)=(A1,1) or (P1,0).                               (0.4)
```

An explicit global polynomial control

```text
X(t)=t^4+t^3-t,          Y(t)=t^2                     (0.5)
```

has one normalization place at infinity and exactly one ordinary affine
two-point identification.  Its infinity braid is `sigma_1^3` and its affine
complement group is cyclic.  Thus the infinity gate is nonvacuous and the
named one-node behavior is globally realizable; it simply does not carry the
primitive four-color escape.

## 1. Charged inputs and primary topology interface

```text
e73f8e83c4031e516f0302dea94e168b5f8b8d5f0bcc6cd86f87eb927a682e14
  xmodel/block-descent-a1-quartic-cycle0-projection-propagation-obstruction-sol56-20260830.md
b9f0352ce63513ce16925f9bf4d7b5be11e0246c9426ecc72cf477cd977103a0
  ops/block_descent_a1_quartic_cycle0_braid_escape_replay.py
cf157e17db8179b590f15808aab84447717df343735416578e005a2085d73d4e
  xmodel/block-descent-a1-quartic-minimal-cycle-nodal-control-threat-map-sol56-20260830.md
768cf08fe2be7a72e9e17cd15acd56976b6743cefa293bf11472a4fb4e701805
  xmodel/block-descent-a1-quartic-branch-topology-acyclic-obstruction-sol56-20260830.md
6e5d5ab57734db02c5d29d264f1d2b3c81b21639f0ff786e19c9723e285e2042
  ops/block_descent_a1_quartic_cycle0_polynomial_link_replay.py
```

The theorem layer uses the following primary sources.

```text
David Eisenbud and Walter D. Neumann,
Three-Dimensional Link Theory and Invariants of Plane Curve Singularities,
Annals of Mathematics Studies 110, Princeton University Press, 1985;
especially Theorem 12.1 (splice-diagram Alexander polynomial).

Walter D. Neumann,
"Complex algebraic plane curves via their links at infinity",
Inventiones Mathematicae 98 (1989), 445--490,
DOI 10.1007/BF01393832.

Walter D. Neumann and Le Van Thanh,
"On irregular links at infinity of algebraic plane curves",
Mathematische Annalen 295 (1993), 239--244,
DOI 10.1007/BF01444886; arXiv:alg-geom/9202008.
```

Neumann's RPI splice construction, recalled explicitly on pages 1--3 of the
1993 paper, applies to the link at infinity of an arbitrary reduced fibre
`V=P^(-1)(0)` of a polynomial `P:C2->C`; its introduction states that this
link is toral before imposing the separate definition of regularity at
infinity.  Every reduced affine plane curve is such a zero fibre after
choosing a reduced defining polynomial.  Regularity of that fibre is
therefore not assumed for the toral-link assertion.  No classification of
polynomial embeddings, no
Abhyankar--Moh rectification, and no claimed classification of affine
complement groups is used.

## 2. The one-place Alexander gate

Let `B` be the irreducible image of (0.1), with `nu` generically one-to-one.
The normalization compactifies from `A1` to `P1` by adding the single point
`t=infinity`.  Hence `B` has one normalization place at infinity and

```text
K_infinity = B intersect S_R^3                              (2.1)
```

is a knot for all sufficiently large transverse spheres.

Neumann's link-at-infinity construction represents `K_infinity` by a toral
(Eisenbud--Neumann graph-link) splice diagram in `S3`.  Eisenbud--Neumann
Theorem 12.1 applies to graph links in integral homology spheres, hence in
particular to this knot in `S3`.  In its one-component clause it gives, up to
a Laurent unit,

```text
Delta_K(t)
 = (t-1) product_v (t^(ell_v)-1)^(delta_v-2),          (2.2)
```

where `v` runs over non-arrowhead vertices, `delta_v` is the valency, and
`ell_v` is the linking number of the knot with the corresponding virtual
component.  Formula (2.2) is an identity in the Laurent fraction field; its
apparent denominator factors cancel because the left side is the knot
Alexander polynomial.

For one component every relevant `ell_v` is nonzero.  Replacing a negative
`ell_v` by its absolute value only changes a Laurent unit.  Consequently all
numerator and denominator factors in (2.2) are of the form `t^N-1`.  After
cancellation, every nonzero zero of `Delta_K` is still a zero of some
`t^N-1`.  Therefore

```text
one-place polynomial plane-curve knot at infinity
  ==> every Alexander zero is a root of unity.          (2.3)
```

Here and below an Alexander polynomial is an element of `Z[t,t^(-1)]`
defined up to multiplication by a unit `+/-t^j`.  Such a unit has no zero in
`C*`, so (2.3) and the off-unit-circle obstruction are normalization
independent.  The displayed choice in (0.2) has `Delta_beta(1)=1`; this fixes
the sign but the Laurent shift remains immaterial.

This implication is the entire global theorem consumed below.  Equivalently,
it follows by decomposing a graph knot into torus-knot, cabling, and
connected-sum pieces and applying the standard cable and product formulas,
but (2.2) avoids any convention about signed cabling.

Now take a generic finite linear projection of `B`.  Over a large circle in
the projection base, its sheets form a closed braid isotopic to (2.1).  The
product of the based finite braid-monodromy factors is that boundary braid,
up to inversion from the orientation convention and up to conjugacy from a
change of the boundary basepoint.  Inversion replaces the Alexander
polynomial by its reciprocal up to a unit, while conjugacy does not change
the closed braid.  Thus the root-of-unity gate (2.3) applies without fixing
those conventions.

## 3. Exact Alexander polynomial of the primitive packet

The preceding report froze the positive bands

```text
b1 = s1,
b2 = s2^3 s1 s2^(-3),
b3 = s3 s2^3 s1 s2^(-3) s3^(-1),
n  = s2 s3^2 s2^(-1),                                  (3.1)
```

and their product

```text
beta = b1 b2 b3 n
 = s1 s2^3 s1 s2^(-3)
      s3 s2^3 s1 s2^(-3) s3^(-1)
      s2 s3^2 s2^(-1).                                 (3.2)
```

The permutation of (3.2) is a four-cycle, so its closure is a knot.  Recall
that the three simple bands in (3.1) have tree incidence and Euler number
one, while `n` supplies the one positive two-point `(2,2)` identification.
The based color tuple from the charged report is fixed by every factor and
generates `S4`.

For transparency, use the unreduced Burau generator whose nontrivial block is

```text
rho(s_i) = [[1-t, t],
            [1,   0]],                                  (3.3)
```

and let `bar(rho)` be its quotient by the invariant vector.  For a four-braid
whose closure is a knot,

```text
Delta_closed(beta)(t)
  = (1-t)/(1-t^4) det(I-bar(rho)(beta))                 (3.4)
```

up to `+/-t^j`.  Exact Laurent arithmetic applied to (3.2) yields (0.2).  In
dense high-to-low Laurent coefficients this is

```text
-t^6 + 6t^5 - 15t^4 + 25t^3 - 31t^2 + 33t - 31
      + 25t^(-1) - 15t^(-2) + 6t^(-3) - t^(-4).        (3.5)
```

It is normalized by `Delta_beta(1)=1`.  Put

```text
P(t)=t^6-4t^5+4t^4-3t^3+4t^2-4t+1.                   (3.6)
```

Then

```text
P(2)=-15,                 P(3)=25.                     (3.7)
```

The intermediate value theorem gives a real zero `r` with `2<r<3`.  In
particular `|r|` is not one, so `r` is not a root of unity.  Equations
(2.3) and (3.7) contradict the existence of a one-place polynomial curve
whose complete boundary braid is (3.2).

This obstruction is stronger than a failure to find low-degree
coefficients: no polynomial degree can globalize this boundary knot.

## 4. Why the entire Hurwitz orbit is excluded

A Hurwitz move on adjacent factors has the form

```text
(g_i,g_(i+1))
  -> (g_i g_(i+1) g_i^(-1), g_i)                       (4.1)
```

or its inverse, depending on convention.  It preserves the ordered product.
A simultaneous conjugation of all factors conjugates that product.  Hence a
Hurwitz-equivalent factorization of (3.1) has boundary braid equal or
conjugate to (3.2); its closure and Alexander polynomial are unchanged.

Changing the orientation convention replaces `beta` by `beta^(-1)`.  Its
Alexander polynomial is reciprocal to (0.2) up to a unit, so the real zero
`r` is replaced by `r^(-1)`, again off the unit circle.  None of these
choices escapes (2.3).

It follows that rearranging the same vanishing paths, choosing a different
distinguished basis, or using an equivalent quasipositive factorization
cannot turn the charged packet into a polynomial one-place curve.  A viable
primitive escape must change the boundary braid type, not merely its
factorization.

## 5. Exact global one-node control

The obstruction is checked against the polynomial parametrization (0.5).
If `(X(t),Y(t))=(X(u),Y(u))`, then `t^2=u^2`.  For `t != u` this forces
`u=-t`, and

```text
X(t)-X(-t)=2t(t^2-1).                                  (5.1)
```

The only nontrivial unordered identified pair is therefore `{+1,-1}`.  The
derivative is

```text
(X'(t),Y'(t))=(4t^3+3t^2-1,2t).                        (5.2)
```

When `Y'` vanishes, `t=0` and `X'=-1`; thus the normalization map is an
immersion.  At the two points above the unique double point `(1,1)`, the
tangent vectors are

```text
t=+1: (6,2),                t=-1: (-2,-2),
determinant=-8.                                               (5.3)
```

The double point is ordinary.  Eliminating `t` gives the irreducible image
equation

```text
(x-y^2)^2-y(y-1)^2=0.                                  (5.4)
```

There are no other affine singularities: away from the unique identified
pair the normalization is injective and immersive.  Since both coordinate
functions have their sole pole at `t=infinity`, the curve has one
normalization place at infinity.

Project (5.4) to the `y`-line.  At `y=0`, `t=0` gives one simple ramification
and the positive braid factor `s1`.  At `y=1`, the ordinary node gives
`s1^2`.  Thus

```text
beta_infinity_control=s1^3,                             (5.5)
```

whose closure is the trefoil.  Zariski--van Kampen on fibre meridians `a,b`
gives

```text
pi1(A2-B_control)
 = <a,b | a=b, [a,b]=1>
 = Z.                                                   (5.6)
```

In particular every transposition-valued representation has cyclic image;
it cannot realize the four-letter primitive overlap.  This control confirms
the familiar equality propagation only in its tail-trivial two-strand
setting.  It is not evidence that based equality propagates through an
arbitrary higher-strand braid.

## 6. Scope, tangencies, and unibranch singularities

The no-go uses only the total boundary knot.  Therefore it remains valid if
the affine interpretation of the factors is deformed while the boundary
braid stays in the conjugacy class of (3.2).  In particular, relabeling the
two conductor preimages or changing local coordinates at the node cannot
help.

It does not license either of the following extrapolations.

1. A tangential two-point conductor generally replaces a node full twist by
   a higher positive pure band.  That changes the total braid and requires a
   fresh Alexander calculation.
2. A unibranch affine singularity contributes its own positive local braid.
   It can change both the splice data and the infinity knot even when the
   normalization remains `A1` and the total conductor census stays small.

Accordingly this report does not claim that every one-node polynomial `A1`
curve has trefoil infinity, that every such complement is cyclic, or that
all admissible transposition colorings preserve a perfect matching.  Those
would require an additional semigroup/splice classification.  The ruling
rows `(A1,Q=1)` and `(P1,Q=0)` are also not consumed by the Alexander gate.

What is proved is exactly

```text
the frozen primitive packet, and every Hurwitz-equivalent packet,
is not the complete braid monodromy of a one-place polynomial A1 curve. (6.1)
```

## 7. Maximum-safe update and successor

Promote the following statements.

1. The braid-local `S4` escape from the charged report is algebraically
   consistent in a bidisc but globally non-polynomial: its Alexander
   polynomial violates the graph-knot gate at infinity.
2. Hurwitz moves cannot repair it, because the obstruction belongs to the
   closed product braid.
3. The explicit parametrization (0.5) realizes the one-place/one-ordinary-
   identification census with trefoil infinity and cyclic complement.
4. `R4-CYCLE-0` remains open for genuinely different boundary packets,
   especially packets altered by tangential conductor or unibranch affine
   singularities.

The sharp next search is finite at each projection degree:

```text
enumerate positive-band factorizations with disk normalization;
impose exactly one disjoint-transposition two-point packet;
retain only full-S4 based colorings;
compute the product-braid Alexander polynomial immediately;
discard every non-cyclotomic product;
for survivors, solve the one-place Puiseux/splice semigroup equations;
only then attempt polynomial coefficients and the ruling constraints.   (7.1)
```

The Alexander test is inexpensive and should precede coefficient searches.
It is necessary, not sufficient: graph knots can share Alexander
polynomials, and a cyclotomic polynomial does not itself produce a
polynomial parametrization or a quartic cover.

Do not infer from this report a finite-flat quartic cover, an actual proper
block, a Keller first leg, a counterexample to JC2, or a proof of JC2.

## 8. Deterministic replay and firewalls

The desk-small exact replay is

```text
6e5d5ab57734db02c5d29d264f1d2b3c81b21639f0ff786e19c9723e285e2042
  ops/block_descent_a1_quartic_cycle0_polynomial_link_replay.py
```

Ordinary, `python3 -O`, and `python3 -OO` runs are byte-identical, with

```text
stdout SHA-256:
5a6a26b5dcc2f7c5c568095d4e70069d305794d847e1258e6ae860883bbe794c

status=PASS-R4-CYCLE-0-POLYNOMIAL-LINK-OBSTRUCTION
payload_sha256=3da75d8ab26d5be82a5c06bbc99afb08468de194c9ab967d2d29215a91b76e9c
```

The replay checks the Burau generators and their exact Laurent inverses, the
four-cycle closure permutation, identity (3.4), the complete factorization
(0.2), normalization at `t=1`, the two signs in (3.7), and the elementary
parametrization checks (5.1)--(5.5).  The mutation
`--mutate-packet-to-trefoil` exits nonzero at the frozen Alexander identity.

The replay does not encode Neumann's toral-link theorem,
Eisenbud--Neumann's splice formula, identification of the large boundary
braid with the link at infinity, Zariski--van Kampen, global existence of a
quartic cover, the source-forest theorem, or either ruling theorem.  Those
are written theorem interfaces or firewalls above.

No heavy local CAS was used.  Nothing here touches the formalization tree,
top ledgers, sealed lanes, or the campaign pilot log.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16539`.
- Body SHA-256:
  `d6cc5f6e08534b1bc1a25a0afbf156c266dd3ab9deae5d35ede2e8c9361b5f04`.
- Frozen basis: `f4ce61d422f11c66b1767d69d83a6c4f6f3c2938`.
