# AWS registration ledger

Date: 2026-08-25

Both workers are started behind `GO_COMPILE`; no charged reconstruction or
solver payload may begin until the worker PID and caps below are recorded.
After independent compilation, both workers stop behind `GO_SOLVE` until the
emitted inputs have been retrieved, compared, and frozen.

## Encoding A

- tag: `max12_912_order3_d1_double_root_toric_20260825T235300Z_box02_A`
- host: Box02, `34.203.207.55`, expected 128 vCPU / 2 TiB RAM
- job directory:
  `/home/ubuntu/jobs/max12_912_order3_d1_double_root_toric_20260825T235300Z_box02_A`
- compiler cap: 64 GiB virtual, timeout 3600 s, nice 10
- solver cap: 1536 GiB virtual, timeout 43200 s, nice 10
- encoding: factored rows, `dp`, sequential `sat`
- worker PID: `243921`, recorded from `worker.metadata`; blocked behind
  `GO_COMPILE` before charged reconstruction

## Encoding B

- tag: `max12_912_order3_d1_double_root_toric_20260825T235300Z_r6d_B`
- host: r6d, `100.26.198.153`, expected 64 vCPU / 512 GiB RAM
- job directory:
  `/home/ubuntu/jobs/max12_912_order3_d1_double_root_toric_20260825T235300Z_r6d_B`
- compiler cap: 64 GiB virtual, timeout 3600 s, nice 10
- solver cap: 448 GiB virtual, timeout 43200 s, nice 10
- encoding: expanded rows, `(lp(2),dp(18))`, inverse elimination
- worker PID: `184305`, recorded from `worker.metadata`; blocked behind
  `GO_COMPILE` before charged reconstruction
