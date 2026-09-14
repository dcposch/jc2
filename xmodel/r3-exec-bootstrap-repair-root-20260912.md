# ROOT bootstrap repair — STATIC / UNEXECUTED

Basis: 0d39df3c9fd69c939a8420c54d03228b9077777d. Author ROOT, September12.
This is one bounded immutable-copy repair following the first independent
actual-code review. It is INTERNAL-UNREVIEWED engineering, not runtime or
mathematical evidence. No program, import, parser, syntax check, test, dummy,
scientific job, worker or enabled specification was executed or issued.

## Exact inputs and new artifacts

- Parent bootstrap box/r3-exec-bootstrap-astra-20260912/bootstrap.py:
  fb37ce50c4acee5f1fd2495dda476fee5d38b63a4d88a04440a9db8e3c4697b8.
- Parent contract in that directory:
  6d764e0060238b3bb4d1799a4cd1904fdd4d6f756f7ba0ff7e4c678f0e9b13c5.
- Fable FIRST xmodel/r3-exec-bootstrap-gate-fable5-20260912.md:
  4f17271e788aae8ae489ba03e80b508c4a5d01d9496f4c03a48a4cf5e39004a3.
- Binding ROOT intake box/r3-exec-bootstrap-gate-fable5-20260912/INTAKE.md:
  7e581d2c276743ae89eea0c8b63782b0b5b68d48ab890647bba5e3992837b775.
- New box/r3-exec-bootstrap-repair-root-20260912/bootstrap.py:
  f04f1b7b16bed194e5d7b503a78fe9bd36e3bd58da3696adf6a40bfdbdcd17d2.
- New CONTRACT.md in that directory:
  21c1c0bd6840ac7aa80a33e9ff2c7a88bab87f51fd7a669ed6e27ba30b32bfeb.

Both new files are0444, WHOLE read back before this report. Old files are
preserved unchanged. A literal unified diff was reread during ROOT intake;
new code has517lines, exactly four insertions and no deletions.

## Four source changes and their boundaries

1. Require binding_deadline_utc <= original outer_started_utc+120seconds
   AND task_deadline_utc <= original outer_started_utc+3000seconds before
   creation. The task bound includes terminal custody, not just mathematics.
   The unchanged dispatcher restarts its internal elapsed counter at exec.
   A genuine externally bound start and independently qualified monotonic
   supervisor remain necessary; these UTC comparisons are not hard realtime.
2. Reject registration_path.parent in native.directories during audit_static,
   before the first creation, and retain later repeated static checks.
3. Require fd0 to match the actual /dev/null character device by type,
   device/inode/rdev and /proc/self/fd/0 path during each outputs check,
   including before creation. Existing bounded fd1/2 and closure of fd>=3
   before exec remain unchanged.
4. Set umask022 once at run entry before creating fresh leaves. Actual
   mode/owner/ACL checks remain load-bearing. No exact platform-specific
   cgroupfs effect of an inherited077umask is asserted.

There are no changed imports, schema keys, authority bytes, nine command
vectors, native/source pins, dispatcher or guard profiles; no child, retry,
cleanup or cap increase. The64KiB ASCII kernel-read ceiling remains fixed.
A qualified host must demonstrate compatible snapshot sizes or STOP.

## Review intake and next discriminator

Import the predecessor FIRST only at the ROOT intake's narrowed scope:
static nine-command interface and same-process design, not installed
readiness. Its source-visible deadline concern is accepted. Unsupported
PEP538/platform-version/native-library-subset particulars, a blanket execve
refusal fixture and exact restrictive-umask outcomes are not imported.

One focused different-model DELTA FIRST should examine these actual changed
bytes, preserve the predecessor interface, and attack the new early checks.
No fresh re-review of unchanged old runner foundations is requested. No
control has been executed. After that gate, actual launcher/native/host/
watchdog qualification is still required before any AWS-only observation;
the report itself authorizes none. All old a/b/c/d batches remain CLOSED.

The contract lists static negative controls: overlong original binding/task
deadlines, non-null stdin, native-inventory registration parent, and inherited
restrictive umask. Positive mode compatibility, bounded I/O, failure recovery
and eventual nine-phase execution remain unmeasured. Genuine r3 rows and
297rank remain UNRUN; this repair resolves no mathematical gap or JC2 case.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4066`.
- Body SHA-256:
  `f35bd5d496493e4f5f7e8d4a323b7d20bd6b052d046de490b916e07d5b652b50`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
