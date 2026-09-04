# Independent re-implementation gate: the (99,66) joint-chart band engine

Date: 2026-09-04 UTC
Lane: `g9966-independent-engine-opus5-20260903`
Basis: `a41cdf71d7ff217ecfdf859423a72a600421e6fe`

## Result

I rebuilt the joint-chart band engine from the charged **design reports only** and
re-ran both branches. Every published quantity reproduced, and the reproduction is
row-level, not merely dimension-level:

```text
delta=2  : 6704 -> 6689(*) -> 1065 -> 1018 -> 976 -> 942 -> DEAD at stage 4
           118 constant residues; first is  J_d159_k35 = 6264
delta=5/2: 6702 -> 6687(*) -> 1063 -> 1016 -> 974 -> 940 -> 913 -> 894 -> 880
           -> 869 -> DEAD at stage 8;  residue  G_local16_pi^0 = 64
```

`(*)` the charged 15-pivot prefix endpoint is not recomputed as a separate stage in
my engine; §5 explains why it is subsumed (its pivot coordinates are deleted by the
outer `D2` preblock, which my stage 0 imposes).

Both constants, both stage numbers, both label names, the seven stage-8 pivot
variables **and** their `Q*` coefficients (`675,576,477,378,279,180,81` on
`B1c_7_19 ... B1c_7_25`), the per-offset outer `D1` raw/rank sequences
`64/41,52/38,40/33,29/25,20/19,11/11,6/6,3/3`, the joint `Q*` sequence
`0,9,9,9,8,8,8,8,7`, and the formal pre-residue generator counts `915` and `862`
agree exactly with the charged reports. Typed verdict:

```text
CONFIRMED-INDEPENDENTLY[delta=2 STAGE-4 DEATH, residue 6264]
CONFIRMED-INDEPENDENTLY[delta=5/2 STAGE-8 DEATH, residue 64]
CONFIRMED-INDEPENDENTLY[BOTH DIMENSION PATHS, ROW-LEVEL]
GAP[MOH p.208 (16,12) CALIBRATION — chart not in the frozen PDF text layer]
NOT-APPLICABLE[TWO-POINT AUTOMORPHISM OF DEGREES >= 6 — see §8.2]
```

The two chart-wide conclusions this supports (`NO-SURVIVING-BRANCH[DECLARED-(99,66)
-JOINT-CHART]`, and conditionally `NO-KELLER-PAIR-WITH-THE-(99,66)-SKELETON`) still
rest on the *same* five necessity/exhaustiveness gates listed in the charged
stage-8 report §7. Independent re-implementation removes gate 5 (faithful
implementation) and materially strengthens gate 4; it says nothing about gates 1–3.

## 0. Input verification

The receipt `xmodel/g9966-independent-engine-opus5-20260903.run.v2` was parsed
mechanically: `awk` joined each indexed `charged_input_<i>_sha256` to the same
indexed `charged_input_<i>_basename` under `lane_inputs_dir`, streaming a 12-line
manifest to `sha256sum -c`. No digest was retyped. **12/12 OK.** The generated
manifest is `/tmp/manifest.sha256`; the command is reproduced in §9.

## 1. Independence discipline

`box/g9966band-20260903/band_engine.py` was **never opened** — not by `cat`, `sed`,
`grep`, `Read`, or any tool. Nor were `outer_major.py`, `first_global_band.py`,
`major_tower_structure.py`, `joint_probe.py`, `xu_joint_extension.py`, or any
charged JSON result file. The only inputs were the twelve frozen files above.

Concretely, the engine below was written from: global-design §2.1 (the chart 2.1,
the order table, the `K3`/`K2` weight rules), §2.3 (the two minor incidences),
§2.4 (the Jacobian ideal and the ring), §3.1–§3.4 (the reduction targets I had to
match); outer-bridge §2 (the `D2`/`D1` thresholds and the recentring) and §4 (the
outer accounting); band §3 (rings, basis, the normalized Jacobian, the branch
substitutions) and §4 (the stage synchronisation convention). No line of charged
*code* was consulted; no charged *numerical output file* was read into the engine.

No ledger, `jc2-lean`, `ideation-*`, or in-progress lane report was read or edited.
All writes are under `box/g9966indep-20260903/` plus this report.

Work is exact over `Q`. Localization uses Rabinowitsch rows in Singular only, after
`Q*` pivoting; `rho` and `c` are declared forbidden as pivots.

## 2. What the design fixes, and where it is ambiguous

**Fixed and unambiguous.** The chart (2.1) and its block degrees; the leading forms
`in h3=P`, `in h2=P^3`, `in F=P^9`, `in G=P^6` with `P=y^3(y-x)^8`; the Theorem-1.2
order bounds at `D1` and `D2`; the recentring `t=e^9, w=1+e^12+Pi e^13`; the two
minor substitutions; the normalized Jacobian expression; the stage synchronisation.

**Ambiguous, and how I resolved each.**

1. *The `h2` `D2` face `(pi^3-1)^8`.* The design **asserts** it (§2.1) without a
   derivation. I re-derived it from the multiplicity table alone: `h2` has
   multiplicity 24 at `D2` and 8 at `D1`, so its 24 `D2` roots must split into
   exactly three clusters of eight; the weight-96 face is therefore a degree-24
   polynomial in `pi` with three distinct roots each of multiplicity 8, i.e.
   `(pi^3-a)^8`. The residual scale `a` is *not* determined by the tower — it is
   fixed to `a=1` by the recentring (2.3), which sends `pi -> 1+Pi e`. I record
   `a=1` as a **normalization convention**, not a theorem. My engine's weight-96
   face came out as `q=24:1, 21:-8, 18:28, 15:-56, ...`, i.e. `(pi^3-1)^8`.
2. *Which 106 slots are the "surviving low-`q` outputs".* The band report names the
   count but not the set. I derived it: `K_C3` has `(w-1)`-degree `<= 10` and
   `K_C2 K3` has `<= 21`, so `K2c_{r,q}` with `q >= 22` is reachable **only**
   through `K3^3` and is not independently controllable. Hence the free low-`q`
   symbols are `{r>=1, q<=21, r+q<=33, 3r+4q>=97}` — which my enumerator counts as
   exactly **106**. This is a derivation, not a fit.
3. *`h2` `D1` pivot columns.* The 7 rows (weights 97, 98) touch both low-`q`
   symbols and the `h3`-determined slots `(3,22)`, `(2,23)`. The design says the
   pivots use `C2,C3` columns. Pivot order is a convention; I ran the whole
   campaign twice (inert-first, and the charged engine's stated plain lexicographic
   name order) with **identical** dimensions and residues (§8.5).
4. *Pole exponent <-> local power.* Not stated as a formula. Derived:
   `t^18 F(t^-1,sigma_2) = t^-81 KF`, so exponent `-81+n` is `[t^n]KF`; the charged
   prefix is `n=1,2,3` (`-80,-79,-78`) and stage `k` is `n=4+k`. For `delta=5/2`,
   `s^9 F(s^-2,sigma_52) = s^-189 KF`, prefix `n=2,4,6` (`-187,-185,-183`), stage
   `k` is `n=8+k`. This reproduces the charged `(-77,-50)`, `(-181,-118)` and the
   stage-8 `-173/-110` at "local power 16" without being told.
5. *`b0=0` and `Hc_11_0=0` for `delta=5/2`.* These come from the Xu `T3` ODE at
   level `n=1`, i.e. from the **`OPEN[EFFECTIVE-T2-T3-BRIDGE]`** that this lane does
   not implement. I imposed `Hc_11_0=0` as a **declared imported convention** and
   then measured its cost: §8.6 shows every `delta=5/2` dimension is exactly `+1`
   without it (`6703,1064,1017,975,941,914,895,881,870`) and the stage-8 residue is
   still exactly `64`. So the single imported input is dimension-only and does not
   participate in either death.
6. *Effective `T2,T3` rows, the `R=pi^25(pi+3)^14(pi-2)` leader, the `18+9 / 9+9+9`
   packet data.* Not implemented — they are the charged `OPEN` bridge and emit zero
   linear rows on the chart (outer-bridge §3). Their absence only **weakens** the
   necessary subsystem, so it cannot rescue a unit ideal.

## 3. The engine

`box/g9966indep-20260903/`: `ring.py` (exact sparse `Q`-polynomial arithmetic and
one-variable series over it), `indep_engine.py` (chart, towers, rows, eliminator),
`run_bands.py` (stage driver), `chart_combinatorics.py`, `controls.py`.

**Ambient.** `S(D,r0)` homogenized as `K_Q = t^D Q(t^-1,w/t) = sum Qc_{r,q} t^r (w-1)^q`,
`r>=0`, `q<r0`, `r+q<=D`. Block sizes computed, not copied:
`H 66, C2 187, C3 308, A2 1650, A3 2739, B1 561, B2 1650`, total **7161**; outer
ambient **6600**.

**Towers.** `K3 = w^3(w-1)^8 + sum Hc_{r,q} t^r (w-1)^q`;
`K2 = [K3^3]_{q>=22} + sum_{q<=21} K2c_{a,q}(w-1)^q` under the `D2` rule
(zero below weight 96, the eight `(-1)^k C(8,k)` constants at weight 96, free
symbols above). A structural check that the design does not state and that my
engine verifies: **`K3^3` has no component of weight `< 96`** — the `h3` `D2` rows
already imply the `h2` `D2` support conditions on the `h3`-determined part.

**Order rows.** `h3`: weight `>= 3(11-1/3)=32`; 66 slots, 45 rows (43 strict, plus
the two equality sites `(4,5),(8,2)`), **21 free** — matching §3.1's (3.1).
`h2`: 561 slots, `384+8=392` `D2` rows, 169 strict, **106** low-`q` free;
`D1` threshold `9(33-1/9)=296`, giving exactly **7** rows on unknowns, at
`e`-powers `291:1, 292:1, 293:1, 294:2, 295:2`, rank **7**.
Outer `D2` thresholds `189/285/93/189` delete **5598** of 6600, leaving **1002**.
Outer `D1` thresholds `583/879/287/583`; rows indexed by `(block, W, j)` with
`e`-exponent `E=3W+j`; **225** raw rows in 8 offsets `64,52,40,29,20,11,6,3` with
exact ranks `41,38,33,25,19,11,6,3`, total **176**, leaving **826**. Every one of
these numbers is produced by my enumerator from the thresholds alone.

**Chart series.** `KF = K2^3 + t(K_A2 K2 + K_A3)`, `KG = K2^2 + t(K_B1 K2 + K_B2)`.
After the `D2` preblock, `A2`,`B2` survive only for `r>=21` and `A3` only for
`r>=53` (my engine derives these, matching outer-bridge §2), so **through
`t`-power 21 the exact identities are `KF = K2^3` and `KG = K2^2 + t K_B1 K2`**.
All bands run here live at `t`-power `<= 8`, so truncating at `t^9` is exact, not
an approximation. This is why my engine runs in 33 s where the charged one needed
~2 h: the charged engine carries all 7161 coordinates symbolically.

**Jacobian.** `KJ = 99 KF (KG)_w - t (KF)_t (KG)_w - 66 (KF)_w KG + (KF)_w t (KG)_t`,
with `J(F,G) = x^163 KJ(1/x, y/x)`; I re-derived the `x^163` and the four
coefficients from `F = x^99 KF(1/x,y/x)` rather than copying them. Hence
`[x^i y^j]J = [t^{163-i-j} w^j] KJ`, so "Jacobian degree `163-n`" is `t`-power `n`
and the `k` index is the `w`-power. Internal assertion, checked every run:
`deg_w KJ_n <= 163-n` (i.e. `i>=0`).

For speed I also proved and used a factored form valid below the `A2/A3/B2` onset,
with `A=K2`, `B=K_B1`:

```text
KJ = t A^3 (99 A B_w - 96 B A_w) + 3 t^2 A^3 (A_w B_t - A_t B_w).
```

`factored_jacobian_check.py` verifies it against the unfactored four-term formula
term by term at truncation 5 (**holds**). It makes the mechanism legible: the
Jacobian bands at `t`-power `n` are linear in `B_{n-1}` alone.

**Minor incidence.** `delta=2`: `w = u t^2 + zeta t^3`, leader target
`[t^9]K3 = zeta^2(zeta+3 rho)`. `delta=5/2`: `t=s^2`, `w = u s^4 + v s^6 + pi s^7`,
target `[s^21]K3 = pi(pi^2-c)`. Substitution is done by expanding
`(w-1)^q = (X-1)^q` with `X` of positive local order, so only `O(M/ord X)` binomial
terms survive — exact and cheap.

**Eliminator.** `Q*` pivots only: a variable is eliminated iff it occurs in exactly
one monomial, that monomial is the pure linear one, and its coefficient is a nonzero
rational. `rho`/`c` are in the forbidden set. Anything else is emitted as a residue.

## 4. Independent confirmation of the pre-band state

| quantity | charged | mine |
|---|---:|---:|
| chart coordinates | 7161 | **7161** |
| outer ambient / `D2` deleted / remaining | 6600 / 5598 / 1002 | **6600 / 5598 / 1002** |
| outer `D1` raw / rank | 225 / 176 | **225 / 176** |
| `h3` slots / free | 66 / 21 | **66 / 21** |
| `K2c` slots / `D2` rows / strict / low-`q` | 561 / 392 / 169 / 106 | **561 / 392 / 169 / 106** |
| `h2` `D1` rows / rank | 7 / 7 | **7 / 7** |
| `delta=2` `h3`-leader pivots; free coords | 18; `c_{7,4},c_{10,1},c_{11,0}` | **18; same three** |
| `delta=5/2` `h3`-leader pivots; free coord | 20; `c_{11,0}` | **20; same** |
| inner dimension, centres included | 104 / 102 | **104 / 102** |
| pre-outer joint | 6704 / 6702 | **6704 / 6702** |

The four shared identities the design prints as (3.4) came out of my leader solve
unprompted: `c_{2,9}=3u`, `c_{3,8}=-3v`, `c_{7,4}=c-3u^2 v`, `c_{10,1}=-cv`
(and in the `delta=2` branch `c_{2,9}=3u`, `c_{3,8}=3rho`).

The design's generic-face spot check also reproduces from my normalization:
`generic_face_probe.py` gives `[x^145 y^17]J = 1764 * A3_{98,0}` and
`[x^146 y^16]J = 0`.

## 5. Why my engine has no separate 15-pivot prefix stage

The charged 15-pivot endpoint (`6704 -> 6689`, `6702 -> 6687`) pivots the outer
coordinates `A3_{98,0} ... A3_{89,9}`, `A2_{65,0}`, `B2_{65,0} ... B2_{63,0}`.
In the homogenized basis these all have `r <= 7`, and my `D2` computation shows
every `A2`,`A3`,`B2` slot with `r <= 7` is deleted (e.g. `A2` needs
`3r+4q>=189` with `q<=32`, forcing `r>=21`). So all fifteen prefix pivots are
identically zero after the `D2` preblock, exactly as the band report states
("makes all 16 prior labels and all newly requested labels zero"). My stage 0
imposes `D2` and therefore subsumes the prefix; the subtraction `6689 - 5624 =
1065` is the same arithmetic, taken in one step (`6704 - 5598 - 41 = 1065`).

## 6. Runs

`run_bands.py <branch> <nstages>`, foreground, `timeout 3000`, `taskset -c 0,1,2,3`.

### `delta=2` (`run_delta2.json`)

| stage | outer raw/rank | pole labels | `J` labels | joint `Q*` new/cum | residue | dimension |
|---:|---:|---:|---:|---:|---|---:|
| 0 | 64/41 | 4 | 1 | 0/0 | 0 | **1065** |
| 1 | 52/38 | 4 | 135 | 9/9 | 0 | **1018** |
| 2 | 40/33 | 6 | 127 | 9/18 | 0 | **976** |
| 3 | 29/25 | 6 | 127 | 9/27 | 0 | **942** |
| 4 | 20/19 | 6 | 126 | 8/35 | **118 constants; unit** | **DEAD** |

Formal pre-residue generator count at stage 4: **915** (the charged report's "that
number is only the formal generator count"). Total wall time 14.9 s.

### `delta=5/2` (`run_delta52.json`)

| stage | outer raw/rank | pole labels | `J` labels | joint `Q*` new/cum | residue | dimension |
|---:|---:|---:|---:|---:|---|---:|
| 0 | 64/41 | 4 | 1 | 0/0 | 0 | **1063** |
| 1 | 52/38 | 4 | 135 | 9/9 | 0 | **1016** |
| 2 | 40/33 | 4 | 127 | 9/18 | 0 | **974** |
| 3 | 29/25 | 4 | 127 | 9/27 | 0 | **940** |
| 4 | 20/19 | 4 | 126 | 8/35 | 0 | **913** |
| 5 | 11/11 | 4 | 133 | 8/43 | 0 | **894** |
| 6 | 6/6 | 6 | 132 | 8/51 | 0 | **880** |
| 7 | 3/3 | 6 | 132 | 8/59 | 0 | **869** |
| 8 | 0/0 | 6 | 131 | 7/66 | `G_local16_pi^0 = 64` | **DEAD** |

`869 = 6702 - (5598 + 176 + 59)` and the stage-8 formal count `862 = 102 + 826 - 66`,
both as published. Total wall time 33.3 s; `/usr/bin/time -v` on a clean re-run gives
31.05 s elapsed, exit 0, peak RSS **25,668 KiB** (the charged stage-8 run needed
1,757.86 s and 279,160 KiB).

## 7. The two deaths, independently certified

**`delta=2`, stage 4.** 118 residues, every one a nonzero integer constant. The
first, in my own labelling, is

```text
J_d159_k35 = 6264,        1 = (1/6264) * J_d159_k35   in Q.
```

Same label, same constant, same count as the charged `stage4_J_d159_k35 = 6264` and
its 118 constants. Singular replay of `<6264, Zrho*rho-1>` over `Q`:
`dim = -1`, standard basis `1`; controls `<rho, Zrho*rho-1>` empty (`-1`),
`<rho-1, Zrho*rho-1>` a point (`0`), raw `<6264>` the unit ideal (`-1`).

**`delta=5/2`, stage 8.** One residue,

```text
G_local16_pi^0 = 64,      1 = (1/64) * G_local16_pi^0   in Q.
```

Same constant and same row identity as the charged `stage8_G_local16_coord0 = 64`
(`G`, local power 16, branch-coordinate power 0). Singular replay of
`<64, Zc*c-1>`: `dim = -1`, basis `1`, same three controls. My control encoding is
Singular's raw `dim` (`-1,0,-1`); the charged report's `0,1,0` encodes the same
three facts (empty localization, nonempty point, raw unit ideal).

Beyond the constants, the stage-8 elimination matches row for row:

| row | pivot | coefficient (mine) | coefficient (charged) |
|---|---|---:|---:|
| `J_d155_k35` | `B1c_7_19` | 675 | 675 |
| `J_d155_k36` | `B1c_7_20` | 576 | 576 |
| `J_d155_k37` | `B1c_7_21` | 477 | 477 |
| `J_d155_k38` | `B1c_7_22` | 378 | 378 |
| `J_d155_k39` | `B1c_7_23` | 279 | 279 |
| `J_d155_k40` | `B1c_7_24` | 180 | 180 |
| `J_d155_k41` | `B1c_7_25` | 81 | 81 |

**Mechanism (new, and not in the charged reports).** The factored `KJ` gives, once
`B_0 = ... = B_{n-2} = 0`,

```text
[t^n] KJ = A_0^3 [ 99 A_0 B_{n-1,w} - (99-3n) B_{n-1} A_{0,w} ],
A_0 = w^9 (w-1)^24,
```

a linear system on the nine-or-fewer coordinates `B1c_{n-1,q}` whose lowest `w`-power
is exactly **35** — which is why `J`-band coordinates `k<35` are vacuous and the
charged prefix rows `k=17..26` and stage-0 row `k=27` reduce to `0=0`. Its rank is
full except where the outer `D1` offset-0 rows (weight 93, 8 rows on 8 columns,
invertible) have already zeroed a column: they hit `B1c_{3,21}` and `B1c_{7,18}`,
which is precisely why the joint sequence reads `9,9,9,8,8,8,8,7` rather than
`9,9,9,9,8,8,8,8`. The branch asymmetry has an equally concrete source
(`pole_row_triviality.py`): the `F` pole rows are identically zero throughout, and
the `G` pole rows are nonzero at `delta=2` local powers `5,6,7,8` (every stage from
1) but at `delta=5/2` only at *even* local powers `10,12,14,16` (every second
stage, because `t=s^2`). `delta=2` therefore collides with the `J` band four stages
earlier. That is the whole of the four-stage gap between the two deaths.

## 8. Controls (all in my engine)

**8.1 Zero-point / end-to-end (`C2`).** Set every free chart coordinate to zero, so
`F=P^9`, `G=P^6` and `J(F,G) == 0` identically. My **unfactored** four-term `KJ`
is identically zero on every `(t,w)` slot, and `KF`'s top form is exactly
`w^27 (w-1)^72 = P^9`. `PASS`.

**8.2 Tame automorphism (`C1`).** Requested: degrees `>= 6`, two-point. I must
report a premise problem: by the classical Jung-van der Kulk structure theorem, for
a plane polynomial automorphism with `max(deg) > 1` the leading forms `in F` and
`in G` are powers of a **common** linear form, so the pair
has **one** point at infinity; a genuine two-point configuration of degrees `>= 6`
with `J=1` would be a Keller pair that is not an automorphism, i.e. the object whose
non-existence is under test. So `NOT-APPLICABLE[TWO-POINT, deg>=6]`, and the
charged design's own two-point control is at degrees `(1,1)` for the same reason.
I therefore built the strongest available substitute — a **tame automorphism of
degrees 6 and 36** whose single point at infinity lies inside my chart:

```text
F = x + y^6,     G = y + (x + y^6)^6,     J(F,G) = 1  (verified directly),
in F = y^6,      in G = y^36,             point at infinity  w = y/x = 0.
```

Running it through my generic normalized Jacobian for degrees `(n,m)=(6,36)`, the
entire band family collapses: `KJ` has exactly one nonzero slot,
`[t^{n+m-2} w^0] = [t^40 w^0] = 1`, and **every** other `(t,w)` slot vanishes. Since
the rows my engine imposes on `(99,66)` are precisely such slots, the machinery does
not falsely kill this automorphism. `SURVIVES[ALL JACOBIAN BANDS I CAN RUN]`.
`NOT-APPLICABLE[s=3 tower, outer D1/D2, minor split; degrees (6,36) have no such
configuration]`.

**8.3 Discriminating power (`C1b`).** Perturbing one homogeneity weight
(`n -> n-1`) in the Jacobian makes the same automorphism control **fail**
(8 violated slots). The control is not vacuous.

**8.4 Relaxation controls (`C3`,`C4`) — what actually kills `delta=2`.**
Re-running `delta=2` with the Jacobian band dropped: **survives** stage 4 at
dimension 945, no residue. Re-running with the pole rows dropped: **survives** at
915, no residue. Neither family alone is inconsistent; the death is exactly their
interaction. This rules out the failure mode "the setup is inconsistent, so
everything dies".

**8.5 Pivot-order convention (`C5`).** Re-ran both branches under plain
lexicographic symbol-name order (the charged engine's stated order) instead of my
inert-first preference: identical dimension paths and identical residues
`6264` and `64`.

**8.6 Cost of the one imported convention (`C6`).** Dropping `Hc_11_0=0` raises every
`delta=5/2` dimension by exactly 1 (`6703,1064,1017,975,941,914,895,881,870`) and
leaves the stage-8 residue at exactly `64`. The imported Xu-ODE input is
dimension-only.

**8.7 Moh p.208 `(64,48) -> (16,12)` — `GAP`, disclosed.** I extracted printed
pp. 207–209 from the frozen PDF. The prose reads ("... the total number of
coefficients is further reduced to 17", the `(16,12)` row of the reduced table, and
the `alpha_i` list), but every display equation defining `h`, `A`, `B` and the
`alpha_i` is absent from the text layer. The charged reports give the *counts*
(17 coefficients plus `kappa`, 77 rows) but never print the ansatz. Reconstructing
it would be fabrication, so I did not run this calibration. `GAP[P208-ANSATZ]`;
`OPEN[PRINTED-C5-EMENDATION]` is untouched by this lane.

## 9. Reproduction

```bash
awk -F= '/^charged_input_[0-9]+_sha256=/{split($1,a,"_");h[a[3]]=$2}
         /^charged_input_[0-9]+_basename=/{split($1,a,"_");b[a[3]]=$2}
         END{for(i=1;i<=12;i++)printf "%s  %s/%s\n",h[i],D,b[i]}' \
    D=/tmp/jc2-lane.Cexilr/inputs \
    xmodel/g9966-independent-engine-opus5-20260903.run.v2 | sha256sum -c

python3 box/g9966indep-20260903/chart_combinatorics.py
timeout 3000 taskset -c 0,1,2,3 python3 box/g9966indep-20260903/run_bands.py delta2  4
timeout 3000 taskset -c 0,1,2,3 python3 box/g9966indep-20260903/run_bands.py delta52 8
timeout 3000 taskset -c 0,1,2,3 python3 box/g9966indep-20260903/controls.py
Singular -q box/g9966indep-20260903/singular/delta2_stage4.sing
Singular -q box/g9966indep-20260903/singular/delta52_stage8.sing
```

Artifact digests: `box/g9966indep-20260903/artifacts.sha256`. Wall times: combinatorics
0.1 s; `delta=2` 14.9 s; `delta=5/2` 33.3 s; controls 3 s; Singular < 1 s each — all
inside `timeout 3000`, foreground, four cores.

## 10. FALLACY-v2 audit

* **Flag/place/series.** The major flag, the two principal-minor places, and the
  cover series remain distinct typed objects here; the agreement of coefficient
  arrays between my engine and the charged one is an agreement of *arrays*, not an
  identification of flags. The `D2` support deletion (strict-below) is kept
  distinct from the at-level `D1` parting throughout §3.
* **Floor/attainment.** Theorem 1.2 gives `>=` bounds; my rows impose exactly the
  strict-below vanishings and, where the design supplies a face, the face. No
  equality is claimed anywhere. The `(pi^3-1)^8` face is flagged in §2 as a
  multiplicity consequence plus a scale normalization, not a theorem.
* **Carrier/attainment.** Nothing here is `REPRESENTATIVE` or `FULL_ACTUAL_EXIT`.
  No point survived either branch, so no candidate `(F,G)` exists to recompose and
  no direct `F_x G_y - F_y G_x == 1` check is possible or claimed.
* **`sat()` wrapping.** Both Singular calls declare their ring
  (`0,(rho,Zrho),dp` / `0,(c,Zc),dp`), assert the Rabinowitsch generator, and run a
  positive control (`<rho-1,Zrho*rho-1>` is a point) and two negative controls.
* **Raw remainder degree.** Residues are normal forms in the declared `Q*` quotient;
  each was classified as a *constant* before any nonlinear question arose, and the
  vanished-leader branch is empty because all 66 (resp. 35) cumulative pivot
  coefficients are nonzero rationals not involving `rho` or `c`.
* **Variable/ring map.** §3 declares the homogenization map, the generator order,
  the coefficient field, and the `K2c` change of variables, with the image checks
  (`deg_w KJ_n <= 163-n`, `K3^3` has no sub-96 weight, `in KF = P^9`). Name
  agreement with the charged engine is *not* used as evidence anywhere; the
  agreements reported are of computed values.
* **Prime label/derivative.** No primes are used as differentiation marks in this
  report; `_w`, `_t` denote declared partial derivatives.
* **Target/arrival index.** Stage indices, `t`-powers, Jacobian total degrees, and
  pole exponents are kept as four separate indices with the conversions written out
  in §2.4 and §3.

No exit claim is made, so no `charge_basis=` line is emitted.

## 11. Verdict

```text
CONFIRMED-INDEPENDENTLY[(99,66) JOINT-CHART BAND ENGINE]
  delta=2   stage-4 death, constant-unit residue 6264   : reproduced, row-level
  delta=5/2 stage-8 death, constant-unit residue 64     : reproduced, row-level
  all published dimensions, outer ranks, joint Q* ranks,
  stage-8 pivot variables and coefficients             : reproduced exactly
DISAGREEMENT: none, at any stage or row.
GAP[MOH p.208 (16,12) CALIBRATION]  (chart absent from the frozen PDF text layer)
NOT-APPLICABLE[TWO-POINT AUTOMORPHISM deg>=6]  (no such automorphism exists; a
  degrees-(6,36) tame automorphism was built instead and survives every band)
```

Two independent implementations, written from different starting points (the
charged engine from the lifts; mine from the design prose alone), agreeing on both
constant-unit certificates and on every intermediate rank, remove implementation
fidelity as a live doubt about the two deaths. The conditional skeleton verdict
`NO-KELLER-PAIR-WITH-THE-(99,66)-SKELETON` continues to depend on the necessity of
the declared joint chart and on `{2, 5/2}` being an exhaustive branch split —
neither of which this lane tested, and neither of which independent
re-implementation can establish.
<!-- BODY-END -->
