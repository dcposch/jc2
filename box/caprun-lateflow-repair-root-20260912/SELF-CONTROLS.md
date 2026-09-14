# Documentary controls; not executed regressions

ROOT2026-09-12. No new source, shell helper, mock, syntax/AST test, scientific
operation, SSH or AWS command was executed. These are manual source traces,
not evidence of runtime behavior or readiness. Whole-flow status remains GAP.

1. **Running session.** For a hypothetical exec response `{session_id:73,
   output:"a"}` without an exit code, the kernel stores73 and LIVE and calls
   write_stdin73. A second such response is still live, not a second exec.
   Terminal `{exit_code:0,output:"b"}` stores TERMINAL; only a completion
   before the original cutoff returns ordinary output. A polling exception
   retains73 with OBSERVATION_ERROR_HANDLE_RETAINED. A launch exception
   without a known handle retains UNKNOWN and disallows relaunch under the
   same key. Deadline expiry preserves73. A separate resume+collectOnly
   polls73 after deadline and returns COLLECTED_NO_SUCCESSOR on terminal.
   Distinct-key/no-concurrent-ROOT discipline remains an external invariant;
   these session-local stores are not a durable cross-process scheduler.
2. **Checksum framing.** The source separator is JS `"\n"`, not `"\\n"`.
   A two-entry map emits two LF-terminated records. Direct hash readback
   additionally rejects missing final LF, duplicate paths, a missing row,
   unexpected path, and any unequal digest. It compares raw hash metadata,
   never scientific coefficient payloads.
3. **No clobber.** In receiver --preflight, the first occupied or symlink
   target causes set-e failure inside the loop, even if the final target is
   absent. Each actual write then uses dd conv=excl and oflag=nofollow.
   A race creating a target between observation and open therefore fails
   exclusive creation. Earlier successful new files remain if a later
   transfer fails; this is not an atomic five-file transaction. A trusted,
   stable, root-owned parent and no concurrent ROOT writer are required.
4. **Authentication.** jc2HashReadback compares each observed digest with
   frozen expected bytes; two different well-shaped hashes do not pass.
   jc2ExactProperties rejects a timer ActiveState change, changed service
   ExecStart, missing key, duplicate key or added key when those properties
   are in the expected map. It does NOT choose or query the required units
   or ensure the expected map covers them. That wiring is still GAP.
5. **Late data.** jc2HolderData extracts the unique actual PID/invocation,
   exact ADMITTED_NOT_RELEASED marker and field22 start ticks from raw
   proc stat (field3 is tail index0; field22 is index19). Last closing
   parenthesis tolerates a space/parenthesis in comm. PID/start are restricted
   decimal metadata; PID<2^31 and at most15-digit start ticks. Script text is
   not rewritten. HOWEVER no fixed leaf+observer or complete authenticated
   release consumer is composed here, so the original late-binding defect
   is only partly addressed, not claimed resolved end-to-end.
6. **Blocking.** jc2Admin wraps the exact administrator argv in timeout
   --foreground TERM plus1-second KILL escalation. SSH also has connect and
   liveness options. FIFO redirect occurs INSIDE the 2-second timed bash,
   not in the parent. A dead reader therefore cannot block the untimed
   parent's FIFO open. Required remote transport/writer bounding is not
   yet composed. No hard real-time claim against uninterruptible kernel
   I/O; original independent holder/phase/worker caps remain mandatory.

Self-review corrected two additional draft issues before freeze: initially
expired handles could not be collected by the same helper; collectOnly now
allows observation without authorizing a successor. Admission marker is now
unique and exact after reading the pinned admission tail. Neither edit was
validated by running the new code. Separate model review remains required.

## Exact remaining integration gaps

- GAP[FIXED-LATE-CONSUMERS]: complete fixed leaf/observer and authenticated
  release consumers preserving all historical identity, namespace, ownership,
  empty-cgroup, original-clock and no-writer checks.
- GAP[CONCRETE-COMPOSITION]: explicit separate ADMIT/ATTEST/INSTALL/RELEASE
  entry points, actual receipt/list authentication, exact fresh retirement
  timer/service queries, five bounded exclusive transfers with readback,
  unchanged six-argument caller and installer. No inferred phase from files.
- GAP[BOUND-QUALIFICATION]: exact preholder source/native inventory including
  new dependencies, bound packet, different-model review and scoped controls.
- GAP[LIVE-LATENCY]: complete actual120-second sequence never measured; old
  caller-only365ms does not cover this flow. No worker run authorized here.

No published v1 artifact or accepted scientific/dispatcher/caller/binder/
installer source was modified. Nine authority files remain documentary
expected runtime outputs and must not be preinstalled.
