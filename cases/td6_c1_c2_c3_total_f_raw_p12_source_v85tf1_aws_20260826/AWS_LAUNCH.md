# V85TF1 dual-host launch record

Date: 2026-08-26

Authoritative source archive SHA-256:
`18cd49f51cc925bab52a37315eb1cce72b3f34a776e122aa7ee2a67d44d82d21`.

Frozen wrapper SHA-256:
`ab9753073d694242d4359dc1edc86774724f62d28d15b7c671ba0b796262100e`.

Frozen original compiler SHA-256:
`a4ccd5d81101fdb82ed2f61571c258e2054961d161f4a98461b8f8614d3fd85e`.

Frozen V82QST3 certificate SHA-256:
`8e892ffa914e0f93969abb9722f926486843f59cf77f5861c5ce3d3438281482`.

## Box02 q2

- endpoint: `34.203.207.55`;
- run root:
  `/home/ubuntu/runs/td6_v85tf1_total_f_v4_box02_20260826T1243Z`;
- fleet supervisor PID: `279875`;
- lane supervisor PID: `279879`;
- registered start: `2026-08-26T12:38:09Z`;
- finish: `2026-08-26T12:54:40Z`.

## Box03 q10

- endpoint: `98.80.65.144`;
- run root:
  `/home/ubuntu/runs/td6_v85tf1_total_f_v4_box03_20260826T1243Z`;
- fleet supervisor PID: `217965`;
- lane supervisor PID: `217969`;
- registered start: `2026-08-26T12:38:10Z`;
- finish: `2026-08-26T12:54:40Z`.

Each lane used `TD6_PIVOT_POLICY=ascending`,
`TD6_PIVOT_SCOPE=all-staged`, a 16 GiB virtual-memory cap, and a 14,400-second
timeout.  Each returned `rc=0` with the V85TF1 PASS banner, used zero swap,
and emitted the same cleared-`h` and source-inventory hashes recorded in
`RESULT.md`.

Archives from the three earlier deployment generations are excluded as
specified in `DEPLOYMENT_ERRATUM.md`.  The authoritative v4 archive includes
the repaired q-jet compiler-state restoration and is the only archive used
for this result.
