# AWS launches: one-parameter Rees race

Frozen source archive, both hosts:

```text
ed3a99b9d5e87c183075fbbf17a9cdfd806355b42246a13c92332beb7d9f7a7b
```

Freeze manifest SHA:

```text
84da88152fcc1ec7552b4c12f950d0979b4edc0a80269e315736cfac37d38f6e
```

## Exact Q / Box03

```text
tag=max12_812_order2_u2_62_oneparam_q_20260826T035200Z_box03
host=ip-172-30-0-249 / 98.80.65.144
job=/home/ubuntu/jobs/max12_812_order2_u2_62_oneparam_q_20260826T035200Z_box03
outer nohup PID=153839
registered launcher PID=153844
Singular PID at audit=153869
registered UTC=2026-08-26T03:51:37Z
timeout=7200 s
virtual-memory cap=201326592 KiB
characteristic=0
emitted input SHA=74d387ce1dd0a60edc943f4ecccf230186e52efaaba942d7257571ea8d826cfe
```

## Good prime / r6d

```text
tag=max12_812_order2_u2_62_oneparam_p32003_20260826T035200Z_r6d
host=ip-172-30-0-45 / 100.26.198.153
job=/home/ubuntu/jobs/max12_812_order2_u2_62_oneparam_p32003_20260826T035200Z_r6d
outer nohup PID=221558
registered launcher PID=221563
Singular PID at audit=221588
registered UTC=2026-08-26T03:51:37Z
timeout=7200 s
virtual-memory cap=134217728 KiB
characteristic=32003
emitted input SHA=61963d1c9a79dd70bebc32ae014b87f2c4e1e1afe201761f86566d242020d842
```

Both compilers passed the exact source/tail/weight/load-linearity checks and
both engines reached `ONEPARAM_STAGE_LAMBDA_START`.  No endpoint has yet been
interpreted.  Timeout or failure is no mathematical verdict.
