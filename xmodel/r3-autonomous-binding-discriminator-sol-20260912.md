# R3 autonomous late-binding discriminator

Status: `DESIGN-POSSIBLE / SOURCE-SCHEMA-ONLY / UNREVIEWED / DISABLED`.
This is a manual static conclusion, not a whole-dispatcher audit, runtime
qualification, registration, launch authority, or scientific result.

## Verdict

The literal `authority.py` schema does **not** require a human to serialize
late observations during a 120-second holder interval. Its workload-facing
inputs are an authority pathname and SHA-256 on argv. The authority object
contains fixed job/mode/limit/source/place data, an artifact path/state, and
interpreter/native-inventory pins. It contains no holder PID, startticks,
namespace, cgroup, leaf identity, release token, wall-clock timestamp, or
human-attestation field. Thus human participation is a deployment dependency
of the failed batch-c workflow, not a requirement of this source schema.

A logical replacement is available: one separately reviewed, immutable,
ROOT-owned **admission supervisor** performs the already-required late
observations, writes/freeze-authenticates the final ROOT documents, and starts
the already-fixed dispatcher only after all predicates pass. It does not
alter the scientific five-file inventory, source authority schema, workload,
caps, or trust model. Whether the uncharged dispatcher and deployment
templates accept this handoff remains `GAP[DISPATCHER-INTERFACE]`; quantity:
decide whether their literal argv/file-state contract admits the frozen
handoff below. Cheapest test: different-model static review of those exact
sources, expected under one lane-hour, before any host is selected.

## Minimal deterministic handoff

The supervisor is fixed reviewed code running as trusted exclusive ROOT. Its
only input is a prelaunch, canonical, hash-pinned constants bundle. Before
launch that bundle can know: batch/job tag; disabled/enabled policy chosen by
ROOT; five scientific source bytes and destinations; fixed unprivileged UID/
GID and argv shape; ordinary interpreter requirement; source, contract and
place pins; exact wall/CPU/memory/output caps; output path; canonical admin,
native-inventory, registration and authority paths; permitted host/namespace/
cgroup topology predicates; and an absolute admission deadline plus outer
retirement deadline. Physical values are not guessed or templated.

After the supervisor creates the holder under the predeclared outer cap and
closed-child cgroup topology, it obtains directly from kernel-owned interfaces:
the actual boot/host identity, holder PID and startticks, invocation identity,
PID/mount/user namespaces, cgroup membership and identity, empty owned-leaf
identities, interpreter bytes, and complete native closure. It also confirms
the fixed installed-source pins and required empty/output state. These are
late observations. The trusted ROOT supervisor authenticates them by reading
the kernel/filesystem objects itself, checking them against the frozen
predicates, and emitting deterministic ROOT registration/attestation bytes
with exclusive creation, canonical paths, fsync, readback, SHA-256, and
read-only freeze. No JSON file, holder, workload, or helper self-authorizes.

Only then does the same supervisor invoke the fixed dispatcher with the
resulting immutable path/hash tuple. The 120-second timer and independent
outer retirement remain armed from the original holder start; every step
checks the monotonic/absolute deadline and any timeout refuses dispatch.
There is one attempt: no second holder, retry, cap increase, or clock reset.
Dispatch remains unprivileged; output/native/source pin custody, independent
outer caps, identity-validated TERM/KILL, kernel-closed child scope, and strict
no-CAS descendant/RSS/cleanup checks remain mandatory. Release, if the
uncharged contract requires one, is a later explicit ROOT policy action and
is not minted by the helper or implied by successful binding.

The deterministic state transition is:

`FROZEN_EARLY -> HOLDER_STARTED -> LATE_OBSERVED -> ROOT_ATTESTED -> FROZEN_FINAL -> DISPATCH_ELIGIBLE`

Any mismatch or deadline yields terminal `REFUSED` and outer retirement,
never `DISPATCH_ELIGIBLE`. This removes human latency, not any predicate.

## Cycles and authority boundary

There is no authority-file self-hash cycle: deterministic final bytes are
formed first, then hashed, and only their path/hash are placed on the later
workload argv. There is no workload-PID cycle because the holder/supervisor is
the process observed before the unprivileged workload child exists. A holder
invocation digest may cover a stable bootstrap argv containing canonical
future paths, but must not cover the not-yet-known final authority digest.
If the uncharged dispatcher instead requires that digest inside the holder's
own already-executed argv, that is a real cyclic interface and the design
fails pending a reviewed split between bootstrap identity and dispatched
child authority. This is included in `GAP[DISPATCHER-INTERFACE]`, not assumed
away.

Likewise, the source does not establish how PID reuse is excluded or how the
holder is retained while files are frozen. The deployment must hold a pidfd
or equivalent identity-stable kernel reference and compare PID/startticks/
cgroup identity immediately before dispatch. This is a required design
predicate, not a claim that current uncharged code implements it.

## First decisive qualification and controls

The first executable test is a separately authorized, fresh AWS, **no-CAS**
qualification of the reviewed supervisor plus exact dispatcher/runner: use a
fixed finite unprivileged probe in the real cgroup topology; require automatic
late observation, byte-identical deterministic attestation/readback, dispatch
inside the unchanged 120 seconds without an operator call, complete descendant
RSS accounting, and identity-validated cleanup leaving no nonzombie child or
orphan. This report did not run that test.

Mandatory negative controls are: alter one captured starttick/cgroup identity
and require refusal; introduce an unexpected descendant and require the
closed-child/no-CAS gate to fail; withhold one late observation and require no
authority/dispatch; and force binding past the original deadline and require
outer retirement with no retry. The historical exact-PGID runner's
false-empty observation disqualifies it as fallback.

Expected information gain is high and binary: a pass establishes that human
serialization, rather than safety checking, was the measured timing
dependency; any false-empty, identity drift, incomplete native closure,
deadline escape, orphan, or need to change source/caps stops the redesign.
Strict stop condition: stop after the first failed predicate or one complete
positive-plus-negative-control qualification; do not launch science or repeat
unchanged. Different-model static review of the supervisor and full charged
dispatcher/runner contract precedes this executable test.

## Evidence, clocks, and limits

First action: `2026-09-12T15:46:18.236269646Z`. Design observation checkpoint:
`2026-09-12T15:47:47.927291414Z`. Original publication reserve
`2026-09-12T15:57:00Z`; HARD `2026-09-12T16:00:00Z`; neither was reset.
Basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.

Exactly four inputs were SHA-256-pinned before fresh WHOLE reads: 806-line
`COORDINATION.md`; 82-line task; 133-line `authority.py`; and 134-line
historical batch-c result. Their pins and byte counts are in the owned
`PINS.json`. No linked source, scientific/runtime report, dispatcher, runner,
peer output, network, worker, protected tree, source execution, helper test,
or external state was consumed. The historical result establishes only its
reported UTF-8/human-latency failure and CLOSED disposition; it is no current
physical evidence. All r3 rows/rank remain unrun.

Claim scope: source-schema and deployment-design discriminator only.
Lifecycle: `INTERNAL-UNREVIEWED`. The design is disabled and unbound; ROOT
owns any later source review, registration, host selection, test, or release.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8030`.
- Body SHA-256:
  `e4072504e04f8b46a8ae2800a466276afc445758911b2845a981d81fb34a1043`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
