# Registration: order-one fixed-load coefficient-curve reconnaissance

Status: preregistered AWS-only navigation probes; no result.

```text
config=A
tag=max12_812_order1_fixedload_A_p32003_20260826T043500Z_box03
host=Box03 / 98.80.65.144
job=/home/ubuntu/jobs/max12_812_order1_fixedload_A_p32003_20260826T043500Z_box03
compile timeout=1200 s
engine timeout=2400 s
virtual-memory cap=67108864 KiB
characteristic=32003

config=B
tag=max12_812_order1_fixedload_B_p65521_20260826T043500Z_r6d
host=r6d / 100.26.198.153
job=/home/ubuntu/jobs/max12_812_order1_fixedload_B_p65521_20260826T043500Z_r6d
compile timeout=1200 s
engine timeout=2400 s
virtual-memory cap=67108864 KiB
characteristic=65521
```

The two lanes use different deterministic load tuples, primes, and hosts.
The compiler performs the substantive Faber/tail reconstruction on AWS before
the Singular phase; both phases share the 64-GiB cap and together have a
one-hour timeout budget.  The instance fleet already occupies the account's
512-vCPU running quota, so these right-sized one-core payloads use spare cores
on existing r6i.16xlarge hosts rather than requesting another instance.  No
instance teardown is associated with these shared hosts; the campaign
coordinator retains the existing fleet teardown decision.

A timeout or failure is no verdict.  Successful modular fibres remain
navigation only under the source/component/genus firewall in the frozen
design.
