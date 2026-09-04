# k4 ray pinned chart lane

Verdict: PARTIAL. The pinned residual chart closes the K=7 wall row exactly over
Q, but it does not close K=8 or K=9 within this lane. Therefore the
UNSPLIT-CONFIGURATION LEMMA is not proved at K=7,8,9, case (A) of (99,66) is
not dead by this computation, D=108 is not closed at skeleton level by this
lane, and there is no notify-worthy complete skeleton promotion.

## 0. Frozen input manifest

The frozen inputs were verified mechanically from
`xmodel/k4ray-pinned-chart-gpt55-20260903.run.v2`. I generated the
`sha256sum -c` manifest from the receipt's `charged_input_<i>_sha256=` and
`charged_input_<i>_basename=` lines with `awk`; no digest was retyped.

All 12 inputs checked OK:

```text
k4ray-degree-tower-opus5-20260903.md        OK
k4ray-highK-opus5-20260903.md               OK
k4ray-unsplit-lemma-opus5-20260903.md       OK
sys-guided-gb-gpt55-20260903.md             OK
guided_gb.py                                OK
staged_band_emitter.py                      OK
moh_skeleton_full.py                        OK
FALLACY-v2.md                               OK
hint_control.py                             OK
gen_certif.py                               OK
gen_lemmas.py                               OK
gen_hk.py                                   OK
```

No ledger files, `jc2-lean`, or `ideation-*` files were edited.

## 1. Chart actually built

Driver: `box/k4raypinned-20260903/pinned_chart.py`.

The driver imports `box.lib.guided_gb` and uses `SingularSystem`,
`RunConfig`, `PromotionPolicy.exact_q`, `HilbertHint`, and `guided_groebner`.
The `guided_gb` wrapper runs Singular through `stdbuf -oL -eL`; the row-count
prelude runner also uses `stdbuf`.

The chart uses the charged normalization

```text
H = y^(K-1)(y-x)
h = H + lower terms, monic in y
B = 2 beta
f = h^2 + B
Al = quo_y(B^2,h) = 4 alpha
Rh = B^2 - Al*h = 4 rho
g = h^3 + (3/2) B h + (3/8) Al
J = (3/8) J(B,Al) - (3/4) J(h,Rh)       (ID6)
```

For the residual bottom band the LEVEL-4 pin is imposed as

```text
beta_b = mu*y^(K-3)*(y-x),     b = K-2
Btop  = 2*mu*y^(K-3)*(y-x)
```

The lower `B_i_j` variables are coefficients of `B=2 beta`, not of beta
itself. This is only a scale convention; the named scalar `mu` is the beta top
coefficient.

The light decision ideal is

```text
I_light =
  < all non-x^4 coefficients of J,
    coeffs of Rh - (4/3)*mu^3*y^(K-7)*(y-x) in degrees >= K-6,
    CSTP - 1,
    mu*mu_inv - 1 >
```

where the rho rows combine the degree consequence `deg Rh <= K-6` with the
LEVEL-4 top formula

```text
rho_(K-6) = beta_b^3 / (3 H^2).
```

This is a weaker ideal than the full theorem-cut ideal because it omits the
additional rows from `deg(64*(g^2-f^3) - lambda*f) <= K+6`. Thus a unit ideal
for `I_light` is a valid kill for the full theorem-valid chart: any larger
ideal containing a unit ideal is also the unit ideal.

The full theorem-cut variant additionally introduces `lambda` and adds all
coefficients of

```text
E64lam = 8*B^3 - 48*Rh*h^2 - 72*B*Rh + 9*Al^2 - lambda*f
```

whose `x,y` degree is strictly larger than `K+6`. Coefficients are extracted
with `coef(...,x*y)` and tested by `deg` on the displayed `x,y` monomial. This
avoids the old `jet()` pitfall where parameter variables are counted in the
degree.

Ring map:

```text
RR = Q,(x,y,parameters),dp
SS = Q,(parameters),wp(weights)
ROWS = imap(RR,I0)
CSTP = imap(RR,CST)
```

The charts are dehomogenized and localized by `CSTP-1` and `mu*mu_inv-1`.
Accordingly, no homogeneous properness promotion is used for the main rows.
Exact Q is the only characteristic-zero promotion path. Modular runs below are
typed F_p-only diagnostics.

## 2. Parameter counts

The old wall rows had parameter counts 48, 63, 80 in the charged high-K chart.
The LEVEL-4 pin removes the whole top beta band and replaces it by the one
scalar `mu`.

```text
K  b=K-2  beta_b                         h vars  lower beta vars  geom params  light GB vars
7  5      mu*y^4*(y-x)                   27      15               43           44
8  6      mu*y^5*(y-x)                   35      21               57           58
9  7      mu*y^6*(y-x)                   44      28               73           74
```

`light GB vars` includes `mu_inv`. The full theorem-cut variant adds one more
variable, `lambda`, so its GB variable counts are 45, 59, 75.

The row formation counts were:

```text
tag                  K  variant       rows  J rows  rho rows  theorem rows  formation
MAIN_K7_PIN_LIGHT2   7  light         149   108     46        disabled      0.055s
MAIN_K8_PIN_LIGHT2   8  light         209   153     62        disabled      0.281s
MAIN_K9_PIN_LIGHT2   9  light         279   206     80        disabled      2.095s
FORM_K7_PIN          7  full form     307   108     46        165           1.187s
FORM_K8_PIN          8  full form     447   153     62        246           24.788s
FORM_K9_PIN          9  full form     n/a   206     80        n/a           420.213s timeout
```

For K=9 full formation, Singular printed `PRE__DEG_ELAM 34 SIZE_ELAM 2381711`
before timing out during theorem-row coefficient/simplification work; no final
`PRE__NROWS` marker was reached.

## 3. Main row verdicts

Exact-Q runs:

```text
row                                    chart/run tag          verdict              time
K=7, (21,14;15;6;4), b=5 pinned        MAIN_K7_PIN_LIGHT2     UNIT_IDEAL_CHAR0     8.23s
K=8, D=108 no-split, b=6 pinned        MAIN_K8_PIN_LIGHT2     INCONCLUSIVE_TIMEOUT 1800.42s
K=9, (99,66) case A, b=7 pinned        MAIN_K9_PIN_LIGHT2     INCONCLUSIVE_TIMEOUT 1801.07s
```

K=7 details:

```text
generators: 149 ROWS + CSTP-1 + mu*mu_inv-1
accepted_run_count: 1
basis_size: 1
unit: true
promotion_note: exact Q standard basis reduced 1 to 0
script sha256: 6a4c02bcecea3b161dc50e47413a2d30ea6e185499bd3662069f8c56fd575a44
stdout sha256: 9d5c1c14bbebdcc1bf167392c9806b67afd3227317b1d01ad393c9646a0c1e5c
```

K=8 details:

```text
generators: 209 ROWS + CSTP-1 + mu*mu_inv-1
accepted_run_count: 0
timed_out: true
unit: false
dimension marker: not reached
promotion_note: no accepted result before timeout
script sha256: 3914d92eaa239bbe09fa1560fb40036ca2ee9c1d071115943b25647bdb3e7f66
stdout sha256: 7cc4671d7140c35ae17f2096e8324ae9f50f386d29cfddf7c3d16e028f400db4
```

K=9 details:

```text
generators: 279 ROWS + CSTP-1 + mu*mu_inv-1
accepted_run_count: 0
timed_out: true
unit: false
dimension marker: not reached
promotion_note: no accepted result before timeout
script sha256: 1d61e96cbd71322b59922ab62cf580d3d809b3e1c8bafd387a4d4f7254df0288
stdout sha256: 7f5ad053dc4f4dcfce32859fbc418d1f922d2fcb3fa2ac21338b67c767c3cabd
```

The K=8 full theorem-cut exact-Q variant also did not decide:

```text
tag: MAIN_K8_PIN_FULL
generators: 447 ROWS + CSTP-1 + mu*mu_inv-1
formed rows: 153 J + 62 rho + 246 theorem cutoff
run result: SIGKILL / returncode -9 during std after 138.17s
accepted_run_count: 0
unit/dimension markers: not reached
typed status here: execution-killed, no mathematical verdict
```

No POSDIM verdict occurred. Therefore no surviving point was extracted and no
`J=f_x g_y - f_y g_x` witness test was applicable.

## 4. Modular diagnostics

The modular runs are F_p-only. They are not promoted to characteristic zero and
they do not supply a row verdict.

```text
tag                 K  primes         status
MOD_K8_PIN_LIGHT2   8  32003,32009    both fibres killed with returncode -9 after 482.61s
MOD_K9_PIN_LIGHT2   9  32003          killed with returncode -9 during prelude after rho markers
```

The K=8 modular fibres reached `GG__STD_BEGIN` but no unit, dimension, vdim, or
basis-size markers. The K=9 modular fibre printed
`PRE__SIZE_AL`, `PRE__PIN_BTOP_DEG`, `PRE__RHO_RDEG`,
`PRE__RHOLEVEL4_ROWS`, then was killed before the Jacobian markers. The
`guided_gb` CRT field is consequently empty; there were no scalar invariants to
reconstruct.

These are execution failures, not evidence for or against the existence of a
point over Q.

## 5. Controls

All current control summaries are under `box/k4raypinned-20260903/runs/`.

```text
control              purpose                                  verdict          time
CTRL_PIN_K4_B3       pinned K=4 kill, exact Q                  UNIT_IDEAL       0.034s
CTRL_PIN_K5_B4       pinned K=5 kill, exact Q                  UNIT_IDEAL       0.116s
CTRL_TAME_K1         tame two-point survivor must survive      DIM0_CHAR0       0.008s
CTRL_HINT_K4_B3      guided_gb Hilbert perturbation control    DIM0_CHAR0       1.015s
```

K=4 control:

```text
K=4, b=3, beta_b=mu*y^2*(y-x)
61 rows = 31 J rows + 16 rho rows + 24 theorem rows
generators include CSTP-1 and mu*mu_inv-1
exact Q unit ideal, basis_size=1
```

K=5 control:

```text
K=5, b=4, beta_b=mu*y^3*(y-x)
137 rows = 56 J rows + 25 rho rows + 69 theorem rows
generators include CSTP-1 and mu*mu_inv-1
exact Q unit ideal, basis_size=1
```

Tame survivor control:

```text
h = y-x
beta = mu*x
f = (y-x)^2 + 2*mu*x
g = (y-x)^3 + 3*mu*x*(y-x)
J = 6*mu^2*x
```

With target `x`, `CSTP-1`, and `mu*mu_inv-1`, the ideal is dimension zero with
`vdim=2`, not unit. This is the expected survivor behavior.

Hilbert perturbation control:

```text
source fixture: box/k16stdhilb-20260903/t5_p1009_b0_tail_guided.sing
field: F_1009, homogeneous positive-weight properness fixture
predicted length: 3640
main lead_vdim: 3640
main accepted: true
perturbed lead_vdim: 3640
perturbed accepted: false
```

The perturbed run computes the same lead length but is deliberately tested
against the perturbed predicted length, so `VDIM_MATCH_PREDICTED=0` and the
negative control fails as designed.

## 6. FALLACY-v2 guardrail check

Variable/ring map: declared above. Names are not used as proof; `ROWS` and
`CSTP` are explicit `imap` images from the construction ring to the parameter
ring, and every main prelude printed `TARGET_FOUND 1`, `CSTP_ZERO 0`,
`HOMOG_I 1`, and `HOMOG_CST 1`.

`sat()` wrapping: none. The localization is the explicit Rabinowitsch generator
`mu*mu_inv-1`; the target coefficient is dehomogenized by `CSTP-1`.

Properness scope: not used for the main rows. These ideals are inhomogeneous
localizations, so exact Q is required for a characteristic-zero row kill.
Modular diagnostics are typed F_p-only.

Carrier/attainment: the report claims only the pinned bottom residual band
`b=K-2`. It does not claim to close the entire `deg beta <= 2K-1` stratum.

Floor/attainment: the LEVEL-4 divisibility and rho-top formula are used as
necessary equations on this pinned chart. A timeout is not promoted to a kill.

No exit-price assertion is introduced in this report, so no `charge_basis=...`
line is emitted.

## 7. K=10 and K=11

Not pushed. The K=8 and K=9 pinned rows did not close, and the next parameter
counts are not cheap relative to the observed wall:

```text
K  b=K-2  h vars  lower beta vars  geom params  light GB vars
10 8      54      36               91           92
11 9      65      45               111          112
```

Given that K=8 at 58 GB variables timed out over Q and K=9 at 74 GB variables
timed out over Q, a K=10/K=11 push would not be a cheap continuation in this
lane.

## 8. Dependency chain status

The requested promotion chain would be:

```text
K=7 pinned row UNIT
K=8 pinned D=108 no-split row UNIT
K=9 pinned (99,66) case A row UNIT
  => UNSPLIT-CONFIGURATION LEMMA holds at K=7,8,9
  => case (A) of (99,66) DEAD
  => with banked (B),(C), (99,66) skeleton verdict COMPLETE modulo N1
  => D=108 no-split DEAD, hence D=108 CLOSED at skeleton level
  => delta_1'=0 row (21,14) DEAD
  => NOTIFY-WORTHY
```

This chain is not activated. Only the K=7 premise is discharged by this lane.
The K=8 and K=9 premises remain undecided:

```text
K=7: UNIT_IDEAL_CHAR0
K=8: INCONCLUSIVE_TIMEOUT / execution-killed variants, no Q certificate
K=9: INCONCLUSIVE_TIMEOUT / full theorem formation timeout, no Q certificate
```

Final lane verdict:

```text
K=7 pinned nonconstant arm: DEAD on this pinned residual chart.
K=8 D=108 no-split pinned row: OPEN/TIMEOUT.
K=9 (99,66) case (A) pinned row: OPEN/TIMEOUT.
UNSPLIT-CONFIGURATION LEMMA at K=7,8,9: NOT PROVED.
D=108 skeleton closure: NOT OBTAINED.
(99,66) skeleton complete modulo N1: NOT OBTAINED.
NOTIFY-WORTHY: false.
```

## 9. Run ledger and containment notes

The main chart commands were run from `/home/ubuntu/jc2`:

```text
python3 box/k4raypinned-20260903/pinned_chart.py count FORM_K7_PIN 7 --timeout 240
python3 box/k4raypinned-20260903/pinned_chart.py count FORM_K8_PIN 8 --timeout 300
python3 box/k4raypinned-20260903/pinned_chart.py count FORM_K9_PIN 9 --timeout 420
python3 box/k4raypinned-20260903/pinned_chart.py count LIGHT2_K8_PIN 8 --no-theorem --timeout 240
python3 box/k4raypinned-20260903/pinned_chart.py count LIGHT2_K9_PIN 9 --no-theorem --timeout 300
python3 box/k4raypinned-20260903/pinned_chart.py run MAIN_K7_PIN_LIGHT2 7 --no-theorem --timeout 300 --count-timeout 180 --cores 4
python3 box/k4raypinned-20260903/pinned_chart.py run MAIN_K8_PIN_LIGHT2 8 --no-theorem --timeout 1800 --count-timeout 240 --cores 4
python3 box/k4raypinned-20260903/pinned_chart.py run MAIN_K9_PIN_LIGHT2 9 --no-theorem --timeout 1800 --count-timeout 300 --cores 4
python3 box/k4raypinned-20260903/pinned_chart.py run MAIN_K8_PIN_FULL 8 --timeout 1800 --count-timeout 300 --cores 4
python3 box/k4raypinned-20260903/pinned_chart.py run MOD_K8_PIN_LIGHT2 8 --no-theorem --chars 32003,32009 --timeout 900 --count-timeout 240 --cores 4
python3 box/k4raypinned-20260903/pinned_chart.py run MOD_K9_PIN_LIGHT2 9 --no-theorem --chars 32003 --timeout 600 --count-timeout 300 --cores 4
python3 box/k4raypinned-20260903/pinned_chart.py controls --timeout 600 --cores 4
python3 box/k4raypinned-20260903/pinned_chart.py summarize
```

Every main exact-Q `run` command goes through `guided_groebner` with
`PromotionPolicy.exact_q`. The accepted K=7 conclusion is therefore not a
modular lift, not a properness lift, and not a saturation inference. It is the
literal Singular certificate that `reduce(1,G)==0` after the controlled
standard-basis computation.

The containment point used for K=7 is:

```text
I_light = < J rows, LEVEL-4 rho rows, CSTP-1, mu*mu_inv-1 >
I_full  = I_light + < theorem cutoff rows >
1 in I_light  =>  1 in I_full
```

So the K=7 light unit is stronger than needed for the full theorem-valid pinned
chart. The converse is not used: K=8/K=9 light timeouts do not say the full
ideals are nonunit, and K=8 full SIGKILL does not say either unit or nonunit.

The exact-Q failure classes are separated:

```text
INCONCLUSIVE_TIMEOUT: guided_gb wrapper timed out after std began and wrote timed_out=true.
EXECUTION_KILLED: process returncode -9; no unit/dimension marker; treated as no certificate.
FORMATION_TIMEOUT: prelude did not reach PRE__ROWS_FINAL; treated as no formed ideal.
```

Only `INCONCLUSIVE_TIMEOUT` appears in the main K=8/K=9 light exact runs. The
K=8 full theorem-cut exact run is `EXECUTION_KILLED`. The K=9 full theorem-cut
attempt is `FORMATION_TIMEOUT`.

## 10. Artifact paths

```text
box/k4raypinned-20260903/pinned_chart.py
box/k4raypinned-20260903/summary-all.json
box/k4raypinned-20260903/runs/MAIN_K7_PIN_LIGHT2/summary.json
box/k4raypinned-20260903/runs/MAIN_K8_PIN_LIGHT2/summary.json
box/k4raypinned-20260903/runs/MAIN_K9_PIN_LIGHT2/summary.json
box/k4raypinned-20260903/runs/MAIN_K8_PIN_FULL/summary.json
box/k4raypinned-20260903/runs/MOD_K8_PIN_LIGHT2/summary.json
box/k4raypinned-20260903/runs/MOD_K9_PIN_LIGHT2/summary.json
box/k4raypinned-20260903/runs/CTRL_PIN_K4_B3/summary.json
box/k4raypinned-20260903/runs/CTRL_PIN_K5_B4/summary.json
box/k4raypinned-20260903/runs/CTRL_TAME_K1/summary.json
box/k4raypinned-20260903/runs/CTRL_HINT_K4_B3/summary.json
```

The `runs/` directory also contains the generated `.sing`, `.out`, `.err`, and
`.guided.json` files for each guided run.

<!-- BODY-END -->
