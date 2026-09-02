# Coordinator ideation — round 20260902T0741Z (Fable 5.1, fresh eyes)

Written 2026-09-02 ~08:05Z by the coordinator BEFORE reading any of the four
blind submissions (grok46, opus5, fable51 sealed at write time; sol56 still
running). Same packet (2646ac69), same contract. Not blind in the coordinator
sense — I froze the packet — but independent of the other lanes. Desk only, no
CAS, no literature, nothing consumed beyond banked reports.

## 0. The one-paragraph reframe

The campaign describes itself as "one theorem away" on the H2 side
(OPEN[A2-U-BOUND]). Fresh eyes say: the horn's live residual is not an
almost-closed obstruction, it is a **formal germ at infinity that has not yet
been shown to fail to algebraize** — the same shape as the D-series/DEPTH-STAB
disproof lane (APPROACHES row 4) seen from the proof side. The order-by-order
ladder giving "four linear conditions on five new coefficients per order" is
exactly the statement that the FORMAL solution space on the ray is nonempty
with one new free parameter per order; polynomial solutions are the
terminating formal solutions. So OPEN[A2-U-BOUND] is an algebraization
question, and both sides of the campaign already own the tools for it. The
second fresh-eyes point is that the two "disconnected instruments" (the A2
analytic residual and the (B3) group cage) meet in one object nobody has put
on the board: the **Galois closure** of the Keller map, a finite normal
S_N-cover of the target plane branched exactly along A_F, on which the cusp
cage supplies every numerical input an orbifold Bogomolov–Miyaoka–Yau
inequality needs. Cards 1–3 below are these two observations made decidable,
plus the cheapest sanity question in the packet (what U geometrically is).

## 1. Disposition vector

### 1a. Over the coordinator's gaps (a)–(l)

| gap | disposition | reason |
|---|---|---|
| (a) A2-U-BOUND | **RETYPE** | Two different questions are conflated: (a1) U ≤ B(N) for a fixed sheet count N, which would make the horn's A2 residual FINITE and cell-decidable for every N ≤ 16 the H2 program cares about; (a2) uniform-in-e termination, which is the all-degree statement. Card 3 decides which one the geometry hands us. Only (a2) is "the missing theorem"; (a1) may be a lemma. |
| (b) (B3) cage rigid-not-empty | unchanged as a fact; **RAISE** as a target | Card 2 gives it a new gate with all inputs pinned. Note N=4 is closed by the checked Domrina chain, so whatever kills the N=4 (B3) survivor there is an all-N candidate mechanism — extract it (§4, attack P2). |
| (c) case (A) N ≥ 8 | unchanged (lane running) | Card 2's inequality is also computable on the N=8 trefoil cell; feed it to the running lane at harvest. |
| (d) (B2) beta-forced 5–16 | unchanged, low | Bounded-N mop-up; no new mechanism proposed. |
| (e) all-degree ceiling | **RETYPE** | H2 = A_F irreducible (Jelonek non-properness curve irreducible). Its complement is the reducible branch, currently blocked on declared-completion data. Directness: the campaign's only all-N instruments are the Orevkov/Chau budgets and the cusp/homology theorems; every closure is bounded in N. The bounded-N architecture cannot finish unless a degree-monotone invariant appears; the Galois-closure orbifold invariants (Card 2) are the first candidates that are monotone in the branching data rather than in N. |
| (f) reducible R0/degree-cap | unchanged | No fresh idea; do not spend Opus seats here this round. |
| (g) N ≥ 6 census | **LOWER** | With N ≤ 5 closed and the frontier at all-degree necks, an S_6-scale census buys a bounded-N negative at high cost. Keep the pipeline warm; do not run a census until a positive-side candidate names a degree. |
| (h) infinite-U family as construction target | **RAISE** | Card 1's dual branch: the formal solution on the ray is the first positive-side object the campaign has ever had that survives every reviewed gate by construction. |
| (i) (B3) N=4 rigid survivor as construction target | **LOWER** | N=4 is closed; the survivor is representation-level only. Testbed, not target. |
| (j) Witt / AS109 | unchanged, orthogonal | — |
| (k) A2 ↔ (B3) bridge | **RAISE** | The Galois closure IS the bridge object (Card 2): A2 is its local model at the cusp-at-infinity chart, (B3) is its monodromy. |
| (l) non-termination as positive signal | **RAISE** | Yes — see §0; it is a formal germ. Treat it as such on both sides. |

### 1b. Over the 46 APPROACHES.md rows (changes only)

- Row 4 (formal-germ certification / algebraization): **RAISE** — its
  machinery (DEPTH-STAB, Padé/algebraicity tests, "modular ≠ germ ≠ char-0 ≠
  polynomial" discipline) is exactly what the ray's formal solution needs;
  reuse, do not rebuild.
- Row 28 (log surfaces / BMY): **REOPEN** — it stalled on NEEDS-DATA and on
  κ̄(C²) = −∞. The cusp cage now pins the data, and the object to apply BMY
  to is the Galois closure (or the orbifold (P², Ā_F with weights)), not C²
  itself. The κ̄ trap is real and is Card 2's step 0.
- Row 31 (ZMT / integrality / étale finiteness): **RAISE** — the normalization
  of the target in the Galois closure is finite (ZMT), so the block-descent
  "étale sandwich" becomes a finite Galois cover with computable invariants.
- Row 26 (primitive monodromy / function-field Galois): **RAISE** modestly —
  the Galois closure's group is rho(G), already pinned at N=4 (S_4) and at the
  N=8 trefoil cell (order 24); its structure is a hypothesis-free input.
- Rows 36, 37 (guided search, finite-field census): **LOWER** — see gap (g).
- Row 46 (formalization): unchanged, non-blocking by directive.
- All other rows: unchanged.

## 2. Reranked bottlenecks

Proof side, in order:
1. Termination of the ray recursion (Card 1) — decides the A2 residual
   uniformly if the tail can never vanish.
2. Per-N boundedness of U (Card 3) — if true, the A2 residual is finite for
   each N and box01 closes it for N ≤ 16 by enumeration.
3. An all-N mechanism for (B3) — Card 2 (orbifold BMY on the Galois closure)
   is the first candidate with pinned inputs.
4. Case (A) at N ≥ 8 — lane running; Card 2 feeds it.
5. Reducible branch R0/degree-cap — parked.

Disproof side, in order:
1. The formal solution on the ray (Card 1, negative branch): compute it,
   test algebraicity, try to terminate it.
2. Anything the U-meaning question (Card 3) turns up: if U is a Keller degree,
   the ray is a degree-unbounded family — the classic place a counterexample
   hides.
3. N ≥ 6 census — only after a candidate names a degree.
4. Witt lifts — orthogonal, unchanged.

## 3. Genuinely new avenue: the Galois closure as the bridge object

Let F = (P,Q): C² → C² be Keller of topological degree N, A_F its
non-properness curve, G = π₁(C² \ A_F), rho: G → S_N the sheet monodromy
(transitive). Let L be the Galois closure of C(x,y)/C(P,Q) and
**X̂ = normalization of the target C² in L**. Facts that need no hypothesis:

- X̂ is a normal affine surface, FINITE over the target C² (normalization of a
  normal variety in a finite extension is finite), with rho(G) acting and
  X̂/rho(G) = C²_target. Its branch locus is contained in A_F (F is étale, and
  proper over C² \ A_F, so L/C(P,Q) is unramified there).
- X̂/Stab(1) = Ŝ is the normalization of the target in C(x,y); by ZMT the
  source C² is an OPEN subset of Ŝ, with complement a curve mapping onto A_F.
  (This is the campaign's SHEET-GATE Y; X̂ is its Galois hull.)
- Everything about X̂ over a point of A_F is determined by rho and the local
  monodromy: over a smooth point of A_F, X̂ has cyclic quotient singularities
  of type given by the cycle structure of rho(meridian); over the cusp and
  the nodes, by rho(Loc) — exactly the data the (B3)/(A) cages pin.

So the (B3) cage is a description of X̂'s singularities, and the A2 analytic
residual is (per its own setup: the ring C[A,U,Z]/(U² − A − A²Z) is a double
cover of an (A,Z)-plane with a Poisson bracket, and the residual equations
are the coefficient identities of {f,g} = κ at A-degree ≤ 2) a LOCAL MODEL
of the pair (f,g) near a boundary point of Ŝ — the same surface, seen at one
chart. That is the bridge the packet asks for in (k): both instruments are
constraints on ONE normal surface, and neither has used the other's data.

What the bridge buys immediately: a compactification X̄ of X̂ has quotient
singularities with known local invariants, hence orbifold Chern numbers
c₁², c₂ computable from (N, p, q, k, the node contacts t_i, rho). The
orbifold BMY inequality (Miyaoka / Kobayashi–Nakamura–Sakai form, for a
normal surface of log general type with quotient singularities) is then a
numerical gate with NO free inputs at the pinned cells — the first gate in
the campaign that is monotone in branching data rather than in N. Its known
trap (row 28) is that it needs κ̄ ≥ 0 (log general type or at least the
inequality's hypotheses); computing κ̄ of the weighted pair
(P², Ā_F + line at infinity with weights 1 − 1/e) is step 0 and is itself
decisive: if κ̄ = −∞ for every admitted cusp pair, the gate is vacuous and we
learn that too.

## 4. Strongest attacks

**P1 (proof, uniform): terminate the ray recursion.** Card 1. The banked
"4-on-5" structure is a linear recursion for the tail coefficients in which,
at each order, the new eta-coefficient (or one designated unknown) is free.
A polynomial solution exists iff some choice of the free parameters makes
every coefficient beyond degree U vanish simultaneously. Write the recursion
in closed form (RAY-1's four rows are its first instance; the (top−2) step is
already computed at ten cells), express the tail coefficient of highest
weight at order k as an explicit affine function of the free parameters
beta₁..beta_k, and show that its leading part in beta_k is a nonzero
constant (unique continuation) while the termination conditions at
successive orders are inconsistent. If that pattern is the same at every e
(the RAY-DEP identity suggests the row structure is e-independent up to
the rho term), this is OPEN[A2-U-BOUND] in the strong form: EMPTY for every
U, uniformly.

**P2 (proof, (B3) all-N): read the mechanism off the checked N=4 chain.**
The repaired Domrina–Orevkov chain closes N=4 including the (B3) profile.
Some lemma in it kills exactly the object the horn flagship calls
RIGID-NOT-EMPTY. Locate that lemma, state its mechanism without the N=4
specifics (splice diagram census vs an invariant), and test N-uniformity
against the general-N cage (G1)–(G4). This is a reading task, not a
research task, and it is cheap. (Distinct from OPEN[RESIDUAL-TO-DOMRINA-
STATE], which asked to instantiate residual DATA in the chain; here we
extract a MECHANISM from it.)

**C1 (counterexample): compute the formal solution on the ray and test it
for algebraicity.** Same computation as P1, opposite reading: fix e = 1, take
the 2-dimensional next-order residual, run the recursion to order 20–30 with
the free parameters as symbols (or specialized to small rationals), and test
the resulting Laurent tail for algebraicity (Padé / linear recurrence with
polynomial coefficients / p-adic growth — row 4's tools). Algebraic ⇒ a
candidate algebraic (not polynomial) pair at the A-degree-2 jet, i.e. a
candidate for the source-side "non-polynomial limit" the char-p lane also
produced; then ask whether a shear/normalization makes it polynomial.
Transcendental with a growth certificate ⇒ P1 by another route.

**C2 (counterexample, structural): if Card 3 says U is a Keller degree,
then the ray IS a degree-unbounded family** of jets satisfying every reviewed
gate, and the campaign should treat it as its first positive-side lead,
running the algebraization discipline of row 4 on it rather than more cells.

## 5. New cross-connections

1. Horn ladder ↔ D-series algebraization (rows 4, 19): the ladder's
   non-termination is a formal-germ statement; the "modular ≠ germ ≠ char-0 ≠
   polynomial" typing and DEPTH-STAB/Padé tests transfer verbatim.
2. (B3) cage ↔ A2 residual ↔ ZMT/Galois closure (rows 26, 28, 30, 31): one
   surface, three descriptions (§3).
3. Case (A) N=8 survivors ↔ orbifold BMY: the trefoil cell has every input
   pinned (p,q) = (2,3), a = 2, j = 2, rho(G) of order 24, dicritical (2,3);
   Card 2's inequality is a one-line evaluation there.
4. HOM-COVER's NO-PUSHFORWARD ↔ Galois closure: torsion in H^ab of the
   index-N subgroup does not push forward, but the Galois closure's
   abelianization H₁(X̂) is a rho(G)-module whose invariants/coinvariants are
   the classical Chevalley–Weil data; the gate "H₁(C² \ E) is free" becomes
   "the Stab-coinvariants of H₁(X̂ ∖ branch) are free", a different (and
   representation-theoretic, hence all-N) statement. Untested.

## 6. Software acceleration / decisive experiment

**Experiment (decisive for Card 1, ~1 desk day + one box job):** a
`ray_recursion.py` that builds the wall system in ray-kill's closed form
(E1 free, Theta = sE1/eta), symbolically solves order top−k for k = 1..K
keeping the free parameters symbolic, and reports at each k: rank, the
new free parameter, and the leading coefficient of the highest-weight tail
unknown. K = 8 at e = 1,2 is sympy-scale; K = 20 is a box job. The one
number that matters is whether the leading coefficient is ever zero.

**Acceleration (measured, small):** the A2 window runner ran single-threaded
(threads=1) on a 64-core box and timed out the (1,9) mod-p screen at 1h while
63 cores idled; a 24-thread rerun with 1.5h/4h timeouts is now running in
parallel. Add `--items` selection and default `--threads` to half the core
count. Also: qqideal's MODULAR verdict on unit ideals should be upgradeable to
PROVEN cheaply by a second prime + a rational reconstruction of the
certificate (1 ∈ I witnesses are small); that would retire the per-cell
"certainty upgrade" review debt wholesale.

## 7. Campaign-systems check

**UPGRADE card (smallest useful test):** lane completion is currently
detected only by the coordinator polling `.lane-locks/`; the runner already
knows when it exits. Have `ops/lane.sh` append one line
`<utc> <tag> exit=<rc> report=<sealed|unsealed|none> bytes=<n>` to
`xmodel/LANES.log` at exit. Test: launch one dummy lane, check the line. Cost:
ten lines of shell. Benefit: every coordinator (any model) gets a durable,
greppable lane ledger instead of session-local watchers, and handoffs stop
losing lane state (this morning's handoff had to reconstruct the running set
from `ps`). Rotation slot: claim/review propagation + operator quality.

## 8. Idea cards

### Card 1 — RAY-RECURSION: terminate or algebraize the horn's formal germ
- Target: OPEN[A2-U-BOUND] (uniform) and gap (h)/(l) simultaneously.
- Mechanism: closed-form order-k recursion on the E1-wall ray; prove the
  tail cannot terminate (proof) or compute and test the formal solution
  (disproof).
- Dependencies: C32 T1–T5, HORN-A2, RAY-1/DEP/EDGE/2 (all reviewed); the
  preserved `box/raykill-cells-20260902/cell.py` builder; row-4 algebraicity
  tests.
- Cheapest discriminator: e = 1, orders top−1..top−6 symbolically. Does the
  highest-weight new unknown at order k enter with a constant nonzero
  coefficient, and are the termination conditions (all coefficients of degree
  < 0 vanish) consistent for any parameter choice?
- Outcomes: (i) inconsistent for all parameters at some finite order ⇒
  EMPTY uniformly in U at e=1; repeat at e=2,3 and look for the
  e-independent pattern ⇒ theorem. (ii) consistent with a free family ⇒
  explicit formal solution; run algebraicity tests ⇒ either a candidate jet
  (positive side) or a transcendence certificate (proof by growth).
  (iii) no structure by order 8 ⇒ hand to msolve as a job on the recursion
  variables (a different, smaller system than the cells).
- Stop condition: order 8 at e = 1,2 with neither inconsistency nor a
  recognizable recurrence.
- Expected information gain: HIGH — it is the same computation both sides
  need, and either outcome moves the ledger.

### Card 2 — GALOIS-CLOSURE ORBIFOLD-BMY gate
- Target: gap (b) (all-N (B3) mechanism), gap (c) (N=8 case (A)), gap (k).
- Mechanism: X̂ = normalization of the target C² in the Galois closure;
  compactify; orbifold Chern numbers from the pinned local monodromy;
  orbifold BMY (Miyaoka/Sakai) as a numerical inequality in
  (N, p, q, k, t_i, rho).
- Dependencies: the cusp cage theorems (reviewed), N4-PIN, HORN-FLAGSHIP
  Props 3.1–3.2 and B3-N4; a primary-source statement of orbifold BMY with
  its exact hypotheses (custody step).
- Cheapest discriminator (step 0): κ̄ of the weighted pair
  (P², Ā_F + L_∞, weights 1 − 1/e from rho) at the N=8 trefoil cell and at
  the N=4 (B3) admitted pairs (2,3),(3,4). If κ̄ = −∞ everywhere the gate is
  vacuous — stop. Step 1: evaluate the inequality at the same cells.
- Outcomes: violated at N=8 trefoil ⇒ a NEW kill and an all-N candidate
  (feed cusp-a-n8-gate); satisfied ⇒ compute the slack as a function of N to
  see whether it is monotone; vacuous ⇒ record NO-GO with the κ̄ reason
  (closes row 28's reopening honestly).
- Stop condition: step 0 vacuous, or the inequality needs an input the cage
  does not pin (name it as an OPEN).
- Expected information gain: MEDIUM-HIGH; cheap; first all-N-shaped gate.

### Card 3 — U-MEANING: is the horn's free degree a Keller degree or a sheet datum?
- Target: gap (a) retype; decides whether box01's cells can ever finish.
- Mechanism: in the one-cusp A2 setup (theta/r2/spec), identify what the
  coordinate Z parametrizes on the geometric surface (a boundary curve at
  infinity of Ŝ, or an affine coordinate of the source), and hence whether
  deg_Z of the level-0 coefficients (U = deg q) is bounded by intersection/
  sheet data (then U ≤ B(N), e.g. via the dicritical degree s_l ≤ N/2) or is
  a free polynomial degree (then U is the Keller degree in disguise).
- Dependencies: theta (one-cusp-a2), r2, spec — reading only.
- Cheapest discriminator: one page of derivation; a coordinator or a
  15-minute lane.
- Outcomes: bounded ⇒ compute B(N) for N ≤ 16, extend RUN_CELLS to that
  bound, and the A2 residual becomes a finite computation per N (the
  bounded-N horn CLOSES on box01 in days); unbounded ⇒ Card 1 is the only
  route and the ray is a genuine degree-unbounded family (positive-side
  signal, C2).
- Stop condition: none needed — it is a reading task.
- Expected information gain: HIGH per unit cost; possibly the cheapest
  decisive question on the board.

## 9. Lane recommendations

- `a2-ubound-opus5-20260902`: CONTINUE; at harvest, inject Card 1's
  recursion framing and Card 3's question if it has not found them.
- `cusp-a-n8-gate-opus5-20260902`: CONTINUE; at harvest, inject Card 2 step
  0/1 on the trefoil cell.
- `web-sweep-20260902-grok46`: DONE (THREAT board empty). Its "Schenk
  unaudited" line is stale: `schenk-audit-b-sol56-20260901` returned
  FATALLY-FLAWED on 2026-09-01. Record, do not relaunch.
- box01 A2 window: REDESIGN — the single-thread run is wasting the box;
  the 24-thread parallel run supersedes it once it passes (1,9); after
  Card 3, extend or truncate RUN_CELLS by B(N).
- Box03 869: CONTINUE to its cap, then STOP; confirmatory only.
- N ≥ 6 census design: DEFER (gap (g)).

## 10. Directness clause

If Card 3 comes back "U is a sheet datum", the H2 residual for N ≤ 16 is a
finite computation and the campaign should say so and run it to the end. If
it comes back "U is a Keller degree", the campaign has been calling a
degree-unbounded formal family "one theorem from closed", and should
re-weight toward the positive side (Cards 1/C1) at once. Either answer is
better than the present framing.

<!-- BODY-END -->
