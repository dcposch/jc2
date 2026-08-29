# HENS-CT backend adapter r1: frozen AWS result

This directory is the local, byte-replayed custody copy of the isolated AWS
namespace

```text
/home/ubuntu/jobs/ggv_hens_ct_backend_r1_20260828T070029Z_r6c
```

The run was performed on the audited Amazon EC2 `r6i.16xlarge` host `r6c`
(`ip-172-30-0-150`, instance `i-040b7a1c2ed72d4cc`) with one charged core,
zero swap, nested hard timeouts, PID/PGID/SID/starttime registration, continuous
group monitoring, and a final no-orphan census.

`custody/JOB_ARCHIVE.tar.gz` is the immutable remote archive.  `job/` is its
local extraction.  The archive contains the frozen adapter sources, all output
and run records, and the complete 14-MiB patched `ore_algebra` checkout.  It
deliberately excludes the reproducible 2.4-GiB Python virtual environment.

See `RESULT.md` for the mathematical and backend verdict and
`LOCAL_REPLAY.md` for the exact custody replay.

