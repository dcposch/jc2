# D43 finite source high-Hensel v3 repair report

Date: 2026-08-28  
Producer: GPT-5.6 Sol, schema-v3 repair role  
Status: **repair packet sealed; independent hostile rereview required; AWS and p3+ remain blocked**

## Decision

The v3 packet closes each launch blocker charged by the sealed schema-v2
hostile review (`e12490ff6d117c8c6baa0a6ce925aa2da291dbb165d2016c8211a8a48b4f4f8b`)
at the implementation and preregistration level.  It is not self-authorized:
the immutable preregistration permanently says `V3_REVIEW_FROZEN_NO_AWS_LAUNCH`.
No AWS instance was launched, no p3+ digit was attempted, and the producer did
not rerun the real D43/NumPy reconstruction locally.

This report deliberately does **not** call the route “launch ready” or
“implementation complete.”  It is a sealed review candidate.  A real pinned
Linux runtime, root-owned systemd unit, live EC2 identity/tag, independent PASS
report, and prospective run paths necessarily exist only after rereview and
must independently satisfy the executable gates before N16 can begin.

## Sealed artifacts

Packet directory:
`cases/d43_source_high_hensel_v3_20260828/`

| Artifact | SHA-256 |
|---|---|
| source seal manifest | `76fbd4f0c723ecafe7030fc9ba0186478cdcffb2678f3d0fe868a67a500b43bc` |
| executable/data payload manifest | `8a859fc8cdc3001c15bd762e4ffd759eaf0372e16c8a3dbcbf36ed00bf769664` |
| immutable preregistration | `091a6ee2ffeed389b9fcd96ec8c82e01fcdeeb26582e05c690ff6ae50e5f2dab` |
| v3 runner | `f48a113083ecd8a3eb8646e58cd1b7fb7c51665669a88839f81a4da43d858438` |
| v3 AWS supervisor | `c210d6b2287da7ac73209801be3d648fab69990dee7434187527d11f2a24311c` |
| v3 worker | `e18a7fc0ade3603d493f736a7f9fbe4457e0601a294dccc53e7dc509dbd264a2` |
| bounded hostile tests | `ef9479b3ed36a83ea983d963db60f373f8a3f4dd358f02176fe6b9dd0643a581` |
| read-only postreview preflight | `701ffa43dd1c5398211694254073e085b03cc8268b49ba0daf3baa6aa6acff38` |
| authorization template (inactive) | `5ae752c5fc431a6a363ea23dfc3ae05aa96c1f6db9e8a07d18fcd9468ee65d8c` |
| corrected real-fixture preregistration | `644b453f9fba6505e08ff69e768c886e3bb16c74c7c6f263fe50bfd0e8dfa8b4` |
| systemd unit template (inactive) | `a750521ab4fe49f70aa1d4bc3b7c17f267550cd8ad5b77ce3b1ecf56a5a03d20` |

Both manifests replayed exactly at seal time.  The payload contains 38 hashed
entries.  The payload manifest and preregistration are separately hash-bound
metadata and are copied into the private execution tree by the supervisor;
they are intentionally not members of their own hash set, avoiding a circular
self-hash.  The deterministic source archive includes both plus the later
independent PASS report and is itself precomputed and externally authorized.

## Exact mathematical scope

Nothing in v3 broadens the schema-v2 arithmetic claim.  The system is the
finite raw 184-row pristine Euler/J-source truncation at `p=105337` on the
registered residue-A, `B=84`, a00pp frame.  The nominal 190 coordinates decompose
as 180 tails, eight fixed coordinates, and `alpha,beta`.  The eight dense-family
columns `tf1/tf2/tg1/tg2` at `r=39,41` are structurally absent from every
selected even band through 42 and are literal zero Jacobian columns.  The
essential ambient is exactly 172 tails + 8 fixed + 2 x-side = 182.  The exact
source rank is 129, with 53 tangent-kernel and 55 left-cokernel dimensions.

At every committed finite digit, v3 replays all 184 source rows, the five
coefficient radical equations, the `HW_i=hW_i` collapse, literal `uf30=0`, the
necessary E relation and W units, the literal corrected-243 E5 pair with common
deterministic `HM`, and E6 with deterministic nonzero `s1F`.  The p2 E/W/E5/E6
gate remains the committed digest
`39702f29d6e1a0b6f45864eca343b555620b41d8cb747b60bca057b3799804e3`.

On the registered localized radical/chart coefficient ring, the E5 pair with
existential common HM and E6 with existential nonzero s1F eliminate to E=0 and
`W1W2 != 0`; this is set-theoretically equivalent over C.  Over an unlocalized
ring where the displayed denominators are not units the existential equations
can be stronger.  The 184 source rows are not asserted to force E, so E-gate
failure is a separate finite terminal outcome, not branch evidence.

The x-side slot-42 formula is an exact support identity: `U_f,U_g` first differ
at slot 42, all cross terms at that output see only the slot-zero y constants,
positive y slots overshoot, `alpha*beta` starts at 84, and lower bands do not
change.  The preserved arithmetic context contains the independent basis and
perturbed-y operator controls.

The diagnostic does not replay the 34 parked constraints, inverse-variable
rows, template/D25 reconstruction, or reducer identities.  Its exact forbidden
claims include parked/source equivalence, a full residue-A/template/D25 point,
branch survival, indefinite lifting/formal smoothness, a Z_p or characteristic-
zero point, a formal germ, an ambient Keller map, and a JC2 counterexample.

## Blocker-by-blocker repair

### 1. Omitted core23 and executable closure

`cases/directionb_core23_p105337.ms` is now a literal payload member with SHA
`0533787f6bf89ff25478f01ddad40230a11f6a19bb19af8889b692ce26a38cdf`.
The runner requires its canonical path in the private execution copy and adds
it to the semantic dependency fingerprint.  Complete real context construction
runs inside an audit hook that rejects every data read outside the immutable
execution tree and the one job-private D21 directory.  The real trace is a
mandatory AWS review/runtime gate; it was not fabricated locally.

### 2. Ambient D21, /tmp, and unsafe pickle

The supervisor exclusively copies the sealed D21 bytes to a new private path.
The runner rejects `DIRECTIONB_STATE`, symlinks, and ambient `/tmp`; it never
calls the historical path selectors.  A restricted unpickler admits only
`fractions.Fraction` and the sealed `r1_experiment.K3`, rejects persistent IDs
and all other globals, and then validates the exact D=21 / 183-variable /
77-row object graph before installing in-memory loader views.  A hostile
`os.system` pickle is rejected without executing.

### 3. Corrected real kernel-shift fixture

The v3 fixture constructs every coordinate as
`(deterministic_p2_coordinate + p*kernel_digit) mod p^2`; it never calls the
old `apply_digits` path that erased the deterministic p2 correction.  Before
testing the validator it requires an exact Jacobian-kernel vector, 184/184
zero raw rows, a passing E/W/E5/E6 gate, and an actually changed point.  It
then requires the exact rejection text `semantic state-chain replay mismatch`
and separately deletes/changes the final history point hash.  This fixture is
sealed behind `JC2_D43_V3_REAL_FIXTURE=1`; per charge, the producer did not run
the heavy fixture.  Prior independent corrected AWS evidence is provenance,
not claimed as v3 execution evidence.

### 4. External live trust root

Caller hashes cannot authorize.  A complete external authorization is exact-
shape checked and its SHA must equal the live EC2 instance tag
`jc2-d43-high-hensel-authorization-sha256`; IMDSv2 supplies live account, AMI,
zone, instance, type, IP, region, and hostname identity.  The immutable prereg
is never edited.  The external record binds the PASS report, manifest, prereg,
runner/base/supervisor/worker, complete deterministic source archive, job,
target, runtime, normalized environment, root-owned unit, claims, D21/core23,
and N16 provenance when applicable.  The runner independently repeats live
identity/tag and artifact-byte checks.

### 5. Absolute sanitized runtime

The systemd supervisor environment and each child environment are exact
allowlists; loader, shell, Python, and Direction-B injection variables are
rejected.  The worker is invoked by an absolute hash-bound Bash with
`--noprofile --norc`; Python is absolute, hash-bound, isolated (`-I -B`), and
inside a symlink-free runtime whose environment manifest is a complete census.
NumPy is exactly 2.1.3, and its distribution-tree and BLAS-config hashes are
bound.  The AMI and absolute Bash hash cover host dynamic-library provenance.
Marker path/hash values are normalized to two literal sentinels only for the
environment digest, eliminating the earlier impossible self-hash fixed point;
actual absolute marker paths and exact marker bytes remain checked.

### 6. Whole-job containment and hard resources

The root-owned, hash-bound systemd unit places the supervisor itself and every
descendant in one nondelegated cgroup.  Kernel limits are aggregate
`memory.max=2147483648`, `memory.swap.max=0`, and `pids.max=32`; RLIMIT_AS is an
additional fail-closed ceiling.  `RuntimeMaxSec=1200`, `MemoryOOMGroup=yes`,
`KillMode=control-group`, `ProtectControlGroups=yes`, `RestrictNamespaces=yes`,
`NoNewPrivileges=yes`, and root-owned/nonwritable cgroup and unit paths prevent
ancestry/session/cgroup escape.  Initial membership must be exactly the one
supervisor.  The sticky monitor records every cgroup PID with process start
time and latches host/cgroup swap, OOM, memory, deadline, monitor death, and PID
reuse.  After each child and throughout terminal packaging, the supervisor
must again be the sole member.  Fault cleanup repeatedly TERM/KILLs every
remaining cgroup member and records any residual.

### 7. Durable fail-closed terminal custody

The 1200-second clock begins before authorization.  Monitoring begins as soon
as the hard cgroup is verified and synchronous gates cover late packaging.
State is copy-on-write and the last committed state is snapshotted on faults.
A fresh second process semantically replays the complete state; report, state,
history, target, necessary gate, scope, claims, marker, row/rank census, and
both process reports are deeply compared.  Artifact manifests and deterministic
archives are independently replayed.  A provisional file is explicitly
`PENDING_TERMINAL_CUSTODY_NO_AUTHORITY`; `TERMINAL.json` is the sole authority
and is atomically created last, never replaced.

Any ordinary or late fault produces only NO_VERDICT.  The systemd
`ExecStopPost` path has 60 seconds inside the same memory/process restrictions
to create a negative terminal after SIGKILL, timeout, or OOM; if live IMDS/tag
telemetry is unavailable it may emit only
`NO_VERDICT_SYSTEMD_POSTSTOP_LIVE_AUTH_UNAVAILABLE`.  Before a fresh run
directory can be owned, an already live-authorized attempt receives a durable
negative rejection sidecar in the registered parent.  No unauthenticated path
can produce a positive result.

### 8. Separate N64 provenance

N64 requires a distinct authorization and job identity.  It binds and replays
the exact N16 terminal authority, artifact manifest, evidence archive, state
envelope/payload/history, achieved exponent 16, N16 authorization, job identity,
and normalized environment.  All handoff artifacts are snapshotted before the
N64 output state is created.  The N64 job identity itself includes the complete
N16 provenance object.  A schema-v3 adapter also fixes the inherited v2
validation ordering so a completed N64 state can be independently replayed
without incorrectly demanding that the final state still have exponent 16.

## Bounded producer verification

Commands run:

```text
python3 -m unittest -v \
  cases/d43_source_high_hensel_v3_20260828/test_v3_light.py
python3 cases/d43_source_high_hensel_v3_20260828/runner_v3.py --selftest
python3 -m py_compile cases/d43_source_high_hensel_v3_20260828/*.py
/bin/bash -n cases/d43_source_high_hensel_v3_20260828/aws_worker_v3.sh
shasum -a 256 -c \
  cases/d43_source_high_hensel_v3_20260828/PAYLOAD.sha256
shasum -a 256 -c \
  cases/d43_source_high_hensel_v3_20260828/SOURCE_SEAL.sha256
```

Results: 14 bounded hostile tests PASS; the one real-D43 fixture SKIP is
intentional and preregistered.  The pure selftest PASS includes the 190 -> 182
census, dead-tail support gate, p2 radical frame hash, and p2 E/E5/E6 gate hash.
Compilation, shell syntax, JSON parsing, payload replay, preregistration replay,
and source seal replay all PASS.  No CAS, heavy local reconstruction, AWS call,
or p3+ computation occurred.

## Review and first possible AWS action

The packet must receive an independent hostile PASS.  A reviewer should attack
the restricted loader, audited open closure, marker/environment normalization,
external tag/identity chain, runtime census, root-owned unit semantics,
cgroup/session/double-fork containment, OOM/timeout/poststop terminalization,
deep output binding, target-64 handoff, and corrected real fixture.  Synthetic
light tests cannot substitute for the real Linux/cgroup/IMDS failure fixtures.

Only after PASS may the coordinator provision one `c7i.xlarge`, freeze a
symlink-free runtime/NumPy 2.1.3 census and a root-owned unit, run the read-only
postreview preflight, create a distinct target-16 authorization, set the live
EC2 tag to its exact SHA, and start the unit.  The unit remains fail closed:
any real-runtime discrepancy yields NO_VERDICT.  Resource estimate is one
4-vCPU/8-GiB instance for at most 20 minutes, one effective numerical thread,
2-GiB aggregate cgroup memory, zero swap.  N64 is never covered by that action.
