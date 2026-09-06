# Class A: smallest source-support receiver compute probe

## Verdict

**OPEN / COMPUTE-BOUND; no SIGNAL, KILL, or screen SURVIVAL.**  The unique
smallest eligible receiver class is `C_n27m18_M20_ell2_s2`, containing only
printed row `R005`.  It has 307 coefficient unknowns and 484 coefficient
generators (308 and 485 after adjoining `T` and `Tc-1`).  Patched guided GB
timed out during its modular Hilbert seed, msolve segfaulted before its first
F4 step, and exact-Q Singular timed out in `std`.  None returned a basis.

The requested class-tree row program is not present on disk; that missing-path
fact is kept distinct from the five charged inputs, whose receipt-derived
SHA-256 check passed without exception.  The compute jobs used only a gated,
worker-scratch reconstruction matching the frozen production-program and
coordinate digests.

## 1. Frozen custody and host-write boundary

Before interpretation, an `awk` program joined the receipt's numbered
`charged_input_<i>_basename` and `_sha256` lines, and its output was passed
directly to `sha256sum -c`.  The mechanically generated manifest returned five
`OK` lines:

| charged frozen input | verified SHA-256 |
|---|---|
| `chart-counts.json` | `4f9382b1c39e2a0b39e2dc14757607f0051969aefc331f3eb2efacd2c1a61d44` |
| `roster.jsonl` | `cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf` |
| patched `guided_gb.py` | `95d12f5b23975e8699b634b1ba8c6f0e6fc4e24abfcd4bad2db936e1c74e9826` |
| `fleet.sh` | `a9da94d341a691942e9d6a6a6d90d97008b2d7baa1cadb2592481cf6b9c11c4c` |
| `FALLACY-v2.md` | `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5` |

The receipt is `xmodel/classA-smallest-receiver-sol56-20260906.run.v2` and
the checked copies remain under `/tmp/jc2-lane.Yhc8AP/inputs/`.  `df -h /`
was run before the first host write; it showed 96 GiB total and 12 GiB
available.  Large generation, solver inputs, logs, and outputs stayed on the
worker.  Host output is limited to the small notes directory and this report.

## 2. Literal roster selection and unique minimum

There is a count discrepancy in the question that must not be silently
normalized.  The frozen roster has 46 rows satisfying nonempty own-route
state, licensed descent, and `u_s=1`.  The literal additional window
`100<n<=200` removes `R001`--`R004` and `R007`, leaving **41**, not 44.  The
prompt's residual count 44 is recovered by removing the two previously killed
rows `R058` and `R063` from all 46; applying the degree window as well leaves
39.  This bookkeeping difference does not change the minimum.

Sorting the frozen classes by unknown count, with generator count and printed
source data as deterministic tie-breakers, begins:

| rank | row | receiver key | unknowns excl./incl. `T` | generators coeff./incl. `Tc-1` |
|---:|---|---|---:|---:|
| 1 | `R005` | `n27_m18_Mlast20_ell2` | 307 / 308 | 484 / 485 |
| 2 | `R006` | `n39_m26_Mlast30_ell1` | 322 / 323 | 495 / 496 |
| 3 | `R008` | `n21_m14_Mlast15_ell4` | 370 / 371 | 595 / 596 |
| 4 | `R009` | `n48_m32_Mlast37_ell1` | 388 / 389 | 600 / 601 |
| 5 | `R010` | `n35_m14_Mlast30_ell1` | 403 / 404 | 576 / 577 |

Thus the minimum is unique.  `R005` prints source `(n,m)=(135,90)`,
`M=(-90,100,133)`, `V=(4,4)`, and `u_s=1`; its licensed receiver is
`(n',m',M'_last,ell)=(27,18,20,2)`.  The V-independent receiver class ID is
`C_n27m18_M20_ell2_s2`, while the frozen historical fibre label is
`C_n27m18_M20_ell2_s2_V4`.  Its `residual_row_count` is one and its sole row
is `R005`.  See the charged machine row at
`/tmp/jc2-lane.Yhc8AP/inputs/roster.jsonl:5`, the identical printed line at
`box/residual66-20260905/roster.md:27`, and its own-route provenance at
`box/child-own-v-20260905/own-rows.jsonl:95`.

The frozen class record fixes coordinate digest
`9758dedb763696c99ee72d3cd7345d7dc336637fb65909731811a6e5afe37c89`,
the fixed production program digest
`8353325956564822d62c676bb8776f09bad015be709e966d58fa48767f632bd5`
(19,571 bytes), and raw program digest
`3cefe3b7f3b1be28c2c446021360cfa5ce8eb787af9ed4e1c5d061ef8a7654ce`.

## 3. Requested row path: absent

The path that the frozen naming convention requires is

```text
box/gi-only-20260905/classes/C_n27m18_M20_ell2_s2/rows/C_n27m18_M20_ell2_s2_G_rows.tsv
```

It does not exist.  A read-only enumeration of
`box/gi-only-20260905/classes/` found only the six materialized `n<=100`
classes, and no file in that tree carries either target digest.  Accordingly,
this report does not cite a nonexistent program as if it had been verified,
does not substitute one of the six unrelated charts, and did not create a
host-side file to manufacture the requested provenance.  This is a missing
uncharged artifact, not a mismatch in the charged-input check.

To execute the requested bounded probe, the exact target was materialized only
in worker scratch from the production chain and source hashes recorded inside
the frozen `chart-counts.json`.  The acceptance gate required the recorded
fixed-program SHA-256, the coordinate SHA-256, 307 variables, 484 nonzero
coefficient rows, source indices 0 through 483, and exact bihomogeneity.  The
accepted exact-Z stream had 485 physical lines including its header,
53,209,262 expanded terms, 2,179,919,994 bytes, no NUL bytes or sparse holes,
and SHA-256
`b4a4160ccef95d28490da264704ec8b272110222f8438d62d91ef62a9eccaf78`.
Generation took 240.804 seconds and peaked at 9,012,812 KiB RSS.

This is a hash-pinned ephemeral reconstruction, not retroactive provenance
for the absent class-tree path.  A duplicate-writer intermediate was rejected
on allocation/NUL/header/line-count checks, deleted, and never transformed or
given to a solver.  Only the clean stream above entered the input transforms.

## 4. Ideals, ring maps, and declared orders

Let `I` be the 484 coefficient rows of `J(P,Q)-c*x^ell` in the declared
coefficient ring.  Here `K=9`, `ell=2`, and `D=n'+m'-1=44`.  A coefficient
of level `i` and exponent pair `(b,a)` has bidegree `(b,iK-a)` (with the
`h` level treated as `i=1`), while `deg(c)=(ell+1,D)=(3,44)`.  The positive
scalar functional is `(b,d) -> 19b+d`.  Every coefficient generator passed
the bidegree check before the three derived inputs were closed.

Job (a) applies the hash-verified patched `box/lib/guided_gb.py` to the
homogeneous saturation `S=(I:c^infinity)` under this weighted order.  Its
prelude extracts the ideal component returned by `sat`, asserts the active
ring, and runs the positive and negative controls required by `FALLACY-v2`.
The patched helper owns a modular Hilbert-seed stage and returns a typed
`INCONCLUSIVE_TIMEOUT` with `timeout_stage=hilbert_seed` or `std` rather than
leaking a bare timeout exception.  Modular unit promotion is disabled.

Job (b) uses a token-level bijection from the remaining 306 coefficient names
to msolve-safe variables, checks every image and generator delimiter, and
substitutes exactly `c=1`.  Its header declares the prime 1,073,741,827; the
command uses msolve 0.10.1 AVX-512 F4 with `-g 2` and verbose degree telemetry.
This section is a screen: even a printed modular `[1]` would be typed SIGNAL
only and would still require a homogeneous lift to a checked `c^N` identity
by the cone lemma.

Job (c) works over exact Q in all 307 coefficient variables plus `T`, adjoining
`Tc-1` as generator 485.  Its Singular order is a separate `T` block followed
by the same positive weighted coefficient block, `(dp(1),wp(weights))`.
Only a completed exact `[1]`, with the declared map and controls intact, is a
KILL of this receiver class.

## 5. Existing worker, dispatch, and resource controls

No instance was launched or terminated.  The already idle worker was
`i-0cd415bd9d3abed39` at `172.30.0.163`, type `r7i.8xlarge`, with 32 vCPUs
(16 cores), 247 GiB visible RAM, no swap, and AVX-512.  Preflight found no
competing CAS process.  Its root filesystem had 23 GiB available before
scratch writes.  Singular reports 4.3.2.  msolve reports 0.10.1 and binary
SHA-256
`0436525b06fe83b1a6a00097a96d9bcafdc40d8de6315c724b9ada9a4c04ff5f`.

All large files were placed below worker scratch
`/home/ubuntu/classA-smallest-20260906.xpXroy` or in the worker's `/dev/shm`.
The four derived solver inputs totalled 7,944,313,946 bytes.  Their transforms
checked 484 generators and 53,209,262 terms before launch.  The three jobs
started together at `2026-09-06T04:36:20Z`.  Each had a 149-minute inner GNU
watchdog and a 150-minute systemd runtime ceiling.  CPU allocations were 16
threads for msolve and eight CPUs apiece for the two Singular-based lanes.

## 6. Bounded results

| job | typed disposition | elapsed / peak RSS | degree wall and basis |
|---|---|---:|---|
| (a) patched guided `(I:c^infinity)` | `TYPED_TIMEOUT_OUTER_DURING_HILBERT_SEED` | 8,940.126 s / 109,918,196 KiB | seed incomplete; exact-Q not started; basis unavailable |
| (b) msolve `c=1`, p=1073741827 | `FAILED_SIGSEGV_BEFORE_F4` | 48.26 s / 8,458,580 KiB sampled | no F4 step or matrix; basis unavailable |
| (c) exact-Q `std(I+(Tc-1))` | `TYPED_TIMEOUT_EXACT_Q_STD` | 8,943.596 s / 124,433,724 KiB | Singular degree 54 closed/55 live; no matrix; basis unavailable |

Job (b) ended at `04:37:09Z` with wrapper and systemd return code 139; GNU
`time` records signal 11 and maximum RSS 8,439,088 KiB, while the 200-ms
process-tree sampler saw 8,458,580 KiB.  Its basis output is zero bytes.  The
last diagnostic was the initial-seed message; no F4 round, degree, matrix,
basis, or unit marker was printed.  The input-size guard also records
`53,209,262*306 = 16,282,034,172`, beyond signed 32-bit range.  An internal
index/capacity overflow is a plausible explanation, but only an inference;
the evidenced disposition is the pre-F4 segmentation fault.

Job (a) ended `07:05:20Z`, rc 124.  Its p=32003 saturation/Hilbert seed never
completed the helper contract: no `GG__STAGE`, Hilbert numerator, or result
JSON was emitted, and the exact-Q stage never started.  GNU `time` peak was
105,619,632 KiB; the 200-ms process-tree sampler saw 109,918,196 KiB and the
cgroup peak was 112,742,891,520 bytes.  Final memory events were
`high=1718066,max=0,oom=0,oom_kill=0`.  Thus the outer-stage type is explicit,
but no modular or rational mathematical result exists.

Job (c) ended `07:05:24Z`, rc 124.  Both pre-target controls passed and
`R005__STD_BEGIN` printed; `BASIS_SIZE`, `UNIT`, and completion did not.
GNU `time` peak was 124,414,112 KiB, the process-tree peak 124,433,724 KiB,
and the cgroup peak 127,647,522,816 bytes.  Final events were
`high=2686266,max=0,oom=0,oom_kill=0`.  Its wall-clock timeout, not a memory
limit, is the terminal cause.

## 7. Promotion boundary, source support, and degree wall

No run finished.  In particular, msolve printed no modular `[1]`, so there is
not even a modular SIGNAL; guided never reached exact Q; and the full exact
ideal returned no `[1]`, so it supplies no KILL.  No proper basis completed,
so there is also no nonunit SURVIVAL of the screen.  The receiver class and
its sole row `R005` remain open.  Had the c=1 lane printed `[1]`, it would still
have required a homogeneous lift to a checked `c^N` identity.  Had the full
exact-Q lane proved `[1]`, it would have killed exactly `R005`.

The row is source-complete at the receiver/theorem level in the precise frozen
sense `coverage_status=PROVED_RECEIVER_FOR_COMPLETE_CHILD_CHAIN`, with support
theorem `17(fffffff) G_i-only source receiver` and effective-complete-chain
scope.  It is **not** an on-disk member of the older six-class frozen
`h-SUPPORT-COMPLETE` artifact family, so that artifact label is not transferred
by analogy.  Receiver necessity is also not attainment and supplies no source
witness.

The next compute lane should size from completed F4 telemetry only:

**F4 wall: none available.**  msolve crashed with zero completed F4 rounds,
so the highest completed F4 degree and its matrix rows/columns are all
`UNAVAILABLE`.  Singular's separate std protocol reached degree 55 live and
closed degree 54, with last `s` counter 149,360, but emitted no matrix
dimensions and is not relabelled as F4 telemetry.  Capacity evidence for a
next lane is therefore the pre-F4 crash on 53,209,262 terms and 306 c=1
variables, plus about 105/120 GiB cgroup peaks for the guided/exact lanes;
`53,209,262*306=16,282,034,172` makes a 32-bit msolve indexing limit plausible
but not proved.

No exit price, carrier attainment, or equality from a floor is asserted.  A
modular unit would be only a signal; a timeout, crash, or missing basis proves
neither unit nor nonunit; and a completed nonunit basis would mean survival of
this screen only.  Therefore no exit-charge declaration is present.

## 8. Artifacts and cleanup

The small retained notes are in `box/classA-smallest-20260906/`.  They record
selection, transforms, commands, per-job timing, RSS, hashes, and cleanup
evidence.  No ledger or
`jc2-lean` file was edited, and no `ideation-*` material was used as an input.

After the 7,236-byte terminal summary (SHA-256
`50108340cf9abe642cb37f945666b38bb10c9d0c3f82347aecbc0d1eb69f1b15`)
was inspected, only the resolved scratch tree and `/dev/shm` row stream were
removed.  Both paths are absent and no related process remains.  At
`07:09:33Z`, worker `/` again had 23 GiB free and memory had 245 GiB available.
Instance `i-0cd415bd9d3abed39` (`172.30.0.163`, `r7i.8xlarge`) remains running;
there was no launch or termination action.  The removed scratch is not
recoverable from the worker.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13495`.
- Body SHA-256:
  `a9f2b9c40073cc3c21730ed1a4089dde57973f62f065c29d646b342f14a02a32`.
- Frozen basis: `4c9725cf9461cfad8cfae366637f98cc08e70b80`.
