# AWS-only next top-carry compiler

This is a preregistered discovery runner, not yet a frozen mathematical
result.  It is intentionally excluded from all local replays.

Run on an AWS host from this directory:

```sh
/usr/bin/time -v python3 compile_next_top_carry.py > /tmp/as-d7-next-top.out 2> /tmp/as-d7-next-top.time
sha256sum /tmp/as-d7-next-top.out /tmp/as-d7-next-top.time
```

Expected work is exactly `1,085,103` visible parent solutions plus small
six-variable linear systems.  Start with one CPU and 8 GB RAM; 16 GB is a
conservative ceiling.  The Python process is single-threaded.  Timeout or
OOM is no mathematical verdict.
