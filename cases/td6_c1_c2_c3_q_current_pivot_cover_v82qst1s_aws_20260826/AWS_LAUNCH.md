# V82QST1S AWS launch ledger

- UTC stamp: `20260826T090357Z`
- archive SHA256: `7db94918342d4bfa0363cbe57a40a2ebdc9533124012bcb0a90051bb7605445f`
- dual-host full source, review-pin, shell, and Python-AST preflight: PASS.
- cells on each host: `reverse:q2`, `sparse:q2`, `reverse:q10`,
  `sparse:q10`.
- per-cell cap: 2 GiB virtual memory, 7200 seconds.

Box03 (`98.80.65.144`):

- root: `/home/ubuntu/runs/td6_v82qst1s_current_box03_20260826T090357Z`
- supervisor PID `190692`
- wrapper PIDs `190696`, `190704`, `190714`, `190724` in the cell order
  above.

r6d (`100.26.198.153`):

- root: `/home/ubuntu/runs/td6_v82qst1s_current_r6d_20260826T090357Z`
- supervisor PID `255956`
- wrapper PIDs `255960`, `255968`, `255978`, `255987` in the cell order
  above.

All eight lanes passed immutable custody/platform preflights and entered the
reviewed ascending transport.  The only alternative pivot boundary is the
staged EJet solver.  No interpretation before terminal dual-host agreement
and factor-ledger comparison with Gate 0.

