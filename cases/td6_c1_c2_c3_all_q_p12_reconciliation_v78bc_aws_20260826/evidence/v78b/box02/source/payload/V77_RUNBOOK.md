# V77 AWS runbook

Set `TD6_V77_EXPECT_HOST` to the exact Linux hostname, set a unique
`TD6_V77_RUN_TAG` beginning with `td6_v77_`, and invoke `run_v77.sh` from
the archive root.  The wrapper refuses Darwin, hostname mismatches, missing
source closure, and unregistered tags.

Recommended supervisor:

```text
systemd-run --user --scope -p MemoryMax=12G timeout 14400 bash run_v77.sh
```

The exact Python replay is substantive and must never run on the local Mac.
