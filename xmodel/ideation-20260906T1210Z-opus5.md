# Ideation 20260906T1210Z — Opus5 blind full round

Lane `/tmp/jc2-lane.E4IDlX`. All 12 charged inputs SHA-256 verified against
`charged-inputs.list`; zero mismatches. Packet body SHA matches. No peer 1210
report or root 1210 coordinator report read. No AWS, no jc2-lean, no live
log/report/ledger/tool writes, no external post, no source fetch (the charged
local PDF+text sufficed). One small exact control run locally (below).

## 2. PRIMARY 99 VERDICT — read from the charged primary, not from summaries

**Verdict: `APPLIES_AS_EXTERNAL_THEOREM` for two of the three normalized cases;
`SPECIFIC_GAP` (unprinted reduction, not an error) for the third.** Detail:

The actual v1 chain for 99 is: §2 Theorem 2.1 (max ≥ 125 or (72,108)/(108,72))
→ table p.3 row `A0=(9,24), (m,n)=(2,3), max=99`, marked "no detail in [10]",
i.e. GGHV claim it, Moh did not prove it → §4 **Proposition 4.2 (Case (9,24))**,
txt:348–352: a counterexample gives `P,Q ∈ L^(1)=K[x,x^{-1},y]` (txt:339) with
`[P,Q]=x` and one of three Newton polygons, all with corners (6,16),(6,18) /
(9,24),(9,27) plus an extra left corner: **(1)** (0,12)/(0,18), **(2)**
(0,6)/(0,9), **(3)** none → §5 **Theorem 5.1** (txt:659): no `P,Q ∈ K[x,y]`
with `[P,Q]=x+g(y)` and `en_{3,-1}=st_{1,0}=(6,16)`, `st_{-1,1}=en_{1,0}=(6,18)`
(resp. (9,24),(9,27) for Q).

Two facts I checked myself, and which nobody in our record has stated:

* **Prop 4.2 is never cited again anywhere in v1**, and **Cor 5.7 is never
  invoked anywhere in v1** (`grep` over the whole text: the only occurrences are
  the statements at txt:348 and txt:982). Corollary 5.7's polygons
  {(0,0),(1,1),(6,16),(6,18),(0,18)} / {…,(9,27),(0,27)} are *verbatim*
  Proposition 4.1's — the **(9,27)=108** case, not the 99 case.
* I evaluated the support functionals directly. Prop 4.2 **case (2)** and
  **case (3)** satisfy Theorem 5.1(2)(3) literally (in case (2), `v_{-1,1}` is
  uniquely maximal at (6,18) for P and (9,27) for Q, so `st_{-1,1}` is as
  required). Prop 4.2 **case (1) does not**: with the corner (0,12),
  `v_{-1,1}` ties at (0,12) and (6,18), so `st_{-1,1}(P)=(0,12) ≠ (6,18)`;
  likewise `st_{-1,1}(Q)=(0,18) ≠ (9,27)`. Theorem 5.1 as printed does not
  apply to case (1).

So the printed 99 closure covers 2 of 3 cases. Case (1) needs the *Corollary 5.7
manoeuvre* (a shear `φ(x)=x+λ` turning `[P,Q]=x` into `x+λ`, which is a legal
`g(y)`, plus a `Succ`/sixth-power argument restoring the corner), applied to the
(0,12)/(0,18) edge instead of the (0,18)/(0,27) edge. That manoeuvre is printed
only for the 108-shape. This is a **narrow, mechanically plausible expository
gap**, not a refutation and not an "arXiv status" objection.

**What I did independently replay (exact, char 0, seconds).** The paper's single
CAS dependency is the elimination producing (5.9): "using a CAS (for example
Mathematica) we eliminate `d_{-10},d_{-8},…,d_{-2}`". I transcribed the nine
printed equations `(D̃²)_{-1..-5,-7}`, `(Q̃)_{-1},(Q̃)_{-2},(Q̃)_{-4}` (with
`d_3=1, d_2=0`, and `A := F_{-4}C_3^{23}`, so `C_3^{69}F_{-4}^3 = A^3`) and ran
`eliminate` in Singular over Q. The eliminant is **principal and equals (5.9) on
the nose**: `27 d_0 d_{-1}^9 + 18 d_1 d_{-1}^6 A + 8A^3`. Their CAS step is
correct and now internally reproduced.

**What I did NOT replay** (type these as unread/unverified, do not pretend):
[1] Guccione–Guccione–Valqui support paper (Cor 7.2/7.4, Prop 1.13/2.1),
[2] Prop 3.12 / Rem 3.31, [3], [5] (the corner tables generating the 10 rows),
[6] Thm 7.3, [10] Moh, [12] Prop 10.2.6. Prop 4.2's own proof consumes [1]
Cor 7.4, [2] Prop 3.12 and [12] Prop 10.2.6, all unread. Prop 5.2–5.6 I read but
did not verify line by line; Prop 5.4's separability of `f` and the two
valuations of Prop 5.6 are load-bearing and unchecked. The final contradiction
(k≥8 multiplicity 66; k≤7 degrees 76,75 < 78) I did check by hand: it is sound
*given* (5.10), (5.11).

**Consequences for our framing, both directions.** (a) The packet is right that
`NOT_CLOSED_BY_THIS_GATE` from a gcd≥16 tool never certified openness; 99 was
never an open frontier under this literature. (b) The 1030 synthesis and AUDIT
17(hhhhhhhhhhhh) say Theorem 2.1/§5 "explicitly exclude" (66,99). That is the
paper's advertised claim and I now believe it, but the **printed** §5 chain
closes cases (2),(3) only. (c) Blanket-filtering by Theorem 2.1's listed pairs
is unsafe for *targets other than x* exactly as the packet warns; the robust
`max < 108` statement is what we should cite for 99, and it is robust here.
(d) Nothing above touches D108: (9,27) and (8,28) are precisely the two surviving
108 rows, and the (8,28) row (txt:493, `[P,Q]=x²`) is the one whose system GGHV
**could not solve** — it is left open by them.

## 1. Disposition vector, avenues 1–46 (historical scores not authority)

| Avenue(s) | Disposition | Reason |
|---|---|---|
| 1 | **RAISE** | Now the interface avenue: our census must be reconciled with the GGHV corner tables ([5]), and Prop 4.2 case (1) is a real target. |
| 2 | RAISE (small) | Boundary-tree/td backbone is untouched by a degree-99 exclusion; it remains the only all-degree structure we own. |
| 3, 6, 25, 29, 31 | UNCHANGED | Scoped clients intact; none was 99-dependent. |
| 4 | **LOWER** | Its natural client was a 99/D108 germ; the 99 half is now literature-closed. Keep as falsification lane only. |
| 5, 8–18, 20, 22–24, 27, 28, 30, 33–35, 37–46 | UNCHANGED | No new evidence bears on them this round; historical dispositions stand (5 dead-ish, 11/18/41/44 refuted, 39–46 low). |
| 7 | UNCHANGED | Dissent unresolved; no new input. |
| 19, 21 | UNCHANGED | Witt/Hensel degree-12 frontier untouched. |
| 26 | UNCHANGED | Block index d2=2 successor still the cheapest. |
| 32 | UNCHANGED | Three-generator presentation stands; still equals injectivity. |
| 36 | **LOWER** | "Search past the GGV cutoff" is now demonstrably a cutoff we mis-read; a search lane needs the *literature* map first. |
| 46 | UNCHANGED | Leaf-layer only. |

Whole-portfolio note: nothing in this round raises any counterexample-side lane.

## 3. Bottlenecks — two cards

**Card A — "Prop 4.2 case (1) closure" (`NEW`).** Mechanism: reproduce the
Cor 5.7 shear for the (0,12)/(0,18) corner: apply `φ(x)=x+λ`, get `[P,Q]=x+λ`,
show `ℓ_{-1,1}(P)` is a sixth power (via [1, Cor 7.2/7.4]) so the shear moves
`Succ` and restores `st_{-1,1}(P)=(6,18)`, then cite Theorem 5.1. Deps: [1]
Cor 7.2/7.4 (unread). Cheapest decisive test: read [1] §7 and check whether the
sixth-power conclusion holds at direction (-1,1) as it does at (0,1) — desk-scale,
no CAS. Outcome: success ⇒ 99 is fully, externally closed and we cite it without
caveat; failure ⇒ a genuine literature gap worth a note to the authors (not a
counterexample). Cap: 1 desk session, stop either way.

**Card B — "D108 (8,28) is the open row, and it is *their* open row"
(`NEW connection`).** Our D108 source top is `h=(X+W)^8 W^{28}`, `F_top=h^3`,
`G_top=h^2`. GGHV's two 108 rows are `A0=(8,28), (m,n)=*(3,2)` and
`A0=(9,27), (m,n)=(2,3)`; §5 kills (9,27) via Cor 5.7, and the abstract states
they **could not solve** the remaining (72,108) system. The `(8,28)` label and
the `(3,2)` multiplicity are literally our `h`-exponents and our `F=h^3,G=h^2`
top. That is a *proposed* interface, not a proved chart identification — the
FALLACY-v2 variable/ring-map clause applies and I do not assert it. Cheapest
decisive test: state the ring map `L^(1) → our chart` with generator order and
coefficient field, then check one invariant both sides — `[P,Q]=x²` (their
txt:493) against our Jacobian normalization. If the normalizations disagree, the
interface is dead in one step. Outcome if it holds: our D108 work is the *same
open problem the literature leaves open*, which is the strongest position the
campaign has occupied. Cap: interface statement only; no solve.

Strongest falsification attack on my own card B: `A0=(8,28)` is a *corner of a
transformed polygon in* `L^(1)` after non-polynomial automorphisms, whereas our
`(X+W)^8 W^{28}` is a literal source top. Matching integers across those two
categories is exactly the flag/place/series conflation FALLACY-v2 forbids. I
therefore type card B as `PROPOSED_INTERFACE`, unproved.

No new exit-price assertion is made in this report, so no `charge_basis` line.

## 4. Specific faster path now

**D108 source-to-known-frontier map (card B), done as a written map, not a
solve.** It is cheap, it is the only place where our compute and the literature's
open case may coincide, and it requires no new licence. Second, and independent:
the **Prop 4.2 case (1)** desk check, because if the printed literature does not
in fact close 99, our completed 99 instruments become literature-relevant rather
than mere method controls. I explicitly do **not** propose replacing 99 with
larger unlicensed compute, and I do not propose a K16 uniform obstruction this
round — I have nothing new there beyond what AUDIT 17(zzzzzzzzzzz) records.

## 5. Software and campaign systems

**Software: ONE bounded proposal.** A `literature-frontier` checker that stores,
per external theorem, its *normalization* (target polynomial, ring: `K[x,y]` vs
`L^(1)`, which degrees are "actual") and its *printed case coverage*, and
answers "is `(n,m)` closed, by which proposition, with which unread deps". The
gcd≥16 tool answered a different question and nobody noticed for weeks. Bound:
a table plus a 100-line query, seeded with the 10 rows of GGHV p.3. `NO_UPGRADE`
elsewhere; the cleanup meets the 48h trial.

**Campaign systems.** Frontier-literature integration is the demonstrated
failure mode, not review overhead: a 4-hour primary read would have outranked
weeks of 99 compute. Round overhead is currently *justified* — this round found
a real, checkable defect (case (1)) that four prior rounds and the coordinator's
own read did not. Model roles: keep primary-source adjudication on a model that
is required to run its own exact control; my (5.9) replay took under a minute and
converted "conditional on their CAS" into "verified". I am not requesting lanes.

## 6. Directions: continue / redesign / stop

* **STOP**: new 99 counterexample compute, permanently, not as a HOLD. Whether
  case (1) is closed by [1] or not, 99 is a literature question now.
* **REDESIGN**: the census→frontier interface (avenue 1) to carry external
  coverage per row, per §5 above.
* **CONTINUE**: D108 as the campaign's live case, with card B's map written
  before any further solve; the boundary-tree/td backbone (avenue 2); K16 at its
  promoted `t ≤ 8` scope with the product target as recorded.
* **CONTINUE (unchanged)**: already-launched capped solves under existing
  custody; no new destructive or external action taken or requested here.

`OPEN[PROP-4.2-CASE-1]`, `OPEN[D108-CHART-IDENTIFICATION]`,
`OPEN[K16-UNIFORM-m]` remain typed open. No proof of JC2, no counterexample,
no new exclusion is claimed by this report.

<!-- BODY-END -->
