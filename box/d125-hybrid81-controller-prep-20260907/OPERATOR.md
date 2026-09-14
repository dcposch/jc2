# Disabled operator checklist

Preparation only. No live authority, boot, GREEN, worker access or execution is
contained here. Root alone checks EC2 Owner, retained EBS, current mount/storage,
free resources, inherited workloads, accepted gate and current binary pins,
then decides START/deploy/engineering GREEN/STOP. Existing FSIZE, descendant and
long-print evidence is reused; do not rerun it by convention.

Future layout is exactly /home/ubuntu/d125-hybrid81-exact-solver-20260907 with
controller.py, unchanged engine/driver/exact/hybrid/run_capped at its root, and
engineering/{REGISTRATION.md,ROOT-GREEN.md,tiny-engine-fixture.jsonl}. Registration
is the unchanged parent-repair copy, SHA364a5d8c...; helper SHA8d8da939....
Opaque D.pins source strings are copied, but no control opens production source.

Future one-shot argv (DISABLED placeholders intentionally reject):

    /usr/bin/python3 -I -B controller.py hybrid --boot BOOT_PENDING --green-sha256 GREEN_PENDING --controller-sha256 CONTROLLER_PENDING --dispatch-before 0

Root must supply exact current boot, this controller digest, physical GREEN
digest and a worker-clock dispatch deadline no more than60 seconds ahead.
Controller must already be invoked in the registered cwd; it never chdirs or
creates the directory. It validates every code/fixture/binary and physical GREEN
before its first write. Both root authorization and custody are cooperative,
not same-UID security isolation. This script is new and still requires review.

One invocation dispatches ONE literal operation, under the exact unchanged
registered10-second CAPRUN vector, outer prlimit64MiBFSIZE/core0 and helper
512MiBAS. Authority starts at issuance and expires9.5 seconds later; driver's
flooring may shorten the hybrid timer. Alarm uses unchanged helper timer<=1s.
No solver authority, production phase, retry, changed support/order or cap raise.

For alarm, root separately accepts the sealed hybrid receipt and supplies
--accepted-hybrid-receipt SHA256. Same-boot accepted hybrid receipt and its hash
are required. A fresh matching physical engineering GREEN is an operator
prerequisite, not inferred from the hybrid result. Never overwrite spent tokens.

Controller waits for the exact live post-prlimit runner argv and a matching live
payload identity. A fast exit without required capture is GAP, even if the math
fixture happens to pass. Helper identity and CAPRUN start_identity remain the
authoritative child record. No live algebraic stdout is read. Terminal telemetry
is consumed before output; outputs/authority/script/identity are retained even
on GAP, normal/-O exact tiny replay runs only after a normal hybrid exit, and
actual alarm success requires ready marker, SIGALRM14 and wall<2s (not10s cap).
Tiny verifier subprocesses are synchronous, bounded and reaped; no descendants
or separate sessions. No shared runner changes.

Rare missing telemetry or a still-live runner is an explicit GAP needing root
custody; the controller does not kill an unvalidated group or retry. Root must
not STOP the worker until all relevant groups/writers are proven terminal.
Ordinary terminal receipt includes current group absence, pins and checks.
Launch/claim/receipt files are all exclusive, operation-specific and never reused.
