# ROOT FIRST — late capture source accepted; initial unit blocked

2026-09-13. Different-model review of Sol's source. CONDITIONAL STATIC
CONFIRMED for dispatch.py079f9ad7b92e64af5c5fc6a5e17de14ffa5245627ee5c8a4ce0ef2a018a2fa5d.
The initial science-unit template3bee708f82e06e77426ddd7bca9953ef84858b058d88f78c5bf25672a6e579eb
is GAP pending the two precise corrections below. No science/dummy/worker.

Sol first00:20:20.394704716, final idle00:25:40.878093386 UTC, before
original reserve00:31/HARD00:34. ROOT independently observed terminal state
before custody FIRST. Custodyfe0dd90ec96621eecbda6a2cd16548609715eb867175e459d9ad59e88e4fded7
matched, all six owned outputs and nine source inputs passed strict postpins.
WHOLE source, unit, DELTA, PINS, report, manifest and custody readback passed;
expected transaction verified report92e5b22e0ca038eb266cc065bf1fbd9133729377cc418c168523f7d22ea8df0a,
manifestc51fb085658a19beb7d9327f1861f0a35ec2e42373d1682724b44d372a78bdfa.

The dispatcher diff is exactly ten inserted lines after the original
registration, frozen-path/data and exact empty-directory checks, before any
dummy or science child. Both Python standard streams are flushed. Two new
files are opened exclusively/no-follow; both are forced0600 before dup2.
The temporary descriptors close in finally, including refusal of the second
open. There is no relaxed freshness check, changed phase, altered authority
schema, scientific code edit or cap increase. The root service starts with
both journal descriptors open, so temporary descriptors are distinct from
1 and2. No other process writes the directories during admission.

All normal later root/CAPRUN status output uses those files on the same
256MiB tmpfs. CAPRUN's scientific-child streams remain separately captured.
Early refusal or failure during redirection launches no scientific phase;
its original unit diagnostic/status must be retained. The exact [Python3.12
dup2 interface](https://docs.python.org/3.12/library/os.html#os.dup2) confirms
descriptor replacement and default inheritability. ROOT inspected actual
insertion/call ordering and the unchanged whole dispatcher, not a runtime
regression or new AST/test claim. Parent fsync, stream/census verification,
fresh host/native/limits and mandatory live dummy remain external obligations.

Two concrete unit issues, not general hardening:

1. The unit compares date-u ISO-Z strings lexically, yet passes the same
   deadline verbatim to systemd --on-calendar. On the actual HQ systemd255,
   the administrative, non-mutating query
   `systemd-analyze calendar --iterations=1 '2030-01-01T00:00:00Z'`
   returned exit1/Invalid argument; the space-separated
   `'2030-01-01 00:00:00 UTC'` form was accepted. This is an actual calendar
   parser test, NOT any scientific interpreter/syntax/test or worker run.
   Convert frozen instants to systemd calendar spelling before timer calls;
   retain equivalent absolute instants and original whole-job deadline.
   The future worker's actual version/date behavior still needs binding.
2. Successful transient units can already be unloaded after --wait releases
   its reference. Unconditionally requiring reset-failed success can then
   misclassify completed mathematics. Handle only the authenticated
   not-found/unloaded case, keep the actual numeric wait result, and retain
   the independently frozen expected cgroup path and genuine final kernel
   cgroup absence. Do not substitute blank ControlGroup or ignore errors
   from an existing nonterminal unit. This is a source/ordering diagnosis,
   not an observed science-unit failure.

The second issue is not permission to weaken cleanup. No template currently
proves actual root capability, burst-zero/cgroup facts, calendar arming,
terminal timing, durable custody or scalar success. Original source/template
copies stay frozen. One narrow operator correction is justified; no new
controller or wholesale runtime/algebra re-review is selected.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3993`.
- Body SHA-256:
  `f3f1d1ac60c423e4022fbe06bcd0f5aeed408f9f5e3af3ffecbe82d8a0b25ede`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
