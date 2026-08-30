# Hostile review: ADE-decorated quadratic boundary/different threat map

Reviewer: GPT-5.5 xhigh  
Review basis: `986427df23c30375b6edfd659ba8a6c6139434ab`  
Target:
`xmodel/bd-a2-ade-decorated-boundary-different-threat-map-sol56-20260830.md`

## Overall Verdict

`CONFIRM_WITH_CORRECTIONS`.

The signed-`D9` root classification, the `A_r` and `D_r` inverse-Cartan
arithmetic, and the proper-intersection transform identities are correct in
their necessary-data scope.  The advertised connected survivors really do
survive these tests as formal Cartier-lattice/one-physical-germ patterns.

The promotion must be worded more narrowly: the finite object proved here is a
finite numerical/combinatorial threat list in the proper-intersection,
no-common-carrier regimes.  It is not a finite enumeration of effective
divisors, analytic germs, incidence equations, finite maps, or polynomial
maps.  Common-carrier and nonfinite cases remain open strata, not capped
subcases.

## Charged Inputs And Scope

I read the sealed producer in full.  Its full-file SHA-256 matches the prompt:

```text
ab10ea83f443c93bdb87194ad0e42fe2c442984ba821c3ddf8ddf5cc3f796133
```

I also read the Section 0 charged predecessor:

```text
f7d1c8cb42d5afd29474eb0975ffae518b0c82620f598649c2ac3d5d59064f94
  xmodel/bd-a2-normal-singular-quadratic-incidence-reduction-sol56-20260830.md
```

For scope control I checked the immediately named promoted inputs from that
predecessor which constrain the smooth/forest/block hypotheses.  No conclusion
below imports the independently active moving-double-section/conductor lane,
basis minimization, nonnormal closures, counterexamples, or JC2.

## 1. `D9` Root Subsystems

Verdict: `CONFIRMED`.

Use coordinates for `D9`:

```text
R(D9)={+-e_i+-e_j : i != j}.
```

Given a connected simple-root set, make the signed coordinate graph whose
vertices are used coordinate positions and whose edges are the simple roots.
Dynkin connectedness forces this coordinate graph to be connected, because
nonorthogonal roots must share a coordinate.  After switching coordinate signs
along a spanning tree, the tree edges are differences `e_i-e_j`.

If `s` coordinates are used, the spanning tree already generates `A_{s-1}`.
Every remaining balanced edge stays in that lattice.  One unbalanced edge
adds a sum root and then the generated lattice is exactly

```text
{x in Z^s : sum x_i even}=D_s.
```

There is no exceptional third case.  Thus an irreducible connected embedded
root subsystem of `D9` is `A_{s-1}` or `D_s`, hence only

```text
A1,...,A8,  D4,...,D9.
```

This excludes `A9,E6,E7,E8` as embedded root subsystems, not merely as one
chosen simple-root presentation.  For example, rank-nine `A9` would have to
use `s=9` and hence generate `D9`, contradicting determinant `det A9=10`
versus `det D9=4`.  Similarly `E6,E7,E8` would force generated lattices
`A6/D6`, `A7/D7`, or `A8/D8`, whose determinants do not match `3,2,1`.

The determinant gate for full-rank disconnected systems is also correct:
for a rank-nine sublattice `Lambda` of `D9`,

```text
det Lambda = det(D9) [D9:Lambda]^2 = 4 [D9:Lambda]^2.
```

No primitivity is needed.

## 2. Cartan Arithmetic

Verdict: `CONFIRMED`, with one wording repair.

For `A_r` with chain numbering `1-...-r`,

```text
(C^{-1})_{ji}=min(i,j)(r+1-max(i,j))/(r+1),
```

so the displayed formula

```text
m_j=((r+1-j) sum_{i<=j} i n_i
     +j sum_{i>j} (r+1-i)n_i)/(r+1)
```

is correct.  The cokernel is cyclic of order `r+1`; the functional
`sum i n_i mod r+1` kills the columns and is surjective.  Hence the exact
integrality gate is

```text
sum i n_i = 0 mod r+1.
```

The one-vertex order

```text
o_i=(r+1)/gcd(i,r+1)
```

and the cap-four table in the producer are correct.  The advertised
one-physical-germ patterns are also correct:

```text
r=2k-1: n=2e_k,       m=(1,2,...,k,...,2,1),
r=2k:   n=e_k+e_{k+1}, m=(1,2,...,k,k,...,2,1).
```

For `D_r` with numbering

```text
1--2--...--(r-2), with (r-1),r attached to r-2,
```

put `a=n_{r-1}`, `b=n_r`, and `T=sum_{i=1}^{r-2} i n_i`.  The inverse
formula

```text
m_j=sum_{i=1}^{r-2} min(i,j)n_i + j(a+b)/2,  1<=j<=r-2,
m_{r-1}=T/2 + r a/4 + (r-2)b/4,
m_r    =T/2 + (r-2)a/4 + r b/4
```

is correct.  Its exact integrality condition is

```text
a=b mod 2,
2T+(r-2)a+r b=0 mod 4.
```

The second spin congruence is equivalent after `a=b mod 2`.  The one-vertex
orders in (4.4) are correct, and `n=e_2` gives

```text
m=(1,2,2,...,2,1,1)
```

for every `D4,...,D9`.

The repair is only wording: the classification should say

```text
n in Z_{\ge 0}^r, n != 0, n in C Z^r
```

classifies the positive integral `m`, because strict positivity of `m` then
follows from positivity of `C^{-1}`.  It is not an independent nonnegativity
condition on `m`.

I spot-checked the bounded semigroups by direct integer enumeration.  The
congruence gates and inverse formulas round-trip for all `A1,...,A8` and
`D4,...,D9` with `sum n_i<=8`.

## 3. Intersection Caps

Verdict: `CONFIRMED_WITH_SCOPE_REPAIRS`.

The total-transform identity is correct.  For a Cartier slice `L` through a
singular point,

```text
r^*L=L_str+ell E,       r^*R=R_str+mE,
n=Cm,                  b=C ell,
```

and the exceptional terms are

```text
L_str.(mE)=ell^t n,
(ell E).R_str=ell^t n,
(ell E).(mE)=-ell^t n.
```

Thus exactly one copy remains:

```text
L.R=L_str.R_str+sum_q ell_q^t n_q.
```

For a target line, `A.R=(A).(2A+B)=8`; for a `B`-fibre,
`B.R=4`; for infinity, `H.R=A.R=8`.  Since any local equation vanishing at
the singular point has positive valuation on every exceptional component,
`ell_i,beta_i,h_i>=1`, and therefore `ell^t n`, `beta^t n`, or `h^t n`
bounds `sum n_i`.

The caps are valid only under the following hypotheses:

```text
target-line cap: the chosen pullback line has no common curve with R_X;
B-fibre cap: the chosen B-fibre has no common curve with R_X;
infinity cap: H and R_X have no common nonexceptional curve;
all caps: strict-transform intersections are proper and nonnegative.
```

Projective finiteness is enough to choose a target line avoiding different
components: finite maps do not contract different components to the target
point, and only finitely many component images can be lines through that
point.  Without that properness, no cap follows.  In particular a coefficient
basepoint or common different carrier may force every relevant slice to share
a component; then the numerical inequality is not licensed.

A cheap strengthening is available but not decisive: the exceptional
coefficient vector of a local function is at least the Du Val fundamental
cycle, not merely componentwise at least one.  This can improve individual
rows, especially for `D_r`, but it does not kill any connected surviving
type because the displayed `A` and `D` one-germ patterns still have
intersection weight at most two against the natural minimal cycles.

## 4. Physical Germs And Forests

Verdict: `CONFIRMED_WITH_SCOPE_REPAIRS`.

The producer correctly separates numerical entries of `n` from physical
boundary contacts.  A tangent branch at a smooth point of one exceptional
component can contribute `n_i>1` but creates one branch path after embedded
resolution.  A branch through a node can contribute to both adjacent entries
of `n` while still being one physical branch; blowing up the node inserts a
single local resolution chain.

The forest criterion is the following exact graph statement.  After taking
the full reduced SNC boundary and after including in `T_p` the ADE tree plus
the extra local vertices introduced to resolve its contacts, each connected
component of the complement of `T_p` may attach to `T_p` by at most one edge.
Two such edges give a cycle by joining them through the unique path in
`T_p` and through the outside component.  Conversely, single attachments to
a tree do not create a cycle.

The repair is to keep the carrier qualifier explicit.  Two contacts are
cycle-forcing only when they lie in the same outside connected carrier
component after the chosen boundary resolution.  If the contacts lie on
outside components connected only through `T_p`, the graph is a star, not a
cycle.  If `H` and `R` share a nonexceptional component, the quotient graph
has changed and the no-common-carrier connector count cannot be applied.

## 5. Finiteness Of The Successor

Verdict: `CONFIRM_WITH_CORRECTIONS`.

The local numerical sets are finite in the capped regimes.  For each
connected type there are finitely many

```text
n in C Z^r cap Z_{\ge 0}^r,  0<sum n_i<=8
```

and finitely many cap-four rows when the `B`-fibre hypothesis is available.
For a singular point on infinity, the paired data are also finite:

```text
a=C h >=0,  n=C m>=0,  h,m>0,
h^t n = a^t C^{-1}n <=8.
```

Because `n` is nonzero and `C^{-1}` is strictly positive, this bounds `h`
and hence `a`.

A complete finite numerical enumeration schema is:

1. Enumerate multisets of connected types from
   `A1,...,A8,D4,...,D9` with total rank at most nine.
2. Enumerate simultaneous embeddings of their root lattices in `D9`,
   modulo the Weyl group `W(D9)` and component Dynkin automorphisms; discard
   full-rank determinant failures `det != 4 square`.
3. For every connected component, enumerate the bounded `n` semigroup by
   the exact `A` or `D` congruence, with the applicable cap.
4. For components lying on infinity, enumerate the paired boundary vector
   `a` equivalently via positive integral `h=C^{-1}a`, with
   `sum h^t n<=8` globally in the no-common-carrier infinity regime.
5. Partition each bounded vector into physical branch contacts: at a smooth
   point, vectors `k e_i`; at an ADE node, vectors `u e_i+v e_j` with
   `u,v>=1`; total weight bounded by the cap.  Then quotient by local Dynkin
   automorphisms and by identical carrier labels.
6. Build the resolved incidence graph using physical branches, not entries
   of `n`, and apply the single-connector forest condition.
7. Only after these finite numerical rows are produced, ask the separate
   effectivity and analytic-incidence questions for the corresponding strict
   carrier classes in the ruled nine-blowup marking.

The correction is in step 7.  Effectivity is not itself a finite enumeration
of actual divisors or analytic germs.  Linear systems and local germs can
have moduli, and the nine-blowup effective cone need not be finite in any
unproved global sense.  What is finite is the list of numerical classes and
bounded contact partitions on which effectivity/incidence predicates must be
tested.  The packet should not advertise a finite list of effective
divisors, maps, or polynomial candidates.

## 6. Remaining ADE Types

Verdict: `CONFIRMED`.

I find no cheaper theorem, using the charged data, that kills any connected
type left after the `D9` root model.  The proper caps, even sharpened by
fundamental cycles, leave all connected `A1,...,A8` and `D4,...,D9`.

Formal survivors can be written uniformly.  For `A_r`:

```text
r=2k-1: n=2e_k,
        m=(1,2,...,k,...,2,1);

r=2k:   n=e_k+e_{k+1},
        m=(1,2,...,k,k,...,2,1).
```

If boundary data through infinity are demanded, take

```text
h=(1,...,1),  a=C h=e_1+e_r
```

with the evident `A1` specialization `a=2e_1`.  Then `h^t n=2`.

For `D_r`:

```text
n=e_2,
m=(1,2,2,...,2,1,1).
```

For matching boundary data one may take the same positive cycle for `h`,
so `a=C h=e_2` and `h^t n=2`.

These are formal numerical Cartier data and physical one-germ patterns only.
They are not effective exceptional configurations, analytic incidence
singularities, finite maps, or polynomial maps.

## 7. Maximum Safe Theorem

Verdict: `CONFIRM_WITH_CORRECTIONS`.

The maximum theorem safe to promote is:

```text
In the normal irreducible class-(2A+3B) quadratic incidence scope of the
charged predecessor, the minimal resolution has ADE exceptional lattice
embedded in D9(-1).  Every connected embedded component is A1,...,A8 or
D4,...,D9.  For each connected component, positive exceptional different
multiplicities and strict-transform attachment vectors are classified
exactly by the A/D Cartan congruences above.  In any stratum where a target
line through the singular image meets the different properly, sum n_i<=8;
where the corresponding B-fibre also meets it properly, sum n_i<=4; and
where infinity and different have no common nonexceptional carrier, the
paired boundary/different data satisfy sum h^t n<=8.  Forest topology acts
on distinct physical branch contacts after embedded resolution.  Under
these necessary numerical and graph tests no connected A1,...,A8 or
D4,...,D9 type is eliminated.
```

The exact unresolved strata are:

```text
common nonexceptional H/R carrier;
different component contained in a B-fibre or other slice used for a cap;
projective coefficient-basepoint or other nonfinite target-line cases;
nonfinite affine/projective coefficient strata inherited from the singular model;
simultaneous effective realization of the allowed root embeddings in the
  ruled nine-blowup marking;
effectivity, irreducibility, and incidence equations for strict carriers;
analytic realization of the formal branch partitions by a bidegree-(2,3)
  normal hypersurface;
nonnormal closures, conductor effects, basis changes, and all JC2 claims.
```

## Repairs Required Before Promotion

1. Replace any bare phrase "finite successor" by "finite numerical/combinatorial
   successor in the stated proper-intersection/no-common-carrier strata".
2. State every cap with its properness and no-common-component hypotheses at
   the point of use.  Do not reuse `A.R=8`, `B.R=4`, or `H.R=8` as a bound
   after a common component appears.
3. Add the carrier qualifier to the forest rule: numerical multiplicity and
   support do not count edges; distinct physical contacts count only after
   assigning outside connected carriers in the resolved boundary graph.
4. Keep formal survivors explicitly formal.  They certify non-exclusion by
   necessary lattice tests only.
5. State that effectivity/incidence remains a predicate on finite numerical
   rows, not a finite construction of divisors or maps.

## Cheapest Decisive Successors

1. Implement the finite numerical enumerator described in Section 5, producing
   Weyl-orbit rows with `type`, embedding orbit, `n`, optional `a`, physical
   branch partition, and resolved carrier graph.
2. Add the fundamental-cycle slice lower bound as a cheap row-pruner.  It will
   not kill connected types, but it can shrink capped rows.
3. Separate common-carrier cases into their own packet: first decide whether
   an `H` component can be contained in the different or a `B`-fibre component
   can be contained in the different under the normal class data.
4. For each remaining numerical row, test effectivity of the strict carrier
   classes in the actual ruled nine-blowup marking before asking for analytic
   incidence realization.

<!-- BODY-END -->
