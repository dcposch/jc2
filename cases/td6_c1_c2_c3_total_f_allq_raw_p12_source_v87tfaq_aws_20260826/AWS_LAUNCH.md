# V87TFAQ authoritative V1 dual-host launch record

Date: 2026-08-26

Authoritative source archive SHA-256:
`e80b1cba7b4a1749c7f12ecd7b6a8d9418e73b6b01d8f82081dbb76f113669d3`.

Frozen V87 client SHA-256:
`7c0890abbce996a221f9389372fa3705742d6ecd72531891bfeb5dfc2f1b9463`.

Frozen V86 parent SHA-256:
`5b160a2bd18434e6142c33be6775e0c212c22ebc67a52d08b246dd0223decd7c`.

Frozen V85 parent SHA-256:
`ab9753073d694242d4359dc1edc86774724f62d28d15b7c671ba0b796262100e`.

Frozen original compiler SHA-256:
`a4ccd5d81101fdb82ed2f61571c258e2054961d161f4a98461b8f8614d3fd85e`.

Frozen V82QST3 certificate SHA-256:
`8e892ffa914e0f93969abb9722f926486843f59cf77f5861c5ce3d3438281482`.

## Box02

- endpoint: `34.203.207.55`;
- run root:
  `/home/ubuntu/runs/td6_v87tfaq_total_f_allq_v1_box02_20260826T150610Z`;
- fleet supervisor PID: `283714`;
- lane supervisor PID: `283718`;
- registered start: `2026-08-26T15:06:43Z`;
- finish: `2026-08-26T15:26:09Z`.

## r6d

- endpoint: `100.26.198.153`;
- run root:
  `/home/ubuntu/runs/td6_v87tfaq_total_f_allq_v1_r6d_20260826T150610Z`;
- fleet supervisor PID: `291576`;
- lane supervisor PID: `291580`;
- registered start: `2026-08-26T15:06:43Z`;
- finish: `2026-08-26T15:26:11Z`.

Each lane used the exact 22-jet scope `q2..q14,q16..q24`, explicitly fixed
`q15=0`, used `TD6_PIVOT_POLICY=ascending` and
`TD6_PIVOT_SCOPE=all-staged`, a 256 GiB virtual-memory cap, and an
86,400-second timeout. Each returned `rc=0`, used zero swap, and emitted
byte-identical mathematical stdout and output files.

The archive builds the full q-dependent transport once, checks all 44
single-path omissions against raw FIRST, reproduces all 39 all-q-zero V85
source hashes, replays the frozen V82QST3 certificate, and audits the exact
augmentation-ideal and denominator-cleared identities.
