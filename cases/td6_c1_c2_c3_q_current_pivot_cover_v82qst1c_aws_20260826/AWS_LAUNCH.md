# V82QST1C dual-AWS launch

Source archive SHA-256:
`f748235a17115e8aad66854d76944d1ed26801b7294a3c258af42b9702af2065`.
Both hosts passed the complete source and nested-review-pin closure.  q2 and
q10 each have a 2 GiB virtual-memory cap and 7,200-second timeout.

## Box03

- host/IP: Box03 / `98.80.65.144`
- run root: `/home/ubuntu/runs/td6_v82qst1c_current_box03_20260826T100043Z`
- supervisor PID: `199537`
- q2 wrapper/Python: `199542` / `199564`
- q10 wrapper/Python: `199550` / `199566`
- tags: `td6_v82qst1c_current_box03_reverse_q2_20260826T100043Z`,
  `td6_v82qst1c_current_box03_reverse_q10_20260826T100043Z`

## r6d

- host/IP: r6d / `100.26.198.153`
- run root: `/home/ubuntu/runs/td6_v82qst1c_current_r6d_20260826T100043Z`
- supervisor PID: `263523`
- q2 wrapper/Python: `263528` / `263550`
- q10 wrapper/Python: `263536` / `263552`
- tags: `td6_v82qst1c_current_r6d_reverse_q2_20260826T100043Z`,
  `td6_v82qst1c_current_r6d_reverse_q10_20260826T100043Z`

Launched at `2026-08-26T10:01:19Z` and `10:01:20Z`.  Every lane prints the
pre-computation assertions
`qst_pivot_scope=current-only`,
`qst_FIRST_and_PREVIOUS_POLE_policy=ascending`, and
`qst_CURRENT_policy=reverse`.  This is a Gate-1 alternate-minor diagnostic;
no raw divisor or cover conclusion is licensed before the four endpoints and
exact table comparison.
