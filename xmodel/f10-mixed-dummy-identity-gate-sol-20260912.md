# DELTA FIRST: mixed dummy identity attachment

Status: **CONDITIONAL SOURCE CONFIRMED / UNEXECUTED**. First action
`2026-09-12T20:44:26.202565694Z`. This review creates no worker, observer,
dummy evidence, runtime qualification, authority, science run or result.

## Exact source delta

The old probe's CLI check, single fork, immediate parent `_exit(0)`, child
SIGTERM ignore, 64MiB allocation, every-4096-byte page touch, readiness marker,
and infinite sleep are preserved. The delta imports stdlib `json` and `Path`,
then after all pages are touched and before the marker reads three proc facts
and constructs one bounded identity object. Its sole write is now the original
`DESCENDANT_READY\n` followed by canonical compact sort-key JSON and one final
newline.

The object has exact keys `schema,status,pid,pgid,start_ticks,boot_id,
pid_namespace,cgroup,payload_bytes`. Schema/status are fixed; PID, PGID,
start ticks and payload size are decimal strings; boot, namespace and cgroup
are captured by the child itself. Payload is exactly `67108864` bytes by source
construction. No scientific input or output is introduced.

## Parsing and ordering review

Linux `/proc/self/stat` fields following the final `)` begin with field3
(`state`). Therefore list index19 is field22, `starttime`; `rfind(")") + 2`
correctly removes the parenthesized `comm` even when it contains an earlier
right parenthesis. A malformed/short stat line raises before output, so it
cannot form valid readiness evidence.

`/proc/self/cgroup` is retained with its terminal LF and any internal LFs.
`json.dumps` escapes those characters inside the JSON string; appending one
literal LF leaves exactly two physical stdout lines. Default ASCII-safe JSON,
compact separators and sorted keys give an exact-text target. Metadata reads
and JSON construction occur after page touching, and the marker is emitted
only in the combined final write. A failed proc read, encoding failure, partial
write, cap before write, absent text, malformed JSON, extra line or wrong key/
value is STOP at intake. The source does not check `os.write`'s return count;
therefore ROOT must require the exact complete bytes rather than infer success
from process survival or CAPRUN's resource-cap status.

## Required consumption boundary

The accepted dispatcher intentionally remains byte-unchanged and does not
parse dummy stdout. ROOT must independently read it after CAPRUN termination
and require exactly the marker plus one canonical JSON line; exact keyset,
schema/status and `payload_bytes="67108864"`; positive decimal child PID/PGID/
start_ticks; expected boot ID, PID namespace and exact service cgroup text.
The forked child PID must differ from the exited leader while its PGID binds to
CAPRUN's recorded target group/leader identity. ROOT must also bind the new
probe digest in registration, native/source records and installed postpins.

That self-reported record is reviewed source evidence, not an independent
kernel observation. ROOT still must correlate CAPRUN leader/group and max-group
RSS telemetry, identity-matched TERM/KILL/reaping, service-cgroup membership,
and finally prove actual kernel cgroup emptiness after cleanup. Missing or
inconsistent metadata cannot be repaired by the old marker or telemetry alone.
No separate observer is added.

## Verdict and remaining gates

**CONDITIONAL SOURCE CONFIRMED.** I find no blocking source mismatch in the
identity attachment or its stated consumption boundary. It closes the missing
child identity/readiness data channel only when ROOT performs the exact
external comparisons above. It does not establish kernel quiescence, no
escape, RSS semantics, package/native/import closure, metadata fit, immutable
ancestry, current host facts, resource limits, runtime success or science
permission. All prior cgroup, absolute-clock, output, cleanup, custody and
retirement predicates remain mandatory.

Fresh WHOLE reads covered all eight inputs in
`box/f10-mixed-dummy-identity-gate-sol-20260912/PINS.json`; final WHOLE readback
covers PINS, report and manifest. Strict postpins precede terminal custody. No
interpreter, import, AST, syntax, compile, test, dummy, CAS, network, AWS,
protected-tree access, repair or source edit occurred.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4271`.
- Body SHA-256:
  `0235d63d278eeef74b6c3ac47ef24003beab38eaa2c684b57bdcf2a1686f066a`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
