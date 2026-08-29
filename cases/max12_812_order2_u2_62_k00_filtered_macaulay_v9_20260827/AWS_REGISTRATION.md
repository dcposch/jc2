# AWS registration: exact K00 filtered Macaulay degree 7 V9

Registered UTC: 2026-08-27T09:03:09Z

Common frozen source:

```text
source_payload_sha256=2d3f2bf7068ab7803ad4c0fd7de7e019286ea4609d23006d81c20a395e1434ca
freeze_sha256=b62f74f8f49d22b5b8e272eee6c49ed8757e04c903b3eff749df3ab51e99a7d6
cutoffs=D2,D3,D4,D5,D6,D7
```

Exact rational lane:

```text
host_alias=Box01
public_host=54.175.21.169
expected_private_hostname=ip-172-30-0-237
tag=max12_812_order2_u2_62_k00_filtered_macaulay_v9_q_20260827T090309Z_box01
remote_job=/home/ubuntu/jobs/max12_812_order2_u2_62_k00_filtered_macaulay_v9_q_20260827T090309Z_box01
field=Q
per_cutoff_timeout_seconds=7200
outer_timeout_seconds=9000
virtual_memory_cap_kib=268435456
```

Good-prime software/navigation lane:

```text
host_alias=r6d
public_host=3.91.104.135
expected_private_hostname=ip-172-30-0-34
tag=max12_812_order2_u2_62_k00_filtered_macaulay_v9_p65521_20260827T090309Z_r6d
remote_job=/home/ubuntu/jobs/max12_812_order2_u2_62_k00_filtered_macaulay_v9_p65521_20260827T090309Z_r6d
field=65521
per_cutoff_timeout_seconds=1800
outer_timeout_seconds=2400
virtual_memory_cap_kib=67108864
```

Only the exact-Q endpoint can promote a filtered compatibility statement.

## Software-lane reroute

The registered r6d process failed before any matrix engine ran because that
host has no `g++`.  Its emitter passed, but it produced no cutoff stdout and
no mathematical result.  The identical frozen payload was therefore
re-registered on compiler-equipped Box02 at `2026-08-27T09:04:45Z`:

```text
host_alias=Box02
public_host=34.203.207.55
expected_private_hostname=ip-172-30-0-186
tag=max12_812_order2_u2_62_k00_filtered_macaulay_v9_p65521_20260827T090445Z_box02
remote_job=/home/ubuntu/jobs/max12_812_order2_u2_62_k00_filtered_macaulay_v9_p65521_20260827T090445Z_box02
field=65521
per_cutoff_timeout_seconds=1800
outer_timeout_seconds=2400
virtual_memory_cap_kib=67108864
```
