# AWS-only pure-N degree-ten successor

Do not run this compiler on the workstation: importing its predecessor runs
the full degree-12/11 enumeration, and this runner then re-enumerates the
visible predecessor locus to append degree ten.

AWS command from this directory:

```sh
/usr/bin/time -v python3 compile_next_top3.py > /tmp/as-d7-next-top3.out 2> /tmp/as-d7-next-top3.time
sha256sum /tmp/as-d7-next-top3.out /tmp/as-d7-next-top3.time
```

Use one CPU, an 8 GiB expected working set, a 16 GiB hard ceiling, and a
12-hour timeout.  Timeout/OOM/incomplete output is no evidence.
