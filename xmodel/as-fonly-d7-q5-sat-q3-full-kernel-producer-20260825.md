# AS F-only D7: three complete pointwise Q4 fibres admit exact Q3 lifts

**Status:** different-model `CONFIRMED`.  All substantive replay ran on AWS.  This note does not claim a complete map modulo 243, an all-depth lift, a counterexample, or any JC2 consequence.

## Typed claim

For each of the three displayed Q5 predecessor states `base0000`, `base0270`, and `base0513`, consume the *entire* affine solution fibre of the reviewed chronological Q4 gate.  Add all degree-four order-81 source digits `H4,J4`.  Impose, from the literal integer Jacobian determinant,

- the four homogeneous degree-three coefficient rows after exact division by 81, modulo 3; and
- all 63 over-cap coefficient rows of total degrees 7 through 12 after exact division by 243, modulo 3.

The resulting 67-row equations are affine on each full finite coefficient cube.  Exact quadratic designs (zero, both nonzero multiples of every basis vector, and every pair sum) check that every pure and mixed quadratic remainder is zero; RREF then describes the whole cube, not a sample.

All three systems are consistent:

| predecessor | variables | design points | rank | kernel | displayed `H4` | displayed `J4` | exact output SHA-256 |
|---|---:|---:|---:|---:|---|---|---|
| base0000 | 18 | 190 | 4 | 14 | `(0,2,0,0,2)` | `(0,0,1,0,0)` | `89c9b8bfb4c46b566e10e7f5716502b0a3b6f64af29a5f4e14234cc09b945187` |
| base0270 | 14 | 120 | 4 | 10 | `(0,0,0,0,2)` | `(0,0,0,0,0)` | `9016e7737c7f3a31107a80f4da91e1e8cec7be686569cd548e55e135fcec4dfb` |
| base0513 | 14 | 120 | 4 | 10 | `(0,0,0,0,0)` | `(0,0,0,0,0)` | `e2711128f358f5b65f215a2898ccf90fa10a7e1e6908ccdde7c9a4410290b4bb` |

For each displayed particular the producer reconstructs the integer map, rechecks the inherited five Q4 rows, the four Q3 rows, and all 63 terminal rows, and verifies coefficientwise divisibility by 729 in total degrees 7 through 12.  The zero-`H4,J4` omission control fails rows `(0,2,3)` at base0000 and row `3` at base0270; it happens to pass at base0513.

## Load-bearing valuation result

Literal determinant valuations after the Q3 lift are:

- base0000: degrees `0..12` have minima `∞,3,3,5,5,5,5,6,6,6,6,6,7`;
- base0270: `∞,3,3,5,5,5,5,6,6,6,6,6,6`;
- base0513: `∞,3,3,5,5,5,5,6,6,6,6,6,6`.

Thus degrees one and two still begin at order 27.  An order-81-only Q2/Q1 continuation is ill-typed.  The source-honest successor must first introduce order-27 degree-three/two pieces and only then order-81 degree-three/two pieces, with carries recomputed between levels.  Degree zero is exactly absent for all three displayed points at this gate.

## Source and replay custody

Case: `cases/as_fonly_d7_q5_sat_q3_full_kernel_20260825/`

- producer SHA-256: `14d69e65255482491293373bbbd212742e2077322931e65b8d5af215915d303b`
- remote runner SHA-256: `6006df0a49d5fcd27fcd2e1137449b7c795b1b75e31a8e7709cc793c7d7ef1e7`
- pinned Q4 parent SHA-256: `ed19ea87d2252e9e483a5c3970549eeac2db62d064e7bd900698b600739180a4`
- different-model Q4-parent review SHA-256: `6a77ff242a4d56461878a25dec7a3321e923f9c29a780ebad6e41d94f9fc6779` (`CONFIRMED`; its harmless `OUTPUT.sha256` self-hash custody noise is not used as mathematical evidence)
- different-model Q3 producer review SHA-256: `81a9531d622b1f0ded90eb5701386ce059c6a60a24c4a469f9bff0d99281b973` (`CONFIRMED`; it independently checks that the Q4-kernel columns vanish identically and that the remaining six-dimensional `H4/J4` solution operator is common to the three parents)
- AWS endpoint: Box02, `/home/ubuntu/jobs/as_q5_sat_q3_full_kernel_20260825T121434Z`
- all three remote exit codes: zero; stderr contains only bounded `/usr/bin/time -v` custody.

Portable AWS replay from a staged repository closure:

```bash
export JC2_ROOT=/path/to/jc2
export OUTPUT_ROOT=/path/to/fresh/output
bash "$JC2_ROOT/cases/as_fonly_d7_q5_sat_q3_full_kernel_20260825/replay_all.sh"
```

The manifest and freeze in the case pin the copied input models, parent outputs, matrices/RHS-bearing JSON, logs, and source closure.

## Refusal scope

This is exactly three pointwise Q5 predecessor states and their complete displayed Q4 affine fibres.  It is not the whole Q5 locus; it does not restore Q2, Q1, or Q0; it is not a complete determinant-one map modulo 243; it supplies no infinite 3-adic lift, algebraization, collision, counterexample, or JC2 conclusion.
