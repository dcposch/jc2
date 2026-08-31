# The charged one-cusp `T(3,4)` row: the second cubic critical point obstruction

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`genus3_cable_recovery` lane)  
Frozen basis: `e66542021690fcc7a1100482716804b2d8f174f7`  
Lifecycle: **FINAL+VERIFIED NARROW EXACT THEOREM / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Theorem and verdict

Assume an actual rank-four charged minimal-cycle packet whose reduced target
branch `B` is irreducible and satisfies

```text
normalization(B)=A1,
b1(B)=n22=1,
n4=0,
m=|T31|=1,
Delta_aff(B)=3,                                        (0.1)
```

with the charged transitive meridional monodromy `S4`.  Then no such packet
exists.

The finalized genus-three cable and `b1` classification reduces (0.1) to the
infinity type `T(3,4)` and delta sequence `(4,3)`.  Its normalization has a
degree-three target coordinate

```text
X:A1_t -> A1.                                          (0.2)
```

The derivative of `X` has critical-divisor length two.  The unique `(3,1)`
point can absorb at most one simple critical point.  A remaining simple
critical point either has local `(2,1,1)/C2` monodromy, which duplicates two
of the three vertical-fibre transpositions, or lies at one endpoint of the
unique `(2,2)` conductor fibre, in which case the entire cubic fibre lies in
the pair-preserving local group `C2 x C2`.  If instead the derivative has one
double root at the `(3,1)` point, the entire cubic fibre lies in its local
`S3`, which fixes the fourth quartic sheet.  Every alternative is
intransitive.

Moving the entire three-meridian tuple between the local and original based
frames by a full Hurwitz tail preserves its generated subgroup, up to
simultaneous conjugacy.  The original tuple therefore cannot generate the
charged `S4`, a contradiction.

This closes only the irreducible charged `b1=1,n4=0,Delta_aff=3,m=1` row.
Together with the separately finalized `m=0` theorem it removes the complete
irreducible charged genus-three minimal packet.  It does not treat
`Delta_aff>=4`, reducible branches, a source forest with several components,
nonminimal rank-four rows, or any higher-rank block.

## 1. Frozen dependencies

The exact genus-three and no-cusp inputs are

```text
03b16c2deba48605482963ae7f98f5e74aca26ce0e1761bbeab653a164bec4b4
  xmodel/block-descent-a1-genus-three-cable-b1-obstruction-sol56-20260830.md
2b3cc0b7dd7db7a9e0f34cec4c76df97424615e3e5205f9a6fc391c5d3bb8d3d
  xmodel/block-descent-a1-genus-three-t34-m0-projection-rank-obstruction-sol56-20260830.md
bcfc47b0467d839f7f19a36620c9ca1436fa3fd3f653faa228b20b1a383ada9f
  xmodel/block-descent-a1-genus-three-m0-complete-obstruction-sol56-20260830.md
```

The charged topology and one-cusp interfaces are

```text
5d7df7ce0ad3548e88fd23734917212d6b3fbd3ada4cab81514b12bb76ea64de
  xmodel/block-descent-a1-quartic-branch-topology-coordinator-integration-sol56-20260830.md
cf157e17db8179b590f15808aab84447717df343735416578e005a2085d73d4e
  xmodel/block-descent-a1-quartic-minimal-cycle-nodal-control-threat-map-sol56-20260830.md
2531a89d6c939aee6e0d402408f15d28a228927dc15d82c10d430e67164cb190
  xmodel/block-descent-a1-quartic-cycle1-function-pair-coordinator-integration-sol56-20260830.md
```

They supply the following exact interfaces used here.

1. At total affine delta three, all prime one-place infinity types except
   `T(3,4)` are removed by the boundary `S4`, semigroup, or `b1=1` gates.
2. The `(4,3)` row has a polynomial normalization coordinate of degree three;
   three meridians in a regular affine vertical fibre generate the complement
   group by affine Zariski--van Kampen.
3. The charged finite fibre strata are disjoint:

   ```text
   T211=(2,1,1), T31=(3,1), S22=(2,2), S4=(4).
   ```

4. In the present row there is exactly one `T31` point, exactly one `S22`
   point, and no `S4` point.  The `S22` point has exactly two normalization
   preimages; every other point has one.
5. The complete quartic local groups needed below are

   ```text
   T211: C2;
   T31:  S3 fixing one quartic sheet;
   S22:  C2 x C2 on two disjoint sheet pairs.          (1.1)
   ```

The local table is a henselian rank-decomposition statement, not merely a
list of divisorial inertia cycles.

## 2. The cusp and conductor cannot coincide

Let `z31` be the unique target point in `T31`, and let `c` be its unique
normalization preimage.  Let `n` be the unique target point in `S22`, with

```text
nu^(-1)(n)={a,b},             a!=b.                    (2.1)
```

The equality `z31=n` is impossible.  The scheme fibre of the quartic map at a
closed target point has one partition of four.  It cannot simultaneously be
`(3,1)` and `(2,2)`.  Equivalently, `T31` and `S22` are disjoint pieces of the
charged fibre stratification.  Hence

```text
c notin {a,b}.                                         (2.2)
```

This separation is stronger than the topological statement `b1(B)=1`; it
uses the actual quartic fibre packet.  It is load-bearing in the two-simple-
critical-point case below.

## 3. Locality of saturated vertical fibres

We record explicitly why the local-group argument really controls the stated
vertical meridians.  Let `x0` be a value of (0.2), and suppose the complete
scheme fibre `X^(-1)(x0)` is supported on normalization parameters which all
map to one target point `z in B`.  Choose a sufficiently small analytic ball
`N` around `z`.  Properness of the finite polynomial map `X:A1->A1` on a
small neighborhood of its finite fibre gives a disk `Delta` around `x0` such
that every corresponding intersection of a nearby vertical line with `B`
lies in `N`.  The geometric meridians of that cluster can therefore be chosen
inside `N-B`.

By definition, their images in the quartic Galois closure lie in the complete
local decomposition group `H_z`.  Transport from the original regular fibre
to this local frame applies a braid to the whole tuple, and changing the
ambient basepoint may simultaneously conjugate the tuple.  Elementary
Hurwitz moves are Nielsen transformations; they preserve the generated
subgroup, while simultaneous conjugacy preserves its order and orbit
partition.  Thus an intransitive local generated subgroup cannot become `S4`
in the original frame.

Two saturated fibres occur below.

* A local-degree-three point of a cubic has
  `X^(-1)(x0)=3c`, so all three vertical meridians are local at `nu(c)`.
* If `a` is a simple critical endpoint of (2.1), then `X(a)=X(b)` and
  local multiplicity gives

  ```text
  X^(-1)(X(a))=2a+b.                                  (3.1)
  ```

  Its length is already three, so there is no remote fourth contribution;
  all three nearby intersections lie in a ball around `n`.

Even without the second bullet's full-local conclusion, the two meridians in
the ramified analytic branch belong to one rank-two factor and are equal
transpositions.  Equation (3.1) supplies the stronger pair-preserving local
group statement and removes any path-choice ambiguity.

## 4. Exhaustive cubic critical-divisor argument

After the exact normal form one may write `X=t^3+A*t`, but only its degree is
needed.  The zero divisor of `X'` has length two.

### 4.1 One double critical point

Suppose `X'` has one double root `r`.  Then `X` has local degree three at
`r`.

* If `r=c`, the whole nearby three-meridian tuple lies in the local `S3` at
  `z31`.  That `S3` fixes the fourth quartic sheet, so it is intransitive.
* If `r` is `a` or `b`, its local multiplicity three plus the distinct
  conductor mate in the same `X` fibre would have length at least
  `3+1>3`.  This is impossible.
* Otherwise `nu(r)` is neither `T31`, `S22`, nor `S4`; it is `T211`.  The
  whole tuple lies in its local `C2` and is intransitive.

Thus the double-root partition cannot carry the global `S4` tuple.

### 4.2 Two simple critical points

Suppose `X'` has distinct roots `r1,r2`.  By uniqueness of `T31` and (2.2),
at most one of them equals `c`.  Choose a root `r` different from `c`.

If `r notin {a,b}`, its target fibre is `T211`.  In a local projection frame,
the two punctures in its simple ramified cluster both map to the unique
nonidentity element of `C2`, hence the complete three-tuple has the form

```text
(tau,tau,rho)                                          (4.1)
```

up to positions.  It contains at most two distinct transpositions.

If `r` is a conductor endpoint, (3.1) puts the whole tuple in
`C2 x C2=<tau,upsilon>`, where `tau` and `upsilon` are disjoint
transpositions.  This group has two sheet orbits.  If both `r1,r2` were the
two conductor endpoints, the same cubic fibre would have length at least
`2+2>3`, so that subcase is already impossible.

These cases exhaust the second critical point: `n4=0`, and every
normalization point outside `c,a,b` belongs to a `T211` target fibre, even if
its image is a point-bijective unibranch singularity of `B`.

## 5. The group contradiction

View a transposition as an edge on the four quartic sheets.  Transpositions
generate a transitive subgroup exactly when their support graph is connected.
Three transpositions generate `S4` only if their three distinct edges form a
spanning tree.

The tuple (4.1) has at most two edges and is intransitive.  The local `S3` at
`T31` has one fixed vertex, and the local `C2 x C2` at `S22` has two orbits;
both are intransitive as well.  By Section 3 the original regular-fibre tuple
generates the same subgroup up to conjugacy.  But affine Zariski--van Kampen
makes those three fibre meridians generate `pi1(A2-B)`, and their charged
images must generate global `S4`.  This contradiction proves the theorem.

The earlier warning that an `S3` packet permits overlapping transpositions
remains correct but is not a surviving escape.  It addresses one simple
critical point in isolation.  The cubic has a second unit of ramification; or,
when both units coalesce at that cusp, the entire tuple is trapped in the
same fixed-sheet `S3`.

## 6. Deterministic replay and scope firewall

The new desk-small replay is

```text
a9fc7358394a373e8e25c162e6d95c79f530090fad265489361f2be9c62ea46c
  ops/block_descent_a1_genus_three_t34_m1_ramification_replay.py
```

Ordinary, `python3 -O`, and `python3 -OO` executions are byte-identical with

```text
stdout SHA-256
bd215282fcf28572401de5d2318c1cf7894ee56739e546a532d9c20cf6f9819a.
```

The replay checks all `6^3=216` quartic transposition triples, the 96
full-`S4` spanning-tree triples, the 24 `T(3,4)` boundary colorings, all
positive and negative elementary Hurwitz moves, the 27 triples inside a
fixed-sheet local `S3`, the eight meridian triples inside the `S22` pair
group, and all 36 simple-`T211` duplicate clusters.  It exhausts the three
double-root event types and the eight ordered two-simple-root assignments
under unique `T31`; the both-`T22` assignment fails by `2+2>3`, leaving seven
realizable assignments, all obstructed.

Each of the mutations

```text
--mutate-allow-duplicate-s4
--mutate-local-s3-as-s4
--mutate-allow-two-t31-critical-points
```

exits nonzero at its intended gate.  The script has no `assert` statements
and uses only the Python standard library.  No heavy local CAS was used.

This artifact does not promote itself past the campaign's different-model
review rule.  It proves no statement about a second `T31` point, a `(4)`
fibre, `Delta_aff>=4`, reducible branch, higher rank, existence of a proper
block, or JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11376`.
- Body SHA-256:
  `8cd8e2b9b8795683468f2ba189173dce74818e14777d5caf19f174c160d61ab6`.
- Frozen basis: `e66542021690fcc7a1100482716804b2d8f174f7`.
