# Rank-four zero-cusp cycle: universal graph-knot obstruction for all minimal B4 packets

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`rank4_cycle_m0` lane)  
Frozen basis: `7ff3257e9a5f944580cef9c7961296b6ca1db50c`  
Lifecycle: **FINAL+VERIFIED UNIVERSAL MINIMAL-PACKET NO-GO / NO SURVIVING ORBIT / NONMINIMAL-TANGENTIAL HORN OPEN**

## 0. Verdict

Every minimal zero-cusp quasipositive four-strand packet with

```text
three normalization bands forming a connected A1 tree,
one ordinary node band-square,
no other affine singularity or local braid factor,
one boundary cycle,
rank-two transposition local colors,
and full S4 based coloring                              (0.1)
```

is excluded from globalization by a polynomially parametrized one-place
plane curve.  This is independent of all braid tails, the order of the local
factors, and the Hurwitz/conjugacy orbit.  There is no surviving packet in
the stated minimal class.

The universal argument has four short steps.

1. If a reduced polynomial fibre has a knot as its link at infinity, the
   corrected Neumann--Rudolph knot-at-infinity lemma says that its defining
   polynomial is good: every fibre is regular at infinity.
2. A nearby smooth fibre therefore has the same boundary knot.  In the
   present census it is obtained by smoothing the sole ordinary node of an
   `A1` normalization.  Its compact core has one boundary and genus one;
   Neumann's regular-curve theorem identifies it with the minimal Seifert
   surface of the boundary knot.
3. That knot is an Eisenbud--Neumann graph knot.  The only genus-one graph
   knots in `S3` are the right- and left-handed trefoils.
4. The fixed transposition tuple descends through the closed-braid Artin
   presentation to a surjection from the knot group onto `S4`, whereas a
   trefoil meridian-transposition representation has image `C2` or `S3`.

The Alexander/root-of-unity gate from the preceding report is recovered as
the coarser first screen:

```text
genus <= 1 graph-knot Alexander candidates =
  1                       (unknot),
  t^2-t+1                 (either trefoil).             (0.2)
```

Thus any packet whose Alexander polynomial is not one of (0.2), up to a
Laurent unit, fails immediately.  A packet with one of those polynomials
still fails the exact graph-knot plus transposition-color gate.  In
particular, sharing the trefoil Alexander polynomial is not a surviving
escape.

This closes the entire **minimal ordinary-node B4 packet lane**.  It does not
cover a tangential two-point identification, an extra unibranch affine
singularity, or any other modification which adds positive bands and raises
the nearby-fibre genus.

## 1. Charged inputs and primary theorem interfaces

```text
43c83d47d864537aae6fec7203111aaa3c6c52fa4bbc0e95c6877c61aa86ad57
  xmodel/block-descent-a1-quartic-cycle0-polynomial-link-obstruction-sol56-20260830.md
6e5d5ab57734db02c5d29d264f1d2b3c81b21639f0ff786e19c9723e285e2042
  ops/block_descent_a1_quartic_cycle0_polynomial_link_replay.py
e73f8e83c4031e516f0302dea94e168b5f8b8d5f0bcc6cd86f87eb927a682e14
  xmodel/block-descent-a1-quartic-cycle0-projection-propagation-obstruction-sol56-20260830.md
b9f0352ce63513ce16925f9bf4d7b5be11e0246c9426ecc72cf477cd977103a0
  ops/block_descent_a1_quartic_cycle0_braid_escape_replay.py
e1d0472bfbd5203d1e75582c3be5b44b50d9db4987d27b97b2864cee4931522f
  ops/block_descent_a1_quartic_cycle0_all_minimal_packets_replay.py
```

The global topology layer uses only these primary sources.

```text
David Eisenbud and Walter D. Neumann,
Three-Dimensional Link Theory and Invariants of Plane Curve Singularities,
Annals of Mathematics Studies 110, Princeton University Press, 1985.

Walter D. Neumann,
"Complex algebraic plane curves via their links at infinity",
Inventiones Mathematicae 98 (1989), 445--489,
DOI 10.1007/BF01393832.

Walter D. Neumann and Le Van Thanh,
"On irregular links at infinity of algebraic plane curves",
Mathematische Annalen 295 (1993), 239--244,
DOI 10.1007/BF01444886; arXiv:alg-geom/9202008.

Walter D. Neumann and Lee Rudolph,
"Unfoldings in knot theory",
Mathematische Annalen 278 (1987), 409--439,
DOI 10.1007/BF01458078;
with "Corrigendum: Unfoldings in knot theory",
Mathematische Annalen 282 (1988), 349--351,
DOI 10.1007/BF01456981.

Horst Schubert,
"Knoten und Vollringe",
Acta Mathematica 90 (1953), 131--286,
DOI 10.1007/BF02392437.
```

Two distinct Neumann interfaces are used and must not be conflated.

1. The link at infinity of an arbitrary reduced polynomial zero-fibre is a
   toral graph link; regularity is not needed for that assertion.
2. Corrected Lemma 7.1 of Neumann--Rudolph says that if such a reduced fibre
   has a **knot** as its link at infinity, then its defining polynomial is
   good, meaning every fibre is regular at infinity.  The 1988 corrigendum
   replaces the original definition of `good` and explicitly restates and
   reproves this lemma.  Neumann 1989, page 446, consumes the corrected form.

For a nearby nonsingular fibre, Neumann 1989, Theorem 1 identifies its compact
core with the unique minimal Seifert surface of the regular link at infinity.
Eisenbud--Neumann supplies the graph-link splice calculus and its generation
in `S3` by cabling and connected sum.  Schubert supplies the satellite/cable
genus formula.  No implication from general quasipositivity to strong
quasipositivity is used; that implication is false.

## 2. The complete minimal packet class

Let `s_1,s_2,s_3` be the standard generators of `B4`.  A packet in the class
under consideration has three positive normalization bands

```text
q_j = a_j s_(i_j) a_j^(-1),       j=1,2,3,             (2.1)
```

whose endpoint-incidence graph is a tree on the four normalization sheets,
and one ordinary node packet

```text
n = c s_i^2 c^(-1).                                     (2.2)
```

The factors may occur in any distinguished-path order.  The permutation of
their product is a four-cycle, equivalently the boundary closure is a knot.
The three bands in (2.1) are the minimal finite ramification needed by a
degree-four polynomial normalization with one totally ramified place at
infinity; their tree gives a disk normalization.

There is also a based color tuple

```text
T=(tau_1,tau_2,tau_3,tau_4),
tau_j an S4 transposition,                               (2.3)
```

which is fixed by every local braid factor under the Hurwitz action.  In the
local frame of (2.1), the two colliding colors agree.  In the local frame of
(2.2), the two colors are disjoint transpositions.  Finally,

```text
<tau_1,tau_2,tau_3,tau_4>=S4.                           (2.4)
```

This definition permits arbitrary winding of every band arc.  There are
infinitely many literal arc systems, so brute enumeration of all braid words
would not be a finite classification.  The proof below instead quotients all
Hurwitz/conjugacy orbits by the two invariants needed for globalization:
boundary genus and meridional finite image.

## 3. The five-band slice-surface check and its firewall

The node factor is literally the product of two equal positive bands:

```text
c s_i^2 c^(-1)
 = (c s_i c^(-1))(c s_i c^(-1)).                       (3.1)
```

Consequently the full packet is a product of five conjugates of positive
standard generators.  Its canonical quasipositive braided surface in the
four-ball has

```text
0-handles = 4,
1-handles = 3+2=5,
chi       = 4-5=-1.                                    (3.2)
```

The first three bands already connect all four disks because their incidence
graph is a tree.  Hence the surface is connected.  Its boundary is the
one-cycle closure `K` of the product braid, so it has one boundary component
and genus one.

```text
-1 = 2-2g-1,          hence g(surface)=1
and g_4(K)<=1.                                           (3.3)
```

This is only a four-ball/slice-surface statement.  An arbitrary conjugate
positive band is quasipositive, not necessarily strongly quasipositive, so
(3.3) does **not** imply that the Seifert genus `g_3(K)` is at most one.  The
genus-one Seifert conclusion used later comes instead from the corrected
knot-at-infinity lemma plus the topology of the nearby regular algebraic
fibre.  This firewall prevents the false general implication
`quasipositive => strongly quasipositive`.

## 4. Full based coloring is a knot-group quotient

Let `F4=<x_1,x_2,x_3,x_4>` be the meridian group of a regular braid fibre.
For a closed four-braid `beta`, the usual Artin presentation is

```text
pi1(S3 - closed(beta))
 = <x_1,x_2,x_3,x_4 | x_j=beta_*(x_j), 1<=j<=4>,       (4.1)
```

with one redundant relation.  A tuple (2.3) fixed by the Hurwitz action of
`beta` is exactly a homomorphism from (4.1) sending `x_j` to `tau_j`.
Because the tuple is fixed by every local factor, it is fixed by their
product.  Equation (2.4) therefore gives a surjection

```text
pi1(S3-K) -> S4                                          (4.2)
```

which sends every strand meridian to a transposition.  A
matching-preserving `D4` packet need not satisfy (4.2); full `S4` is used
again only after polynomial globalization forces the trefoil group.

## 5. Globalization forces a genus-one graph knot

Assume now that the packet globalizes to a polynomial parametrization

```text
nu:A1 -> B subset A2                                    (5.1)
```

which is generically one-to-one and has the packet as its complete finite
braid monodromy.  The normalization adds only `t=infinity`, so the braid
closure `K` is the one-component link at infinity of `B`.

Choose a reduced polynomial `f` with `B=f^(-1)(0)`.  Corrected Lemma 7.1 of
Neumann--Rudolph applies literally: `B` is reduced and its link at infinity
is a knot, so `f` is good.  Choose a sufficiently small regular value
`epsilon` in a disk about `0` containing no other critical value.  Goodness
has two consequences needed here:

```text
the link at infinity of f^(-1)(epsilon) is still K;
there are no vanishing cycles escaping to infinity.     (5.2)
```

The compact core of `f^(-1)(epsilon)` is obtained by the ordinary local
smoothing of the sole affine node.  Indeed, choose one large ball for the
good fibration at infinity and a small Milnor ball around the node.  On the
complement of that Milnor ball the map has no critical point over the chosen
small value disk; Ehresmann triviality there, together with goodness outside
the large ball, leaves only the local node replacement.  Completeness of the
minimal packet excludes any other affine singularity or vanishing cycle.

To compute the core, start with a compact core of the normalization `A1`,
which is a disk `D`.  Remove small open disks around the two preimages of the
node.  The result has

```text
chi(D minus two disks)=1-2=-1.                          (5.3)
```

The Milnor fibre of an ordinary node is an annulus, of Euler characteristic
zero, and gluing its two boundary circles to those new boundary components
does not change (5.3).  The only remaining boundary is `K`.  Thus the nearby
regular fibre has a compact core of genus one.  Neumann 1989, Theorem 1 says
that this core is the unique minimal Seifert surface of its regular link at
infinity.  Consequently

```text
g_3(K)=1.                                                (5.4)
```

This is the rigorous genus bridge.  It depends on polynomial globalization,
connectedness at infinity, the absence of other affine singularities, and
the node being ordinary.  It does not follow merely from the abstract
quasipositive packet in Section 3.

Independently, Neumann's link-at-infinity construction makes `K` a graph
knot in `S3`.  A graph knot in `S3` is obtained from the unknot by iterating
connected sums and cable operations.  The Seifert genera obey

```text
g(J#K)=g(J)+g(K),
g(C_(p,q)(J))
 = p g(J) + (p-1)(|q|-1)/2,       p>=2, gcd(p,q)=1.     (5.5)
```

The second formula is Schubert's cable-genus formula.  Formula (5.5) makes
the genus-one census immediate.

* A connected sum of two nontrivial knots has genus at least two.
* A nontrivial cable of a nontrivial companion has genus at least
  `2g(J)>=2`.
* A cable of the unknot is a torus knot.  Genus one requires

  ```text
  (p-1)(|q|-1)=2.                                      (5.6)
  ```

  The only coprime solutions are `(p,|q|)=(2,3)` and `(3,2)`, which describe
  the same trefoil knot; the sign of `q` gives its mirror.

Thus (5.4) and the graph-knot classification force

```text
K = right trefoil or left trefoil.                      (5.7)
```

The Alexander screening statement (0.2) is now exact.  The unknot has
Alexander polynomial `1`, and either trefoil has `t^2-t+1`, up to a unit
`+/-t^j` in `Z[t,t^(-1)]`.  Multiplication by such a Laurent unit does not
alter nonzero roots.  No other Alexander polynomial belongs to a
genus-at-most-one graph knot.

## 6. The trefoil cannot carry the S4 coloring

Either orientation of the trefoil has a two-meridian Wirtinger presentation

```text
G_3_1=<a,b | aba=bab>.                                  (6.1)
```

Suppose a meridian-transposition representation sends `a` and `b` to
transpositions `A,B` in `S4`.

* If `A=B`, the image has order two.
* If `A` and `B` are distinct and disjoint, they commute.  Then
  `ABA=B` and `BAB=A`, so (6.1) would force `A=B`; this case is impossible.
* If `A` and `B` overlap in one letter, they satisfy the braid relation but
  generate the `S3` on their three-letter support.

Therefore

```text
|image(G_3_1)| is 2 or 6, never 24.                     (6.2)
```

This contradicts the surjection (4.2).  It follows that (5.1) cannot exist
for any packet in the class (2.1)--(2.4).

The deterministic exhaustive census is

| graph-knot candidate | Alexander polynomial | largest meridional transposition image |
|---|---:|---:|
| unknot | `1` | `C2`, order 2 |
| either trefoil | `t^2-t+1` | `S3`, order 6 |

There is no `S4` row and hence no smallest surviving packet.

## 7. Hurwitz/conjugacy classification at the required resolution

Hurwitz moves preserve the product braid, while simultaneous conjugation
conjugates it.  Both preserve the closure knot, the five-band census, and the
existence and image of the transported coloring.  Even between different
Hurwitz orbits, every packet satisfying (0.1) has the same slice-surface
census and the same full meridional quotient.  If any orbit globalizes, the
corrected good-polynomial lemma and the fixed affine singularity census give
the same genus-one regular fibre.

For the polynomial-globalization question the entire infinite packet space
therefore maps into the finite decision tree

```text
minimal packet
  -> genus-one quasipositive slice surface + meridional S4 quotient
  -> if polynomial one-place, good defining polynomial
  -> node smoothing = genus-one minimal Seifert surface
  -> genus-one graph knot
  -> trefoil
  -> meridional image at most S3
  -> contradiction.                                    (7.1)
```

This is a complete classification of the Hurwitz/conjugacy orbits at the
resolution needed by the infinity gate.  Distinguishing the arc systems more
finely cannot change any arrow in (7.1).

## 8. Firewalls and next global gate

Promote the universal exclusion only under the literal minimal/ordinary
hypotheses (0.1).

1. If the two conductor branches meet with intersection multiplicity `r>1`,
   the local factor is a conjugate of `s_i^(2r)`, not `s_i^2`.  The same
   four-disk construction then has `3+2r` bands and genus `r`; globally the
   local smoothing also has delta contribution `r`.  The trefoil collapse no
   longer applies.
2. An extra unibranch affine singularity contributes additional positive
   local bands and positive delta.  It likewise raises the nearby regular
   fibre genus and changes the graph-knot splice possibilities.
3. A nonminimal projection packet with extra positive factors is outside the
   five-band census even if its local quartic inertias remain rank two.
4. Dropping full `S4` coloring removes (4.2).  This report does not exclude a
   `D4`, `V4`, `S3`, or cyclic cover representation.

The next global gate for any surviving broader zero-cusp lane is therefore:

```text
compute the exact excess-band genus;
enumerate genus-g graph-knot splice/cable types allowed at infinity;
test their knot groups for meridional S4 transposition quotients;
then impose the one-place Puiseux semigroup and ruling data.             (8.1)
```

For tangency order `r`, (8.1) is finite at fixed `r` after the charged degree
and splice bounds are imposed.  The Alexander root-of-unity test remains the
cheapest first rejection, but it is not complete: distinct hyperbolic and
graph knots can share an Alexander polynomial.

Nothing here constructs a finite-flat quartic cover, an actual proper block,
a Keller first leg, a counterexample, or a proof of JC2.  The two ruling rows
`(A1,Q=1)` and `(P1,Q=0)` are not used.

## 9. Deterministic replay

```text
e1d0472bfbd5203d1e75582c3be5b44b50d9db4987d27b97b2864cee4931522f
  ops/block_descent_a1_quartic_cycle0_all_minimal_packets_replay.py
```

Ordinary, `python3 -O`, and `python3 -OO` runs are byte-identical, with

```text
stdout SHA-256:
ac80c949927f595026a04a245dc624a5b73b1107bc786ba1f9aeadfb06cf8521

status=PASS-R4-CYCLE-0-ALL-MINIMAL-B4-PACKETS
payload_sha256=05b5193ea018a8977ae67238aeb8c0b05f51e905362334a4103e4dcc01f8099f
```

The replay checks the four-disk/five-band genus census, enumerates all six
transpositions in `S4`, exhausts all 36 ordered transposition pairs in the
trefoil relation, obtains exactly six order-two and 24 order-six
representations, and verifies that none has image order 24.  It also finds
936 ordered four-tuples of transpositions which do generate `S4`, so the
full-color requirement is not vacuous, and it solves (5.6) exactly.  The
mutation `--mutate-drop-full-s4` exits nonzero when the forbidden threshold
is weakened to order six.

The replay does not encode the quasipositive band-surface theorem, the Artin
closed-braid group presentation, corrected Neumann--Rudolph good-polynomial
lemma, local-to-global node smoothing, Neumann's minimal-Seifert theorem,
Neumann's graph-link theorem,
Eisenbud--Neumann generation of graph knots, Schubert's genus formula, or
identification of the total braid with the knot at infinity.  Those are the
written theorem interfaces above.

No heavy local CAS was used.  Nothing here touches the formalization tree,
top ledgers, sealed lanes, or the campaign pilot log.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18443`.
- Body SHA-256:
  `6056d2720d9ae93feba5becca7de8d99119ee6f7f264c5c78c764aca9b3a22af`.
- Frozen basis: `7ff3257e9a5f944580cef9c7961296b6ca1db50c`.
