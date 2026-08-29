# V86TFQ2 authoritative V3 dual-host launch record

Date: 2026-08-26

Authoritative source archive SHA-256:
`a7e3681db04b927458be08106bcf9756ce50ea56ff176c80e4b146b4eaf0d508`.

Frozen V86 client SHA-256:
`5b160a2bd18434e6142c33be6775e0c212c22ebc67a52d08b246dd0223decd7c`.

Frozen V85 parent SHA-256:
`ab9753073d694242d4359dc1edc86774724f62d28d15b7c671ba0b796262100e`.

Frozen original compiler SHA-256:
`a4ccd5d81101fdb82ed2f61571c258e2054961d161f4a98461b8f8614d3fd85e`.

Frozen V82QST3 certificate SHA-256:
`8e892ffa914e0f93969abb9722f926486843f59cf77f5861c5ce3d3438281482`.

## Box03

- endpoint: `98.80.65.144`;
- run root:
  `/home/ubuntu/runs/td6_v86tfq2_total_f_q2_v3_box03_20260826T143102Z`;
- fleet supervisor PID: `230192`;
- lane supervisor PID: `230196`;
- registered start: `2026-08-26T14:31:08Z`;
- finish: `2026-08-26T14:48:32Z`.

## r6d

- endpoint: `100.26.198.153`;
- run root:
  `/home/ubuntu/runs/td6_v86tfq2_total_f_q2_v3_r6d_20260826T143102Z`;
- fleet supervisor PID: `287598`;
- lane supervisor PID: `287602`;
- registered start: `2026-08-26T14:31:14Z`;
- finish: `2026-08-26T14:48:32Z`.

Each lane used `TD6_Q_EXPONENT=2`, `TD6_PIVOT_POLICY=ascending`,
`TD6_PIVOT_SCOPE=all-staged`, a 32 GiB virtual-memory cap, and a 21,600-second
timeout.  Each returned `rc=0`, used zero swap, and emitted byte-identical
mathematical stdout and output files.

The authoritative V3 archive expands P12 once, applies path-omission controls
to raw FIRST, checks all 39 beta-zero source hashes against the frozen V85
inventory, and literally replays the special certificate.  The pre-result V1
failure and V2 redundant replay are excluded exactly as recorded in
`DEPLOYMENT_ERRATUM.md`.
