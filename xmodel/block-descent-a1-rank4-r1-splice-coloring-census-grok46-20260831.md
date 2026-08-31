# R1 two-component splice-colouring census at `n22=1`

Date: 2026-08-31 UTC
Lane: bounded primary research; not a review and not a promotion
Git HEAD: `2fb3d7c6bb046edb05193782da4e1f597fed3016`
Charged input SHA-256: `513fe4c022b3a84531c0e42e4cc61a1c9cf2732dde4a5931cb6f8384e166ad4d`
Charged input: frozen copy of `xmodel/block-descent-a1-rank4-reducible-component-tree-ledger-grok46-20260831.md`

This report asserts no new exit price. The charged ledger is `PROVISIONAL` and under separate hostile review; every dependence on it is labelled `PROVISIONAL`. Lemma 2.3 of that ledger (missing-multiplicity) is not charged. Row R1 is live in the safe column of the ledger (`OREV-MISS; else OPEN`).

## 0. Verdict

Row R1 at `n22=1` is **not closed**. The conductor/delta budget licenses three chargings of the unique `A2` cusp and the unique ordinary conductor node. Two chargings are empty for every licensed splice diagram. The third is colourable.

- Charging `(1,1)` — cusp on one component, self-node on the other, both knots at infinity trefoils — is empty. A trefoil transposition representation never contains a disjoint pair, so that component cannot carry the charged `(12)|(34)` pairing (Lemma 2.5). The explicit torus-link control `T(4,+/-6)` has 72 labelled stage-A `S4` colourings and zero with cusp packet on one component and pairing on the other.
- Charging `(2,0)` — cusp and self-node on the same component, the other an unknot — is empty at stage A. The licensed genus-two knots `T(2,+/-5)` and `C(2,+/-1)(T(2,+/-3))`, each union an unknot, have no full-`S4` transposition colouring of the closed braid.
- Charging `(1,0)` mixed — cusp on `B1` (trefoil), conductor node an inter-component identification, `B2` an unknot — is **colourable** for every linking residue. This is the family `F1` of 3-braids `sigma1^{+/-3} sigma2^{+/-2n}` with `n>=1`. Stage B, with the individual cusp factor, the ordinary mixed twist, and the charged pairing, has exactly eight labelled full-`S4` colourings, independent of `n` and of both signs. Witness: strand colours `(13)`, `(12)`, `(34)`.

The colourable family is a sharpened surviving target for `PROVISIONAL` row R1 at `n22=1`. It is not an existence proof of an embedded curve, a finite cover, or a Keller map. The honest infinite direction is the linking number `n` of the two-unknot torus-link core; transposition colouring depends on `n` only through the order-six Artin action of `sigma2` on `6^3` triples, so the colouring census is finite. Higher unibranch points `A_{2p}` with `p>1` are outside the enumerated slice (§2.4).

## 1. What is consumed

`PROVISIONAL` row R1, from the charged ledger §4.1 and §5.1:

- Target branch `B=B1 union B2`, incidence tree T2: the two components meet at one affine point `p`.
- Both components `A1`-normalized, one analytic place at infinity, and both places occupy the unique set-theoretic infinite point of `A_F` (Chau Theorem 1 and Chau 2004 Corollary 2, as bound in the charged `S4` integration).
- Euler packet E1: `C=A1`, `Q=0`, `n4=0`, `t=1`. Orevkov leftover `3-m=1` is consumed by the unique unibranch critical parametrization, leaving leftover 0.
- One affine `(3,1)` unibranch point, taken here as an ordinary `A2` cusp of type `(2,3)` on exactly one component. Higher `A_{2p}` is recorded in §2.4 and is not enumerated.
- Exactly one `(2,2)` conductor node (`n22=1`), an ordinary two-branch node.
- Generic meridians are transpositions in `S4`. The node pairing is the charged perfect matching `(12)|(34)`.
- The hanging component supplies an extra meridian, so the promoted one-node obstruction does not apply.

Promoted interfaces, used only in their stated scope:

- One-place identity `g_3(K_infinity(B_i))=Delta_aff(B_i)` for each irreducible component separately (total-delta packet: nearby-fibre Euler plus Neumann 1989 Theorem 1, after goodness of a *knot* link at infinity, which holds for each `B_i` because `B_i` is irreducible one-place).
- Zariski--van Kampen as in the one-node and genus-ladder packets: fibre meridians, individual affine braid relations, boundary braid equal to their product, hence a meridian-preserving surjection `pi1(S3-L_infinity) ->> pi1(A2-B)`.
- Schubert cabling/genus and primeness of nontrivial cables.
- Eisenbud--Neumann splice calculus and Neumann's RPI construction for links at infinity (Neumann 1989; Neumann--Le Van Thanh 1993 for the toral assertion without regularity of the union).
- Abstract 72-packet: any ordered overlapping-transposition cusp packet together with any node perfect matching generates `S4` (`cf157e17...` §4). Used only as a local-feasibility screen.

Not used as killing theorems: Lemma 2.3 of the charged ledger; the genus-three/four irreducible closures; the one-node obstruction applied to a component of a reducible curve; `PROVISIONAL` genus-ladder conductor exclusions.

Primary topology sources: Eisenbud--Neumann, Ann. of Math. Studies 110, 1985; Neumann, Invent. Math. 98 (1989), Theorems 1 and 2(i); Neumann--Le Van Thanh, Math. Ann. 295 (1993); Neumann--Rudolph 1987 with 1988 corrigendum, used only per component; Schubert, Acta Math. 90 (1953).

Two Neumann interfaces remain distinct. Regularity of the *union* is not granted: Lemma 7.1 needs a knot, and `L_infinity(B)` has two components. That is the source of the unbounded linking direction in Lemma 2.3.

## 2. Candidate links at infinity

Write `B1` for the component that carries the `A2` cusp. The conductor node is either a self-node of `B1`, a self-node of `B2`, or an inter-component identification. The forest point `p` is never a self-singularity of either component.

**Lemma 2.1 (component delta).** For the minimal `(2,3)` cusp and one ordinary conductor node, the pair `(Delta_aff(B1), Delta_aff(B2))` is one of

```text
(1,0)  mixed node: cusp on B1, B2 smooth, node identifies a point of R1 with a point of R2;
(1,1)  self-node on B2: cusp on B1, ordinary node of B2;
(2,0)  self-node on B1: cusp and node both on B1, B2 smooth.
```

*Proof.* An ordinary node and an `A2` cusp each have delta one. Inter-component points are not singularities of either irreducible component. There is no other affine unibranch point (`PROVISIONAL` leftover 0 of E1). QED.

**Lemma 2.2 (component knots).** Each `K_i = L_infinity(B_i)` is an iterated cable of the unknot of Seifert genus `Delta_aff(B_i)`. After trivial winding-one steps are deleted, the possibilities are

```text
genus 0:  unknot;
genus 1:  T(2,+/-3);
genus 2:  T(2,+/-5) or C(2,+/-1)(T(2,+/-3)).
```

*Proof.* Each `B_i` is irreducible one-place, so a reduced equation of `B_i` has a knot as its link at infinity and is good by the corrected Neumann--Rudolph lemma. The nearby-fibre identity of the total-delta packet gives `g_3(K_i)=Delta_aff(B_i)`. Neumann's rooted construction, root valency one, makes `K_i` an iterated cable of the unknot, hence prime or unknot by Schubert. Schubert's formulas then give exactly the displayed list. Connected sums are excluded by one-place. QED.

**Lemma 2.3 (splice form, and the unbounded direction).** Chau's unique set-theoretic infinite point forces a two-arrowhead Eisenbud--Neumann diagram of two-branch type: the RPI construction starts from the one-component Hopf link and adds exactly one parallel-cable step, equivalently a (possibly trivial) shared companion with two private cabling arms. Diagrams with two separate roots are two points at infinity and are excluded.

The private cabling of each arm is bounded by Lemma 2.2. The shared torus-link parameter `T(2,2n)`, `n>=1`, is not bounded by affine delta: Bézout `I_infinity = d1 d2 - I_aff` can grow with embedding degree at infinity. This is the honest infinite direction. It is not a silent truncation.

The bounded slice licensed by the conductor/delta budget is the list of component knot types in Lemma 2.2, spliced as a two-branch algebraic link on a `T(2,2n)` core or as a two-component torus link `T(2p,2q)` with `gcd(p,q)=1` and each `T(p,q)` of genus at most two. That torus-link list is `T(2,2n)`, `T(4,+/-6)`, and `T(4,+/-10)`.

**Lemma 2.4 (colouring types are finite).** A transposition colouring of an `s`-strand braid takes values in a set of cardinality `6^s`. The Artin action of any fixed generator is a permutation of that finite set, hence has finite order. For the F1 3-braid the action of `sigma2` on `6^3` triples has order six, so `sigma2^{2n}` depends on `n` only modulo three. Stage B below imposes the ordinary mixed twist `sigma2^{+/-2}` and is therefore independent of `n` entirely. The colouring census of the unbounded linking family is a finite list of residues, of size six, not an infinite search.

The census is well below the 10,000-diagram and five-minute stop conditions. No AWS registration is required.

**Lemma 2.5 (a trefoil cannot carry the pairing).** Let `A,B` be transpositions in `S4` satisfying the trefoil relation `ABA=BAB`. Then either `A=B` or `A` and `B` overlap in one letter. They are never a disjoint pair.

*Proof.* Direct exhaustion of the thirty-six ordered pairs, recorded in the replay: six equal pairs and twenty-four overlapping pairs satisfy the relation; all six disjoint pairs fail it. Equivalently, two disjoint transpositions commute, so the relation would force `A=B`. QED.

Consequently charging `(1,1)` is empty at the group level: `B2` is a trefoil, the self-node pairing consists of two meridians of `B2`, and those meridians cannot be disjoint transpositions. This does not use a braid presentation.

**Slice not enumerated.** A higher unibranch `A_{2p}`, `p>1`, raises `Delta_aff(B1)` above the values in Lemma 2.1 while remaining a single leftover-consuming critical parametrization. That is a strictly larger knot at infinity for `B1` (genus at least two with an extra cabling step, or genus at least three). It is typed `OPEN` as a successor slice, not filled by cap or analogy. Cabling depth that does not change component genus is the winding-one family, deleted as trivial by Lemma 2.2.

## 3. Presentations

All presentations are Wirtinger presentations of closed braids, with the Zariski--van Kampen convention of the one-node packet: individual affine braid factors impose their Artin action on fibre meridians; the boundary braid is their product and imposes only the product action. A colouring of `G_aff` is a colouring of `G_infinity` that additionally satisfies the affine factors.

Artin action, same convention as the genus-ladder compiler: `sigma_i` sends `(..., x_i, x_{i+1}, ...)` to `(..., x_i x_{i+1} x_i^{-1}, x_i, ...)`. Negative generators use the inverse automorphism. A transposition colouring is a tuple of transpositions fixed by the word.

**F1, charging `(1,0)` mixed.** Three strands, two components. Word

```text
beta_F1(e1, e2, n) = sigma1^{3 e1} sigma2^{2 n e2},     e1,e2 in {+/-1}, n>=1.
```

The permutation of the closed braid has cycle type `2+1`: strands `{1,2}` close to `T(2, 3 e1)`, strand `{3}` is an unknot, linking number `n`. Generators `x,y,z` are the three strand meridians, with `x,y` meridians of `B1` and `z` a meridian of `B2`.

```text
G_infinity = < x,y,z | sigma1^{3 e1}(x,y,z)=(x,y,z),
                       sigma2^{2 n e2}(x,y,z)=(x,y,z) >.
```

Affine factors: the cusp is the individual factor `sigma1^{3 e1}` on the two `B1` strands (the `(2,3)` torus braid of an `A2` germ, equivalently the trefoil relation on `x,y` together with the third-power return). The ordinary mixed twist is `sigma2^{+/-2}`, the local relation at an ordinary two-branch point of the union. The charged pairing requires `{x or y, z} = {(12),(34)}` as images. Stage A is invariance under the product only. Stage B is invariance under each displayed factor plus the pairing.

The corresponding splice diagram has two arrowheads at a single node of the unique infinite point, one arm the `(2,3)` cable, the other arm weight one, and shared linking weight `2n`.

**F3, charging `(2,0)`.** Same 3-braid shape with the pentafoil in place of the trefoil:

```text
beta_F3(e1, e2, n) = sigma1^{5 e1} sigma2^{2 n e2}.
```

Strands `{1,2}` close to `T(2, 5 e1)`, strand `{3}` is an unknot. Affine cusp/node both live on the two `B1` meridians.

**Satellite `(2,0)`.** The 4-braid `C(2, m)(T(2, c))` of the genus-ladder compiler, `c in {+/-3}`, `m in {+/-1}`, union an unknot as a fifth strand with mixed crossings `sigma4^{2n}`:

```text
beta_C21 = Cab_2(sigma1^c) sigma1^{m - 2c}  sigma4^{2n}.
```

**T(4, +/-6), charging `(1,1)` control.** Four-strand torus braid `(sigma1 sigma2 sigma3)^{+/-6}`. Two components, each a trefoil. Wirtinger on four meridians, product relation only at stage A; stage B asks for an overlapping pair on one component's two strands and a disjoint pair on the other's.

**T(2, 2n) core.** Two-strand braid `sigma1^{2n}`. Two unknots. Two meridians. Included as a control: two transpositions never generate `S4`.

**T(4, +/-10).** Two pentafoils. Overfills Lemma 2.1 (would need delta `(2,2)`). Included as a control; stage A is already empty.

## 4. Colouring

Direct enumeration on at most five strands. The `V4 -> S4 -> S3` split of the genus-ladder census is used as an independent count on the surviving 3-braid: each transposition maps to a transposition of `S3`, Fox 3-colourings of the closed braid are the linear quotient, and transposition lifts are the two-element fibres. The Fox/lift count of labelled full-`S4` colourings of `F1` at `n=1` equals the direct count 24.

Stage A: closed-braid transposition colourings whose generated subgroup is all of `S4`. This is a necessary condition, because `G_infinity` surjects onto `G_aff`.

Stage B, used on F1 and as a control on `T(4,6)`: Stage A, plus the individual cusp factor, plus the ordinary mixed twist where present, plus the charged pairing `(12)|(34)` at the node. For F1 the node is mixed, so one `B1` strand colour and the `B2` colour form that pairing. For `T(4,6)` the node would be a self-node, so the two strands of one component would form the pairing and the two strands of the other an overlapping cusp packet.

Lemma 2.5 already kills `(1,1)` without a braid. The `T(4,6)` control confirms it: 72 labelled stage-A `S4` colourings, zero with cusp packet on one component and pairing on the other.

Two transpositions generate a subgroup of order in `{2,4,6}`, never 24. Every 2-strand diagram dies at stage A.

## 5. Verdict per diagram

All counts are labelled: every strand is assigned a transposition, with no conjugacy quotient, except that the node pairing is fixed to `(12)|(34)` at stage B.

| family | charging | licensed? | stage A `S4` | stage B charged `S4` | verdict |
|---|---|---|---|---|---|
| `T(2,2n)`, `n=1,2,3,4` | none (both unknots) | no | 0 | — | empty |
| `F1` `sigma1^{+/-3} sigma2^{+/-2n}`, `n>=1` | `(1,0)` mixed | yes | 24 (`n not≡0 mod 3`) or 72 (`n≡0 mod 3`) | **8**, all signs, all residues | **colourable** |
| `T(4,+/-6)` | `(1,1)` | yes | 72 | 0 cusp-plus-pairing | empty |
| `F3` `sigma1^{+/-5} sigma2^{+/-2n}` | `(2,0)` | yes | 0 | — | empty |
| `C(2,+/-1)(T(2,+/-3)) union unknot` | `(2,0)` | yes | 0 | — | empty |
| `T(4,+/-10)` | overfill `(2,2)` | no | 0 | — | empty |

F1 stage B is independent of `n`: the ordinary mixed twist `sigma2^{+/-2}` is imposed, and `sigma2` has order six on triples, so every residue is checked and the charged count is constantly eight. Explicit witness, strands `(x,y,z)`:

```text
(13), (12), (34).
```

The pair `(13),(12)` overlaps and generates `S3` on `{1,2,3}` (cusp packet, fibre type `(3,1)` with letter 4 free). The pair `(12),(34)` is the charged node matching. The three transpositions generate `S4`. This is one of the 72 abstract local packets of `cf157e17...` §4, now realized as a closed-braid colouring of the two-component link at infinity with the affine factors.

F1 at `n=0` is the split link trefoil disjoint union unknot, linking zero, two points at infinity, forbidden by Chau. It is not a row of the census. Its 72 labelled `S4` colourings are the abstract 72-packet with no splice coupling; the mutation below does not treat them as legal.

Geometric model of the colourable family, not an existence claim: a cuspidal cubic union a line through the same infinite point, meeting at two affine points, one of which is the forest point `p` and one of which is the mixed conductor node. Bézout on degrees `3` and `1` gives `I_aff+I_infinity=3`, compatible with `I_aff=2` and `I_infinity=1`, i.e. the residue `n=1`. Higher `n` are the same knot types with more contact at infinity, colourable for the same group-theoretic reason.

## 6. Replay

The script `ops/block_descent_a1_rank4_r1_splice_coloring_replay.py` is a pure-stdlib enumerator. It does not import a CAS, does not touch the network, and contains no `assert`. It recomputes Lemma 2.5, the two-transposition order screen, closed-braid colourings of every licensed family, the F1 stage-B charged count on all six residues and all four signs, the Fox/V4 lift cross-check on `F1` at `n=1`, and the `T(4,+/-6)` cusp-plus-pairing control.

Ordinary, `-O`, and `-OO` executions are byte-identical, with

```text
stdout SHA-256:
36d2d33f677590807b9e6c301e5ae5312abf5fb08bbd3746e02cb7a8bfda4d1a
payload_sha256=27c8b12a4000a8b83100a4da65bc3d1bc02ec55dbda5ff6061806cad82d80762
status=PASS-RANK4-R1-SPLICE-COLORING
```

Documented mutation, required to exit nonzero:

```text
--mutate-kill-trefoil-unknot     demand that every F1 charged colouring is empty
```

The mutation fails with `FAIL:mutation rejected: F1 trefoil-unknot is colourable`. This is the required old-pass/new-fail control: the unmutated census reports eight charged `S4` colourings on F1, and the mutation asks for zero.

What the replay does not prove: Chau's unique infinite point, the one-place genus identity, goodness of a two-component link at infinity, Zariski--van Kampen, Schubert primeness, or existence of an algebraic curve or cover realizing F1.

## 7. Firewalls

- Flag, place, and series remain distinct: infinite places are Chau places of components, not cv flags, and not cover series of `pi`.
- No exit-price assertion is made. Promoted prices are consumed without a `charge_basis` line.
- `REPRESENTATIVE` diagrams (F1, F3, `T(4,6)`, the satellite 5-braids) are the complete list of two-branch algebraic links whose component knots are the iterated cables of Lemma 2.2, not a sample of a larger knot-type family. The infinite family is the linking number `n`, named as such, and collapsed to six colouring residues by Lemma 2.4.
- Floor versus attainment: `m<=3` and leftover 0 are the charged ledger's Orevkov bounds, labelled `PROVISIONAL`. Equality `I_aff=2`, `I_infinity=1` on the cubic-plus-line model is Bézout on those degrees, not a claim that every F1 residue is attained by an embedded pair.
- Higher `A_{2p}` is typed `OPEN`. If the leftover-zero reading that forbids a second unibranch point is granted but a single higher cusp is allowed, the safe replacement is a genus-`p` splice census, not a cap that the `(2,3)` slice is the whole of R1.
- Colourable means a transposition representation of the presented group. It does not produce a polynomial parametrization, a finite cover, or a Keller first leg.

Maximum safe statement: *for `PROVISIONAL` row R1 at `n22=1` with the minimal `(2,3)` cusp, the `(1,1)` and `(2,0)` chargings have no full-`S4` transposition colouring compatible with the charged pairing, while the mixed `(1,0)` charging of the two-component link trefoil union unknot has eight labelled colourings for every linking residue, with witness `(13),(12),(34)`. This does not close R1, does not realize a curve, and is not JC2.*

<!-- BODY-END -->
