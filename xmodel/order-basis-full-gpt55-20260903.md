# Order-Basis Full Necessary Over-Approximation Audit

Date: 2026-09-04

Status: completed skeleton-level instrument repair. The corrected instrument
was built and row systems were emitted. The requested row deaths are not
confirmed: the corrected full standard-basis jobs timed out before a basis
verdict.

## Scope

Inputs were the frozen lane copies under `/tmp/jc2-lane.sA4mxQ/inputs`.
The repair target was the general order chart charged in
`xmodel/order-chart-general-gpt55-20260903.md`, with the row-specific audit
`xmodel/row2515-order-gate-sol56-20260903.md`, the D=108 no-split descent
report, the D=108 split/minor report, Moh 1983, Xu 2016, and `FALLACY-v2.md`.

Driver directory:

`box/orderbasis-20260903/`

Main driver:

`box/orderbasis-20260903/order_basis_full.py`

## Hash Verification

The manifest was regenerated mechanically from
`xmodel/order-basis-full-gpt55-20260903.run.v2`; no digest was retyped into the
check. The driver emitted
`box/orderbasis-20260903/charged_input_manifest.sha256` and all 16 charged
inputs passed. Manifest hash:

`d03a8ec37a5eddd5d309d0b0c50770ff01d5479f5d492da37c49b717bc5fc58e`

## Moh Theorem 1.2 Use

Moh Theorem 1.2 is a necessary lower-bound statement on the coefficients of a
descended two-point datum. In the notation used here, if

`f = h^d + a_1 h^(d-1) + ... + a_d`

and the coherent complete system has accuracy `lambda`, while `h` is a
`d`-th quasi-approximate root with accuracy `lambda/d`, then every descended
coefficient must satisfy, at every emitted root `sigma`,

`ord a_j(sigma) >= j*lambda/d`, for `j = 1,...,d`.

In this order-chart normalization the monomial weight is

`wt(x^r y^s) = -r + delta_1' * s`.

The chart must therefore include every monomial in the relevant finite
polynomial inventory whose weight meets the lower bound. Equality with a
small emitted filtered basis is not a theorem. This is exactly the
`FALLACY-v2` floor/attainment issue: a lower bound is not an exact support
description.

## Corrected Instrument

For row `(n',m';M_2',V_2';k)` define

- `K = gcd(n',m')`, `e = n'/K`, `q = m'/K`, `u' = K - V_2'`;
- `R = n' - M_2' - 1`, `Pi = e + q`;
- `delta_2' = -(k+1)/R`;
- `delta_1' = (k+1)(Pi*u' - R)/(R(Pi*V_2' - 1))`;
- `B = V_2' delta_1' + u' delta_2'`.

The repaired finite `D_1` over-approximation uses:

- top face fixed by the root partition;
- `h` lower monomials `x^r y^s` with `s < K`, `r+s < K`,
  `0 <= r <= u'`, and `wt(x^r y^s) >= B`;
- coefficient monomials for deficit `j`: `x^r y^s` with `s < K`,
  `r+s <= jK`, and `wt(x^r y^s) >= jB`;
- constant translation gauges only where the constant monomial is present in
  the terminal coefficient space;
- the old scalar shear gauge only if the full `alpha_{e-q}` space is exactly
  scalar and every shifted `beta` monomial embeds in the target `alpha` space.

The shear audit fails for both target rows. Therefore the corrected systems
do not set the shear coefficient space to zero:

- `(25,15;21;2;k=2)`: `alpha_2` has full dimension 19, not scalar; shifted
  `beta` does not embed.
- `(24,16;18;7;k=4)`: `alpha_1` has full dimension 16, not scalar; shifted
  `beta` does not embed.

## Diagnosis

Artifact:

`box/orderbasis-20260903/diagnostics.json`

The strict-subfamily causes are present as follows.

| row | partition | `delta_1'` | full `h` | old image rank | `h` cokernel | max coefficient cokernel | diagnosis |
|---|---:|---:|---:|---:|---:|---:|---|
| `(25,15;21;2;k=2)` | `3` | `7/5` | 9 | 5 | 4 | 20 | (a) and (b) |
| `(25,15;21;2;k=2)` | `2+1` | `7/5` | 9 | 5 | 4 | 20 | (a) and (b) |
| `(25,15;21;2;k=2)` | `1+1+1` | `7/5` | 9 | 5 | 4 | 20 | (a) and (b) |
| `(24,16;18;7;k=4)` | `1` | `0` | 15 | 8 | 7 | 23 | (a), (b), and (c) |

For `(25,15)`, the old prefix tower image misses

`x*y^3`, `x*y^2`, `x^2*y^2`, `x*y`.

For D=108 no-split, the old prefix tower image misses

`x*y^6`, `x*y^5`, `x*y^4`, `x*y^3`, `x*y^2`, `x*y`, `x`.

The coefficient map cokernel is also nonzero. Therefore the sparse
`H_1..H_K` chart is not a valid necessary over-approximation for either target
row. The omitted directions were added in the corrected systems.

## `delta_1' = 0`

The D=108 no-split row has

`(K,e,q,u',R,Pi,delta_1',delta_2',B) = (8,3,2,1,5,5,0,-1,-1)`.

This is a slope-zero degeneration: the numerator in the slope formula
vanishes, so the centre exponent no longer raises the `D_1` order. The
necessary inequality becomes `-r >= -j` for deficit `j`, and the full
coefficient spaces must include the `x` directions through degree `j` for
every allowed centre power. The corrected D=108 builder includes those
directions.

The standalone old row `-c` is not emitted as a kill. In the corrected native
row extraction:

- `level0_deg_x_before_minus_c = 17`;
- `target_xk_level0_nonzero = 1`;
- rows emitted: 472.

Thus the target coefficient exists in the full support and is not forced to be
the isolated equation `-c = 0`.

## Row `(25,15;21;2;k=2)`

Corrected builders:

- `box/orderbasis-20260903/builders/25_15_21_2_k2_part_3_full_builder.sing`
- `box/orderbasis-20260903/builders/25_15_21_2_k2_part_2_1_full_builder.sing`
- `box/orderbasis-20260903/builders/25_15_21_2_k2_part_1_1_1_full_builder.sing`

Native row extraction completed for all three partitions:

| partition | unknowns excluding `T` | rows | `h` monomials | `alpha` dims | `beta` dims | native target gate |
|---:|---:|---:|---:|---|---|---|
| `3` | 141 | 598 | 9 | `12,19,20,21,21` | `19,19` | nonzero |
| `2+1` | 142 | 598 | 9 | `12,19,20,21,21` | `19,19` | nonzero |
| `1+1+1` | 143 | 598 | 9 | `12,19,20,21,21` | `19,19` | nonzero |

For all three partitions the native gate reports:

`level0_deg_x_before_minus_c = 21`, `target_xk_level0_nonzero = 1`.

Systems were emitted over `Q`, `p=32051`, and `p=32057` for all three
partitions under `box/orderbasis-20260903/systems/`.

Completed decision attempt:

`box/orderbasis-20260903/systems/25_15_21_2_k2_part_3_full_p32051_slimgb.sing`

Command shape:

`timeout 1800 Singular --cpus=1 --threads=1 --flint-threads=1 -q --no-rc <system>`

Result:

- return code 124;
- wrapper controls passed;
- `MAIN_START equations=598 unknowns=141 char=32051 algorithm=slimgb`;
- no `MAIN_DONE`, no `MAIN_SATURATED_EMPTY`, no `MAIN_NONTRIVIAL`.

The first full necessary modular decision timed out. Since the smallest
partition/field did not produce `[1]`, the row cannot be promoted to
`CONFIRMED[2515-DEAD]` in this lane. The remaining emitted Q and prime systems
were not launched after this timeout, because they cannot repair the missing
completed decision for the already-open full chart within the bounded lane.

Verdict:

`OPEN[FULL-BASIS-TIMEOUT]`, not dead.

## D=108 No-Split Row

Target descended no-split pair:

`(24,16; M_2'=18, V_2'=7; k=4)`.

Corrected builder:

`box/orderbasis-20260903/builders/24_16_18_7_k4_part_1_full_builder.sing`

Native row extraction completed:

| partition | unknowns excluding `T` | rows | `h` monomials | `alpha` dims | `beta` dims | native target gate |
|---:|---:|---:|---:|---|---|---|
| `1` | 110 | 472 | 15 | `16,24,31` | `23` | nonzero |

The native gate reports:

`level0_deg_x_before_minus_c = 17`, `target_xk_level0_nonzero = 1`.

Systems were emitted over `Q`, `p=32051`, and `p=32057`.

Completed decision attempt:

`box/orderbasis-20260903/systems/24_16_18_7_k4_part_1_full_p32051_slimgb.sing`

Command shape:

`timeout 1800 Singular --cpus=1 --threads=1 --flint-threads=1 -q --no-rc <system>`

Result:

- return code 124;
- wrapper controls passed;
- `MAIN_START equations=472 unknowns=110 char=32051 algorithm=slimgb`;
- no `MAIN_DONE`, no `MAIN_SATURATED_EMPTY`, no `MAIN_NONTRIVIAL`.

The split D=108 branch remains consumed from the charged `17(ddddd)` chain,
but the no-split corrected full necessary system did not return empty.
Therefore the skeleton-level row is not closed by this lane.

Verdict:

`OPEN[FULL-BASIS-TIMEOUT]`; D=108 is not closed at skeleton level here.

## Controls

Control artifact:

`box/orderbasis-20260903/controls/controls.json`

Tame two-point automorphism control:

- scripts: `box/orderbasis-20260903/controls/tame_automorphism_Q.sing`,
  `..._p32051.sing`, `..._p32057.sing`;
- stdout markers: `TAME_J_PASS`, `TAME_SURVIVES`;
- verdicts: `TAME-CONTROL-PASS` for all three fields.

Deliberately omitted necessary row control:

- script: `box/orderbasis-20260903/controls/omitted_target_row_control_Q.sing`;
- stdout markers: `OMITTED_ROW_FALSE_POINT_THROUGH`, `RESTORED_ROW_EMPTY`;
- verdict: `OMITTED-ROW-CONTROL-PASS`.

This proves the over-approximation is real: deleting a necessary row can admit
a false point, while restoring that row kills it.

K16 count replay and banked validation controls were checked against the local
charged artifacts:

| control | local log | count | basis |
|---|---|---:|---|
| K16 `(16,12;13;3;k=1) [1]` | `box/orderchart-20260903/logs/16_12_13_3_k1_part_1_Q_std.out` | 18/23 | `[1]` |
| K16 `(28,20;25;3;k=1) [1]` | `box/orderchart-20260903/logs/28_20_25_3_k1_part_1_Q_std.out` | 27/37 | `[1]` |
| banked `(15,10;11;3;k=2) [1,1]` | `box/orderchart-20260903/logs/15_10_11_3_k2_part_1_1_Q_std.out` | 18/37 | `[1]` |

The K16 rows have `K=4,u'=1`, so they remain useful arithmetic and CAS
controls for the one-direction case. They do not validate the multi-direction
prefix generalization. The banked `(15,10)` validation row is also a slice
control only: Moh Appendix II p.211 shows additional lower coefficient
directions, so completeness is not promoted from that sparse validation.

## Artifact Index

Corrected row metadata:

- `box/orderbasis-20260903/meta/25_15_21_2_k2_part_3_full.json`
- `box/orderbasis-20260903/meta/25_15_21_2_k2_part_2_1_full.json`
- `box/orderbasis-20260903/meta/25_15_21_2_k2_part_1_1_1_full.json`
- `box/orderbasis-20260903/meta/24_16_18_7_k4_part_1_full.json`

Corrected native row files:

- `box/orderbasis-20260903/rows/25_15_21_2_k2_part_3_full_rows.tsv`
- `box/orderbasis-20260903/rows/25_15_21_2_k2_part_2_1_full_rows.tsv`
- `box/orderbasis-20260903/rows/25_15_21_2_k2_part_1_1_1_full_rows.tsv`
- `box/orderbasis-20260903/rows/24_16_18_7_k4_part_1_full_rows.tsv`

Corrected `(25,15)` systems emitted:

- `box/orderbasis-20260903/systems/25_15_21_2_k2_part_3_full_Q_slimgb.sing`
- `box/orderbasis-20260903/systems/25_15_21_2_k2_part_3_full_p32051_slimgb.sing`
- `box/orderbasis-20260903/systems/25_15_21_2_k2_part_3_full_p32057_slimgb.sing`
- `box/orderbasis-20260903/systems/25_15_21_2_k2_part_2_1_full_Q_slimgb.sing`
- `box/orderbasis-20260903/systems/25_15_21_2_k2_part_2_1_full_p32051_slimgb.sing`
- `box/orderbasis-20260903/systems/25_15_21_2_k2_part_2_1_full_p32057_slimgb.sing`
- `box/orderbasis-20260903/systems/25_15_21_2_k2_part_1_1_1_full_Q_slimgb.sing`
- `box/orderbasis-20260903/systems/25_15_21_2_k2_part_1_1_1_full_p32051_slimgb.sing`
- `box/orderbasis-20260903/systems/25_15_21_2_k2_part_1_1_1_full_p32057_slimgb.sing`

Corrected D=108 no-split systems emitted:

- `box/orderbasis-20260903/systems/24_16_18_7_k4_part_1_full_Q_slimgb.sing`
- `box/orderbasis-20260903/systems/24_16_18_7_k4_part_1_full_p32051_slimgb.sing`
- `box/orderbasis-20260903/systems/24_16_18_7_k4_part_1_full_p32057_slimgb.sing`

System file sizes are a useful proxy for why the full-basis decision did not
behave like the old sparse chart:

| system family | smallest file | largest file |
|---|---:|---:|
| `(25,15) [3]` | 58,401,556 bytes | 58,401,564 bytes |
| `(25,15) [2+1]` | 127,884,540 bytes | 127,884,548 bytes |
| `(25,15) [1+1+1]` | 255,979,207 bytes | 255,979,215 bytes |
| `D=108 [1]` | 181,787,742 bytes | 181,787,750 bytes |

The old saturated-empty systems were small sparse projections. The corrected
systems carry the added `D_1` directions and omit the unsafe shear, so a
timeout is not surprising and is not mathematical evidence of emptiness.
This size change is also a direct operational check that the emitted basis is
not the old equality-prefix basis in different notation.

Decision-attempt manifest:

`box/orderbasis-20260903/decision_attempts.json`

Timeout captures:

- `(25,15) [3] p32051` stdout:
  `box/orderbasis-20260903/systems/25_15_21_2_k2_part_3_full_p32051_slimgb.sing.out`
- `(25,15) [3] p32051` stderr:
  `box/orderbasis-20260903/systems/25_15_21_2_k2_part_3_full_p32051_slimgb.sing.err`
- `D=108 [1] p32051` stdout:
  `box/orderbasis-20260903/systems/24_16_18_7_k4_part_1_full_p32051_slimgb.sing.out`
- `D=108 [1] p32051` stderr:
  `box/orderbasis-20260903/systems/24_16_18_7_k4_part_1_full_p32051_slimgb.sing.err`

## Mechanical Run Log

All lane jobs were run in the foreground with `timeout 1800`; Singular was
invoked with one core/thread for the corrected systems.

| step | result |
|---|---|
| `python3 -m py_compile box/orderbasis-20260903/order_basis_full.py` | pass |
| `order_basis_full.py manifest` | all 16 frozen inputs OK |
| `order_basis_full.py diagnose --rows all --all-partitions --write` | diagnostics JSON emitted |
| emit `(25,15)` builders for `3`, `2+1`, `1+1+1` | emitted |
| run `(25,15)` builders | all completed; 598 rows each |
| emit D=108 builder for `1` | emitted |
| run D=108 builder | completed; 472 rows |
| emit `(25,15)` Q and two-prime systems for all partitions | emitted |
| emit D=108 Q and two-prime systems | emitted |
| run `(25,15) [3] p32051` full system | timeout 124 after 1800 seconds; no basis marker |
| run D=108 `[1] p32051` full system | timeout 124 after 1800 seconds; no basis marker |
| run controls | tame and omitted-row controls pass |

Process hygiene: after the lane jobs, a stale unrelated
`box/k16stdhilb-20260903` Singular process was found under a `timeout 3000`
wrapper and was terminated as a process group so this turn did not end with a
Singular job running. A final `pgrep` found only the `pgrep` command itself.

## FALLACY-v2 Status

The corrected chart is an over-approximation of the necessary Moh Theorem 1.2
coefficient locus in the finite descended `D_1` inventory. If such a full
necessary over-approximation returns saturated empty, it is a valid kill.

The old charged chart was a strict sub-approximation:

- it used a sparse prefix tower;
- it omitted nonzero `D_1` coefficient cokernel directions;
- in the `delta_1'=0` row it emitted the old standalone `-c` equation.

Therefore the old saturated-empty results are not kills for `(25,15)` or
D=108 no-split.

## Verdicts

`(25,15;21;2;k=2)`:

`OPEN[FULL-BASIS-TIMEOUT]`. The full necessary systems were generated for all
three partitions over `Q`, `p=32051`, and `p=32057`; the completed corrected
decision attempt for partition `3` over `p=32051` timed out after 1800 seconds.
Do not promote `CONFIRMED[2515-DEAD]`.

D=108 no-split `(24,16;18;7;k=4)`:

`OPEN[FULL-BASIS-TIMEOUT]`. The corrected zero-slope system no longer has the
standalone `-c` kill. The completed modular decision attempt timed out after
1800 seconds. Since the no-split branch is not empty, the split-dead chain
does not close D=108 in this lane.

Corrected instrument spec for the 166-group / leftover-4-tuple batch:

Use `box/orderbasis-20260903/order_basis_full.py`. Require the full `D_1`
monomial inventory, the full coefficient-space cokernel audit, and the shear
audit before any row death is promoted. The `delta_1'=0` stratum must include
the zero-slope centre-support directions and must not emit `-c` as an isolated
row equation.

No new exit-price assertion is made in this report.

<!-- BODY-END -->
