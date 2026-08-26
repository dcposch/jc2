# AWS v2 registration

Source archive:

```text
b2e29088ff63e171c91cfc7a52d0bfcbe7b87fc74869cb142edd092948286882
```

- A: tag
  `max12_912_order3_d1_double_root_control2_rees_v2_20260826T005028Z_box02_A`,
  host Box02 `34.203.207.55`, job of the same tag under
  `/home/ubuntu/jobs/`, blocked PID `262230`, factored/saturation encoding.
- B: tag
  `max12_912_order3_d1_double_root_control2_rees_v2_20260826T005028Z_r6d_B`,
  host r6d `100.26.198.153`, job of the same tag under `/home/ubuntu/jobs/`,
  blocked PID `192593`, expanded/inverse-elimination encoding.

Each job permits one compiler and one Singular process at nice 10.  Compiler
cap: 64 GiB / 3600 s.  Solver cap: 256 GiB / 21600 s.  Both workers were
recorded in `WAITING_COMPILE` before a GO sentinel existed.  Timing telemetry
goes to `singular.time`; `singular.stderr` is reserved for the CAS and must be
empty.

