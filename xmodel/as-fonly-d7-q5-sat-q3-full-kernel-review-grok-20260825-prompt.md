# Hostile review prompt: AS F-only D7 Q3 whole-kernel producer

Audit `xmodel/as-fonly-d7-q5-sat-q3-full-kernel-producer-20260825.md` and the complete case `cases/as_fonly_d7_q5_sat_q3_full_kernel_20260825/` adversarially and independently.

Required checks:

1. Reconstruct the transitive source provenance, including the pinned Q4 parent SHA and all model inputs.  Check determinant orientation and every exact division before reduction modulo 3.
2. Verify that the row inventory is exactly four degree-three `/81` rows plus 63 degree-7-through-12 `/243` terminal rows, and that inherited Q4 rows are replayed.
3. Check that the quadratic design really proves global affineness on each full finite coefficient cube; independently recompute matrix/RHS, ranks, kernels, and displayed particulars.
4. Reconstruct the literal integer maps at all three displayed solutions and verify all claimed divisibilities and valuation-by-degree tables.
5. Charge the zero-`H4,J4` omission control, especially that base0513 may pass while the other two fail.
6. Check the typed consequence that degree-one/two valuation three requires earlier order-27 pieces before any order-81-only Q2/Q1 continuation.
7. Enforce scope: three predecessor points/full displayed Q4 fibres only; no whole-Q5, complete-mod-243, all-depth, counterexample, or JC2 inference.

Return `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `BLOCKED`, separating source/compiler correctness from replay/custody correctness.  If replay is run, it must be on AWS and its host, command, source hashes, stdout/stderr hashes, exit status, time, and peak RSS must be recorded.
