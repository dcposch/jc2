# Hostile review: capped local ADE Cartier-pair enumeration

Verdict: **CONFIRM_WITH_CORRECTIONS**.

I confirm the exact local enumeration and the advertised totals on review basis
`02572552f8f894ede08acb4a020a3af722b03e54`.  I do not confirm any promotion
from these formal local data to effective exceptional curves, analytic
incidence equations, polynomial maps, counterexamples, or JC2 evidence.

## 1. Artifact Identity And Scope

**CONFIRMED.**  The submitted artifact identities match the prompt:

```text
memo SHA-256:        03263fe7f7d97356f07291bb30ec38d5b4182a1ffc85fcbf57722d59cf3b50a9
script SHA-256:      d79fd1c484f229a0d564f537e29a31de6b86c97250db7649a6edf2de34ee8a94
gzip SHA-256:        bfbd89d61d1181bc0bdb9a243c8d3b85074541194621eb57047af9ecf884e279
canonical JSON SHA:  11ca074c9a4bc6656960222897d8c674f8486970b7a20cb1975cfcdb818d1d19
canonical JSON bytes: 3762426
```

The scope firewall in `xmodel/bd-a2-ade-cartier-pair-enumeration-sol56-20260830.md:38`
is essential and must remain attached to every use of the table: this is one
connected local exceptional component of one fixed type at a time.  The
predecessor cap is a proper-intersection cap: target-line cap eight is licensed
only under the no-common-curve hypothesis in
`xmodel/bd-a2-ade-decorated-boundary-different-threat-map-sol56-20260830.md:293`;
the `B`-fibre cap four is separately conditional at lines 329-349.  Neither cap
allocates a single global budget among several singular points unless a separate
global proper-intersection identity and the relevant slice data are being used.

## 2. A/D Integrality Gates

**CONFIRMED.**  For `A_r`, with chain numbering `1--...--r`, the inverse of the
Cartan matrix has entries

```text
(C_A^-1)_{j i}=min(i,j)*(r+1-max(i,j))/(r+1).
```

Therefore

```text
m_j=((r+1-j) sum_{i<=j} i n_i
     +j sum_{i>j} (r+1-i)n_i)/(r+1),
```

matching the memo at lines 101-112 and the script at
`ops/ade_cartan_pair_enumerate.py:68`.  The cokernel test is exactly
`sum i n_i = 0 mod r+1`: the weight vector `(1,...,r)` kills the columns of
`C_A` modulo `r+1` and is surjective because the first coordinate has weight
one.  No further lattice condition is missing.

For `D_r`, with chain `1--...--(r-2)` and fork vertices `r-1,r`, put
`a=n_{r-1}`, `b=n_r`, and `T=sum_{i=1}^{r-2} i n_i`.  Solving the Cartan
equations gives

```text
m_j=sum_{i=1}^{r-2} min(i,j)n_i + j(a+b)/2,  1<=j<=r-2,
m_{r-1}=(2T+r a+(r-2)b)/4,
m_r    =(2T+(r-2)a+r b)/4.
```

Thus the necessary and sufficient integrality conditions are
`a=b mod 2` and `2T+(r-2)a+r b=0 mod 4`; the other spin numerator differs by
`2(a-b)`, so parity makes the two spin congruences equivalent.  This matches
the memo at lines 114-134 and the script at `ops/ade_cartan_pair_enumerate.py:87`.

Because a connected finite ADE Cartan matrix is a positive definite irreducible
M-matrix, `C^-1` is entrywise strictly positive.  Hence every nonzero
`n>=0` with `n in C Z^r` gives `m=C^-1 n` with all `m_i>0`; conversely every
positive integral `m` with `Cm>=0` gives such an `n`.  Enumerating all nonzero
weak compositions through weight eight is therefore exactly equivalent to all
capped positive integral solutions.  There is no hidden positivity gate after
integrality.

## 3. Script And Data Audit

**CONFIRMED.**  I audited the standard-library producer line by line.

The Cartan graph construction in `ops/ade_cartan_pair_enumerate.py:45` is
correct.  For `D_r`, the generated edges are the chain through vertex `r-1`
plus the second fork edge from `r-2` to `r`; as an undirected graph this is
exactly the memo's convention.  For `D4`, this gives arms `1,3,4` around
vertex `2`, and the triality group at lines 165-174 is the full `S_3` on those
arms.  For `D_r`, `r>=5`, line 175 swaps only the two spin vertices.  For
`A_r`, line 162 correctly gives chain reversal, deduplicating `A1`.

The Weyl sentence is also correct in its limited sense.  If
`lambda=sum m_i alpha_i`, then `(lambda,alpha_i)=(Cm)_i=n_i`; thus `n>=0` puts
`lambda` in the closed dominant chamber.  A finite Weyl orbit has exactly one
closed-dominant representative.  The script does not quotient by Weyl
reflections; diagram canonicalization begins only at line 325.

Canonicalization, orbit recovery, cap nesting, and summary aggregation check
out.  I independently rebuilt graph automorphism groups by brute-force edge
preservation, solved all candidate systems over `fractions.Fraction`, recomputed
the multiset germ DP, and compared every canonical JSON record.  The check
matched:

```text
candidate vectors before congruence filters: cap8 72695, cap4 3218
all pairs:             cap8 16360 raw / 12238 canonical
all pairs:             cap4   772 raw /   646 canonical
one-germ survivors:    cap8   718 raw /   563 canonical
one-germ survivors:    cap4   198 raw /   163 canonical
canonical min histogram cap8: 1:563, 2:4180, 3:5312, 4:1915, 5:268
canonical min histogram cap4: 1:163, 2:356, 3:114, 4:13
```

The script's own `--deep-check --summary` path also reported
`deep_check_vectors=72695` and the same totals.  Rebuilding the payload through
the checked-in script in memory produced the exact compressed bytes; the gzip
header has `mtime=0`.

## 4. Physical-Germ Atom Model

**CONFIRM_WITH_CORRECTIONS.**  The atom model is locally correct, but it must
not be promoted beyond numerical local signatures.

On a smooth SNC resolution, one irreducible strict branch not contained in the
exceptional divisor has one center on the exceptional locus.  At a smooth point
of `E_i`, local coordinates give intersection vector `k e_i`.  At a node
`E_i intersect E_j`, local coordinates `xy=0` give vector `u e_i+v e_j` with
`u,v>0`.  There is no third support possibility on the minimal SNC exceptional
tree.  Conversely, each single numerical atom is locally realizable as a
reduced irreducible plane branch: for `gcd(u,v)>1`, adding a higher primitive
term preserves the two leading intersection orders while making the
parametrization primitive.

The generating-function DP in `ops/ade_cartan_pair_enumerate.py:231` counts
unordered multisets of atom types correctly.  The update processes each atom
type once and permits repeated use only through increasing total weight, which
is the standard unbounded coin-change recurrence for multisets.  The base-`9`
encoding has no carries for vectors of total weight at most eight.  The
metadata map is collision-free for ADE trees because a positive two-coordinate
atom determines its unique edge.

Repair required for promotion: the DP minimum lower-bounds the number of actual
analytic local branch germs only after an actual strict divisor is already
given.  It does not lower-bound the number of global carrier components,
distinct physical points on the minimal exceptional divisor, separated final
leaves before embedded resolution, or realized incidence solutions.  A counted
partition is a necessary numerical decomposition, not a simultaneous analytic
realization theorem for the charged different.

## 5. Forest Cut

**CONFIRM_WITH_CORRECTIONS.**  The forest conclusions are correct only in the
conditional form stated in the memo.

Without carrier labels, the unit-vertex decomposition `n=sum n_i e_i` can be
drawn with separate outside leaves attached to the ADE tree.  This proves only
non-exclusion by the unlabelled local forest test; it proves neither analytic
realization nor global connected-carrier compatibility.  The memo says this at
`xmodel/bd-a2-ade-cartier-pair-enumeration-sol56-20260830.md:286`, and that
wording should be preserved.

Under the stated one-connected-outside-carrier hypothesis, two separated final
joining edges between the connected inner resolved tree and the connected
outside reduced carrier graph force a cycle: take the unique path inside the
inner tree and a path inside the outside graph.  Therefore at most one analytic
branch can occur; since `n` is nonzero for an actual record, this means exactly
one local germ.  The one-germ numerical filter is then exact, giving the
confirmed `718/563` and `198/163` survivor counts.

Required guardrail: shared trunks, coincident physical points, branches
initially passing through the same ADE node, and node blowups do not invalidate
the cut only if the common trunks are included in the connected inner graph and
the argument is applied to distinct final joining edges on one common embedded
SNC resolution.  Carrier intersections or shared nonexceptional components
destroy the disjoint-connected-subgraph hypothesis and must be handled
separately.

## 6. Scope Enforcement

**CONFIRM_WITH_CORRECTIONS.**  The maximum safe result is:

```text
An exact finite table of local numerical Cartier pairs (m,n), for one connected
ADE exceptional component of type A1..A8 or D4..D9 at one point, under the
proper target-line cap sum n_i<=8 and the separately conditional proper
B-fibre cap sum n_i<=4, together with diagram-automorphism orbits and exact
unordered numerical germ-signature partition polynomials.

If, on one common embedded SNC resolution, the actual outside carriers form one
connected subgraph disjoint from the inner attachment graph before distinct
final joining edges, then only the one-germ records can survive.
```

Everything stronger remains open: disconnected ADE multisets, simultaneous
`D9(-1)` embeddings, effective exceptional curves, paired infinity vectors
`(h,a)`, carrier labels, analytic incidence equations, polynomial maps, and
global slice-budget allocation.  The all-type totals are a disjoint local sum,
not a count of global configurations.  The cap eight is per chosen proper
target-line local consequence; the cap four is a separate proper `B`-fibre
stratum.  Neither is a license to spend one global budget across unrelated
points without the actual proper-intersection identity.

## 7. Repairs

No script or canonical-data repair is required.

Promotion repairs required:

1. Every citation of `16360/12238`, `772/646`, `718/563`, or `198/163` must say
   "one connected local ADE component" and must state the relevant properness
   cap.
2. Replace any unqualified "survivor" by "not excluded local numerical
   signature" unless effectivity and incidence realization have been proved.
3. State that the DP minimum is a lower bound for actual analytic local branch
   germs only, not for global carriers or physical points.
4. State the one-germ forest cut only with the connected-outside-carrier,
   disjointness, common-SNC-resolution, and distinct-final-joining-edge
   hypotheses.
5. Keep the predecessor's common-component and nonfinite strata open; do not
   cap them by analogy.

## 8. Cheapest Decisive Successor

The cheapest global successor is not another local Cartier enumeration.  It is
a carrier-labelled finite global packet: for each actual singular point, attach
the strict different/infinity carrier labels and the paired boundary data
`(h,a)`, verify the proper-intersection identities, enumerate simultaneous
effective embeddings in the fixed `D9(-1)` marking, and then apply the
one-connected outside-carrier forest cut only where its hypotheses are
certified.  This is the smallest step that can turn the confirmed local table
from a threat map into a genuine global exclusion or realization test.

<!-- BODY-END -->
