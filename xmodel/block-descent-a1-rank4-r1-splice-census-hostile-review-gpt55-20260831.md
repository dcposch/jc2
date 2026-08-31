# Hostile review: R1 splice-colouring census

Charged producer: Grok 4.6  
Review date: 2026-08-31  
Frozen inputs: the four files in `/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.kqzLHh/inputs`

## 1. Hash gate and scope

I first created this report shell, then recomputed the four required SHA-256 hashes before reading the mathematical content. They match exactly:

```text
5d5b3d1fc1b2f7f57a59ea62c9409bec24e81e80e1e529b47612e5302aae4c11  block-descent-a1-rank4-r1-splice-coloring-census-grok46-20260831.md
ebafe10307564b12a17c4875bb8467a912008f46518078afe5c57e0ae1091ea7  block_descent_a1_rank4_r1_splice_coloring_replay.py
513fe4c022b3a84531c0e42e4cc61a1c9cf2732dde4a5931cb6f8384e166ad4d  block-descent-a1-rank4-reducible-component-tree-ledger-grok46-20260831.md
ed0d288bec800bc1cfb59506a60ac76243aa47378692330f54f9d0860d754fb9  block-descent-a1-rank4-reducible-component-tree-ledger-hostile-review-sol56-20260831.md
```

I did not inspect `jc2-lean`, did not run Singular/msolve/CAS, and did not edit any charged or canonical ledger. Computation was limited to the named frozen Python replay and desk arithmetic.

## 2. Dependency audit

The census is not allowed to inherit the parent ledger as a black box, because the prior hostile review refuted its 16-row bookkeeping. The exact dependencies are:

| census dependency | cited use | ledger-review status | verdict |
|---|---|---|---|
| `B=B1 union B2`, source tree T2, all components `T211`, row R1 finite stratum | census lines 21-31, parent lines 149-167 | R1 lies in the finite-`T31` Euler stratum; that stratum was confirmed. It is not one of the refuted split rows. | **CONFIRMED**, as a selected row, not as evidence for the parent 16-row ledger |
| E1 packet `C=A1,Q=0,n4=0,t=1` | census lines 27-28, 51-59 | finite-`T31` Euler arithmetic was confirmed. | **CONFIRMED** |
| `m<=3` and leftover budget `3-m`, hence R1 leftover one before the cusp | parent lines 90-93, 116-117; prior review lines 131-150 | rests on untyped dicritical hypotheses (D1)--(D4). | **GAP** |
| E1's finite `(3,1)` value is a unibranch critical parametrization value consuming that leftover | census lines 27-29, 59; prior review lines 152-156 | explicitly identified as an unproved premise. | **GAP** |
| leftover zero after an ordinary `A2` cusp, hence no other affine unibranch singularity and only the three delta chargings | census lines 51-59 | depends on the two preceding gaps. | **GAP** |
| each `B_i` is `A1`-normalised and one-place; all infinite places share Chau's set-theoretic point | census lines 25-26, parent lines 15-18 | promoted rank-four/Chau interface; not refuted by the ledger review. | **CONFIRMED** |
| `S22` cannot lie on `T31`; R1 conductor support is legal on `T211` | parent lines 20, 56-63; prior review lines 198-204 | confirmed local rule. | **CONFIRMED** |
| the single `S22` point is an ordinary immersed conductor node with zero component delta except for self-node delta | census lines 29, 51-59 | zero Orevkov charge was confirmed only for distinct immersed parameter values; immersion is not pinned. | **GAP** |
| fixed global node pairing `(12)|(34)` on the displayed strand meridians | census lines 30, 108, 138; prior review lines 204-206 | the pair-transport issue applies. One node can be normalized up to global conjugacy only after the ZVK paths are fixed. | **GAP** |
| parent ledger's split rows, 16-row count, and absence of connected mixed `T31/T211` rows | not needed for the R1 finite-row arithmetic | refuted. | **NOT CONSUMED** |

Thus no F1 arithmetic conclusion is invalid merely because it rests on the refuted split rows. The damage is different: the census is only a conditional minimal-`A2`, `n22=1`, fixed-pairing splice calculation. It is not a licensed exhaustive census of row R1.

## 3. Lemma 2.1: delta chargings

**Verdict: CONFIRMED conditionally; licensed-slice claim GAP.** If the affine singularities are exactly one ordinary `A2` cusp on `B1` and one ordinary conductor node, the displayed component deltas are correct. The cusp contributes delta one to `B1`; a self-node contributes delta one to the component on which it lies; an inter-component ordinary node is not a singularity of either irreducible component. This gives `(1,0)`, `(1,1)`, `(2,0)`.

The proof's final sentence, "there is no other affine unibranch point", is not licensed. It requires both the dicritical leftover bound and the premise that the E1 finite `(3,1)` value is a unibranch critical value. The prior review marked both as gaps. Therefore the census may study the minimal cusp sub-slice, but it cannot say the conductor/delta budget has exhausted R1. Higher `A_{2p}` and non-unibranch realizations of the finite `(3,1)` value remain outside the proved slice.

## 4. Lemma 2.2: component knots

**Verdict: CONFIRMED under the promoted one-place genus interface and the conditional deltas.** For an irreducible one-place rational component, the promoted interface gives `g_3(K_i)=Delta_aff(B_i)`. Algebraic one-place links at infinity are iterated cables of the unknot. After winding-one steps are deleted, Schubert's genus formula gives:

```text
g=0: unknot
g=1: T(2,+/-3)
g=2: T(2,+/-5) or C(2,+/-1)(T(2,+/-3))
```

The enumeration is tight: a nontrivial cable of a genus-one companion has genus `2` only for winding `2` and longitudinal parameter `+/-1`; higher winding or `|q|>1` overfills. This does not repair Lemma 2.1's gap: if the affine delta packet is larger or not exhausted, the knot list is no longer complete for R1.

## 5. Lemma 2.3: splice form and unbounded linking

**Verdict: GAP for exhaustiveness; CONFIRMED only for the one-root warning.** Chau's one set-theoretic point at infinity rules out two independent infinity roots. Eisenbud-Neumann splice diagrams apply to plane-curve singularity links, so a two-branch local link at that point should be represented by one rooted two-arrowhead graph link.

The census needs more than that. It needs the full assertion that the R1 two-component link at infinity is exhausted by the listed `T(2,2n)` core plus bounded private arms, or by `T(4,+/-6)` and `T(4,+/-10)`. The packet cites Neumann 1989 and Neumann-Le Van Thanh 1993, but the advertised external interface is not proved inside the charge. A primary-source spot check confirms the danger: Neumann 1989 is stated as classifying regular affine curves via splice diagrams, and Neumann-Le Van Thanh treats the equivalence between regularity at infinity and regular toral links. Those citations do not by themselves supply an exhaustive two-component irregular-at-infinity RPI census without a local Puiseux/semigroup argument.

The unbounded direction is honestly named if read as "not bounded by affine delta or by the finite `S4` colouring computation." It is not an attainment theorem for every `n`. The weakest replacement is an explicit hypothesis: the projective closure at the unique infinite point has exactly the claimed two-arrowhead splice type, with the only unbounded parameter the mutual `T(2,2n)` linking core and no additional algebraic-link shapes of component genus at most two.

## 6. Lemma 2.5: trefoil relation

**Verdict: CONFIRMED.** Let `A,B` be transpositions. If they are disjoint, they commute, so `ABA=B` and `BAB=A`; the braid relation forces `A=B`, contradicting disjointness. If `A=B`, the relation holds. If they overlap in one letter, they are adjacent transpositions in an `S3`, and both sides equal the third transposition.

Counting ordered pairs in `S4`: six equal pairs, `6*4=24` overlapping pairs, and six ordered disjoint pairs. The disjoint pairs all fail. The self-node-on-trefoil charging `(1,1)` is therefore killed independently of the braid replay and independently of the fixed matching label.

## 7. Stage-A/stage-B protocol

**Stage A verdict: CONFIRMED as a necessary screen.** The Zariski-van Kampen interface says the affine complement is obtained from the link-at-infinity group by adding individual affine braid-factor relations. Hence every affine colouring must first be a closed-braid colouring of the product boundary word. Stage A is not sufficient, and the packet correctly does not treat it as sufficient.

**Stage B factor verdict: CONFIRMED for F1, conditional on the ZVK presentation.** The `A2` cusp contributes the individual `sigma1^3` factor on the two trefoil strands. An ordinary mixed node contributes `sigma2^2` between the relevant branch meridians. Imposing these individual factors is the right affine quotient for the displayed F1 braid.

**Pairing verdict: GAP.** The packet fixes `(12)|(34)` directly on the strand colours. For a single node, a global conjugation can normalize one local perfect matching, but only after the base paths identifying local node meridians with the chosen fibre meridians are fixed. The prior pair-transport gap applies here. It does not revive the trefoil-pair kill, and it does not negate the exhibited F1 compatibility colouring; it does make the labelled count "exactly 8" a count for this chosen transported presentation rather than an invariant row count.

## 8. Verdict-table recomputation

**F1 `(1,0)` mixed: CONFIRMED conditionally.** Stage B requires `x,y` to be an overlapping trefoil pair, `y,z` to commute under the ordinary mixed twist, full `S4` generation, and one of `x,z` or `y,z` to be the charged matching `(12),(34)`.

Desk count: if the charged arm is `y`, then `(y,z)` is either `((12),(34))` or `((34),(12))`. In each case `x` has four choices overlapping `y`, and each such triple generates `S4`. That gives `8`. If the charged arm is `x`, then `x` is disjoint from `z`; the twist requires `y` commute with `z`, while the cusp requires `y` overlap `x`, which has no solution. Total: `8`. The witness `(13),(12),(34)` is valid. Reversing signs does not change fixed sets, and imposing `sigma2^2` makes the charged count independent of `n`.

**Residue collapse for F1: CONFIRMED.** On transposition pairs, one Artin generator has periods `1` on equal pairs, `2` on disjoint pairs, and `3` on overlapping pairs; hence order `6` on triples. Since Stage B fixes `sigma2^{+/-2}`, it fixes every `sigma2^{2n}`. The replay's stage-A residues `[24,24,72,24,24,72]` and charged count `8` are consistent with this.

**`T(4,+/-6)` control: CONFIRMED.** The replay gives `72` full-`S4` stage-A colourings for each sign and `0` charged cusp-plus-pairing colourings. The zero is already forced by Lemma 2.5: a trefoil component cannot supply a disjoint transposition pair.

**`T(2,2n)` core: CONFIRMED.** Two transpositions generate a subgroup of order at most `6`, never `S4`.

**F3 `T(2,+/-5)` union unknot: CONFIRMED.** For a two-strand pentafoil factor, equal transposition pairs are fixed, while overlapping and disjoint non-equal pairs are not fixed by the fifth power in the required way. Adding one unknot meridian leaves at most two transpositions, so full `S4` is impossible. The replay agrees for all six residues and signs.

**Satellite `(2,0)`: GAP as a full unbounded-family claim.** The replay checks only `linking in (1,2)` for the five-strand satellite. The same Artin-period logic says the missing residue `n % 3 == 0` is a distinct colouring problem, just as it is for F1 stage A. No desk proof in the packet rules it out. Therefore the statement "the satellite family is empty" is confirmed only for the two tested residues; as a verdict-table row for all `n`, it is unproved.

**`T(4,+/-10)`: CONFIRMED as a control, not as a licensed row.** It overfills the conditional delta packet `(2,2)` and the replay finds no full-`S4` stage-A colouring.

## 9. Replay audit

**Execution verdict: CONFIRMED.** The named frozen replay ran successfully in normal, `-O`, and `-OO` modes. All three stdout streams had SHA-256

```text
36d2d33f677590807b9e6c301e5ae5312abf5fb08bbd3746e02cb7a8bfda4d1a
```

The printed payload digest was `27c8b12a4000a8b83100a4da65bc3d1bc02ec55dbda5ff6061806cad82d80762`, with status `PASS-RANK4-R1-SPLICE-COLORING`. The mutation `--mutate-kill-trefoil-unknot` exited `1` with `FAIL:mutation rejected: F1 trefoil-unknot is colourable`.

**Semantic verdict: REFUTED AS ADVERTISED.** The script is a useful finite `S4` enumerator, but it does not verify the topological census. It hard-codes the braid families, the ZVK factor split, the chosen matching, the component-knot list, and the unbounded-direction interpretation. It does not encode Chau, Orevkov, the one-place genus identity, the two-arrowhead splice classification, or path transport at the node. It also fails to enumerate the satellite residue `n equiv 0 mod 3`. The mutation proves only that the positive F1 count is not accidentally zero; it is not a semantic mutation of the topology or dependency gaps.

## 10. Scope firewalls

**Verdict: CONFIRMED with wording discipline.** The packet correctly says colourable means compatibility of a transposition representation with the presented group, not existence of an embedded curve, finite cover, or Keller map. The cubic-plus-line paragraph is only a Bezout consistency check for the `n=1` contact pattern; it must not be read as a realized proper-block branch or cover. The higher `A_{2p}` slice is explicitly OPEN and is not filled by the minimal-cusp census.

One wording correction: "geometric model" is too strong unless immediately read as "Bezout model." The maximum safe use is consistency of intersection numbers, not curve-realization evidence for R1.

## 11. Weakest hypotheses and blast radius

The exact hypotheses under which the positive F1 result is valid are:

1. the confirmed R1 finite-E1/T2/T211 setup with two `A1`-normalised one-place components and one set-theoretic infinite point;
2. the gapped dicritical leftover package (D1)--(D4), plus the extra premise that E1's finite `(3,1)` value is a single ordinary `A2` unibranch critical value and exhausts the leftover;
3. the conductor point is an ordinary immersed `S22` node;
4. the component genus identity applies separately to each component;
5. the two-component link at infinity is exhausted by the packet's listed two-arrowhead splice forms;
6. the ZVK paths identify the charged local node matching with the displayed strand colours, after one global conjugacy.

Blast radius: Lemma 2.5, the F1 fixed-presentation count, the F3 hand kill, and the `T(4,6)` trefoil-pair kill survive. The claims that the minimal cusp slice is licensed by the ledger, that the listed splice families exhaust R1, that the labelled pairing count is intrinsic, and that the satellite `(2,0)` row is empty for every linking residue do not survive review. No conclusion should consume this packet as a closure of R1 or as an exhaustive splice census.

## 12. Best next falsification test

Add one exact replay mutation that forces the satellite family to be checked at all three linking residues modulo three, especially `n=3`, with the same fixed component braid and with an explicit charged `(2,0)` self-node condition on the cable component. The test should fail if any residue is omitted. This is desk-scale (`6^5` transposition assignments) and directly attacks the largest finite arithmetic hole in the verdict table before any heavier topology is attempted.

## 13. Per-claim verdicts

| claim | verdict | attack |
|---|---|---|
| Hash integrity and replay execution | **CONFIRMED** | hashes and stdout digest reproduce; mutation exits nonzero |
| Dependency on parent row R1 finite-E1/T2 | **CONFIRMED** | lies in confirmed finite-`T31` stratum, not in refuted split rows |
| Parent ledger licenses leftover zero | **GAP** | depends on (D1)--(D4) and unproved unibranch-critical premise |
| Lemma 2.1 delta triples | **CONFIRMED** | correct for exactly one `A2` cusp and one ordinary node |
| Lemma 2.1 as exhaustive R1 slice | **GAP** | other unibranch or non-unibranch E1 realizations are not excluded |
| Lemma 2.2 knot list | **CONFIRMED** | follows from per-component genus identity and Schubert, conditionally on the delta packet |
| Lemma 2.3 exhaustive splice list | **GAP** | cited regular/RPI literature is not enough as stated for irregular two-component union |
| Lemma 2.4 F1 residue collapse | **CONFIRMED** | Artin action order on transposition triples is six; Stage B fixes `sigma2^2` |
| Lemma 2.5 trefoil-pair obstruction | **CONFIRMED** | disjoint transpositions commute, forcing equality |
| Stage A as necessary condition | **CONFIRMED** | affine relations quotient the infinity group |
| Stage B F1 factors | **CONFIRMED** | cusp `sigma1^3` and ordinary node `sigma2^2` are the right local factors for the displayed presentation |
| Pairing normalization as intrinsic | **GAP** | transported local pair is not derived from path data |
| F1 charged count `8` | **CONFIRMED** | hand count gives eight for the fixed transported pairing; witness valid |
| `T(4,+/-6)` charged emptiness | **CONFIRMED** | replay count plus trefoil obstruction |
| F3 emptiness | **CONFIRMED** | pentafoil factor leaves no full-`S4` transposition image |
| Satellite `(2,0)` emptiness for all `n` | **GAP** | replay omits residue `n % 3 == 0` |
| Replay verifies topology/exhaustiveness | **REFUTED** | topology, pairing transport, and several family choices are hard-coded |
| Firewalls: colourable is not existence; cubic-plus-line is only Bezout; higher `A_{2p}` open | **CONFIRMED** | packet states these limitations; only wording of "geometric model" needs tightening |

<!-- BODY-END -->
