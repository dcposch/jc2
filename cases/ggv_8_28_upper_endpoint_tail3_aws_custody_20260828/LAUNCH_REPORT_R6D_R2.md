# Cutoff-three modular r6d R2 launch report

Classification: **LIVE DISCOVERY-ONLY MODULAR RECONNAISSANCE**

Explicit coordinator clearance charged
`LAUNCH_PREREGISTRATION_R2.md` SHA-256
`1de65c54ca1460577189e74a5070f53aa22d10cff857e196f0929f3588b0f0a5`.
The command was executed verbatim from its first fenced Bash block.  Its
immediate full preflight passed, including the final dummy-descendant
regression, with:

```text
PROCESS_GROUP_REGRESSION_PGID=383909
PROCESS_GROUP_REGRESSION_DUMMY_PID=383917
PROCESS_GROUP_REGRESSION_DUMMY_RSS_KIB=42896
PROCESS_GROUP_REGRESSION_GROUP_RSS_KIB=46556
PROCESS_GROUP_REGRESSION_RSS_INCLUDED=PASS
PROCESS_GROUP_REGRESSION_TERM_CLEARED=PASS
PREFLIGHT=PASS
MEM_AVAILABLE_KIB=514771236
DISK_AVAILABLE_BYTES=118764384256
SWAP_TOTAL_KIB=0
SWAP_USED_KIB=0
```

The launcher identity is PID/SID/PGID `383943`, Linux start time
`28555137`.  The sole run namespace is:

```text
/home/ubuntu/jobs/ggv_8_28_tail3_core_mod_r6d_r2_20260828T050159Z/runs/tail3_core_mod_r6d_call_20260828T051902Z_383943_cutoff3_core_mod_r6d_r2
```

The runner's independent second source/resource/regression preflight also
passed.  The six recorded workers and their actual Singular descendants are:

```text
chart0 worker PID=PGID=SID 384230; Singular 384237
chart1 worker PID=PGID=SID 384248; Singular 384255
chart2 worker PID=PGID=SID 384266; Singular 384273
chart3 worker PID=PGID=SID 384284; Singular 384291
chart4 worker PID=PGID=SID 384302; Singular 384309
chart5 worker PID=PGID=SID 384320; Singular 384327
```

For every chart, the observed live chain is worker Bash, `/usr/bin/time`,
GNU `timeout --foreground`, then Singular.  Every member has the recorded
worker PGID/SID and the exact immutable run-namespace job path.  There is no
inner PGID.

The source-hashed independent live audit at `2026-08-28T05:23:49Z` returned
`R2_LIVE_TOPOLOGY_RESOURCE_AUDIT=PASS`: six hostwide Singular processes,
aggregate validated worker-group RSS 36,040,180 KiB, MemAvailable
477,687,176 KiB, free disk 118,740,312,064 bytes, zero swap, all six PGIDs
in live telemetry, and no terminal/resource marker.  The audit script has
SHA-256 `ad5e8ed8aeecd94568793439ed032f161d7cf60a96b71d64de9dd7f61a18c842`;
its output has SHA-256
`ab86674b738e34537d710dda9a4b3b6f702736daf65c63b483d0db12ccc18a19`.
The remote stable start-custody manifest has SHA-256
`96459f753fad7d7cb5b92037e778cec5de9f55acaed76ce1bab7e529a246ada8`
and verified every charged start artifact and all six rendered jobs.

The lane remains modular heuristic only.  No live observation, timeout,
nonunit, or modular unit is an exact mathematical result.  A terminal state
requires immutable harvest and literal classification.
