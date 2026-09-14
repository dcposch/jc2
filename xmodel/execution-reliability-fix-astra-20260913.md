# Execution pilot: bounded correction after Sol FIRST

Astra; September13,2026. IMPLEMENTED / MANUAL-STATIC-READ /
RUNTIME-UNTESTED. This is a corrective source slice for independent delta
FIRST, not permission to launch a worker or use it for mathematics.

## Preserved basis and decisive finding

First actual clock04:54:53UTC; original reserve05:14/HARD05:17, ROOT
collector, unchanged. I whole-read Sol's terminal FIRST, SHA
e9d078786c5bfe513dea86ab23942a638629ca8053d9d4ed4650e33594e31bc1,
whose report/manifest/custody pins ROOT had collected and I reproduced.
Its admission-tee finding is valid: a child job's terminal cgroup did not
cover separate asynchronous log writers in the caller's cgroup. The old
pilot was therefore not ready for runtime qualification.

Before editing, I copied all four reviewed source/document versions into
`box/execution-reliability-fix-astra-20260913/reviewed/`, made those copies
readonly0444, compared complete bytes and reproduced their old hashes.
The old reports, PINS and TEST-PLAN were not edited. Old PINS intentionally
describe historical source versions; the exact reviewed copies now preserve
those bytes while the four announced canonical source paths change.

## Corrections implemented

1. **Admission/collection race.** `start` takes `lifecycle.lock` before
   publishing minimal identity metadata or redirecting its logs. Both streams
   go directly to files. The descriptor remains held through the last write
   and final filesystem flush, with no explicit early unlock. `collect`
   acquires that same lock nonblocking before checking terminal manager state
   and absent cgroup, then holds it through archive/hash publication. Busy
   admission or collection is an explicit exit70 refusal. The test driver
   also uses direct logs, eliminating its unnecessary tee processes.

2. **Source authority.** Start now requires an expected runner SHA in
   addition to the manifest SHA. Runner, manifest and each payload file must
   be canonical, nonsymlink, root-owned0444, below actual root-owned ancestors
   with no group/other write bits. The runner's copied privileged-hook bytes
   are checked against the same expected SHA. The external test plan also
   names exact installed paths, hashes and ancestry observations. These are
   trusted-root invariants, not protection against a hostile root operator.

3. **Effective identity and FSIZE.** Before phase1, the source now compares
   all four real/effective/saved/fs UID and GID fields to65534. A tokenized
   single `Max file size` row must contain the exact requested soft/hard byte
   limits and units; padding is irrelevant. Manager status adds LimitFSIZE,
   User and Group. Existing capability/NNP/cgroup/CPU/memory/task gates remain.

4. **Causal negative controls.** Every refusal fixture saves its actual exit,
   requires70 and its exact `JC2-JOB ERROR:` line, and checks expected
   absent/admitted/unchanged directory state, MainPID0 and absent exact cgroup.
   Post-admission errors are checked in their actual durable admission.stderr,
   not assumed to be mirrored to the caller. Unrelated failures cannot satisfy
   the intended controls. The failed-collection case now requires153 and the
   C-locale file-size-limit diagnostic, rather than any nonzero exit.

5. **Two added discriminators.** A fast-terminal job is given a controlled
   admission-log writer holding the same lifecycle lock. Collection must
   refuse while it lives; after explicit FIFO release and actual writer wait,
   the archive's admission log must equal the complete final file. This is a
   controlled lock test, not a claimed real-world race occurrence. A new
   expected17 phase records17, then must release its successful successor and
   final batch0. The existing unexpected17 case must still block its successor.

The API remains one admission followed by read-only status and idempotent
collection. No model-timed interfaces, controller framework, EC2 action,
process-name kill, automatic retry or scientific caller migration was added.

## Verification and remaining gates

The four changed files and fresh TEST-PLAN were read back wholly, and the
exact delta was inspected. Explicit no-index Git whitespace checks are only
text checks; their ordinary difference exit1 is not a runtime failure or test
success. All initial report/policy/legacy-code inputs and reviewed snapshots
remain hash-identical. New source hashes are in fresh PINS.sha256. No source,
schema, Bash syntax, interpreter/import, dummy or CAS execution took place;
there was no AWS API/SSH, external model, extra agent or network action.

The corrected plan keeps one c7i.large/equivalent,10-minute root driver,
independent <=30second child active intervals plus <=10seconds cleanup/receipt,
256MiB, CPU80%, Tasks32, zero swap and FSIZE8MiB. Nine literal suffixes replace
eight because `expected` is now a genuine additional control. Original job
limits were not raised. ROOT still owns original absolute worker retirement,
retained EBS and verified archive transfer; all filesystem paths and finite
unit names are in the fresh TEST-PLAN.

Actual systemd/kernel identity, limits, post-stop behavior, descendant cleanup,
refusal causality, collection recovery and log ownership remain UNRUN. So do
SSH-disconnect, power-loss and OOM experiments; the suite does not claim them.
Per-file limits still do not provide aggregate disk quota. Native/library
completeness and mathematical source fidelity remain route-specific. The
pilot has not become a hostile-code sandbox, a scientific qualification or
a proof of JC2. The next action is ROOT's independent delta FIRST, followed
by at most one explicitly registered worker regression if that gate permits.

## Custody

Only the four announced source paths, this new transactional report and its
own box metadata/snapshots were written. Legacy user-dirty fleet.sh and
dispatch.sh, shared campaign ledgers, protected workloads, mathematical
sources, old reports and evidence were untouched. COORDINATION and FLEET
match their initial current pins; no policy transition occurred in this slice.
All source/report writers cease before the terminal handoff; ROOT must confirm
agent completion before custody-first intake. No worker or process handle is
left running by this lane.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6316`.
- Body SHA-256:
  `ed85cd22f473ee9a243bb3966d07797d3a3210d31bc5f8b7c467874a2ffa4159`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
