# Frozen cutoff-three AWS target

This bundle has two exact stages.  Neither was run locally.

## Stage A: root-core diagnostic

The `root` scope contains the exact 17-dimensional `D21` root-core
intersection.  It is split into three fieldwise branches of

```text
K = Q0*(b_bar*Q0 + L0^2).
```

The two `Q0=0` branches use the exact factor
`L0*(4*b_bar-L0)` and its field-radical consequences.  The `Q0!=0` branch
introduces `tau=L0/Q0` and retains the two independently checked scalar
equations.  This stage is diagnostic: it contains no endpoint equation and
cannot itself close the cutoff-three endpoint stratum.

```bash
TARGETS/run_aws.sh mod root root-recon
TARGETS/run_aws.sh exact root root-exact
```

## Stage B: nonzero-V endpoint cover

The `core` scope uses the 17 exact `D21` root-core consequences, the monic
carrier relation for literal `c=p86`, the literal endpoint
`-1-p32*p189+p86*p91`, and the 17 nonendpoint `D22` rows.  It is a necessary
subsystem: a unit proves emptiness, while a nonunit is inconclusive.  The
`full` scope replaces the root-core consequences by all exact staged basis
constraints from `D14` through `D21` and is the fallback.

For either scope, all six commands/charts are mandatory.  Chart `i` adds
`chartinv*V_i-1`; it never sets `V_i=1` and does not normalize an endpoint
carrier.

```bash
TARGETS/run_aws.sh mod core core-recon all                # r6d only
TARGETS/run_aws.sh exact core core-r6a 0,1                # r6a only
TARGETS/run_aws.sh exact core core-r6c 2,3                # r6c only
TARGETS/run_aws.sh exact core core-r6d 4,5                # r6d only
```

Use the analogous three exact commands with scope `full` only if `core` is
inconclusive.  Exact `core/full` runs reject a missing selection, `all`, an
unordered/wrong pair, duplicate, or pair on the wrong host.  Each pair is
explicitly partial and nonpromotable alone.  After custody download, combine
the three disjoint manifests with:

```bash
python3 TARGETS/validate_results.py combine RUN_R6A RUN_R6C RUN_R6D
```

Modular runs are reconnaissance only.  Every empty chart used in a proof
requires an exact-Q run with `CERTIFICATE_CHECK=PASS`.  A timeout, killed
job, nonunit standard basis, or modular result is not evidence of a point or
of nonemptiness.

## Host envelope and custody

The frozen exact assignment is r6a (`i-02cb2b4a379ffcc64`) for charts 0,1;
r6c (`i-040b7a1c2ed72d4cc`) for charts 2,3; and r6d
(`i-07eeaf8ba6f0bc419`) for charts 4,5.  Each is an r6i.16xlarge with 64
vCPU, approximately 528 GB RAM, swap disabled, and the pinned Singular
binary.  Modular all-six and the root diagnostic are pinned to r6d.
Modular mode runs at most six 40-GiB workers for six hours.  Each exact pair
runs two 120-GiB workers with a 12-hour per-job and global cap; the three
hosts reduce the complete cover to roughly 12 hours.  The three exact root
jobs have two batches and a 24-hour cap.  Per-process address-space,
six-GiB combined-transcript, CPU, per-job wall, global wall,
aggregate-memory, free-disk, swap, host identity, source hash, and
Singular-binary gates are enforced before launch.  Live 30-second guards
retain 150 GiB available RAM and 50 GiB free disk and stop on any swap.
Every telemetry sample records UTC, available RAM, swap used, free disk, and
RSS summed by validated worker PGID; `/usr/bin/time -v` records each job's
maximum RSS, wall time, and exit status.

Each worker starts in a fresh session/process group.  PID, PGID, namespace
job path, and runner start time are recorded.  Stop and guard paths validate
every live group member against the namespace before signalling the whole
group, then escalate from `TERM` to `KILL`; they never signal an unvalidated
PID/PGID.  Each run uses a fresh UTC namespace and never deletes an older
namespace.  Each exact host reserves at most 12 GiB for its pair; modular
all-six reserves 36 GiB.  The remaining cumulative reservation is rechecked
before every launch.  The fail-closed validator checks rendered-job hashes,
RC zero, exact field, unit, cofactor replay, and exactly the requested chart
set.  Only the combined validator's disjoint union `{0,...,5}` is
coverage-complete.

The worker uses GNU `timeout --foreground`, keeping `timeout`, the limited
command, and the actual Singular descendant in the worker's recorded
`setsid` PGID.  Every preflight also runs the bounded, no-CAS
`regress_process_group_control.sh`.  Its time/timeout/prlimit/Python chain
allocates memory in a dummy descendant, proves that the recorded PGID RSS
includes that child, validates the group through the production helper,
sends TERM, and fails unless every namespace-bound descendant disappears
without KILL.

The target does not use the rejected external five-mode/full-fixture
reduction: forced literal coefficients `c14,c16,c18,c20` remain in the
authoritative staged rows.

The exact input census is recorded in
`tail3_v_nonzero_d22_target.json`.  Rebuild and verify the complete packet
with:

```bash
python3 analyze_tail3.py --check --output .
sha256sum -c SOURCE.sha256
sha256sum -c EVIDENCE.sha256
```
