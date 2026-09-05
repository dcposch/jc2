# Census sweep: reusable kill pipeline on the smallest u_s ≥ 2 classes

Lane `census-sweep-grok46-20260905`, receipt basis `b478879ba7180c3829a5fcc863ea2c25552d3460`.
Charged inputs verified against `xmodel/census-sweep-grok46-20260905.run.v2`
by `awk`-generated manifest + `sha256sum -c`: **10/10 OK**, no content mismatch.

## 0. Headline

1. **`box/lib/census_sweep.py` is committed** (1822 lines). It enumerates
   Moh (1)–(13) skeletons, descends by Prop 6.3/6.4, classifies split/unsplit,
   sizes the full necessary chart (Theorem-1.2 D1 + outer-disc completion),
   emits via `order_basis_full` **through the fixed builder** (`builder_fix.py`:
   unknowns in the polynomial ring, y-monic `division()`), extracts, and
   solves with `guided_gb` exact-Q (msolve optional, never promoted). A class
   is DEAD only if every fibre is UNIT, the chart is the full necessary
   over-approximation, and the unit is characteristic zero.
2. **Census, measured on the frozen enumerator.** At Kmin=16 and
   48 ≤ n ≤ 200: 23,720 raw (1)–(13) rows, **6,117 with u_s ≥ 2**. Fibre-complete
   descended keys `(n',m',M',ell,s',V')` are 1:1 with those rows (6,117).
   Grouping by `(n',m',M',ell)` gives **4,012** (the h1-nonres raw-group
   count). Four-int keys `(n',m',ell,V₂')` are **1,291**. Coarse `(n',m',ell)`
   keys are **523**. The synthesis figure 6,209 → 1,359 is **not** reproduced
   on this grain; the Astra correction **296 xu_ok_candidate records → 132
   four-int keys is reproduced exactly** (0 unmatched).
3. **Controls, all passed, via the sweep's certificate writer.** D=108 δ=3
   common-h₃ incidence: exact-Q UNIT (dim −1). (99,66) δ=2 stage-4: exact-Q
   UNIT (the 6264 generator). K=8 no-split pin+lower-band and K=9 case-A
   internal A: exact-Q UNIT. A genuine tame automorphism **survives**
   (dim 0, non-unit).
4. **Sweep of the 19 smallest source-complete classes (nunk ≤ 80):**
   **k = 14 DEAD of N = 19**, all unsplit, all exact-Q `UNIT_IDEAL_CHAR0`.
   Two of the 14 have Jacobian identically 0 on an x-free D1 support
   (J=c is impossible). Twelve have 27–39 genuine coefficient equations
   and die in < 1 s. Five TIMEOUT: two mixed (split-window) order charts
   at 67 and 71 unknowns (75 and 68 equations, 180 s exact-Q std), and
   three unsplit charts at 79 unknowns with x-degree 1 (57–61 equations).
5. **Compute-bound threshold.** For a *real* Jacobian order chart (x-support
   present, 60+ equations) the 180 s exact-Q `std` wall is already hit at
   **67 unknowns**. The lesson that “≤ ~120 unknowns finish in
   seconds–minutes” holds for the ell=0 x-free unsplit charts in this
   bucket, not for mixed joint-necessary order charts. The joint chart
   remains required for every nonempty split window (FALLACY-v2:
   conjunctive stems).

No `charge_basis` line. This lane asserts no new exit price. It consumes
the banked D=108 / (99,66) / k=4-ray units and records order-chart
emptiness of 14 unsplit descended classes.

## 1. Frozen-input verification

The receipt `xmodel/census-sweep-grok46-20260905.run.v2` carries
`charged_input_<i>_sha256=` / `_basename=` lines and
`lane_inputs_dir=/tmp/jc2-lane.UrqJiB/inputs`. The manifest was built
with `awk`, not transcribed:

```bash
receipt=xmodel/census-sweep-grok46-20260905.run.v2
inputs=/tmp/jc2-lane.UrqJiB/inputs
awk -F= -v dir="$inputs" '
  /^charged_input_[0-9]+_sha256=/ {
    n=$1; sub(/^charged_input_/,"",n); sub(/_sha256$/,"",n); sha[n]=$2
  }
  /^charged_input_[0-9]+_basename=/ {
    n=$1; sub(/^charged_input_/,"",n); sub(/_basename$/,"",n); bn[n]=$2
  }
  END { for (i=1; i<=10; i++) printf "%s  %s/%s\n", sha[i], dir, bn[i] }
' "$receipt" > /tmp/charged-manifest.sha256
sha256sum -c /tmp/charged-manifest.sha256
```

All ten lines returned `OK`. Digests match the prompt byte-for-byte.

## 2. The library

`box/lib/census_sweep.py` is the reusable box. CLI:

```text
python3 box/lib/census_sweep.py enumerate --nmin 16 --nmax 200 --kmin 16
python3 box/lib/census_sweep.py controls  --dest box/census-sweep-20260905
python3 box/lib/census_sweep.py sweep     --limit 19 --max-unknowns 80
python3 box/lib/census_sweep.py run-class --class-id C_...
```

Pipeline per class:

| step | instrument | rule |
|---|---|---|
| enumerate | `moh_skeleton_full.census(..., full=True)` | (1)–(13), fail-closed on the frozen file |
| descend | Prop 6.3/6.4 | `u_s = d_s − V_s`, `(n',m') = (n,m)·u_s/d_s`, `ell = v_s − u_s − 1` (ERRATUM 17(dddddd): not `n'−M₂'−2`) |
| classify | split window | `1 < a/b < v_s/u_s`, `1 ≤ b ≤ u_s`; genuine split needs a partition of `u_s` with ≥ 2 parts. Nonempty window ⇒ mixed (split fibres **and** unsplit descent). Empty window ⇒ unsplit only. |
| size | `sprime3_compiler` inventories | source-complete = Theorem-1.2 D1 ∪ outer-disc; k=4-ray shape (ell=4, u=1, e=3, q=2, K≥7) sized at 36 (pin+lower-band); mixed sized at least the order chart |
| emit | `sprime3.build_spec` + `builder_fix.fix_text` | free leading `y^K`, `B_safe`, no tot-degree cap; unknowns in the polynomial ring under `(lp(1),dp)` |
| extract | Singular native builder | `NATIVE_GATE lead_h_is_yK=1` required; header-only TSV is not “0 equations” |
| solve | `guided_gb` exact Q | `PromotionPolicy.exact_q`; modular `[1]` is `MODULAR_UNIT_NOT_PROMOTED`. Optional msolve `-g 2` is a screen only. |
| certificate | `census-sweep-class-certificate-v1` JSON | class DEAD iff **every** stem UNIT **and** kind is unsplit (or a registered joint engine UNIT on every split fibre) |

Union UNIT of an order chart implies every unsplit fibre UNIT (one
direction). The converse does not hold. For mixed/split classes an order
UNIT is recorded as `unsplit_order_unit=true` and the class stays OPEN:
the joint chart (order + minor-incidence + pole + Jacobian) is still
required. That is the 17(rrrrrr) lesson, encoded rather than restated.

Registered joint/k=4-ray engines (replayed, not analogised):

| id | chart | nunk | expected |
|---|---|---:|---|
| `D108_delta3` | common-h₃ minor incidence | 4 | UNIT |
| `G9966_delta2_stage4` | (99,66) δ=2 stage-4 | 2 | UNIT |
| `K8_d108_nosplit` | pin+lower-band, 36 vars | 36 | UNIT |
| `K9A_9966_unsplit` | pin+lower-band, 36 vars | 36 | UNIT |
| `CTRL_GENUINE_TAME_AUTOMORPHISM` | J=const tame auto | 2 | SURVIVES |

## 3. Enumeration

Command (17.95 s on math-hq):

```text
python3 box/lib/census_sweep.py enumerate \
  --dest box/census-sweep-20260905 \
  --nmin 16 --nmax 200 --kmin 16 \
  --xufloor box/xufloor-20260903/results.json
```

Kmin=16 with e = n/K ≥ 3 forces n ≥ 48, so “16 ≤ n ≤ 200” is the Kmin
convention of 17(ll), not a degree floor of 16.

| layer | count |
|---|---:|
| raw (1)–(13) rows | 23,720 |
| u_s ≥ 2 rows | 6,117 |
| descended fibre keys `(n',m',M',ell,s',V')` | 6,117 |
| groups `(n',m',M',ell)` | 4,012 |
| four-int keys `(n',m',ell,V₂')` | 1,291 |
| coarse keys `(n',m',ell)` | 523 |
| unsplit / mixed | 2,363 / 3,754 |
| k=4-ray shape (ell=4, u=1, (e,q)=(3,2), K≥7) | 6 |
| xu_ok_candidate u_s>1 records | 296 |
| four-int keys of that cohort | **132** |

The 6,117 u_s ≥ 2 rows match h1-nonres (`raw with u_s ≥ 2`: 6,117 rows /
4,012 groups). Fibre-complete descent does not compress: each row has a
unique `(M',V')`. Compression lives at coarser grains.

The 17(eeeeee) “6,209 → 1,359 (4.57×)” figure is a different grain than
any of the four measured here. This lane does not silently identify it
with 1,291 or 4,012. The number that *is* gated is the Astra correction
of the sharpened cohort: 296 records, 132 keys, 0 unmatched against the
frozen enumerator.

Solvable-nunk histogram (source-complete, or k=4-ray 36, or joint-at-least-order):

| bucket | classes |
|---|---:|
| ≤ 80 | 19 |
| 81–120 | 135 |
| 121–200 | 841 |
| > 200 | 5,122 |

Zero classes sit at ≤ 40. The 19 in ≤ 80 are the sweep.

## 4. Controls (via the sweep)

```text
python3 box/lib/census_sweep.py controls \
  --dest box/census-sweep-20260905 --timeout 180
```

Wall clock 7.9 s. All five passed.

| control | engine | dim | unit | verdict |
|---|---|---:|:---:|---|
| D=108 δ=3 common-h₃ incidence (`death_replay.sing`) | Singular exact Q | −1 | yes | UNIT |
| (99,66) δ=2 stage-4 (`stage4.sing`, generator 6264) | Singular exact Q | −1 | yes | UNIT |
| K=8 D=108 no-split pin+lower-band | `guided_gb` exact Q | −1 | yes | UNIT |
| K=9 case A internal A | `guided_gb` exact Q | −1 | yes | UNIT |
| genuine tame auto `(f,g)=(x²−y, x)` | `guided_gb` exact Q | 0 | no | SURVIVES |

The D=108 script prints `MAIN_DIM` / `MAIN_NF1`; the (99,66) script prints
`BEGIN_DIM` / `BEGIN_GB`. The sweep parser accepts both envelopes and the
`GG__` markers. Certificates live at
`box/census-sweep-20260905/controls/<id>/certificate.json`.

The tame control is the required negative: a genuine automorphism is
dim-0 non-unit, not a unit ideal. Forward and inverse maps print as 0
on `x` and `y`.

These are replays of banked necessary charts, not new joint compilers.
A D=108-style incidence is **not** copied onto other (3,2)-ratio rows
by analogy (FALLACY-v2 pole/interior and variable/ring map).

## 5. Sweep of the 19 smallest classes

Sorted by source-complete unknown count. All 19 emitted through
`builder_fix`. Extract always passed `lead(h)=y^K`. Solve is exact Q
via `guided_gb`; no modular unit was promoted.

### 5.1 Fourteen DEAD (unsplit, exact-Q unit)

| nunk | eqs | jac ≡ 0 | class (descended) | ancestor |
|---:|---:|:---:|---|---|
| 55 | 1 | yes | `C_n32m24_Mm20_m6_ell0_s3_V1_6` | (80,60) |
| 59 | 1 | yes | `C_n36m24_Mm18_m8_ell0_s3_V2_9` | (90,60) |
| 59 | 27 | no | `C_n32m24_Mm20_2_ell0_s3_V1_6` | (80,60) |
| 61 | 35 | no | `C_n36m24_Mm16_m2_ell0_s3_V1_6` | (90,60) |
| 63 | 27 | no | `C_n36m24_Mm8_2_ell0_s3_V5_6` | (90,60) |
| 63 | 27 | no | `C_n36m24_Mm18_2_ell0_s3_V2_9` | (90,60) |
| 71 | 35 | no | `C_n36m24_Mm16_6_ell0_s3_V1_6` | (90,60) |
| 76 | 39 | no | `C_n40m32_Mm12_2_ell0_s3_V1_6` | (100,80) |
| 79 | 39 | no | `C_n40m24_M14_ell0_s2_V12` | (100,60) |
| 79 | 39 | no | six further `(40,24)` ell=0 fibres with 39 eqs | (100,60) |

All have empty split windows (unsplit), ell=0 (descended Jacobian J=c),
and exact-Q `UNIT_IDEAL_CHAR0` with `nf_all_zero`, `dim=-1`, `basis_size=1`,
`accepted=true`. Solve wall is 0.008–0.36 s on the 27–39 equation charts
and 0.008 s on the two 1-equation charts.

**The two 1-equation units are not vacuous builder failures.** The D1
inventory at δ₁' = 0 (or too small to admit x-powers) is polynomials in
y only. Then P and Q are functions of y, J(P,Q) ≡ 0, and J=c with
saturation `T·c−1` is the unit ideal. The builder gate
`level0_deg_x_before_minus_c=-1` records that the Jacobian polynomial
was zero *before* subtracting c. That is a genuine obstruction on this
chart: no point realises a nonzero constant Jacobian. The other twelve
have `target_xk_level0_nonzero=1` and 27–39 nonzero coefficient rows;
those are ordinary exact-Q units, not the identically-zero case.

These kills are **order-chart emptiness of the unsplit descended arm**.
They are not Keller counterexamples, not joint-chart kills, and not a
degree-wide theorem.

### 5.2 Five TIMEOUT

| nunk | eqs | kind | x-deg | class | note |
|---:|---:|---|---:|---|---|
| 67 | 75 | mixed | 4 | `C_n18m12_Mm3_ell3_s2_V2` | (60,40), window `{4/3,3/2,5/3,2}`; 180 s std, no unit |
| 71 | 68 | mixed | 2 | `C_n24m16_Mm4_6_ell1_s3_V5_8` | (72,48), window `{3/2}`; 180 s |
| 79 | 61 | unsplit | 1 | `C_n32m24_Mm12_14_ell0_s3_V1_6` | 180 s |
| 79 | 61 | unsplit | 1 | `C_n32m24_Mm12_14_ell0_s3_V7_6` | extract 61 eqs, same band |
| 79 | 57 | unsplit | 1 | `C_n36m24_Mm18_14_ell0_s3_V2_9` | extract 57 eqs, same band |

The two mixed classes are the first *real* Jacobian systems in the size
order (x-degree 4 and 2, 68–75 equations). Exact-Q `std` produced no
`GG__UNIT` and no dimension marker in 180 s. Because they have nonempty
split windows, even an order UNIT would not have been a class kill.

The three 79-unknown unsplit charts with x-degree 1 are the first ell=0
charts whose Jacobian has an x-factor. They sit on the other side of
the wall from the 39-equation x-degree-0 charts that died in < 1 s.

No NON-EMPTY point was extracted. Nothing in this lane is a
counterexample candidate. TIMEOUT is not survival.

### 5.3 Fleet

Workers `172.30.0.7`, `.18`, `.28` answered SSH (c7i, 32 vCPU / 61 GiB,
Singular 4.3.2, msolve present, `~/PROVISION_DONE`). Dependencies
(`census_sweep.py`, `builder_fix.py`, `sprime3_compiler.py`,
`guided_gb.py`, `moh_skeleton_full.py`, `order_basis_full.py`) rsynced
and imported. First remote launch failed: relative `--dest` made
`Path.relative_to(ROOT)` raise (`'box/census-sweep-...' is not in the
subpath of '/home/ubuntu/jc2'`). Fixed by resolving dest to absolute.
A second launch hit a 20 s SSH timeout under concurrent k16 load on
the workers. The 19-class bucket was therefore finished on math-hq
(123 GiB, Singular 4.3.2), which is the same CAS stack. Controls and
the 14 units are exact-Q Singular, independent of msolveio (absent on
`.18`/`.28` and on math-hq). No unwaited local background job was
left running; worker k16 jobs were not killed.

## 6. Tally and the size wall

**k = 14 classes DEAD of the swept N = 19**, plus five TIMEOUT, plus
five controls (4 UNIT, 1 SURVIVES).

Size threshold where the sweep becomes compute-bound, for a *necessary
order chart with x-support*:

```text
67 unknowns / 75 equations / exact-Q std / 180 s → TIMEOUT
```

Below that, ell=0 x-free unsplit charts (1–39 equations, nunk 55–79)
die in milliseconds to 0.4 s. The 17(ssssss)/(uuuuuu) wall at 88–378
unknowns for s'≥3 Moh residual charts is consistent with this: the
first mixed Jacobian in the u_s≥2 size order is already stuck at 67.
The k=4-ray pin+lower-band reduction to 36 variables remains the
validated route for the six ell=4 (3,2)-sheet unsplit descendants
(K=8 and K=9 already UNIT as controls; the other four have
source-complete nunk 402–4,889 and were not in this bucket).

Joint charts for mixed classes were **not** synthesised by copying the
D=108 incidence. Those two mixed TIMEOUT rows stay OPEN on the joint
side. Their unsplit order charts timed out rather than uniting, so
there is no unsplit_order_unit to record.

## 7. FALLACY-v2 checks

- **Full necessary chart.** Emit uses source-complete inventories
  (Theorem-1.2 D1 ∪ outer-disc), free leading `y^K`, `B_safe` (never
  `B_tight`). Tot-degree envelope is not used. The two jac≡0 units are
  on that full support, not on a deleted-x sub-slice: x-powers are
  *not D1-allowed* at those (δ₁', B_safe).
- **Every stem UNIT, conjunctive.** Unsplit: one fibre, union UNIT
  implies the fibre UNIT. Mixed: order UNIT would not have been
  promoted to class DEAD; the two mixed rows timed out anyway.
- **Exact-Q confirm.** Every DEAD certificate has
  `guided_verdict=UNIT_IDEAL_CHAR0`, `characteristic=0`,
  `promotion=EXACT_Q`. Modular units are not promoted
  (`allow_modular_unit_promotion=False`).
- **sat() wrapping.** Saturation is the explicit generator `T*c−1`
  (resp. `Zc*c−1`, `Zrho*rho−1` on the joint replays), on a declared
  ring, with empty/nonempty controls in the guided prelude.
- **Variable/ring map.** Builder_fix ring
  `R=0,(y,x,params),(lp(1),dp(N+1))` is declared; matching names are
  not treated as a theorem. Control scripts keep their own rings.
- **Floor/attainment.** den(δ) ≤ u_s is tagged as Xu's working bound,
  not a theorem. 1,359 is not identified with 1,291. REPRESENTATIVE
  fibre is not FULL_ACTUAL: the class chart is the union.
- **Prime mark.** ell is the Prop 6.3(3) exponent, a label, not a
  derivative.
- **No new exit price.** No `charge_basis` line.

## 8. Reproduction

```bash
# hashes
awk -F= -v dir=/tmp/jc2-lane.UrqJiB/inputs '...'  # as §1
sha256sum -c /tmp/charged-manifest.sha256

# controls (~8 s)
python3 box/lib/census_sweep.py controls \
  --dest box/census-sweep-20260905 --timeout 180

# census (~18 s)
python3 box/lib/census_sweep.py enumerate \
  --dest box/census-sweep-20260905 --nmin 16 --nmax 200 --kmin 16

# one small unsplit class (~1 s)
python3 box/lib/census_sweep.py run-class \
  --dest box/census-sweep-20260905 \
  --class-id C_n32m24_Mm20_2_ell0_s3_V1_6 \
  --extract-timeout 180 --solve-timeout 180 \
  --support source-complete
# expected: class_verdict=DEAD, equations=27, UNIT_IDEAL_CHAR0
```

Library SHA-256:
`700bfeb07ceb84d9afcaa7504f7007c5a285a9f78bae0623e5ff2c790f7af206`.

## 9. Artefacts and scope

Committed: `box/lib/census_sweep.py`;
`box/census-sweep-20260905/tally.json`,
`inventory-summary.json`, and the five control certificates.
Not committed: `inventory.json` (13 MB row dump), class
builders/rows/jobs (regenerable). Certificates for the 19 swept
classes sit on disk at
`box/census-sweep-20260905/classes/*/certificate.json`.

This lane edited only `box/lib/` and `box/census-sweep-20260905/`.
No other ledger, no `jc2-lean`, no `ideation-*`.

What this does **not** do: close the u_s ≥ 2 census; compile a general
joint incidence engine; kill mixed classes; promote a modular unit;
treat 1,359 as a measured key count; treat an order-chart unit of a
split-window class as a class kill.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17276`.
- Body SHA-256:
  `ead095d0d56c5a8d26af32f1ab9dea104379f2b05c921710d8ce54957e6d5b1a`.
- Frozen basis: `b478879ba7180c3829a5fcc863ea2c25552d3460`.
