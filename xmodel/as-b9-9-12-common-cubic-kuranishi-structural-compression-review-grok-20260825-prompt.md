# Hostile review request: exact B9 Kuranishi structural compression

Audit, without mutating producer bytes, the report
`xmodel/as-b9-9-12-common-cubic-kuranishi-structural-compression-producer-20260825.md`
and case
`cases/as_b9_9_12_common_cubic_kuranishi_solver_20260825/`.

Charge the following separately:

1. The reviewed parent really licenses one exact map `K:F3^95->F3^176` at
   the displayed one-parent scope.
2. `analyze_structural_span.py` groups only byte-identical recursive DAG
   expressions, computes the F3 row rank correctly, selects original rows,
   and emits relations that reconstruct all 176 coordinates from 111.
3. Box02/Box03 certificates are byte-identical and the Box02 missing-PID
   custody defect is non-mathematical.
4. `analyze_structural_span_constants.py` evaluates every input-independent
   operation with the correct F3/mod-531441 semantics; group 215 is exactly
   zero; deleting row 96 and obtaining rank 110 is sound.
5. Verify enough relation rows directly from the gzip certificates to exclude
   an indexing/transposition error, and check that `K=0` iff basis110=0`.
6. Audit the exact-unused-input claim and the explicit overapproximation
   firewall on used syntactic supports.
7. Enforce scope: no zero-locus verdict, no lift/all-depth/counterexample/
   maximum-12/JC2 claim; sampled rank 9 and solver failures are diagnostics.

Return `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `REFUTED`, with exact defects
and the strongest licensed theorem.  Do not run local CAS/solver/Python replay;
any substantive independent replay must be staged on AWS under the campaign
resource policy.
