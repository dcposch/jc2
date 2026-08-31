# Hostile review: all-degree one-node meridional-rank obstruction

Reviewer: Opus 5, independent hostile referee  
Date: 2026-08-30 UTC  
Target: `xmodel/block-descent-a1-one-ordinary-node-all-degree-meridional-rank-obstruction-sol56-20260830.md`  
Companion charged predecessor: `xmodel/block-descent-a1-quartic-cycle0-all-minimal-packets-graph-knot-obstruction-sol56-20260830.md`

## 0. Verdict

```text
CONFIRM_W_CORR
```

The theorem (0.1)-(0.3) is **CONFIRMED**. Every load-bearing implication
reproduces, and the two citation interfaces I judged most likely to be
mis-stated -- corrected Neumann--Rudolph Lemma 7.1 and Neumann 1989
Theorem 1 -- were obtained from the primary sources and match the charged
wording essentially verbatim, including the absence of a smoothness
hypothesis on the fibre to which Lemma 7.1 is applied.

Four corrections, none fatal, none altering (0.3): one genuinely missing
step (C1, one sentence), two omitted-hypothesis nits (C2, C3), and one
overstatement of what the argument needs (C4, the conclusion is strictly
more robust than claimed).

I could not construct a counterexample to any interface. A 90-curve
computer search inside the theorem's own class (Section 5.2) failed to
break the single most load-bearing citation.

New results proved in this review, beyond the charged text:

```text
(R1)  g_3(K_infinity) = gamma + delta                    (Section 8.1)
(R2)  d <= 1 + bridge(K_infinity)                        (Section 8.2)
(R3)  the theorem extends verbatim to gamma+delta=1,
      and is SHARP there: the cuspidal cubic attains d=3 (Section 8.3)
(R4)  the true infinity class is iterated torus knots,
      not merely graph knots; connected sums cannot occur (Section 4.2)
```

No new exit price is asserted, so no `charge_basis` line is emitted.

## 1. Custody

All six charged hashes reproduce byte-exactly.

```text
c61f0cebdc06bdca88ad76f3714047a1998ff7aeb885a79e84b060a091c23329  (report)
6e21fa6cc4623e3e19a683e0b4e8a2b4d4d776ce04d4141e0630463dce6aa224  (artifact)
a6b000430e872e372c6c4cad9d694baa522746717eeef837e52884b206eff6fa  (replay)
e72a78f7dd027626b38ace5d770bf3b9be386b6626a2033fbb9d3ef81d79a444  (pred. report)
2200c712df980bc7ddc0e2c6d86be45878180f88b26851eec25dd39db51f5419  (pred. artifact)
e1d0472bfbd5203d1e75582c3be5b44b50d9db4987d27b97b2864cee4931522f  (pred. replay)
```

Both producer seals and both manifests recompute. Body is defined as every
byte through the unique standalone body-end HTML comment line inclusive
(marker spelled out only once per file, at its terminator); each charged
file contains exactly one such line.

```text
target : file_bytes 10979 = manifest; body_bytes 10646 = manifest;
         body bf9dfc3740dc88e6865b7f8a49b47c12a2b49d0f1da71b3411d07ea86d3d0dec
pred.  : file_bytes 18776 = manifest; body_bytes 18443 = manifest;
         body 6056d2720d9ae93feba5becca7de8d99119ee6f7f264c5c78c764aca9b3a22af
```

Custody status: **PASS**. No `CUSTODY_FAIL` condition arose.

### 1.1 Replay, three modes, negative controls

```text
ops/block_descent_one_node_all_degree_meridional_rank_replay.py
  ordinary / -O / -OO : rc=0, stdout SHA-256 identical in all three modes
  583da5d653ad234c9d642c3c7cc8d8ad31b30ab61f417c12df8fbdb7fa32831d   = report Sec.6
  payload_sha256 c4593ac35230962ea90bc535534fb9fa77abe0e409d18158743b660a0f1c1cd1
                                                                     = report Sec.6
  status PASS-ONE-NODE-ALL-DEGREE-MERIDIONAL-RANK                    = report Sec.6
  --mutate-allow-degree-three : rc=1 in all three modes

ops/block_descent_a1_quartic_cycle0_all_minimal_packets_replay.py
  ordinary / -O / -OO : rc=0, stdout SHA-256 identical in all three modes
  ac80c949927f595026a04a245dc624a5b73b1107bc786ba1f9aeadfb06cf8521   = pred. Sec.9
  payload_sha256 05b5193ea018a8977ae67238aeb8c0b05f51e905362334a4103e4dcc01f8099f
                                                                     = pred. Sec.9
  --mutate-drop-full-s4 : rc=1 in all three modes
```

**Fail-open check (explicit).** Neither script contains a single `assert`
statement; both gate through `require(cond, msg)` which raises
`RuntimeError`. This is why both negative controls still exit non-zero
under `-O` and `-OO`. This is the correct pattern and it closes the
`-O` fail-open hole that has bitten other lanes in this campaign. Neither
script reads `__doc__`, so `-OO` docstring stripping is inert. Recorded as
a positive finding.

Reported secondary counts also reproduce: predecessor
`s4_generating_ordered_transposition_4tuples = 936`, image-order census
`{2:6, 6:24}`, torus census `[[2,3],[3,2]]`; target `maximum_transitive_support = 3`
and per-degree census `equal = d(d-1)/2`, `overlapping = d(d-1)(d-2)`.

I re-ran the entire group-theoretic census in an **independently written
implementation** (my own composition/orbit/closure code, not the charged
one) for `2 <= d <= 8`. Every number agrees, including `disjoint = 0`,
`max orbit = min(d,3)`, `max image order = 6` for `d >= 3`.

## 2. Obligation 1 -- A1 normalization, one place, and Lemma 7.1

### 2.1 `A1` implies a knot at infinity: CONFIRMED

Reconstruction, not paraphrase. `B` is an affine plane curve, hence closed
in `A2`; normalization is a finite birational morphism, so
`nu: A1 -> B` is finite and surjective and `B` is a polynomial image of
the line. Let `Bbar` be the projective closure. The normalization of
`Bbar` is the smooth compactification of `A1`, namely `P1`, and the places
of `B` at infinity are the points of `P1` over `Bbar ∩ L_infinity`, i.e.
`P1 - A1`, a single point. Components of the link at infinity
`B ∩ S^3_R` correspond to branches of `Bbar` at `L_infinity`, hence
`K_infinity` is a knot. **CONFIRMED.**

Side consequence used later: one place at infinity forces `B` irreducible
(every affine curve component has at least one end), so the irreducibility
hypothesis in (0.1) is redundant given the normalization hypothesis, and
`f` is irreducible hence primitive (if `f = P(g)` with `deg P >= 2`, then
`f` factors over `C`), so generic fibres are irreducible. The report does
not use primitivity explicitly; it does not need to (Section 3.2).

### 2.2 Corrected Neumann--Rudolph Lemma 7.1: CONFIRMED VERBATIM

I obtained the corrigendum itself (Math. Ann. 282 (1988) 349-351,
Gottinger Digitalisierungszentrum scan, `PPN235181684_0282/LOG_0040`) and
read pages 349-351. The corrected statement is, literally:

> **7.1. Lemma (A Knot at Infinity is Good).** If `V ⊂ C^2` is a fiber of
> `f: C^2 -> C` and is *reduced* and its link at infinity is a knot (`V` is
> connected at infinity) then `f` is good.

Audit of every hypothesis against the report's use:

```text
"V is a fiber of f"          : V = f^{-1}(0) = B.                       OK
"V is reduced"               : f squarefree, chosen so in Sec.2.        OK
"link at infinity is a knot" : Section 2.1 above.                       OK
NO smoothness/regularity hypothesis on V.                               OK
NO primitivity hypothesis.                                              OK
NO degree or genus hypothesis.                                          OK
```

This is the audit item that mattered most: the report applies 7.1 to a
**singular** fibre (the one carrying the node). The corrected lemma places
no non-singularity hypothesis on `V`, so the application is legitimate.
The direction is also as stated (knot at infinity `=>` good, not the
converse). **CONFIRMED.**

The corrigendum's own definition, which is the one consumed:

> The fiber `f^{-1}(c)` ... is *regular at infinity* if there exists a
> neighborhood `D` of `c` and a compact set `K` such that
> `f | f^{-1}(D) - K : f^{-1}(D) - K -> D` is a locally trivial `C^inf`
> fibration. The polynomial map `f` is *good* if every fiber is regular at
> infinity. ... We denote by `H(f,inf)` the link at infinity of any fiber
> which is regular at infinity; up to isotopy this is independent of the
> choice of the fiber.

That last clause is exactly the report's "goodness identifies the links at
infinity of `f^{-1}(0)` and `f^{-1}(epsilon)`". **CONFIRMED.**

The report's three claims about the corrigendum are each true:

```text
"corrects the definition of a good polynomial"  -> p.349: "the definition
     of 'good' must be modified as follows", replacing the old
     "only isolated singularities" definition.                        OK
"explicitly restates and reproves the lemma"    -> p.349 restatement,
     p.351 "Proof of 7.1".                                            OK
"Neumann 1989, page 446, consumes the corrected form" -> Neumann 1989
     p.445-446 cites "[N-R 1, Lemma 7.1]", and the 1989 bibliography
     defines [N-R 1] as the 1987 paper "and: Corrigendum ... ibid. 282,
     349-351 (1988)". The citation therefore points at the corrected
     lemma.                                                           OK
```

Neumann 1989, pp. 445-446, states the consequence in the report's own
words: `f` is good "if any fiber of `f` is reduced and has a knot as its
link at infinity (i.e., it is connected at infinity), cf. [N-R 1, Lemma 7.1]".

The corrigendum's proof of 7.1 also gives a bonus the report does not use:
"By Suzuki [S], the general fiber of `f` is also connected at infinity, so
`H(f,inf)` is a knot. As described in [N-R], **it is an iterated torus
knot**, hence fiberable, so `f` is good by Theorem 6.1." See Section 4.2.

Note the corrigendum's Example on p.349, `f = x^2 y + x`, whose zero fibre
has three components at infinity while nearby fibres have two: this is the
canonical failure of goodness, and it has no knot fibre, consistent with
7.1. I re-derived that example independently before reading the page.

## 3. Obligation 2 -- the nearby fibre and the genus-one core

### 3.1 Node smoothing and absence of hidden vanishing cycles: CONFIRMED

Given goodness, choose `R >> 0` with `f` transverse to `S^3_R` over a small
disc `D` about 0 containing no other critical value, and a Milnor ball `M`
about the sole node. Over `D`, `f` restricted to `B_R - M` is proper with
no critical point, and by goodness the exterior of `B_R` is a product; so
Ehresmann gives triviality outside `M`, and the only change from
`f^{-1}(0)` to `f^{-1}(epsilon)` is replacement of the node cone by the
node Milnor fibre. Absence of vanishing cycles at infinity is exactly the
"regular at infinity" clause; absence of other affine vanishing cycles is
hypothesis (0.1). **CONFIRMED.**

### 3.2 Euler count, connectedness, genus: CONFIRMED

Core of the normalization is a disc, `chi = 1`; delete two discs at the two
node preimages (an ordinary node has two distinct smooth branches, so the
preimages are distinct), `chi = -1`, three boundary circles; glue the
node Milnor fibre, an annulus with `chi = 0`, along two of them:
`chi(A ∪_{S^1 ⊔ S^1} B) = chi(A) + chi(B) = -1`, one boundary circle left,
which is `K_infinity`. Then `2 - 2g - 1 = -1` gives `g = 1`. **CONFIRMED.**

Cross-check by a second route (mine, not the report's): for a good
polynomial `chi(F_eps) = chi(B) - mu`, with `chi(B) = chi(A1) - (r_p - 1) = 0`
and `mu(node) = 1`, so `chi(F_eps) = -1`; `F_eps` has one end because its
link at infinity is `K_infinity`, a knot; hence `1 - 2g = -1`, `g = 1`.
Agrees.

**Connectedness** is not argued in the report but is not a gap: a
disconnected `F_eps` would have at least two ends, hence a link at infinity
with at least two components, contradicting goodness. It is also delivered
by primitivity of `f`, and independently by Suzuki's theorem quoted inside
the corrigendum's proof of 7.1. Three independent routes; no defect.

### 3.3 Boundary knot identity: CONFIRMED

`f^{-1}(0)` and `f^{-1}(epsilon)` have the same link at infinity by the
corrigendum's definition clause quoted in Section 2.2.

## 4. Obligation 3 -- Neumann 1989 Theorem 1

### 4.1 What the source actually says: CONFIRMED, with a separation

Neumann 1989, p.447, verbatim:

> **Theorem 1.** The topology of a *regular* algebraic plane curve
> `V ⊂ C^2` (as an embedded smooth manifold) is determined by its link
> `L = (S^3, L)` at infinity. In fact a minimal Seifert surface `F` for `L`
> in `S^3` is unique up to isotopy in `S^3`, and `V` can be recovered up to
> proper isotopy in `C^2` by attaching a collar out to infinity to the
> boundary of such an `F`.

with footnote 5: "A minimal Seifert surface `F` is a surface with maximal
Euler characteristic among all oriented embedded surfaces with no closed
components in `S^3` with `∂F = L`. `F` may not be unique up to isotopy as a
Seifert surface: the isotopy need not fix `L`."

And p.446: "An algebraic curve `V` will be called *regular* if it is a
regular fiber of its defining polynomial `f`", together with p.445
"'Regular' is equivalent to 'regular at infinity and non-singular'".

Applied to `V = f^{-1}(epsilon)`: non-singular because `epsilon` is a
regular value, regular at infinity because `f` is good. So `V` is a regular
algebraic curve and Theorem 1 applies. Since `V` is `F` plus a collar, the
compact core of `V` *is* `F` up to isotopy, and `F` is a minimal Seifert
surface in `S^3`. Hence `g_3(K_infinity) = 1`. **CONFIRMED.**

**Separation of what is needed from the stronger wording.** The report says
"identifies this core with the *unique minimal* Seifert surface". Two
distinct pieces are bundled:

```text
(a) the core is isotopic to a surface in S^3 with boundary K_infinity
    -> gives g_3 <= 1.  LOAD-BEARING.
(b) that surface is minimal, and minimal ones are unique
    -> gives g_3 = 1 exactly.  NOT load-bearing.
```

Only (a) is needed. If one keeps only (a), the genus census admits the
unknot as well, and the unknot case gives image `C2`, maximum orbit `2`,
hence `d <= 2`, which is stronger than (0.3). So (0.3) survives on (a)
alone. See correction C4. Note that (a) is genuinely needed: the
predecessor's Section 3 quasipositive band surface lives in `B^4` and
bounds only `g_4 <= 1`; the report is right to firewall that, and right not
to substitute it. Neumann 1989 p.446 supplies the mechanism for (a)
independently: "If `f` is good it is easy to see that there is a 'Milnor
fibration at infinity,' so `L(f,inf)` is a fibered link."

### 4.2 A source-level strengthening the report did not take: (R4)

Both primary sources state that the class is narrower than "graph knot":

* Neumann 1989 p.447: "A link at infinity is always a *toral link*, that
  is, it can be built up by iterated cabling operations from the unknot."
* NR corrigendum p.351, proof of 7.1: for a knot at infinity, "it is an
  **iterated torus knot**".

A connected sum of two non-trivial knots is a graph knot but is *not* an
iterated torus knot. The report's candidate set (graph knots = cablings and
connected sums) therefore strictly **contains** the truth. That is the safe
direction: the report enlarges the candidate set and still wins, so no
defect. But it is worth banking, because it deletes the entire connected-sum
branch of every future genus-`g` census (Section 9). **CONFIRMED, safe
over-approximation.**

## 5. Obligation 4 -- graph knots of genus one

### 5.1 The census: CONFIRMED

Reconstructed independently:

* `g(J # K) = g(J) + g(K)` (Seifert genus additive under connected sum).
  A connected sum of two non-trivial knots therefore has `g >= 2`.
* `g(C_{p,q}(J)) = p g(J) + (p-1)(|q|-1)/2`, `p >= 2`, `gcd(p,q) = 1`.
  If `g(J) >= 1` then `g >= p >= 2`. So the companion is the unknot
  (`g(J) = 0` implies `J` unknotted), leaving `(p-1)(|q|-1) = 2`, whose only
  coprime solutions are `(p,|q|) = (2,3)` and `(3,2)`, both the trefoil, the
  sign of `q` selecting the mirror.
* Degenerate satellites are handled: `p = 1` returns the companion; `|q| = 1`
  gives `(p-1)·0 = 0 != 2`; `p = 0` is not a cable.
* Orientation: mirroring preserves genus, and both trefoils are retained.

Hence genus `<= 1` toral/graph knots are exactly `{unknot, T(2,3), T(2,-3)}`.
**CONFIRMED.** With (R4) the argument shortens to "cables of the unknot are
torus knots, `(p-1)(|q|-1) = 2`", with no connected-sum case at all.

### 5.2 Disclosure on Schubert

I did **not** read Schubert, *Knoten und Vollringe*, Acta Math. 90 (1953),
directly; it was not obtained. I cross-validated the two formulas instead:
the cable formula on the unknot reduces to the classical torus-knot genus
`(p-1)(q-1)/2`, which returns `g(T(2,3)) = 1` and `g(T(3,4)) = 3`, and
`g(T(2,3)) = 1` is independently pinned by `deg Delta_{3_1} = 2` and by the
once-punctured-torus fibre of the trefoil. Genus additivity under connected
sum is classical and not in dispute. This is an execution gap, declared;
its blast radius is confined to Section 5.1, and Section 5.1 is
over-determined by the reduction in (R4).

I also did not obtain the Eisenbud--Neumann book. Its two uses -- links at
infinity are toral/graph links, and generation of such knots in `S^3` -- are
both stated in Neumann 1989 p.447 and in the NR corrigendum p.351, which I
did read. So the EN interface is corroborated without the book.

## 6. Obligation 5 -- the surjection `G_infinity ->> G_aff`

### 6.1 Topological identification of the boundary braid: CONFIRMED

Take a projection with `f` monic in `y` up to a constant, i.e. `pi|_B`
proper of degree `N = deg_y f` ("generic finite projection" in the report).
Properness gives `B ∩ (D_R x ∂D_{R'}) = ∅` for `R' >> R`, so

```text
B ∩ ∂(D_R x D_{R'}) = B ∩ (∂D_R x D_{R'}) = closed braid of beta_infinity,
```

and `∂(D_R x D_{R'})` is a sphere at infinity for a suitable exhaustion.
So `K_infinity` is the closure of the total braid monodromy braid
`beta_infinity = beta_1 ... beta_s` over a circle enclosing all critical
values. The closed-braid/axis distinction is respected: the closure is
taken in the solid torus `∂D_R x D_{R'}`, and the complementary solid torus
`D_R x ∂D_{R'}` carries the axis. **CONFIRMED.**

Independent numerical cross-check of this identification: for the nodal
cubic `y^2 = x^3 + x^2`, `N = 2`, `disc_y = 4x^2(x+1)` of degree 3, so
`beta_infinity = sigma_1^3`, whose closure is the trefoil, matching the
genus-1 prediction (`chi = N - e = 2 - 3 = -1`). Had one wrongly used
`N = deg f = 3` strands with `e = d(d-1) = 6`, one would get `chi = -3`,
genus 2, and a contradiction. The report's "generic finite projection" is
the hypothesis that prevents that error.

### 6.2 The two presentations and the direction of the map: CONFIRMED

Artin: `pi1(V - beta^) = <x_1..x_N, t | t x_j t^{-1} = beta_*(x_j)>` is the
mapping torus of `beta` on the `N`-punctured disc; filling the complementary
solid torus kills `t` (its meridian is the longitude of `V`), giving

```text
G_infinity = pi1(S^3 - K_infinity) = F_N / <<x_j^{-1} beta_infinity(x_j)>>,
```

one relation redundant because `beta_*` fixes `x_1...x_N`.

Zariski--van Kampen for the affine complement, with the same properness
hypothesis and `B` containing no vertical line:

```text
G_aff = pi1(A^2 - B) = F_N / <<x_j^{-1} beta_v(x_j) : all j, v>>.
```

Direction check, since this is the step most easily inverted. If each
`beta_v` induces the identity on `G_aff`, so does the composite
`beta_infinity`, hence `x_j^{-1} beta_infinity(x_j)` lies in the normal
closure of the affine relators. Therefore the affine relator set is the
larger one, and

```text
G_infinity ->> G_aff ,  x_j |-> x_j ,
```

surjective, meridian to meridian, and *not* the other way. **CONFIRMED.**
"Individual affine braid relations imply the single infinity relation" is
exactly this containment. **CONFIRMED.**

The inverse convention is genuinely harmless: `beta` induces the identity on
a quotient iff `beta^{-1}` does, so the two normal closures coincide;
mirroring `K_infinity` is also harmless because both trefoil mirrors are
carried through Section 7.

The product ordering depends on the distinguished path system; different
choices change `beta_infinity` only by Hurwitz moves and conjugation, which
change neither the closure nor the normal closure of the relators.

There is no projective/infinity relation to worry about here: the base of
the affine pencil is `A1`, whose fundamental group is free on the loops
around the critical values, so no extra relation is imposed, and the
*single* extra relation of the projective theory is precisely (3.2). The
report keeps these separate correctly.

## 7. Obligation 6 -- trefoil meridional rank

### 7.1 Two-meridian presentation, both mirrors: CONFIRMED

`<a,b | aba = bab>` is the Wirtinger presentation of the standard trefoil
diagram with `a,b` meridians; the mirror has an isomorphic group under an
orientation-reversing homeomorphism carrying meridians to meridians. Since
a transposition is an involution, the orientation of a meridian is
irrelevant to hypothesis (0.2). **CONFIRMED.**

### 7.2 Exhaustion of transposition pairs: CONFIRMED

Two transpositions are equal, disjoint, or overlap in exactly one letter.

```text
A = B          : ABA = A = BAB.               relation holds, image C2,
                                              largest orbit 2.
A,B disjoint   : ABA = B, BAB = A, so the
                 relation forces A = B.       impossible.
A,B overlap    : (12),(23): ABA = BAB = (13). relation holds, image S3 on
                                              three letters, orbit 3.
```

Hence every meridian-transposition image of the trefoil group moves at most
three letters and has order 2 or 6, for every `d`. A transitive image needs
orbit `d`, so `d <= 3`, i.e. transitivity is impossible for all `d >= 4`.
**CONFIRMED** symbolically for all `d`, and reproduced numerically in my own
implementation for `2 <= d <= 8` and by the charged replay for `2 <= d <= 10`.

### 7.3 The step the report omits: correction C1

The report writes "Put `A = rho(a)` and `B = rho(b)`. Both are transpositions
in `S_d`" without justification. `a,b` are the *Wirtinger* meridians of
`K_infinity`; the hypothesis (0.2) is about meridians of `B`, and the
presentations (3.1)/(3.2) are written on the *fibre* meridians `x_j`. The
missing link is:

> all meridians of a knot are conjugate in its group (they are isotopic on
> the boundary torus, hence freely homotopic in the complement), and all
> meridians of an irreducible plane curve are conjugate in the complement
> group;

so `a, b` are conjugate to the `x_j` in `G_infinity`, their images are
conjugate to `rho(x_j)`, and conjugates of transpositions are
transpositions. With that sentence the step is airtight. **GAP, fillable in
one sentence; blast radius: Section 4 of the report only; conclusion
unaffected.**

The alternative formulation the report offers in the last paragraph of its
Section 4 -- transitive transposition generation of `S_d` needs `>= d-1`
generators, trefoil meridional rank is 2 -- is correct and needs the same
conjugacy fact.

## 8. Obligation 7 -- the cover interpretation

**Connectedness vs. transitivity: CONFIRMED.** For an unbranched degree-`d`
cover of `A^2 - B` with monodromy `rho`, connectedness of the total space is
equivalent to transitivity of `rho`. This is what (0.2) encodes.

**Simple branching vs. transposition meridians: CONFIRMED.** Generic simple
ramification over `B` gives transposition image for a generic meridian; `B`
irreducible makes all meridians conjugate, so *every* meridian, including
those encircling a branch at the node, maps to a transposition. The report's
"every positively oriented generic meridian" is therefore neither weaker nor
stronger than needed.

**Singular branch values: CONFIRMED harmless.** Nothing in the argument
requires the cover to be simply branched over the node or over the vertical
tangency values; only the conjugacy class of the generic meridian is used.

**Unrecorded branch components: correctly flagged.** If the cover were also
branched over some `B'` disjoint from `B`, then the monodromy would live on
`pi1(A^2 - B - B')`, with extra meridional generators, and the theorem would
not apply. The report states exactly this in its Section 5, item 4, and
phrases the corollary as "complete branch curve". **No overclaim.**
Ramification in codimension two is irrelevant, since deleting a codimension-two
set does not change `pi1`.

## 9. Obligation 8 -- the degree-three firewall

Precise content, in three separated statements:

```text
(i)  The group-theoretic step cannot exclude d=3: two overlapping
     transpositions in S_3 satisfy aba=bab and act transitively.
     The replay mutation --mutate-allow-degree-three exits non-zero
     for exactly this reason.  Verified in all three modes.
(ii) At an ordinary node the two local branch meridians commute, because
     the local complement group of a node is Z^2.  Two commuting
     transpositions are equal or disjoint.  In S_3 there is no pair of
     disjoint transpositions.  So in degree three the node meridians must
     be EQUAL; the local (2,2) inertia does not exist below degree four.
(iii) Consequently the S_3 quotient of the trefoil group says nothing
     about a (2,2) node packet, and conversely the (2,2) obstruction says
     nothing about d=3.  They are disjoint statements.
```

The report asserts exactly (i)-(iii) and no more. **CONFIRMED, no
overclaim.** The degree-three survivor, if it exists at all, must carry
equal node colours, whose local cover is the `A1` surface point `z^2 = xy`
plus `d-2` trivial sheets; nothing in (0.1)-(0.2) forbids that.

Sharpness note, mine: `d = 3` is *not* known to be attained inside the
report's node class. For the smallest member, the nodal cubic
`y^2 = x^3 + x^2`, I computed the affine Zariski--van Kampen presentation
from `beta_1 = sigma_1^2` (node) and `beta_2 = sigma_1` (vertical tangency):
the relation from `sigma_1` alone gives `x_2 = x_1` and
`x_1 = x_1 x_2 x_1^{-1}`, so `pi1(A^2 - B) = Z` and `d <= 2` there. So (0.3)
is correct but possibly not sharp in the node class. See Section 11.

## 10. Obligation 9 -- falsification attempts

I attacked the weakest link, which is Lemma 7.1, before I had the source.

**Attempt 1 (analytic).** In the chart at the unique point `p` at infinity,
the whole pencil is `G_c = G_0 - c z^d`, i.e. `c` perturbs only the
coefficient of `z^d`, while every other monomial of the germ lies strictly
below the line `u + v = d`. Along the branch `B_0`, `(B_0 . {z^d}) = d^2`,
while Teissier's polar identity gives
`(B_0 . {∂G_0/∂y = 0}) = mu + (B_0 . {z=0}) - 1 = 2 delta_inf + d - 1`,
which is `< d^2` for all `d` by the genus bound
`delta_inf <= (d-1)(d-2)/2`. So the perturbation always sits strictly beyond
the polar. This is the right shape of a proof but I could not close the
remaining estimate `d^2 - (B.polar) > beta_g` by crude bounds for
`d >= 4`; I record it as suggestive, not as a proof. (I verified the polar
identity on two germs: `z - y^3` gives 2, and `z^2 - y^3` gives 4.)

**Attempt 2 (computational, 90 curves in the theorem's own class).** I
sampled polynomial parametrizations `t |-> (x(t), y(t))` with
`gcd(deg x, deg y) = 1`, which produces exactly the geometry of (0.1)
without the node condition: `A1` normalization and one place at infinity.
For each, I formed the implicit equation by resultant, verified the leading
form is a `d`-th power of a linear form, passed to the chart at `p`, and
computed the number of branches and the delta invariant of the germ of
`f^{-1}(c)` at `p` for `c = 0, 1, 2` with Singular's Hamburger--Noether
expansion.

```text
degrees covered      : 3,4,5,6,7,8,9,10,11
delta_infinity range : 0 .. 30
curves fully tested  : 90
germ at infinity constant in c (branches AND delta) : 90
jumps found          : 0
```

Positive controls for the tool: `delta((z-y^3)z) = 3`, `delta(yz) = 1`,
`delta(z^2-y^3) = 1`, `delta(z^2-y^5) = 2`, all correct.

**Attempt 3 (random dense search) produced 15 apparent jumps, all
artifacts.** Every one had `f` in `C[y]` alone or non-squarefree
(`f = y^3`, `y^4`, `y^3 - y + 1`, `y^4 + 2y^2`), i.e. a union of parallel
lines or a multiple line. These violate the reducedness hypothesis of
Lemma 7.1 or are not irreducible curves at all, and Singular's branch count
on a non-reduced germ reports the reduced branch count, which is what
produced the false positives. Recorded because it is instructive: the
reducedness hypothesis in Lemma 7.1 is *not* decorative. Any future lane
that drops it will produce exactly these fake survivors.

**No counterexample to any interface was found.** After the sources arrived,
Attempts 1-3 became redundant, but they remain the honest independent check.

I also checked the citation metadata: both charged reports cite
Eisenbud--Neumann as *Annals of Mathematics Studies* **110**, which is
correct; Neumann's own 1989 bibliography prints "101". The charged reports
are right and the primary source has the typo.

## 11. Maximum-safe theorem

Everything below is proved, not conjectured.

**Theorem (safe form, strictly stronger than the charged (0.3)).**
Let `B ⊂ A^2` be a reduced irreducible affine plane curve with

```text
(H1) exactly one place at infinity (equivalently, B is connected at
     infinity, equivalently its link at infinity K is a knot);
(H2) gamma + delta = 1, where gamma is the geometric genus of B and
     delta = sum of the delta invariants of its affine singularities.
```

Let `rho: pi1(A^2 - B) -> S_d` send generic meridians to transpositions with
transitive image. Then `d <= 3`.

The charged theorem is the sub-case `gamma = 0`, `delta = 1`, singularity an
ordinary node. The extension is free: (H1) plus reducedness is all that
Lemma 7.1 needs, and the genus law below replaces the node-specific Euler
count.

**(R1) Genus law.** Under (H1) and goodness, `g_3(K) = gamma + delta`.
Proof: `chi(F_eps) = chi(B) - sum mu_p`, `chi(B) = (1 - 2 gamma) - sum(r_p - 1)`,
`mu_p = 2 delta_p - r_p + 1`, so `chi(F_eps) = 1 - 2 gamma - 2 delta`;
`F_eps` has one end, so `g(F_eps) = gamma + delta`; by Neumann 1989
Theorem 1 that core is a minimal Seifert surface for `K`. This reproduces
`g = 1` for the charged case and is the invariant form of the report's
Section 2 count.

**(R2) Degree law.** `d <= 1 + mr(K) <= 1 + bridge(K)`, where `mr` is the
meridional rank. Proof: the image is generated by `mr(K)` transpositions;
the orbits of a group generated by transpositions are the components of the
graph whose edges are their supports; transitivity forces that graph
connected on `d` vertices, hence at least `d - 1` edges. `mr <= bridge`
since a bridge presentation supplies that many meridian generators. No
meridional rank conjecture is invoked, only the trivial inequality.

**(R3) Sharpness at `gamma + delta = 1`.** The bound `d <= 3` cannot be
improved in the safe class: the cuspidal cubic `y^2 = x^3` satisfies (H1)
and (H2) with `gamma = 0`, `delta = 1`, is the discriminant of the versal
deformation of `A2`, has `pi1(A^2 - B) = B_3 = <a,b | aba = bab>`, and its
degree-three simple cover `{(x,p,q) : x^3 + px + q = 0}` realises a
transitive transposition image in `S_3`. Within the *node* class the bound
is not known to be sharp; the nodal cubic itself only reaches `d = 2`
(Section 9).

**Robustness.** (0.3) does not need `g_3 = 1`; `g_3 <= 1` suffices, because
the extra candidate admitted, the unknot, gives `d <= 2`. So the theorem
survives even if only clause (a) of Neumann Theorem 1 is granted.

**What remains outside.** All five scope items of the report's Section 5
stand, with item 2 sharpened: a *unibranch* singularity is not by itself
outside the safe theorem (a cusp has `delta = 1` and is covered); what is
outside is any configuration with `gamma + delta >= 2`. Multiple places at
infinity remain the expensive horn, because Lemma 7.1 then gives nothing
and goodness has to be bought separately.

## 12. Corrections

```text
C1  Sec.4, "Both are transpositions in S_d" is asserted without the
    conjugacy of meridians.  Insert: all meridians of a knot are conjugate
    in its group, so the Wirtinger meridians a,b of K_infinity are
    conjugate to the fibre meridians x_j, whose images are transpositions
    by (0.2).
    Blast radius: Sec.4 only.  Conclusion unaffected.  Severity: editorial.

C2  Sec.2, formula (2.4) drops the hypotheses "p >= 2, gcd(p,q) = 1" that
    the predecessor's (5.5) carries.  Without them the census argument does
    not close (p = 1 returns the companion).
    Blast radius: Sec.2 statement only.  Severity: editorial.

C3  Sec.3 leans on "generic finite projection" to deliver both the
    Zariski--van Kampen presentation and K_infinity = closure(beta_infinity).
    The operative content is properness of the projection on B (leading
    y-coefficient constant, no vertical asymptote) and N = deg_y f, not
    N = deg f.  Worth making explicit: the wrong strand count changes the
    predicted genus (Section 6.1).
    Blast radius: Sec.3 exposition.  Severity: editorial.

C4  Sec.2 claims g_3(K_infinity) = 1 via the "unique minimal" clause of
    Neumann Theorem 1.  Only g_3 <= 1 is load-bearing, and the unknot case
    it admits yields d <= 2.  The report is therefore weaker than its own
    argument.  Also, Neumann's footnote 5 restricts the uniqueness to
    isotopy in S^3 not fixing L; immaterial here.
    Blast radius: none; the correction strengthens the result.
```

No `REFUTED` finding. No claim in either charged report was found false.

## 13. Cheapest next attack

Ranked, cheapest first.

**A. The `gamma + delta = 2` census (recommended).** By (R1) the infinity
knot has `g_3 = 2`, and by (R4) it is an *iterated torus knot*, so
connected sums are already excluded and the census is tiny. Enumerate:
one-step cables of the unknot give `(p-1)(|q|-1) = 4`, i.e. `T(2,5)` only
(bridge 2, so `d <= 3` by (R2)). Two-step cables need
`p_2 g_1 + (p_2-1)(|q_2|-1)/2 = 2` with `g_1 >= 1`, forcing
`p_2 = 2`, `g_1 = 1`, `|q_2| = 1`, i.e. `C_{2,±1}(trefoil)`, bridge 4,
`d <= 5`. So the **entire** question at `gamma + delta = 2` reduces to one
finite, purely combinatorial gate:

```text
Can a (p, ±1) cabling step occur in the RPI splice diagram of a
one-place link at infinity?
```

If no, then `gamma + delta = 2` also yields `d <= 3`, closing tangential
nodes (`r = 2`), two-node curves, node-plus-cusp, `A4`, and genus-one
one-node curves in one stroke. The decision procedure is Neumann 1989
Section 3 plus the regularity condition `l_v >= 0` (Neumann--Le Van Thanh,
Definition 1.1 and Theorem 1.2, arXiv alg-geom/9202008, which I read).
Cost: a splice-diagram calculation on a chain with at most two nodes. This
is by far the highest ratio of horn closed to work done.

**B. Sharpen the node class to `d <= 2`.** Add the node relation to the
trefoil quotient: in `S_3` the two node meridians must be equal, so ask
whether the equal-colour node is compatible with the `S_3` quotient of
`G_aff` for *some* member of (0.1), not merely of `G_infinity`. The
nodal-cubic computation in Section 9 shows the answer is no for the
smallest member. Cost: one braid-monodromy computation per degree, or a
structural argument. Payoff: removes the residual `d = 3` row.

**C. Multiple places at infinity.** Expensive and not recommended yet:
Lemma 7.1 is unavailable, goodness must be purchased (Neumann--Le Van Thanh
Theorem 1.2 gives the exact criterion, `l_v >= 0` on the RPI diagram), and
the link at infinity is no longer a knot, so the meridional-rank step must
be redone for links.

Do not attempt to infer JC2, exclusion outside the stated branch-curve
class, or anything about proper blocks or ruling data from this review.
None of it is licensed by the material audited here.

## 14. Execution disclosure

Shell, network, Singular 4.x, sympy and pdf tooling were available and used.
Primary sources actually read: Neumann, Invent. Math. 98 (1989), pp.
445-447 and p. 489 (GDZ scan `PPN356556735_0098/LOG_0028`);
Neumann--Rudolph corrigendum, Math. Ann. 282 (1988), pp. 349-351 (GDZ scan
`PPN235181684_0282/LOG_0040`); Neumann--Le Van Thanh, arXiv
alg-geom/9202008 (TeX source). Not obtained, and declared as gaps:
Eisenbud--Neumann (1985), corroborated indirectly as described in Section
5.2; Schubert (1953), formulas cross-validated as described in Section 5.2;
the body of Neumann--Rudolph (1987), of which only the corrected statements
in the corrigendum were needed. Zariski--van Kampen and the Artin
closed-braid presentation were reconstructed from scratch rather than cited.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `36327`.
- Body SHA-256:
  `377ef6c76542c350636c74e33ba4fd0ecb6a67a2a56cfc3b091253fcc8483bbb`.
- Frozen basis: `684350d99a7386a208a14eebf461d399dcd95713`.
