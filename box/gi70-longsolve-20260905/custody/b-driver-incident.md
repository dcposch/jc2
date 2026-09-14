# Job (b) driver and duplicate-dispatch incidents

- Original start: `2026-09-05T17:01:46Z`.
- The original `run_guided.py` called the Hilbert-seed Singular subprocess with
  `timeout=9900`, inside the wrapper's requested 10,200-second guard.
- At `2026-09-05T19:46:49Z` Python raised `subprocess.TimeoutExpired` after
  `9899.999988764` seconds. The wrapper wrote return code `1`. No
  `GI70_B_HNUM_BEGIN`, Hilbert vector, guided run, CRT result, UNIT, dimension,
  or completed-basis marker was emitted.
- The original `/usr/bin/time -v` record (captured before the overwrite below)
  reported user `9831.45` s, system `83.70` s, elapsed `2:45:02`, CPU `100%`,
  maximum RSS `91863060` KiB, 2 major faults, 70,626,116 minor faults, no swap,
  and exit status `1`.
- This is a 165-minute internal driver timeout, not the requested 170-minute
  watchdog and not a mathematical solver verdict.

The first multi-dispatch controller shell remained blocked behind job (a).
When (a) timed out, that stale shell advanced and launched a duplicate (b) at
`2026-09-05T19:50:53Z`. It overwrote the home dispatch log and truncated the
top-level stdout/stderr/time files, but did not overwrite the original
`returncode.txt` (mtime `2026-09-05T19:46:49Z`) or the accumulated RSS log.
At about `19:53:35Z`, after resolving the exact process tree, the duplicate's
remote process groups `13109`, `13110`, and `13118` and the stale controller
process group `218871` were sent TERM. No broad fleet/job kill was used; the
original msolve and slimgb process groups were untouched. The duplicate ran
about 162 seconds and none of its output is admitted as mathematical evidence.

The same blocked controller then advanced once more and launched a duplicate
(c) at `2026-09-05T19:53:35Z`.  It truncated the top-level c dispatch log,
`stderr.log`, `stdout.log`, `time-v.txt`, and `msolve.out`; the identical guard
was rerun.  It did not overwrite the original `returncode.txt` (mtime
`2026-09-05T19:51:52Z`) and the RSS monitor appended rather than truncated.
The final process snapshot identifies the duplicate as PID 13348 with elapsed
57 seconds.  Exact-ID instance termination stopped it.  Its output is also
excluded; original-c evidence is the return-code timestamp, PID 4040 RSS
samples, and controller snapshots, including the degree-8 line at counter
269,752.

Primary surviving evidence is the original return-code mtime, the RSS samples
through `2026-09-05T19:46:47Z` (including original PID 3966 and its peak), the
executed `run_guided.py` containing `timeout=9_900`, and the controller/tool
transcript. The report explicitly discloses both operational errors.
