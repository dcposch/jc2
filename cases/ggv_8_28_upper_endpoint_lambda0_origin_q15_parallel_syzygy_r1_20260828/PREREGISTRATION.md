# Lambda-zero origin q15 parallel syzygy portfolio r1

Date: 2026-08-28

## Trigger and immutable input

The preceding arbitrary-Q general r2 screen terminated
`NO_VERDICT_MODULAR_SURVIVOR_OR_CAP`.  Each of its G15-only membership,
full-base membership, and full endpoint-ideal runs reached the identical
five-minute cap at all three registered primes without a marker.  No exact-Q
run was started.  Its byte-frozen archive SHA-256 is
`d0a722a33e26cd90f8665df234f15036ec133e95636a8f537a253b2aea14595a`.
This portfolio must not repeat that same generator ordering serially.

The only mathematical input is the already completed exact reduction:

```text
16a1d0ec3206a0c0a870c7a1395e4bb36e6788c847d30e6be3b445e453a05bd0  input/ORIGIN_Q15_SYSTEM.json
b3f1196f9d69fd060c8acfd21d867c6da1b5447af984bbce6013c5c9a4ec0ba6  input/REDUCTION.json
0751cb1bad59ee7ac70326ce628121b8ee4f8068e63412e9727e1be3d85586ed  input/GENERATED.sha256.json
```

No compiler, raw recurrence, peer derivation, or mutable upstream case is read
by a portfolio job.

## Exact receiver-row compression

Before emitting a solver input, `compile_dedup_portfolio.py` independently
replays the hash of every exact rational polynomial record.  Within each named
receiver family it normalizes by the first nonzero monomial coefficient and
requires every discarded row to be an exact nonzero rational scalar multiple
of its retained representative.  The required class counts are:

```text
q compatibility: 5 -> 5
G13 receivers:    1 -> 1
G14 receivers:   89 -> 5
G15 receivers:   73 -> 5
open condition:   1 -> 1
full base:             17 generators
```

Thus the 17-generator full base ideal is exactly the original reduced base
ideal.  The G15-only and G13+G15 subsets are diagnostic subideals: membership
there implies full-base membership, but timeout or nonmembership there proves
nothing about the full base.

## Parallel portfolio

Every job recompiles the exact dedup certificate from the pinned reduction and
runs a solver self-check before its unique discriminator.  The initially
authorized independent jobs are:

```text
syzygy_g15_target_d7_p65521
  bounded homogeneous Macaulay solve, target-support multipliers, p=65521,
  degree 7, <=5000 columns, 1200 s

syzygy_full_active_d7_p65519
  bounded homogeneous Macaulay solve, all active multiplier variables,
  p=65519, degree 7, <=20000 columns, 2400 s

singular_g15_core_block_std_p65497
  exact-dedup G15 subideal, core/endpoint/receiver dp blocks, std, 1800 s

singular_full_core_block_slimgb_p65521
  exact-dedup full base, core/endpoint/receiver dp blocks, slimgb, 1800 s

singular_full_reverse_dp_slimgb_p65519
  exact-dedup full base, reversed variables, dp, slimgb, 1800 s

msolve_full_endpoint_p65497
  exact-dedup full endpoint ideal, grevlex modular screen, one thread, 1800 s
```

The first two are assigned to newly idle `r6c` and `r6b`, respectively.  Later
jobs may start only when another preregistered r6i host becomes completely idle
and its existing namespace has been frozen.  No two portfolio jobs share a
host concurrently.

The sparse solver emits a complete modular coefficient list and directly
replays it against the target before writing
`MODULAR_SYZYGY_FOUND_WITH_REPLAY`.  Singular variants emit only a modular
normal-form signal; msolve emits only a modular empty-ideal signal.  A bounded
failure, timeout, nonzero normal form, modular unit, factor, or dimension is
navigation only.  Exact-Q replay is forbidden in r1 and requires a separately
frozen successor after a modular signal.

## Backend inventory

Read-only inventory on the eligible r6i hosts found Singular 4.3.2 with
`std`, `slimgb`, `liftstd`, and `lift`, plus `msolve`.  No Sage, Macaulay2, or
licensed Magma executable was present.  r1 installs nothing.  `liftstd/lift`
is reserved for a later exact replay because it can emit replayable
coefficients; msolve is a discriminator only.

## AWS custody and stop rules

Each job must use a new immutable namespace on an audited idle Amazon EC2
`r6i.16xlarge` host (64 vCPU, 512 GiB, below the 1-TiB ceiling).  The host gate
requires the exact DMI vendor/product/hostname/instance ID, at least 450 GiB
available memory, at least 50 GiB disk, zero total swap, no conflicting user
process, and an exact job tag.  Runtime is one pinned core, 64-GiB address
space, 16-GiB file size, a one-hour master cap, explicit inner caps, registered
PID/PGID/SID/starttime, continuous group monitoring, and final no-orphan
census.  Stop with `NO_VERDICT` on source/prereg drift, dedup disagreement,
solver self-check failure, parser failure, swap drift, active-job conflict, or
guard failure.

Initially frozen namespaces:

```text
ggv_origin_syzygy_g15_d7_p65521_r1_20260828T111200Z_r6c
ggv_origin_syzygy_full_d7_p65519_r1_20260828T111200Z_r6b
```

No canonical file, `jc2-lean`, HENS namespace, live lambda job, or unrelated
AWS process is in scope.

