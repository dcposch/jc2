# V82QS AWS launch ledger

Launched: 2026-08-26 06:57:12Z

Source archive SHA-256:
`7c6e648e72eafde683cd64cbb9354d2278e4cfeb11d8c4a9d00d9fd4224e8bb6`.

## Box03

- host: `98.80.65.144` / hostname `ip-172-30-0-249`
- run root:
  `/home/ubuntu/runs/td6_v82qs_current_box03_20260826T065557Z`
- supervisor PID: `174312`
- axes: `q2 q3 q4 q5 q6 q7 q8 q9 q10 q11 q12`
- lane PIDs:
  `174317 174324 174335 174345 174354 174365 174375 174385 174395 174405 174415`
- tag pattern: `td6_v82qs_current_box03_qN_20260826T065557Z`

## r6d

- host: `100.26.198.153` / hostname `ip-172-30-0-45`
- run root:
  `/home/ubuntu/runs/td6_v82qs_current_r6d_20260826T065557Z`
- supervisor PID: `240790`
- axes: `q13 q14 q16 q17 q18 q19 q20 q21 q22 q23 q24`
- lane PIDs:
  `240795 240802 240813 240823 240833 240843 240853 240863 240873 240882 240893`
- tag pattern: `td6_v82qs_current_r6d_qN_20260826T065557Z`

Each lane has cap `4194304` KiB and timeout `21600` seconds.  Initial source
preflights passed and all 22 lanes entered exact transport.  Both original
V82Q monoliths remain live as aggregate authority.

## Exact union-parser preflight

The prospective 24-axis union/reconciliation script has SHA-256
`608f6c1ddd1a04d1a356ef62a3c1f8d7889bd92758584e9a22e047ead2aa6243`.
Its exact E(C,V,U) scalar parser, including rational coefficients and powers,
passed independently on both AWS hosts under a 1 GiB cap:

- Box03: `/home/ubuntu/runs/td6_v82qr_parser_preflight_box03_20260826T0705Z`
- r6d: `/home/ubuntu/runs/td6_v82qr_parser_preflight_r6d_20260826T0705Z`

Both returned `rc=0` and the standalone verdict
`TD6-V82QR-EXACT-PARSER-PREFLIGHT PASS`.  This is a software preflight, not
current-stage evidence.
