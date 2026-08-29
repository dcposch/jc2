# AWS launch metadata: `p=0` cusp grade-12 unit replay

Date: 2026-08-26

Both lanes replayed the same frozen exact-rational source independently.  The
finite-field reductions printed by the client are controls only; the exact-Q
collection precedes them and carries the producer claim.

## Box03

```text
tag=max12_812_order2_p0_cusp_g12_unit_20260826T110537Z_Box03_exact
instance=Box03 (AWS r6i.16xlarge)
remote_host=ip-172-30-0-249
remote_job=/home/ubuntu/jobs/max12_812_order2_p0_cusp_g12_unit_20260826T110537Z_Box03_exact/source/cases/max12_812_order2_p0_cusp_grade12_unit_replay_20260826/aws_Box03_exact
start_utc=2026-08-26T11:05:49Z
end_utc=2026-08-26T11:05:50Z
engine_rc=0
validator=PASS_P0_CUSP_GRADE12_UNIT_REPLAY
wall=0.81 s
max_rss=18996 KiB
major_faults=0
swaps=0
```

The compiled result has SHA-256
`59728f3bf784d6e9a4e45b3a684511a83fc2630a968822291b00cf1a435a1ff7`.

## r6d

```text
tag=max12_812_order2_p0_cusp_g12_unit_20260826T110537Z_r6d_exact
instance=r6d (AWS r6i.16xlarge)
remote_host=ip-172-30-0-45
remote_job=/home/ubuntu/jobs/max12_812_order2_p0_cusp_g12_unit_20260826T110537Z_r6d_exact/source/cases/max12_812_order2_p0_cusp_grade12_unit_replay_20260826/aws_r6d_exact
start_utc=2026-08-26T11:05:49Z
end_utc=2026-08-26T11:05:50Z
engine_rc=0
validator=PASS_P0_CUSP_GRADE12_UNIT_REPLAY
wall=0.80 s
max_rss=18864 KiB
major_faults=0
swaps=0
```

The compiled result has SHA-256
`99be700dc6ccd07df46f772aa6661cac7173b74cf701016748b056d1b5a0aee2`.

The two JSON result hashes differ only because the registered lane tag is a
field in the JSON.  Every mathematical field and every validator line agrees.
Both remote `freeze_check.stdout` files have SHA-256
`5fa4f3eba1aeb80230b0a6e633437d85ea2307600d1afce4e91c9fe156c8a692`
and report every frozen source as `OK`.

