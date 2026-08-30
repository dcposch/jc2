# Coordinator integration: reduced bidegree-(2,3) rational-forest locus

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen basis: `4c91d6fc398d1b4f2b8ca1a11d69c4bb3fef9c0d`  
Lifecycle: **BINDING INTEGRATION / REDUCED SQUAREFREE INFINITY SCOPE**

## 0. Disposition and custody

Fable 5 independently reconstructed the sealed producer

```text
d783cecfcc818f1ec5c056fa04126c21dab0f17c073d11d8e230703b9755feaa
  xmodel/bd-a2-firstleg-bidegree23-rational-forest-classification-sol56-20260830.md
  body 13761 / b76971e671237b906d4c772ec4008e7153ca6f47705cc994839fef33c12a604e
```

and returned `CONFIRM_WITH_CORRECTIONS`.  Its sandbox-attested raw review body
is

```text
77d489d7168ce40079c0806bc485c6c444446ec3ea759bdd15ad5c2007ead5aa
  xmodel/bd-a2-bidegree23-rational-forest-classification-hostile-review-fable5-20260830.md
```

and its sealed full-file SHA-256 is
`8db0d0f8ae48434e538b83e8e16f2ca9ba8deecc90b40568570c4fc2b7065ecb`.
The clean schema-v2 receipt has exit code zero and pins unchanged prompt,
adapter, launcher, Seatbelt profile, validator, fallacy appendix, and composed
model-prompt hashes.

The review finds no mathematical error and no false type row.  This
integration adopts its two scope repairs: `F8,F9` are factorization types but
have no forest refinement, and common coefficient zeros at an affine target
point are invisible to the infinity restriction and remain a separate
normality/finiteness/etaleness client.

## 1. Exact genus-budget theorem

Let `C` be a reduced divisor of class `(2,3)` on
`S=P1 times P1`.  Let `C_i` be its irreducible components, let `g_i` be their
normalization genera, and for each singular point `p` let `delta_p` be its
delta invariant and `r_p` its number of analytic branches.  Put

```text
G(C)=sum_i g_i,
K(C)=sum_p(delta_p-r_p+1),
B(C)=b1(branch-incidence multigraph).
```

Every such divisor is connected: the ideal sequence and Kunneth give
`H^1(S,O(-2,-3))=0`.  Adjunction gives `p_a(C)=2`.  Normalization and the
connected branch-incidence graph give

```text
2 = G(C)+B(C)+K(C),                                  (1.1)
```

and each summand is nonnegative.  Replacing a singular-point vertex by its
embedded-resolution exceptional tree preserves `b1`, including loops and
parallel edges.  Hence:

> The reduced total transform of `C` on any embedded log resolution has only
> rational components and forest—necessarily tree—dual multigraph if and
> only if `K(C)=2`.

The identity covers reducible curves, disconnected normalization, arbitrary
branch count, and nonordinary singularities.  A two-branch contact of order
`m` contributes `m-1`; an ordinary triple point contributes one.

## 2. Exhaustive factorization table

There are exactly nine unordered reduced component-degree partitions.  The
rational-tree locus is nonempty exactly in `F1`--`F7`:

```text
F1  (2,3)
    rational normalization; either two A2 cusps or one A4 cusp.

F2  (0,1)+(2,2)
    the (2,2) component has one A2 cusp; its intersection with the ruling
    fibre is supported at one point with length two.

F3  (1,0)+(1,3)
    the two components have one length-three contact.

F4  (1,1)+(1,2)
    the two components have one length-three contact.

F5  (0,1)+(1,1)+(1,1)
    all three meet at one point; the two (1,1) components have contact two.

F6  (0,1)+(1,0)+(1,2)
    all three meet at one point; the (1,0) and (1,2) components have
    contact two.

F7  (0,1)+(0,1)+(2,1)
    the (2,1) component has one length-two contact with each of the two
    disjoint ruling components.

F8  (0,1)+(0,1)+(1,0)+(1,1)       impossible: K<=1.

F9  3(0,1)+2(1,0)                  impossible: K=0, B=2.
```

These conditions are necessary and sufficient within their factorization
types.  Every viable row has an exact witness.  In particular irreducible
survivors genuinely occur: normalization maps of bidegrees `(3,2)` give

```text
t |-> (t^3,t^2)                         two A2 cusps,
t |-> (t^2/(1-t^3),t^2)                 one A4 cusp.
```

The review checks injectivity, all finite poles, infinity charts, and the
claimed local delta invariants.  Thus reducibility is not forced.

## 3. Exact Miranda typing

For a fixed-basis quadratic Miranda presentation, the leading binary cubic

```text
F_infinity(s,t;X,Y)
 = b_2 X^3-3a_2 X^2Y+3d_2 XY^2-c_2 Y^3
```

ranges over all of `H^0(O(2,3))`.  Therefore the theorem governs precisely
the presentations for which this leading form is squarefree: all nine
factorization types are present in the ambient family, and the infinity-curve
test retains exactly `F1`--`F7`.

The following interfaces remain distinct:

* a simple common factor of the four leading quadratics gives a projective
  coefficient basepoint and a `(1,0)` factorization type (`F3,F6,F8,F9`);
* a fixed fibre root gives a `(0,1)` component and is not by itself target-
  degree drop;
* a repeated leading factor is nonreduced and must be squarefreed/retyped;
* simultaneous vanishing of all four leading quadratics is literal target-
  degree drop and returns to degree at most one;
* a common zero of the full coefficient sections at an affine target point is
  invisible to `F_infinity` and remains a separate normality/finiteness/
  etaleness condition.

## 4. Binding campaign consequence

Combine this classification with the promoted rational-forest first-leg
theorem.  A fixed-basis quadratic Miranda incidence with squarefree infinity
can admit a dominant rational `A2` first leg only if its infinity divisor lies
in one of `F1`--`F7`.  This is necessary only.  The next finite gate is the
resolved union of infinity with reduced ramification support; any positive-
genus ramification component or new graph cycle excludes the presentation.

No ramification-support exclusion, general quadratic or cubic block closure,
basis-minimization theorem, primitivity result, map existence/nonexistence,
counterexample, or JC2 statement is promoted.  Nonreduced infinity, singular
ambient closure, affine coefficient zeros, projective basepoints, and both
fibre/target degree drops retain their separate lifecycle entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6106`.
- Body SHA-256:
  `9371f0961222e0db02f1d9e7d2bb5fb20f3d857b1b0cf0a7cb021c1d23faefce`.
- Frozen basis: `4c91d6fc398d1b4f2b8ca1a11d69c4bb3fef9c0d`.
