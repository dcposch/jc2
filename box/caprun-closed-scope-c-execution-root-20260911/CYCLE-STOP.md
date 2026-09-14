# Batch c CLOSED — no release, no preflight phase, no science

ROOT stop decision16:10:32UTC September11. Holder admitted16:08:04--05,
PID32315/start81252/invocation5fa4785de938458e8cc6125550a25385.
Nine actual leaves were captured16:08:32.100071960. The original120second
holder ceiling expired before ROOT finished candidate handling/readback.
No final installation or FIFO write was attempted, and no dispatcher ran.
The16:11:10 independent observation records MainPID0/ControlPID0,
failed exit2 at16:10:05, original/proc/32315 absent, exact cgroup absent,
final-registration path absent and only the waiting/STOP outer streams.

The accepted pure-data binder itself returned candidate documents. ROOT's
first output transport erroneously decoded all returned documents as ASCII;
the execution card contains an ordinary UTF-8 em dash, so transport failed
after bind returned, before any file write. ROOT then repeated the same
metadata-only call with UTF-8 transport. No helper/source/runtime byte changed,
no holder was restarted, and no clock or cap was reset. The candidate write
completed after the holder deadline and was therefore never installed.
This is ROOT orchestration latency/failure, not a mathematical result or
evidence of a source/CAPRUN defect. The UTF-8 handling should have been fully
prepared before admission; the changed helper did not eliminate this gap.

Candidate enabled flags/card wording remain attached to SUMMARY.json's
CANDIDATE_NOT_INSTALLED_NOT_RELEASED state. Actual identities refer only to
their captured instant, not present liveness or a late release entitlement.
No complete final registration human-WHOLE read or operational qualification
is claimed: only card/installer readback finished before the stop decision.

This cycle's engineering allocation is CLOSED. No automatic retry, new
worker, holder replacement, broader serializer/framework, cap increase or
science run follows. Both batch-b and batch-c sequencing attempts failed to
reach a phase; the current coordinator-mediated120second mechanism needs
reconsideration before any further expenditure. A new plan is not selected
by this closeout, and changing metadata names is not a redesign.

Original worker TERM/KILL timers were inspected at16:12:07 and stopped
16:12:50 only after confirmed terminal state. Retained worker archive is
630637bytes, SHAf49ca15aedf5efd633859baafe74c9f787695f93c05e66c0a42b3ef432e0ff35,
both on retained EBS and downloaded into
box/caprun-closed-scope-c-archive-root-20260911.xT1s5Y/worker-evidence.tar.gz.
Remote tar comparison and fsync, local SHA match and fsync passed.
Sixteen installed pins plus1226 native pins were rechecked after termination
of the holder. The EC2 worker itself awaits immediate retirement after the
coordinator-side evidence snapshot is also secured. No mathematical outcome.
