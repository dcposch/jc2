# Future ROOT-only execution interface — ALL MODES/TESTS UNEXECUTED

This document is not an authority, launch request, enabled JSON, scheduler
or CAPRUN rewrite. Retain the existing execution_gate.py, probe.py and
run_capped.py unchanged. The bridge and mutator are SOURCE ONLY.

## Fixed argv

Stage payload_exec.py, mutate_certificate.py, execution_gate.py,
produce.sing and check_certificate.py as regular nonsymlink siblings in
a ROOT-owned immutable source directory. Every argument below is a full
canonical absolute path; INPUT must occupy sys.argv[2] in the bridge.

    /usr/bin/python3 -I -B PAYLOAD_EXEC AUTHORITY INPUT MODE

- produce: INPUT is exactly the staged sibling produce.sing. Replacement:

      /usr/bin/Singular -q --no-rc --no-stdlib --no-tty --random=0 PRODUCE_SING

- check: INPUT is the actual independently collected pinned certificate.
  Replacement (fresh CLI; no direct check(raw) API):

      /usr/bin/python3 -I -B CHECK_CERTIFICATE INPUT

- mutate: INPUT is the pinned original certificate copied into the fresh
  registered cwd. ROOT must already have its independent positive checker
  receipt. Replacement:

      /usr/bin/python3 -I -B MUTATE_CERTIFICATE INPUT

No shell, arbitrary executable, fork, process-group change or second
supervisor. os.execv preserves the recorded CAPRUN child PID/PGID and
inherited caps. This is static intent; a live ROOT dummy is still required.
The Singular options disable automatic .singularrc/standard.lib startup,
avoid terminal adjustment and fix the random seed. --no-shell is NOT used:
the permitted pinned manual says it would disable the serializer's links.
No installed-version, typed-link, formatting or native-run claim follows.

## Existing authority form and exact CAPRUN parent binding

ROOT creates and pins the existing F10-R1-REGISTERED/v1 authority schema;
no authority artifact is supplied here. Its required fields are schema,
enabled (true ONLY after ROOT registration), job_tag, admissibility_sha256,
operation (the exact MODE), instance_id, hostname, runner_path, caps, cwd,
stdout_file, stderr_file, telemetry_file, child_argv, parent_argv and
file_sha256. All five caps below are their ROOT-approved string values.

child_argv is exactly the bridge argv above. parent_argv is exactly:

    /usr/bin/python3 -I -B RUN_CAPPED
      --wall-seconds WALL --cpu-seconds CPU --rss-bytes RSS
      --rss-sample-seconds SAMPLE --term-grace-seconds GRACE
      --cwd CWD --stdout-file STDOUT --stderr-file STDERR
      --telemetry-file TELEMETRY -- CHILD_ARGV...

The unchanged gate checks physical EC2 instance/vendor/hostname, flags,
FULL child/parent argv, cwd, registered caps and every file_sha256 entry.
The bridge hashes the gate BEFORE its metadata import, calls authorize
before any scientific payload, and binds its later authority reread to
the returned authority SHA256. Registration files and admitted inputs must
remain immutable with no concurrent writers through launch/collection;
this is not a new race-proof authority or installation framework.

Mandatory file_sha256 entries: canonical bridge, unchanged gate and runner;
selected fixed sibling payload; actual INPUT; /usr/bin/python3 and its
resolved target if different; /usr/bin/Singular and its resolved target
for produce; unchanged check_certificate.py ALSO for mutate. ROOT must add
the full admitted installed-native/library closure and any remaining
runtime inputs. Selected membership is checked explicitly, so unrelated
declared files cannot substitute for a missing payload/input/native pin.
The runner, gate, producer and checker accepted source hashes are fixed in
the bridge; new bridge/mutator hashes come from terminal custody and ROOT's
future exact registration. No current authority/native digest is invented.

## Outputs, pins and controls

Producer requires CWD/contact-eliminant.cert absent before exec. Mutate
requires INPUT.parent==CWD and BOTH contact-F-plus-one.cert and
contact-H4-plus-one.cert absent, including dangling symlinks. The mutator
also checks absence and uses exclusive creation; never overwrite.
After a failure one output may remain partial: fail the whole run and
collect it, not silently reuse it. No atomic-two-file claim is made.

Input, each mutation output and each checker input retain the 64MiB bound.
ROOT declares fresh directories and finite output/native file limits,
external wall/CPU/RSS/cleanup caps, and all native/source pins before launch.
Prospective outputs have no fictional precomputed hashes. ROOT collects
and hashes them, then creates separate fresh check authorities pinning the
EXACT original, F-plus-one and H4-plus-one bytes respectively. Each check
must launch the unchanged CLI under -I -B so the process-local digit setter
runs before parsing. Mutation environment SHA values only transport the
wrapper's admitted input/authority bindings; they are NOT an authority.

Mandatory pending regression: ROOT's existing five-refusal probe suite,
valid-authority POSTAUTHORIZE marker, and descendant-RSS/leader-exit/cleanup
dummy using the unchanged pinned probe and CAPRUN. Existing registered
cases are not replaced or purportedly run here; no fixture list outside
the charged scope was read. A failure must refuse/leave no postauthorize
marker as registered; valid/dummy evidence must be collected before any
new contact runtime. Exec identity and descendant cleanup remain live gates.

Future positive checker: status0, CHECK_OK and matching exact certificate
SHA. Future BOTH corruptions: status2 and CHECK_FAIL (F+1 residual1, or
zero-F refusal; H4+1 residual -I4=1-zcA nonzero). The mutator's stored marker
is only exact-delta/source-sameness evidence, not positive checking.
Omitted-I4/free-z control is DOCUMENTARY ONLY: remove z when discussing the
X-line in Q[V,W,X]; it is NOT a third production fixture/test.

ALL dispatches, probes, dummies, syntax/import/AST checks, native/version
invocations, mutations and checker tests remain UNEXECUTED. No F or source
closure has been obtained and no following lane or execution is authorized.
