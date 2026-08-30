# One-place A1 branch: total-delta-two iterated-knot S4 obstruction

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`rank4_cycle_m0` lane)  
Frozen basis: `adb847313c6c946d893100a2cd4c8226a5cc2f0c`  
Lifecycle: **FINAL+VERIFIED THEOREM / TOTAL AFFINE DELTA <=2 EXCLUDED / DELTA 3 SHARP CONTROL**

## 0. Theorem and verdict

Let `B` be a reduced irreducible affine plane curve over `C` with

```text
normalization(B)=A1.                                      (0.1)
```

For every affine singular point `p` of `B`, let `delta_p` be its local
delta invariant, and put

```text
Delta_aff(B)=sum_p delta_p.                               (0.2)
```

Suppose that

```text
rho: pi1(A2-B) -> S4                                      (0.3)
```

sends every positively oriented generic meridian to a transposition and has
transitive image.  Then

```text
Delta_aff(B) >= 3.                                        (0.4)
```

Thus no connected generically simply ramified degree-four cover has such an
irreducible one-place branch curve with total affine delta at most two.  This
strictly extends the sole-ordinary-node theorem: the affine singularities may
now be arbitrary, provided their total delta is at most two.

The proof has four exact parts.

1. The compact core of a nearby regular fibre has genus exactly
   `Delta_aff(B)`.
2. The knot at infinity is not merely a graph knot.  The one-place polynomial
   parametrization and Neumann's rooted cabling construction make it an
   iterated cable of the unknot, hence either the unknot or a prime knot.
3. Genus-two graph knots are exactly the pentafoil, a connected sum of two
   trefoils, or a `(2,+/-1)` cable of a trefoil, allowing mirrors.  A
   double-branched-cover determinant lemma excludes the two prime families.
   The connected sums pass the group test but are excluded by the one-place
   prime-knot interface.
4. The bound cannot be increased using only (0.1)--(0.3): the curve
   `(x,y)=(t^3,t^4)`, or `y^3=x^4`, has total delta three and its `T(3,4)`
   complement has an explicit transitive meridian-transposition `S4` quotient.

This is a topological monodromy obstruction.  It does not construct or exclude
a Keller map once total delta is at least three.

## 1. Charged inputs and primary interfaces

This artifact uses the predecessor theorem and replay

```text
c61f0cebdc06bdca88ad76f3714047a1998ff7aeb885a79e84b060a091c23329
  xmodel/block-descent-a1-one-ordinary-node-all-degree-meridional-rank-obstruction-sol56-20260830.md
a6b000430e872e372c6c4cad9d694baa522746717eeef837e52884b206eff6fa
  ops/block_descent_one_node_all_degree_meridional_rank_replay.py
```

and the following primary sources.

```text
David Eisenbud and Walter D. Neumann,
Three-Dimensional Link Theory and Invariants of Plane Curve Singularities,
Annals of Mathematics Studies 110, Princeton University Press, 1985.

John Milnor,
Singular Points of Complex Hypersurfaces,
Annals of Mathematics Studies 61, Princeton University Press, 1968.

Walter D. Neumann,
"Complex algebraic plane curves via their links at infinity",
Inventiones Mathematicae 98 (1989), 445--489,
DOI 10.1007/BF01393832.

Walter D. Neumann and Lee Rudolph,
"Unfoldings in knot theory",
Mathematische Annalen 278 (1987), 409--439,
DOI 10.1007/BF01458078;
with "Corrigendum: Unfoldings in knot theory",
Mathematische Annalen 282 (1988), 349--351,
DOI 10.1007/BF01456981.

Lee Rudolph,
"Some knot theory of complex plane curves",
L'Enseignement Mathematique 29 (1983), 185--208;
corrected redaction arXiv:math/0106058, especially Sections 4 and 6.

Horst Schubert,
"Knoten und Vollringe",
Acta Mathematica 90 (1953), 131--286,
DOI 10.1007/BF02392437.
```

The exact division of labor matters.

* Corrected Neumann--Rudolph Lemma 7.1 says that a reduced fibre whose link at
  infinity is a knot makes its defining polynomial good.  The 1988
  corrigendum is essential; the uncorrected formulation is not used.
  Neumann 1989 recalls this interface on pages 445--446.
* Neumann 1989, Theorem 1 on page 447, identifies a regular plane curve with a
  collar on the unique minimal Seifert surface of its infinity link.
* Neumann 1989, Theorem 2(i) on page 450, gives the rooted splice diagram and
  identifies the root valency with the number of points at infinity.  The
  cabling definitions are on pages 447--448.
* Milnor supplies the local Milnor-fibre Euler characteristic and the plane
  curve identity `mu_p=2 delta_p-r_p+1`.
* Eisenbud--Neumann supplies the graph-link splice/cabling calculus.
* Schubert supplies genus additivity, the satellite/cable genus interface,
  and primeness of nontrivial cable knots; see Sections 5, 12, and 24.  On
  page 192 Schubert also records the cable Alexander formula, attributed
  there to Seifert.
* Rudolph gives the direct parametrized version: a polynomial curve
  `t -> (p(t),q(t))` meets a sufficiently large bidisk boundary in an iterated
  torus knot.  The local epicycle/cabling construction is in Section 4 and the
  large-bidisk statement is in Section 6.

No implication from general quasipositivity to strong quasipositivity is used.

## 2. Exact nearby-fibre genus for arbitrary affine singularities

Choose a reduced equation

```text
B=f^(-1)(0).                                              (2.1)
```

The normalization `A1` has one end, so `B` has one normalization place at
infinity and its link `K_infinity` is a knot.  Corrected Neumann--Rudolph
Lemma 7.1 makes `f` good.  Choose a sufficiently small nonzero regular value
`epsilon`, with no other critical value between `0` and `epsilon`.  Goodness
prevents vanishing cycles at infinity, so `f^(-1)(epsilon)` is obtained from
`B` by smoothing precisely its affine singularities and has the same infinity
knot.

Let `r_p` be the number of local branches at `p`, and let `M_p` be its local
Milnor fibre.  A compact core of the normalization is a disk.  Remove one
small disk around each of the `r_p` normalization preimages of every `p`, then
glue in `M_p`.  Gluing along circles changes no Euler characteristic, and

```text
chi(M_p)=1-mu_p.
```

Consequently the compact nearby fibre `F_epsilon` has

```text
chi(F_epsilon)
 = 1-sum_p r_p + sum_p(1-mu_p)
 = 1-sum_p(mu_p+r_p-1)
 = 1-2 sum_p delta_p.                                    (2.2)
```

Its only boundary component is `K_infinity`.  Therefore

```text
g(F_epsilon)=Delta_aff(B).                                (2.3)
```

Neumann's Theorem 1 makes this compact core the minimal Seifert surface, so

```text
g_3(K_infinity)=Delta_aff(B).                             (2.4)
```

Equation (2.3) is the exact generalization of the node computation.  For an
ordinary node, `r=2`, `mu=1`, and `delta=1`; for a unibranch singularity the
same formula detects delta even though there is no two-point normalization
fibre.

## 3. One place forces an iterated cable, not a connected sum

The coordinate functions on the normalization are regular functions on `A1`.
Thus the normalization map is a polynomial parametrization

```text
nu(t)=(p(t),q(t)).                                        (3.1)
```

All affine failures of injectivity lie in a compact set.  On the unique tail
at `t=infinity`, the successive characteristic terms of `(p,q)` give the
standard Puiseux/epicycle cabling construction.  Hence a sufficiently large
bidisk boundary meets `B` in an iterated cable of the unknot.  This is the
direct Rudolph interface.

The same conclusion follows intrinsically from Neumann's rooted construction.
The projective normalization is `P1` and `P1-A1` is one point, so the closure
of `B` has one point at infinity.  By Neumann Theorem 2(i), the root has
valency one.  The construction therefore starts with the one-component Hopf
link, namely the unknot.  Since the final link also has one component, no
component-adding cabling can occur; every nontrivial step replaces the current
knot by a cable.

Delete winding-one steps and steps that produce an unknot.  A nontrivial torus
knot is prime, and a nontrivial cable of a knot is prime by Schubert.  Induction
gives

```text
K_infinity is the unknot or a prime iterated cable.        (3.2)
```

This is stronger than merely saying that `K_infinity` is a graph knot.  In
particular, a connected sum of two nontrivial knots cannot occur in the present
one-place setup.

Finally, the infinity-knot group maps onto the affine complement group while
preserving generic meridians.  For a generic finite projection, let
`x_1,...,x_N` be fibre meridians and `beta_1,...,beta_s` the based finite braid
monodromies.  Zariski--van Kampen imposes every individual relation

```text
x_j=beta_v(x_j),
```

whereas the Artin presentation of the closed boundary braid imposes only the
relations for the total braid `beta_infinity=beta_1...beta_s`.  The individual
relations imply the total ones, giving a meridian-preserving surjection

```text
pi1(S3-K_infinity) ->> pi1(A2-B).                         (3.3)
```

Composing (3.3) with (0.3) gives the same transitive transposition image.
Therefore it suffices below to obstruct such an image for the infinity knot.

## 4. Complete genus-two graph-knot census

It is useful first to classify the larger graph-knot category, before applying
(3.2).  A graph knot is built from the unknot using connected sum and cabling.
Schubert's formulas, with `p>=2` after trivial steps are removed, are

```text
g(J#L)=g(J)+g(L),
g(C_(p,q)(J))=p g(J)+(p-1)(|q|-1)/2.                     (4.1)
```

At genus one, the only graph knots are `T(2,+/-3)`, the two trefoils.  At
genus two, (4.1) gives exactly the following unoriented families, allowing all
mirrors.

```text
(A) T(2,+/-5);
(B) T(2,+/-3) # T(2,+/-3), with either chirality per factor;
(C) C_(2,+/-1)(T(2,+/-3)), with either companion chirality. (4.2)
```

Indeed, a composite genus-two graph knot is a sum of two genus-one graph knots.
For a prime cable with unknot companion, the equation

```text
(p-1)(|q|-1)=4
```

and coprimality leave only `T(2,5)` up to exchanging the torus coordinates and
mirroring.  For a nontrivial companion, `p g(J)<=2` forces
`p=2`, `g(J)=1`, and then `|q|=1`.

The list deliberately allows more signs than complex orientation may permit;
enlarging the list makes the exclusion stronger.  By (3.2), family (B) is
already impossible for a one-place polynomial curve.  Families (A) and (C)
are the only one-place genus-two candidates.

## 5. The double-branched-cover determinant obstruction

The following elementary lemma exactly tests the remaining candidates.

**Lemma.**  If a knot group has a transitive representation to `S4` sending a
meridian to a transposition, then its determinant is divisible by three.

To prove it, note first that an image generated by transpositions is the full
`S4` whenever it acts transitively on four letters.  The sign of the image is
the unique map

```text
pi1(S3-K) -> Z/2
```

sending a meridian to `1`, namely mod-two abelianization.  The restriction of
the `S4` quotient to its kernel surjects onto `A4`.  Killing the square of a
meridian turns this kernel into the fundamental group of the double cover of
`S3` branched over `K`; the square already maps to the identity.  Hence

```text
pi1(Sigma_2(K)) ->> A4.                                  (5.1)
```

Abelianizing (5.1), and using `A4_ab=Z/3`, gives

```text
H1(Sigma_2(K)) ->> Z/3.
```

Since `|H1(Sigma_2(K))|=det(K)=|Delta_K(-1)|`, the lemma follows.

Now

```text
det(T(2,5))=5.                                           (5.2)
```

For a cable, the Alexander formula is, up to a Laurent unit,

```text
Delta_C(p,q)(J)(t)=Delta_T(p,q)(t) Delta_J(t^p).         (5.3)
```

The `(2,+/-1)` torus pattern is an unknot.  With the standard normalization
`Delta_J(1)=1`, evaluation of (5.3) at `t=-1` gives

```text
det(C_(2,+/-1)(J))=|Delta_J(1)|=1.                       (5.4)
```

Equations (5.2)--(5.4) exclude both prime genus-two families.  Laurent-unit
normalization can change `Delta(-1)` only by sign, so it cannot affect the
determinant conclusion.

For completeness, the genus-zero infinity knot is the unknot and cannot have
a transitive transposition image on four letters.  The genus-one infinity knot
is a trefoil or mirror; its two-meridian braid presentation shows that any
transposition image moves at most three letters.  Together with the genus-two
argument, this proves (0.4).

## 6. Composite control and the ordinary-node firewall

The composite family in (4.2) is a genuine group-level survivor of the
determinant filter.  The connected sum of two trefoils, with either chirality,
has a meridian presentation

```text
G=<m,a,b | mam=ama, mbm=bmb>.                            (6.1)
```

The assignment

```text
m=(23),  a=(12),  b=(34)                                 (6.2)
```

satisfies both braid relations and generates `S4`.  Mirrors do not change this
transposition control because transpositions are their own inverses.  Thus the
determinant condition is sharp within all genus-two graph knots.

One must not claim that a bare ordinary-node relation automatically kills
(6.2).  In fact `a=(12)` and `b=(34)` are disjoint and commute, exactly the
local transposition pattern permitted by a `(2,2)` node.  To use node relators
against a hypothetical composite infinity group, one would need the actual
based identification of both local branch meridians; the abstract connected-
sum presentation does not provide it.  The present proof makes no such
unsupported identification.  It excludes (6.1) earlier and cleanly by the
one-place prime-knot theorem (3.2).

## 7. Exact delta-three primitive escape

The total-delta threshold is sharp for the group-theoretic obstruction.  Let

```text
B_3={(x,y)=(t^3,t^4)}={y^3=x^4}.                         (7.1)
```

Its normalization is `A1`; it has one place at infinity and one unibranch
affine singularity.  The semigroup `<3,4>` has gaps `{1,2,5}`, so

```text
Delta_aff(B_3)=3.                                        (7.2)
```

Its infinity knot is `T(3,4)`, the closure of the three-braid

```text
beta=(sigma_1 sigma_2)^4.                                (7.3)
```

Use the Artin action convention

```text
sigma_i:(A,B) |-> (A B A^(-1),A).
```

Starting from the fibre-meridian colors `((12),(13),(14))`, the eight letters
of (7.3) give

```text
((12),(13),(14))
((23),(12),(14))
((23),(24),(12))
((34),(23),(12))
((34),(13),(23))
((14),(34),(23))
((14),(24),(34))
((12),(14),(34))
((12),(13),(14)).                                       (7.4)
```

Thus the coloring is fixed by the closed-braid relations.  The three star
transpositions generate `S4`, so (7.4) is a transitive meridian-transposition
quotient.  Weighted radial contraction identifies the complement of (7.1)
with the `T(3,4)` knot-complement group, so this is also an affine-complement
quotient, not merely a boundary coloring.

The escape is an explicit unibranch `delta=3` horn.  Other total-delta-three
horns, including order-three tangency of two smooth branches, remain open;
the theorem does not assert that each such local type realizes an `S4`
quotient.  The `T(2,7)` unibranch type still fails the determinant test, whereas
the `<3,4>` type demonstrates that total delta alone cannot do more.

## 8. Campaign consequence and scope

The theorem closes every irreducible `A1`-normalization, one-place, connected
simple quartic lane whose complete affine singularity census has total delta
at most two.  In particular it closes, simultaneously:

* a sole order-two tangency of two smooth branches (`A3`, delta two);
* a sole unibranch `<2,5>` singularity (topological `A4`, delta two);
* any two delta-one singularities, including arbitrary node/cusp combinations;
* the predecessor's sole ordinary-node case.

No assumption about a chosen ruling, Hurwitz packet, quasipositive
factorization, or local `(2,2)` labeling is needed after the singularity delta
census is known.

The following are outside the conclusion.

1. Total affine delta at least three.  Section 7 proves this is an essential
   boundary, not an artifact of the proof.
2. Reducible curves or normalization forests with more than one component.
   Their root and smoothing Euler ledgers differ, and composite infinity knots
   need not be excluded by (3.2).
3. More than one normalization place at infinity.
4. Non-transposition generic inertia, disconnected covers, or covers of degree
   other than four.  The determinant lemma specifically uses
   `A4_ab=Z/3`.
5. Existence of a finite algebraic cover, a polynomial map, or a Keller map
   realizing the delta-three control.

## 9. Deterministic replay and firewalls

```text
ops/block_descent_a1_total_delta_two_iterated_knot_s4_replay.py
```

Ordinary, `python3 -O`, and `python3 -OO` executions are byte-identical.  The
replay:

* solves the genus-two torus/cable/connected-sum Diophantine census;
* applies the determinants `5`, `1`, and `9`;
* verifies the composite presentation (6.1)--(6.2), including a compatible
  disjoint commuting pair;
* exhausts all transposition triples for the braid (7.3), finding 24 labelled
  transitive `S4` colorings and the explicit witness (7.4);
* computes the semigroup gaps `{1,2,5}` of `<3,4>`.

Its mutation

```text
python3 ops/block_descent_a1_total_delta_two_iterated_knot_s4_replay.py \
  --mutate-exclude-delta-three
```

exits nonzero because the exact `T(3,4)` coloring survives.

The replay does not encode the corrected Neumann--Rudolph lemma, local Milnor
fibre theory, Neumann's minimal-Seifert or rooted-splice theorems, Schubert's
genus and primeness results, the infinity-to-affine group quotient, or the
double-branched-cover group identification.  Those are the written theorem
interfaces above.

Nothing here proves JC2, alters campaign ledgers, or touches the formalization
tree.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17754`.
- Body SHA-256:
  `4a7283350f8ead55bb7fa4afb36a07677387db02a86456e575eb5f40a32555e4`.
- Frozen basis: `adb847313c6c946d893100a2cd4c8226a5cc2f0c`.
