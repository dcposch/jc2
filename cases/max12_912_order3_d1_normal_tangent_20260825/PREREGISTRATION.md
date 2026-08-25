# D1 common-cubic normal-deformation reconnaissance

Date: 2026-08-25

All substantive source reconstruction, sparse expansion, factorization, and
standard-basis work in this directory is AWS-only.  Local execution is
forbidden; the Mac may edit, hash, inspect already emitted text, and SSH.

Registered jobs:

- Box03 `98.80.65.144`,
  `/home/ubuntu/jobs/max12_912_order3_d1_normal_tangent_20260825T220700Z_box03`,
  Python normal Taylor extraction, PID `113593`, `timeout 1800`, `nice -n 10`.
- Box03 `98.80.65.144`,
  `/home/ubuntu/jobs/max12_912_order3_d1_composition_jacobian_20260825T222000Z_box03`,
  Python reconstruction plus Singular factorization, `timeout 1800`,
  `nice -n 10` for each stage.
- Box03 `98.80.65.144`,
  `/home/ubuntu/jobs/max12_912_order3_d1_weight20_20260825T223500Z_box03`,
  exact weight-20 extraction, `timeout 1800`, `nice -n 10`.
- Box03 `98.80.65.144`,
  `/home/ubuntu/jobs/max12_912_order3_d1_general_leading_20260825T225000Z_box03`,
  exact general weight-15/18 extraction and optional characteristic-zero
  Singular basis, PID recorded remotely before execution, `timeout 1800`,
  `ulimit -v 33554432` (32 GiB), `nice -n 10`.
- Box03 `98.80.65.144`,
  `/home/ubuntu/jobs/max12_912_order3_d1_general_leading_charts_20260825T231000Z_box03`,
  exact `q2=0` and `q2!=0` polynomial-parameter charts of the same initial
  ideal, PIDs recorded remotely before execution, `timeout 1800`,
  `ulimit -v 33554432` (32 GiB), `nice -n 10`.
- Box03 `98.80.65.144`,
  `/home/ubuntu/jobs/max12_912_order3_d1_firewall_controls_20260825T224323Z_box03`,
  independent inverse-triangularity, missed-layer, singular-cubic negative,
  and binomial-weight controls.  Worker PID `117398`, held behind a `GO`
  sentinel until this registration was written.  Caps: `timeout 1800`,
  `ulimit -v 16777216` (16 GiB),
  `nice -n 10`.
  The first sentinel release failed closed before algebra with
  `REFUSE_UNREGISTERED_AWS_TAG`; the registered retry uses the identical
  source bytes in a source-tree-shaped staging root, exports
  `JC2_AWS_TAG=max12_912_order3_d1_firewall_controls_20260825T224323Z_box03`,
  and was again held behind `GO2` until worker PID `118237` was recorded
  here.  It retains the same `timeout 1800`, 16-GiB virtual-memory cap, and
  `nice -n 10` limits.
  That retry reached the algebra and failed because the test called a matrix
  with unit diagonal and entries below it "upper triangular".  This is a
  control-harness orientation error, not a theorem identity failure.
- Box03 `98.80.65.144`,
  `/home/ubuntu/jobs/max12_912_order3_d1_firewall_controls_v2_20260825T224711Z_box03`,
  corrected lower-triangular orientation control, source SHA-256
  `202cc9895216ca8c3dd741de6339bded1413939d4c0b62e8707a19428757db8c`.
  Worker PID `118818`, held behind a `GO` sentinel until this line was
  recorded; caps are `timeout 1800`, `ulimit -v 16777216` (16 GiB),
  `nice -n 10`.

These computations are reconnaissance for exact identities and a smaller
successor gate.  They do not adjudicate the parent slope-uniform saturation,
prove accessibility, or exclude a D1 trajectory unless a separately stated
theorem supplies the valuation and chart coverage.
