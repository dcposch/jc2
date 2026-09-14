**8. Reissued finite schedule and decision table.** All36 main circuit attempts reached complete emission and `ALL_ROWS_PARSED`. None reached a complete accepted result/control block. Each cell is **status+rc; recorded elapsed seconds; RSS GiB**: T=COMPUTE-BOUND OPEN, M=MEMORY-BOUND OPEN. Both clients' times include emitter/build overhead; build times are separately retained. A dash means RSS was not captured. An inequality is the observed `/proc` VmHWM through the last sample, rounded downward, hence only a lower bound on final peak RSS. The 16 GiB address-space caps are not substituted for RSS.

| Stage | 99 delta2 | 99 delta5/2 | D108 mean-zero restriction | D108 repaired free mean |
|---:|---|---|---|---|
| 0 | T1; 601.6; — | T1; 601.2; — | M14; 587.8; — | T1; 600.8; — |
| 1 | T1; 601.5; — | T1; 601.1; — | M14; 605.4; — | T1; 600.8; — |
| 2 | T1; 601.4; — | T1; 601.1; — | M14; 843.7; — | T1; 600.8; — |
| 3 | T1; 601.4; — | T1; 601.1; — | M14; 844.1; — | T1; 600.7; — |
| 4 | T1; 601.3; — | T1; 601.0; — | M14; 848.4; — | T1; 600.7; — |
| 5 | T1; 601.4; — | T1; 601.1; — | T1; 900.8; — | T1; 600.7; — |
| 6 | T1; 601.3; ≥11.16 | T1; 601.1; ≥11.09 | T1; 900.8; ≥15.01 | T1; 600.7; ≥10.06 |
| 7 | T1; 601.3; ≥11.16 | T1; 601.0; ≥11.12 | T1; 900.7; ≥14.87 | T1; 600.6; ≥10.17 |
| 8 | T1; 601.3; ≥11.21 | T1; 601.1; ≥11.11 | T1; 1800.9; — | T1; 600.6; ≥10.18 |

Every stage's script, input, emitter, source-map, ordered-ring and output SHA-256 is bound in [99 custody](/home/ubuntu/jc2/box/char-degree-20260905/resume-r2/audit-99.json) and [D108 custody](/home/ubuntu/jc2/box/char-degree-20260905/resume-r2/audit-d108-custody.json). These retain exact row counts, localizer strings, ring order and target checks. Ring/block sizes are: 99 delta2: 2537–2912 generators, 1280–1389 characteristic Q rows; 99 delta5/2: 2535–2910 generators, 1280–1389 characteristic Q rows; 108 mean zero: 2495–2906 generators, 1144–1256 characteristic Q rows; 108 free mean: 2520–2931 generators, 1144–1256 characteristic Q rows. A zero residual-source-row count after graph elimination does not mean original source conditions were dropped; their images and rational pivots are separately audited.

Selected stage8 alternatives also remained OPEN. The 99 delta2 `slimgb` run ended rc1 at1200.467s; the delta5/2 active-front run ended rc1 at1801.169s; the delta5/2 remainder run failed for memory at1215.298s. Their peak RSS was not captured. D108 `meanfree_jet0_stage8_slimgb`: rc1, 1200.517s, observed HWM ≥15.4 GiB, OPEN; `meanfree_stage8_slimgb`: rc1, 1200.417s, not captured, OPEN. No selected run supplies a branch kill or proper ideal.

The final historical inventory is [status-catalog-final.json](/home/ubuntu/jc2/box/char-degree-20260905/resume-r2/status-catalog-final.json). It includes the older normalized/active/construction attempts and quarantined startup failures. Stale `RUNNING`, `EXPANDING_FULL_CHARACTERISTIC`, or `EMITTED_NOT_DECIDED` metadata is reconciled against the final process inventory; it proves no solver completion. Some legacy `CAS_ERROR_OPEN` records are memory failures during construction, not parser failures. No control result or administrative `CLOSED` receipt is promoted to a production verdict.

Fresh emitter and all-production-ring inverse controls pass. The independent [final strict reader](/home/ubuntu/jc2/box/char-degree-20260905/resume-r2/strict-acceptance-production-final.json) binds39 actual production outputs: **34 time-bound,5 memory-bound, zero complete clean unit/proper candidates**. Its controls reject incomplete markers, wrong control vectors, and a real malformed Singular script that exits rc0. Production inline controls never completed after the bounded Gröbner calls, so acceptance stops at OPEN.

**Per-client verdict:** (99,66) delta2 — **compute-bound OPEN**; (99,66) delta5/2 — **compute-bound OPEN**; D108 delta3 — **compute-bound OPEN**, including the coverage-repaired free-mean chart. No independent unit replay or coordinate extraction was triggered because no production unit or proper candidate existed. If a complete validated ideal had been proper, the charged typing would be **PROPER — EXACT-Q-PROPER-AUGMENTED-IDEAL: an existential nondegenerate necessary-chart survivor over Qbar**, even without extracted coordinates. That event did not occur here.

