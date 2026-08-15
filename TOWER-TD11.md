# TOWER-TD11.md — entry-level clash analysis for the three td-11 entries

Status: **PROMOTED AT THE EXACT-CORE TIER; OPEN-residue campaign
through round 10 (2026-08-14): NF-Z† DIE-horn closed the two-word
deep families (§15); the 129 nested rows are CLOSED-AT-TIER — 62 by
inner-merge H8 (§16), 67 by the NF-M enumeration + the round-9
outer-merge analysis, confirmed by grok-67-final with round-10
errata folded (closed-form both-nonzero menu with its seven
`A < Q` schemas; the 109-member free-`ν_A` census, all
census-unrealizable). Remaining OPEN: beyond-core region, cap-free
closures, NF-P slice, refile (§17).**
Review chain: round 1 (window verdicts) → round 2 (obligation
discharges, 46 checks) → dual review `xmodel/grok-td11-review.md`
SOUND-WITH-ERRATA + `xmodel/sol-td11-review.md` BROKEN → round 3
(budget-9 erratum, 145-row nested layer, corollary restriction) →
`xmodel/sol-td11-rereview.md` STILL-BROKEN (one break: the false
`R <= 47` grammar law) → round 4 (exit (b): beyond-core extension
WITHDRAWN, exact-core restatement) → `xmodel/sol-td11-final.md`
(math done: exact cores CONFIRMED, OPEN inventory COMPLETE; five
editorial targets) → round 5 (this revision: §9 proof assembly, §4
M-dichotomy scope, ledger row 8 historicized, gate comments, §13.0
path-(a) scope — all reconciled to the exact-core tier).
The tier: entry packets, direct hierarchies, single-word-deep zones,
px2-menu discipline on the AUDITED REGION (budget-9 exact cores
12/10/8 below deg 94 + budget-5 closure blocks). OPEN residue:
beyond-core states, 129 nested 11-C rows, two-word deep families,
cap-free closures, `nu = 1`/resonance chains (NF-P), the Q+E5/E5F
refile. Round-3 history: The entry-tier kill is REAL and replays (both
reviews); round 3 corrects the three quantifier breaks: (1) the
OB-6 audit ran budget 5, not 9 — now a budget-9 DEGREE-AWARE cutoff
audit for all three seeds (§7.5; the `R* < p` law is retired,
ledger row 8); (2) OB-8 was not discharged on the nested 11-C
skeletons — the corrected 145-row layer is built (`145/34` exact,
old-defect `103/25` regression), 16 direct rows in-theorem, **129
nested rows OPEN** (§7.6); (3) the NF-D corollary overreached its
own perimeter — now restricted to single-word-deep zones, with the
two-word co-scaled families explicitly OPEN (§9). §10 is a per-row
census TEMPLATE with the perimeter conjunct, not an emptiness
certificate. Machine gate: `cases/tower_td11.py` (57 checks, exit
0; count printed; ~3 min — the budget-5 census blocks dominate; the
budget-9 cutoff audit itself is instant).

Consumer discipline throughout: **H8 = `P/μ` with `μ | M`** of the
current state (grok-nfd-review finding 1); every synchronization
statement below is made in that form. Sources:
`xmodel/sol-td11-13-scope.md` §§2–3 (packets, menus, port
obligations), `xmodel/sol-normalform.md` (1.4)/(2.5)/584–599 (the μ
law; the promoted 11-A `H8_EQUAL_QUOTIENT_VP_MISMATCH` row),
`TOWER-UNIFORM.md` (L-A and the td-7 apparatus), `NF-D.md` (M-drop
monotonicity D5; the co-scaling windows; the depth-cap OPEN this
document is ordered before). No git commit.

## 0. The letter-domain law (used everywhere below)

A neutral letter `nu` is legal at state weight `w = a/d` iff

```text
gcd(a, nu) = 1   and   d | nu + 1.
```

Instances: `w = 2` forces `nu` odd; `w = 3` forces `3 ∤ nu` with
parity FREE (`nu = 2` legal); `w = 3/2` forces `nu` odd AND
`3 ∤ nu`; `w = 4/3` forces `nu` odd and `nu ≡ 2 (mod 3)`. This law
re-derives every scope §3.2 neutral maximum exactly
(`(3,2;4) → 3/8`, `(4/3,3;6) → 1/5`, `(3/2,2;4) → 3/10` — gate
block 0), which is the consistency check that the domain reading is
the one the scope tables were computed under.

## 1. Entry 11-A — `(2,3): [1@2;2] + [2@3;4]`, pole top `5/2`

| item | value (exact) |
|---|---|
| chain-1 freeze | seed `(2,1)`: L-A hypotheses HOLD (merge-free `M=1`; `w=2` has no state-changing clean resonance, scope:278) — **frozen**, td-7-style |
| `gap(X)` | `(nu_X+1)/(2 nu_X) ∈ (1/2, 2/3]`, `nu_X` odd (domain law `a = 2`) |
| chain-2 menu | charged `{7/16, 2/5, 3/8, 5/14, 11/32}`; pure `<= 3/11`; neutral `<= 3/8`; resonance `5/8` |
| non-resonant window content | NONE: every non-resonant gap `< 1/2 < gap(X)` |
| **the intruder** | the zero-cost clean resonance `Delta=3, n=2, nu=2`: `w: 3→2`, `M: 2→1`, `pdeg = 8`, `dq = 5`, **`gap = 5/8`, `lambda = 0`**. In-window iff `5/8 > gap(X)` iff `nu_X > 4`, i.e. odd `nu_X >= 5`; `nu_X = 3` clears it (`2/3 > 5/8`). Padded copies `5/(8A) < 1/2` are below every X |
| **the intruder's kill (μ-robust)** | the resonance is an **M-drop** (`2 → 1`), so `μ | M = 1` forces `μ = 1` on that branch — the `μ = M` escape of grok-nfd finding 1 is CLOSED by the drop (NF-D D5: drops are irreversible). The scale is then compared raw: `v_2(8·A·B) >= 3` for every `w=3` prefix `A` and `w=2` suffix `B`, vs chain-1's `v_2(2·Pi) = 1` for every odd stack — `H8_EQUAL_QUOTIENT_VP_MISMATCH` fires on EVERY route shape (gate A4; the promoted 11-A row, now μ-checked) |
| Case-A refusal | `k = 2 nu_X` (odd `nu_X >= 3`) divides neither cap candidate `2` nor `4` — robust under the unresolved cap (see OB-5: `w=3` `P_pre` parity is unforced, so the td-7 `k|2` derivation does not port verbatim; `k|4` is the conservative joint cap and refuses Case A equally) |
| synchronized window | INHABITED under `μ = (1,2)`: `2Pi_1 = 4Pi_2/2 ⇒ Pi_1 = Pi_2` (NF-D round 2) — the clash is about real routes |
| **verdict** | **WINDOW CLEAN-CONDITIONAL**: non-resonant routes → empty prefix → Case-A refusal; resonant routes → H8-dead. Conditional on the promoted H8 row and on route realization (OB-4/OB-10) |

The 11-A dichotomy is the new structural fact: **every chain-2 route
either preserves `M` (then no gap ever reaches `1/2` and the clash
runs on an empty prefix) or drops `M` (then `μ = 1` is forced and
the `v_2` mismatch kills the synchronization)**. The scope's "next
hard td-11 object" is dead at this tier via the dichotomy: realized
routes die by H8/CAP-DEN, unrealized ones by non-realization (§7.7);
the residual realization work is the refile itself (perimeter (v)).

## 2. Entry 11-B — `(2,5): [1@3;2] + [3@4/3;6]`, pole top `7/2`

| item | value (exact) |
|---|---|
| chain-1 freeze | seed `(1@3;2)`: **NOT td-7-frozen.** L-A still gives uncharged + `M=1` propagation (its kernel is budget- and `w`-independent), but `w = 3` carries one classified state-changing clean resonance: `(n,nu) = (2,2)`, `gap 5/4`, `w: 3→2` (scope:281-283). Freeze holds MODULO that step |
| `gap(X)`, neutral | `(nu_X+1)/(2 nu_X)` over `3 ∤ nu_X` (parity free, `nu_X = 2` legal): `∈ (1/2, 3/4]`, max `3/4` at `nu_X = 2` |
| `gap(X)`, resonant | pole-adjacent resonance: `X = 5/4`; padded copies `5/(4 Pi) <= 5/8 < 3/4` lie BELOW the pole-adjacent X (scope:357-360) |
| chain-2 menu | charged `{5/22, 3/14, 7/34}`; pure `{1/5, 2/11}`; neutral `<= 1/5`; NO resonance. Max `5/22` |
| window | **EMPTY at one step**: `5/22 < 1/2 <` every X (neutral or resonant); the resonant X `5/4` also has an empty window above it (all pads `<= 3/4`, opponent `<= 5/22`) |
| Case-A refusal | `k = 2 nu_X` divides neither cap candidate `2` nor `6`, for EVERY legal `nu_X` — including even `nu_X = 2` (`k = 4`). **Load-bearing near-miss (gate X4): `nu_X = 3` WOULD give `k = 6 | 6` — a Case-A escape — and is excluded exactly by the domain law `3 ∤ nu` at `w = 3`.** The clash uses the letter domain, not just the gap order |
| synchronized window | inhabited under `μ = (1,3)`: `Pi_1 = Pi_2` |
| **verdict** | **WINDOW EMPTY** (one-step tier). The type-`(2,5)` packet (`(k_0,l_0)`, `alpha_1`, pole exponents) and its prefix exhaustion are OB-1/OB-7 — genuinely new, not portable from type `(2,3)` |

## 3. Entry 11-C — `(2,3): [1@2;2] + 2×[2@3/2;4]`, pole top `5/2`

| item | value (exact) |
|---|---|
| chain-1 freeze | identical seed `(2,1)` to td-7/11-A: **L-A ports verbatim** (strict `w=2` freeze) |
| `gap(X)` | `(nu_X+1)/(2 nu_X) ∈ (1/2, 2/3]`, `nu_X` odd |
| chain-2 menus (×2) | BOTH opponents are the exact td-7 chain-2 seed `(3/2,2;4)`: charged `{2/5, 5/14}` (= the td-7 first-charged gaps), pure/neutral `<= 3/10`; no resonance |
| window | **EMPTY at both leaves**: max `2/5 < 1/2 < gap(X)` — exact td-7 local pairs |
| sibling structure | second opponent has the same menu, so every sibling gap `<= 2/5 < gap(X)`: the attached-vertex hypothesis of the local-to-global inheritance conjecture (scope:191-196) HOLDS arithmetically. No second `M=1` carrier ⇒ no 13-4-style sibling-X tie |
| cap | chain-2 is td-7's seed with the SAME domain law (odd AND `3 ∤ nu` at `w = 3/2`), so the td-7 N2/N3 joint-cap derivation `k | 2` carries; Case A refused (`2 nu_X ∤ 2`) |
| synchronized window | inhabited under `μ = (1,2)`: `Pi_1 = Pi_2` (either opponent) |
| **verdict** | **WINDOW EMPTY** (leaf one-step tier). The 145-row three-pole skeleton (direct AND nested orders) is where the risk lives: an inner merge before the candidate clash can change the seed states. Composition is OB-8 |

## 4. What the corrected μ-discipline changed

* **It made all three clashes non-vacuous.** Under the round-1 raw-`P`
  misreading the td-11 synchronized windows were "empty" and every
  clash statement would have been about nothing. Under `P/μ` the
  windows are inhabited (`Pi_1 = Pi_2` co-scaling, NF-D round 2), so
  an entry-clash theorem here kills REAL route families.
* **It did not resurrect the 11-A intruder.** The one place the
  μ-correction could have re-opened a kill, it does the opposite:
  the `5/8` resonance drops `M` to `1`, and `μ | M` then FORCES the
  raw comparison the promoted certificate uses. The NF-D D5
  monotonicity (M-drops irreversible) is exactly why no later step
  can restore the `μ = M` escape.
* **The M-drop dichotomy is the organizing principle** (gate X2):
  on the audited region (the exact cores and budget-5 closures),
  M-preserving routes never produce a gap `>= 1/2`, and M-dropping
  routes die on `v_2`. This is the td-11 analogue of td-7's "pure
  `n=1` clean neutrals forced" step — scoped, like every window
  statement here, to the audited region (§7.5).

## 5. The NF-D byproduct (why this came before NF-P)

NF-D round 2 left td-11 depth OPEN: the synchronized windows are
infinite (`Pi = 5^k` at every depth) and no mechanism-A pin exists.
The entry-clash theorem closes the SINGLE-WORD-DEEP slice of that
question (round-4 wording, matching the §9 corollary): a neutral
word whose depth keeps the deep zone single-word extends a spine
whose X-death is refused in every case above, so those words die
with the spine — no depth cap needed on that slice, and the
depth/census circularity is broken there. Deep co-scaled families
with sub-`theta*` tails on BOTH chains are two-word deep-zone
objects: OPEN (POLICY NF-Z-dagger), exactly as `cases/nfd_check.py`
still reports.

## 6. The td-11 entry-clash theorem: statement prospect and obligations

**PROSPECT (round-1 text, kept as history; the round-3 theorem at its audited tier is §9).** *For each of 11-A, 11-B, 11-C: no
global approximate-root ladder is compatible with any synchronized
route. The forced death gaps put the chain-1 pole-adjacent vertex X
above every opponent gap, the prefix menu in the window
`(gap(X), pole top)` is empty (11-B, 11-C) or H8-dead (11-A's
`5/8`), and the X-death step `k = 2 nu_X` is refused by the joint
cap for every domain-legal `nu_X`.* — The analogue of the td-7
`tower.obstruction` statement, per-entry.

Obligations to promotion (numbered against scope §2.3; round 1
listed them — round 2 discharges each in §7, as indicated):

* **OB-1 (packets):** derive `(k_0, l_0)`, `alpha_1`, pole top, and
  all full pole exponents for each entry — in particular the
  type-`(2,5)` packet for 11-B. Do not infer from type `(2,3)`.
* **OB-4 (H8 stacks):** prove the synchronized stack products
  integral and characterize nonemptiness per route under `P/μ`; the
  co-scaling windows above are the round-2 NF-D objects.
* **OB-5 (caps):** derive each entry's actual joint cap
  (`k | gcd(pdeg_P, i_first·P_pre)` shape). 11-A's `w=3` side does
  NOT force `P_pre` odd, so td-7's `k|2` may weaken to `k|4` — Case
  A survives both, but the Case-C prefix grid depends on it.
* **OB-6 (global window):** bound charged predecessor strata,
  state-changing descendants, inner merges, pads/E5F reroutes,
  trunks, terminals — the full TOWER-UNIFORM perimeter, per entry.
* **OB-7 (prefix exhaustion):** recompute the A/B/C-analogue
  exhaustion from each entry's `alpha_1`, cap, and window (new for
  type `(2,5)`; the 11-A/11-C grids should port modulo OB-5).
* **OB-8 (composition):** 11-C's three-pole direct AND nested
  orders (145-row skeleton); prove the local-to-global inheritance
  whose arithmetic hypothesis is verified here.
* **OB-10 (E5F/realization):** whether a completed Q+E5/E5F route
  realizes each X/opponent pair (scope's first refile question for
  11-A); E5F is not applicable until the merge arrival frames are
  chosen.

Round 2 discharges these as follows (§7); the theorem is §9.

## 7. Obligation discharges (round 2, machine blocks 6–12)

### 7.1 OB-1: packets, derived not inferred (gate block 6)

**Packet law.** The pole pattern `(t−A)^α (t−B)^β` gives the P1
scale relation `m^α = σ0·λ^β`, i.e. the pole death step
`(k_0, l_0) = (α, β)`; `g_top = (α+β)/α`; Z1 gives
`alpha_1 = l_0 + 1 − g_top = β(α−1)/α`. Regression: type `(2,3)`
reproduces the promoted td-7 packet EXACTLY (`(2,3)`, `5/2`, `3/2` —
`t9_15_direct.json`'s `m^2 = σ0 λ^3`, `alpha 3/2`). The NEW type
`(2,5)` packet (11-B): `(k_0, l_0) = (2, 5)`, `g_top = 7/2`,
**`alpha_1 = 5/2`**. Pole full degrees per scope §3.1: 11-A `(2,4)`,
11-B `(2,6)`, 11-C `(2,4,4)`; the X-side pole is `(t−A)^2` in all
three (type `(2,x)`), so `i_X = 2`. `den(alpha_1) = 2` divides every
cap candidate (entry compatibility).

### 7.2 OB-4: H8 stacks under `P/μ` (gate block 7)

Stack products are integers; the empty stack passes on all three
entries (`2/1 = 4/2 = 6/3`); `Pi = 5^k` passes at every depth — the
synchronized windows are INHABITED and the theorem is about real
routes. Characterization of the common `Pi`: odd and `3`-free
(11-A/11-C; both sides' domains), plus side-2 factorability at 11-B
(`25 = 5·5`, `35` as the single letter `35 ≡ 2 (mod 3)`). The
`μ = (1,1)` branches stay unsat (raw-`P` valuations, NF-D round 2),
and a FAILED synchronization is spine-death (scope port obligation 4:
no H8 match, no X) — either way no escape.

### 7.3 OB-5: joint caps, covered conservatively (gate block 8)

X-side: X lives at the `(t−A)^2` power (`i_X = 2`, all three
entries), giving the td-7-style `k | 2` while X is alive
(Prop 4.2(iii)/Prop 8.1 — CITED, not reproved). Because that citation
is a port, the exhaustion below does NOT depend on it: it runs over
the conservative chain-2-side candidates
`{2,4}` (11-A: `gcd(4, i·P_pre)`, `i ∈ {2,4}`, `P_pre` parity FREE —
`nu = 2` is legal at `w = 3`, so even `P_pre` is realized),
`{2,6}` (11-B: `gcd(6, i·P_pre)`, `i ∈ {2,6}`, `P_pre` odd and
`3`-free), `{2}` (11-C: td-7 derivation ports with the seed), PLUS
the divisor closure `{1}` (a third pole can only shrink the cap).

### 7.4 OB-7: the den-criterion prefix exhaustion (gate block 9)

**α-lattice lemma.** `den(alpha_1) | c`, and every prefix step with
`k | c` keeps `den(alpha) | c` (`alpha_next = alpha + l(k−1)/k`). So
the exhaustion may quantify over the FULL lattice `alpha ≡ a/c` — a
SUPERSET of the reachable registers — which makes it
**menu-independent**: no first-charge menu derivation is needed for
the kill, only the cap.

**Criterion.** The X-death step is FORCED to
`k_m = den(alpha_m − 1 + gap(X))`; it is legal iff `k_m | c`.

**Lemma CAP-DEN (the ν-quantifier closes algebraically).** With
`gap(X) = (ν+1)/(2ν)`: `num = 2aν + c(1−ν) ≡ c (mod ν)`, so
`den | c` forces `ν | c²`. Odd `ν >= 3` divides none of
`{1, 4, 16, 36}` (after the 11-B domain removes `3` and `9`); the
residual 11-B cases `ν ∈ {2, 4}` refuse 2-adically
(`(2a−3)/12`, `(4a−9)/24`, `(2a−1)/4`, `(4a−3)/8` — denominators in
`{4, 8, 12, 24}`, none dividing `6` or `2`), and the 11-B resonant X
`5/4` gives `(2a+3)/12`-type values, same refusal. Gate block 9
sweeps every entry × every cap candidate × every register residue ×
every domain-legal X (`ν <= 300` lattice + `5/4`): **zero escapes.**
Case A is the `alpha_1` instance; Case B is refused by gap order +
the promoted no-skip descent law (cited); Case C is the full lattice.
td-7 regression: the criterion reproduces the promoted Case C
verbatim (`k=1` forces `2ν | rν+1`, `k=2` forces `ν | 1`).

### 7.5 OB-6: multistep window audit — **CORRECTED IN ROUND 3**
(gate blocks 10 + 14; sol/grok finding 1 folded)

**Erratum accepted.** The round-2 audit ran `px5.close_with_cells`
at its DEFAULT budget 5 (td-7's `td−2`), not td-11's gross budget 9;
`21 + 347 + 69` are budget-5 counts, and perimeter clause (iii)
claimed the opposite. Additionally the round-2 "ratio law
`R* < p`" is **RETIRED** — falsified at budget 9 by Sol's reachable
path `(3,2) → deg 40 → deg 400 at (3/4,8)` carrying a step of ratio
`9·8/18 = 4 = p` (its gap is `4/400 = 1/100`, so it is not a window
escape — but the law as stated was false; the audit must be
degree-aware).

**The round-4 EXACT-CORE audit (gate B9d, runs inline).** A Dijkstra
over actual degrees at budget 9, for ALL THREE seeds: exact menu
checks for every state first reached at `deg <= 94` — cores of 12,
10, 8 states, **zero gaps `>= 1/2` beyond 11-A's seed-level `5/8`**,
parsed ratio maxima `5/2, 5/2, 7/3` (re-review-confirmed).

**The beyond-core extension is WITHDRAWN (round 4).** Round 3
claimed every deeper state safe via a universal grammar bound
`R <= 47 = 1 + k_max + lex_max`. That law governs only the DIRTY
branch (`px2.py:77-125`); the CLEAN branch (`px2.py:45-60`) has
`R_clean = dq/nu = 1 + Delta/nu` with `Delta | num(w)` — the
identity `n·nu + 1 = Delta + nu` (gate B9f) — which is UNBOUNDED as
`num(w)` grows: the abstract grammar row `(95,1) -> clean D95n48nu2`
has `R = 97/2 > 47` (sol-td11-rereview finding 1, replayed). Since
dirty/pure-b transitions can grow numerators
(`w' = l·w·(1+k+lex)/E`), a hereditary beyond-core safety argument
needs a reachable-state invariant relating `num(w)` and degree —
exactly the unfinished closure question. No such invariant is proved,
so states first reached above deg 94 are **OPEN**, joining the
residue of §12. (Frozen sizing record, gate B9b: `(3,2)` ladder
`21/56/130/330/743` matching the sol-review; `(3/2,2)`
`69/162/349/785` at budgets 5–8 with ~10× time growth per unit;
`(4/3,3)` `347` at budget 5; full budget-9 closures of the latter
two are session-infeasible.)

**Honesty rider (gate B9e):** the exact-core audit is a
**px2-MENU-SLICE** statement — the engine inherits td-7's
`k <= 6, lex <= 40` loop caps, which the scope forbids a production
compiler to inherit; `47` caps the dirty branch only. Both the caps
and the beyond-core region are compiler-gap items (§13), stated, not
hidden. The budget-5 blocks (round-2 gate block 10: growth `>= 2`,
resonance censuses, chain-1 menus at `(2,1)`/`(3,1)`) remain valid
budget-5-slice facts.

### 7.6 OB-8: three-pole composition, 11-C (gate blocks 11 + 13) —
**PARTIAL: direct orders only (round 3; sol finding 2 folded)**

Round 3 builds the corrected decorated skeleton layer with the
μ-independence law (an inner merge keeps its emitted `M_child`; the
next edge independently chooses `μ_e | M_child` — the documented
`expand` defect repaired). It reproduces the scope/sol diagnostic
EXACTLY: `16 + 40 + 40 + 49 = 145` decorated rows, mixed-node rows
`0 + 8 + 8 + 18 = 34`; and the old-defect law reproduces the
checked-in `103/25` (gate SK1/SK2 — both regressions).

* **The 16 direct rows are in-theorem**, each with a per-row verdict:
  `μ = 1` on a B-edge makes that pair's `P/μ` equalization unsat
  (`Pi_A = 2·Pi_B`, `v_2` 0 vs `>= 1`) — H8 spine-death; `μ =
  (1,2,2)` gives the co-scaled inhabited window — CLASH-dead by
  CAP-DEN (the second opponent adds no window step, menu max
  `2/5 < 1/2 < gap(X)`, and only shrinks the joint cap; the
  exhaustion is divisor-closed and dynamic-cap-checked, so every
  shrunk cap and register class is covered). No sibling-X tie
  (leaf M-vector `(1,2,2)`: exactly one `M = 1` carrier).
* **The 129 nested rows were OPEN at round 3** — stamped so by the
  gate classifier (SK3), never `TOWER-DEAD` at that tier. (Rounds
  6–10 subsequently closed them: 62 by inner-merge H8, 67 by the
  NF-M enumeration + outer-merge analysis — §17 and NF-M.md §5;
  SK3's OPEN stamp remains the correct ROUND-3 record and the
  correct behaviour for any decoration outside the audited class.) Two distinct reasons:
  `G(G(A,B1),B2)` / `G(G(A,B2),B1)` put the clash inside an inner
  merge with a rootward sibling (the nested-TERM gap, port
  obligation 11); `G(G(B1,B2),A)` makes the opponent a merged chart
  whose post-merge menu is NF-M-gated. The 34 mixed-node rows
  (`all μ_e >= 2` at some node) are Sol's concrete printed-tier
  witnesses, e.g. `Gout(Gin(B1,B2),A)` with `M_in = 4 | (2+2)`,
  `μ(inner) = 2`, `M_out = 3 | (2+1)`.

OB-8 is therefore NOT fully discharged: the theorem's 11-C quantifier
is the direct hierarchy (16/145 rows); nested composition needs a
global-ladder restriction lemma or per-order first-death enumeration
(§13).

### 7.7 OB-10: E5F / realization (gate block 12)

The kill is E5F-input-free. Dichotomy: a Q+E5/E5F-realized
X/opponent pair dies by the cap exhaustion (§7.4) or the H8 `v_2`
mismatch (§8); an unrealized pair is dead by non-realization. Either
horn gives emptiness. The E5F base law
(`n = ν_U·kbar_G − ν_G·kbar_U >= 1`) is td-agnostic (scope §2.1) and
only shrinks the realized set; no td-7 offset formula is imported.

## 8. Lemma 11A-RES (the entry-specific intruder kill, μ-robust)

*The `5/8` resonance route of 11-A — the ONLY object in any td-11
clash window — is H8-dead on every route shape.* Proof: the
resonance (`Δ=3, n=2, ν=2`, `w: 3→2`, `M: 2→1`, `pdeg 8`, `λ=0`) is
an **M-drop**, so `μ | M' = 1` forces `μ = 1` on that branch — the
grok-nfd-finding-1 `μ = M` escape does not exist there, and by NF-D
D5 (drops irreversible) no later step restores it. The comparison is
therefore raw: `v_2(8·A·B) >= 3` for every `w=3` prefix stack `A`
and `w=2` suffix stack `B`, against chain-1's `v_2(2·Pi) = 1` for
every odd stack — `H8_EQUAL_QUOTIENT_VP_MISMATCH`
(`sol-normalform.md:584–599`, promoted) fires always. Padded copies
of the resonance (`5/(8A) < 1/2`) never re-enter any window. ∎
(gate blocks 1, 2/A4)

## 9. Theorem TD11-CLASH

**Theorem (round-3 tier: entry packets, DIRECT hierarchies,
single-word-deep zones, px2-menu window discipline, within the
corrected §12 perimeter).** *For each td-11 L6-surviving entry
`E ∈ {11-A, 11-B, 11-C}` with its derived packet (§7.1), restricted
to the direct hierarchies (11-A, 11-B binary; 11-C's 16 direct
decorated rows of §7.6) and to configurations whose deep zone is
single-word: every synchronized configuration — `μ`-assignments in
the AUDITED CLASS (the direct decorated rows of §7.6, read through
§10(b); the §7.7 current-state witnesses are exercised examples, not
a proved class — sol-rereview finding 2), every stack `Pi` in the
co-scaling window, every E5F-admissible realization — dies at the
tower tier. Explicitly: the global
ladder's death order reaches the entry's pole-adjacent X (neutral
`gap(X) = (ν_X+1)/(2ν_X)` over the domain-legal `ν_X >= 2` — the
X-interval `(1/2, 2/3]` / `(1/2, 3/4]`, which excludes `ν = 1` — or
11-B's resonant `X = 5/4`) with every competing object below `1/2`
(§7.5, the budget-9 EXACT-CORE audit plus budget-5 closure blocks on
the px2-menu slice — competing objects beyond the audited region are
OPEN, not covered); and the
X-death step is REFUSED — `den(alpha_m − 1 + gap(X))` divides no
cap candidate for any lattice register `alpha_m`, including the
dynamic-cap register classes (§7.4, Lemma CAP-DEN + OB7f) — while
the sole in-window intruder (11-A's `5/8`) is H8-dead (Lemma
11A-RES) and non-synchronized routes are spine-dead (§7.2).
Configurations extending such a spine by a neutral word whose depth
keeps the deep zone single-word — in particular every single-tail
truncation of the `Pi = 5^k` family — die with it.*

Per-entry constants:

| entry | packet `(k_0,l_0)`, `alpha_1`, `g_top` | cap candidates | X family | intruder |
|---|---|---|---|---|
| 11-A | `(2,3)`, `3/2`, `5/2` | `{1,2,4}` | `(ν+1)/(2ν)`, `ν` odd | `5/8` — dead (Lemma 11A-RES) |
| 11-B | `(2,5)`, `5/2`, `7/2` | `{1,2,6}` | `(ν+1)/(2ν)`, `3∤ν` (even `ν` legal); resonant `5/4` | none |
| 11-C | `(2,3)`, `3/2`, `5/2` | `{1,2}` | `(ν+1)/(2ν)`, `ν` odd | none |

*Proof assembly:* §7.1 (packets) + §7.2 (synchronization dichotomy)
+ §7.5 (no competing object at or above `1/2` on the EXACT CORE —
the audited states, 12/10/8 below deg 94, plus the budget-5 closure
blocks; competing objects beyond the audited region are OPEN — so X
is reached in gap order with at most cap-legal prefixes there; Case
B refused by descent) + §7.4 (X-death refused over
the full register lattice under every cap candidate — Cases A and C)
+ §8 (the intruder) + §7.6 (third pole only shrinks caps, adds no
window step) + §7.7 (realization dichotomy). ∎ within §12.

**Corollary (NF-D closure for td-11 — RESTRICTED to the §12
perimeter, round 3; sol finding 3 folded).** *For every synchronized
configuration whose deep zone (below `theta*`) is SINGLE-WORD, of any
depth, the clash kills the spine and the word with it.* The unbounded
co-scaled families (`Pi = 5^k` on BOTH poles at large `k`) eventually
have sub-`theta*` tails on both chains simultaneously — that is
multi-word deep-zone coexistence, which is POLICY NF-Z† and perimeter
clause (ii): **excluded, OPEN, not closed by this corollary.** The
td-11 NF-D depth question remains OPEN exactly on that two-word
slice (as `cases/nfd_check.py` continues to print). Remark: the
X-refusal argument itself never reads the deep zone (all deep deaths
occur after X in gap order), so a future cross-branch decoupling
lemma for two-word deep zones would lift the restriction verbatim;
until it exists, Rule 6 applies. Shallow co-scaled pairs (at most one
tail below `theta*`) ARE covered. The depth/census circularity is
broken on the single-word-deep slice without a depth cap.
**Round-6 amendment:** the restriction is LIFTED for the td-11
synchronized pure-neutral class — NF-Z† instantiated on its DIE horn
(§15) shows every cross-branch coupling event lies strictly below
the refused X, so the two-word families die at X with everything
else; the cross-branch decoupling lemma this paragraph anticipated
turned out to be unnecessary FOR CLASHED ENTRIES (it remains the
open object for entries without an entry-level kill).

## 10. Census template (round 3 — NOT an emptiness certificate; grok
finding 2 / sol finding 4 folded)

The td-11 census does not exist (the Q+E5/E5F refile is UNKNOWN in
the scope), so nothing here certifies an unenumerated book. What the
eventual compiler consumes is a **per-row classifier template**, and
its condition has THREE conjuncts:

```text
stamp TOWER-DEAD(entry id, packet constants, cap candidate,
                 CAP-DEN instance or Lemma 11A-RES or spine-death)
  IFF  (a) the row maps to one of the three entry packets, AND
       (b) the row's hierarchy/decoration is in the audited class
           (11-A, 11-B binary; 11-C direct — the 16 rows of SK3), AND
       (c) the configuration is inside the corrected §12 perimeter
           (single-word-deep, px2-menu window discipline, no nu = 1,
           no resonance-bearing chain, budget within the audited
           horizon);
  ELSE stamp OPEN (Rule 6) — in particular ALL 129 nested 11-C rows,
       every multi-word-deep configuration, and every row that fails
       to map.
```

The gate implements conjuncts (a)/(b) — the hierarchy and direct-`μ`
split — on the 145-row layer and verifies the classifier never
stamps a nested row dead (SK3). Conjunct (c) is a REQUIRED FUTURE
COMPILER PRECONDITION, not something the current gate enforces:
SK3's row carries no fields for deep-zone multiplicity, menu
horizon, budget, resonance, mapping, or refile status
(sol-rereview finding 5). Conjunct (c) is what the round-2 text
omitted; a compiler implementing the round-2 sentence would have
stamped nested rows §12 forbids. The mapping
claim in (a) is a per-row check, not a theorem — a future compiler
can emit decorations that are labelled 11-C and are not in the
audited class; those fall to (b)'s OPEN.

## 11. Near-miss ledger (where a hostile reviewer should push)

| # | near-miss | what saves it | gate row |
|---|---|---|---|
| 1 | 11-B, `ν_X = 3`, cap `6`: `k = 2ν_X = 6 | 6` — a genuine Case-A escape | the domain law `3 ∤ ν` at `w = 3` excludes `ν_X = 3` EXACTLY | X4 |
| 2 | 11-B, `ν_X = 2`, cap `6`: `ν | c²` (Lemma CAP-DEN's necessary condition) PASSES | the 2-adic part: `den((2a−3)/12) ∈ {4,12}`, never `| 6` | OB7c |
| 3 | 11-A, cap `4`: the prefix menu is NONEMPTY (`k = 4` rows exist arithmetically, unlike td-7's `k|2` menu) | the exhaustion is menu-independent (α-lattice superset); every lattice register still refuses X | OB7a/b |
| 4 | 11-A, `ν_X = 3`: the `5/8` intruder is NOT in the window (`2/3 > 5/8`) — the kill must not cite Lemma 11A-RES there | it doesn't: `ν_X = 3` dies by CAP-DEN directly (`3 ∤ 16`) | OB7b/c |
| 5 | **(round 3, found by our own sweep)** quarter-register `3/4` vs the `ν = 2` gap `3/4` under cap `2`: `r = 1/2`, `k = 2 \| 2` — a genuine Case-C escape shape | no entry realizes the cell: 11-A's `w = 2` domain forbids even `ν_X`; 11-B's cap set `{1,2,6}` contains no `4`, so no quarter-lattice register exists there. The dynamic-cap lemma is sound ONLY entry-paired | OB7g |
| 6 | `(c, ν) = (4, 2)`: `ν \| c²` and the den test passes shapes | 11-A domain (odd `ν` at `w = 2`); 11-B has no cap 4 (grok finding 7) | OB7b |
| 7 | `ν_X = 1`: `gap = 1`, `r = 3/2 − 1 + 1 = 3/2`, `k = 2` divides every even cap — a Case-A escape shape | `gap = 1` lies outside every X-interval (`(1/2, 2/3]` / `(1/2, 3/4]`); `ν = 1` insertions are NF-P (§12(iv)). The theorem line now says `ν_X >= 2` explicitly (grok finding 5) | — |
| 8 | budget-9 state `(3/4, 8)` carries a step of ratio `4 = p` (Sol's path), falsifying the round-2 `R* < p` law | historical: round 3 replaced the ratio law with a degree-aware cutoff whose `47` grammar bound row 9 then REFUTED; what survives is the state's arithmetic (min reachable degree `400` ⇒ gap `1/100`) and the exact-core audit, which checks such states exactly or leaves them OPEN | B9c/B9d |

| 9 | **(round 4)** the beyond-core cutoff's `R <= 47` law: the clean branch has `R = 1 + Delta/nu`, `Delta \| num(w)` — abstract grammar row `(95,1) -> D95n48nu2`, `R = 97/2 > 47` | no rescue claimed: the bound was FALSE as a grammar law; the extension is withdrawn and the beyond-core region is OPEN pending a reachable-numerator invariant (`num(w)` vs deg) or a cap-free closure | B9f |

These nine exclusions are exact and each is one arithmetic fact away
from an escape; they are the load-bearing edges of the theorem. Row 5
was found by our own round-3 sweep; row 9 by Sol's re-review, and it
COST the theorem its beyond-core region rather than being excluded —
the one entry in this ledger that is a withdrawal, not a defense.

## 12. Perimeter honesty (machine-checked vs law-covered)

**Machine-checked (round-3 gate, 57 rows; the literal-`True` rows of
round 2 are replaced or [CITED]-labelled per grok finding 3):** the
domain law against the scope menus; the window arithmetic; packet
derivations with td-7 regression; H8 windows under `P/μ` (inhabited +
unsat branches) including Sol's two current-state stress witnesses;
cap candidates including realized even `P_pre` at 11-A; the α-lattice
lemma, the full den-criterion exhaustion (every cap × residue ×
domain-legal X, algebraic ν-closure), the entry-paired dynamic-cap
register classes, and the row-5 near-miss; the budget-5 closure
blocks (relabelled as budget-5-slice facts); the budget-9
degree-aware cutoff audit for all three seeds with the grammar-cap
verification; the corrected M′ law (`gcd(l, dq)`); the 145-row
skeleton layer with both regressions (`145/34` corrected, `103/25`
old-defect) and the per-row classifier; Lemma 11A-RES's `v_2`
computation over domain stacks.

**Law-covered (cited promoted results, not re-proved here):** the
ladder calculus itself (delta descent, no-skip, death equations, Z1);
the L-A kernel; Prop 4.2(iii)/8.1 for the X-side `k | 2` (the
exhaustion is robust to its failure via the conservative caps); the
promoted `H8_EQUAL_QUOTIENT_VP_MISMATCH` certificate; the E5F base
law; px2's menu completeness per state ON ITS OWN GRAMMAR (the same
trust td-7's book stands on — see clause (iii)).

**Perimeter clauses (outside the theorem, Rule 6 on their slice):**
(i) the 129 NESTED 11-C rows (SK3 stamps them OPEN; the two nested
flavors and the 34 mixed-node rows are enumerated, not audited);
(ii) multi-word deep-zone coexistence (POLICY NF-Z†; the §9
corollary is restricted accordingly); (iii) the engine horizon: all
multistep statements are px2-MENU-SLICE statements (`k <= 6`,
`lex <= 40` inherited caps); the budget-9 audit covers the EXACT
CORES ONLY (12/10/8 states below deg 94) — the beyond-core region is
OPEN (round-4 withdrawal, ledger row 9); budget-5 closures back the
census blocks; full budget-9 closures of `(3/2,2)` and `(4/3,3)` are
session-infeasible — sized, recorded;
(iv) `nu = 1` insertions and resonance-bearing chains stay NF-P's;
(v) the Q+E5/E5F refile itself (scope: UNKNOWN). A configuration
reaching any clause is reported OPEN, never certified.

### 13.0 What would restore the withdrawn beyond-core region

Either (a) a **reachable-numerator invariant, correctly scoped**:
prove that every state FIRST REACHED BEYOND degree 94 (the exact
core and the seed are excluded — the invariant is FALSE at the seed
`(3,2)` itself, where `num(w) = 3` against degree `4` and the `5/8`
is the audited exception) satisfies `1 + num(w)/2 < deg/2`, i.e.
`num(w) < deg − 2` (the empirical facts — `num(w) <= 6` on the full
`(3,2)@9` closure, parsed clean ratios `<= 7/2` — say this is TRUE
there; what is missing is a proof that dirty/pure-b numerator growth
`w' = l·w·(1+k+lex)/E` cannot outrun degree growth `dp/l` on
reachable paths past the core); or (b) the **cap-free
shared-budget-9 closure** the scope demands anyway, which makes the
question empirical per state. Both are compiler-tier items; neither
is claimed here.

## 13. What td-13 needs (forward pointer)

The same apparatus ports to five of six td-13 entries (max-X empty
windows per scope §3.3) with new constants: a `k | 3` exhaustion
lattice for 13-2d (type `(3,4)`: pole `(t−A)^3`, so the α-lattice
runs mod `3`-caps and CAP-DEN's `ν | c²` changes base), max-X
relabelling + tie handling for 13-3/13-4 (sibling-X ties are REAL
there — the carve-out here), and the all-off-axis 13-2b, which has
NO L-A carrier and a genuinely inhabited menu window
(`3/10 < 2/5 < 5/2`) — the scope's designated architecture test. The
th td-13 analogue of Lemma 11A-RES will need the `7/16`-family
intruders of the `(3,2;4)`-type seeds classified per entry.

## 14. Reproduction

```bash
python3 cases/tower_td11.py    # 66 checks, exit 0 (count printed; ~3 min,
                               # the budget-5 (4/3,3) closure dominates)
```

Blocks: 0 domain law vs scope §3.2; 1 resonance identities (round-3
M′ = gcd(l, dq) fix); 2–4 the per-entry round-1 window verdicts
(B1 de-tautologized); 5 cross-entry μ-discipline and the NF-D
byproduct; 6 OB-1 packets; 7 OB-4 H8 windows; 8 OB-5 caps; 9 OB-7
den-criterion exhaustion (α-lattice lemma, full sweep, CAP-DEN
algebra, td-7 regression, Case-B gap dominance, entry-paired
dynamic-cap classes OB7f, ledger row 5 OB7g); 10 OB-6 budget-5
census blocks (relabelled); 11 OB-8 direct-only composition; 12
OB-10 with Sol's two current-state stress witnesses; 13 the
corrected 145-row skeleton layer + per-row classifier (SK1–SK3); 14
the budget-9 record: erratum, frozen sizing ladders, R*-law
retirement, the inline EXACT-CORE audit (B9d), the clean-branch
ratio law + Sol's counterexample and the beyond-core withdrawal
(B9f), grammar-cap rider (B9e); 15 the theorem aggregate at the
exact-core tier (b9 conjuncted) + the not-claimed list including the
beyond-core region; 16 NF-Z-dagger instantiated (coupling census,
resonance dispatch, coupled-cap divisor completion incl. c = 3,
monotonicity, DIE-horn verdict, finiteness honesty); 17 the nested
129 after inner-H8 stamping (62 dead / 67 open). Companion gates unchanged:
`cases/nfd_check.py` (22), `cases/nfz_check.py` (39),
`cases/tower_check.py` (promoted td-7 book). No git commit.

## 15. NF-Z† instantiated for td-11 (round 6): the DIE horn

NF-Z.md §6 defines NF-Z† as a fail-closed POLICY on multi-word
deep-zone coexistence: a deep death on one word must keep the other
words' deep vertices alive (`k'` dividing their nested-product
exponents; cross-branch gcds not automatic), and no general finite
check was ever defined (the round-2 `c_x` sketch was withdrawn as
not-an-algorithm). The td-11 instantiation below is the **DIE
horn** of "decouple-or-die": it proves the coupling never gets to
act, because the entry-level clash kills first.

**The per-entry finite check (gate block 16):**

1. **Coupling census (DG1).** Enumerate every `(chain, depth,
   letter-class)` whose gap can reach `1/2`: the max gap of a
   depth-`d` neutral letter is `(u_min+1)/(P_0·u_min^d)`, which at
   least halves per depth — so the enumeration is FINITE (this is
   the load-bearing finiteness step, and it is entry-conditional:
   it works because the comparison point `1/2 < gap(X)` exists).
   Result: the ONLY objects at gap `>= 1/2` anywhere are the
   depth-1 chain-1 letters — X itself. Opponent-chain maxima:
   `3/8` (11-A), `1/5` (11-B), `3/10` (11-C).
2. **Dispatch of the above-1/2 non-X objects (DG2).** 11-A's `5/8`
   resonance: H8-dead (Lemma 11A-RES). 11-B's `5/4`: it IS the
   resonant X, refused in the sweep. Padded copies `< 1/2`.
3. **Coupled-cap divisor completion (DG3 — the dagger's own
   find).** Cross-branch coupling shrinks caps to `gcd(c, e) | c`;
   the refusal sweep must therefore be divisor-complete. Divisors
   of 6 include `3`, which rounds 2–5 never swept: swept now on
   both candidate register lattices (third and sixth) — zero
   escapes (CAP-DEN: `3`-free `ν | 9` is empty; resonant `5/4` dens
   `{4,12} ∤ 3`). The refusal set is now `{1,2,4} / {1,2,3,6} /
   {1,2}`.
4. **Monotonicity (DG4).** Extra alive deep vertices only shrink
   the cap (gcd) and only remove prefix steps (the exhaustion is
   already menu-independent over the full α-lattice), so the
   X-refusal is monotone under coupling.

**VERDICT (DG5): PASS on all three entries.** Every multi-word
synchronized neutral configuration — including the both-tails-deep
`Pi = 5^k` families — dies at X before any cross-branch coupling
event. Decouple-or-die resolves as DIE; the two-word OPEN item
CLOSES for this class, and the §9 corollary restriction is lifted
(round-6 amendment there).

**Finiteness honesty (DG6).** This check is finite BECAUSE the kill
precedes all coupling. The general NF-Z† — for entries where live
configurations would actually reach deep deaths — still has no
algorithm; NF-Z.md §6's definition gap stands (flagged there,
round-6 addendum). No general repair is claimed.

## 16. The nested 129 after inner-merge H8 stamping (round 6)

The per-node ledger discipline (scope port obligation 4: "Nested
merges require a ledger at every node") lets the promoted
equal-quotient consumer run at every POLE-POLE merge — the same
arithmetic as the direct rows, no new law. Applied to the corrected
145-row layer (gate block 17):

| hierarchy | rows | inner-H8 SPINE-DEAD | still OPEN |
|---|---:|---:|---:|
| `G(G(A,B1),B2)` | 40 | 20 (inner `μ_B = 1`: `v_2` 1 vs 2) | 20 |
| `G(G(A,B2),B1)` | 40 | 20 | 20 |
| `G(G(B1,B2),A)` | 49 | 22 (inner `μ` mismatch) | 27 |
| **nested total** | **129** | **62** | **67** |

The 67 survivors have synchronizing inner pairs (co-scaled or
`μ = 2`), so their kill would happen at or after the OUTER merge —
whose emission law (merged-chart `P/μ`) and merge-vertex window are
NF-M objects. **The beyond-core closure alone would NOT stamp
them**; they need the merged-emission law first. The dagger does not
extend to them either (its census runs on pole chains, not merged
charts).

## 17. OPEN inventory (round-6 per-item status)

| item | round-5 status | round-6 status |
|---|---|---|
| two-word deep families (`Pi = 5^k`, both tails deep) | OPEN (NF-Z† hold) | **CLOSED — dead at X (§15, DG5)** |
| 129 nested 11-C rows | OPEN | **CLOSED-AT-TIER (rounds 8–10; review chain: grok-td11-block2-review SOUND-WITH-ERRATA -> round-9 outer-merge repair -> grok-67-final YES-all-67-dead + three writeup errata -> round-10 fold): 62 SPINE-DEAD (inner-H8, §16) + 67 via NF-M (NF-M.md §5): 31 unrealizable, 12 AB self-refused (GENERAL den-criterion at `k \| i_G = 2`, X alive — round-9 attribution, not Lemma CAP-DEN), 3 split (cylinder self-refused + discrete `(11,7)` alternatives outer-dead), 21 DEAD-OUTER by the round-9 outer-merge analysis (parametric in the unknown inner emission `w_in`; census-pinned zero-slots; algebraic family refusals; below-window schemas fall to the completed-object clash where CAP-DEN applies genuinely). 0 LIVE, 0 DEFERRED. Named objects: the two above-window free-`ν_A` candidates (census-unrealizable). Riders: `ν = 1` modes (NF-P), post-merge P0 strata, current-state arrivals |
| beyond-core budget-9 region | OPEN | OPEN — §13.0 paths unchanged; NOT sufficient for the 67 nested rows |
| cap-free closures `(3/2,2)@9`, `(4/3,3)@9` | OPEN | OPEN (compiler-tier) |
| `ν = 1` insertions, resonance-bearing chains | NF-P | **STAMPED (NF-P.md round 1): ν=1 modes classified — η-absorbed `ε>0` EMPTY (η-pole lemma), η-factor covered by the ν-uniform square system, the 18-schema ν=1 menu all refused/out (zero live); resonance chains dead by promoted rows with per-state finiteness; pure-b below-window at every ν. Residue = NF-P-OB1 (the state-changing closure) = the standing beyond-core item, not a new object** |
| Q+E5/E5F refile | UNKNOWN | UNKNOWN (unchanged) |
| general NF-Z† algorithm | — | OPEN (definition gap flagged in NF-Z.md §6; the td-11 DIE-horn instantiation does not repair it) |

Remaining genuinely-OPEN td-11 items after the NF-P round:
**three** (beyond-core region — which now also absorbs NF-P-OB1's
state-changing closure, cap-free closures, refile) plus the
general-dagger definition gap, which is cross-rung. The NF-P slice
is stamped (NF-P.md), completing the three quotient lemmas:
NF-Z (closed record + in-zone core), NF-M
(REDUCED-WITH-PROVED-CORE), NF-P (REDUCED-WITH-PROVED-CORE). The 129 nested rows are CLOSED-AT-TIER,
confirmed by grok-67-final (YES — all 67 DEAD-AT-TIER; writeup
errata folded round 10: the sign lemma replaced by the closed form
with its seven `A < Q` schemas, the free-`ν_A` census completed at
109 members all census-unrealizable, I1/I2b now real gates).
