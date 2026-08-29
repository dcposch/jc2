# V82QST1 AWS launch ledger

- UTC stamp: `20260826T085035Z`
- archive SHA256: `f03dba730b2287eb22675f9ea8fad30420a65319fa967db7f871b6771483172f`
- closure/startup smoke: PASS on Box03 and r6d; every `SOURCE.sha256`
  and `V82QST1_SOURCE.sha256` entry verified.
- per-lane cap: 2 GiB virtual memory, 7200 seconds.

Box03 (`98.80.65.144`):

- root: `/home/ubuntu/runs/td6_v82qst1_current_box03_20260826T085035Z`
- supervisor PID `188677`
- `reverse:q2` wrapper PID `188681`
- `sparse:q10` wrapper PID `188688`

r6d (`100.26.198.153`):

- root: `/home/ubuntu/runs/td6_v82qst1_current_r6d_20260826T085035Z`
- supervisor PID `253898`
- `sparse:q2` wrapper PID `253902`
- `reverse:q10` wrapper PID `253909`

The sparse cells both ended `rc=1` at the same ascending-only affine form
back-substitution assertion before any CURRENT denominator computation.  They
are deployment-negative only.  The reverse cells are retained under the same
firewall pending terminal status.  V82QST1R is the nonmutating source-honest
pivot-insertion-DAG repair.

