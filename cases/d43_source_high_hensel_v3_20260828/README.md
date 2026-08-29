# D43 finite raw-source high-Hensel packet v3

Status: **frozen for independent hostile review; no AWS launch authorized**.

This is a versioned repair of the preserved schema-v2 arithmetic engine.  It
does not mutate or supersede the v2 evidence.  It closes the executable and
custody gaps charged in the sealed hostile review with SHA-256
`e12490ff6d117c8c6baa0a6ce925aa2da291dbb165d2016c8211a8a48b4f4f8b`.
No `p^3+` computation or AWS launch was performed while producing v3.

## Mathematical scope

The finite diagnostic follows one deterministic Newton branch in the exact
184-row pristine Euler/J-source system at `p=105337`.  The nominal source
registry has 190 coordinates.  Eight columns—`r=39,41` in each of
`tf1,tf2,tg1,tg2`—are structurally absent from every selected even band at
most 42 and replay as literal zero Jacobian columns.  Removing only those
columns leaves 172 tail coordinates, eight fixed coordinates, and
`alpha,beta`: 182 essential coordinates.  The exact source Jacobian rank is
129, so its tangent-kernel dimension is 53 and left-cokernel dimension is 55.

At every committed finite digit the runner replays:

- all 184 raw source rows;
- the five coefficient radical equations and their simple-root/unit gates;
- `HW1=hW1`, `HW2=hW2`, literal `uf30=0`, and the named evaluator completion;
- `E=(9+5r3)A1W1^4+(9-5r3)A2W2^4=0`, with `W1,W2` units;
- the literal corrected-243 E5 pair with one deterministic `HM`, and E6 with
  one deterministic nonzero `s1F`.

The registered `p^2` anchor has `E=0` exactly modulo `p^2`, unit `W1,W2`, a
common unit `HM`, and the explicit unit `s1F=2^8 HM/7^16`.  On this localized
radical/chart coefficient ring the E5 pair plus existential `HM`, and E6 plus
existential nonzero `s1F`, project to exactly `E=0` with `W1W2 != 0`.  They are
set-theoretically equivalent over `C`; over an unlocalized coefficient ring
where the displayed denominators cease to be units the existential system can
be stronger.  The raw 184 equations are not asserted to imply E: failure of
this separately checked necessary gate has its own terminal mathematical
status.

The band-42 x-side formula is an exact support identity, not merely a
base-point tangent check.  `U_f,U_g` first differ at slot 42, so every cross
term reaching output slot 42 sees only the slot-zero `Phi_y,Gamma_y` constants;
positive y-slots overshoot, `alpha*beta` starts at slot 84, and lower rows are
unchanged.  The preserved schema-v2 context includes basis and perturbed-y
operator controls.

## Finite claim firewall

A successful target `N` certifies only a compatible point modulo `p^N` of the
declared finite raw 184-row source truncation along the deterministic
zero-free-digit branch, with the finite necessary E/W/E5/E6 gate.  It does not
replay the 34 parked constraints, inverse-chart rows, template/D25 equations,
or source-to-normal-form/reducer identities.  It therefore does **not** certify
parked/source equivalence, a full residue-A/template/D25 point, branch survival,
indefinite lifting, formal smoothness, a `Z_p` or characteristic-zero point, a
formal germ, an ambient Keller map, or a JC2 counterexample.

## Schema-v3 replay and sealed data

Every resume starts from the deterministic exponent-one state and replays each
complete digit: root lift, input point and rows, exact `-F/p^n`, all cokernel
pairings or obstruction, deterministic RREF correction, output point, all 184
rows, both template gates, and every record/prefix hash.  The committed p2
frame/RHS/correction/point/gate anchors are mandatory.  A finite stored state
is never interpreted as an indefinite lift.

The formerly ambient D21 pickle is copied exclusively to a job-private path,
hash checked, loaded by a restricted unpickler admitting only `Fraction` and
the sealed `K3` tuple, structurally censused, and converted to in-memory loader
views.  `DIRECTIONB_STATE`, host `/tmp`, symlinks, and arbitrary pickle globals
are rejected.  The omitted `directionb_core23_p105337.ms` is now a canonical
sealed execution input with hash
`0533787f6bf89ff25478f01ddad40230a11f6a19bb19af8889b692ce26a38cdf`.
Real context construction runs under a file-open audit limited to the immutable
execution copy and the one private D21 directory.

## AWS custody and authorization

The immutable preregistration remains `V3_REVIEW_FROZEN_NO_AWS_LAUNCH` forever.
It cannot self-authorize.  After an independent PASS, a distinct external
authorization must bind the reviewed bytes, review hash, complete source
archive, exact host/AMI identity, job, target, runtime, root-owned systemd unit,
normalized child environment, and—for N64—the complete N16 handoff.  Its exact
SHA-256 must be present in the live EC2 instance tag
`jc2-d43-high-hensel-authorization-sha256`.  Both supervisor and runner query
IMDSv2 and compare the live identity/tag.

The worker and validation process execute only from a fresh, replayed,
read-only private payload copy.  Python and Bash are absolute/hash bound; the
runtime manifest is a complete symlink-free census; NumPy 2.1.3's distribution
tree and BLAS configuration are pinned.  Child environments are built from an
exact allowlist.  Marker path and marker hash use canonical sentinels for the
environment digest, eliminating a self-hash fixed point while actual absolute
paths and bytes remain checked at each execution.

The root-owned systemd service puts supervisor and every descendant in one
nondelegated cgroup.  It enforces aggregate `memory.max=2 GiB`,
`memory.swap.max=0`, `pids.max=32`, `MemoryOOMGroup=yes`, `RuntimeMaxSec=1200`,
`KillMode=control-group`, `ProtectControlGroups=yes`, no namespaces, no
privilege gain, and a 60-second post-stop negative-terminal window.  The
supervisor is itself inside every hard limit.  A sticky monitor records
PID/start-time identities, memory, OOM, cgroup swap, host swap, and deadline;
success requires the supervisor to be the sole remaining cgroup member after
each child and throughout terminal packaging.

The main run and a fresh second semantic-replay process are deeply bound to the
same state, history, target, claims, source archive, and authorization.  All
late checks, archive replay, and atomic terminal promotion remain inside the
hard unit.  `TERMINAL.json` is the sole authority and is created last with
atomic create-if-absent semantics.  OOM, timeout, signal, supervisor death, or
any custody fault yields only `NO_VERDICT`; `ExecStopPost` provides a negative
terminal even when live authorization telemetry is temporarily unavailable.

N64 is never a continuation under the N16 authorization.  It needs a distinct
live-tagged authorization binding the exact N16 terminal authority, artifact
manifest, evidence archive, state envelope/payload/history, N16 authorization,
job identity, and normalized runtime environment.  All handoff artifacts are
replayed and snapshotted before the N64 output state is created.

## Producer tests and launch order

The bounded default command is:

```text
python3 -m unittest -v \
  cases/d43_source_high_hensel_v3_20260828/test_v3_light.py
```

It runs no CAS, real D43 reconstruction, AWS call, or `p^3+` work.  The corrected
real fixture uses
`(deterministic_p2_coordinate + p*kernel_digit) mod p^2`, first requires all
184 rows and the necessary template gate, and then requires the precise
semantic-chain rejection plus two history-point-hash mutations.  It is gated by
`JC2_D43_V3_REAL_FIXTURE=1` and is reserved for independent AWS review.

The first possible authorized computation, only after a hostile PASS and an
external live-tag authorization, is target 16 on one `c7i.xlarge` (4 vCPU,
8 GiB), with one numerical thread, a 2 GiB aggregate cgroup cap, zero swap, and
1200 seconds.  Target 64 requires the separate provenance-bound authorization
described above.  `preflight_v3.py` is read-only and merely computes the
post-review source/environment bindings; it never authorizes or launches.
