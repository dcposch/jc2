# TOWER-TD11.md — entry-level clash analysis for the three td-11 entries

Status: **THEOREM STATED AND MACHINE-CHECKED WITHIN ITS PERIMETER
(2026-08-14, round 2 — obligations OB-1/4/5/6/7/8/10 discharged in
§7, Lemma 11A-RES in §8, Theorem TD11-CLASH in §9, census
implication in §10, near-miss ledger in §11, perimeter honesty in
§12).** Round-1 content (§§0–5, the window verdicts) is unchanged
and review-ready. Machine gate: `cases/tower_td11.py` (46 checks,
exit 0; count printed) — blocks 0–5 are the round-1 window
arithmetic; blocks 6–13 are the obligation discharges, including the
px2/px5 closure-wide window audit (21 + 347 + 69 states) and the
den-criterion prefix exhaustion over the full register lattice.

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
hard td-11 object" is dead at this tier if the promoted H8 row
survives route realization — the first refile question of
scope:354-355 is now the ONLY question for 11-A.

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
  preserve `M` and stay below `1/2` forever, or drop `M` and die on
  `v_2`. This is the td-11 analogue of td-7's "pure `n=1` clean
  neutrals forced" step.

## 5. The NF-D byproduct (why this came before NF-P)

NF-D round 2 left td-11 depth OPEN: the synchronized windows are
infinite (`Pi = 5^k` at every depth) and no mechanism-A pin exists.
The entry-clash theorem closes that from the other side: **every
neutral word extends a spine whose X-death is refused in every case
above, so a proved clash kills all depths at once** — deep words die
as a corollary, no depth cap needed, and the depth/census circularity
(census needs depth bound, depth bound needs census) is broken
entry-wise. The `Pi = 5^k` family lives in the synchronized window
but every member's spine faces the same Case-A refusal.

## 6. The td-11 entry-clash theorem: statement prospect and obligations

**PROSPECT (not yet a theorem).** *For each of 11-A, 11-B, 11-C: no
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

### 7.5 OB-6: closure-wide window audit (gate block 10, px2/px5)

The td-7 enumeration engines close all three opponent seeds:
`(3,2)` → 21 states, `(4/3,3)` → 347, `(3/2,2)` → 69. Over EVERY
state and EVERY menu step (parametric families included):

* **growth law:** every step multiplier `dp/l >= 2`, so a depth-`j`
  step sees `deg >= p·2^{j−1}`;
* **ratio law:** the max step ratio `R* = dq·l/dp` per closure is
  `5/2, 3, 5/2 < p = 4, 6, 4` — hence EVERY depth-`>=2` step gap is
  `<= R*/(2p) < 1/2`. Depth-1 gaps are the frozen §3.2 menus
  (`< 1/2` except 11-A's `5/8`).
* **resonance census:** at-seed resonances are exactly `D3n2nu2` at
  `(3,2)` (the `5/8`) and NONE at the other two seeds; all deeper
  copies (`D3n2nu2`, `D5n2nu4`, `D4n2nu3`) fall under the
  depth-`>=2` law.
* **chain-1 engine audit:** the zero-cost clean `n>=2` menu at
  `(2,1)` is EMPTY (the L-A freeze, engine-confirmed) and at `(3,1)`
  is exactly `{D3n2nu2}` (11-B's classified `5/4`).

So the ONLY object anywhere in the three multistep closures with a
gap `>= 1/2` is 11-A's seed-level `5/8` — the round-1 window verdicts
are closure-stable, not just one-step facts.

### 7.6 OB-8: three-pole composition, 11-C (gate block 11)

The second opponent adds NO window step (same seed, menu max
`2/5 < 1/2 < gap(X)`) and only SHRINKS the joint cap (intersection
of simultaneously-alive caps — tower-N3 kernel); the exhaustion is
divisor-closed (`c = 1` swept), so every shrunk cap is covered. No
sibling-X tie: the second and third poles are charged `M = 2` seeds,
not `M = 1` carriers. Nested inner-merge orders (an inner merge
BEFORE the candidate clash, creating states outside the audited
closures) are the one law-covered perimeter clause — §12.

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

**Theorem (entry tier, within the §12 perimeter).** *For each td-11
L6-surviving entry `E ∈ {11-A, 11-B, 11-C}` with its derived packet
(§7.1): every synchronized configuration — all `μ`-assignments under
`μ | M`, every stack `Pi` in the co-scaling window (including the
`Pi = 5^k` deep-word family and arbitrary neutral insertions within
the NF-D/clash perimeter), every E5F-admissible realization — dies
at the tower tier. Explicitly: the global ladder's death order
reaches the entry's pole-adjacent X (neutral `gap(X) = (ν_X+1)/(2ν_X)`
over the domain-legal `ν_X`, or 11-B's resonant `X = 5/4`) with
every competing object below `1/2` (§7.5), possibly after a prefix
of cap-legal steps; and the X-death step is REFUSED —
`den(alpha_m − 1 + gap(X))` divides no cap candidate for any lattice
register `alpha_m` (§7.4, Lemma CAP-DEN) — while the sole in-window
intruder (11-A's `5/8`) is H8-dead (Lemma 11A-RES) and
non-synchronized routes are spine-dead (§7.2). Configurations
extending any such spine by neutral words of any depth — in
particular the NF-D-round-2 `Pi = 5^k` family — die with it.*

Per-entry constants:

| entry | packet `(k_0,l_0)`, `alpha_1`, `g_top` | cap candidates | X family | intruder |
|---|---|---|---|---|
| 11-A | `(2,3)`, `3/2`, `5/2` | `{1,2,4}` | `(ν+1)/(2ν)`, `ν` odd | `5/8` — dead (Lemma 11A-RES) |
| 11-B | `(2,5)`, `5/2`, `7/2` | `{1,2,6}` | `(ν+1)/(2ν)`, `3∤ν` (even `ν` legal); resonant `5/4` | none |
| 11-C | `(2,3)`, `3/2`, `5/2` | `{1,2}` | `(ν+1)/(2ν)`, `ν` odd | none |

*Proof assembly:* §7.1 (packets) + §7.2 (synchronization dichotomy)
+ §7.5 (no competing object at or above `1/2` anywhere in the
closures, so X is reached in gap order with at most cap-legal
prefixes — Case B refused by descent) + §7.4 (X-death refused over
the full register lattice under every cap candidate — Cases A and C)
+ §8 (the intruder) + §7.6 (third pole only shrinks caps, adds no
window step) + §7.7 (realization dichotomy). ∎ within §12.

**Corollary (NF-D closure for td-11).** The td-11 neutral-depth
question (NF-D: `D` OPEN, `S` infinite) is closed entry-wise: every
neutral word of every depth extends a clashed spine and is dead. The
depth/census circularity is broken without a depth cap.

## 10. Census implication (the td-11 census does not yet exist)

The theorem operates at the entry/configuration tier. What the
eventual compiler consumes: **any td-11 class-B/C census row whose
configuration passes the E5F-corrected enumeration discipline
contains a synchronized spine in one of the three entry shapes (or
fails H8, which is spine-death); the row therefore emits TOWER-DEAD
with certificate = (entry id, packet constants, cap candidate, the
CAP-DEN refusal instance or Lemma 11A-RES).** That statement — not a
cell count — is the emptiness certificate: it is quantified over
entries with per-entry constants and is independent of how many rows
the census will eventually have. A census row that CANNOT be mapped
to one of the three shapes is outside the theorem and must be
reported, not certified (Rule 6).

## 11. Near-miss ledger (where a hostile reviewer should push)

| # | near-miss | what saves it | gate row |
|---|---|---|---|
| 1 | 11-B, `ν_X = 3`, cap `6`: `k = 2ν_X = 6 | 6` — a genuine Case-A escape | the domain law `3 ∤ ν` at `w = 3` excludes `ν_X = 3` EXACTLY | X4 |
| 2 | 11-B, `ν_X = 2`, cap `6`: `ν | c²` (Lemma CAP-DEN's necessary condition) PASSES | the 2-adic part: `den((2a−3)/12) ∈ {4,12}`, never `| 6` | OB7c |
| 3 | 11-A, cap `4`: the prefix menu is NONEMPTY (`k = 4` rows exist arithmetically, unlike td-7's `k|2` menu) | the exhaustion is menu-independent (α-lattice superset); every lattice register still refuses X | OB7a/b |
| 4 | 11-A, `ν_X = 3`: the `5/8` intruder is NOT in the window (`2/3 > 5/8`) — the kill must not cite Lemma 11A-RES there | it doesn't: `ν_X = 3` dies by CAP-DEN directly (`3 ∤ 16`) | OB7b/c |

These four exclusions are exact and each is one arithmetic fact away
from an escape; they are the load-bearing edges of the theorem.

## 12. Perimeter honesty (machine-checked vs law-covered)

**Machine-checked (blocks 0–13, 46 rows):** the domain law against
the scope menus; the window arithmetic; packet derivations with td-7
regression; H8 windows under `P/μ` (inhabited + unsat branches); cap
candidates including realized even `P_pre` at 11-A; the α-lattice
lemma and the full den-criterion exhaustion (every cap × residue ×
domain-legal X, plus algebraic ν-closure); the closure-wide
growth/ratio laws and resonance censuses over all 437 engine states;
the chain-1 zero-cost menus; Lemma 11A-RES's `v_2` computation over
domain stacks; the composition cap-shrink arithmetic.

**Law-covered (cited promoted results, not re-proved here):** the
ladder calculus itself (delta descent, no-skip, death equations, Z1);
the L-A kernel (uncharged + `M = 1` propagation on merge-free
branches); Prop 4.2(iii)/8.1 for the X-side `k | 2` (the exhaustion
is robust to its failure via the conservative caps); the promoted
`H8_EQUAL_QUOTIENT_VP_MISMATCH` certificate; the E5F base law; px2's
menu completeness per state (the promoted enumeration engine — the
same trust td-7's book stands on).

**Perimeter clauses (outside the theorem, Rule 6 on their slice):**
(i) nested inner-merge orders that create chart states BEFORE the
candidate clash outside the audited closures (NF-M territory; 11-C's
145-row nested skeleton is enumerated but not state-audited here);
(ii) multi-word deep-zone coexistence (POLICY NF-Z†, unchanged);
(iii) the budget horizon: closure audits ran the gross budget 9
discipline of the scope tables; (iv) `nu = 1` insertions and
resonance-bearing chains stay NF-P's. A configuration reaching any
clause is reported OPEN, never certified.

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
python3 cases/tower_td11.py    # 46 checks, exit 0 (count printed; ~3 min,
                               # the (4/3,3) closure dominates)
```

Blocks: 0 domain law vs scope §3.2; 1 resonance identities; 2–4 the
per-entry round-1 window verdicts; 5 cross-entry μ-discipline and
the NF-D byproduct; 6 OB-1 packets; 7 OB-4 H8 windows; 8 OB-5 caps;
9 OB-7 den-criterion exhaustion (α-lattice lemma, full sweep,
CAP-DEN algebra, td-7 regression, Case B); 10 OB-6 closure audit
(growth/ratio laws, resonance census, chain-1 menus); 11 OB-8
composition; 12 OB-10 realization dichotomy; 13 the theorem
aggregate + census implication. Companion gates unchanged:
`cases/nfd_check.py` (22), `cases/nfz_check.py` (39),
`cases/tower_check.py` (promoted td-7 book). No git commit.
