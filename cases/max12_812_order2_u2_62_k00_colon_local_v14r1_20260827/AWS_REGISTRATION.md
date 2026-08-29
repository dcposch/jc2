# AWS registration: K00 colon-local V14R1 custody repair

Registered UTC: 2026-08-27T09:59:01Z

Exact-Q primary lane:

```text
source_payload_sha256=b84439a483d033dc18b7141b2c5ec0e1159c6cafddab2a945a7c0a95ac725f7f
freeze_sha256=8c6dd8e2e012d72519051a708975d892c0bed700fbfd17df7c1a15b899fde010
host_alias=Box01
public_host=54.175.21.169
expected_private_hostname=ip-172-30-0-237
tag=max12_812_order2_u2_62_k00_colon_local_v14r1_q_20260827T095901Z_box01
remote_job=/home/ubuntu/jobs/max12_812_order2_u2_62_k00_colon_local_v14r1_q_20260827T095901Z_box01
field=Q
timeout_seconds=1800
outer_timeout_seconds=2100
virtual_memory_cap_kib=67108864
```

Good-prime control lane:

```text
source_payload_sha256=b84439a483d033dc18b7141b2c5ec0e1159c6cafddab2a945a7c0a95ac725f7f
freeze_sha256=8c6dd8e2e012d72519051a708975d892c0bed700fbfd17df7c1a15b899fde010
host_alias=r6a
public_host=3.91.104.135
expected_private_hostname=ip-172-30-0-34
tag=max12_812_order2_u2_62_k00_colon_local_v14r1_p65521_20260827T095901Z_r6a
remote_job=/home/ubuntu/jobs/max12_812_order2_u2_62_k00_colon_local_v14r1_p65521_20260827T095901Z_r6a
field=65521
timeout_seconds=900
outer_timeout_seconds=1200
virtual_memory_cap_kib=33554432
```

Both lanes regenerate the frozen V14 calculation.  V14R1's only mathematical
change is evidence custody: it serializes all 36 colon-lift entries, freezes
the chosen six-multiplier unit witness, and replays that identity in a fresh
Singular process built from the serialized polynomial bytes.
