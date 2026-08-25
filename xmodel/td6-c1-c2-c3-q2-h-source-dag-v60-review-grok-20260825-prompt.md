# Hostile no-shell review: TD6 H-stratum source DAG V60

Act as an independent hostile algebraic/source-fidelity referee.  Review the
frozen V60 claim, not the wider campaign.  You may use only read/search/glob
operations.  Do **not** use Bash, Python, CAS, shell commands, web access, or
network access.  Do not edit any repository file except the single report
named below, and do not edit this prompt.

Read these files completely:

- `xmodel/td6-c1-c2-c3-q2-h-source-dag-v60-aws-20260825.md`
- `cases/td6_c1_c2_c3_q2_h_source_dag_v60_aws_20260825/README.md`
- `cases/td6_c1_c2_c3_q2_h_source_dag_v60_aws_20260825/verify.py`
- `cases/td6_c1_c2_c3_q2_h_source_dag_v60_aws_20260825/MANIFEST.sha256`
- `cases/td6_c1_c2_c3_q2_h_source_dag_v60_aws_20260825/FREEZE.sha256`
- `cases/td6_c1_c2_c3_q2_h_source_dag_v60_aws_20260825/aws_run/v60.stdout`
- `cases/td6_c1_c2_c3_q2_h_source_dag_v60_aws_20260825/aws_run/v60.stderr`
- `cases/td6_c1_c2_c3_q2_h_source_dag_v60_aws_20260825/aws_run/artifacts/N13_PROOF_DAG.txt`
- `cases/td6_c1_c2_c3_q2_h_source_dag_v60_aws_20260825/aws_run/artifacts/DAG_LEAF_DENOMINATORS.tsv`

The exact source archive has been expanded read-only outside the repository
at `/tmp/jc2-td6-v60-review.ePmK88/td6-aws-handoff-20260825-v59/`.
Read the V60 source
`jc2/cases/td6_c1_c2_c3_q2_full_source_glue_raw_edge_dag_v60_20260825/replay.py`
there in full, together with every directly imported or dynamically executed
source/runbook/hash file needed to audit its dependency chain.  Follow only
dependencies needed for this claim; do not substitute old reports for the
actual source.

Attack every item below.

1. Verify that the raw center is source-typed as `H=C-3*U^2=0`, hence
   `C=3*U^2`, and that no stronger center or output equation slipped in.
2. Verify that arbitrary-degree original rows are really preserved and that
   current row 13 is traced through exactly previous rows `('X-1',0)` and
   `('X-1',14)`, then through genuine original first rows.  Distinguish an
   algebraically checked edge relation from a digest or marker assertion.
3. Verify that P12 is the genuine direct-first object: 2,885 terms, 28
   nonzero original rows, 1,640 multiplier terms, exact agreement of the old
   tail and multiplier objects, and no giant nested-multiplier shortcut.
4. Check the exact P12/N13 composition and residual `-k/50`.  Audit how `k`
   is typed/nonzero and whether it contributes an unreported localization.
5. Check the one-required-edge omission control and the P12-without-N13
   control.  Say whether each attacks the claimed dependency rather than only
   a wrapper.
6. Audit all 16 denominator-ledger lines.  Check coefficient and termwise
   denominators, factor normalization, and whether the radical is exactly
   `{U,V,P3,QH}`, where
   `P3=V^4-32*V^2*U^3+128*U^6` and
   `QH=V^4+8*V^2*U^3-64*U^6`.
7. Verify specifically that QH occurs in the row-13-to-first multipliers and
   the previous-row-14-to-first edge.  Look for cancellation, hidden powers,
   missing factors, or a reason QH could be removed.
8. Check the logical conclusion.  At most it may be an exact fraction-field
   obstruction on `H=0,D(U*V*P3*QH)`.  It is not a whole-H divisor theorem,
   not a cover, not fixed-A3 globally, and not TD6/JC2.
9. Cross-check manifest/freeze/path/hash strings and endpoint status as far
   as a no-shell session permits.  Explicitly disclose which byte hashes you
   could not recompute.  Do not treat custody markers as proofs of algebra.

Write exactly
`xmodel/td6-c1-c2-c3-q2-h-source-dag-v60-review-grok-20260825.md`.
Give a separate finding for each numbered item, the smallest exact repair for
every defect, and a precise survival statement.  End with exactly one verdict
token on its own line: `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, `REFUTED`, or
`NOT_PROVED`.
