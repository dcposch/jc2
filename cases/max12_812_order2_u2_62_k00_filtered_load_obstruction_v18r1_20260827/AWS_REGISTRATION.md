# AWS registration: K00 filtered first-load obstruction V18R1

Registered UTC: 2026-08-27T11:18:42Z

Good-prime preflight lane (explicit provisional dependency):

```text
dependency=V17 p65521 endpoint only; no characteristic-zero inference
repair=whitelisted factored-polynomial AST parser plus modular-dual replay
failed_v18_emitter_sha256=a26149ce209c57491fa7f6610160e750fb280873429ab22bd6dda6cc6b6b7a88
v17_result_sha256=6e26a3211a86cbda10cdc8ead0e5cfc875964db2c44b225c99733e84fe71bdcc
v17_branches=K10:LOCAL_NONZERO,K6:LOCAL_NONZERO,K2:LOCAL_NONZERO
freeze_sha256=08c28764ed4c63bfca477940a5889b6e31ee421c81baab5725351d0a3a30e849
host_alias=r6a
public_host=3.91.104.135
expected_private_hostname=ip-172-30-0-34
tag=max12_812_order2_u2_62_k00_filtered_load_v18r1_p65521_20260827T111842Z_r6a
remote_job=/home/ubuntu/jobs/max12_812_order2_u2_62_k00_filtered_load_v18r1_p65521_20260827T111842Z_r6a
field=65521
maximum_cutoff=6
timeout_seconds_per_matrix=600
virtual_memory_cap_kib=67108864
scope=MODULAR_PREFLIGHT_ONLY; exact V17 r2 and exact V18 remain mandatory
```

The r6a lane completed emission but failed before algebra because that host
does not provide `g++`; see `FAILURE_R6A_NO_GXX.md`.  The following host-only
repair reuses the identical frozen V18R1 source and immutable V17 `p=65521`
endpoint bytes:

```text
registered_utc=2026-08-27T11:25:13Z
dependency=V17-p65521 provisional; no characteristic-zero inference
repair=host relocation after missing g++; source/algorithm/order unchanged
v17_result_sha256=6e26a3211a86cbda10cdc8ead0e5cfc875964db2c44b225c99733e84fe71bdcc
freeze_sha256=08c28764ed4c63bfca477940a5889b6e31ee421c81baab5725351d0a3a30e849
host_alias=Box01
public_host=54.175.21.169
expected_private_hostname=ip-172-30-0-237
tag=max12_812_order2_u2_62_k00_filtered_load_v18r1_p65521_20260827T112513Z_box01_hostrepair
remote_job=/home/ubuntu/jobs/max12_812_order2_u2_62_k00_filtered_load_v18r1_p65521_20260827T112513Z_box01_hostrepair
field=65521
maximum_cutoff=6
timeout_seconds_per_matrix=600
virtual_memory_cap_kib=67108864
toolchain_preflight=g++ and FLINT header/library present
scope=MODULAR_PREFLIGHT_ONLY; exact V17 r2 and exact V18 remain mandatory
```
