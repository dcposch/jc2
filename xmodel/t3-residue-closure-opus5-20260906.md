# T3 residue: the sibling-tower closure with the depth cap lifted — Opus 5 — 2026-09-06

## 0. Custody

Built the manifest from the receipt's numbered `charged_input_<i>_sha256=`/`_basename=` fields
with `awk`, piped it to `sha256sum -c`: **6/6 OK** before any mathematical read. All reads were
the frozen copies in `/tmp/jc2-lane.slTSed/inputs`. The `sibling_tower*.py` drivers named in the
task were read from `box/exact-contact-20260906/` (task-named, not a charged input; flagged as
such). Writes: this report and `box/t3-residue-20260906/` (128 KB; JSON 54 KB; `df -h /` 13 GB
free). No ledger, no `jc2-lean`, no `ideation-*`, no fleet.

Source key. **X** = charged Xu PDF; **M** = charged Moh PDF; **EC** = the charged
exact-contact-r009-r050 report; **RS** = residual65-structure-fable5.

No exit-price assertion is made: every verdict below excludes or exhibits a *configuration*,
which is a root datum, not a pair and not an exit. Hence no `charge_basis=` line.

## 1. What actually bounds the depth — it is the gcd lattice, and it is not a cap

Three printed bounds were candidates. The binding one is **not** Def 5.1(2)'s window and **not**
the p.174 truncation; it is the reduction lattice.

**M Prop. 4.6(1)/Def. 5.1(4).** At a tower disc `D_i`, `g_{σ_i} = c·p^{n/d_i}` and
`f_{σ_i} = c'·p^{m/d_i}` — the *same* `p`. So a root of `p_i` of multiplicity `r` carries exactly
`ρ_f = (m/d_i)·r` roots of `f`, and **every** sub-packet of `D_i` has `ρ_f ∈ (m/d_i)Z`. This is
integral: `d_i = gcd(n, M_1,…,M_{i−1})` and `M_1 = −m` on all 66 roster rows, so `d_i | m` for
`i ≥ 2`.

**The bound.** Put `unit = m/d_i` and `r = ρ_f/unit`. A split has `≥ 2` parts, each a positive
multiple of `unit`, so `max_j r_j ≤ r − 1`: **`r` strictly drops at every split**. A sibling
tower rooted at a root of `p_i` of multiplicity `r` therefore has split depth `≤ r − 1`, and
searching to `r − 1` is *exhaustive*, not capped. Deeper the divisor is `gcd(d_i, M) ≤ d_i`, so
`unit` only **grows** with depth — `m/d_i` is the most permissive unit at every level, with or
without Lemma B.

Second, independent bound (used as a cross-check, never binding here): `W = n − M` strictly
increases along a packet (Def. 5.1(2)) and a major packet goes final at `W = n+m`
(X Lemma 4.4(i)), with `ρW/m ∈ Z` (Prop. 4.6(2)); so `W` runs over a finite subset of
`(W_0, n+m)`.

All ten searches below were run with **`maxdepth = None`** — no cap of any kind, no orbit cap
(the prior closure capped orbit-partitions at 4), and the recursion terminated by exhaustion.

## 2. An instrument correction found by bisecting, and stated as such

Run 1 used `unit = m/gcd(n,m)` — X Lemma 2.1(ii) alone, which I took to be the most permissive
reading. It returned **all six kills ALIVE already at depth 1**, i.e. an apparent refutation.
Before reporting that, I re-ran the prior lane's own `row_close.py` at depth 2 and reproduced
its six DEAD verdicts **exactly**. Bisecting located the difference: it is **not depth**, it is
the unit. X Lemma 2.1(ii) (`ρ_f : ρ_g = m : n`) gives only `ρ_f ∈ (m/gcd(n,m))Z`; M Prop. 4.6(1)
gives the strictly stronger `ρ_f ∈ (m/d_i)Z`, and `d_i | gcd(n,m)` properly on these rows
(e.g. R028 level 3: `m/d_3 = 10` against `m/gcd = 2`). The prior closure's `unit = m//dcur` is
correct; my Run 1 was illegally permissive. Everything below uses `m/d_i` per level, with the
`d_i/gcd(multiplicities)` refinement when the pattern is a perfect power.

## 3. The four T3 rows: all four are ALIVE, and the towers are named

Verdicts under the full layering (BASE + GO + Lemmas A,B), uncapped depth:

| row | `(n,m)` | cfgs | surviving | `I_M` | `I_m` | margin | depth searched / bound |
|---|---|---|---|---|---|---|---|
| **R039** | (144,96) | 4 | 1 | **16** | **3** | 13 | 0 / 4 |
| **R040** | (144,96) | 1 | 1 | **16** | **3** | 13 | 0 / 0 |
| **R048** | (200,150) | 2 | 1 | **22** | **5** | 17 | 2 / 4 |
| **R063** | (168,112) | 509 | 84 | **10** | **10** | **0** | 3 / 33 |

**R039 — ALIVE via the depth-0 tower `T(mult 5)`.** Pattern `p_3 = (π^4−c)^3`,
`p_2 = π^5(π^4−c_1)`, tower through the multiplicity-1 orbit class (`A_2 = 4`, `lo_2 = 3/7`).
Leaves: principal minor `ρ_f = 24` at `δ = 3`; 16 final major `D_1` at `δ_1 = 11/16`, `ρ_f = 2`,
`3/8` each `= 6`. Sibling: the `z`-class, multiplicity 5, `ρ_f = 10`, 4 conjugates, terminating
**at once** as a final major disc at `δ = 7/12`, `5/2` each `= 10`. Total `I_M = 16`, `I_m = 3`.
The "genuinely new sibling tower" is a single extra final major disc, not a deep tower: `r = 5`
permits depth 4, and no split at any `W` is admissible.

**R040 — ALIVE, and it is R039's mirror.** R039 and R040 share `n, m, M, d` and differ only in
`V_2` (1 vs 5). Their surviving leaf ledgers are the **same multiset**: `{principal minor
ρ_f = 24 at δ = 3; 16 discs ρ_f = 2 at δ = 11/16; 4 discs ρ_f = 10 at δ = 7/12}`, with the roles
of tower and sibling exchanged. Both give `I_M = 16`, `I_m = 3`. So the two rows are two
tower-*selections* of one root configuration, not two configurations. They are not independent
survivors, and any receiver chart built for one is the other's chart with the selection swapped.

**R048 — ALIVE via the depth-0 tower `T(mult 1)`.** `p_3 = (π^5−c)^3(π^5−c')`,
`p_2 = π^4(π^2−c)`. Leaves: principal minor `ρ_f = 30` at `δ = 4`; 5 minor at `δ = 6/5`,
`ρ_f = 6`; 5 final major `D_1` at `δ_1 = 8/15`, `ρ_f = 12`, `16/5` each `= 16`. Sibling: level-2
multiplicity-1 class, `ρ_f = 3`, 10 conjugates, final at `δ = 13/20`, `3/5` each `= 6`.
`I_M = 22`, `I_m = 5`.

**R063 — ALIVE, and the only one with a genuinely deep tower; margin 0.** Minimal-margin
survivor: `p_3 = π^{21}`, `p_2` with `A_2 = 2` and orbit multiset `[4,3,3,3,3,1,1,1,1,1]`
(`deg = 42 = P_2`, 20 distinct roots `≤ Q_2 = 21`), tower through a multiplicity-3 class.
Leaves: principal minor `ρ_f = 28` at `δ = 3`; ten minor `ρ_f = 2` at `δ = 17/10`; 2 final major
`D_1` at `δ_1 = 3/4`, `ρ_f = 6`, `9/10` each. Sibling towers: three multiplicity-3 packets
terminating at `δ = 3/4`, and **one multiplicity-4 packet, `ρ_f = 8`, that genuinely splits** —
`SPLIT @ W = 112` (`M = 56`, `δ = 3/5`, `A = 1`) into `(4,2,2)`, giving final major discs at
`δ = 2/3, 3/4, 3/4`, `ΔI_M = 7/5` each. Total `I_M = I_m = 10`.

R063 therefore joins EC §5's margin-0 set (R009, R014, R049, R050). It is **not** pinned: 84 of
its 509 configurations survive, so margin 0 is the minimum over a set, not a determined datum.
Reporting the minimum as a fact would be exactly the floor/attainment error.

## 4. The six depth-≤2 kills: confirmed, and the cap was vacuous

Re-run uncapped with the correct unit, all six are **DEAD** — and the depth cap was never a
hypothesis on any of them:

| row | sibling root (level, mult) | `ρ_f` | `unit` | `r` | depth bound `r−1` | depth searched | verdict |
|---|---|---|---|---|---|---|---|
| R025 | (2,2),(2,3),(3,4) | 4,6,40 | 2,2,10 | 2,3,4 | 3 | 1 | DEAD |
| R026 | (3,1) | 10 | 10 | 1 | **0** | 0 | DEAD |
| R027 | (2,2),(3,4) | 4,40 | 2,10 | 2,4 | 3 | 1 | DEAD |
| R028 | (3,1) | 10 | 10 | 1 | **0** | 0 | DEAD |
| R057 | (3,3) | 36 | 12 | 3 | 2 | 1 | DEAD |
| R058 | (3,1) | 12 | 12 | 1 | **0** | 0 | DEAD |

For R026, R028, R058 the sibling root has multiplicity **1**, so `r = 1` and the packet
**cannot split at all**: depth 0 is the complete search and "depth ≤ 2" was vacuous there.
For R025, R027, R057 the bound is 2–3 and the search closed at depth 1 by exhaustion.
**Answer to (4): yes — the lifted search confirms all six, and the `mod depth ≤ 2` clause in
EC's typing should be struck, not upgraded.**

## 5. What the six kills actually rest on (layer audit)

Each constraint layer switched off in turn, uncapped, on the six plus the R001 calibration kill:

| layers active | R001 | R025 | R026 | R027 | R028 | R057 | R058 |
|---|---|---|---|---|---|---|---|
| BASE+GO+A+B (full) | DEAD | DEAD | DEAD | DEAD | DEAD | DEAD | DEAD |
| −Lemma B | **ALIVE** | DEAD | DEAD | DEAD | DEAD | DEAD | DEAD |
| −Lemma B, −Lemma A | ALIVE | DEAD | DEAD | DEAD | DEAD | DEAD | DEAD |
| −GO final congruence only | DEAD | DEAD | DEAD | DEAD | DEAD | DEAD | DEAD |
| −GO entirely, −A, −B | ALIVE | **ALIVE** | **ALIVE** | **ALIVE** | **ALIVE** | **ALIVE** | DEAD |

Three readings, all new:

1. **Lemmas A and B are not load-bearing for the six.** EC typed them `DEAD-mod-[depth ≤ 2;
   Lemmas A,B]`; both components are wrong. Lemma B *is* load-bearing for R001 — dropping it
   revives R001 exactly as EC §4 predicted, which re-confirms that retrodiction from the other
   side.
2. **The operative hypothesis is the GO split-shape law**, `p = π^z ∏(π^A − c_ν)^{r_ν}` with
   `A = den(L·δ)` (M p.201(8)). Dropping only the *final-disc congruence* `ρ_f, ρ_g ≡ 0,1 (mod A)`
   changes nothing anywhere; dropping the split shape revives five of the six.
3. **R058 is DEAD on BASE alone** — Prop. 4.6(2),(3),(4), Def. 5.1(2)/A.3, and the Prop. 4.6(1)
   lattice, with no orbit law, no Lemma A, no Lemma B, no depth cap. That is the only
   unconditional kill of the six.

Retyped: **R058 DEAD (unconditional).** **R025, R026, R027, R028, R057 DEAD-mod-[GO
split-shape law]** — a promoted campaign law, but a hypothesis, and named.

## 6. Controls

* **Positive.** R009 and R050 reproduce `I_M = I_m = 8`, ALIVE and single-configuration; R001
  DEAD. Reproduced under every layering that keeps Lemma B, and under minor-splitting.
* **Prior-instrument replay.** `row_close.py` at depth 2 reproduces EC's six DEAD verdicts
  verbatim, which is what made the bisect in §2 possible.
* **Minor-split control (new).** "Minor packets terminate at once" is itself a hypothesis, and
  EC's claim that any split strictly raises `I_m` is not true term-by-term (at `Q = 3` an equal
  2-split leaves `I_m` unchanged). I therefore wired every minor leaf through the same closure
  and re-ran: the six stay DEAD, R009/R050 stay ALIVE at 8/8, R001 stays DEAD. The hypothesis is
  discharged on these ten rows, not assumed.
* **Negative.** With GO dropped the search revives rows, so the instrument is not a
  kill-everything; with the unit set to the too-weak `m/gcd(n,m)` it revives all six, which is
  how the §2 error surfaced.

## 7. FALLACY-v2 ledger

*Cap/hypothesis.* The depth cap is replaced by a proved bound (`r − 1`), and the search is
reported as exhausted-by-termination with both numbers printed per row. Where a layer remains a
hypothesis (GO) it is named in the verdict type, not absorbed.
*Floor/attainment.* R063's margin 0 is the minimum over 84 surviving configurations and is
reported as such; only R009/R050 have a single configuration.
*Configuration is not a pair.* No row is asserted to be realised by a polynomial pair; every
ALIVE verdict is `NECESSARY_TOWER_CONFIGURATION_NOT_POLYNOMIAL_PAIR`.
*f/g orientation.* X's `(f,g)` is the roster's `(g,f)`: `f` is the smaller, `deg_y f = m`, and
`ρ_f` always counts roots of the degree-`m` member. `I_M` is symmetric under the swap; `unit`
and `ρ` are not, and both are computed on the `m` side throughout.
*Flag/place/series.* `ρ` counts roots, `κ` is a series datum, `A` a Galois orbit size, `W = n−M`
a tower parameter kept distinct from `Q = ρW/m`.
*Prime label.* No differentiation is used; `d_i`, `d_true`, `unit` are declared at each use.

## 8. Verdict

```text
DEPTH BOUND   Moh Prop 4.6(1): rho_f in (m/d_i)Z at D_i, and d_i | M_1 = -m.
              A split has >=2 parts => r = rho_f d_i/m strictly drops => a sibling
              tower rooted at a root of p_i of multiplicity r has depth <= r-1.
              PROVED-HERE. Searching to r-1 is EXHAUSTIVE; no cap was applied.

R039 (144,96) ALIVE  I_M=16 I_m=3  tower T(level 2, mult 5, rho_f=10, x4, FINAL delta=7/12)
                     1 of 4 configurations; depth searched 0, bound 4
R040 (144,96) ALIVE  I_M=16 I_m=3  tower T(level 2, mult 1, rho_f=2, x16, FINAL delta=11/16)
                     = R039's configuration with tower and sibling exchanged
R048 (200,150) ALIVE I_M=22 I_m=5  tower T(level 2, mult 1, rho_f=3, x10, FINAL delta=13/20)
                     1 of 2 configurations; depth searched 2, bound 4
R063 (168,112) ALIVE I_M=10 I_m=10 margin 0; tower T(level 2, mult 4, rho_f=8, x2)
                     = SPLIT@W=112 (M=56, delta=3/5, A=1) -> (4,2,2), finals at 2/3,3/4,3/4
                     84 of 509 configurations survive: margin 0 is a minimum, NOT pinned
                     depth searched 3, bound 33

SIX KILLS     R058                     DEAD  unconditional (BASE only: Prop 4.6(2)(3)(4),
                                             Def 5.1(2)/A.3, Prop 4.6(1) lattice)
              R025 R026 R027 R028 R057 DEAD-mod-[GO split-shape law, M p.201(8)]
              In all six the depth cap was VACUOUS: bound r-1 in {0,0,2,3,3,0},
              search closed at depth <= 1.  EC's "mod depth <= 2" is struck.
              Lemmas A and B are NOT used by any of the six (B is used by R001).

RESIDUAL      65 -> 59, conditional on the GO split-shape law for five of the six;
              R058 removes unconditionally.  The four T3 rows stay in, and R039/R040
              are one configuration, so 59 rows carry 58 distinct configurations.

OPENS RAISED
  1. GO split-shape law. Five of six kills now rest on it alone. It is a promoted campaign law
     read off M p.201(8) and calibrated on four Xu displays, never re-derived. QUANTITY: source
     work <= 3 h to derive the orbit shape at a NON-tower disc, where Moh states it only for
     sigma_i.
  2. R063 margin 0 with 84 surviving configurations. Deciding whether integrality plus a
     second-generation condition pins it, as it pins R009/R050. QUANTITY: <= 2 h, 1 core,
     re-run the child ell-shift of EC sec.6 on all 84.
  3. R039 = R040 as one configuration. If tower-selection duplicates exist elsewhere the roster
     over-counts. QUANTITY: = 66 rows, <= 30 min to test leaf-ledger equality pairwise.
  4. Minor-split equality at Q = 3. An equal 2-split of a minor packet leaves I_m unchanged, so
     "any split strictly raises I_m" (EC sec.1) is false as stated; harmless here because the
     control was run. QUANTITY: <= 1 h to restate the lemma with the Q >= 4 hypothesis.
  5. No configuration here is a witness pair. QUANTITY: >= 600 rows for the cheapest receiver
     chart (R009), unchanged.
```

Drivers, exact-rational and re-runnable, in `box/t3-residue-20260906/`: `t3_closure.py`
(uncapped closure, switchable layers, `--minor-split`, `--maxdepth`), `t3_witness.py` (names the
surviving tower), `t3_summary.py`, `exact_contact.py` (path-fixed copy), `prior/` (the charged
lane's drivers, path-fixed, for the depth-2 replay), and the JSON: `t3_summary.json`,
`t3_witnesses.json`, `t3_uncapped_a.json`, `t3_uncapped_b.json`, `six_uncapped.json`,
`minorsplit_control.json`.

<!-- BODY-END -->
