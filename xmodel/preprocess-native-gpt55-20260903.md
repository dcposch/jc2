# Native preprocessing pipeline for large two-point charts

Date: 2026-09-03 UTC.

## Custody

MEASURED. The checksum manifest was generated mechanically from `xmodel/preprocess-native-gpt55-20260903.run.v2` and checked with `sha256sum -c`; all 12 frozen inputs under `/tmp/jc2-lane.lpjOgw/inputs` returned `OK`.

| # | frozen input | sha256 |
|---:|---|---|
| 1 | `emitter-native-gpt55-20260903.md` | `455d42bb1002093427976f67d5c3351fd37b6995c0a4accb7b666b586e2711cd` |
| 2 | `emit_chart.py` | `28cf67fd5386a9fef69094f3f00c4944a4930c79d4c464df170a9513a1224e66` |
| 3 | `emit_chart.sing` | `3c8075b59d81ec996cfb553df2edd4f1fb55f92d33fb9cec5ee1e3e7dd999f2f` |
| 4 | `validation.json` | `ddc23e03e84e3462add743862bf5af459db7cd1d993d4c6f73b7a5f2799d3299` |
| 5 | `bigrows-preprocess-gpt55-20260903.md` | `3f994067f8149636fc81e57e98122261dc1435d4c0ac77f266893e58646c5273` |
| 6 | `preprocess.py` | `67b3735d27d8b92af2bf091566a14f9b2f49163577f51d54da751a76d22b2f2a` |
| 7 | `k16-t3-gate-gpt55-20260903.md` | `5593aa5443dd755cadedca4b0d284a3dec4048f7cd5822da576587552f36aba6` |
| 8 | `k16-t4-normalizer-gate-gpt55-20260903.md` | `e868a7f2df3814caf1847411918c17cbf8e71688779819fd4764d70e9d86ae83` |
| 9 | `triangular_preprocess.py` | `f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93` |
| 10 | `t_order_system.py` | `e115d576e850523f8796008d1b9d7899382cbac918ac2e74419207d9e7e7dc28` |
| 11 | `shape.py` | `ba25cd10fa5cc998017688db455094bcd3b7a8e870085dd2db64fb4f66b098de` |
| 12 | `FALLACY-v2.md` | `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5` |

MEASURED. New writes are confined to `box/preprocess-native-20260903/` and this report. No ledger, `jc2-lean`, `ideation-*`, or in-progress lane report was edited.

## Implementation

MEASURED. `prep.sing` implements the native Singular stage. It detects only rows `f=a*x+b` with `a in Q*`, `x` absent from `b`, substitutes `x=-b/a` by `subst`, and records each pivot. Parameter-dependent coefficients are rejected because the derivative coefficient must have total degree zero. The same Singular session exports exact monomial exponent-difference constraints for the residual ideal.

MEASURED. `prep.py` streams the emitter row TSV into generated Singular scripts by copying polynomial payload text verbatim. Python does not parse the 42-180 MB expressions symbolically; it only reads row metadata, ring variables, Singular's small audit files, and the integer exponent-difference matrix. The grading step solves that matrix exactly over `Q` and reports rank/nullity and a primitive positive weight vector when one is found.

AUDIT. The current driver also contains slice/base-scan helpers in `prep.sing`, but the `(25,15)` native Q stage below does not reach a usable forced-nonzero slice. No division by a parameter-dependent pivot is promoted.

## Validation

| case | native Q pivots | residual | grading | field/std verdict | wall |
|---|---:|---|---|---|---:|
| K16 t=3 | 13 | 35 rows, 23 vars | POSITIVE, rank 22/nullity 1 | SATURATED-EMPTY | 0.167 s |
| K16 t=4 | 16 | 46 rows, 29 vars | POSITIVE, rank 28/nullity 1 | SATURATED-EMPTY | 1.490 s |
| `(33,22;30;8;1)` `[3]` | - | 62 rows, 28 vars | direct exact | SATURATED-EMPTY | 0.036 s |

MEASURED. The K16 t=3 native Q stage reproduces `36 -> 23` variables including `c`; the charged normalized field script over `Q[q7_1]/(147*q7_1^2-84*q7_1+11)` replays as `[1]` from 6 generators.

MEASURED. The K16 t=4 native Q stage reproduces `45 -> 29` variables including `c`; the charged `Q(sqrt15)` eight-generator `nfmodStd` replay returns `[1]`.

### Validation Audit

| case | qstage wall | qstage residual artifact | exponent constraints | natural-weight check | exact script/log | RSS |
|---|---:|---|---:|---|---|---:|
| K16 t=3 | 11.816 s | `box/preprocess-native-20260903/results/k16_t3_native_residual.tsv (53.8 KB)` | 2104 | VERIFIED_NATURAL, nonhom=0 | `box/k16t3-20260903/preprocessed/t3_normalized_K_std.sing; box/preprocess-native-20260903/logs/k16_t3_normalized_K_std.out, box/preprocess-native-20260903/logs/k16_t3_normalized_K_std.err` | 13280 |
| K16 t=4 | 21.868 s | `box/preprocess-native-20260903/results/k16_t4_native_residual.tsv (171.1 KB)` | 6307 | VERIFIED_NATURAL, nonhom=0 | `box/k16t4-gate-20260903/t4_exact_Qsqrt15_nfmodstd.sing; box/preprocess-native-20260903/logs/k16_t4_Qsqrt15_nfmodstd.out, box/preprocess-native-20260903/logs/k16_t4_Qsqrt15_nfmodstd.err` | 15672 |
| `(33,22;30;8;1)` `[3]` | - | direct system | - | direct exact | `box/emitter-20260903/systems/33_22_part_3_ab_Q.sing`; `box/preprocess-native-20260903/logs/33_22_part_3_ab_Q.out`, `box/preprocess-native-20260903/logs/33_22_part_3_ab_Q.err` | 11440 |

MEASURED. The K16 grading LPs were solved from exact exponent-difference TSVs exported by Singular: t=3 has 2104 constraints, 1047 unique constraints, rank 22 and nullity 1; t=4 has 6307 constraints, 3172 unique constraints, rank 28 and nullity 1. In both cases the natural-weight verifier reports zero nonhomogeneous residual rows.

## `(25,15;21;2;k=2)`

| stratum | unknowns | rows | native Q status | pivots | residual/stuck replay | grading | base row | field | verdict |
|---|---:|---:|---|---:|---|---|---|---|---|
| `1+1+1` | 137 | 517 | TIMEOUT | 3 | not reached; replay OK, 514 rows | NOT_RUN_INCOMPLETE_SINGULAR_STAGE; natural=MISSING | not reached | not reached | COUNTING-BOUND: native Q* stage timed out before a certificate |
| `2+1` | 136 | 517 | TIMEOUT | 6 | not reached; replay OK, 510 rows | NOT_RUN_INCOMPLETE_SINGULAR_STAGE; natural=MISSING | not reached | not reached | COUNTING-BOUND: native Q* stage timed out before a certificate |
| `3` | 135 | 517 | TIMEOUT | 13 | not reached; replay OK, 498 rows | NOT_RUN_INCOMPLETE_SINGULAR_STAGE; natural=MISSING | not reached | not reached | COUNTING-BOUND: native Q* stage timed out before a certificate |

MEASURED. The base rows, coefficient fields, and final exact standard bases for the three `(25,15)` strata were not reached in this bounded run. Where a stuck replay completed, the post-pivot residual TSV and JSON audit are listed in `box/preprocess-native-20260903/results/`; otherwise the exact retained data are the original row TSV plus the checked partial Q*-pivot chain. No mathematical emptiness claim is made from a timeout.

### Target Artifacts

| stratum | source rows | row sha256 | qstage script | qstage logs | pivot TSV | stuck residual | stuck JSON |
|---|---|---|---|---|---|---|---|
| `1+1+1` | `box/emitter-20260903/rows/25_15_part_1_1_1_generic_rows.tsv` | `88dfc843516b61d63c3635f74a4a6e2ccb6d2e3999b617c5e00726f0722645ba` | `box/preprocess-native-20260903/work/25_15_part_1_1_1_generic_qstage.sing` (180.4 MB) | `box/preprocess-native-20260903/logs/25_15_part_1_1_1_generic_qstage.out; box/preprocess-native-20260903/logs/25_15_part_1_1_1_generic_qstage.err` | `box/preprocess-native-20260903/results/25_15_part_1_1_1_generic_pivots.tsv` | `box/preprocess-native-20260903/results/25_15_part_1_1_1_generic_stuck_after_3_residual.tsv (178.0 MB, 514 rows)` | `box/preprocess-native-20260903/results/25_15_part_1_1_1_generic_stuck_after_3.json` |
| `2+1` | `box/emitter-20260903/rows/25_15_part_2_1_generic_rows.tsv` | `692905e95e195a1ad76cc6e2075403f607005c8ed22f3b1e6b25472d472586d4` | `box/preprocess-native-20260903/work/25_15_part_2_1_generic_qstage.sing` (91.5 MB) | `box/preprocess-native-20260903/logs/25_15_part_2_1_generic_qstage.out; box/preprocess-native-20260903/logs/25_15_part_2_1_generic_qstage.err` | `box/preprocess-native-20260903/results/25_15_part_2_1_generic_pivots.tsv` | `box/preprocess-native-20260903/results/25_15_part_2_1_generic_stuck_after_6_residual.tsv (86.2 MB, 510 rows)` | `box/preprocess-native-20260903/results/25_15_part_2_1_generic_stuck_after_6.json` |
| `3` | `box/emitter-20260903/rows/25_15_part_3_generic_rows.tsv` | `9273f538d8954f49b7529e79c848391eccd2e1a169adc20b191404e5ea65d742` | `box/preprocess-native-20260903/work/25_15_part_3_generic_qstage.sing` (42.4 MB) | `box/preprocess-native-20260903/logs/25_15_part_3_generic_qstage.out; box/preprocess-native-20260903/logs/25_15_part_3_generic_qstage.err` | `box/preprocess-native-20260903/results/25_15_part_3_generic_pivots.tsv` | `box/preprocess-native-20260903/results/25_15_part_3_generic_stuck_after_13_residual.tsv (56.4 MB, 498 rows)` | `box/preprocess-native-20260903/results/25_15_part_3_generic_stuck_after_13.json` |

### Partial Q* Chains

MEASURED. The following are the completed affine pivots before timeout. Each coefficient is the recorded constant `Q*` coefficient, and each `rhs#` is the SHA-256 prefix of the recorded right-hand side payload in the pivot TSV. The replay stage verifies `subst(row, variable, rhs)==0` for every listed pivot before writing the stuck residual.

`1+1+1` (3 pivots):
1:A1_1_1 row=516 hxy=7/0/0 coeff=-15 rhs#0d0bff26d82d; 2:A1_1_2 row=515 hxy=7/0/1 coeff=-15 rhs#5287e5f69690; 3:A1_1_3 row=514 hxy=7/0/2 coeff=-15 rhs#028f36ccd443.

`2+1` (6 pivots):
1:A1_1_1 row=516 hxy=7/0/0 coeff=-15 rhs#b78edacb969e; 2:A1_1_2 row=515 hxy=7/0/1 coeff=-15 rhs#6ed14199f52b; 3:A1_1_3 row=514 hxy=7/0/2 coeff=-15 rhs#2402d06bf941; 4:A1_1_4 row=513 hxy=7/0/3 coeff=-15 rhs#5feceb66ffc8; 5:A1_2_2 row=511 hxy=7/1/1 coeff=-30 rhs#c0471b528ff5; 6:A1_2_3 row=510 hxy=7/1/2 coeff=-30 rhs#5feceb66ffc8.

`3` (13 pivots):
1:A1_0_2 row=516 hxy=7/0/0 coeff=-18 rhs#029e4d3a7bd5; 2:A1_0_3 row=515 hxy=7/0/1 coeff=-27 rhs#59026b2b0e79; 3:A1_0_4 row=514 hxy=7/0/2 coeff=-36 rhs#778f341d73dc; 4:A1_1_4 row=513 hxy=7/0/3 coeff=-15 rhs#5feceb66ffc8; 5:A1_1_2 row=512 hxy=7/1/0 coeff=-12 rhs#dcfc37242753; 6:A1_1_3 row=511 hxy=7/1/1 coeff=-21 rhs#b87ff81e6edf; 7:A1_2_3 row=510 hxy=7/1/2 coeff=-30 rhs#5feceb66ffc8; 8:A1_2_2 row=509 hxy=7/2/0 coeff=-6 rhs#ee38f3257a4f; 9:A1_3_2 row=508 hxy=7/2/1 coeff=-45 rhs#5feceb66ffc8; 10:A2_0_4 row=504 hxy=6/0/2 coeff=-36 rhs#97487e5f21dd; 11:A2_1_4 row=503 hxy=6/0/3 coeff=-15 rhs#c1df3c8c76b0; 12:A1_0_1 row=502 hxy=6/0/4 coeff=-9 rhs#04a67e6df056; 13:A2_0_3 row=501 hxy=6/1/0 coeff=-27 rhs#507b6ae2430e.

AUDIT. These chains are branch-free only because their leading coefficients are constants in `Q*`. They do not license division by any parameter-dependent expression, and the timeout point is reported as a retained exact system rather than as an emptiness certificate.

MEASURED. The optional `(24,16;17;2;5)` stratum was not run; the required `(25,15)` bounded native passes plus stuck-system replays consumed the available lane time.

## Verdict

CONFIRMED. The native lane removes the SymPy parser from the row-file path and validates the Q*-pivot/field-certificate pattern on the K16 t=3/t=4 controls, plus the `(33,22)` `[3]` exact `[1]` check.

COUNTING-BOUND. The three `(25,15)` strata are not promoted to saturated-empty here. The blocker has moved from Python parsing to native affine elimination or the absence of a certificate after that stage.

ENABLED. The same driver can now be pointed at the remaining large row files and later `(99,66)` joint chart bands without SymPy ingest; the next useful improvement is a stronger native sparse/compiled affine pass plus in-Singular branch generation for the slice/base-factor field systems.

FALLACY-v2. No new exit-price assertion is made, so no `charge_basis=...` line is due. Saturation, representative, and timeout statuses are kept separate.

<!-- BODY-END -->
