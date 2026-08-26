# AWS launches: order-one fixed-load coefficient curves

Status: live dual-fibre navigation probes; no endpoint interpreted.

The frozen package manifest has SHA-256
`bc8b149cb5b20245b494d99294cbcecd408123d3faf31b6cee326ff3788e6765`.
At launch the seven running AWS instances were exactly one `x8i.16xlarge`
(64 vCPU), one `x2idn.32xlarge` (128 vCPU), and five `r6i.16xlarge`
(5 times 64 vCPU), totaling the authorized 512 vCPUs.  Box03 and r6d had
spare cores and hundreds of GiB available, so no additional instance was
requested.

## Tuple A / characteristic 32003

```text
tag=max12_812_order1_fixedload_A_p32003_20260826T043500Z_box03
host=ip-172-30-0-249 / Box03 / 98.80.65.144
job=/home/ubuntu/jobs/max12_812_order1_fixedload_A_p32003_20260826T043500Z_box03
registered start=2026-08-26T04:35:36Z
outer SSH shell PID=159605
registered launcher PID=159606
aws_exact_lane PID at first audit=159623
Singular PID at first audit=159632
compile timeout=1200 s; compiler rc=0
engine timeout=2400 s
virtual-memory cap=67108864 KiB
emitted input SHA-256=064ae9342b944dfe489d6a3710f6833c7c34256ec262939b056d54b995eb4371
```

## Tuple B / characteristic 65521

```text
tag=max12_812_order1_fixedload_B_p65521_20260826T043500Z_r6d
host=ip-172-30-0-45 / r6d / 100.26.198.153
job=/home/ubuntu/jobs/max12_812_order1_fixedload_B_p65521_20260826T043500Z_r6d
registered start=2026-08-26T04:35:36Z
outer SSH shell PID=226967
registered launcher PID=226968
aws_exact_lane PID at first audit=226985
Singular PID at first audit=226994
compile timeout=1200 s; compiler rc=0
engine timeout=2400 s
virtual-memory cap=67108864 KiB
emitted input SHA-256=02e43376af5562fdc251802a48c9112ed5884b655eb95652258f1bac21507309
```

Both compilers passed the reviewed shared-Faber replay, exact target gauges,
all eleven high rows, inverse-series closure through the order consumed by
`r7`, and exact tail emission.  Both Singular engines were live near one
CPU core and neither host used swap at first audit.  These fibres remain
navigation only; in particular no plane eliminant is a normalization genus,
and `r7` was not saturated away.
