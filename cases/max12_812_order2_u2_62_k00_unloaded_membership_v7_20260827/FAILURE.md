# Rejected V7 endpoint: unsupported Singular termination syntax

Date: 2026-08-27

Both frozen V7 lanes reached a raw membership decision and wrote residual
artifacts, but neither passed the external fail-closed validator.  The emitted
source ended with

```text
exit(0);
```

and the installed Singular reported ``exit(0) is undefined``.  This diagnostic
is explicitly forbidden by the validator.  The direct lane therefore stopped
at `engine_rc=0` without a validator pass, and the normalized lane did the
same.  Their raw nonzero residuals are quarantined as rejected evidence and
are not promoted as mathematical results.

This also corrects the earlier implementation assumption: neither coded
`quit(N)` nor `exit(N)` is a supported fail-closed termination mechanism in
this Singular build.  The repaired lane uses plain `quit;`; failure paths emit
an explicit failure marker before quitting, which the external validator
rejects.

The defect is in endpoint control flow, not in the frozen tail source or the
formulas emitted before the final line.  Nevertheless, under the registered
fail-closed policy there is no V7 membership verdict.
