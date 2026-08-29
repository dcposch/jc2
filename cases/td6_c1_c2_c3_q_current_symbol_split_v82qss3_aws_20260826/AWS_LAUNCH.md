# V82QSS3 dual-AWS launch

Source archive SHA-256:
`8b896294909a488d2271e4aa401316e2a3c7ed9474b79d3064d84428c857f606`.
The complete `SOURCE.sha256` and `V82QSS_SOURCE.sha256` closures passed on both
hosts.  Each lane has a 4 GiB virtual-memory cap and 10,800-second timeout.

## Box03

- host/IP/hostname: Box03 / `98.80.65.144` / `ip-172-30-0-249`
- run root: `/home/ubuntu/runs/td6_v82qss3_symbol_box03_20260826T094501Z`
- fleet supervisor PID: `196974`
- q11 wrapper/Python: `196979` / `196999`
- q16 wrapper/Python: `196987` / `197001`
- tags: `td6_v82qss3_symbol_box03_q11_20260826T094501Z`,
  `td6_v82qss3_symbol_box03_q16_20260826T094501Z`

## r6d

- host/IP/hostname: r6d / `100.26.198.153` / `ip-172-30-0-45`
- run root: `/home/ubuntu/runs/td6_v82qss3_symbol_r6d_20260826T094501Z`
- fleet supervisor PID: `261469`
- q11 wrapper/Python: `261474` / `261494`
- q16 wrapper/Python: `261482` / `261496`
- tags: `td6_v82qss3_symbol_r6d_q11_20260826T094501Z`,
  `td6_v82qss3_symbol_r6d_q16_20260826T094501Z`

Launched at `2026-08-26T09:45:34Z` after live headroom checks.  The first live
marker on every lane is `empty_map_unit_denominator_positive_control=true`;
all four then entered the exact transport.  This launch is provisional pending
four rc=0 endpoints and cross-host reconciliation.
