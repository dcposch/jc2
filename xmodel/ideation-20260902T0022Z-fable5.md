# Blind full-portfolio ideation — round 20260902T0022Z — fable5

Packet hash verified:
`df7df824c39e3b9a2eeefc398f813e9b99aa11268ac98ff6b4c8fc26cd9a6c2c`.
Blind: this report cites only the sealed packet and banked repository
reports; no round-20260902T0022Z lane material was read.

## 1. Disposition vector (packet-named avenues)

Basis: the packet's six state-delta lanes and open fronts. The 46-row master
inventory carries over from round 20260831T1033Z unchanged except where these
rows touch it (rows 25/26/27 absorb the monodromy-side raises; row 46 holds).

| # | Avenue (packet ref) | Disp | Reason for change |
|--:|---|---|---|
| 1 | N=4 literature chain — Domrina I/II custody, mu2 Grok review in flight (delta 1) | unchanged | Await the review; no further custody spend per mission posture. Card C converts the verified machinery from a trust liability into an attack instrument. |
| 2 | N=4 campaign chain — (8,6,9) rep+curve, (9,6,4) six-node, (9,6,2) BM-factorisation (delta 2) | raise | Closest-to-closure front. The block-reading ZERO-survivor result makes the running 6^9 convention-free check the highest-information pending bit anywhere: it decides whether the strongest CE substrate carries any `phi` at all. |
| 3 | REP-96 §7 fork — BM-FACT / SOURCE-IS-C2 / MPRIME-COMPANION (delta 3) | raise | Both signs of the conjecture route through it. §6/card B add a mechanical necessary-condition layer between R1 and R2 that neither the fork report nor the flagship charges name. |
| 4 | MPRIME-ALLN-H2 flagship (delta 6, Path 1) | unchanged | Launched. Augmentation in §3: the (7.1) cancellation shows the natural-action identity is too coarse at reducible profiles; the subgroup system is the repair candidate. |
| 5 | COMPANION-CURVE-ALLN flagship (delta 6, Path 2) | unchanged | Launched. Instrument gap: its charged list (Bezout / genus-degree / log-Chern / BMY / Zaidenberg-Lin) omits the freshly repaired Domrina lattice machinery (DET-LINF + Lemma 2.12); card C supplies it. |
| 6 | One-cusp A2 horn — OPEN[A2-CELL-32] (delta 6) | unchanged | Bounded, orthogonal; two sections already closed by degree termination. |
| 7 | N=5 census (delta 6) | raise | The Zoladek Lemma 4.10 gap (delta 4) makes N=5 the sound literature frontier, and the pipeline is proven end-to-end on a real curve. Sequencing redesign in §4(d). |
| 8 | Primitive monodromy front (delta 6) | raise | `reducible-all-n-r2-opus5-20260901.md:536` reverses the old (S3) sign: block systems are a live descent at N>=5, so imprimitivity is load-bearing for any all-N induction; shares the recognize-C^2 subproblem with SOURCE-IS-C2 (§4a) and is under-resourced for that role. |
| 9 | All-degree degree-monotone invariant (delta 6) | unchanged | Goal unchanged; §3 supplies the first concrete candidate family (the Burnside chi_c vector). |
| 10 | Instruments — msolveio+qqideal, SIROCCO+ZvK+S_4 pipeline, oracle window (delta 5) | unchanged | Continue; prioritize the PARAM/point-extraction release — it gates the D_2 decision job (Path-2 item 3). |

Net: four raises (2, 3, 7, 8), six unchanged, no lowers, no reopens.

## 2. Bottleneck rerank

**Proof bottlenecks, ranked:**

1. **The BM-factorisation conventions** — OPEN[BMFACT-BASEPOINT],
   OPEN[BMFACT-STRAND-VS-BLOCK], plus the running 6^9 check. A
   convention-robust ZERO closes the (9,6,2) representation level; with
   (8,6,3) dead and the two curve jobs running, campaign-side N=4 closure
   is then within reach. Cheapest, highest-leverage, already in flight.
2. **All-N non-nodal (M') survivor classification** (MPRIME item 2). Risk:
   the survivor family is infinite — `reducible-all-n-opus5-20260901.md`
   proves there is no uniform finite survivor list, and NO-DEG-CAP bars a
   numeric cap — so a structural re-coupling mechanism is needed, not more
   enumeration. §3 is my candidate.
3. **Reducible-branch companion pressure** (COMPANION items 1-2). (RC2)
   gives `b=1` only at N=4,5; `b=2` opens at N=6 and core counts grow like
   partitions of N-2. Structural kill or bust; the only binding identity so
   far, (7.1), constrains the companion alone.
4. **Absent degree-monotone invariant** — no induction handle across N;
   §3's Burnside vector is the first candidate with degree-independent
   anchor rows.
5. **Imprimitive/block-system descent at N>=5** — needs an
   intermediate-cover identification lemma; shares the C^2-recognition gap
   with SOURCE-IS-C2 (§4a). Nobody owns this lemma.
6. **Foundation trust residue** — mu2 PROVISIONAL until the Grok review
   lands; five structure packages (F1)/(F2)/(S1)/(S2)/(S4) behind
   SOUND-AFTER-REPAIRS. Bounded per mission posture; escalate only if the
   review or card C's second branch localizes a load-bearing failure.

**Disproof bottlenecks, ranked:**

1. **The same BMFACT bit** — no surviving `phi`, no CE seed on (9,6,2).
2. **OPEN[REP-96-SOURCE-IS-C2]** — the hard geometric step
   (`rep-96-inner-opus5-20260901.md:643-652`). Card B cheapens it by
   filtering data that fail necessary conditions (H_1, chi_c, local links)
   before any construction attempt is priced.
3. **The D_2 existence decision** — blocked on Path-2 item 3 instantiation
   plus the qqideal PARAM release; the forced companion is the missing half
   of the (9,6,2) substrate.
4. **The running curve jobs** — (8,6,9) at its named global input `c_2(T)`;
   (9,6,4) six-node (which additionally dies to a YES on
   OPEN[NA-R1-SHARPNESS-IRREDUCIBLE]).
5. **N=5 census as substrate space** — after the §4(d) reorder.

Packet statement check: I find no wrong statement in the packet. One typing
caution it invites (§4c): the GGV gcd bound in delta 4 is about the map's
coordinate total degrees and must not be evaluated against the (9,6)
branch-curve parametrization degrees.

## 3. New avenue: BURNSIDE-CHI — the full subgroup-lattice chi_c system

**Mechanism.** For a hypothetical degree-N Keller counterexample with
monodromy `G <= S_N`, let `X^` be the normalization of the target `C^2` in
the Galois closure of the function-field extension. Every subgroup `H <= G`
yields an intermediate normal affine surface `Y_H = X^/H`, finite (hence
proper) over the target. Two rows are pinned: `Y_G` is the target `C^2`
(`chi_c = 1`), and `Y_{H_1}` (`H_1` a point stabilizer) is the finite hull of
the source — the source `C^2` sits inside it as the complement of the
boundary curve assembled from the `W_i` escaping sheets, so
`chi_c(Y_{H_1}) = 1 + chi_c(C_b)` with the sheet-location bookkeeping typed
per the SHEET-GATE correction (consume the typed `a^{(i)} = N - W_i` and the
`a_p` census; never `#Fix`).

A nontrivial deck transformation acts freely on the étale locus, so each
fixed locus `X^g` (`g != 1`) is concentrated over the branch strata, and
`chi_c(X^g)` is an integer assembled from the same local census (M')
consumes: cycle types at generic points, `a_p` cluster data at singular
points, local data at infinity. The standard quotient formula
`chi_c(X^/H) = (1/|H|) * sum_{h in H} chi_c(X^h)` then determines every
intermediate `chi_c` from one class-function vector `(chi_c(X^g))_g`. The
constraint system:

- (i) the two pinned rows above;
- (ii) integrality of every row (the averages must be integers);
- (iii) independent recomputation on rows with autonomous geometry: the
  `sgn`-row is the double cover of the target branched over the odd-meridian
  part of the branch configuration, computable from the curve alone; the
  `S_3`-resolvent row is exactly the TB-GERM triple-cover object already in
  the promoted toolset.

That is one identity per subgroup class instead of the single natural-action
pair — at N=4, eleven rows of `S_4` instead of two.

**Why now, and why this is not (M) redux.** The fork computation
(`rep-96-inner-opus5-20260901.md:688-708`) shows the natural-action identity
COLLAPSES at the N=4 reducible profile to (7.1) `chi_2 + sigma_2 = 1`, with
the branched component's node count `s_1` cancelling identically: the natural
permutation character is too coarse to see `s_1`. The subgroup rows weight
the same strata by different class functions (fixed-coset counts on `G/H`),
so the cancellation cannot persist across the full table unless the strata
data satisfy genuinely new integer relations — and each such relation is a
new gate. The 20260831 (M) failure mode (sheet location) is typed away by
construction: `X^` and all `Y_H` are finite covers, so no sheet escapes; the
source enters only through the one pinned open-complement row, where the
`a`-vs-`#Fix` bookkeeping appears once, explicitly.

**General-N payoff.** The vector `(chi_c(X^g))_g` and its table-of-marks
image is a candidate for the missing degree-monotone invariant: the table
grows with N, while the two anchor rows are degree-independent. Whether
monotonicity holds is card A's question, not an assertion. Novelty check
performed: "Burnside"/"table of marks" have zero hits in the banked corpus;
the `S_3` resolvent and TB-GERM triple cover are single rows of this table
used in isolation; `reducible-all-n-r2` names block systems as a live
descent but builds no chi_c system on them.

## 4. New cross-connections

**(a) SOURCE-IS-C2 x primitive-monodromy front share one unowned lemma.**
Both reduce to: recognize `C^2` (or reject it) among normal surfaces finite
over `C^2`, given only cover data. The r2 correction makes block systems "a
live descent" at N>=5 — but the descent target is an intermediate normal
surface, exactly the object OPEN[REP-96-SOURCE-IS-C2] cannot identify.
Neither flagship charge names this shared dependency; card B's gate is the
computable half of it (necessary conditions), and a positive identification
lemma (Ramanujam-style: smooth + acyclic + simply connected at infinity)
would serve both fronts at once.

**(b) The repaired Domrina II machinery x the campaign's own N=4 residual.**
The campaign now owns a replayed, repaired N=4 proof (DET-LINF banked
unconditional, `domrina-gap-repair-opus5-20260901.md:141,466`, review
CONFIRMED) AND an explicit surviving N=4 configuration ((9,6,2) plus the
(7.1)-forced companion). Nobody has instantiated the verified literature
proof on the concrete campaign residual. Running the former on the latter
either kills the substrate a third way or localizes exactly which structure
package is load-bearing — converting diffuse five-package trust into one
named question. Formalized as card C.

**(c) GGV gcd bound x census pre-filters, with a typing firewall.** Delta 4's
"gcd of total degrees >= 16, and != 2p" applies to the map's coordinate
degrees `(deg P, deg Q)`, not to branch-curve parametrization degrees; it
must NOT be consumed against (9,6) (gcd 3 there means nothing —
flag/place/series discipline). Where it can bite and is currently consumed
nowhere: any lane carrying map-degree bookkeeping — companion existence
pressure via Newton data at infinity, and N=5 census rows that pin
`(deg P, deg Q)` — inherits a strong integer pre-filter. Carry the typing
with the filter.

**(d) BMFACT experience x N=5 pipeline ordering.** At (9,6,2) the expensive
step (curve realization + SIROCCO) preceded the representation-level screen;
the block reading then found zero survivors. Two of the fork's structural
pins (the eight-tangency spanning tree; the `V_4*tau` pin on `Pi`,
`rep-96-inner-opus5-20260901.md:618-635`) were derived from the census,
realization-free. Reorder N=5: run census-level fixed-tuple / Hurwitz
screens (6^k-style, both conventions) before realizing any curve; realize
only screen-survivors. Same instruments, strictly cheaper expected path.

## 5. Strongest proof attack / strongest counterexample attack

**Strongest proof attack.** The two launched flagships stand; the strongest
marginal addition is BURNSIDE-CHI at the reducible profiles. Reason: (7.1)
is a proof-side alarm — the reducible branch's only binding identity
constrains the companion alone, and since there is no uniform finite
survivor list at growing N, natural-action pressure alone plausibly never
closes that branch. The eleven-row system is the cheapest candidate source
of the missing relations (it re-couples `s_1` and the source-side census
through the subgroup rows). Card C is the N=4-specific complement: kill the
one concrete residual configuration with already-verified machinery, so the
all-N lanes inherit a fully closed base case.

**Strongest counterexample attack.** Unchanged in shape, sharpened in order:
(1) land the 6^9 convention-free check and resolve the two BMFACT convention
OPENs — if ZERO survives conventions, (9,6,2) is dead as a seed and CE
effort moves to (9,6,4)/(8,6,9) and the N=5 space; (2) if survivors exist,
run card B's gate (H_1 of the source candidate zero; chi_c = 1; all local
links S^3) on each surviving `phi`; (3) only for gate-passers, decide D_2
(the Path-2 item-3 qqideal job), then attempt the genuine SOURCE-IS-C2
construction — invariant-ring presentation of `Y`, then two-coordinate
recognition. Every stage is finite and every failure is a permanent kill,
so the CE lane self-terminates into proof-side value instead of stalling on
the hard geometric step.

## 6. Software acceleration / decisive experiment: COVER-INVARIANTS

One tool, three gates, Sage/GAP, bounded and deterministic:

- **Input:** a braid factorization of a realized curve (SIROCCO output), a
  permutation datum `phi` (tuple), and the typed weight/sheet-location data
  (`W_i`, `a_p` census).
- **Output:** (i) ZvK presentation of `pi_1(C^2 - D)`; Reidemeister-Schreier
  for the index-N subgroup `phi^{-1}(Stab(1))`; abelianization with filling
  relations added at affine sheets only — H_1 of the source candidate;
  (ii) chi_c of the source candidate by strata assembly; (iii) local link
  certificates over each singular point (plumbing/splice presentation of the
  local cover, S^3 recognition), so Mumford's criterion decides local
  smoothness; (iv) optionally the full §3 Burnside table from the same
  census.
- **Controls, mandatory:** positive — a known cyclic double cover branched
  over a nodal cubic, H_1 and chi_c reproduced against hand computation;
  negative — a single-transposition mutation of `phi` must change the claim
  digest; fail-closed per §7.
- **Decisiveness:** for every BMFACT survivor it either kills the datum or
  upgrades it to a Ramanujam-open candidate with only
  simple-connectivity-at-infinity left — the exact interface where the
  splice/DET-LINF machinery applies. Reusable unchanged at N=5 and for the
  §4(a) primitivity descent; if the 6^9 check returns ZERO, it retargets as
  the §4(d) pre-realization screen, so neither branch wastes it.

## 7. Campaign-systems check — UPGRADE: FAIL-CLOSED-LINT

Three independent banked instances of the same fail-open class:

1. `bd-a2-d3-sectioned-two-support-split-control-coordinator-integration-sol56-20260830.md:279`
   — replay §6 checks are bare `assert`s that vanish under `python3 -O`,
   so deliberately corrupted inputs pass;
2. the SECTIONED-OUTPUT v1 review verdict REPAIR_REQUIRED for a fail-open
   leak;
3. packet delta 5, CAS footgun #11 — conda-forge sage scripts with no
   `__main__` execute nothing and exit 0, the purest fail-open.

The selected SEMANTIC-REPLAY/v1 trial (round-1033 synthesis §4) tests
generator/witness/mutation semantics; none of these three holes is in its
scope, so this is complementary, not duplicate.

**Smallest implementation** (launcher-side): (a) lint rejecting bare
`assert` in replay/verifier scripts (require a raise-always helper); (b) one
extra replay mode running each verifier under `python3 -O` and requiring
verdict identity with the normal mode; (c) an execution sentinel every
sage/python entry script must print and the harness must see (catches
footgun #11 mechanically).

**Smallest test:** two banked fixtures — the BD-A2 §6 replay must FAIL the
gate; the promoted conductor-census replay must PASS. Zero new mathematics;
closes a class with three recorded instances.

## 8. Idea cards

**Card A — BURNSIDE-CHI (§3).**

- Claim under test: the full subgroup-lattice chi_c system yields at least
  one integer relation on the N=4 reducible residual beyond (7.1); and
  symbolically at general N, the system's rank on the cage's residual
  classes exceeds the natural-action pair's.
- Dependencies: `rep-96-inner-opus5-20260901.md` §7 R4 profile data;
  `reducible-all-n-opus5-20260901.md` cage rows as corrected by r2; the
  quotient-chi_c formula and the free-action-on-étale-locus lemma (standard;
  literature-pinned at execution); sheet-location typing per SHEET-GATE —
  the 20260831 (M) failure is the standing negative control.
- Cheapest discriminator: the eleven-row `S_4` table at the pinned N=4
  profile (core (2,1,0), W=(1,2), `D_1` = the realized (9,6,2) curve, `D_2`
  carrying unknowns `(chi_2, sigma_2, j)`). Exact integer arithmetic, desk
  or one Sage script.
- Outcomes: a new relation on `(s_1, sigma_2, j)` — immediate Path-2
  consumable, and the general-N system becomes a flagship augmentation; a
  provable collapse to (7.1) — mechanism retired permanently with the
  degeneracy proof, closing a direction that keeps resurfacing ((M), (E),
  (M'), TB-GERM are all rows of this table); partial — keep exactly the
  non-degenerate rows as named gates.
- Stop condition: one N=4 evaluation plus one general-N rank statement on
  the cage's residual classes; no open-ended generalization hunt.
- Expected information gain: high in every branch — either the first new
  all-N identity family since (M'), or a permanent closure of the "more
  Euler identities" direction.

**Card B — COVER-TOPOLOGY-GATE (§6 tool run as a lane).**

- Claim under test: every BMFACT-surviving `phi` on (9,6,2) fails at least
  one of — H_1(source candidate) = 0; chi_c(source candidate) = 1; all
  local links S^3.
- Dependencies: BMFACT survivors (the 6^9 check is running; the lane fires
  only if the survivor set is nonempty, else the tool retargets per §6);
  SIROCCO factorization (banked, census-confirmed); the strand-vs-block and
  basepoint conventions resolved first — until then the gate runs both
  conventions and labels each run; the typed `W_i`/`a_p` profile data.
- Cheapest discriminator: H_1 alone (Reidemeister-Schreier plus Smith normal
  form; minutes per datum).
- Outcomes: all survivors fail — (9,6,2) dead as a CE seed at the
  representation+topology level without touching SOURCE-IS-C2; some pass —
  the strongest CE candidate the campaign has ever had, handed to the D_2
  job and the invariant-ring construction with pi_1 at infinity the only
  remaining test; either way the output feeds §4(a)'s shared lemma.
- Stop condition: all six pinned classes (144 tuples) processed under both
  conventions; no extension to unrealized curves.
- Expected information gain: decisive per survivor; bounded cost; every
  verdict permanent.

**Card C — DOMRINA-INSTANTIATE (§4b).**

- Claim under test: the repaired Domrina II chain, instantiated on the
  campaign residual (core (2,1,0), W=(1,2), `D_1` = (9,6,2)), kills the
  configuration, and the kill consumes only already-repaired steps (R1/R2,
  DET-LINF, Lemma 2.12) plus explicitly named package calls.
- Dependencies: `domrina-gap-repair-opus5-20260901.md` (R1/R2 and DET-LINF
  CONFIRMED by `domrina-repair-review-gpt55-20260901.md`); custody
  `0be24c5c`; the mu2 track is PROVISIONAL — if the kill routes through
  mu2, the verdict inherits that flag, typed, until the Grok review lands.
- Cheapest discriminator: a desk replay of her §§5-7 walk on the concrete
  lattice data; first fork is whether the (9,6,2) infinity data is forced
  into `Q1 u Q2` by Lemma 2.12 + DET-LINF.
- Outcomes: clean kill via repaired steps only — a third independent
  closure of the substrate, freeing the CE lane to (9,6,4)/(8,6,9) and
  validating the two chains against each other; kill routes through a
  package (F*/S*) — that single package becomes the sharpest remaining
  verification target (verify one, not five); no kill — genuine tension
  between the received proof and a live substrate: escalate to DC
  immediately, since either her proof has another gap or the substrate
  hides a contradiction, and both are major.
- Stop condition: one desk pass; no re-verification of already-replayed
  sections.
- Expected information gain: high in all three branches; the third is the
  cheapest possible detector of a residual foundation flaw, obtained by
  doing attack work rather than custody work.

## 9. Lane dispositions (continue / redesign / stop)

- **MPRIME-ALLN-H2 (Path 1): continue** unchanged; consume card A's output
  when it lands.
- **COMPANION-CURVE-ALLN (Path 2): continue**; one-line charge addendum on
  landing — check the DET-LINF/Lemma-2.12 lattice route (card C) and the
  §4(c) map-degree filter against its survivor characterization.
- **(8,6,9) corrected curve job and its `c_2(T)` input; (9,6,4) six-node
  job: continue.**
- **6^9 SAGE-native convention-free check + the two BMFACT convention
  OPENs: continue, top priority** — everything CE-side sequences behind
  this bit.
- **mu2 Grok review: continue**; the PROVISIONAL flag holds until it lands.
- **One-cusp A2 horn (OPEN[A2-CELL-32]): continue, bounded.**
- **N=5 census: redesign** per §4(d) — census-level screens before curve
  realization — then launch when a seat frees; do not launch in the old
  order.
- **Domrina package verification beyond the in-flight review: stop** at
  current depth, unless card C's second branch names a load-bearing package
  (then verify exactly that one).
- **Oracle window / msolveio+qqideal: continue**; prioritize the PARAM/point
  extraction release (it gates the D_2 decision job).

Logged deviation: body ~21.8KB against the 12-20KB target; the overrun is
the ten-row disposition table and the three cards' outcome branches, kept
per the submission contract rather than compressed away.

<!-- BODY-END -->
