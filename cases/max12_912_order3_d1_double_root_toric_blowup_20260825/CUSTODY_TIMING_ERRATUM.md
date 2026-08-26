# Custody timing erratum

Date: 2026-08-26  
Status: mandatory endpoint firewall; mathematical solver source unchanged

The frozen v1 worker launches

```text
/usr/bin/time -v /usr/bin/Singular ... > singular.stdout 2> singular.stderr
```

but later requires `singular.stderr` to be empty.  GNU time writes its own
23-line telemetry block to that stream, so a completed v1 solve necessarily
trips `SOLVE_FAILED` even when Singular has rc zero and emits no stderr.  No v1
endpoint is directly promotable.

`remote_worker_v2.sh` is the prospective wrapper repair: it sends telemetry
to `singular.time` and reserves `singular.stderr` for the CAS.  The long live
v1 solves need not be restarted solely for this wrapper defect.  After a v1
terminal, run `validate_v1_timing_stderr.py` on registered AWS with the exact
job/tag/encoding.  It fails closed unless:

- compile and solve hashes check;
- compiler and Singular rc are zero;
- compiler stderr is empty;
- stdout contains exactly one expected PASS and verdict and no FAIL;
- the mixed stderr is **exactly** the ordered 23-line GNU-time block for the
  selected immutable input, with exit status zero;
- parser negative controls reject an extra CAS line and a nonzero exit.

Only a unique AWS validator PASS permits consumers to reinterpret logical CAS
stderr as empty.  The validator does not alter the Singular result and does
not widen the toric chart scope.  Any unexpected line, missing line, source
change, signal, timeout, rc, or marker is `INCONCLUSIVE_SOFTWARE`.

