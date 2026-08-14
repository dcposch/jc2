**VERDICT: SOUND — both cells are tower-dead by the same level-1 clash; the (7,15) tripwire is a genuine E5-refutation (`n = −1`) and the corrected (37,15) ledger `27750/1850/925` is exact and covered by the kill; the k-symbolic frame identities hold for all six `2/(2k+1)` members and each member has a genuine legal realization; kbar=7 is generic in the three consumed formulas. The `n ≥ 1` filter omission does not touch either kill or the promoted §11a cell/route census; it does contaminate 7 of 16 rollout min-witness columns (the filed (58,87) row plus 6 others).**

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-14.
Target: `TOWER-58-87.md` + `TOWER-25-35.md` + `cases/towers/t58_87.json` + `cases/towers/t25_35.json` + the parameterized `cases/tower_check.py`. (No `t58_87*.json` sibling exists.)
Kills under review: the two new cell-level tower kills — `(58,87,43,29)@15` (PROBE 2, family representative) and `(25,35,17,5)@8` (PROBE 3, the kbar=7 outlier). The `(9,15)` / `(10,15)` machinery is triple-reviewed and promoted — **not re-reviewed**. Scope is what is NEW: (1) probe-2 k-symbolic frame in `m` and the six-member coverage claim where specialization was forced; (2) THE TRIPWIRE, verified both ways, plus blast radius of the `n ≥ 1` omission on other rollout rows and on the promoted §11a census (3 arrival spot-checks); (3) probe-3 kbar-genericity, 3 consumed formulas at kbar=7 independently; (4) the 1435-gate suite.
Method: line-read of the five artifacts against `TOWER-ROLLOUT.md` §1–§2 / Risk 4 / U-OB5, `BOOK-OFFAXIS.md` §11a, `SHEET6-III.md` E5 `(g')/(h')`; `python3 cases/tower_check.py` (exit 0, **1435/1435** PASS, 21/21 perturbations including the four new probe-2/3 controls); independent exact `Fraction` replay of the family identities (six members + odd-`m` lattice 5..41), the `(7,15)` BOOK-2.1 chain and E5 offset, the `(37,15)` deg-transport ledger and death-gap table, the uniform offset law `n = (X ν_U − ν_G)/μ0`, every §11a-listed direct arrival on the 16 remaining cells, and the three kbar=7 formulas re-derived from (H6) + the chain-1 freeze. Cellmap of the 69-state closure used only as a menu-existence check. No other repo file modified. No git.

---

## Blast-radius statement (explicit)

The `(h')` filter `n = ν_U κ̄_G − ν_G κ̄_U ≥ 1` is a **vertex-level** constraint. The rollout engine's `direct_ok` and the promoted §11a census are **state-level** (`w_U` priced, `μ0 ∣ M_U`, stored step-cell or `ν ≡ −1 (mod μ0)`). That is exactly Risk 4's arrival-superset rider. Consequences, independently recomputed (charged `κ̄_U = w ν_U + 1/M`; clean/neutral pad `κ̄_U = w(ν_U+1)`; both reduce to `n = (X ν_U − ν_G)/μ0` on an E5-matching `M = μ0` arrival):

| object | hit by `n < 1`? | survives? |
|---|---|---|
| **(58,87) kill** | displayed min-witness `(7,15)` yes (`n = −1`); authors already rerouted | **YES** — legal `(37,15)` at `27750/1850/925`; clash is arrival-independent |
| **(25,35) kill** | displayed `(5,8)` has `n = 1` | **YES** — no alarm, row exact |
| **Other rollout §2 min-deg / `i_G` / `P_min` columns** | **YES: 6 further rows** (7/16 including the filed one) | cell still ARITH-DEAD-PREDICTED; those three columns are wrong |
| **Promoted §11a cell list (17) and route counts (238/233)** | **NO** | routes are `px5.feasible` completions of the arrival *state*, not of a `(ν, κ̄)` vertex |
| **Promoted §11a arrival-vertex lists** | **YES: 7 listed directs** (and the three kbar=5 minimal neutrals) are E5-illegal | lists are a known Risk-4 superset; every such cell has another legal vertex |

The six additional dirty min-witnesses, not filed in the probe-2 erratum:

| cell @ μ0 | claimed witness | `κ̄_U` | `n` | first legal replacement |
|---|---|---:|---:|---|
| `(15,25,12,5)@3` | neutral `ν=2` | 1 | **−2** | pad `ν=5`, `n=1` |
| `(21,35,17,7)@4` | neutral `ν=3` | 1 | **−2** | pad `ν=7`, `n=1` |
| `(27,45,22,9)@5` | neutral `ν=4` | 1 | **−2** | pad `ν=9`, `n=1` |
| `(34,51,25,17)@9` | direct `ν=4` | 1 | **−1** | direct `(13,9)`, `n=3` |
| `(42,63,31,21)@11` | direct `ν=5` | 1 | **−1** | direct `(16,11)`, `n=3` |
| `(90,135,67,45)@23` | direct `ν=11` | 1 | **−1** | pad `ν=45`, `n=2` (this cell has **no** legal direct) |

The three kbar=5 hits are *not* "small-`κ̄_U` directs" — they are the **minimal neutral pads**, a class the U-OB5 addendum as written does not name. The closed form on the kbar=5 family (`X=3`, `ν_G = 5μ0−3`) is `n = ν_U − 4` at the minimal pad `ν_U = μ0−1`, hence **identically −2**. Same pattern as the probe-2 pad `ν=14` (`n=−2`).

Probes 1/3 and `(9,15)` pass, as claimed: `(10,15)` direct `(7,3)` has `n=7`; `(25,35)` has `n=1`; `(9,15)` recorded `ν=7` at `M=2` has `n=7`. Gap/window/`P=1`-escape columns are unaffected (gaps are `d_q/deg p_f`; the empty-stack scan at `deg_U ≤ 50` never used a refuted vertex that would have been a `P=1` escape anyway).

**No cell is deleted.** The filter only shrinks realization families. The two kills under review never relied on a refuted vertex's realizability.

---

## Findings (worst first)

### 1. Severity: suggestion — the `n ≥ 1` omission is a 7-row rollout-table defect, not a one-row erratum; the three kbar=5 minimal pads were not in the named audit class

- File: `TOWER-ROLLOUT.md:243-248,412-416`; `TOWER-58-87.md:28-45`; `cases/tower_rollout_arith.py:192-207`
- Claim (authors): the `(58,87)` min-witness `13650/910/455` is E5-refuted; "rows with small-`κ̄_U` direct arrivals need the same audit"; gap/window unaffected; probes 1/3 and `(9,15)` pass.
- How checked. Closed form on an E5-matching `M=μ0` arrival, charged or clean as the vertex type demands:

  ```
  n = (X · ν_U − ν_G) / μ0.
  ```

  Replayed against every §2 min-witness and every §11a-listed direct (Part 5 of the independent run). Seven min-witnesses fail; seven census directs fail (the kbar=6 "small" list `ν_U = (μ0−1)/2`, which has `n ≡ −1`); three kbar=5 minimal neutrals fail with `n ≡ −2`. Authors correctly diagnosed the mechanism and correctly exempted probes 1/3 / `(9,15)` / gap-window. They did **not** run the audit they named, and the addendum as written misses the kbar=5 pad class.

  This does not touch either kill under review (Risk 4 was applied: the clash never used an arrival's realizability; `(25,35)`'s displayed vertex is legal). It is a residual defect of the *prediction table*, exactly the class U-OB5 was just extended to catch.

  **Erratum to write (rollout §2, not the certificates).** Recompute the seven dirty `min deg / i_G / P_min` triples under `n ≥ 1`. Name the kbar=5 pad class in U-OB5. The §11a arrival-vertex column can stay as a state-level superset if the rider is explicit; do not silently shrink the 17-cell / 233-route book.

### 2. Severity: suggestion — the six-member E5 filter is a uniform law, not "per-vertex census data"; `(9,19)` and `(11,23)` are the same `n = −1` as `(7,15)`, and `m=23` has no legal direct

- File: `TOWER-58-87.md:89-97`; certificate `family.scope`; `BOOK-OFFAXIS.md:768-773`
- Claim: specialization was forced at (i) member-specific census menus and (ii) the vertex-level E5 filter because `κ̄_U` is per-vertex census data; the family kill at the frame+exhaustion tier needs one mechanical witness row + arrival-filter table per member.
- How checked.

  **Menus are genuine.** The 69-state cellmap at `(w,M) = (2/m, m)` is exactly the listed census directs, every member:

  | `m` | cell | cellmap at `(2/m, m)` | matches `family.scope` |
  |---:|---|---|---|
  | 15 | `(58,87,43,29)` | `(7,15),(37,15)` | yes |
  | 17 | `(66,99,49,33)` | `(25,17)` | yes |
  | 19 | `(74,111,55,37)` | `(9,19),(47,19)` | yes |
  | 21 | `(82,123,61,41)` | `(31,21)` | yes |
  | 23 | `(90,135,67,45)` | `(11,23)` | yes |
  | 25 | `(98,147,73,49)` | `(37,25)` | yes |

  **The E5 filter is not member-specific data.** On this family (`X=4`, `ν_G=3m−2`, `M=m`) the charged offset collapses to

  ```
  n = (4 ν_U − (3m − 2)) / m.
  ```

  Every listed direct with `κ̄_U = 1` (i.e. `2ν_U+1 = m`, `ν_U = (m−1)/2`) has `n = −1` identically: `(7,15)`, **`(9,19)`**, **`(11,23)`**. Every `κ̄_U = 3` direct has `n = 3`; every `κ̄_U = 5` direct has `n = 7`. Minimal pads `ν = m−1` have `n = −2`; first legal pad is `ν = 2m−1` with `n = 2`. The probe-2 writeup records this table only for `m=15`. The same three-line computation covers the other five.

  **Every member is genuinely covered by a legal vertex**, which is the question asked:

  | `m` | legal realization | `n` |
  |---:|---|---:|
  | 15 | direct `(37,15)` (displayed) | 7 |
  | 17 | direct `(25,17)` | 3 |
  | 19 | direct `(47,19)` | 7 |
  | 21 | direct `(31,21)` | 3 |
  | 23 | **pad `ν=45` only** (sole direct refuted) | 2 |
  | 25 | direct `(37,25)` | 3 |

  The frame-tier claim is therefore honest and the six members are each covered at that tier. Completing the family kill still needs a witness row per member (menus really are not functions of `m` — the stored `(ν,M)` list is closure data). What it does *not* need is six independent E5-filter arguments. Write the closed form; record that `m=23` has no legal direct. The checker family block (`tower_check.py:440-463`) verifies identities + the substring `"specializ"` in `scope` and never looks at the menus or the filter — so it would accept a tampered menu list.

  Scope of the `(58,87)` *cell* kill is not overclaimed: one filed route, full realization family of that cell, including the refuted-`(7,15)` pads. The other five members are framed, not killed. Matches `family.scope` and the obstruction `scope` paragraph.

### 3. Severity: nit — two of the advertised family identities are tautologies; N1 is automatic for odd `m`

- File: `TOWER-58-87.md:83-88`; `tower_check.py:442-461`; certificate `family.frame_identities`
- Claim: `kbar=6`, `X=4`, `w_G=4/(2m−1)`, `j=2m−5`, N1 `gcd(6,3m−2)=1`, P3 `6m−4=2(3m−2)`, verified for all six members and the odd-`m` lattice.
- How checked. Independent replay (Part 1): every identity holds for `{15,17,19,21,23,25}` and for odd `m ∈ [5,41]`. Content vs tautology:

  | identity | content |
  |---|---|
  | `κ̄ = 2(6m−3)/(2m−1) = 6` | real (the family is the kbar=6 slice) |
  | E5 (I4) `(m·(3m−2)·(2/m)−2)/(m−1) = 6` | real (E5 pin on this `w`) |
  | (H6) `m(6 − (3m−2)·2/m) = 4` | real (`X=4`) |
  | `w_G = 4/(2m−1)`, `j=2m−5` | real (terminal package) |
  | `X = 6m−(6m−4) = 4` | **tautology** (the content is `X=κ̄−2`) |
  | P3 `6m−4 = 2(3m−2)` | **tautology** (checker `(dq−1) % ν_G == 0` is the same identity) |
  | N1 `gcd(6,3m−2)=1` | automatic for every odd `m` (`3m−2 ≡ 1 (mod 6)`); the even-`m` perturbation (`m=16`, gcd `=2`) is a real control of a constraint the family never meets |

  The even-member perturbation is the right negative test. Do not advertise P3 / the written `X=4` form as load-bearing family content. The four non-tautological identities are the frame.

### 4. Severity: clear — THE TRIPWIRE verifies both ways; the kill covers the corrected `(37,15)` numbers

- File: `TOWER-58-87.md:14-45`; certificate `arrival.e5_refuted_arrivals`, `e5_legal_pads`, displayed U, `sources.rollout`
- Claim: `(7,15)` has `n=6·7−43·1=−1`; legal minimum is `(37,15)` at `27750/1850/925`; kill unaffected.
- How checked.

  **(A) Refutation arithmetic.**

  1. `(7,15)` is the stored cell `(105,15,7)` at state `(2/15,15)` (cellmap; last step `st96 l9e0k1S6x0nu7(105,15)` off `(2/9,9)`, and a second path `l10` off `(3/10,10)`).
  2. BOOK-2.1 from the P2 frame `(ρ,κ̄,ν)=(1/2,5,3)`, independently:

     ```
     P2 → (20,16) l=2:  n=7,  κ̄=4,
     (20,16) → (130,40) l=4:  n=16, κ̄=4,  (ν,M,ρ)=(13,10,1/10),
     (130,40) → (105,15) l=10: n=9,  κ̄=(4+9)/13=1.
     ```

     Charged frame check: `κ̄_U = (2/15)·7 + 1/15 = 1`. Matches the writeup.
  3. E5 `(h')` `κ̄_G = (ν_G κ̄_U + n)/ν_U` rearranges to `n = ν_U κ̄_G − ν_G κ̄_U = 7·6 − 43·1 = −1`. Printed `(h')` requires a positive integer offset (`SHEET6-III.md:139,147`: `n ≡ −ν_F κ̄_G (mod ν_G)` and the `n ≥ 1` window). `n = −1` is E5-refuted.
  4. Pads over the `ν=7` witness are clean (`κ̄ = w(ν+1) = 2(ν+1)/15`, the charged formula is non-integral on `ν ≡ 14 (mod 15)`). `ν=14`: `κ̄=2`, `n=−2` refuted. `ν=29`: `κ̄=4`, `n=2` legal. `ν=44`: `κ̄=6`, `n=6` legal. Matches the recorded `e5_refuted_arrivals` / `e5_legal_pads` blocks exactly. The perturbation that sets the refuted row's `n` to `1` raises 1 failure.

  **(B) Corrected minimum `27750/1850/925`.**

  1. `(37,15)` is the stored cell `(555,75,37)` (cellmap: `st96 l8e0k1S7x0nu37(555,75)` off `(3/8,8)`). BOOK-2.1 from V2 `(ρ,κ̄,ν)=(1/8,2,5)`: `n=23`, `κ̄_U=(2+23)/5=5`. Charged check: `(2/15)·37 + 1/15 = 5`. Offset `n = 37·6 − 43·5 = 7 ≥ 1` legal.
  2. Deg-transport from `deg p_{f,P2}=4` along the displayed DAG:

     ```
     (C)=(20,16) l=2:  4 · 20/2 = 40
     (40,16)     l=4:  40 · 40/4 = 400
     (555,75)    l=8:  400 · 555/8 = 27750
     ```

     Then (H8) `i_G = 27750/μ0 = 27750/15 = 1850`, stack product `P = i_G/2 = 925`. (H8) converse `27750 = 1850·15`. E5 `(g')` `D_{f,G} = (43·1850 + 7·27750)/37 = 7400`. (H6) `15(6 − 43·2/15) = 4`. All match the spine.
  3. Pads over `(7,15)` are larger (`deg · 29 = 13650·29 = 396150` under the engine's `deg·ν` pad multiplier), so `(37,15)` at 27750 is the E5-legal minimum among the filed family. Displayed ledger check: variant `(C)` records `deg_p_f_U=27750`, `i_G=1850`, `chain1_product=925`.

  **Kill coverage.** Death gaps on the displayed spine, two ways (`κ̄/D_f` and `d_q/deg p_f`), identical:

  | vertex | gap | `< 1/2` |
  |---|---|---|
  | V1 | `2/5` | yes |
  | V2 | `1/25` | yes |
  | U | `1/370` | yes |
  | G | `3/3700` | yes |
  | X | `463/925 = (925+1)/(2·925)` | **no** (`> 1/2`) |

  Window `(463/925, 5/2)` contains no chain-2 gap. `gap(X) = (ν+1)/(2ν)` is P1-anchored and lives in `(1/2, 3/4]` for every `ν ≥ 2`; the first-charged cap is P2-anchored (`i=2`, `k ∣ 2`). Neither uses the arrival vertex or `P`. Insertion `Dprev_min=13650` at `(2/15,15)` is the *refuted* family's degree — conservative for the N4 upper bound (smaller `Dprev` ⇒ larger insertion gaps; they still sit below `2/5`). The kill covers `(37,15)` and the legal pads.

### 5. Severity: clear — kbar=7 is generic in the three consumed formulas; the 10 flattening failures are all frame identities; the window never sees kbar

- File: `TOWER-25-35.md:42-54`; certificate `obstruction.statement`; `tower_check.py:1353-1356`
- Claim: nothing in the window arithmetic used `kbar ≤ 6`; flattening kbar 7→6 raises 10 failures; the three consumed formulas (I4, `X=kbar−2`, terminal `j`) hold at 7.
- How checked. Independent replay of the three named formulas, plus the two E5 evaluations the writeup also consumes:

  | formula | replay | value |
  |---|---|---|
  | E5 (I4) `κ̄ = (μ0 ν_G w_U − 2)/(μ0−1)` | `(8·17·3/8 − 2)/7` | **7** |
  | re-derivation of (I4) | `X = κ̄−2 = μ0(κ̄ − ν_G w_U)` ⇒ (I4) | same |
  | (H6) / handshake | `8(7 − 17·3/8) = 5 = X = 7−2` | **5** |
  | terminal `j = M(1−w)`, `R=1/(1−w)` | `5·3/5 = 3`, `5/3` | **3**, **5/3** |
  | E5 `(h')` on the displayed edge | `(17·2+1)/5` | **7** |
  | E5 `(g')` | `(17·50+400)/5` | **250** |
  | vertex filter | `n = 5·7 − 17·2` | **1** (legal) |
  | deg ledger | `4·(20/2)·(40/4) = 400`, `i_G=50`, `P=25` | exact vs §2 |

  Flattening `vertices[1].kbar` 7→6 raises **exactly 10** failures, all at G's frame / the two G-incident handshakes / G's recorded death gap:

  ```
  kbar = κ(1−π);  θ = X/kbar;  w = (kbar−ρ)/ν;  Cor 6.1 q-law;
  case-IV π = (ν−kbar)/ν;  (H4) X and n on G→X;
  E5 (h') and (H6) on G→U;  death gap 7/250 vs 6/250 = 3/125.
  ```

  None of A/B/C, N1–N4, the prefix menu, `gap(X)=(ν+1)/(2ν)`, or the `(gap(X), 5/2)` emptiness check appears. The flattened G-gap `3/125` is still `≪ 1/2`. The window does not see kbar. The 10 failures are the load-bearing frame doing what it should.

  Displayed route is slack (`λ=4 < 5=6−ψ`); L-A as the R1.3+P3 corollary (promoted, t10 suggestion 1) carries the residue — not re-opened. Terminals table: all three filed endpoints `(2/5,5,ψ=1)` slack / `(2/7,7,1)` eq / `(2/9,9,1)` eq replay (`j ∈ ℕ*`, `ψ=⌈R⌉−1`). Saturation-tamper perturbation raises 1 failure.

### 6. Severity: clear — Attack on "the family is only a frame layer" fails as an overclaim challenge; Attack on "kbar=7 is a new clash" fails; 1435-gate suite is green

- File: both writeups; `cases/tower_check.py`; both certificates
- How checked.

  **Suite.** `python3 cases/tower_check.py` from the repo root: exit 0, **1435** `[PASS]` lines, **0** `[FAIL]`, five certificates `OBSTRUCTED`, 21/21 perturbations caught. The four new controls do the jobs they advertise: `(58,87)` refuted arrival claimed legal → 1 failure; even family member `m=16` → 1 failure (N1); `(25,35)` kbar flattened → 10 failures; slack claimed saturated → 1 failure.

  **Wrong-object tripwire (Risk 6) is clean on both cells.** On `(58,87)`, `μ0=15` is the G→U edge multiplicity and the family parameter; the constants 2 and 4 in `gap(X)` and N3 are pole degrees and do not equal `μ0`. On `(25,35)`, `μ0=8` is even and is used only as that multiplicity; kbar=7 enters only the frame identities verified above.

  **`(58,87)` spine identities used by the NEW claims**, independent of the checker's printout: H5a Q-value `κ_G = 43 = 43·37/37`; displayed E5 `n=7`; K=`238650` matches `2·3·5²·37·43`; both Prop 4.1 poles `d_f+d_g = 5/79550 = 1−π` and `5/2775 = 1−π`. Insertion `(6,4)` ledger `i`-chain `2/6/30/150`, `i_G 1850→5550`, product `925→2775`. Menu lock: `first_charged_gaps = {5/14, 2/5}` equals the variant gap set (t10 suggestion 2, in force).

  **`(25,35)` spine.** Single DAG `(C)→(40,16)`, census `3(2)`, arrival `(3/8; 4; M8)`, `gapmax=2/5`: all exact against the constructed spine. First slack displayed route; L-A inherited.

---

## What is not claimed

- The other four `2/(2k+1)` members (`m=17,19,21,23,25` minus the displayed 15) are **not** tower-killed. Frame + exhaustion-shape + a legal vertex each; no spine, no T1, no insertion ledger. `m=23` in particular still needs an explicit pad witness.
- The six dirty rollout min-deg numbers (Finding 1) are **not** corrected by this review. Prediction-table debt, U-OB5.
- The promoted §11a 17-cell / 233-route book is **not** reopened. Arrival-vertex lists remain a state-level superset (Finding 1).
- L-A, N1–N4, the three-case exhaustion, and the single-ladder reading were not re-opened (machinery core).
- `(9,15)` and `(10,15)` remain the only promoted cell kills.

---

## Reproduction

```bash
cd /Users/dc/code/math/jc72108
python3 cases/tower_check.py           # exit 0, 1435 PASS, 21 perturbations
# independent replay of Findings 1, 2, 4, 5 is in this file, not in the checker
```
