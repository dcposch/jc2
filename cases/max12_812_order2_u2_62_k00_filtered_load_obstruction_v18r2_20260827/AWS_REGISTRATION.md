# AWS registration: provisional exact-Q K00 filtered load V18R2

```text
registered_utc=2026-08-27T11:36:27Z
dependency=V17-p65521 provisional; exact V17-Q local-colon endpoint pending
promotion_gate=no promotion before V17-Q agrees and exact artifacts match
q_provisional_freeze_sha256=92706f32740b73255086b0596832b075a6bce670745eed471359aeaa021f06e1
compiled_v17_q_sha256=9e22780c0f9b38f2e502b08ac51c1b9d8fee21e7b40e9569d08d77a3683d8b5c
v17_p_result_sha256=6e26a3211a86cbda10cdc8ead0e5cfc875964db2c44b225c99733e84fe71bdcc
expected_exact_pattern=K10:D4,K6:D3,K2:D2
host_alias=Box01
public_host=54.175.21.169
expected_private_hostname=ip-172-30-0-237
tag=max12_812_order2_u2_62_k00_filtered_load_v18r2_qprov_20260827T113627Z_box01
remote_job=/home/ubuntu/jobs/max12_812_order2_u2_62_k00_filtered_load_v18r2_qprov_20260827T113627Z_box01
field=Q
extract_timeout_seconds=1800
timeout_seconds_per_matrix=1200
virtual_memory_cap_kib=134217728
scope=PROVISIONAL_EXACT_Q_FILTERED_CLASSES_ONLY
firewall=NO_V17_Q_BRANCH_CLAIM_NO_PROMOTION_NO_COUPLING_NO_LAMBDA19_NO_HONEST_SOURCE_REACHABILITY_NO_ARC_EXCLUSION
```

R0 failed before algebra on the frozen output-parent conflict documented in
`FAILURE_QPROV_R0.md`.  Runner-only R1 relocation:

```text
registered_utc=2026-08-27T11:38:55Z
dependency=R0 path failure only; base Q provisional freeze unchanged
q_provisional_r1_freeze_sha256=0315b3ab04d8dcbe3f98bd3713701eeeb460a3fb711da02684ef6c15ade37fbc
repair=exact-input script parent moved to absent compiled/extracted directory
host_alias=Box01
public_host=54.175.21.169
expected_private_hostname=ip-172-30-0-237
tag=max12_812_order2_u2_62_k00_filtered_load_v18r2r1_qprov_20260827T113855Z_box01
remote_job=/home/ubuntu/jobs/max12_812_order2_u2_62_k00_filtered_load_v18r2r1_qprov_20260827T113855Z_box01
field=Q
extract_timeout_seconds=1800
timeout_seconds_per_matrix=1200
virtual_memory_cap_kib=134217728
promotion_gate=no promotion before V17-Q agrees and exact artifacts match
```
