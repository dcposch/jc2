# TOWER-TD11.md — entry-level clash analysis for the three td-11 entries

Status: **ENTRY/ONE-STEP TIER COMPLETE (2026-08-14, round 1).** All
three L6-surviving td-11 entries have their clash windows closed at
this tier: 11-B and 11-C are EMPTY by exact gap arithmetic; 11-A's
window contains exactly one intruder — the `5/8` resonance — which is
H8-dead by the promoted `v_2` mismatch, and that kill is **μ-robust**
(the resonance drops `M` to `1`, forcing `μ = 1`; the
grok-nfd-finding-1 escape does not exist on that branch). The td-11
entry-clash theorem is therefore a REAL PROSPECT with the same shape
as td-7's; its remaining proof obligations are enumerated in §6 and
none is discharged here. Machine gate: `cases/tower_td11.py`
(24 checks, exit 0; count printed) — a prediction engine in the
`tower_rollout_arith.py` mold, NOT a certificate.

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

Obligations to promotion (numbered against scope §2.3; none
discharged here):

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

If OB-1..10 discharge with the windows as computed here, the three
entries fall to the same theorem shape as td-7 — and with them, by
§5, the td-11 neutral-depth question.

## 7. Reproduction

```bash
python3 cases/tower_td11.py    # 24 checks, exit 0 (count printed)
```

Blocks: 0 the domain law vs the scope §3.2 menu maxima; 1 the
resonance identities (`5/8`, `5/4`, M-drop structure); 2 entry 11-A
(freeze, window, the intruder and its μ-robust H8 kill, Case-A
refusal under both caps, inhabited synchronization); 3 entry 11-B
(freeze-modulo-resonance, empty window, resonant-X placement, Case-A
refusal incl. even `nu_X = 2`); 4 entry 11-C (ported freeze, empty
leaf windows, sibling arithmetic, ported cap); 5 cross-entry
(μ-discipline, M-drop dichotomy, the NF-D byproduct, and the
load-bearing `nu_X = 3` near-miss at 11-B). `cases/nfd_check.py`
(22), `cases/nfz_check.py` (39), `cases/tower_check.py` unchanged.
No git commit.
