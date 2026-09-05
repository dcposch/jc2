# k=4-ray β-strata coverage — no degree kill of b>b_min; extra strata charted, not closed

Lane `k4ray-beta-strata-grok46-20260905`. Adapter grok-4.6.
Drivers: `box/k4ray-beta-strata-20260905/`. No ledger, no `jc2-lean`, no `ideation-*`.

**VERDICT.** Task (1) has no clean proof that `b>b_min` is empty: the `3b≤2K` argument is a floor, MASTER supplies the already-used ceiling `b≤2K-1`, LEVEL 4 saturates the numerical tower at `c=3`, and the next `J`/`E` band is underdetermined. Task (2) builds per-stratum I_light charts with the LEVEL-4 top band parametrized (one scalar at `b=b_min`, two scalars above) and the lower β-block the exact box of 17(bbbbbb)/`pinned_chart.py` (no weight-floor drop of unknowns). The 17(bbbbbb) 36-variable PIN12/terminal cut does **not** transfer to the generic two-scalar top: DIV-band pivots depend on `q1`. Task (3): **K=8 no-split is not DEAD for all deg β**; **K=9 case (A) is not DEAD for all deg β**. The banked `b=b_min` units stand; every extra stratum that this lane decided is `INCONCLUSIVE_TIMEOUT` (not a modular non-unit, not a Q unit). Surviving/open list below.

No new exit-price assertion, so no FALLACY-v2 `charge_basis=` line.

## 0. Custody

The manifest was built from `xmodel/k4ray-beta-strata-grok46-20260905.run.v2` by joining numbered `_sha256` / `_basename` fields with `awk` and prefixing `lane_inputs_dir=/tmp/jc2-lane.E8XFPq/inputs`. `sha256sum -c` returned **8/8 OK**. Retained as `box/k4ray-beta-strata-20260905/frozen-inputs.sha256` and `.check.log`. No content mismatch.

Repo reads outside the frozen set were read-only. Writes: `box/k4ray-beta-strata-20260905/` and this report. Fleet worker **`i-01de3f3912cb345f7`** (`r7i.8xlarge`, `172.30.0.127`) was launched by this lane and is the only instance this lane may terminate.

## 1. Task (1) — the degree/order count does not exclude `b>b_min`

Notation as charged (`k4ray-degree-tower-opus5-20260903.md:49-68`): `H=y^{K-1}(y-x)`, `J(f,g)=c x^4`, `b=deg β`, LEVEL 4 `H^2|β_b^3` and `deg ρ=3b-2K` exactly, MASTER `deg(E-λf)=K+6` and `deg E≤2K` for `K≥7`. Residual band (`:349-362`):

```text
b_min = max(ceil((2K+1)/3), ceil(2(K-1)/3)+1)   <=  b  <=  2K-1 = b_max
K=7: 5..13    K=8: 6..15    K=9: 7..17
```

Machine markers in `box/k4ray-beta-strata-20260905/argument-analysis.out`.

**The `3b≤2K` argument is a floor.** Coefficient B of the tower (`:96-107`) assumes `ρ∈k`, forces `[J]_{3b-K-2}=3J(P,A)=0`, then LEMMA INJ kills `P`. That hypothesis is exactly `b<b_min`. For `3b≥2K+1` the top of `J(β,α)` and `J(h,ρ)` occupy the same degree and cancel by LEVEL 4; the argument does not run.

**MASTER does not lower `b_max`.** Combined with LEVEL 2 it is the charged ceiling `b≤2K-1`. LEVEL 4 is a lower bound. The numerical tower saturates at `c=3` (`:300-303`); LEVEL 5 is OPEN and would still only raise the floor (at `K=8`, `4b≥25` gives `b≥7`, which kills the already-charted wall row `b=6` and leaves `b=7..15`).

**The top total-degree of `J` is never 4 on the residual.** `D_top=3b-K-2`. `D_top=4` iff `3b=K+6`. For `K=7,8,9` that integer is absent or strictly below `b_min` (`MARK_T4_DTOP_NEVER_4_IN_RESIDUAL`, `MARK_T1_EXCEPTION_BELOW_BMIN`). After LEVEL 4 the leading-form Jacobian vanishes identically (`MARK_T3_LEAD_J_VANISHES 9 of 9`; polynomial division, not `together()`). All of `J=c x^4` is therefore carried by subleading bands.

**The first subleading band is underdetermined as a count, and a count is not a kill.** At `b=b_min+1` the linear unknowns `(h_{K-1}` after the constant gauge, `β_{b-1})` exceed the `D_1+1` coefficients of a binary form of degree `D_1=3b-K-3` by 3 at `K=7,8,9` (`MARK_T6_SUBLEADING_SURPLUS_POSITIVE`). FALLACY-v2: a linear surplus is not a proof of existence, a deficit is not a proof of emptiness. The next expressible `E`-band at `4b-2K` has leading-form part `-(3/4)P^4/H^2` but is separated from `3b` by `2K-b≥1` free subleading bands (tower `:488-496`). That gap is why LEVEL 5 is not a theorem.

**LEVEL 5 is not implied by LEVEL 4 at `K=7,8`.** The generic minimal-`s` shape has `H^3` not dividing `P^4` (`MARK_T5_LEVEL5_FAILS_GENERIC_K78`). At `K=9` the `s`-valuation holds with equality at `b_min` and does not raise the floor.

**α² and βρ contaminate the MASTER terminal above one extra degree.** `4b-2K < K+6` iff `b ≤ floor((3K+5)/4)`: `K=7` b≤6, `K=8` b≤7, `K=9` b≤8. The PIN12/terminal construction of 17(bbbbbb) (structure-note `:87-109`) uses `b=K-2` to keep those terms strictly below `K+6`. It is a `b=b_min` instrument.

`CLEAN_PROOF_EXCLUDES_B_GT_BMIN=NO`. Action: per-stratum charts.

## 2. LEVEL-4 top band for every residual `b`, not only `b_min`

`H^2|P^3` with `deg_y P≤K-1` is equivalent to `y^{smin}(y-x)|P` for `smin=ceil(2(K-1)/3)`. Write

```text
P = y^{smin} (y-x) Q ,   d = b-smin-1 ,   ymax_Q = K-2-smin .
```

At `K=7,8,9` one has `ymax_Q=1`, so `Q=q0 x^d + q1 x^{d-1} y` (omit `q1` when `d=0`). This is the full LEVEL-4 locus, not a slice: extra `y` or `(y-x)` factors of `Q` are the loci `q0=0` and `q0 x+q1 y ∥ (y-x)`. The one-scalar pin of the tower (`:368-378`) is exactly `d=0`, i.e. `b=b_min` (`MARK_T2_PIN_ONLY_AT_BMIN`).

Cover of `P≠0` (exact degree `b`, not the cumulative cap `deg β≤b`):

```text
q0-chart:  q0 * q0_inv - 1          (q1 free)
q1-chart:  q0 = 0,  q1 * q1_inv - 1
```

Rabinowitsch localizers, not dropped unknowns. Jacobian `c≠0` is `CSTP-1`. No `G_m` is consumed on the I_light charts (the hensel probe below does name one, and is not used for a row verdict).

## 3. I_light chart (what was actually solved)

Driver `box/k4ray-beta-strata-20260905/strata_chart.py`, cloned from the charged `pinned_chart.py` with the two-scalar top and general `b`.

```text
h  = y^{K-1}(y-x) + sum_{i+j<=K-1, (i,j)≠(0,K-1)} h_ij x^i y^j
B  = 2P + sum_{i+j<=b-1, j<=K-1} B_ij x^i y^j          (B=2β)
Al = quo_y(B^2,h),  Rh = B^2-Al h
I_light = < non-x^4 coeffs of ID6 J,
            coeffs of (Rh - (4/3) y^{3 smin-2K+2}(y-x) Q^3) in degrees >= 3b-2K,
            CSTP-1,  q_j q_j_inv-1 >
```

The lower β-block is `mons(b-1,K-1)`: every monomial with total degree `≤b-1` and `y`-degree `≤K-1`. No D2-style weight floor. Dropping the MASTER cutoff rows is dropping ROWS (safe): a unit of `I_light` kills the theorem-cut ideal. The converse is not used. Coefficient field `Q`. Ring map: `RR=Q[x,y,params]` with `dp`, `SS=Q[params]` with `wp(tower weights)`, `ROWS=imap(RR,I0)`, `CSTP=imap(RR,CST)`. Names are not a proof; every prelude that reached GB printed `TARGET_FOUND 1` and `CSTP_ZERO 0`. Promotion: `PromotionPolicy.exact_q` only. Modular fibres are F_p-only.

Control: `K=7,b=5` (the banked one-scalar chart) → `UNIT_IDEAL_CHAR0` in 7.78 s, 149 rows = 108 J + 46 rho, 44 GB variables, matching `k4ray-pinned-chart-gpt55-20260903.md:154-169`.

## 4. Sizes, reported honestly

Geometric = `#h + #lower β + #Q`. GB count adds one localizer (no `λ`). 17(bbbbbb) reduced K=8 b=6 / K=9 b=7 to **36** variables by PIN12+terminal; the unreduced top-pin light rings were 58 / 74.

```text
K  b   h  lowerβ  #Q  geom  GB   formed rows (q0)  SIZE_J    form wall
7  5  27   15      1   43    44   149              (banked)  0.056s   [b_min UNIT]
7  6  27   21      2   50    51   178               62757    0.55s
7  7  27   28      2   57    58   198              188515    4.7s
7  8  27   35      2   64    65   219              376761    22.4s
7 13  27   70      2   99   100   not formed
8  6  35   21      1   57    58   17(aaaaaa) light            [b_min; 36-var UNIT in 17(bbbbbb)]
8  7  35   28      2   65    66   241              236710    6.5s / 7.0s fleet
8  8  35   36      2   73    74   264              680063    71s fleet
8 15  35   92      2  129   130   FORMATION_TIMEOUT at 180s (no PRE markers)
9  7  44   28      1   73    74   17(aaaaaa) light            [b_min; 36-var UNIT in 17(bbbbbb)]
9  8  44   36      2   82    83   314              824908    100s fleet
9 17  44  117      2  163   164   FORMATION_TIMEOUT at 180s (no PRE markers)
```

q1-charts are one variable smaller (q0 omitted). At `b=b_max` the I_light Jacobian did not finish `coef(J,x*y)` in 180 s, matching the charged high-K observation that the monolithic full-stratum `J` is not a cheap continuation. K=8 b=8 and K=9 b=8 fleet jobs spent formation inside `coef` (`SIZE_J` 6.8e5 / 8.2e5) and had not printed `GG__STD_BEGIN` at the last poll.

## 5. Why the 36-variable PIN12 cut is not available above `b_min`

`box/k4ray-beta-strata-20260905/hensel_probe.py` row-reduces DIV=`B^2-A h-R_forced` from degree `2b-1` down, the 17(bbbbbb) Hensel step (`hensel_reduced_sol56.py:332-401`).

- **1-scalar shapes** (`q0=0,q1=1` = the whole q1-cover after `G_m`; and the slice `q0=1,q1=0`): pivot matrices lie in `Q`. Free counts after RREF: K=7 b=6 q1 → 35 free + `tau`; K=7 b=6 `q1=0` → 24; K=8 b=7 q1 → 48. The `q1=0` count is a slice of the q0-cover, not a cover.
- **Generic q0-cover** (`q0=1`, `q1` free): already the first DIV band has `q1`-dependent columns (K=7 b=6: 9 of 12 rows, 5 of 17 columns constant). The constant-matrix RREF does not transfer. Working over `Q(q1)` was not completed as a certificate.

A reconstructed-`h` Singular prelude for the 1-scalar RREF hit Singular's long-line parser (`poly ^ number` on a 17 289-character assignment) and produced a **fake unit** via `tau*CSTP-1` with `CSTP≡0` / `TARGET_FOUND 0`. That run is discarded (`HENSEL_K7_B6_Q1`, `HENSEL_K7_B6_Q1_v2`). A sympy-extracted `J`-row path (`v3`) did not finish extracting `J` in 3+ minutes and was killed. **No hensel GB verdict is promoted.**

msolve: `export_msolve.py` dumped the K=7 b=6 q1 I_light fibre over `F_32003` (50 vars, 174 gens, 945 KB `.ms` after renaming `h_i_j` → `v0,v1,…` because msolve forbids underscores). That is an emitter, not a finished Groebner run in this report unless a result file is cited in §6.

## 6. Solves

All main exact-Q jobs go through `guided_gb` with `PromotionPolicy.exact_q`. A timeout is a timeout. A modular unit would still need exact Q. A modular **non-unit** would be a Q non-unit; none occurred.

```text
tag                         K b pin  field     GB  rows  wall      verdict
CTRL_K7_B5_Q0               7 5 0    Q          44  149     7.78s  UNIT_IDEAL_CHAR0
K7_B6_Q0_LIGHT_c0           7 6 0    Q          51  178      600s  INCONCLUSIVE_TIMEOUT
K7_B6_Q1_LIGHT_c0           7 6 1    Q          50  172      600s  INCONCLUSIVE_TIMEOUT
MOD_K8_B7_Q0                8 7 0    F_32003    66  241      180s  INCONCLUSIVE_TIMEOUT
FLEET_K7_B6_Q0_Q            7 6 0    Q          51  178     1800s  INCONCLUSIVE_TIMEOUT
FLEET_K7_B6_Q1_Q            7 6 1    Q          50  172     1800s  INCONCLUSIVE_TIMEOUT
FLEET_K8_B7_Q0_Q            8 7 0    Q          66  241     1800s  INCONCLUSIVE_TIMEOUT
FLEET_K8_B7_Q1_Q            8 7 1    Q          65  235     1800s  INCONCLUSIVE_TIMEOUT
FLEET_K8_B8_Q0_P32003       8 8 0    F_32003    74  264     1200s  INCONCLUSIVE_TIMEOUT
FLEET_K9_B8_Q0_P32003       9 8 0    F_32003    83  314     1200s  INCONCLUSIVE_TIMEOUT
```

Fleet instance `i-01de3f3912cb345f7` (`r7i.8xlarge`, 32 vCPU / 256 GiB). Every extra-stratum `std` that this lane started printed `GG__STD_BEGIN` and then hit the wrapper timeout with no `GG__UNIT` / `GG__DIM`. Summaries: `box/k4ray-beta-strata-20260905/fleet-results.json`. The worker was terminated by this lane (`fleet.sh term i-01de3f3912cb345f7` → `shutting-down`). No other `jc2fleet` instance was touched. The K=7 b=5 unit is exact Q, `reduce(1,G)=0`, not a modular lift.

msolve on the worker refused at the version gate (`MsolveVersionUnsupported` on `/usr/bin/msolve`); that is an emitter-plus-version-mismatch, not a mathematical non-unit.

## 7. Lane verdict (task 3)

```text
K=8 no-split row DEAD for ALL deg β?     NO.
K=9 case (A) DEAD for all deg β?         NO.
D=108 no-split arm restored?             NO  (still conditional on deg β = b_min = 6).
(99,66) configuration (A) restored?      NO  (still conditional on deg β = b_min = 7).
```

Banked coverage, unchanged by this lane:

- composite arm: `deg β=0` only
- `3b≤2K`: `b<b_min`
- pinned/PIN12 charts: `b=b_min` (K=7 I_light unit; K=8,9 36-var units of 17(bbbbbb))

**Open extra strata** (this lane; sizes are GB variables on the q0-cover I_light ring, plus the q1-cover of one fewer variable). None is a measured non-unit.

```text
K=7:  b=6 (51), 7 (58), 8 (65), 9 (72), 10 (79), 11 (86), 12 (93), 13 (100)     — 8 strata
K=8:  b=7 (66), 8 (74), 9 (82), 10 (90), 11 (98), 12 (106), 13 (114), 14 (122), 15 (130)  — 9
K=9:  b=8 (83), 9 (92), 10 (101), 11 (110), 12 (119), 13 (128), 14 (137), 15 (146), 16 (155), 17 (164)  — 10
```

K=7 b=6 both covers and K=8 b=7 both covers are measured exact-Q timeouts at 1800 s on an `r7i.8xlarge`, not absences of a chart. K=8 b=8 and K=9 b=8 are measured `F_32003` timeouts at 1200 s after formation (`SIZE_J` 6.8e5 / 8.2e5). `b=b_max` I_light charts did not finish Jacobian coefficient extraction in 180 s.

## 8. FALLACY-v2

- **Carrier/attainment.** A chart at `b=b_min` is not the residual. This lane does not promote the banked K=8/K=9 units to “all deg β”.
- **Floor/attainment.** `3b≥2K+1` is a floor. LEVEL 4 is a necessary shape, not a kill (`k4ray-degree-tower-opus5-20260903.md:418-424`).
- **Dropping rows vs unknowns.** I_light omits MASTER cutoff rows (safe). The lower β-block does not apply a weight floor. Localizers are extra generators, not deleted coordinates.
- **Group element.** I_light uses Rabinowitsch `q_j q_j_inv-1` and `CSTP-1`. The hensel probe’s `G_m: q_j=1` is named and is not used for a promoted unit.
- **Modular unit.** None promoted. Timeouts on `F_32003` are not units. msolve over `F_32003` is a screen.
- **Variable/ring map.** Declared in §3. `imap` images; `TARGET_FOUND 1` on every prelude that entered `std`.
- **`sat()`.** Unused.
- **Fake unit.** The broken hensel prelude with `CSTP≡0` is recorded and discarded.

No exit claim.

## 9. Artifacts

```text
box/k4ray-beta-strata-20260905/frozen-inputs.sha256
box/k4ray-beta-strata-20260905/frozen-inputs.check.log
box/k4ray-beta-strata-20260905/argument_analysis.py
box/k4ray-beta-strata-20260905/argument-analysis.out
box/k4ray-beta-strata-20260905/argument-census.json
box/k4ray-beta-strata-20260905/strata_chart.py
box/k4ray-beta-strata-20260905/hensel_probe.py
box/k4ray-beta-strata-20260905/hensel_chart.py
box/k4ray-beta-strata-20260905/export_msolve.py
box/k4ray-beta-strata-20260905/fleet_parallel.sh
box/k4ray-beta-strata-20260905/runs/CTRL_K7_B5_Q0/
box/k4ray-beta-strata-20260905/runs/K7_B6_Q0_LIGHT_c0/
box/k4ray-beta-strata-20260905/runs/K7_B6_Q1_LIGHT_c0/
box/k4ray-beta-strata-20260905/runs/MOD_K8_B7_Q0/
box/k4ray-beta-strata-20260905/fleet-instance-id.txt   # i-01de3f3912cb345f7, terminated
box/k4ray-beta-strata-20260905/fleet-results.json
box/k4ray-beta-strata-20260905/fleet-pull/runs/FLEET_*/
```

Reproduction (I_light):

```bash
python3 -u box/k4ray-beta-strata-20260905/argument_analysis.py
python3 -u box/k4ray-beta-strata-20260905/strata_chart.py run CTRL_K7_B5_Q0 7 5 --timeout 120 --cores 4
python3 -u box/k4ray-beta-strata-20260905/strata_chart.py count FORM_K8_B7_Q0 8 7 --timeout 180
# exact Q on an extra stratum (expected timeout at 10 min on 16 cores):
python3 -u box/k4ray-beta-strata-20260905/strata_chart.py run K7_B6_Q0_LIGHT_c0 7 6 --pin-index 0 --timeout 600 --cores 4
```

Grep: `MARK_T3_LEAD_J_VANISHES`, `CLEAN_PROOF_EXCLUDES_B_GT_BMIN`, `UNIT_IDEAL_CHAR0`, `INCONCLUSIVE_TIMEOUT`, `TARGET_FOUND 1`.

<!-- BODY-END -->
