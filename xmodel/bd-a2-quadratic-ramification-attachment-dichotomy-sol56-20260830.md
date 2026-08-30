# Quadratic Miranda infinity: ramification-attachment dichotomy

Date: 2026-08-30 UTC  
Producer: Sol 5.6 Ultra coordinator  
Frozen basis: `4c91d6fc398d1b4f2b8ca1a11d69c4bb3fef9c0d`  
Lifecycle: **EXACT CONDITIONAL PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint

This packet combines the promoted rational-forest obstruction with the
promoted reduced bidegree-`(2,3)` classification.  On the projectively finite
smooth quadratic-incidence stratum, it reduces the seven exact infinity types
to one sharp dichotomy:

```text
dominant block morphism A2 -> U
+ reduced rational-forest infinity H
+ irreducible reduced ramification support
=> H has type F5.                                      (0.1)
```

Here `F5=(0,1)+(1,1)+(1,1)` with all three components through one point and
the two `(1,1)` components tangent there.  Types `F1,F2,F4,F7` force at least
two distinct attachments of the irreducible ramification closure to the
connected infinity tree, hence a boundary cycle.  Types `F3,F6` have a
projective coefficient basepoint, so they lie outside the projectively finite
hypothesis and remain separate.  The rational-forest refinements of `F8,F9`
are empty, although those factorization types themselves exist.

Equivalently, within the smooth projectively finite scope and without
assuming ramification irreducibility, every reduced quadratic survivor enters
at least one of

```text
R_red reducible;       F5 one-point triple collision.  (0.2)
```

The projective coefficient-basepoint types `F3,F6` are a separate branch
outside the finiteness hypothesis.  This is a presentation-scoped boundary
reduction.  It proves neither that `F5` occurs nor that reducible ramification
survives.  It says nothing about nonreduced infinity, singular incidence
surfaces, literal fibre-degree drop, or target-degree drop.

## 1. Frozen inputs and hypotheses

The inputs are

```text
6a8558e42a67f1ec5c8bcf12321b6e6805b30a570eba17862c6e7e24cd631b08
  promoted rational-forest coordinator integration
e3dc96f07825ea882edc3d2701e9f0a0357ae863c062ad695d9377a37aa2b761
  promoted bidegree-(2,3) classification coordinator integration
  body 9371f0961222e0db02f1d9e7d2bb5fb20f3d857b1b0cf0a7cb021c1d23faefce
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  promoted block-descent structure integration.
```

Let `X` be a smooth irreducible quadratic Miranda incidence surface in
`P2 times P1`, and let

```text
pi:X -> P2
```

be projection.  Assume `pi` is finite in a neighbourhood of
`H=pi^{-1}(L_infinity)`, that `H` is reduced of bidegree `(2,3)`, and that the
affine block first leg has image in `U=Y minus R_red`, where
`Y=X minus H` and `R_red` is the reduced ramification support of `pi|Y`.
Let `Rbar` be its closure in `X`.  Resolve the reduced divisor
`H union Rbar` without deleting branch multiplicities from the dual
multigraph.

The promoted first-leg theorem says that a dominant rational `A2 -> U`
forces every resolved boundary component to be rational and the entire dual
multigraph to be a forest.  The promoted classification then restricts `H`
to the exact types `F1`--`F7`.

## 2. Attachment-cycle lemma

Let `T` be a connected reduced divisor whose embedded-resolution graph is a
tree, and let `Q` be an irreducible curve not contained in `T`.  If the
normalization of `Q` has two distinct branches at the boundary `T`—whether
over two physical points or as two analytically distinct attachments resolved
over one point—then the resolution graph of `T union Q` contains a cycle.

Indeed, contract every resolution subtree belonging only to one local
attachment.  The strict transform of `Q` supplies one vertex and the
connected tree for `T` supplies a unique path between the two attachment
vertices.  The two attachment edges together with that path and the `Q`
vertex form a cycle.  Tangency multiplicity along one analytic branch only
subdivides or lengthens one attachment path and does not create a second
edge.

Consequently, if the full resolved boundary is a rational forest, every
irreducible component of `Rbar` is rational and has at most one distinct
normalization branch along the connected infinity tree `H`.

## 3. Critical points are ramification attachments

Work near a point of `H` in a fibre chart.  Write target coordinates `(u,v)`
with `L_infinity={u=0}`, fibre coordinate `z`, and

```text
X: f(u,v,z)=0,            H: f(0,v,z)=0.
```

Finiteness gives a genuine cubic in `z`; the ramification support is
`f=f_z=0`.  Let a normalization branch of `H` be
`t |-> (v(t),z(t))`.  At a smooth point of that branch, a critical point of
the map to `L_infinity` has `v'(t)=0` and `z'(t)!=0`; differentiating the
equation gives `f_z=0`.  At a singular point of the reduced curve `H`, both
partials of `f(0,v,z)` vanish, again giving `f_z=0`.  Thus every critical
point of a normalized nonvertical component, and every collision point of
distinct components, is an attachment to `Rbar`.

The closure assertion uses the existing smoothness, reducedness, and
finiteness hypotheses.  On smooth `X`, `f_z=0` cuts the ramification as a
Cartier divisor.  It has no component contained in `H`: at the generic point
of a reduced factor of `f(0,v,z)`, divisibility of both `f` and `f_z` would
make that factor independent of the fibre coordinate, producing a vertical
component and a positive-dimensional fibre, contrary to finiteness near
`H`.  Hence every ramification point on `H` is approached by ramification
points off `H` and lies in the closure of the affine support `R_red`.

For a smooth rational component of bidegree `(a,b)`, projection to the first
`P1` has degree `b`.  Riemann--Hurwitz gives total ramification

```text
2b-2.                                                   (3.1)
```

A point contributes at most `b-1`; hence a component with `b=2` or `b=3`
has at least two distinct critical points.  In the forest types at issue,
the normalization maps are injective on physical points: otherwise their
branch-incidence graph would already contain a cycle.  Those critical points
therefore give at least two distinct attachments to `Rbar`.

## 4. Type-by-type consequence

Use the promoted classification's orientation, in which `(a,b)` has
degree `b` over the target line at infinity.

* `F1=(2,3)`: the rational normalization has degree three.  Its ramification
  degree is four and has at least two distinct support points, including in
  both the two-`A2` and one-`A4` cases.
* `F2=(0,1)+(2,2)`: the rational cuspidal `(2,2)` component has degree two,
  hence two distinct critical points.  A cusp or the prescribed length-two
  contact may account for one, but cannot identify the two normalization
  points.
* `F4=(1,1)+(1,2)`: the `(1,2)` component has degree two and therefore two
  distinct critical points, regardless of which one participates in the
  length-three component contact.
* `F7=(0,1)+(0,1)+(2,1)`: every normalized component maps with degree one,
  but the `(2,1)` component has length-two contact with each of two disjoint
  `(0,1)` components.  The two collision points are distinct, and at each the
  cubic and its fibre derivative vanish.

If `Rbar` is irreducible, the two attachments in any of these four cases lie
on the same ramification vertex and contradict the attachment-cycle lemma.

In `F5`, all three degree-one components and their entire excess-contact
budget meet at one physical point.  The preceding support-count argument
forces only one ramification attachment and therefore does not exclude this
type.  A local different/normality computation is still required.

Types `F3` and `F6` contain a `(1,0)` component.  Equivalently all four
quadratic leading coefficient forms share a target-direction factor, so
`pi` is not finite over that infinity direction.  They must be handled by a
projective-basepoint blowup chart and are not conclusions of (0.1).

## 5. Reducible-ramification successor

There is a useful exact algebraic constraint on the reducible branch of (0.2).
Dominance of the block morphism `A2 -> U` forces

```text
O(U)^*=C^*,             O(Y)^*=C^*.                  (5.1)
```

Indeed every unit pulls back to a unit of `C[x,y]`, hence to a constant, and
density makes the original unit constant.  The localization sequence for a
normal affine `Y` therefore makes the component-class map

```text
Z^{components(R_red)} -> Cl(Y)                       (5.2)
```

injective.  Thus a reducible ramification support requires at least that many
independent divisor classes.  Computing `Cl(Y)` on `F1,F2,F4,F7` is the
cheapest next gate: rank at most one would force ramification irreducible and
combine with (0.1) to eliminate those four types.

The remaining finite queue is then:

1. class groups and ramification-component classes on `F1,F2,F4,F7`;
2. the local different at the one-point `F5` triple collision;
3. separate blowup charts for the coefficient-basepoint types `F3,F6`.

## 6. Nonclaims

This packet consumes the promoted nine-type curve classification and itself
needs different-model review.  It does not prove
ramification support irreducible, compute a class group, exclude `F5`, repair
projective basepoints, or treat a nonreduced or singular ambient closure.
It proves no basis-minimization theorem, general quadratic or cubic block
closure, primitivity statement, source occurrence, polynomial map,
counterexample, or JC2 result.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9399`.
- Body SHA-256:
  `c37282a42af45c57e723dddd061ce2681203564df1b76008e8001206b2c69199`.
- Frozen basis: `4c91d6fc398d1b4f2b8ca1a11d69c4bb3fef9c0d`.
