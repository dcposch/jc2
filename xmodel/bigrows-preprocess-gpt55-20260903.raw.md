# Bigrows preprocessing lane

Date: 2026-09-03

## Custody

**MEASURED.** The manifest was generated from `xmodel/bigrows-preprocess-gpt55-20260903.run.v2`; every frozen input in `/tmp/jc2-lane.PIFGo9/inputs` matched its receipt hash.

**MEASURED.** Writes are confined to `box/bigrows-20260903/` and this report. No ledger, `jc2-lean`, `ideation-*`, or named in-progress lane file is edited by the driver.

**MEASURED.** `Singular for x86_64-Linux version 4.3.2 (4330, 64 bit) Apr  1 2024 04:44:00`.

## Driver

**MEASURED.** `box/bigrows-20260903/preprocess.py` builds the corrected symbolic top-face systems, prints the `deg_x J` sanity data, applies constant `Q*` pivots, verifies the ring-map image of every source row, checks a grading, normalizes only from a displayed `c` equation, factors one univariate base row, and treats each irreducible factor as a separate coefficient-field branch.

**DERIVED.** A branch is promoted only when the covering chain is present and every irreducible factor branch is saturated-empty. A nonunit branch without an extracted point is left `COUNTING-BOUND`, not called a survivor.

## Controls

**MEASURED.** The K=16 t=3 control is `SATURATED-EMPTY`. The charged table gives `36 -> 23` unknowns after `13` `Q*` pivots and `51 -> 37` equations; the ring map is verified on every original generator.

**MEASURED.** The charged normalization uses `q4_1`; the base row is `147*q7_1**2 - 84*q7_1 + 11`, irreducible of degree `2`, so `Q[q7_1]/(H)` covers both conjugates.

**MEASURED.** The coefficient-field pass leaves `b3,b4,a2_0` with `6` rows after `17` checked field pivots. The exact Singular script `box/k16t3-20260903/preprocessed/t3_normalized_K_std.sing` returned `SATURATED-EMPTY` with basis size `1` in `0.072` seconds.

**MEASURED.** The actual-pair control has `J=gamma` and tuple membership `FAIL`: degree/support data (2, 2, None, None, 1) is not one of the charged D<=200 rows [(24, 16, 17, 2, 5), (25, 15, 21, 2, 2), (30, 24, 25, 4, 3), (35, 20, 31, 2, 2), (35, 25, 31, 3, 2), (49, 14, 46, 4, 1), (50, 30, 47, 7, 1)].

## Support Correction

**DERIVED.** The emitted large-row systems use `ord h(sigma1) >= V2' delta1' + u' delta2'` for lower `h`, and every beta coefficient support is capped by `deg_x beta <= k+1`. This is the delta-zero correction; it prevents the old false kill where the `x^k` Jacobian coefficient was absent.

**MEASURED.** With the corrected support, the seven `(24,16;17;2;k=5)` strata are no longer the old 37-40 unknown A/B systems; their honest generic estimates are 273-276 unknowns. The six large rows range from 135 to 218 unknowns under this implementation.

## Batch Run

**MEASURED.** The batch ran sorted by corrected unknown estimate with `jobs=2`, no bigrow Singular launch, and a 600-second worker cap. `TimeLimitExceeded` is a real bounded worker result, not a content mismatch or a transcription stop.

**MEASURED.** Stage reach counts: `21/21` strata blocked before a completed symbolic build record, `0/21` reached `Q*` pivots, `0/21` reached grading, and `0/21` reached a coefficient-field branch.

**DERIVED.** Since no large stratum reached a completed corrected symbolic system, no modular or exact Gröbner verdict is promoted for those strata. Their status is `COUNTING-BOUND` with the blocker typed as corrected-emitter/preprocess wall clock.

## Strata

| row              | part        | unk | after Q | grading | H factors | verdict        | blocker                                                               |
| ---------------- | ----------- | --- | ------- | ------- | --------- | -------------- | --------------------------------------------------------------------- |
| (24,16;17;2;k=5) | 2+2+2       | 273 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |
| (24,16;17;2;k=5) | 4+1+1       | 273 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |
| (24,16;17;2;k=5) | 3+2+1       | 273 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |
| (24,16;17;2;k=5) | 3+1+1+1     | 274 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |
| (24,16;17;2;k=5) | 2+2+1+1     | 274 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |
| (24,16;17;2;k=5) | 2+1+1+1+1   | 275 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |
| (24,16;17;2;k=5) | 1+1+1+1+1+1 | 276 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |
| (25,15;21;2;k=2) | 3           | 135 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |
| (25,15;21;2;k=2) | 2+1         | 136 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |
| (25,15;21;2;k=2) | 1+1+1       | 137 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |
| (30,24;25;4;k=3) | 2           | 143 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |
| (30,24;25;4;k=3) | 1+1         | 144 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |
| (35,20;31;2;k=2) | 3           | 190 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |
| (35,20;31;2;k=2) | 2+1         | 191 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |
| (35,20;31;2;k=2) | 1+1+1       | 192 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |
| (35,25;31;3;k=2) | 2           | 148 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |
| (35,25;31;3;k=2) | 1+1         | 149 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |
| (49,14;46;4;k=1) | 3           | 188 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |
| (49,14;46;4;k=1) | 2+1         | 189 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |
| (50,30;47;7;k=1) | 3           | 217 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |
| (50,30;47;7;k=1) | 2+1         | 218 | ?/?     | ?       | -         | COUNTING-BOUND | worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded |

## Corrected Inventory

| row              | part        | K  | u | d/e | delta     | h lower | slopes | alpha dims           | beta dims   | unknowns |
| ---------------- | ----------- | -- | - | --- | --------- | ------- | ------ | -------------------- | ----------- | -------- |
| (25,15;21;2;k=2) | 3           | 5  | 3 | 3/5 | (7/5,-1)  | 9       | 0      | 12,19,20,21,22       | 15,16       | 135      |
| (25,15;21;2;k=2) | 2+1         | 5  | 3 | 3/5 | (7/5,-1)  | 9       | 1      | 12,19,20,21,22       | 15,16       | 136      |
| (25,15;21;2;k=2) | 1+1+1       | 5  | 3 | 3/5 | (7/5,-1)  | 9       | 2      | 12,19,20,21,22       | 15,16       | 137      |
| (30,24;25;4;k=3) | 2           | 6  | 2 | 4/5 | (2/5,-1)  | 9       | 0      | 11,14,17,19,22       | 14,17,19    | 143      |
| (30,24;25;4;k=3) | 1+1         | 6  | 2 | 4/5 | (2/5,-1)  | 9       | 1      | 11,14,17,19,22       | 14,17,19    | 144      |
| (35,25;31;3;k=2) | 2           | 5  | 2 | 5/7 | (3/5,-1)  | 7       | 0      | 9,11,12,13,14,15,16  | 11,12,13,14 | 148      |
| (35,25;31;3;k=2) | 1+1         | 5  | 2 | 5/7 | (3/5,-1)  | 7       | 1      | 9,11,12,13,14,15,16  | 11,12,13,14 | 149      |
| (49,14;46;4;k=1) | 3           | 7  | 3 | 2/7 | (5/7,-1)  | 13      | 0      | 16,21,22,23,24,25,26 | 17          | 188      |
| (49,14;46;4;k=1) | 2+1         | 7  | 3 | 2/7 | (5/7,-1)  | 13      | 1      | 16,21,22,23,24,25,26 | 17          | 189      |
| (35,20;31;2;k=2) | 3           | 5  | 3 | 4/7 | (10/7,-1) | 9       | 0      | 12,19,19,20,21,21,22 | 15,15,16    | 190      |
| (35,20;31;2;k=2) | 2+1         | 5  | 3 | 4/7 | (10/7,-1) | 9       | 1      | 12,19,19,20,21,21,22 | 15,15,16    | 191      |
| (35,20;31;2;k=2) | 1+1+1       | 5  | 3 | 4/7 | (10/7,-1) | 9       | 2      | 12,19,19,20,21,21,22 | 15,15,16    | 192      |
| (50,30;47;7;k=1) | 3           | 10 | 3 | 3/5 | (2/5,-1)  | 20      | 0      | 23,28,30,32,34       | 24,25       | 217      |
| (50,30;47;7;k=1) | 2+1         | 10 | 3 | 3/5 | (2/5,-1)  | 20      | 1      | 23,28,30,32,34       | 24,25       | 218      |
| (24,16;17;2;k=5) | 2+2+2       | 8  | 6 | 2/3 | (8/3,-1)  | 26      | 2      | 32,70,93             | 49          | 273      |
| (24,16;17;2;k=5) | 4+1+1       | 8  | 6 | 2/3 | (8/3,-1)  | 26      | 2      | 32,70,93             | 49          | 273      |
| (24,16;17;2;k=5) | 3+2+1       | 8  | 6 | 2/3 | (8/3,-1)  | 26      | 2      | 32,70,93             | 49          | 273      |
| (24,16;17;2;k=5) | 3+1+1+1     | 8  | 6 | 2/3 | (8/3,-1)  | 26      | 3      | 32,70,93             | 49          | 274      |
| (24,16;17;2;k=5) | 2+2+1+1     | 8  | 6 | 2/3 | (8/3,-1)  | 26      | 3      | 32,70,93             | 49          | 274      |
| (24,16;17;2;k=5) | 2+1+1+1+1   | 8  | 6 | 2/3 | (8/3,-1)  | 26      | 4      | 32,70,93             | 49          | 275      |
| (24,16;17;2;k=5) | 1+1+1+1+1+1 | 8  | 6 | 2/3 | (8/3,-1)  | 26      | 5      | 32,70,93             | 49          | 276      |

## Stage Notes

**MEASURED.** For every timed-out large stratum, `deg_x J` is recorded as not reached because the exact corrected h-adic symbolic build did not finish. The driver is written to print `deg_x_J_gate` once `eqs_from_by_power` completes; none of the 21 large/unfinished records reached that point in this bounded run.

**MEASURED.** No `Q*` pivot table was produced for the 21 target strata. The only pivot tables present in this lane are the K=16 control references and any partial files from interrupted dry runs are not used as certificates.

**DERIVED.** The absence of a completed build is not evidence of nonemptiness. It only says the triangular/weighted-torus/field-normalisation preprocessing did not get an exact object to act on within the lane bound.


## Row Verdicts

| row   | verdict        | empty/total | open strata                                                                                                                                                                          |
| ----- | -------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 24_16 | COUNTING-BOUND | 0/7         | 2+2+2:worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded; 4+1+1:worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded; 3+2+1:worker blocked: Time |
| 25_15 | COUNTING-BOUND | 0/3         | 3:worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded; 2+1:worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded; 1+1+1:worker blocked: TimeLimitE |
| 30_24 | COUNTING-BOUND | 0/2         | 2:worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded; 1+1:worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded                                   |
| 35_20 | COUNTING-BOUND | 0/3         | 3:worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded; 2+1:worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded; 1+1+1:worker blocked: TimeLimitE |
| 35_25 | COUNTING-BOUND | 0/2         | 2:worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded; 1+1:worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded                                   |
| 49_14 | COUNTING-BOUND | 0/2         | 3:worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded; 2+1:worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded                                   |
| 50_30 | COUNTING-BOUND | 0/2         | 3:worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded; 2+1:worker blocked: TimeLimitExceeded: stratum wall-clock budget exceeded                                   |

## Tally

**MEASURED.** `{"rows_open_or_counting_bound": 7, "rows_saturated_empty": 0, "strata_open_or_counting_bound": 21, "strata_saturated_empty": 0, "strata_total": 21}`

## FALLACY-v2

**DERIVED.** The report separates source-safe partition coverage from actual attainment; a representative is required before any nonunit branch is called `SURVIVES`.

**MEASURED.** Saturation is represented by `T*(c*Omega)-1` or its mapped image, with empty/nonempty controls in each emitted Singular ring.

**DERIVED.** No new exit-price assertion is made, so no `charge_basis` line is due.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line, including its terminating newline.
- Body bytes: `13490`.
- Body SHA-256: `3f994067f8149636fc81e57e98122261dc1435d4c0ac77f266893e58646c5273`.
