# Operative sweep: exact-Q harvest on the 1,420-row residual

Lane `operative-sweep-grok46-20260905`, receipt basis
`ad9888e36073ad66695e559482d3bf154d6f34b2`. Charged inputs verified against
`xmodel/operative-sweep-grok46-20260905.run.v2` by `awk`-generated manifest +
`sha256sum -c`: **9/9 OK**, no content mismatch.

## 0. Headline

1. **The operative residual is 1,420 fibre-complete classes**, one per
   `C_FULL_TREE_POLYNOMIAL_ODE` row at `16 ≤ n ≤ 200`, matching child-data
   exactly: **174 live `u_s=1` / 310 `u_s≥2` / 936 (C-TOP)-killed**. (C-TOP)
   stays under gate; the 936 are a separate tier, not promoted kills.
2. **Cheap order-chart kills in this residual: none.** Source-complete
   `nunk ≤ 100` is six (C-TOP) classes plus three live `u_s=1` k=4-ray
   *sort* sizes. The six are ell=1 real Jacobians. Five were emitted through
   the frozen `census_sweep` builder_fix path and dispatched to c7i.4xlarge
   workers: every one **extract-TIMEOUT at 300 s** (`lead(h)=y^K` passed;
   coefficient TSV never written; msolve never reached; exact-Q never
   reached). The sixth is U-NEGATIVE (`V'_2=17 > K'=12`) and was not
   emitted. The three k=4-ray rows sort at 36 unknowns via the pin+lower-band
   *engine type*; their source-complete order charts are 370 / 475 / 593
   unknowns. The validated 36-var scripts are D=108 K=8 and (99,66) K=9, not
   these parents. FALLACY-v2 forbids transporting them.
3. **`u_s≥2` has no class with source-complete nunk ≤ 100.** Minimum is 123
   (unsplit, ell=0). Mixed: 168 classes; `split_window` leaves 77 with
   `≥1` surviving `(ρ,λ)` (cheapest nunk 197) and 91 with empty survivor
   lists (G+L killed every split pair). Order charts cannot kill split
   fibres. D=108 keeps leaf `(ρ,λ)=(3,[1,1])`; (99,66) keeps `(2,[2,1])` and
   `(5/2,[1,1,1])` — the campaign's known live branches, recomputed here,
   not transported.
4. **k = 0 classes DEAD of N = 1,420** by exact-Q on the full necessary
   order chart. The 14 DEAD of the prior census-sweep (ell=0 x-free unsplit
   `(1)–(13)` `u_s≥2` at Kmin=16) are **0/14 in this residual**. Those
   kills do not move. Hard-row list = all 1,420 classes.
5. **Controls, all passed, same code path.** Tame automorphism SURVIVES
   (dim 0, non-unit). Two J≡0 order charts
   `C_n32m24_Mm20_m6_ell0_s3_V1_6` and `C_n36m24_Mm18_m8_ell0_s3_V2_9`
   replay as exact-Q UNIT with `jacobian_identically_zero=true` (0.008 s).
   They are not operative rows.

No `charge_basis` line. This lane asserts no new exit price.

## 1. Frozen-input verification

The receipt `xmodel/operative-sweep-grok46-20260905.run.v2` carries
`charged_input_<i>_sha256=` / `_basename=` lines and
`lane_inputs_dir=/tmp/jc2-lane.CnC4TW/inputs`. Manifest built with `awk`,
not transcribed:

```bash
receipt=xmodel/operative-sweep-grok46-20260905.run.v2
inputs=/tmp/jc2-lane.CnC4TW/inputs
awk -F= -v dir="$inputs" '
  /^charged_input_[0-9]+_sha256=/ {
    n=$1; sub(/^charged_input_/,"",n); sub(/_sha256$/,"",n); sha[n]=$2
  }
  /^charged_input_[0-9]+_basename=/ {
    n=$1; sub(/^charged_input_/,"",n); sub(/_basename$/,"",n); bn[n]=$2
  }
  END { for (i=1; i<=9; i++) printf "%s  %s/%s\n", sha[i], dir, bn[i] }
' "$receipt" > /tmp/charged-manifest.sha256
sha256sum -c /tmp/charged-manifest.sha256
```

All nine lines returned `OK`. Digests match the prompt byte-for-byte.

Library SHA-256 (workspace = charged):
`700bfeb07ceb84d9afcaa7504f7007c5a285a9f78bae0623e5ff2c790f7af206`.

## 2. Operative rows and the three-tier partition

Rows from `box/scopeleaks-20260905/scope_enum.json` (`operative_rows`,
1,420). Descent, split-window classification, and source-complete sizing
use the frozen `census_sweep` functions (`descend`, `classify_row`,
`child_closed_form`, `inventory_counts`, `solvable_unknowns`) plus
`sprime3_compiler.drop_p174` for (C-TOP). Split leaves use charged
`box/lib/split_window.py` (`screen_skeleton`).

(C-TOP) after the p.174 drop on the child's `M'` list is `V'_{s'} ≤ d'_{s'}`
at the last effective index. U-NEGATIVE is `V'_2 > d'_2`.

| tier | rows = classes | criterion |
|---|---:|---|
| `live_us1` | **174** | `u_s=1` and (C-TOP) holds |
| `us_ge2` | **310** | `u_s≥2` (C-TOP unlicensed) |
| `ctop_killed` | **936** | `u_s=1` and (C-TOP) fails; **under gate** |

`174+310+936 = 1,420`. Live `u_s=1` by `s'`: `{2:24, 3:100, 4:41, 5:9}`,
46 parent degree pairs — the child-data p.174-effective recount, reproduced.
U-NEG: 0 / 6 / 84 (90 total; the child-data family-(a) close). Fibre-complete
keys are 1:1 with rows (no compression at this grain).

The 14 census-sweep DEAD class-ids (ancestors `(80,60)`, `(90,60)`,
`(100,80)`, `(100,60)`) are **absent** from all three tiers.

## 3. Source-complete sizes, sorted

Sizing is Theorem-1.2 D1 ∪ outer-disc, `B_safe`, free leading `y^K`, through
`builder_fix`. Mixed classes use `joint_at_least_order` (never smaller than
the order chart). k=4-ray *shape* (`ell=4`, `u=1`, `(e,q)=(3,2)`, `K≥7`)
sorts at 36 via the pin+lower-band engine type; the table below reports the
**source-complete order nunk**, which is the chart `emit_order_class` would
actually write.

| source-complete nunk | live_us1 | us_ge2 | ctop_killed |
|---|---:|---:|---:|
| ≤ 80 | 0 | 0 | 1 |
| 81–100 | 0 | 0 | 5 |
| 101–120 | 0 | 0 | 21 |
| 121–200 | 1 | 42 | 189 |
| 201–400 | 23 | 57 | 275 |
| 401–800 | 41 | 47 | 186 |
| > 800 | 109 | 164 | 259 |

Live `u_s=1` smallest *order* nunk is 185 after the three k=4-ray rows
(order 370/475/593). `u_s≥2` minimum is **123**. The only honest
`nunk ≤ 100` order charts sit in the (C-TOP) tier.

## 4. Controls (same code path)

```text
python3 box/operative-sweep-20260905/run.py controls --timeout 180
```

Wall < 1 s. All three passed.

| control | engine | dim | unit | verdict |
|---|---|---:|:---:|---|
| genuine tame auto `(f,g)=(x²−y, x)` | `guided_gb` exact Q | 0 | no | SURVIVES |
| `C_n32m24_Mm20_m6_ell0_s3_V1_6` (J≡0) | `census_sweep.run_class` exact Q | −1 | yes | UNIT, jac≡0, nunk=55, 1 eq, 0.008 s |
| `C_n36m24_Mm18_m8_ell0_s3_V2_9` (J≡0) | `census_sweep.run_class` exact Q | −1 | yes | UNIT, jac≡0, nunk=59, 1 eq, 0.008 s |

Certificates: `box/operative-sweep-20260905/controls/`. SHA-256:
tame `7fb0f83138c5fffc01f6f598bd609b14b9dd061efff3612eea678a7db2a40ac4`;
J0_A `bf515809e9d1eb78b67ae617061d086d3f4853dcafd9a69eabaa90893fbc40a8`;
J0_B `380157e03be6ca55ae9c4debc8a8d05ee0180311b8db4747caef1e9a8298d6aa`.
Schema `census-sweep-class-certificate-v1`. Promotion `EXACT_Q`. The J≡0
pair is the required positive that an x-free D1 Jacobian still dies; the
tame auto is the required negative that a genuine automorphism is dim-0
non-unit. Neither J≡0 class is in the 1,420.

## 5. Sweep of nunk ≤ 100

### 5.1 Five order charts, extract-TIMEOUT at 300 s

Emitted locally through `census_sweep.emit_order_class` (`builder_fix`,
source-complete, `NATIVE_GATE lead_h_is_yK=1` in the builder). Dispatched
one class per c7i.4xlarge (Singular 4.3.2, msolve present). Pipeline per
fibre: extract 300 s, then msolve `-g 2` p=32003 screen, then exact-Q 300 s.
Extract never finished, so msolve and exact-Q did not run.

| nunk | class | parent | wall | extract | lead(h)=y^K | cert SHA-256 |
|---:|---|---|---:|---|:---:|---|
| 77 | `C_n24m16_Mm12_m2_5_ell1_s4_V1_1_6` | (96,64) | 300.367 | TIMEOUT | yes | `58e5fcd1…b45fd4e` |
| 98 | `C_n36m24_Mm18_3_5_ell1_s4_V5_18_9` | (144,96) | 300.367 | TIMEOUT | yes | `f3dc1887…a0c62c43` |
| 98 | `C_n36m24_Mm18_m4_5_ell1_s4_V5_18_6` | (144,96) | 300.166 | TIMEOUT | yes | `d3f5e2d7…341fa6b` |
| 98 | `C_n36m24_Mm18_m4_5_ell1_s4_V7_18_6` | (144,96) | 300.166 | TIMEOUT | yes | `3ce47ac9…7b40e31` |
| 100 | `C_n36m24_Mm18_3_5_ell1_s4_V3_18_9` | (144,96) | 300.167 | TIMEOUT | yes | `8e6a4f1c…16feaa4c` |

All unsplit, ell=1, `s'=4`, fibre_size=1. The 77-unknown class is the
cheapest `s'≥3` receiver named in scope-leaks (parent
`M=(-48,-8,20,94)`, `V=(1,1,6,3)`). Builder log on every worker:

```text
NATIVE_GATE lead_h_is_yK=1
halt 1
```

Rows TSV stayed at the 42-byte header. The gate is line 101 of the
builder; coefficient `write` is after `H0..H33` Jacobian remainders.
TIMEOUT is inside the expansion, not a missing `y^K` leader and not a
vacuous empty TSV treated as “0 equations”.

msolve was installed on every worker (`/usr/bin/msolve`) and was the
specified modular screen. It is not a kill, and it was never reached.

### 5.2 One nunk=98 class not emitted: U-NEGATIVE

`C_n36m24_Mm18_3_5_ell1_s4_V17_18_9`, parent (144,96), `V'_2=17`, `K'=12`,
`u'=-5`. Scope-leaks / Def 5.1(1): no honest chart. Certificate
`class_verdict=OPEN`, reason `U-NEGATIVE_no_honest_chart`, SHA-256
`842ab1e9bae8ae66c32f038fb60d8ba4405b16e5934282d7dc658a1612fe9885`.

### 5.3 Three live k=4-ray rows: 36 is not this chart

| sort nunk | order nunk | class | parent | K |
|---:|---:|---|---|---:|
| 36 | 370 | `C_n21m14_M15_ell4_s2_V6` | (147,98) | 7 |
| 36 | 475 | `C_n24m16_M18_23_ell4_s3_V7_7` | (168,112) | 8 |
| 36 | 593 | `C_n27m18_M21_26_ell4_s3_V8_8` | (189,126) | 9 |

`solvable_unknowns` returns 36 for k=4-ray *shape*. `emit_order_class`
would write the 370–593 unknown order chart. The registered 36-var
scripts (`K8_d108_nosplit`, `K9A_9966_unsplit`) are for parents (108,72)
and (99,66), which in *this* residual are mixed `u_s≥2` classes (below),
not these three. OPEN-compute; engines not transported.

## 6. Split fibres (`u_s≥2` only)

`u_s=1` has no genuine partition of `u_s` with ≥2 parts, so live and
(C-TOP) tiers are unsplit even when the arithmetic window `{2,…}` is
nonempty. Mixed classes exist only in `us_ge2`: **168 mixed / 142 unsplit**.

`split_window.screen_skeleton` on each mixed source:

| survivor `(ρ,λ)` count | mixed classes |
|---:|---:|
| 0 | 91 (4 of these U-NEG; 87 otherwise) |
| 1 | 58 |
| 2 | 9 |
| 3 | 5 |
| 4 | 4 |
| 6 | 1 |

Empty survivor list means G and/or L excluded every raw `(ρ,λ)` pair.
That *does* kill those split fibres (the screen is necessary). The unsplit
Prop 6.3 descent remains. Those 87 non-U-NEG empty-leaf mixed classes are
still OPEN-split in the tally: this lane did not run their unsplit order
charts (all nunk ≥ 123 > 100). A later exact-Q UNIT on the unsplit fibre
would still have to be recorded as unsplit-only.

77 mixed classes keep ≥1 leaf. Cheapest five:

| nunk | class | leaves | `(ρ,λ)` |
|---:|---|---:|---|
| 197 | `C_n36m24_Mm20_6_ell4_s3_V5_14` | 1 | `(3,[1,1])` |
| 206 | `C_n36m24_Mm4_18_ell2_s3_V5_10` | 1 | `(2,[1,1])` |
| 221 | `C_n36m24_Mm20_6_ell4_s3_V1_14` | 1 | `(3,[1,1])` |
| 302 | `C_n36m24_Mm4_18_ell2_s3_V1_10` | 1 | `(2,[1,1])` |
| 318 | `C_n36m24_Mm6_20_ell2_s3_V2_2` | 1 | `(2,[1,1])` |

Sanity against banked split faces, recomputed, not copied:

- D=108 `(108,72)` `C_n24m16_M18_ell4_s2_V7`: mixed, order nunk 475, one
  leaf `(3,[1,1])`. The common-h₃ incidence UNIT is a *joint* chart on
  that leaf; it is not an order-chart class kill.
- (99,66) `C_n27m18_M21_ell4_s2_V8`: mixed, order nunk 593, leaves
  `(2,[2,1])` and `(5/2,[1,1,1])` — the two live branches.

Six `u_s≥2` U-NEG rows: two unsplit empty-window (R forced) and four
mixed `{3/2}` with 0 leaves (TEST 3, (L)). Structurally dead by
child-data; not Groebner DEAD here.

## 7. Tally and the hard-row list

Per tier, a class is in exactly one bucket. DEAD = every fibre exact-Q
UNIT on the full necessary chart. Mixed never DEAD by an order UNIT.

| tier | classes | DEAD (exact-Q) | OPEN-compute | OPEN-split | U-NEG |
|---|---:|---:|---:|---:|---:|
| live `u_s=1` | 174 | **0** | 174 | 0 | 0 |
| `u_s≥2` | 310 | **0** | 140 | 164 | 6 |
| (C-TOP) killed | 936 | **0** | 852 | 0 | 84 |
| **total** | **1,420** | **0** | **1,166** | **164** | **90** |

OPEN-compute 852 in the (C-TOP) tier includes the five extract-TIMEOUTs.
OPEN-split 164 = 168 mixed minus 4 U-NEG mixed (U-NEG takes priority).
OPEN-compute 140 in `u_s≥2` = 142 unsplit minus 2 U-NEG unsplit.

**Hard-row list = every operative class**, with nunk and reason.
Exhaustive JSONL: `box/operative-sweep-20260905/hard-rows.jsonl` (1,420
lines). Named below: every class with source-complete nunk ≤ 120, the
three k=4-ray live rows, and the `u_s≥2` floor.

**(C-TOP) nunk ≤ 120** (27 classes; 5 TIMEOUT, 5 U-NEG, rest OPEN-compute
not attempted):

| nunk | reason | class |
|---:|---|---|
| 77 | extract TIMEOUT 300 s | `C_n24m16_Mm12_m2_5_ell1_s4_V1_1_6` |
| 98 | U-NEGATIVE | `C_n36m24_Mm18_3_5_ell1_s4_V17_18_9` |
| 98 | extract TIMEOUT 300 s | `C_n36m24_Mm18_3_5_ell1_s4_V5_18_9` |
| 98 | extract TIMEOUT 300 s | `C_n36m24_Mm18_m4_5_ell1_s4_V5_18_6` |
| 98 | extract TIMEOUT 300 s | `C_n36m24_Mm18_m4_5_ell1_s4_V7_18_6` |
| 100 | extract TIMEOUT 300 s | `C_n36m24_Mm18_3_5_ell1_s4_V3_18_9` |
| 102 | OPEN-compute | `C_n36m24_Mm18_3_5_ell1_s4_V2_18_9`, `…_m4_5_…_V2_18_6` |
| 107 | OPEN-compute | `…_V1_18_9`, `…_V1_18_6` |
| 108 | OPEN-compute | `C_n42m28_Mm26_3_ell1_s3_V5_6` |
| 110 | OPEN-compute / U-NEG | `C_n30m24_Mm22_1_ell2_s3_V1_8`; U-NEG `C_n40m32_Mm28_m14_1_ell1_s4_V9_12_6` |
| 111–119 | OPEN-compute (and 3 U-NEG) | 14 further (C-TOP) classes; see JSONL |

**Live `u_s=1`:** three k=4-ray OPEN-compute (order nunk 370/475/593);
then `C_n24m16_M12_17_ell1_s3_V3_2` at 185; 170 classes with nunk > 200.

**`u_s≥2` floor:** `C_n48m32_Mm24_m4_10_ell0_s4_V1_1_6` nunk=123,
unsplit, ell=0, parent (120,80) — first unsplit order chart past the
cutoff. 42 classes in 121–200; 164 OPEN-split (min nunk 197); 6 U-NEG.

The prior census-sweep wall (67 unknowns / 75 equations / 180 s exact-Q
`std` on a *real* Jacobian) is consistent with this: the cheapest
operative real-Jacobian charts never reach `std`. Extract of the 77-unknown
ell=1 chart is already past 300 s after the `y^K` gate. TIMEOUT is not
survival and is not a counterexample.

## 8. Fleet

`ops/fleet/fleet.sh launch 6 c7i.4xlarge ondemand` at 14:32Z. Instance
ids `i-0dda84fa149666cf8`, `i-0035eeae12cd0e7f1`, `i-01ba5656dbd7d521c`,
`i-0b059239c80a17b43`, `i-03effc60d705503c0`, `i-07eb0cd6ef9a9bce8`.
All six reached `PROVISION_DONE` (Singular, msolve, `qqstack=ok`).
Workers `172.30.0.{165,59,101,229,102,248}`. Frozen `census_sweep.py`,
`builder_fix.py`, `sprime3_compiler.py`, `guided_gb.py`, and class
builders rsynced; remote `imports_ok`.

The first `setsid` launch via the `dispatch.sh` quoting pattern left the
SSH session attached (remote pid stayed in the login tree). Remaining
four jobs launched with `ssh -n` + `nohup`; all five ran. Sixth worker
idle. After certificates: `fleet.sh term` on those six ids only
(**not** `term-all`). All six `terminated`. No other jc2fleet instance
was touched.

## 9. FALLACY-v2 checks

- **Full necessary chart.** Emit is source-complete D1 ∪ outer-disc,
  free `y^K`, `B_safe`. Tot-degree envelope not used. The five TIMEOUTs
  died in that builder, after `lead(h)=y^K`.
- **Every stem UNIT, conjunctive.** No stem reached exact-Q. Mixed
  classes were not pretended DEAD; split leaves are the `split_window`
  survivor lists.
- **Exact-Q confirm.** Zero DEAD certificates. Modular units are not
  promoted (`allow_modular_unit_promotion=False`). msolve was a screen
  that never ran.
- **Never transport an old-chart unit.** The 14 census-sweep DEAD are
  not in the 1,420. K=8/K=9 36-var scripts were not copied onto
  (147,98)/(168,112)/(189,126). D=108 incidence was not copied onto
  other mixed rows.
- **sat() wrapping.** Guided prelude is `T*c−1` on the declared ring,
  with empty/nonempty controls (reached only on the J≡0 replays).
- **Variable/ring map.** Builder_fix ring
  `R=0,(y,x,params),(lp(1),dp(N+1))` is declared.
- **Floor/attainment.** den(δ) ≤ `u_s` is Xu's working bound.
  REPRESENTATIVE is not FULL_ACTUAL: the class chart is the union.
  (C-TOP) is under gate: 936 rows are a tier, not a kill.
- **Prime mark.** ell is the Prop 6.3(3) exponent, a label.
- **No new exit price.** No `charge_basis` line.

## 10. Reproduction

```bash
receipt=xmodel/operative-sweep-grok46-20260905.run.v2
inputs=/tmp/jc2-lane.CnC4TW/inputs
awk -F= -v dir="$inputs" '
  /^charged_input_[0-9]+_sha256=/ {
    n=$1; sub(/^charged_input_/,"",n); sub(/_sha256$/,"",n); sha[n]=$2
  }
  /^charged_input_[0-9]+_basename=/ {
    n=$1; sub(/^charged_input_/,"",n); sub(/_basename$/,"",n); bn[n]=$2
  }
  END { for (i=1; i<=9; i++) printf "%s  %s/%s\n", sha[i], dir, bn[i] }
' "$receipt" > /tmp/charged-manifest.sha256
sha256sum -c /tmp/charged-manifest.sha256

python3 box/operative-sweep-20260905/run.py inventory
# expected: rows_by_tier live_us1=174 us_ge2=310 ctop_killed=936

python3 box/operative-sweep-20260905/run.py controls --timeout 180
# expected: ALL CONTROLS PASSED; tame survives; both J≡0 DEAD jac0=true

python3 box/operative-sweep-20260905/run.py run-class \
  --class-id C_n24m16_Mm12_m2_5_ell1_s4_V1_1_6 \
  --extract-timeout 300 --solve-timeout 300 --msolve
# expected: class_verdict=TIMEOUT, extract timed_out=true, lead_h_gate=true
```

Inventory SHA-256:
`0ad650bbe1fbc5f35dd659b3f6bf45cc69ef6f9011ccf8d695c4bde0c7e70ef8`.

## 11. Artefacts and scope

`box/operative-sweep-20260905/`: `inventory.json`,
`inventory-summary.json`, `tally.json`, `hard-rows.jsonl` (1,420 lines),
`run.py`, nine class certificates (schema
`census-sweep-class-certificate-v1`), three control certificates, fleet
id/ready/job-map files. Builders for the five TIMEOUT classes are on
disk and regenerable.

This lane edited `box/operative-sweep-20260905/` and this report.
No ledger, no `jc2-lean`, no `ideation-*`. `box/lib/census_sweep.py` was
not modified.

What this does **not** do: close the 1,420-row residual; promote (C-TOP);
promote a modular unit; treat a k=4-ray sort size of 36 as an order-chart
kill; treat an order UNIT of a split-window class as a class kill; claim
the five TIMEOUTs would die given a longer extract; identify the 14
non-operative census-sweep DEAD with this residual.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17931`.
- Body SHA-256:
  `808c71ce5d17a264d1fd327687a0efd51b859ff2a1a2d40362d4db039a209aff`.
- Frozen basis: `ad9888e36073ad66695e559482d3bf154d6f34b2`.
