# V82P4E extended CURRENT launch

Launched 2026-08-26 08:17:26Z on two registered Amazon EC2 hosts after the four
original V82P4 lanes ended at the preregistered four-hour outer timeout.  Those
`rc=124` endpoints are duration/deployment negatives only: each reached typed
previous/pole replay, but none emitted a CURRENT table.

The extended lanes use the unchanged source archive
`e03277a2a2f1aaf8d599cd43423527e85c39a3b2ba07e2c8d4350f4169c3c03f`,
an 8 GiB virtual-memory cap per lane, and a 43,200-second timeout.

## Box03

- host: `98.80.65.144` / `ip-172-30-0-249`
- run root: `/home/ubuntu/runs/td6_v82p4e_dead_current_box03_20260826T081726Z`
- d10 wrapper PID: `185083`; Python PID at startup: `185101`
- d15 wrapper PID: `185089`; Python PID at startup: `185102`
- tags: `td6_v82p4_extended_box03_d10_20260826T081726Z`,
  `td6_v82p4_extended_box03_d15_20260826T081726Z`

## r6d

- host: `100.26.198.153` / `ip-172-30-0-45`
- run root: `/home/ubuntu/runs/td6_v82p4e_dead_current_r6d_20260826T081726Z`
- d10 wrapper PID: `250367`; Python PID at startup: `250385`
- d15 wrapper PID: `250372`; Python PID at startup: `250386`
- tags: `td6_v82p4_extended_r6d_d10_20260826T081726Z`,
  `td6_v82p4_extended_r6d_d15_20260826T081726Z`

All four AWS/platform/source-hash preflights passed.  This registration makes no
mathematical claim until both hosts close, exact tables agree, and the result is
composed with the reviewed 24-dimensional Stage-A kernel on the same principal
open.
