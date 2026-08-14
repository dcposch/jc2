# TOWER-ROLLOUT.md — rollout plan for the 16 remaining §11a cells at the tower tier

> **STATUS: PLANNING ARTIFACT (2026-08-14). NO NEW KILL IS CLAIMED
> HERE.** Input: the promoted `(9,15,7,3)@2` cell-level tower kill
> (`TOWER-9-15.md`, Grok SOUND-WITH-ERRATA + Sol CONFIRMED-KILL, 696/696)
> and the promoted §11a census (17 cells; 16 remain). Output: (1) a
> uniformity decomposition of the kill mechanism into panel-level vs
> cell-level ingredients, (2) the clash-window arithmetic for ALL 16
> cells (engine `cases/tower_rollout_arith.py`, exact `Fraction`, census
> parity PASS), (3) a candidate UNIFORM THEOREM with its proof
> obligations, (4) execution order, costs, and risk register. Every
> per-cell verdict below is a PREDICTION (arithmetic confirmed on a
> realization probe), not a certificate. "Untouched" never means safe.

Engine: `cases/tower_rollout_arith.py` (reuses `px2`/`px5` READ-ONLY;
reproduces the §11a route census 16/16 cells exactly — raw and eq counts
— before computing anything new). No git commit was made; no spine was
constructed.

## 0. Inputs and trust perimeter

| input | role |
|---|---|
| `TOWER-9-15.md` (PROMOTED) | the kill mechanism: level-1 clash, three-case exhaustion, universality (ν_X ≥ 2), N1–N4, terminal-independence |
| `cases/tower_check.py` | the validated engine; its UNIVERSAL A/B/C blocks are ν_X-parametric identities, reusable verbatim |
| BOOK-OFFAXIS §1a/§8 Step 1/P3 | the UNIQUE td-7 off-axis entry: type (2,3), Λ=(3,4), poles (1,1,2)⊕(1,2,3), M=(1,2); chain 1 frozen at (μ,w,M)=(1,2,1); chain-2 seed = ENTRY (3/2,2) |
| BOOK-OFFAXIS §10 P0–P2 (PROMOTED) | priced step menu, ψ-budget, arrival law |
| §11a census (PROMOTED) | the 17-cell book, arrivals, route counts; H5a conditionality riders |
| `xmodel/grok-tower-review.md` finding 7 | the per-cell checklist this plan executes: (type, i_G parity, min i on the priced chain-2, chain-1 budget residual, pole-adjacent gap vs smallest chain-2 gap) |

H5a rider inherited: 15 of the 16 cells exist only in the promoted
Q-value/E5 reading. `(10,15,7,5)@3` is the ONLY remaining cell of the
forced-ν book (which was exactly {(9,15),(10,15)}). Under the P-value
reading no census is derivable (rider only). Fleet: not needed — all
tower work is exact local `Fraction` arithmetic (FLEET.md hard rule not
triggered).

## 1. UNIFORMITY ANALYSIS

### 1.1 The decisive structural fact

**Every §11a cell is a merge of the SAME two chains.** The td-7 off-axis
entry is unique (BOOK §1a), so for all 17 cells: chain 1 is the b=1 pole
(2,3) with state frozen at (μ,w,M)=(1,2,1) (§8 Step 1 / P3 — DS3: no
resonance from w=2; R1.3: no dirty vertex at μ=1; St 8.4: l | M = 1);
chain 2 is the b=2 pole (4,6) with seed state (3/2,2), walking the SAME
px5 priced closure (69 states, budget 5). Cells differ only in: μ0, the
arrival state (w_U^req, M_U), the arrival vertex menu, the cell frame
(κ̄, X = κ̄−2), and the trunk/terminal family. Consequently the entire
tower-clash apparatus of `TOWER-9-15.md` §3 decomposes as follows.

**Cell-GENERIC (panel-level, prove once):**

- **(G1) Level 0.** Both poles are reduced type (2,3) for every cell
  (entry-level). Pole death gap g₀ = κ̄_P/D_{f,P} = 5/2 at both ⟹
  (k₀,l₀) = (2,3), α₁ = 3/2. `deg p_{f,P1} = 2`, `deg p_{f,P2} = 4` —
  the constants "2" and "4" in the whole (9,15) argument are entry
  facts, NOT cell facts (at μ0 = 2 they coincidentally equal μ0 and
  2μ0; see Risk 6).
- **(G2) Chain-1 stack and gap(X).** Chain 1 is a stack of clean l=1
  neutrals for EVERY cell, with pole-adjacent vertex X carrying
  `deg p_{f,X} = 2ν_X`, `d_{q,X} = ν_X+1`, hence **gap(X) =
  (ν_X+1)/(2ν_X) ∈ (1/2, 3/4]**, shape-independent — verbatim (9,15).
  New observation (candidate lemma **L-A**): the freeze is
  budget-INDEPENDENT — at l = 1 a non-clean step is shape-impossible
  (any NE orbit or ε needs m_j·dq < dp resp. ε·dq < dp, while the own
  searrow needs E = 1·dq − dp > 0: contradiction), so charged chain-1
  steps are excluded even on budget-slack routes. If L-A certifies, the
  "budget saturation" ingredient (TOWER-9-15 §6 door 4, §9(iv))
  becomes redundant and the 7 cells with non-eq routes need no special
  treatment. If L-A fails review, those routes need per-route charged
  exhaustion (Risk 8).
- **(G3) The F1-analog.** The first CHARGED chain-2 step from ENTRY is
  forced to arriving mult l = 2 (l | M_entry = 2; l = 1 steps are
  neutral; the two λ=3 first steps, ε (7,5) and pure-b, land M = 1
  which is absorbing, so no class-C arrival can follow them). The
  complete menu (engine-verified = the P0/px2 menu):
  | first vertex | state | λ | i = 4/l | deg p_f | **death gap** | Case-A delta form |
  |---|---|---|---|---|---|---|
  | (A) = (21,15), ν=7 | (2/3,3) | 2 | 2 | 42 | **5/14** | δ₁ = 2 + 7/ν_X ∈ ℕ iff ν_X \| 7 |
  | (C) = (20,16), ν=5 | (3/4,4) | 2 | 2 | 40 | **2/5** | δ₁ = 1 + 5/ν_X ∈ ℕ iff ν_X \| 5 |
  So every realization of every cell carries a P2-adjacent charged
  vertex with **i = 2 (= 2P_pre under insertions), cap k | 2, gap
  ≤ 2/5 < 1/2 < gap(X)** — the (9,15) F1 package, with (C) literally
  the same cell. Both menu cells have simple reduced factors (the cap
  carrier) and prefix-menu δ₁ ∈ ℕ at all three pairs ((A)/ε: 16, 9,
  23; (C): 11, 6, 16 — the Sol-table row).
- **(G4) Window emptiness.** Engine audit over ALL enumerated
  realization path-vertices of all 16 cells: **max chain-2 vertex gap
  = 2/5** (witness: the (C) cell; 5/14 for the one cell whose routes
  avoid (C)), i.e. `< 1/2 ≤ inf gap(X)`. Structural backing, panel
  level: gap(v) = d_q/deg p_f with deg p_f ≥ 4 at the first vertex and
  multiplied by ≥ 2 per step; resonant (n ≥ 2) landings could poke
  above 1/2 only with Δ = (n−1)ν+1 ≥ 13 | num(w), and NO closure state
  has num(w) ≥ 13 (engine check; the only resonances in the whole
  closure are n=2,ν=2 steps at three deg-large states). Inserted
  neutrals: gap ≤ 3/8 (N4, Dprev ≥ 4). Trunk/G/root gaps sit far below
  the window by searrow growth (lemma **L-E**, same argument as trunk
  §7: κ-rescaling cancels in κ̄/D_f).
- **(G5) The exhaustion itself.** Cases A/B/C are IDENTITIES in
  ν_X ≥ 2 (already machine-checked as the UNIVERSAL blocks of
  `tower_check.py`): A: k₁ = 2ν_X ∤ 2 (cap; at ν_X = 2 vs the joint
  cap 4 it is N2-parity that refuses — parity's one remaining
  load-bearing role); B: gap(F1') < gap(X) and δ(X) ∈ ℕ cannot skip
  its zero; C: 2ν_X ∤ rν_X + 1 and ν_X ∤ 1, any prefix length, prefix
  menu = half-integer grid ∩ (gap(X), 5/2) = {(1,2),(2,3),(2,5)}.
  NOTHING cell-specific enters. Per-cell prefix-δ integrality at
  deeper vertices can only SHRINK the menu (harmless).
- **(G6) Terminal-independence.** The clash lives on the pole-to-merge
  subtree; (H8) at G reads deg p_{f,U} = i_G·μ0 from the priced chain-2
  regardless of G's rootward neighbour — the §7 argument is a schema,
  reusable per cell for every trunk/terminal of its route list (route
  multiplicity is almost entirely terminal multiplicity: e.g. 47 routes
  of (10,15) over 1 arrival state).

**Cell-SPECIFIC (per-cell obligations):**

- the arrival states (M_U classes) and λ; three cells have TWO M_U
  classes (Risk 2);
- i_G = deg p_{f,U}/μ0 and the stack product P = i_G/2 per realization
  (H8): existence (P ≥ 2, "stack nonempty") and integrality (P ∉ ℕ ⟹
  spine-dead, bookkept separately — "dead either way" hygiene §7a);
- the C3-N eligible-state tables (which chain states can host zero-cost
  insertions on THIS cell's routes) — generic FORM (gcd(l,ν+1) =
  M_state), cell-specific LIST;
- per-vertex prefix-δ tables and, for probe-grade certificates only,
  the full C1 spine decoration + C4 T1 rows.

### 1.2 Answer to (a): X and F1' exist for all 16; the gap arithmetic

For every cell: gap(X) = (ν_X+1)/(2ν_X) ∈ (1/2, 3/4] (identical
family), F1' gap ∈ {2/5, 5/14} (per-route from the two-cell menu), the
clash window (gap(X), 5/2) contains NO vertex gap, and the stack is
NONEMPTY on every probed realization: min product over all 16 cells and
all realizations is P = 7 (at (10,15)@3); the exact small-deg scan
(complete enumeration of all realizations with deg p_{f,U} ≤ 50 =
2·μ0_max) found **zero** empty-stack (P = 1) realizations panel-wide.
So the (9,15) squeeze applies verbatim to every cell: X must die first,
its death step can never be integral while F1' is alive. Per-cell
numbers in §2.

### 1.3 Answer to (b): N1–N4 cell-independence audit

| lemma | proof consumed | cell-independent? |
|---|---|---|
| N1 (insertion menu: n=1, clean single-orbit (lν,ν+1), gcd(l,ν+1)=M_state) | R1.2 w-law identity Δ−n = (n−1)(ν−1) ≥ 1 + state-preservation | **YES, as stated** — pure transport identity |
| N2 (parity: pre-F1 inserted ν odd, P_pre odd) | ENTRY state (3/2,2) has M = 2; gcd(l,ν+1) = 2 | **YES** — ENTRY is shared by all 16 (it is the entry pole state, not a cell datum) |
| N3 (joint cap k \| 2) | deg p_{f,P2} = 4 (full pattern (t−A)^4), first-charged i = 2P_pre, gcd(4, 2P_pre) = 2 via N2 | **YES after one restatement**: replace "F1 = (20,16)" by "the first charged vertex (either menu cell)" — both have i = 2; the constant 4 is the P2/entry fact |
| N4 (uniform gap bound for insertions) | Dprev ≥ 4, gap = (ν+1)/(Dprev·ν) ≤ 3/8, l-free | **YES after retargeting** the comparison from "< 2/5 = gap(F1)" to "< 1/2 ≤ gap(X)" (which is all the exhaustion needs); the "charged gaps only shrink" clause is per-cell mechanical |

The P0 pricing and gcd caps (St 8.4) they consume are panel-level
promoted laws. The single genuinely cell-specific residue is the
ELIGIBLE-STATE LIST for C3-N (per-state ν-constraints, minimal Dprev,
cap-relevance) — regenerable mechanically from px5 per cell.

### 1.4 Answer to (c): parity-lemma reach

Universality (ν_X ≥ 2 closed forms) removed oddness from the main
exhaustion, so the chain-1 product's parity is NOT needed — for any
cell. Parity survives in exactly two places, both panel-universal:
(i) N2 ⟹ N3's gcd(4, 2P_pre) = 2 (the joint cap), which is what
refuses Case A at ν_X = 2 (relevant to every cell whose realizations
admit even stack members — e.g. all M_U-even variants); (ii) the §7a
spine-tier rider: a realization with i_G odd (product ∉ ℕ) fails (H8)
i-sync and is dead at the spine tier — bookkeep separately per cell,
never claim it as a tower kill. Reach: all 16 cells, with no per-cell
parity computation required beyond P ∈ ℕ checks.

### 1.5 THE UNIFORM THEOREM (candidate) and its proof obligations

**UT (td-7 tower uniformity).** *Let Z be any cell of the §11a promoted
book and R any filed completion route of Z, with realization family as
in design §2.4/§4.1 (charged DAG + free characteristics + neutral
padding + zero-cost insertions at eligible states, all arrivals M_U).
Then the approximate-root tower of every realization of R is obstructed
at ladder level 1 by the X/F1' clash; hence Z is tower-dead.* Under UT
plus the promoted (9,15) kill, the td-7 §11a book is EMPTY at the tower
tier (in the promoted H5a reading; the forced-ν book closes with
(10,15) alone).

Proof obligations, in dependency order:

- **U-OB1 (= L-A).** Chain-1 freeze is budget-independent (the l = 1
  shape contradiction above), OR: per-route saturation bookkeeping for
  the 7 cells with budget-slack routes. One page; decides quantifier
  form for everything else.
- **U-OB2 (= G3).** The first-charged-step menu is exactly {(A),(C)}
  with l = 2, i = 2, simple reduced factors, gaps 5/14 and 2/5; the
  M = 1 absorbing argument. (px2 menu is already the complete printed
  menu — cite P0; add the absorbing-M lemma.)
- **U-OB3 (= G4 + L-E).** Closure-wide window emptiness: every
  realization vertex gap < 1/2 (first-step base cases + the ×≥2 growth
  + no-resonance-fuel audit + N4 for insertions + searrow for
  trunk/root). The engine's audit is the numeric shadow; the lemma
  needs the parametric closure (identity + lattice, C3-V style).
- **U-OB4.** The universal A/B/C block + prefix-menu derivation,
  imported from `tower_check.py` unchanged, with the joint-cap
  parameter 2P_pre and the two Case-A δ-forms (ν_X | 5 and ν_X | 7
  exponent-kill branches, both already exercised at (9,15) for the
  first).
- **U-OB5 (per cell, mechanical).** Stack-nonemptiness quantifier:
  deg p_{f,U} > 2μ0 for every realization (engine result: min over the
  panel is 42 vs 2μ0 ≤ 50 per cell — the per-cell margins in §2 are
  enormous; the certificate states it as a growth bound per arrival
  state, plus the exact ≤ 2μ0 scan showing emptiness).
- **U-OB6 (per cell, mechanical).** C3-V/C3-N analogues: M_U-class
  realizations (pure-b gcd classes), padding families, eligible-state
  insertion tables, H8 product integrality ledger (∉ ℕ ⟹ spine-dead
  rider).
- **U-OB7 (= G6).** Terminal-independence instantiated per cell (one
  table per cell: every terminal's trunk gaps below window; κ-rescaling
  cancellation).

A second zero-chain-law moment is exactly what this is shaped like: one
theorem, sixteen corollary rows, each row = the finding-7 checklist
with all entries green. The (9,15) certificates become the UT's worked
example rather than a template to copy 16 times.

## 2. PER-CELL TRIAGE TABLE

Clash-window arithmetic for all 16 (engine output; exact fractions).
Columns: arrival = E5 arrival w_U (λ; M_U classes); DAGs = distinct
charged step-sequences reaching the arrival states within budget 5
(minimal parametric instantiation); depth = min # chain-2 vertices;
F1′ = first-charged-step cells occurring on its routes (gap); min
deg p_{f,U} with witness realization; P_min = min stack product
deg p_{f,U}/(2μ0); gapmax = max chain-2 vertex gap on its routes.
gap(X) = (ν_X+1)/(2ν_X) ∈ (1/2,3/4] and window emptiness hold for ALL
rows; empty-stack (P = 1) realizations: NONE, all rows (exact scan).

| cell @ μ0 | κ̄ | X | arrival | routes raw(eq) | DAGs | depth | F1′ (gap) | min deg p_{f,U} (witness) | i_G | P_min | gapmax | class |
|---|---:|---:|---|---|---:|---:|---|---|---:|---:|---|---|
| `(10,15,7,5)@3` | 6 | 4 | 2/3 (2; M3) | 47 (29) | 16 | **1** | A (5/14), C (2/5) | 42 (direct ν=7: U = (A) itself) | 14 | **7** | 2/5 | 3 |
| `(15,25,12,5)@3` | 5 | 3 | 1/3 (5; M3,**6**) | 2 (2) | 8 | 3 | A, C | 5100 (neutral ν_U=2 over pure-b) | 1700 | 850 | 2/5 | 1 |
| `(18,27,13,9)@5` | 6 | 4 | 2/5 (3; M5) | 37 (33) | 19 | 2 | A, C | 490 (direct ν=7 = the (35,15) cell) | 98 | 49 | 2/5 | 2 |
| `(21,35,17,7)@4` | 5 | 3 | 1/4 (5; M4,**8**) | 2 (2) | 4 | 4 | C only | 91800 (neutral ν_U=3 over pure-b) | 22950 | 11475 | 2/5 | 1 |
| `(25,35,17,5)@8` | **7** | **5** | 3/8 (4; M8) | 3 (2) | **1** | 2 | C only | 400 (direct ν=5 = (40,16)) | 50 | 25 | 2/5 | 2 |
| `(26,39,19,13)@7` | 6 | 4 | 2/7 (3; M7) | 63 (53) | 11 | 2 | A, C | 1190 (direct ν=17 = (119,35)) | 170 | 85 | 2/5 | 2 |
| `(27,45,22,9)@5` | 5 | 3 | 1/5 (5; M5,**10**) | 2 (2) | 2 | 4 | C only | 710600 (neutral ν_U=4) | 142120 | 71060 | 2/5 | 1 |
| `(34,51,25,17)@9` | 6 | 4 | 2/9 (4; M9) | 18 (17) | 7 | 3 | A, C | 7650 (direct ν=4) | 850 | 425 | 2/5 | 2 |
| `(42,63,31,21)@11` | 6 | 4 | 2/11 (4; M11) | 23 (22) | 5 | 3 | A, C | 2750 (direct ν=5) | 250 | 125 | 2/5 | 2 |
| `(50,75,37,25)@13` | 6 | 4 | 2/13 (4; M13) | 31 (30) | 2 | 3 | A, C | 41990 (direct ν=19) | 3230 | 1615 | 2/5 | 2 |
| `(58,87,43,29)@15` | 6 | 4 | 2/15 (5; M15) | 1 (1) | 3 | 3 | A, C | 13650 (direct ν=7) | 910 | 455 | 2/5 | 1F |
| `(66,99,49,33)@17` | 6 | 4 | 2/17 (5; M17) | 1 (1) | 1 | 4 | A only | 541450 (direct ν=25) | 31850 | 15925 | **5/14** | 1F |
| `(74,111,55,37)@19` | 6 | 4 | 2/19 (5; M19) | 1 (1) | 2 | 3 | C only | 116090 (direct ν=47) | 6110 | 3055 | 2/5 | 1F |
| `(82,123,61,41)@21` | 6 | 4 | 2/21 (5; M21) | 1 (1) | 1 | 4 | C only | 553350 (direct ν=31) | 26350 | 13175 | 2/5 | 1F |
| `(90,135,67,45)@23` | 6 | 4 | 2/23 (5; M23) | 1 (1) | 1 | 4 | C only | 817190 (direct ν=11) | 35530 | 17765 | 2/5 | 1F |
| `(98,147,73,49)@25` | 6 | 4 | 2/25 (5; M25) | 1 (1) | 1 | 4 | C only | 2987750 (direct ν=37) | 119510 | 59755 | 2/5 | 1F |

All 16: **PREDICTED TOWER-DEAD by the identical level-1 clash** —
verdict "ARITH-DEAD-PREDICTED", pending the UT obligations (or
per-cell certificates). Notes:

- **Difficulty classes.** 1 = hand-arithmetic decided, all-eq routes,
  ≤ 8 DAGs, UT-corollary once panel lemmas land ((15,25,12,5),
  (21,35,17,7), (27,45,22,9)); 1F = the w = 2/(2k+1) FAMILY, μ0 =
  2k+1 ∈ {15..25}: single exact-fit route each, cells
  (4μ0−2, 6μ0−3, 3μ0−2, 2μ0−1)@μ0, κ̄ = 6 — arithmetically uniform in
  μ0, ONE parametric certificate should kill all six; 2 = same
  mechanism, more realization bookkeeping (multi-DAG, one slack route,
  large route lists — all of it terminal multiplicity); 3 = one
  structurally distinct configuration to pin ((10,15): depth-1 chain-2,
  U = F1′ coincide, 18 slack routes, reading-independent).
- **The structurally-different candidates dissolve.** The 2/(2k+1)
  family is the EASIEST class, not a hard one (deep M-cascade chains ⟹
  huge products, single eq route). The four N1-biting even-ν_G cells
  ((14,21,10,7)@4 etc.) are dead upstream of the tower tier (N1, §11a)
  — not in the 16, no rounds spent. The (39,65)-class cells
  ((15,25,8,5)@7, (39,65,32,13)@7) were REMOVED by the corrected
  census (E5-required w_U ∉ closure) — none survive, nothing to roll
  out.
- **What each spine needs that (9,15)'s didn't** (per-cell deltas):
  (10,15): U = first charged vertex (H8 and the cap live on the SAME
  vertex — new configuration to state cleanly), direct M3 arrivals at
  (A), ψ-varied 47-terminal family, L-A load-bearing (18 slack routes).
  (15,25,12,5): nearest sibling of (9,15) (pure-b penultimate, neutral
  arrivals) but TWO M_U classes {3,6}. (18,27): the (35,15) cell —
  (9,15)'s TRUNK vertex — reappears as a chain-2 vertex (chart-hazard
  tripwire). (21,35)/(27,45): (C)-only depth-4 chains, dual M_U,
  neutral-only arrivals. (25,35)@8: the only κ̄ = 7 / X = 5 frame;
  single DAG (C)→(40,16); μ0 = 8 even. (26,39): heaviest route list
  (63); (119,35) = (9,15)'s F2 as arrival vertex. (34,51)/(42,63)/
  (50,75): mixed direct+neutral menus, mid-cascades. Family: parametric
  μ0 arithmetic; direct arrival cells (7,15),(25,17),(9,19)/(47,19),
  (31,21),(11,23),(37,25) from the census menus.

## 3. EXECUTION SEQUENCE

Ordering rule: information value × kill probability / cost. All 16
have ~equal (high) predicted kill probability; information value is
dominated by (i) closing the forced-ν book, (ii) validating UT
obligations on the widest structural spread, (iii) the family
parametrization.

**Probe 1 — `(10,15,7,5)@3`** (1–2 rounds). The ONLY
reading-independent cell: killing it closes the forced-ν book entirely
— td-7's tower verdict becomes H5a-independent. Also the hardest
uniformity test: depth-1 chain-2, U = F1′, largest slack-route count
(L-A load-bearing), 47-route terminal family exercising U-OB7 at full
width. If the mechanism ports here, classes 1/1F/2 are de-risked.

**Probe 2 — `(58,87,43,29)@15`** (1–2 rounds). Family representative,
built as the PARAMETRIC certificate in μ0 = 2k+1 from the start
(instantiate all six members numerically in the checker). Tests U-OB5/6
at maximal chain depth and the direct-arrival superset rider.

**Probe 3 — `(25,35,17,5)@8`** (1 round). The frame outlier (κ̄ = 7,
X = 5, even μ0, num-3 arrival state 3/8, single DAG). If the clash
survives the weirdest frame, UT generality is validated on all axes.

**Then:** UT panel engine + statement (2–3 rounds; build
`cases/tower_uniform.py` from `tower_check.py`'s reusable blocks +
L-A/L-E + U-OB2/3 + negative controls); Class-1 batch (1 round,
3 cells); Class-2 batch (2–3 rounds, 5 cells incl. the (18,27)/(26,39)
route-heavy pair); family completion via Probe-2 certificate (0–1
round). Batched hostile reviews: ONE Grok + ONE Sol round per batch
(probes; then the UT + remaining rows), plus repair rounds — the
(9,15) history (every review found a real quantifier gap) argues for
review-early on Probe 1, not review-once at the end.

**Estimated agent-rounds** (vs the (9,15) cost of ~8 incl. 4 review
cycles): probes 3–5; UT engine 2–3; batches 3–4; reviews+repairs 4–6.
**Total ≈ 12–18 rounds for all 16 cells**, vs ≥ 100 for 16 independent
(9,15)-style builds. The uniform route is ~6× cheaper and produces a
stronger artifact (one theorem + 16 checklist rows).

**`tower_check.py` generalization map** (1212 lines): reusable
UNCHANGED ≈ 40% — the check harness, exact eta-calculus, C2 td=6
calibration, the UNIVERSAL A/B/C identity blocks, N1/N4 identity forms,
the C6 negative-perturbation pattern. PARAMETRIZE: C3 window/prefix
checks (table-driven per cell), C3-V/C3-N quantifier tables (regenerate
from px5 per cell). PER-CELL only if probe-grade: C1 spine decoration,
C4 T1 rows (the two F1′ menu shapes once, panel-wide; per-cell G-vertex
rows exist via the promoted T1 law — cite, don't re-derive). DROP: C5
(LEAD-PILOT gate is a (9,15)-only fixture; no design pilot blocks exist
for other cells).

## 4. RISK REGISTER (wrong-object hazards when porting)

1. **κ̄ pin.** Three pins circulate (E5/ν_G — correct; BOOK/ν_U —
   stale px5 mixed pin; forced-ν). Tripwire at certificate load:
   κ̄ = 2d_q/(d_q−d_p) = (μ0·ν_G·w_U−2)/(μ0−1) must close, else abort.
2. **M-fold ambiguity / M_U classes.** The dedup key DROPS M_U (Sol
   finding-3 lesson). Three cells have two M_U states — (15,25,12,5):
   {3,6}; (21,35,17,7): {4,8}; (27,45,22,9): {5,10} — each raw class
   needs a REALIZED variant (§7a pure-b gcd-class analogue), and
   4-preserving pads must be covered (C3-N eligible states).
3. **Vertex identity collisions.** (35,15) is (9,15)'s trunk vertex AND
   a chain-2 vertex of (18,27)+family; (119,35) is (9,15)'s F2 AND
   (26,39)'s arrival vertex; at (10,15) the arrival vertex IS the first
   charged vertex. Frames (κ, i, chart) differ per role — never port a
   decoration row by cell-name lookup, only by position in the route.
4. **Arrival superset rider (v).** Direct-arrival lists are recorded
   along ANY in-budget path — a kill may COVER a direct arrival but
   must never RELY on its realizability; neutral classes are infinite
   (parametric ν_U) and must be closed by identity + lattice (C3-V
   style), never by instantiation lists. The engine here instantiates
   minimally — it is a probe, not a quantifier closure.
5. **Chart conventions per cell class.** PREFIX chartMode, the (R5)
   terminal chart swap, per-terminal κ-rescaling (the trunk κ-doubling
   49 vs 7 pattern recurs on every trunk variant), fiber-zero gauge
   f := f_old − a. The ψ ∈ {1,2,3,4} terminal spread within one cell's
   route list ((10,15): all four) multiplies swap opportunities.
6. **The constants 2 and 4.** gap(X)'s "2" is `deg p_{f,P1}` (chain-1
   pole, M=1) and N3's "4" is `deg p_{f,P2}` (entry M=2) — BOTH
   entry-level constants. At μ0 = 2 they coincide with μ0 and 2μ0;
   for the 16 cells they do NOT. Any ported formula containing μ0
   where a pole degree belongs is the top wrong-object candidate.
   Likewise i_G = deg p_{f,U}/μ0 (edge mult), NOT /M_U.
7. **H8/spine-tier vs tower-tier bookkeeping.** Realizations with
   non-integral stack product die at (H8) spine tier — record as
   spine-dead riders, never absorbed silently into the tower-kill
   count ((9,15) §7a discipline).
8. **L-A failure mode.** If review rejects budget-independence of the
   chain-1 freeze, the 7 cells with slack routes ((10,15) 18, (26,39)
   10, (18,27) 4, (25,35)/(34,51)/(42,63)/(50,75) 1 each) need
   per-route charged-chain-1 exhaustion. Blast radius is contained
   (charged chain-1 steps still face the w-return impossibility
   Δ−n = (n−1)(ν−1) ≥ 1) but plan the fallback.
9. **Census perimeter.** A genuinely beyond-perimeter route (charged
   step outside the filed closure, budget violation) is a §11a
   under-enumeration to FLAG, never something a tower certificate
   absorbs ((9,15) §9 discipline). §11a is not edited from here.

## 5. ANTI-STALL RULES + STATUS BOARD

Rules (binding for all rollout agents): (i) every cell carries exactly
one status from {UNTOUCHED, ARITH-DEAD-PREDICTED, CERT-BUILT,
REVIEWED-SOUND, ESCAPE-NAMED(lemma, witness)}, updated every round in
this file; (ii) no spine construction for a cell whose table row is not
green (P_min, window, census parity); (iii) any claimed escape must
name the failing obligation (L-A, U-OB2..7, N-table) plus a concrete
witness realization — "needs more work" is not a status; (iv) probes
capped at 2 rounds before a triage checkpoint; (v) reviews batched, one
hostile round per reviewer per batch; (vi) no git commits from rollout
agents; certificates land in `cases/towers/`; (vii) "untouched" never
means safe, predictions never mean killed.

Status board (2026-08-14): all 16 cells **ARITH-DEAD-PREDICTED** (this
document, §2 table). Next transition owner: Probe 1 agent.

## 6. Reproduction

```bash
cd /Users/dc/code/math/jc72108
python3 cases/tower_rollout_arith.py   # ~2 min, census parity PASS,
                                       # per-cell table + global audit
python3 cases/tower_check.py           # the promoted (9,15) baseline, exit 0
python3 cases/td7_census_e5.py         # the 17-cell census, exit 0
```

The engine enumerates realization paths with exact deg p_f transport
(deg p_{f,child} = deg p_{f,parent}·d_p/l, St 8.3(ii) + Prop 8.1(i)),
audits every gap d_q/deg p_f against the window, scans exhaustively for
empty-stack realizations at deg p_{f,U} ≤ 50, and cross-checks all 16
route counts against the §11a census before reporting. Parametric
families (pure-b ν, neutral pads, inserted cells) are instantiated at
minimal legal values — quantifier closure is certificate work (U-OB5/6),
not engine work.
