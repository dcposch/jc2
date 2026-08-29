# AWS registration: K00 closure-first incidence V1

Registered UTC: 2026-08-27T07:32:00Z

Frozen source payload:

```text
522b5a267364657ec6168252bd50b897dab6eeab751b4c49f58dc1f85c3912d9
```

Source-closure / freeze manifest SHA (byte-identical files):

```text
e1bb1590a14d37ccf57e4809241ac7b5b442be45b5b01c6de005b6ef57528632
```

## Exact Q mathematical lane

```text
host_alias=Box02
public_host=34.203.207.55
expected_private_hostname=ip-172-30-0-186
tag=max12_812_order2_u2_62_k00_closure_v1_q_20260827T073200Z_box02
remote_job=/home/ubuntu/jobs/max12_812_order2_u2_62_k00_closure_v1_q_20260827T073200Z_box02
characteristic=0
timeout_seconds=21600
virtual_memory_cap_kib=201326592
role=MATHEMATICAL_ENDPOINT
```

## Good-prime software/control lane

```text
host_alias=Box03
public_host=98.80.65.144
expected_private_hostname=ip-172-30-0-249
tag=max12_812_order2_u2_62_k00_closure_v1_p65521_20260827T073200Z_box03
remote_job=/home/ubuntu/jobs/max12_812_order2_u2_62_k00_closure_v1_p65521_20260827T073200Z_box03
characteristic=65521
timeout_seconds=21600
virtual_memory_cap_kib=201326592
role=SOFTWARE_CONTROL_ONLY
```

Both hosts had zero swap and more than 490 GiB available memory at the live
prelaunch audit.  Box02 had no material worker; Box03 had no material
worker.  The jobs are serialized separately on distinct hosts.  Neither
lane has an endpoint at registration, and a timeout or failed validation is
no mathematical verdict.
