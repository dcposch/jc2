# AWS metadata: fixed `p=0` residual `A`-Cech replay

Date: 2026-08-26

## Exact Q — Box03

```text
tag=max12_812_order2_p0_a_cech_20260826T112534Z_Box03_q
host=ip-172-30-0-249
remote_job=/home/ubuntu/jobs/max12_812_order2_p0_a_cech_20260826T112534Z_Box03_q/source/cases/max12_812_order2_p0_a_cech_g14_g15_20260826/aws_Box03_q
start_utc=2026-08-26T11:25:49Z
end_utc=2026-08-26T11:25:49Z
engine_rc=0
validator=PASS_P0_A_CECH_G14_G15
wall=0.02 s
max_rss=12784 KiB
major_faults=0
swaps=0
```

Compiled result SHA-256:
`72fd6e5b5d90bee397e99ce4ee1c59dfbf2a98b6649caf6b471d6a54340fa98d`.

## Independent `F_65521` control — r6d

```text
tag=max12_812_order2_p0_a_cech_20260826T112534Z_r6d_p65521
host=ip-172-30-0-45
remote_job=/home/ubuntu/jobs/max12_812_order2_p0_a_cech_20260826T112534Z_r6d_p65521/source/cases/max12_812_order2_p0_a_cech_g14_g15_20260826/aws_r6d_p65521
start_utc=2026-08-26T11:25:49Z
end_utc=2026-08-26T11:25:49Z
engine_rc=0
validator=PASS_P0_A_CECH_G14_G15
wall=0.01 s
max_rss=12328 KiB
major_faults=0
swaps=0
```

Compiled result SHA-256:
`b1f38b69b251ae5b269fcc023b4f05d5762b5ac7e56008cc82f99e1b892172dc`.

Exact Q carries the producer claim.  The good-prime lane is a control only.
Both remote freeze checks are byte-identical (SHA-256
`113ed25f0aab68f7e65ef417fd070560e78091ceb3fd38cd998b0c1543924e95`)
and report every frozen input as `OK`.

