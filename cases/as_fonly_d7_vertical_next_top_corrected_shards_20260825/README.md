# AWS-only corrected degree-eleven shard census

This runner attaches the divided single-Frobenius term identified by the
frozen source erratum.  Run only on AWS with at least 27 idle CPUs:

```sh
nohup setsid ./launch_all.sh UNIQUE_UTC_TAG > launch_UNIQUE_UTC_TAG.log 2>&1 < /dev/null &
```

Each shard has one CPU, an 8 GiB VM ceiling, and a 12-hour timeout.  The
aggregate is fail-closed and must reproduce the exact N12 control total.
