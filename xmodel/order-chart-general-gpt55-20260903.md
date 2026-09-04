# General Two-Point Order Chart

Date: 2026-09-03

## Scope

Generalise the K=16 independent two-point order-chart generator to descended
data `(n',m',M2',V2',k)` with symbolic top-face partition strata.  Outputs are
under `box/orderchart-20260903/`; the driver is
`box/orderchart-20260903/order_chart.py`.

Verdict: **CONFIRMED inside the order-tower chart.**  The banked K16 charts are
reproduced, the requested validation rows are `[1]`, and the open row
`(25,15;21;2;k=2)` is `[1]` over `GF(32003)`, `GF(32009)`, `GF(32027)`, and
`Q` for all three strata `[3]`, `[2,1]`, `[1,1,1]`.  No preprocessing was
needed for the open row after the order chart reduction.

## Input Manifest

MEASURED.  I generated `box/orderchart-20260903/charged_input_manifest.sha256`
mechanically from `xmodel/order-chart-general-gpt55-20260903.run.v2` by pairing
the `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines and
prefixing `/tmp/jc2-lane.YtvJBb/inputs/`.  `sha256sum -c` returned `OK` for all
13 frozen inputs.

```text
7e7e763fab3771250a089e41292e40830a66f8fa87774a7126207d9ecbfc21af  box/orderchart-20260903/charged_input_manifest.sha256
811a763816879e1205d224d7624237428a750fe17126d3d0e6b97fedf915f51e  box/orderchart-20260903/order_chart.py
```

Singular version:

```text
Singular for x86_64-Linux version 4.3.2 (4330, 64 bit) Apr  1 2024 04:44:00
```

Durable lane writes are confined to this report and `box/orderchart-20260903/`
apart from temporary `/tmp` scratch summaries.  No ledger edits or `jc2-lean`
commands were used.  Singular jobs were launched as foreground
`timeout ... Singular ...` commands with this lane's Singular options capped to
one thread.

## Construction Notes

For a row put

```text
K=d2'=gcd(n',m'),  u'=K-V2',  e=n'/K,  q=m'/K,
R=n'-M2'-1,        Pi=e+q.
```

The closed-form Phi radii used by the generator are

```text
delta2'=-(k+1)/R,
delta1'=(k+1)(Pi*u' - R)/(R(Pi*V2' - 1)),
B=V2'*delta1' + u'*delta2'.
```

The Theorem-1.2 coefficient bound is common:

```text
lambda_P/e = lambda_Q/q = B,
alpha_i, beta_i in S_i where ord(S_i) >= i*B.
```

For a partition `lambda=(e1,...,el)` of `u'`, the normalized symbolic top face
is

```text
H_top = y^V2'*(y-x)^e1*prod_{i=2..l}(y-s_i*x)^e_i,
Omega = prod_i s_i(s_i-1) * prod_{i<j}(s_i-s_j).
```

The saturation factor is `c*Omega`; when there are no symbolic slopes,
`Omega=1`.

The approximate-root tower is the sparse K16-compatible prefix tower:

```text
H1 = L1,
H2 = L2*H1 + b1*y + b2,
Hr = Lr*H(r-1) + br       for r>=3,
h  = HK.
```

The factor order is `(y-x)` repeated `e1`, then `(y-s_i*x)` repeated `e_i`,
then `y` repeated `V2'`.  This reproduces the K16 tower
`z, B, A, h` exactly after renaming the `b_i`.  The lower monomial support of
the resulting `h` is checked against the corrected Lemma-2.1/D1 support; every
reported row has `lemma21_support_ok=True`.

The filtered basis is

```text
1, H_{K-1},...,H_1, x
```

with weights from the factor prefix order and `ord(x)=delta2'`.  The driver
deduplicates equal basis polynomials and keeps every basis vector whose weight
is at least the deficit threshold `i*B`.

The h-adic Jacobian identity is the same as the K16 generator.  For
`a*h^r` and `b*h^s`,

```text
J(a h^r, b h^s)
 = h^(r+s) J(a,b)
 + h^(r+s-1) (s*b*J(a,h) + r*a*J(h,b)).
```

Each level is monically divided by `h` in `y`; no coefficient leader is
inverted.  The level-0 normal form is compared with `c*x^k`, and the emitted
ideal is the coefficient ideal plus the Rabinowitsch equation
`T*(c*Omega)-1`.

The sparse tower is narrower than the full D1 monomial inventory, so the driver
records both the tower and the support envelope.  In each metadata JSON:

```text
h_parameter_count     number of b_i in the approximate-root tower,
h_lower_support_count number of monomials actually present in h-H_top,
lemma21_h_support     corrected D1/Lemma-2.1 support envelope,
lemma21_support_ok    set(h-H_top support) subset lemma21_h_support.
```

All promoted rows have `lemma21_support_ok=True`.  The reductions are therefore
typed as order-tower reductions, not as generic D1 reductions.  Representative
support counts:

```text
(33,22) [3]: h parameters 11, h support 13, D1/Lemma support contains it.
(45,30) [4]: h parameters 15, h support 20, D1/Lemma support contains it.
(25,15) [3]: h parameters 5,  h support 7,  D1/Lemma support contains it.
```

Artifact layout:

```text
box/orderchart-20260903/order_chart.py          generator
box/orderchart-20260903/meta/*.json             counts, gauges, sanity gates
box/orderchart-20260903/systems/*.sing          standard-basis scripts
box/orderchart-20260903/logs/*.out|*.err|*.time Singular outputs and time -v
box/orderchart-20260903/builders/*.sing         native row emitters
box/orderchart-20260903/rows/*_rows.tsv         native coefficient rows
```

Representative CAS commands:

```text
timeout --kill-after=10s 1200s Singular --cpus=1 --threads=1 --flint-threads=1 -q --no-rc <system.sing>
timeout --kill-after=10s  600s Singular --cpus=1 --threads=1 --flint-threads=1 -q --no-rc <builder.sing>
```

Every completed standard-basis log printed `CONTROL_EMPTY_PASS`,
`CONTROL_NONEMPTY_PASS`, `MAIN_DONE basis_size=1`, and
`MAIN_SATURATED_EMPTY`.

## Gauge Audit

Safe for general `k`:

1. `Q -> Q - const(beta_q)` is a target translation when `1 in S_q`.
2. `P -> P - const(alpha_e)` is a target translation when `1 in S_e`.
3. `P -> P - alpha_(e-q)*Q` is used only when `alpha_(e-q)` is scalar and each
   beta space embeds into the shifted alpha space:
   `S_j(beta) subset S_{j+e-q}(alpha)`.

Thus the K16 `alpha_t=0` gauge is not copied by name.  It is the special case
`e-q=t`.  If the scalar/embedding test fails, the driver omits the shear and
records that forcing it would be a slice.  This occurs in the delta1-zero
check below.

## Validation Runs

All validation entries below are exact `Q` runs with `std(I)`, `T*(c*Omega)-1`,
and passing empty/nonempty wrapper controls.  `unk` excludes the Rabinowitsch
variable.

| row | stratum | unk | eq | h-par | h-support | alpha dims | beta dims | deg_x J0 | Q |
|---|---:|---:|---:|---:|---:|---|---|---:|---|
| `(16,12;13;3;k=1)` | `1` | 18 | 23 | 4 | 4 | `0,2,3,4` | `2,2` | 1 | `[1]`, 0:00.06 |
| `(28,20;25;3;k=1)` | `1` | 27 | 37 | 4 | 4 | `1,0,2,2,3,3,4` | `1,2,2,2` | 1 | `[1]`, 2:26.55 |
| `(33,22;30;8;k=1)` | `3` | 19 | 54 | 11 | 13 | `0,2,4` | `1` | 3 | `[1]`, 0:00.02 |
| `(33,22;30;8;k=1)` | `2+1` | 20 | 54 | 11 | 13 | `0,2,4` | `1` | 3 | `[1]`, 0:00.02 |
| `(45,30;42;11;k=1)` | `4` | 23 | 84 | 15 | 20 | `0,2,4` | `1` | 4 | `[1]`, 0:00.01 |
| `(45,30;42;11;k=1)` | `3+1` | 24 | 84 | 15 | 20 | `0,2,4` | `1` | 4 | `[1]`, 0:00.03 |
| `(45,30;42;11;k=1)` | `2+2` | 24 | 84 | 15 | 20 | `0,2,4` | `1` | 4 | `[1]`, 0:00.02 |
| `(15,10;11;3;k=2)` | `2` | 17 | 37 | 5 | 5 | `0,4,4` | `3` | 3 | `[1]`, 0:00.02 |
| `(15,10;11;3;k=2)` | `1+1` | 18 | 37 | 5 | 5 | `0,4,4` | `3` | 3 | `[1]`, 0:00.02 |
| `(21,14;18;5;k=1)` | `2` | 15 | 30 | 7 | 7 | `0,2,4` | `1` | 2 | `[1]`, 0:00.02 |
| `(21,14;18;5;k=1)` | `1+1` | 16 | 30 | 7 | 7 | `0,2,4` | `1` | 2 | `[1]`, 0:00.02 |

The K16 banked counts are reproduced exactly: `(16,12)` is `18/23`, and
`(28,20)` is `27/37`.

Count comparison against the banked A/B symbolic-strata charts:

```text
(33,22) A/B: 28,29 unknowns -> order chart: 19,20.
(45,30) A/B: 44,45,45 unknowns -> order chart: 23,24,24.
```

Actual-pair control: `(pi, pi-gamma^2/2)` has `J=x` and pi-degrees `(1,1)`.
It fails the requested descended tuple classifier and is not a witness for any
row above.

Primary validation artifacts:

| row/stratum | script | log |
|---|---|---|
| `(16,12)` `1` | `box/orderchart-20260903/systems/16_12_13_3_k1_part_1_Q_std.sing` | `box/orderchart-20260903/logs/16_12_13_3_k1_part_1_Q_std.out` |
| `(28,20)` `1` | `box/orderchart-20260903/systems/28_20_25_3_k1_part_1_Q_std.sing` | `box/orderchart-20260903/logs/28_20_25_3_k1_part_1_Q_std.out` |
| `(33,22)` `3` | `box/orderchart-20260903/systems/33_22_30_8_k1_part_3_Q_std.sing` | `box/orderchart-20260903/logs/33_22_30_8_k1_part_3_Q_std.out` |
| `(33,22)` `2+1` | `box/orderchart-20260903/systems/33_22_30_8_k1_part_2_1_Q_std.sing` | `box/orderchart-20260903/logs/33_22_30_8_k1_part_2_1_Q_std.out` |
| `(45,30)` `4` | `box/orderchart-20260903/systems/45_30_42_11_k1_part_4_Q_std.sing` | `box/orderchart-20260903/logs/45_30_42_11_k1_part_4_Q_std.out` |
| `(45,30)` `3+1` | `box/orderchart-20260903/systems/45_30_42_11_k1_part_3_1_Q_std.sing` | `box/orderchart-20260903/logs/45_30_42_11_k1_part_3_1_Q_std.out` |
| `(45,30)` `2+2` | `box/orderchart-20260903/systems/45_30_42_11_k1_part_2_2_Q_std.sing` | `box/orderchart-20260903/logs/45_30_42_11_k1_part_2_2_Q_std.out` |

## Open Row Runs

For `(25,15;21;2;k=2)` the closed-form data are

```text
K=5, u'=3, e=5, q=3, delta2'=-1, delta1'=7/5, B=-1/5.
```

The old generic charts had 135, 136, and 137 unknowns with 517 rows.  The
order chart has 12, 13, and 14 unknowns with 21 equations.  Direct `std(I)`
finished in every field, so no Q-star pivots, grading normalization, or slice
was used.

| stratum | unk | eq | alpha dims | beta dims | deg_x J0 | 32003 | 32009 | 32027 | Q | verdict |
|---|---:|---:|---|---|---:|---|---|---|---|---|
| `3` | 12 | 21 | `1,0,1,1,2` | `1,0` | 3 | `[1]` 0:00.02 | `[1]` 0:00.02 | `[1]` 0:00.01 | `[1]` 0:00.02 | `SATURATED-EMPTY` |
| `2+1` | 13 | 21 | `1,0,1,1,2` | `1,0` | 3 | `[1]` 0:00.02 | `[1]` 0:00.01 | `[1]` 0:00.02 | `[1]` 0:00.02 | `SATURATED-EMPTY` |
| `1+1+1` | 14 | 21 | `1,0,1,1,2` | `1,0` | 3 | `[1]` 0:00.02 | `[1]` 0:00.02 | `[1]` 0:00.02 | `[1]` 0:00.01 | `SATURATED-EMPTY` |

## Delta1 Zero Rows

Time remained for `(21,14;15;6;k=4)`.  Here

```text
K=7, u'=1, e=3, q=2, delta2'=-1, delta1'=0, B=-1.
```

The emitted order chart has 38 unknowns and 57 equations.  The shear
`alpha_1=0` is **not** safe because `alpha_1` is not scalar; the driver records
`alpha_1 shear omitted; forcing it would be a slice`.

The h-adic sanity gate fails: `deg_x J0=2<k=4`.  The saturated systems are
nevertheless `[1]` over all three primes and over `Q` in 0.04 seconds or less,
but this is reported as **INSTRUMENT-FAIL / degenerate order chart**, not as a
promoted row kill.

## Verdict

CONFIRMED for the requested instrument:

```text
K16 count replay:        PASS
banked validation rows:  SATURATED-EMPTY over Q
open (25,15) row:        SATURATED-EMPTY over 32003, 32009, 32027, and Q
preprocessing needed:    no
delta1'=0 row:           degenerate/instrument-fail, not promoted
```

FALLACY-v2 check: the saturation is Rabinowitsch in the declared ring, no
parameter-dependent pivot is inverted, raw/full Jacobian degree is not used as
a promotion shortcut, and the general target shear is applied only after the
scalar/shifted-space check.  No exit-price assertion is made, so no
`charge_basis=...` line is due.

<!-- BODY-END -->
