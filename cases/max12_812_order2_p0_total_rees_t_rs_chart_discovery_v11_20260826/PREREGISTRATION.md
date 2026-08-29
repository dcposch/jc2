# Preregistration addendum: `T-rs` chart discovery V11

Date: 2026-08-26

Status: **FAIL-CLOSED SOFTWARE REPAIR OF V10. NO REES-CHART OR CAMPAIGN
VERDICT.**

V10's two grade-10 engines reached matching mathematical telemetry, but the
attempt is a software no-verdict for two independent reasons:

1. Singular 4.3.2 `sat` returned a one-entry list on this installation, while
   the script attempted to print `STot[2]` and `SZero[2]`. Singular emitted
   diagnostics and continued.
2. `ops/aws_exact_lane.sh` deliberately wraps engines in `/usr/bin/time -v`,
   whose normal resource report occupies the engine stderr file. The V10
   validator incorrectly required that file to be empty.

V11 imports the frozen V10 compiler byte-for-byte. It makes only these
changes to the generated script and validation contract:

- replace the invalid saturation-exponent accesses by checks/prints of the
  actual return-list lengths;
- accept a normal GNU-time resource report only when it contains exactly one
  timed command, reports exit status zero, and contains none of the registered
  failure tokens;
- rename run sentinels from V10 to V11 and pin both the prepatch and final
  script hashes.

All V10 source pins, exact-Q versus independently compiled F65521 comparison,
chart substitutions, prefix schedule, two saturation algorithms, ideal
membership tests, artifacts, and firewalls remain unchanged. No V10
mathematical telemetry is imported as an expected outcome. Equality or
inequality remains acceptable if the repaired computation proves it.
