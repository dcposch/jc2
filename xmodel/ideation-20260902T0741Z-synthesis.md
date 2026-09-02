# Synthesis — full ideation round 20260902T0741Z

Coordinator: Fable 5.1. Packet 2646ac69 (frozen 07:41Z, basis 8939320b).
Trigger: DC directive ("run a full round soon; fresh eyes on every gap").
Five submissions — four blind roster lanes plus the coordinator's own,
written before any lane was read:

```text
grok46    ideation-20260902T0741Z-grok46.md                (25.0KB, sealed ~07:58Z)
opus5     ideation-20260902T0741Z-opus5.md                 (41.2KB, sealed ~08:03Z)
fable51   ideation-20260902T0741Z-fable51.md               (26.0KB, sealed ~08:06Z)
fable51c  ideation-20260902T0741Z-fable51-coordinator.md   (b905417b, 08:05Z)
sol56     ideation-20260902T0741Z-sol56.md                 (see §9)
```

Round quality: high novelty, low duplication, and — unusually — three
different submitters rejected the coordinator's framing at the same two
points (§2). The coordinator's own submission was wrong at exactly those
points and right at one other (§3); both facts are recorded.

## 1. Headline: case (A) is claimed EMPTY at every degree, twice, independently

Two producers, blind to each other, reached the same theorem by the same
mechanism read in opposite directions:

- `cusp-a-n8-gate-opus5-20260902` (a research lane, landed 08:10Z):
  THEOREM NO-CUSP-PREIMAGE (the cusp of the cone x^p = y^q has no
  preimage under F, because a preimage would be a section of the
  connected degree-N covering over a punctured ball whose local pi_1
  surjects onto the global one) and THEOREM CUSP-A-VOID (chi(E) = 1 then
  forces an A^1 component mapping non-constantly into C^*). H2-free;
  one page; also a second, representation-level chain (PERIPHERAL-RANK +
  MERIDIAN-SPAN) and a proof of CUSP-A-KAPPA.
- `ideation-…-fable51` §1.1: THEOREM CUSP-A-ALL-N — LOCAL-ISO TRANSPORT
  (an affine preimage of a point of A_F gives a trivial sheet fixed by the
  local group) plus Prop 6.1's a_{p_0} = 1 and the conical isomorphism
  pi_1(B \ A_F) = G give a fixed sheet of a transitive group, so N = 1.

These are contrapositives of each other around the single datum
a_{p_0} ∈ {0, 1}: if the cusp has a preimage the Fable-lane argument kills;
if it has none the Euler argument kills. Either way case (A) dies at every
N ≥ 2, provided (i) Lin–Zaidenberg puts A_F in the form x^p = y^q and
(ii) the weighted C^*-action makes the local complement a deformation
retract of the global one. The coordinator checked chain I by hand and
found no hole. FLAGGED by both producers: MPRIME Prop 6.1 as quoted says
a_{p_0} = 1 while NO-CUSP-PREIMAGE says 0 — the review must say which
object Prop 6.1's ledger is about.

Typing at freeze: PROVED-HERE/UNREVIEWED (two independent derivations,
both Anthropic models). Paired review launched 08:12Z, pair-don't-pick:
`cusp-a-void-review-gpt55-20260902` (line-by-line, ten mandatory checks)
and `cusp-a-void-countermodel-grok46-20260902` (hidden-assumption audit
and small-representation search). **UPDATE 08:36Z: the GPT-5.5 gate
landed (0ab02c19) and CONFIRMED every theorem** — NO-CUSP-PREIMAGE, the
cone corollary (local-to-global pi_1 is an isomorphism), CUSP-A-VOID,
(G-C) with a puncture-split repair, PERIPHERAL-RANK, MERIDIAN-SPAN,
kappa | a, CUSP-A-VOID-II, CUSP-A-KAPPA, the SMOOTH-KILL composition,
and the Prop 6.1 cross-check (an affine-fibre statement: a_p = 1 there
against a_p = 0 here is itself a direct kill, i.e. the Fable-lane route
also stands). Reviewer's PROMOTE list: case (A) empty for every N ≥ 2;
the local-transitivity lemma; PERIPHERAL-RANK; MERIDIAN-SPAN; kappa | a;
chi(E) = nu − Sigma*. DO NOT PROMOTE: any (B3) deletion. **08:52Z: the
Grok countermodel arm (c50ecca9) also passed** — every theorem SURVIVES
its hidden-assumption audit; PERIPHERAL-RANK is scoped to the cage
window F1 (2 ≤ j ≤ a ≤ N−2; explicit violators outside it); Lin–
Zaidenberg's citation corrected (Soviet Math. Dokl. 28, 1983). Both
arms passed: integration #9 binds this set.
Label: NEW (mechanism family KNOWN: covering-space sections; not in the
ledger). Now that it is CONFIRMED: THEOREM
PROFILE loses row (A) at every N; under H2 the residual below 17 is
exactly (B2) ∪ (B3); OPEN[HOMCOVER-CUSP-A-N8] and OPEN[MPRIME-CUSP-J2]
close negative at all N; composed with SMOOTH-KILL at its own typing,
"the non-properness set of a noninvertible Keller map is never
homeomorphic to C". Also to bank on confirmation: LOCAL-ISO TRANSPORT as
a standing rule (the set {p : a_p ≥ 1} and the surjectivity defect of
Loc_p → G are one datum; #cusps of E = a_{p_0}, not a) — it is a free
prefilter for every future representation census.

## 2. Headline: the A2 residual is not the (B3) horn — the packet's gaps (k)/(l) were mis-posed

Three submitters, independently:

- Grok §1.1–1.2: WRONG-OBJECT. The A2 residual is a map-germ at infinity
  (polynomials eta, s, q, r, G in C[Z]); (B3) is a representation of
  pi_1(C^2 \ A_F). RAY-KILL §6 had already said they do not compose.
  Gap (l) is WRONG-INFERENCE: four-on-five is a jet statement, the
  D-series pattern in costume.
- Opus §2(ii), §5: retire (k); OPEN[A2-U-BOUND] is the wrong target
  because RAY-KILL (C5) proves there is no Z-scaling covariance, so no
  symmetry can bound U. Replace by OPEN[A2-DEPTH-BOUND] and MECHANISM
  PARAM-U: truncate to the top k coefficients, whose count is
  U-independent and whose coefficients are polynomial in U (CELL-32's
  Euler eigenvalues are linear in the degree indices); one Groebner basis
  over Q(U) decides all but finitely many U. Decisive experiment
  DEPTH-PROFILE: at what depth k did (1,3), (1,5), (1,7), (2,6) become
  empty?
- Fable lane §1.2: THEOREM PHI-IMMERSION (PROVED-HERE/UNREVIEWED): in the
  A2 model the Jelonek set of the first map is Phi = V(A,U), its image
  C_0 = pi(Phi) is the immersed image of A^1 (E0 forces (f_0', g_0')
  coprime), so under H2 A_F = C_0 has a smooth branch through every
  point: the A2 model is PROFILE (0)/(B1), EMPTY for N ≤ 16 by
  SMOOTH-KILL / NODAL-ALL-N. The horn's "one cusp" is a pole structure at
  infinity of a map-germ, not MPRIME's affine cusp; the (B3) horn has NO
  analytic model in the campaign.

The coordinator's Card 3 (what U means) is answered: U is a map-germ
degree, a Keller degree in disguise, not a sheet datum; the coordinator's
Card 1 (ray recursion) is superseded by Opus's better-posed DEPTH-PROFILE
/ PARAM-U, and its "infinite-U family as a counterexample-level object" is
WITHDRAWN on Grok's and Opus's grounds (§5.2 of Opus: the top-of-ladder
deficit is an artefact of equations switching on at staggered depths).

Coordinator error adopted: the 07:22Z handoff and the 07:41Z packet
conflated two objects under the name "one-cusp horn". Correction: the
A2/CELL-32/RAY line is OBSTRUCTION[A-DEGREE-TWO] on a block-descent
map-germ; the (B3) horn is MPRIME's cusp + multibranch profile; neither
result transfers to the other.

Adjudication launched 08:20Z: `phi-immersion-adjudication-sol56-20260902`
(Sol, producer model of the block-descent structure report). **UPDATE
~08:45Z: landed (4820a2cf) — steps (1)–(4) CONFIRMED.** The package
"A2 exact-model identification + H2 + affine (B3) cusp" is INCONSISTENT
(GAP[EXACT-MODEL-ID]: the structure report's identification of the
block surface with the horn was provisional). Re-filing adopted: the
bare A2/CELL-32 lane is PROFILE-UNTYPED and N-UNTYPED; with H2 it is
(B1) at even N ≥ 18 only; any actual N ≤ 16 survivor is reducible-A_F.
OPEN[A2-U-BOUND] is demoted from "the horn's missing theorem" to an
untyped algebra question; the bare equations encode no cusp at all. The
(B3) horn has NO analytic model; its live instruments are the cage and
E (§3). Allocation: box01's redundant single-thread run killed; the
24-thread run continues at zero priority as finite-box evidence;
`a2-ubound` runs to its seal, then its successor charge is the BRIDGE
(m = [K(S):C(f,g)], A_pi and the components of A_F = A_pi ∪ C_0, the
residue-collision hypotheses), with O0/O1 and DEPTH-PROFILE/PARAM-U as
tools for whichever branch that selects.

**UPDATE ~08:55Z — a P0 on top of the re-filing.** `a2-ubound` sealed
(e8eb9d77) and found that the CELL-32 spec's displayed E2 omits the
term −2qE1; the coordinator recomputed [A^2]Even from the spec's own
definitions and CONFIRMED it (difference exactly −2·q·E1; E0, E1
exact). Claimed blast radius, under a different-model gate
(`a2-e2-p0-gate-gpt55`): HORN-A2's Chamber II determinant is
identically zero on the corrected system (the E1-wall is not derived),
RAY-2 is refuted, N2 loses a column, and every box01 cell EMPTY was
computed on the wrong system. Unaffected: RAY-DEP, RAY-EDGE (e ≥ 2),
C32 T1–T5. Two hostile reviews had reproduced the transcription rather
than the source — a review-process finding recorded in AUDIT.
The lane's positive results on the corrected system (O0 was never
missing, O1 is inert; DEV-FREE; a U-FREE bound deg X, deg Y ≤ 4e − 1;
a finite-U dichotomy with one named residual branch) are the
successor's starting point once the gate lands. The box01 window was
stopped. Net for the A2 line: wrong object AND wrong equation, both
caught by this round's lanes within four hours of the packet.

## 3. Headline: attack the (B3) horn through the source curve E — four proposals, one lane

Four submitters converged on E = F^{-1}(A_F), explicit at N = 4 by
THEOREM B3-N4 (k = 1: rational, five places at infinity, one A2 cusp,
smooth elsewhere), as the object nobody has attacked:

- Grok Card I: three embedding gates on E — componentwise CUSP-KILL in
  the k_odd = 0 arm; the 5-component link at infinity against the
  multiplicity-2 dicritical (splice); existence of a rational
  five-punctured plane curve with a unique A2 cusp.
- Fable lane Card C: log-Kodaira dimension and log-BMY on (A^2, E) with
  the cusp type pinned; stop if kappa-bar = −infinity.
- Opus §4.2 AVENUE ANTI-MONOTONE: the counting inequality
  a − 1 ≤ C(2a − N) and the covering cage have opposite monotonicity in
  a; tabulate both on one (N, a) grid — the only named route to a
  degree-monotone obstruction. Dependency OPEN[B3-INFINITY-RANK].
- Coordinator Card 2: the Galois closure X-hat (normalisation of the
  target plane in the Galois closure of C(x,y)/C(P,Q)) as a finite
  S_4-cover branched along A_F with quotient singularities pinned by rho;
  orbifold BMY there.

Dedup: one target (the rigid-not-empty (B3) cage at N = 4 and its all-N
mechanism), four mechanisms, zero overlap in method. All four merged into
`b3-e-geometry-opus5-20260902` (launched 08:29Z, Opus flagship; order
G-KAPPA → G-SPLICE → G-EMBED → G-ANTI, plus a reading task: name the
lemma in the checked Domrina–Orevkov chain that kills this object at
N = 4 and say whether it is N-uniform). Label: NEW as a target; mechanism
family KNOWN (row 28 reopened with data; rows 6, 27, 31 raised).

## 4. The Chau degree cap: an index failure, and a disagreement resolved by scope

Opus §3: OPEN[DEG-AF-VS-N] — ranked first by both H2 flagships, one of
which wrote "could not find it promoted anywhere" — is answered in the
form the delta-budget needs by the Chau clauses banked the same day on the
REDUCIBLE branch (COMPANION C6/C7/C8; M ≤ K; sum deg D_i ≤ max(deg P,
deg Q)): under H2, deg A_F = M·max(d,e) with one place at infinity. Opus
also raises CLAIM [D] (UNREVIEWED): at (9,6) the cap is saturated by D_1
alone, so no companion fits and OPEN[COMPANION-R0-REALISATION] is negative
at (9,6,2) by substitution.

Grok §1.4, independently: the raw bound deg A_F ≤ f(N) is FALSE (target
automorphisms move A_F without changing N); retype as min-degree in the
target-Aut orbit (Card II: degree 3 is empty for (B2), degree 4 is the
first cell). The two are compatible and both right in scope: the cap is
in terms of max(deg P, deg Q), which N does not bound (Opus's own
OPEN[N-VS-MAPDEG], "plausibly false"). The companion report itself flags
the cap as gauge-dependent on the x,y coordinates (line 836), which is
Grok's point from the other side.

Disposition: OPEN[DEG-AF-VS-N] RETYPED → OPEN[DEG-AF-CHAU] (answered,
cross-branch, at Chau's typing) + OPEN[N-VS-MAPDEG] (open) + Grok's
Aut-normalised min-degree question. Desk lane launched 08:22Z:
`chau-delta-budget-gpt55-20260902` (verify the transfer; delta_infty
(M,d,e) in closed form with the (9,6,2) reconciliation control; the (B2)
budget per admissible (M,d,e); CLAIM [D] with its three checks; the (B3)
N = 4 admissible list with n ≤ 8). **UPDATE 08:37Z: landed (99ade634).**
(1) transfer CONFIRMED with a notation repair (n = m·max(d,e), m ≤ K;
the resultant exponent is alpha·m, not m, unless R_0 is reduced);
(2) delta_infty is NOT numerical in (m,d,e) for m > 1 — needs the
Puiseux characteristic of the branch at infinity
(OPEN[DELTA-INFTY-NOT-NUMERICAL], Opus's own stop condition); (3) no
finite (m,d,e) list at fixed N without a bound on max(deg P, deg Q) in
N — Grok's objection confirmed from the other side; (4) **CLAIM [D]
CONFIRMED**: at coordinate degrees (9,6) the cap is saturated by the
realised degree-9 component, so no companion fits — OPEN[COMPANION-R0-
REALISATION] NEGATIVE at (9,6) (scope: coordinate degrees), and the cap
is a valid census prefilter; (5) (B3) needs n ≥ 4, with a finite
NECESSARY list for n ≤ 8 (cusps (2,3), (3,4), (3,8); k ranges per n)
whose exact realisability inherits (2). Opus's B3-PARAM-SEARCH (Card 3,
dual use) now has its input list; it launches after `b3-e-geometry`
reports, to avoid duplicating its G-EMBED arm.

## 5. Counterexample side: a genuine disagreement, deferred one micro-round

Four different answers to "where should a counterexample be hunted":
Grok — prime N = 7, curve-first against (B2) ∪ (B3) (Card III); Opus —
the (B3) N = 4 object as a bidegree-(Md, Me) parametrisation search,
dual-use (EMPTY closes (B3) at N = 4 by exhaustion, NONEMPTY feeds the
pipeline); Fable lane — the reducible branch at N = 6 through
COMPANION-EXISTS realisations with the fixed-sheet prefilter; the
coordinator — the A2 formal solution (WITHDRAWN, §2). All agree the S_6
enumeration is not a first move. Decision: no census launch this round;
the fixed-sheet prefilter (LOCAL-ISO TRANSPORT per component) is adopted
as a free instrument pending §1's review; the census design goes to the
micro-round that follows the four adjudications, with Opus's search first
if the Chau lane returns a finite n ≤ 8 list.

## 6. Systems check — one upgrade chosen, test already run

Four cards: Opus — OPEN/BANKED collision check at seal time (evidence:
the DEG-AF-VS-N index failure of §4); Fable lane — an OBJECT-LEDGER per
named object (evidence: the immersed-vs-cuspidal join of §2); Grok —
certainty tags on the A2 cell ledger; coordinator — a durable LANES.log.
Chosen: the collision check. Its smallest useful test was run by the
coordinator at 08:28Z: grepping the banked corpus for OPEN[DEG-AF-VS-N]'s
bounded quantity surfaces companion-curve-alln:685/785/836 — PASS.
Implementation (seal-time hook `ops/open_collision.py`, fail-closed
COLLISIONS section) is queued for a Sol systems lane in the next window.
Grok's certainty words are adopted free in the LIVE STATE cell table
(Q-TWO-ENGINE (1,3),(1,5); MODULAR (1,7); BOUNDARY-THEOREM (2,6);
RUNNING (1,9)). The object ledger is the next candidate (same failure
class). PREFLIGHT continues, unchanged.

## 7. Disposition digest and lane calls

Gaps: (a) RETYPE (map-germ; DEPTH-BOUND/PARAM-U; possibly moot for N ≤ 16
pending §2); (b) RAISE — the H2 neck, attacked through E (§3); (c) CLOSE
pending §1's review; (d) RAISE via the Chau budget / Aut min-degree;
(e) RETYPE — H2 = A_F irreducible, complement = reducible branch; the
bounded-N architecture cannot finish without an opposite-monotone
inequality (Opus) or a valuation statement such as R ≤ 1 for (B1) (Grok,
Fable lane); (f) unchanged, with CLAIM [D] pending; (g) LOWER, redesign
per profile; (h) LOWER hard; (i) LOWER (N = 4 closed; testbed); (j)
unchanged; (k) CLOSED as posed; (l) CLOSED (not a family signal).
APPROACHES rows: raise 6, 7, 25, 26, 27, 28 (reopened with data), 31;
lower 1, 19, 36 (as A2-ray search), 46; retype 29 (the A2 lane is its
instance); all else unchanged.

Lanes: `a2-ubound` CONTINUE to seal, then REDESIGN (O0/O1 → DEPTH-PROFILE
→ PARAM-U, profile per §2); `cusp-a-n8-gate` DONE (exceeded charge);
`web-sweep-20260902` DONE (THREAT board empty; its Schenk line is stale —
audited FATALLY-FLAWED 09-01); box01 A2 window CONTINUE at low priority
on the 24-thread run, no cells beyond RUN_CELLS; Box03 869 to its cap
then STOP. New this round: `b3-e-geometry-opus5` (flagship),
`cusp-a-void-review-gpt55` + `cusp-a-void-countermodel-grok46` (paired
review of §1), `phi-immersion-adjudication-sol56` (§2),
`chau-delta-budget-gpt55` (§4). Seats: Opus 2/5; GPT-5.5 2; Grok 1;
Sol 1 (+ its ideation).

## 8. Deduplication and labels

```text
fingerprint (target / mechanism / object / test)                    votes            label
case (A) all-N / local pi_1 surjects at cone cusp / rho / N=1      n8-lane, fable51  NEW (review running)
A2 residual not (B3) / object identity / map-germ vs rho / --      grok, opus, fable51  RETYPE (adjudication running)
A2 for all U / depth truncation over Q(U) / Lad_k / DEPTH-PROFILE   opus (coord. weaker form) NEW mechanism
(B3) via E / BMY, splice, embedding, anti-monotone / E at N=4 k=1  grok, fable51, opus, coord  NEW target (merged lane)
deg A_F / Chau cap cross-branch / (M,d,e) / delta_infty             opus (grok: scope)  KNOWN-ELSEWHERE (index failure)
CLAIM [D] / cap saturation at (9,6) / D_1 / substitution           opus              NEW (desk lane running)
CE frontier / four different designs / --                          all four          DISAGREEMENT, deferred
systems / collision check / OPENs vs banked lemmas / grep test      opus (fable51 adjacent)  ADOPTED, test passed
```

Shared wording was not counted as support; the two case-(A) derivations
share a mechanism but were produced by different lanes with different
inputs and different proofs, and are counted as two.

## 9. sol56 — MISSED THE CLOSE; round marked DEGRADED

At 08:56:40Z the Sol lane was still running with a 6-byte skeleton on
disk (its log shows a long body being composed in place: "exact finite
windows cannot resolve JC2 … expose a cofinal invariant or advance a
survivor through a declared state arrow"). Per COORDINATION.md the round
closes now with three of four blind submissions plus the coordinator's,
and is marked DEGRADED. Sol's submission is charged to the next
micro-round on its seal as a late arrival with full standing; nothing in
§§1–8 waits on it.

## 10. Round close and clocks

Closed 08:57Z (DEGRADED: 3/4 blind + coordinator). Launched or in flight
from this round: `b3-e-geometry-opus5` (flagship), the CUSP-A-VOID pair
(both PASSED → integration #9 bound, 00e55ac2), `phi-immersion-
adjudication-sol56` (CONFIRMED → A2 re-filed), `chau-delta-budget-gpt55`
(CLAIM [D] CONFIRMED), `a2-e2-p0-gate-gpt55` (the E2 P0). Deferred:
B3-PARAM-SEARCH (after b3-e-geometry), the profile-driven census design
and the a2-ubound successor (after the P0 gate), the collision-check
hook (Sol systems lane, next window). Next full-round floor: 20:57Z
2026-09-02, sooner on a significant event. Micro-round on the landing
of the P0 gate, b3-e-geometry, and Sol's late submission. Web-sweep
deadline 2026-09-03 ≈ 08:00Z.
