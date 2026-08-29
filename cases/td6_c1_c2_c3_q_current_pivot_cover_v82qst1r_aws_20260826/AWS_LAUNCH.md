# V82QST1R AWS launch ledger

- UTC stamp: `20260826T085656Z`
- archive SHA256: `3e2b618084ea87f965642a930d24f25f2754bbcad3e182c9d608715d8d16c6b8`
- dual-host closure and Python-AST smoke: PASS.
- each host runs all four cells: `reverse:q2`, `sparse:q2`, `reverse:q10`,
  `sparse:q10`.
- per-lane cap: 2 GiB virtual memory, 7200 seconds.

Box03 (`98.80.65.144`):

- root: `/home/ubuntu/runs/td6_v82qst1r_current_box03_20260826T085656Z`
- supervisor PID `189276`
- wrapper PIDs: `189280`, `189288`, `189298`, `189308` in the cell order
  above.

r6d (`100.26.198.153`):

- root: `/home/ubuntu/runs/td6_v82qst1r_current_r6d_20260826T085656Z`
- supervisor PID `254495`
- wrapper PIDs: `254499`, `254507`, `254517`, `254527` in the cell order
  above.

All eight lanes passed platform, archive, source-closure, policy, and q-axis
preflights and entered exact transport.  Interpretation remains fail closed
until terminal status, per-host equality, and exact denominator/factor-table
comparison against ascending Gate 0.

