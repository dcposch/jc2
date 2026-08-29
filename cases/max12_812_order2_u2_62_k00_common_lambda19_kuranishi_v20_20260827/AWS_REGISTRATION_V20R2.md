# AWS registration: V20R2 contracted source compiler

## R0 — failed before algebra

```text
host_alias=r6b
public_host=34.204.74.226
private_hostname=ip-172-30-0-106
tag=max12_812_order2_u2_62_k00_common_lambda19_v20r2_20260827T123800Z_r6b
remote_job=/home/ubuntu/jobs/max12_812_order2_u2_62_k00_common_lambda19_v20r2_20260827T123800Z_r6b
source_freeze_manifest_sha256=647de67b40f66eb88e7202ee76208771b4a1fae69900dd5f34e959f3ca21e549
compiler_sha256=13342b16367b347680d6cbb4fb726798b7c1904422b10a661f31f5b7b59974b0
wrapper_sha256=f6332a9d4535b3731b097f4b54747ba87ed52fcf2c627fc313bc0877d35819d1
field=Q_with_F65521_fixture_control
cores=1
virtual_memory_cap_kib=67108864
wall_cap_seconds=3600
```

R0 failed in 0.19 seconds / 34,880 KiB before algebra because the wrapper
pre-created the compiler output directory.  It is nonpromotable and preserved
under `aws_r6b_r0_failed/` and `FAILURE_V20R2_R0.md`.

## R1 — runner-only repair

```text
registered_utc=2026-08-27T12:41:00Z
host_alias=r6b
public_host=34.204.74.226
private_hostname=ip-172-30-0-106
tag=max12_812_order2_u2_62_k00_common_lambda19_v20r2r1_20260827T124100Z_r6b
remote_job=/home/ubuntu/jobs/max12_812_order2_u2_62_k00_common_lambda19_v20r2r1_20260827T124100Z_r6b
outer_pid=56609
source_freeze_manifest_sha256=4331078823c3bf88e4de46826a6a071b749ec2162d3093e872f9ae54e9b5a224
compiler_sha256=13342b16367b347680d6cbb4fb726798b7c1904422b10a661f31f5b7b59974b0
wrapper_sha256=7bbbf96f1de34906399dc08f85388582b41feac53472c4d23a44b4013a06e5f6
repair_preregistration_sha256=847ae7fc8f0b86d48ba445f0a67c77c3c1c831d7c79cef94121da365cccdfb26
field=Q_with_F65521_fixture_control
cores=1
virtual_memory_cap_kib=67108864
wall_cap_seconds=3600
source_tree_mode=read_only
```

At launch r6b had approximately 476 GiB available and no swap.  One existing
unrelated one-core job used about 14 GiB; neither path nor process was
modified.

R1 failed closed in 3.19 seconds / 159,252 KiB before Singular because the
modular DAG fixture compared unreduced integer representatives with reduced
`F_65521` values.  It is preserved under `aws_r6b_r1_failed/`; its exact-Q
fixtures passed, but it emitted no endpoint.

## R2 — modular-normalization repair

```text
registered_utc=2026-08-27T12:45:00Z
host_alias=r6b
public_host=34.204.74.226
private_hostname=ip-172-30-0-106
tag=max12_812_order2_u2_62_k00_common_lambda19_v20r2r2_20260827T124500Z_r6b
remote_job=/home/ubuntu/jobs/max12_812_order2_u2_62_k00_common_lambda19_v20r2r2_20260827T124500Z_r6b
outer_pid=57799
source_freeze_manifest_sha256=8f9e893fa3357787ef8d095cb8e1e040efe788ce54b70f150b77ad1b5bab41cb
compiler_sha256=2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
wrapper_sha256=7bbbf96f1de34906399dc08f85388582b41feac53472c4d23a44b4013a06e5f6
repair_preregistration_sha256=c50d8ca9cba09a2783815d961d22446340aa9f82e401db2a5a94375985656b2b
field=Q_with_F65521_fixture_control
cores=1
virtual_memory_cap_kib=67108864
wall_cap_seconds=3600
source_tree_mode=read_only
```
