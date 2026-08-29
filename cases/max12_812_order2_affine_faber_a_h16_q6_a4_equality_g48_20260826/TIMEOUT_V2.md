# V2 timeout custody: `H=16,q=6,alpha=4` equality wall

Date: 2026-08-26

Status: **DUAL-AWS TIMEOUT; NO MATHEMATICAL VERDICT.**

The frozen V2 producer compiled successfully on exact `Q` and in the
characteristic-`65521` control lane, then both complete standard-basis runs
reached the registered 1800-second timeout before emitting any coefficient,
chart, or endpoint line.  Each stdout consists only of Singular's
post-timeout `halt 1`; each validator records

```text
engine_rc=124
validator=FAIL_ENGINE_OR_TIMEOUT
```

Telemetry was healthy but does not count as algebraic evidence:

```text
Box03 / exact Q:  30:00.60, max RSS 15,271,912 KiB, zero swaps.
r6d / F65521:     30:00.95, max RSS 18,563,120 KiB, zero swaps.
```

The exact-Q lane is the intended evidence characteristic and the finite-field
lane is only a software control, but neither returned a result.  Moreover V2
saturated only `D(p*m*x0)` and `D(p*m*y0)`, omitting the registered equality
open factors `a0` and `kk0`; even a survivor would therefore have been
ambiguous.  The localized V3 source, frozen separately, is controlling.

The copied immutable remote outputs are under `evidence_v2_timeout/` and are
listed byte-for-byte in `EVIDENCE_TIMEOUT_V2.sha256`.  This custody does not
establish a survivor, a unit ideal, rational regrading, source/Rees coverage,
order two, maximum twelve, or JC2.
