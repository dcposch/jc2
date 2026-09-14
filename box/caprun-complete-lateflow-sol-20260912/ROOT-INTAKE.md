# ROOT terminal intake: v1 complete-flow claim fails source review

2026-09-12 04:03UTC. Native author independently COMPLETED before custody
FIRST. Custody50e4d67955895326c53866a85b14f4b57338bf5209049e622914e597ac441313
matched before WHOLE read. All44 listed source pins and six output pins
matched, as did report/transaction/PINS/POSTPINS. Report
d78a5bbc83c9c9483d54a871240a1bea37d6503364ede4e7d14a3ad5d71986ec,
manifest ec816484d0af00902325f784d0abc473124017c89cb938a043dd5b4622767200,
expected VERIFY passed. Report/manifest/CUSTODY/PINS/POSTPINS and all six
new artifacts freshly WHOLE-read as inert text. No execution or syntax test.

Disposition: RETAIN DISABLED / GAP, NOT complete-flow qualified or promoted.
The intended separation and DO_NOT_PREINSTALL correction are sound, but
the code has the following concrete defects beyond its two declared GAPs.

1. RECIPE.js:26 (also85--86,93--94) treats absent exit_code after a
   one-second observation yield as a terminal command failure. A returned
   session_id instead means the same command is still running. The recipe
   throws without preserving/polling that handle. Ordinary slow SSH or
   hashing can therefore fail the flow while an administrative process or
   holder remains live. Observation expiry must not imply terminal or restart.
2. RECIPE.js:105 joins checksum records using literal backslash-n characters;
   line106 uses printf %s, which does not translate those into newlines.
   The purported five-line remote checksum input is malformed. This is a
   direct source-string diagnosis, not a runtime experiment.
3. RECIPE.js:102's remote for-loop has no fail-fast shell setting or explicit
   exit. If an earlier target exists but the final native.sha256 does not,
   the last test succeeds and the whole loop can exit0. Subsequent scp can
   overwrite earlier stage targets. Preserve absent-target guarantees for
   EVERY target; exclusive-writer assumptions do not repair sequential logic.
4. RECIPE.js:30--31 validates the shape of freshly computed receipt/list
   digests, but does not compare them to the frozen expected hashes. Later
   observation values are embedded constants, not independent fresh reads
   of those bytes. Do not claim those lines authenticate expected contents
   or actual coordinator-timer liveness. A preholder manifest may cover
   some bytes, but its required complete membership is not specified here.
5. The historical prepare-leaves script needs holder PID/start/invocation
   values known only AFTER admission, yet RECIPE.js calls an already bound
   descendant immediately after admission without a concrete late binding
   step. release.template.sh similarly contains those late identities and
   the final registration hash. All sources cannot be fully substituted
   before holder as claimed. Freeze CODE before holder and define validated
   late DATA inputs; do not invent unknown identities or compose source live.
6. release.template.sh:29 can block opening the FIFO if its reader exits
   after liveness checks. It has no independent bounded open/write wrapper.
   SSH/scp calls also lack transport execution timeouts. Checking time before
   and after a blocking command is not bounding that command. Preserve the
   original holder/phase/worker clocks and exact process ownership.

Additional integration caution: streamed `bash -s` invokes scripts whose
placeholder guard greps "$0"; that is not the streamed script pathname.
Such a guard is not source authentication. ROOT must independently pin and
fully bind actual installed/streamed bytes before use. No runtime experiment
was performed to discover this source-level mismatch.

Manual negative scenarios above provide exact controls for any repair:
live session after1s; two checksum records; existing first stage target with
absent last target; changed receipt bytes; unknown pre-admission PID; and
reader disappearance just before FIFO open. They are not executed controls.
Do not send a confirm-only echo gate or allocate a worker on this v1 packet.
Existing accepted dispatcher/caller/binder/installer code remains unchanged;
defects are in the new orchestration and its completeness claim.

Timing correction: custody calls03:48:14.876921810 the first action, but the
transaction opened03:47:48. Report finalized03:58:59; all-writers-idle custody
03:59:06.382297155. Use the earlier observed transaction time as a lower
bound on task duration, not the inconsistent later first-action field.
Original fallback reserve04:04/HARD04:07 met; initial Astra task began
03:44:59.962985091 before the provider-capacity failure. No dollar/credit/
token/CPU inference from these wall times. Frozen author bytes unchanged.

No AWS/SSH/holder/runtime/probe/dummy/science or caller execution, no source
edit, cap increase, second holder or review launch by this intake. JC2 remains
unresolved. Root has collected all live work; no native/model job remains.
