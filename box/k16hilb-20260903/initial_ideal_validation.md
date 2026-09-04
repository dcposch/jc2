# Prompt-order initial-ideal extraction validation

`extract_initial_ideal.py` was run on the seven completed, clean outputs
below.  It checked the printed `META` and `JOB_DONE` records, exponent
arity/order, contiguous indices, cardinality against `FULL_GB_SIZE`, pairwise
divisibility-antichain minimality, and every printed `FULL_PURE_POWER` minimum.
All checks passed.

| output | exponent record | generators | least pure powers in `(b4,q...,b3)` order | TSV |
|---|---:|---:|---|---|
| `t2_split_exact_b0_full.out` | `INITIAL_EXP` | 3 | `b4^6`; no `b3` power | `t2_split_exact_b0_full_initial_ideal.tsv` |
| `t2_split_exact_b1_full.out` | `INITIAL_EXP` | 4 | `b4^6, b3^3` | `t2_split_exact_b1_full_initial_ideal.tsv` |
| `t3_exact_full.out` | indexed `LM` fallback | 20 | `b4^8, q2_0^6, b3^4` | `t3_exact_full_initial_ideal.tsv` |
| `t4_exact_full.out` | indexed `LM` fallback | 81 | `b4^10, q2_0^7, q3_0^6, b3^5` | `t4_exact_full_initial_ideal.tsv` |
| `t5_mod_p1009_b0_full.out` | `INITIAL_EXP` (cross-checked against `LM`) | 340 | `b4^12, q2_0^8, q3_0^7, q4_0^7, b3^6` | `t5_mod_p1009_b0_full_initial_ideal.tsv` |
| `t6_mod_p1009_b0_full.out` | `INITIAL_EXP` (cross-checked against `LM`) | 1391 | `b4^14, q2_0^10, q3_0^8, q4_0^8, q5_0^7, b3^6` | `t6_mod_p1009_b0_full_initial_ideal.tsv` |
| `t7_mod_p1009_b0_full.out` | `INITIAL_EXP` (cross-checked against `LM`) | 5830 | `b4^16, q2_0^11, q3_0^9, q4_0^8, q5_0^8, q6_0^8, b3^7` | `t7_mod_p1009_b0_full_initial_ideal.tsv` |

The clean exact `t=3,4` jobs predate the `INITIAL_EXP` print loop.  Their
`LM[i]=...` records are still indexed and complete, so the parser strictly
reconstructs exponent vectors from those monomials instead of treating absent
records as zeros.

The exact antichain check now intersects cumulative coordinate-threshold
bitsets, with the smallest candidate population first; it does not trust the
`minbase` label.  On the 5,830-generator `t=7` output, complete parsing,
cross-checking, antichain validation, pure-power validation, and TSV emission
took 0.75 s wall / 0.67 s user with 24,504 KB peak RSS.  The timing record is
`t7_mod_p1009_b0_full_initial_ideal_validation.resource`; stderr is empty and
the recorded exit status is zero.  A regression replay of the prior six cases
took 0.20 s wall and reproduced all six existing TSVs byte-for-byte.
