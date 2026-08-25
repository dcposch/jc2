# AWS-only Q9 source-state gate

This runner reconstructs the canonical integer carry state after corrected
Q10 and solves the exact 23-by-32 affine Q9 extension problem. Run only on
AWS with at least 27 idle CPUs:

```sh
nohup setsid ./launch_all.sh UNIQUE_UTC_TAG > launch_UNIQUE_UTC_TAG.log 2>&1 < /dev/null &
```

Each shard has one CPU, an 8 GiB VM ceiling, and a 12-hour timeout. The
aggregate is fail-closed and must reproduce all four predecessor totals.
