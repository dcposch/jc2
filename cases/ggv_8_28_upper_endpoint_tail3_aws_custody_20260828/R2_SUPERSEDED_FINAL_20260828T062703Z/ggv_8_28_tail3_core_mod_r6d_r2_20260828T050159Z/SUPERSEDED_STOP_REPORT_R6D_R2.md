# Tail-three modular R2 supersession stop

Date: 2026-08-28

Classification: **OPERATIONAL SUPERSEDED STOP — NON-EVIDENCE** for each of
charts 0, 1, 2, 3, 4, and 5.

## Reason and scope

The coordinator ordered an immediate orderly stop after the complete
fixed-fixture `D18`--`D22` endpoint exclusion passed an independent hostile
review with 289/289 checks.  That exact result strictly subsumes this
discovery-only modular necessary-subsystem reconnaissance.  The charged
superseding hostile-review report has SHA-256
`a294cdf70f0496b360855b1b88e6f362e752e0bda33498902eb6fba7785e23a5`;
its machine result has SHA-256
`378eac96f59427218a30e40848defe7a1a6670da4efadc17f71a04046348382e`.

This report makes no mathematical inference from the stopped modular run.

## Pre-stop classification gate

The immutable pre-stop snapshot was completed at
`2026-08-28T06:22:54Z` before any stop signal.  It found no `RUN_*`,
`WORKERS_*`, `RESOURCE_*`, `STOP_*`, or `chart*.rc` terminal marker.  Each
of the six logs was exactly 78 bytes and contained only its scope, branch,
chart, field, generator count, and variable count.  In particular, no
`STD`, `UNIT`, result, certificate, or other algebraic terminal marker
predated the stop.

The final pre-stop telemetry row at `2026-08-28T06:22:45Z` had
`MemAvailable=303414328 KiB`, free disk `118740066304` bytes, swap used
zero, and these namespace-validated worker-group RSS values:

```text
384230:33818424 KiB  384248:35666232 KiB  384266:35334252 KiB
384284:35199196 KiB  384302:35659812 KiB  384320:35518624 KiB
```

Their aggregate, `211196540 KiB`, is also the maximum aggregate RSS in the
retained telemetry.  The 150-GiB live MemAvailable floor was never crossed.

## Validated stop

The exact second fenced stop command from
`LAUNCH_PREREGISTRATION_R2.md` SHA-256
`1de65c54ca1460577189e74a5070f53aa22d10cff857e196f0929f3588b0f0a5`
was used.  It re-resolved the sole immutable run namespace and validated
PID = PGID, SID, and namespace job path for every member before signaling.
It issued TERM, and no KILL, to exactly these six registered worker groups:

```text
384230 384248 384266 384284 384302 384320
```

The `STOP_REQUESTED` marker dates to `2026-08-28T06:23:05Z`.  All workers
terminated promptly.  Their failure returns caused the runner to write
`RUN_INCOMPLETE_OR_FAILED` and `RUN_EVIDENCE.sha256`, stop its internal
guard, and exit naturally before a separate runner TERM was necessary.
The final logs are 86 bytes: the same pre-stop headers followed only by
`halt 1`, emitted during interruption.  That post-signal line is
operational and is not an algebraic result.

A first read-only post-check aborted on shell/Awk quoting and issued no
signal or mutation.  Independent corrected censuses then found all seven
registered SIDs empty, no hostwide `Singular`, and no residual process with
the immutable namespace path.

## Final custody state

At `2026-08-28T06:27:03Z`, the final retained markers were exactly:

```text
RUN_EVIDENCE.sha256
RUN_INCOMPLETE_OR_FAILED
STOP_REQUESTED
```

There are no chart return-code files and no result marker.  Literal replay
of the inner `RUN_EVIDENCE.sha256` passed for every listed file.  The final
host snapshot recorded `MemAvailable=514946308 KiB`, zero configured/used
swap, free disk `118731567104` bytes, no registered SID, no hostwide
`Singular`, and no namespace descendant or orphan.

Therefore charts 0--5 are each and only:

**OPERATIONAL SUPERSEDED STOP — NON-EVIDENCE.**
