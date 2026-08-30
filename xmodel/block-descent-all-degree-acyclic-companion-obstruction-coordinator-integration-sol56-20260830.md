# Coordinator integration: all-degree acyclic-branch obstruction

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, campaign coordinator  
Frozen basis: `7afc73b69182b7fc7b33b1153bb945469668f00e`  
Lifecycle: **REVIEW-INTEGRATED PROMOTED THEOREM**

## 0. Verdict

Fable 5 independently reconstructed the arbitrary-degree cover theorem, both
Euler extensions, the canonical-normalization interface, and the degree-three
corollary.  Its verdict is `CONFIRM_WITH_CORRECTIONS`; no conclusion is
retracted.  This integration binds the three substantive obligations:

1. the generic disk-meridian argument now explicitly uses analytic
   irreducibility of the normal excellent local factor;
2. Chau's primary source is pinned and hash-charged locally; and
3. the degree-three point-count explicitly includes singular branch values.

The resulting promoted conclusion is:

> For the canonical normalization of every hypothetical noninvertible complex
> plane Keller map, the reduced branch support has a connected component with
> nontrivial fundamental group.  In particular, no complex plane Keller map
> has generic field degree
> `[C(x,y):C(F,G)]=3`.

The first sentence is an all-degree necessary condition, not a proof of JC2.
It does not show that the branch is connected, classify its cyclic components,
or exclude degree four or higher.

## 1. Frozen evidence

```text
28f29711366f58f4a1c9e6e5d7f16d8e6ca29fddf730bfd436100da04e4d2eda
  xmodel/block-descent-all-degree-acyclic-companion-obstruction-sol56-20260830.md
3d0b72c7001bf403fa334f746dd09a21d8a55fc8074f9b4680e249b92f73beb3
  xmodel/block-descent-all-degree-acyclic-companion-obstruction-sol56-20260830.md.artifact.json
aecd3a826af11bcc6e9c0eaeeca2ebf2551d110a40f38d15f5f131dd97f1889e
  xmodel/block-descent-all-degree-acyclic-companion-obstruction-hostile-review-fable5-20260830.md
b3bdd87cb27b614ca4bac476fd7f4c676b9551026397f3a895dbf84f4f195419
  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-coordinator-addendum-sol56-20260830.md
95c99e2d271df25d80b3200e777c268a80c5ce9d6b2671168d6f76c16d8a2611
  xmodel/block-descent-canonical-normalization-degree3-coordinator-integration-sol56-20260830.md
5d7df7ce0ad3548e88fd23734917212d6b3fbd3ada4cab81514b12bb76ea64de
  xmodel/block-descent-a1-quartic-branch-topology-coordinator-integration-sol56-20260830.md
8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f
  refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf
```

The last file is the nine-page arXiv source `math/0305088v1`, Nguyen Van
Chau, *Non-proper value set and the Jacobian condition* (published in
Annales Polonici Mathematici 84 (2004), 203--210, DOI
`10.4064/ap84-3-2`).  Theorem 1 polynomially parametrizes every irreducible
component of the nonproper-value curve of a Keller map; Corollary 2 gives the
one-point-at-infinity statement.  The PDF was downloaded directly from the
arXiv PDF endpoint and checked with `pdfinfo` and `pdftotext`.  Only the
componentwise polynomial parametrization is needed below.

Fable's external run passed receipt-first custody.  The unsealed report body
was `49a081ea...`, the completed run receipt was `1f785c08...`, and the log
was `3f7c07fb...`; all prompt, adapter, launcher, sandbox, validator,
fallacy, and composed-model-prompt hashes reproduced exactly before the
report was read.  The sealed review is the third charged file above.

## 2. Arbitrary-degree local inertia repair

Let

```text
pi:X -> A2_C
```

be finite flat of degree `d>=2`, with `X` integral and normal.  Let `B` be
the reduced image of the non-etale locus and put

```text
U=X-NonEt_X(pi).
```

At the generic point `eta_D` of every irreducible component `D` of `B`, the
semilocal finite algebra over the DVR `O_(A2,eta_D)` has at least one
ramified DVR factor.  In characteristic zero its ramification index is
`e>=2`; a generically unramified factor of residue degree `f` contributes
exactly `f` fixed sheets after specialization to a general complex closed
point.

The missing articulation is the passage from this height-one statement to a
disk meridian.  Choose a general smooth closed point `b` of `D`, away from
the finitely many other branch and specialization strata, and a point `x`
on a ramification component dominating `D`.  The local ring `O_(X,x)` is an
excellent normal local domain.  Its completion is normal and local, hence a
domain: the corresponding analytic surface factor is analytically
irreducible.  After restricting to a sufficiently small transverse disk at
`b`, that local factor is therefore one connected ramified disk cover, so
the meridian acts by a single cycle of its local rank.  Since one dominating
ramification component has `e>=2`, the generic meridian is nonidentity.

This is the arbitrary-degree version of the already reviewed cubic repair
`b3bdd87c...`.  It is load-bearing: without normality,
`z^2=x^2y` has a conductor branch with identity meridian.  The argument does
not identify companion labels across distinct branch components or across
different based meridians.

At a particular closed branch point, a rank-one direct factor of the
henselian fibre algebra is a local section: a rank-one finite flat algebra
over the henselian local base is the base itself.  Hence its sheet is fixed
by the complete local monodromy group.

## 3. Promoted cover theorem

The following two versions are now promoted.

### 3.1 Pointwise companion version

Assume additionally that `B` is nonempty, connected, and simply connected,
and that the henselian fibre algebra at every point of `B` has a rank-one
direct factor.  Then no such cover exists.

Arzhantsev--Zaidenberg classify connected reduced simply connected plane
curves, up to an automorphism of `A2`, as a line/comb or a weighted cone.  In
the comb case the complement group has a central spine meridian.  Section 2
makes its image nonidentity, while the companion makes its fixed set nonempty
and proper.  Centrality makes that fixed set invariant under the transitive
global monodromy, a contradiction.  In the weighted-cone case radial
scaling identifies the global complement group with the local group at the
vertex; its rank-one factor fixes a sheet, again contradicting transitivity.

The connectedness hypothesis is essential.  Fable supplied the sharp
degree-three control

```text
(t,y) |-> (3t^2-2t^3,y),
```

whose branch is two parallel lines, whose local partition is `(2,1)` with a
companion everywhere, and whose global monodromy is transitive `S3`.

### 3.2 Generic companion plus Euler version

Assume instead that every irreducible component of `B` has a generically
unramified sheet, every connected component of `B` is simply connected, and

```text
e_c(U)>0.                                                (3.1)
```

Then no such cover exists, whether or not `B` is connected.

For a connected line/comb, the central-meridian proof applies when the
vertex/spine companion persists; otherwise the drop-only constructible fibre
census gives `e_c(U)<=0`.  For a connected weighted cone, the same dichotomy
is supplied by its vertex and by the weighted radial Euler calculation.  If
`B` is disconnected, Arzhantsev--Zaidenberg make it a union of `r>=2`
parallel lines.  Writing `s_i` for the support size and `c_i` for the number
of nontrivial cycles of the `i`th generic inertia, transitivity gives

```text
sum_i(s_i-c_i)>=d-1,
sum_i s_i>=d-1+r>=d+1,
e_c(U)<=d-sum_i s_i<=-1,                                (3.2)
```

contrary to (3.1).  The strict positivity in (3.1) cannot be weakened:
normal cusp and quartic weighted-cone controls attain `e_c(U)=0`.

## 4. Canonical normalization of a Keller map

For a hypothetical noninvertible Keller map

```text
F:A2 -> A2,             K=C(F,G) subset L=C(x,y),
```

let `S` be the integral closure of `C[F,G]` in `L`, `Y=Spec(S)`, and
`pi:Y->A2` the finite normalization map.  Integrality and the normality of
`C[x,y]` give `S subset C[x,y]`, hence a factorization

```text
A2 --j--> Y --pi--> A2.
```

Here `Y` is a normal Cohen--Macaulay surface, `pi` is finite flat of generic
degree `d=[L:K]`, and Zariski Main makes the birational quasi-finite map `j`
an open immersion.  If `R=NonEt_Y(pi)_red` and `U=Y-R`, then `R` is contained
in `Y-j(A2)`, while `j:A2->U` is an everywhere-defined dominant etale
morphism.

The reviewed ruling theorem applies at first-leg degree one: `U` is a smooth
rational affine surface with constant units and logarithmic Kodaira dimension
`-infinity`, carrying an `A1`-fibration over `A1` or `P1`.  Therefore

```text
e_c(U)=e_c(C)+Q>=1.                                     (4.1)
```

For every irreducible branch component `D`, the nonconstant polynomial
`p_D(F,G)` vanishes on a source curve inside the etale chart.  Its image is
dense in `D`; consequently `D` has a generically unramified sheet.  Applying
Section 3.2 and (4.1) proves:

```text
some connected component of B=pi(R)_red has pi1 != 1.   (4.2)
```

This is the promoted all-degree branch-topology obstruction.

## 5. Chau pin and the degree-three endpoint

Approaching a point of `R` through `j(A2)` produces an escaping source
sequence with convergent image, so each component of `B` is an entire
component of the nonproper-value curve `A_F`.  The pinned Chau theorem gives
a nonconstant polynomial map `A1->B_i`.  It lifts to the normalization and
extends to a surjective map of projective normalizations.  All finite source
points remain affine, so at most the one source point at infinity lies over
the projective boundary; affineness supplies exactly one puncture.  Thus

```text
Norm(B_i)=A1.                                           (5.1)
```

At generic degree three, every non-etale local factor has rank at least two.
Two such factors cannot fit in total rank three.  This argument is pure rank
arithmetic and remains valid when the point of `Y` or the branch value is
singular.  Hence `R_red->B` is finite and point-bijective, and therefore a
homeomorphism in the complex topology.

The morphic rational-forest theorem applied to `j:A2->U`, together with
(5.1), gives

```text
e_c(R_red)=e_c(B)=h=b0(B)>=1.                           (5.2)
```

Let `S0` be the finite set of branch values without an unramified sheet.  The
degree-three fibre census and ruling identity give

```text
e_c(U)=3-2h-|S0|=e_c(C)+Q.                              (5.3)
```

For `C=P1`, (5.3) would read `2h+|S0|+Q=1`, impossible.  For
`C=A1`, it has the unique solution

```text
h=1,                 S0=empty,                 Q=0.     (5.4)
```

The forest and (5.1) then make `B` connected and simply connected, while
`S0=empty` gives a rank-one factor at every point.  Section 3.1 contradicts
the existence of the cover.  Therefore

```text
[C(x,y):C(F,G)] != 3.                                  (5.5)
```

This reaffirms the previously promoted degree-three endpoint with the last
primary-source trust boundary now pinned.

## 6. Firewalls and next frontier

The theorem requires normality of the finite cover; the nonnormal conductor
control shows why.  The pointwise version requires connected branch, and the
Euler version requires strict positivity.  Neither version propagates a
named fixed sheet between unrelated meridians.

Equation (4.2) says only that at least one connected branch component has
nontrivial `pi1`.  It does not imply `B=A_F`, connectedness of `A_F`, or any
classification of the cyclic branch.  At degree four, `(2,2)` values make
`R_red->B` noninjective and can create exactly the required cycle.  The live
minimal rank-four row is therefore not touched by the degree-three
homeomorphism argument.

The useful degree-four successors are now embedding-sensitive: the
zero-cusp horn requires global polynomial one-place braid/Puiseux control;
the no-cusp discriminant double plane requires the anti-invariant
`H^1_et(-,Z/3)` class; and the one-cusp horn requires the actual polynomial
pair on its affine pseudo-plane.  No result here excludes primitive field
extensions without a proper block, constructs a counterexample, or proves
JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12035`.
- Body SHA-256:
  `05c5c299adaa96b772ec45378249978756719c3ecabf359ba5e10e94e7c05c9b`.
- Frozen basis: `7afc73b69182b7fc7b33b1153bb945469668f00e`.
