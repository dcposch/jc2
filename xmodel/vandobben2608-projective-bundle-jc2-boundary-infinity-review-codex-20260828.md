# Source audit and JC2 ideation: projective-bundle complements and an essential fork at infinity

Date: 2026-08-28 UTC  
Status: **PRIMARY-SOURCE-CHECKED / PLANE ANALOGUE DECIDED / JC2 VERDICT `REDESIGN`**  
Scope: no canonical-file or Lean edits; no CAS or heavy computation.

## 0. Source custody and headline

Primary source:

- Remy van Dobben de Bruyn, *Divisors in projective bundles over the
  projective line whose complement is affine space*, arXiv:2608.27341v1,
  12 pages, 2026-08-27.
- Local source:
  `refs/vandobben2026_projective_bundle_complements_affine_space_arxiv2608.27341v1.pdf`.
- Exact PDF SHA-256:
  `ad2b2f112a5c61b101758cd45f38339a69a7e3ce6343dfa81e87f784298298c6`.

Independent verdict:

> The paper appears mathematically useful and essentially sound in its
> stated special geometry, but it supplies no new plane-Keller restriction
> without a global source/target boundary-landing theorem.  Its direct
> two-dimensional symmetric-power analogue fails completely: for a
> non-tangent line the two boundary curves have the same Picard class, and
> for a tangent line the source is explicitly
> `A^1 x G_m`, not `A^2`.  The genuinely reusable delta is a fail-fast
> **weighted minimal-boundary / fundamental-group-at-infinity checksum**.
> This is a redesign of existing boundary-tree and source-filling work, not
> a new avenue.

The recommended campaign action is:

```text
STOP       naive Sym^2 descent of the dimension-three construction;
REDESIGN   the new source as one full-boundary, ordinary-minimalization filter;
HOLD       any universal JC2 claim until source/target label custody is proved;
CONTINUE   only one bounded essential-fork discriminator on a fully completed graph.
```

## 1. What the source actually proves

Let `X=P(E)->P^1`, where `E` has rank `n>=2`, and write
`Pic(X)=Z f + Z h`, with `f` the pullback of `O_{P^1}(1)` and `h` the
relative hyperplane class.  For two distinct irreducible divisors

```text
D ~ d f + h,        E' ~ e f + h,
```

Theorem 3.1 says, over the characteristic-zero/topological perimeter used
in the proof,

```text
X \ (D union E') ~= A^n
iff
e=d+-1 and the torsion part of coker(L+M -> E) has length one.
```

For `n=2`, `X` is a Hirzebruch surface and the last condition is exactly
that the two smooth sections meet in one reduced point.  If instead they
meet at a single point with multiplicity `k>1`, `k` successive blowups give
the SNC dual graph `D_{k+2}`: the last exceptional curve is the trivalent
vertex, the strict transforms of the two sections are two leaves, and the
earlier exceptional curves form the third arm.  Ramanujam's weighted-boundary
criterion then gives a nontrivial fundamental group at infinity.

The appendix applies this to

```text
P^1 x Sym^2(P^1) -> Sym^3(P^1),
(p,{q,r}) |-> {p,q,r},
```

whose ramification and pulled-back hyperplane have relative classes
`(2,1)` and `(1,1)`.  Their class difference is one, and a
tangent-but-not-osculating hyperplane produces the required reduced
one-fibre intersection.  This explains why the source complement of the
dimension-three counterexample is `A^3`.  It does not address a hypothetical
plane Keller map.

### 1.1 Proof audit

The load-bearing steps check out at theorem-design level:

1. The units/Picard localization sequence forces exactly two irreducible
   boundary components and makes their classes a basis when the complement
   is affine space.
2. Linear projection away from the common rank-`n-2` projective bundle
   reduces the complement to an affine-plane complement times `A^(n-2)`.
3. Affineness, `Pic=0`, splitting on `P^1`, and vanishing of quasi-coherent
   `H^1` trivialize the affine-bundle torsor.
4. The cited cancellation theorem reduces recognition to the Hirzebruch
   surface.
5. In dimension two, two smooth sections with contact `k>1` really do
   produce `D_{k+2}` after the final blowup separates the triple point.

One small proof-writing omission is harmless but should not be copied.  The
Grothendieck-ring computation gives

```text
[U] = L^n + (r-1)L^(n-2).
```

Concluding `r=1` is not licensed merely by cancellation inside
`K_0(Var)`, where `L` is a zero divisor.  Applying the Hodge--Deligne
polynomial over `C` (or an appropriate compactly supported realization)
immediately gives `r=1`.  Thus this is an omitted one-line realization, not
a substantive failure.

The topological necessity of reducedness is genuinely complex/topological;
the author explicitly leaves its positive-characteristic analogue open.

## 2. Exact `n=2` symmetric-power analogue: it is not `A^2`

Consider the obvious quotient/forgetful map

```text
q : P^1 x P^1 -> Sym^2(P^1) ~= P^2,
(p,q) |-> {p,q}.
```

Let `C` be the image of the diagonal, a smooth conic, let `H` be a line in
`P^2`, and set

```text
R = Ram(q),
U_H = (P^1 x P^1) \ (R union q^(-1)(H)),
V_H = P^2 \ H ~= A^2.
```

Then `q|U_H : U_H -> V_H` is generically degree two and etale, but its
source is never `A^2`.

### 2.1 Ramification and hyperplane classes

The swap involution has fixed divisor the diagonal, so in characteristic
zero

```text
R = Delta,             [R]=(1,1) in Pic(P^1 x P^1).
```

The symmetric-polynomial quotient is bihomogeneous of degree `(1,1)`, hence

```text
q^* O_{P^2}(1) = O_{P^1 x P^1}(1,1),
[q^(-1)(H)] = (1,1).
```

Thus the two natural boundary divisors have the **same** class.  This is the
dimension-two failure of the dimension-three class difference
`(2,1)-(1,1)=(1,0)`.

### 2.2 Non-tangent line

Write a line on `Sym^2(P^1)` as a symmetric bilinear form on the two
factors.  If `H` is not tangent to `C`, that form has rank two, so
`E_H=q^(-1)(H)` is an irreducible `(1,1)` curve.  The localization sequence
gives

```text
Pic(U_H)
  = Pic(P^1 x P^1) / <[Delta],[E_H]>
  = Z^2 / <(1,1)>
  ~= Z.
```

Since `Pic(A^2)=0`, `U_H` is not `A^2`.  Equivalently, if an `A^2`
complement had two irreducible boundary components, their classes would have
to be a basis of `Pic(P^1 x P^1)`; two copies of `(1,1)` are not.

### 2.3 Tangent line: an explicit identification

If `H` is tangent to the conic `C` at the divisor `2p`, its symmetric
bilinear form has rank one.  Therefore it factors as

```text
q^(-1)(H) = ({p} x P^1) union (P^1 x {p}).
```

Move `p` to infinity.  Removing these two rulings leaves `A^1 x A^1`, and
removing the ramification diagonal leaves

```text
U_H = {(x,y) in A^2 : x != y}
    ~= A^1 x G_m,
(x,y) |-> (x,y-x).
```

The unit `y-x` is nonconstant, so this is not `A^2`.  In the boundary
localization sequence the three components have classes

```text
(1,1), (1,0), (0,1),
```

and their one relation is exactly the source of this unit.  Resolving the
triple boundary point gives a `D_4`-shaped graph, but after ordinary
minimalization it becomes a linear two-vertex graph with determinant zero;
the nontrivial topology is in the weights/group, not in the bare presence of
a fork.

This settles every line `H`: the naive plane analogue never has affine-plane
source.  It is an instructive negative control, not a candidate JC2
counterexample.

## 3. Deduplication against the repository

This source is not a fresh campaign lane.

- `xmodel/websweep-20260828T0524Z.md` already records the exact PDF SHA, the
  projective-bundle criterion, the `D_{k+2}` obstruction, and the same-class
  obstruction to the obvious plane analogue.
- `APPROACHES.md` avenue 2 is already the Sigray--Orevkov resolved
  boundary-tree backbone; avenue 27 already covers links, splice diagrams,
  and plumbing; avenue 35 already records the structural failure of
  dimension-three descent.
- `ladder/SHEET6-CLASSICAL.md` already ran splice/link-at-infinity tests on
  the live two-pole genome.  The pinned skeleton passes, while the full
  weighted graph is unavailable because the `B`- and `x`-side resolution
  tails are unpinned (§3b).
- `xmodel/ideation-20260824T0719Z-atlas.md` already proposes a source-filling
  presentation coupling target inertia to the fact that the filled source is
  `A^2`.
- `xmodel/ideation-20260827T2137Z-grok46-face-hostile-review-sol-ultra.md`
  already isolates the missing map from face/boundary loops to target
  asymptotic meridians.  A shared label is not a loop map.

The independent delta here is narrower:

1. the tangent plane analogue is explicitly `A^1 x G_m`;
2. the non-tangent analogue has `Pic ~= Z`;
3. the smallest honest Ramanujam client is an **essential weighted fork that
   survives ordinary source-boundary minimalization**, not a nonlinear
   map-relative subgraph.

## 4. The smallest precise bridge worth naming

Let `F:A^2_C -> A^2_C` be a hypothetical nonproper Keller map.  Resolve its
extension as in Orevkov:

```text
Phi : X -> P^1 x P^1,
D = X \ A^2.
```

Write `D_infty` for the reduced inverse image of the target boundary and
write `D_fin=D-D_infty` for the finite-image boundary.  Orevkov's regularized
model makes every connected component of `D_fin` a linear branch attached
once to `D_infty`, ending in a nonconstant finite-image component after any
constant components.

Now perform an **ordinary Ramanujam minimalization** of the full pair `(X,D)`:
choose a maximal sequence contracting boundary `(-1)`-curves meeting at most
two other boundary components, without requiring `Phi` to descend.  (No
uniqueness of the resulting minimal completion is assumed.)  Denote the
chosen weighted graph by `Gamma_min`.  For an induced connected branch `T`, let
`pi(T)` be the fundamental group of its plumbing boundary in Ramanujam's
sense; call `T` nonspherical when `pi(T)` is nontrivial.

The smallest useful missing statement is:

> **KEF — Keller essential-fork bridge.**  If `F` is nonproper, then there
> is an ordinary minimalization for which `Gamma_min` has a vertex `v` with
> at least three nonspherical components `T_1,T_2,T_3` of `Gamma_min-v`.
> Moreover at least one of
> these branches carries a surviving target-pole label from `D_infty` and at
> least one carries a surviving finite-image/dicritical label from `D_fin`.

Why this is enough is one line.  The full boundary compactifies the source
`A^2`, so its fundamental group at infinity is trivial.  Ramanujam's Lemma 4
(the Mumford free-product lemma) says that at a vertex of a boundary graph
with trivial plumbing group, at most two branches can be nonspherical.  KEF
would therefore contradict `pi_1^infty(A^2)=1` and rule out the hypothetical
map.  A universal proof of KEF would settle JC2; a proof for one completed
boundary book would kill that book.

This formulation is deliberately only one vertex and three branch groups.
It needs neither a classification of all weighted trees nor a topological
degree ceiling.  A branch intersection determinant outside `{+1,-1}`
(including determinant zero) already certifies nonsphericity through
nontrivial `H_1`; determinant `+1` or `-1` does not by itself certify
sphericality.

## 5. Hidden gaps that prevent promotion

### 5.1 A map-relative fork is not an end invariant

Resolving a polynomial map blows up only the original source boundary.
Consequently the full boundary of the resolved source can always be blown
down, after forgetting the map, toward the standard line at infinity of
`P^2`.  Branching in a **Phi-relative minimal graph** can disappear under
ordinary boundary contractions.  Ramanujam's theorem concerns the full
weighted end after the latter contractions.  Confusing these two notions
would manufacture an immediate false proof.

### 5.2 A subgraph does not automatically inject on `pi_1`

The `D_{k+2}` computation in the paper controls the whole relevant minimal
boundary under strong Picard/homology hypotheses.  In a Keller resolution,
extra pole, constant, and dicritical components attach to the proposed fork.
Their plumbing relations can kill its meridians.  Nontriviality of a local
fork group therefore cannot be promoted by an unproved inclusion
`pi_1(M_T)->pi_1(M_D)`.  KEF avoids asserting such an injection, but it must
prove the three branches are nonspherical **in the induced full minimal
graph**, exactly the missing custody.

### 5.3 `Ram(Phi) union Phi^(-1)(target infinity)` need not be the full source boundary

The dimension-three construction defines its affine source by removing
precisely the projective ramification and pulled-back hyperplane.  For a
resolved plane polynomial map, a finite-image dicritical component need not
belong to the ramification support merely from the definitions; in
particular, a generically unramified dicritical is omitted unless an
additional Keller theorem excludes it.  Removing only ramification and
target-pole divisors can therefore produce an open surface strictly larger
than the original source `A^2`.  Applying Ramanujam to that different open
surface is a category error unless a boundary-coverage theorem is proved.

### 5.4 Target meridians and source-end meridians are different objects

Monodromy around the asymptotic curve lives in a target complement.  The
plumbing generators live in the source link at infinity.  A resolved map
must provide an explicit induced word/filling relation between them.  This
is the same missing `theta`/target-meridian custody already isolated in the
face-character hostile review; the new paper does not supply it.

### 5.5 Bare graph shape is insufficient

Nonlinear graphs can be introduced by nonminimal blowups of an affine-plane
completion, while linear weighted graphs can have nontrivial plumbing group
(the tangent `Sym^2` control above ends with determinant zero).  The weights,
full boundary, ordinary minimality, and Ramanujam's homological hypotheses
are all load-bearing.

### 5.6 The low-degree topology is classical

Orevkov's published theorem already excludes generic degrees two and three
for complex plane Keller maps and already uses a resolved source boundary,
the finite-image branches, branched-cover Euler characteristic, and
fundamental groups.  The degree-two symmetric-power failure is therefore a
geometric explanation/negative control, not a new degree theorem.

## 6. Bounded next discriminator

Run exactly one **`KEF-ONE-VERTEX` custody test**, with no broad graph census:

1. Select one source-derived candidate for which every boundary component,
   attachment, and self-intersection weight is claimed complete.
2. Fail closed as `NOT-TYPED` if any tail or weight is missing.  On the
   current TD6 two-pole record, `ladder/SHEET6-CLASSICAL.md` §3b already
   predicts this stop because the `B`- and `x`-tails are unpinned.
3. Ordinary-minimize the full graph, explicitly allowing contractions that
   destroy the resolved morphism.
4. At one surviving pole/finite-image contact vertex, compute the three
   induced branch determinants and, only where needed, their Mumford
   presentations.  Three nonspherical branches kill that completed
   candidate by Ramanujam Lemma 4.
5. Calibrate the conventions on the tangent `Sym^2` model
   (`A^1 x G_m`, nontrivial end) and one triangular automorphism
   (ordinary boundary reduces to the affine-plane end).

Bound: one completed graph, one vertex, desk arithmetic or a short exact
integer script, at most one working day, no CAS/AWS.  If the input is not a
full graph or the fork vanishes under ordinary minimalization, stop the lane;
do not infer anything from the pinned skeleton.  If the test kills a graph,
the next obligation is a finite full-tail coverage theorem, not another
isolated plumbing example.

## 7. Final disposition

**Verdict: `REDESIGN`, secondary priority.**

The source is worth retaining as a clean recognition theorem and as a
warning that reduced versus nonreduced boundary contact is detected by a
nonabelian invariant at infinity.  It strengthens the conceptual vocabulary
of avenues 2 and 27.  It does not repair `G2-PSC`, `G2-BD`, full graph
landing/coverage, target-meridian custody, or the absence of a cofinal sheet
bound.  It gives no reason to move resources away from the current exact
branch-P/endpoint work.

The direct plane analogue is closed negatively.  The only licensed
continuation is the bounded full-boundary essential-fork test above.

## References used in this audit

- C. P. Ramanujam, *A topological characterisation of the affine plane as
  an algebraic variety*, Ann. of Math. 94 (1971), 69--88,
  <https://annals.math.princeton.edu/1971/94-1/p04>.
- S. Yu. Orevkov, *On three-sheeted polynomial mappings of C^2*,
  Math. USSR-Izv. 29 (1987), 587--596,
  <https://www.math.univ-toulouse.fr/~orevkov/jc86.pdf>.
