# AWS-only source-corrected degree-ten shard census

This runner consumes the frozen corrected-Q11 source, attaches both
degree-ten divided-Frobenius summands, and tests all visible predecessor
states. Run only on AWS with at least 27 idle CPUs:

```sh
nohup setsid ./launch_all.sh UNIQUE_UTC_TAG > launch_UNIQUE_UTC_TAG.log 2>&1 < /dev/null &
```

Each shard has one CPU, an 8 GiB VM ceiling, and a 12-hour timeout. The
aggregate is fail-closed and must reproduce all three predecessor totals.
