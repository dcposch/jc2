# Registration: `(8,12)` order-two `U=2,[6,2]` strict-Rees compiler

Status: preregistered, AWS-only, no result yet.

The compiler reconstructs the four Faber polynomials and all seven ordinary
tails from the reviewed shared sparse-arithmetic source, verifies every tail
weight, and emits the exact ordinary `T=1` strict-Rees ideal.  It does not run
the emitted saturation and does not compile either finite Taylor family.

Required environment:

```text
Linux on Amazon EC2
JC2_REGISTERED_AWS_LANE=<nonempty registered tag>
```

Inputs and output hashes are checked or recorded.  A launch must use
`ops/aws_exact_lane.sh` and record remote host, job directory, PID, timeout,
memory cap, engine version, source archive hash, and UTC start before the
payload.

The frozen `run_compile_aws.sh` applies a 7,200-second inner timeout and a
128-GiB virtual-memory cap before calling the hardened shared wrapper.

Frozen sources:

```text
840a12e29386d37801f986e39273c3fb34f5542019cc1da7043ee1730dcb31f2  compile_rees.py
f0630c6ce8131494e2c9df66927c747186358032aba8fcf2a60abd88ae2f6c72  run_compile_aws.sh
e5e3472f052b2ae932daefc9dec7a17106ca4c13f8b920ba59da627d0653fec7  ../../xmodel/max12-812-order2-u2-62-strict-rees-client-20260825.md
69f9e12c0fa1e98bb7bc4dda87ab00c7f87ce2fd9c80a4bf210d216ee1bd2d9f  ../max12_high_row_probe_20260824/shared_faber_probe.py
```

Terminal scope:

```text
tail_reconstruction=EXACT_IF_PASS
strict_saturation=EMITTED_NOT_RUN
Taylor_x0=CHARGED_NOT_COMPILED
Taylor_x1=CHARGED_NOT_COMPILED
order2_closed=false
JC2=NOT_CLAIMED
```
