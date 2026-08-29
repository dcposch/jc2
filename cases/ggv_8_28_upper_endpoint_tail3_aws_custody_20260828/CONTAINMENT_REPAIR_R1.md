# Cutoff-three containment repair R1

Date: 2026-08-28

Status: **REPAIRED AND PREFLIGHTED; HOLD FOR EXPLICIT R2 CLEARANCE**

The aborted R0 modular namespace remains immutable operational non-evidence.
No R0 archive byte or aborted-run artifact was reused or replaced.  R1 is a
new source archive and a new remote source namespace.

## Repair

R0 launched each worker with `setsid`, but GNU `timeout` created an inner
process group.  The recorded outer PGID therefore omitted the actual
Singular RSS and was not a complete termination handle.  R1 changes the
worker to GNU `timeout --foreground`: the worker shell, `/usr/bin/time`,
`timeout`, `prlimit`, and the Singular descendant now remain in the one
recorded `setsid` PGID.

The new source-covered `regress_process_group_control.sh` mirrors that
topology with a bounded 32-MiB Python descendant.  It requires the worker
PID and PGID to agree, validates every PGID member through the production
namespace helper, proves the descendant RSS is included in the recorded
PGID total, sends validated TERM, and fails unless the complete session is
empty without KILL.  `preflight_aws.sh` runs this regression after the
source, host, resource, swap, Singular-hash, and no-heavy-process gates and
before any CAS launch.

Frozen-regression telemetry on r6d was:

```text
PROCESS_GROUP_REGRESSION_PGID=383374
PROCESS_GROUP_REGRESSION_DUMMY_PID=383382
PROCESS_GROUP_REGRESSION_DUMMY_RSS_KIB=42924
PROCESS_GROUP_REGRESSION_GROUP_RSS_KIB=46588
PROCESS_GROUP_REGRESSION_RSS_INCLUDED=PASS
PROCESS_GROUP_REGRESSION_TERM_CLEARED=PASS
PROCESS_GROUP_REGRESSION=PASS
```

No Singular process was started by the repair, archive replay, dry render,
or preflight.

## Frozen source and equivalence

The R1 archive is
`GGV_8_28_TAIL3_SOURCE_R1_20260828T050159Z.tar.gz`, 10,197,012 bytes,
SHA-256
`be3a9915cea967e01b634b637f39d482204316f041dd6c57f6e64592a8cf6b87`.
It has 22 members: the 17-file case, two externally named raw inputs, and
three directory entries.  It has no AppleDouble or `.DS_Store` member.

Charged inner hashes are:

```text
SOURCE.sha256       07626ff48f5acbf78b14bc3b6e3832f311b962358d7c82b8684dcfdb44a3ea08
EVIDENCE.sha256     10667433866a1b1abe361ba8dd7efc56aa1325afcfb97a6c8c3fda2f179f0387
analyze_tail3.py    df15d5a309ad9c0dbcdcd76368ec14daa2318d94c21ce20fef11945bc7f86a1a
target JSON         8443dcb605c15e1fafd281d669c1ea23ec5e875589914af5d6c4540e83fa9363
job_worker.sh       3968e2a92393462c261d9955f94a1a29f47dc359d66732921d4a827a96f5c0ed
PGID guard          6443f437db4b1d537c4a9cdd33b0740b16be883d3a9a82be7402cfcbcb0d39bf
PGID regression     688b039845b16c9121d4854d59d7c62c2065adb7cdc12555664639036d28d56e
preflight           6ef2ea1b847141e997dd042df5acd25fafd1d3b8776caa51c5742e09ba2eebd8
runner              616dc3d18ab9fcfeb131b6738e5fdce1bd1dfe26a760e5d9e6c5af75301763b4
stop helper         95f15c9690565aaef55945f5b8d3ae985abd15ac4f0ed1c7ea32156a54bfebe0
```

Local generation, an independent local `--check`, both manifests, all shell
syntax checks, and a fresh extracted-archive replay passed.  The same
analyzer and manifest replay passed from the transferred r6d archive before
the source tree was made read-only.  Removing only the generated
`producer_script_sha256` field gives the same R0 and R1 target SHA-256,
`3619b434988671811a2f41db241283bcee55ab4c5ddf1c3be836fd79bc031f3e`;
the mathematical target is unchanged.

All six modular `core` dry renders on r6d were byte-identical to independent
local renders.  The remote manifest has SHA-256
`b2d855b7ec280fa23b1f07a33a145b152e1f0fa473692ca5f59168aeb6081117`.

## Remote state

The read-only R1 source is
`/home/ubuntu/jobs/ggv_8_28_tail3_source_r1_20260828T050159Z` on r6d,
instance `i-07eeaf8ba6f0bc419`.  At `2026-08-28T05:13:13Z`, the registered R2
launch root was absent, no Singular process existed, MemAvailable was
515,059,340 KiB, free disk was 118,764,400,640 bytes, and configured/used
swap was zero.  The earlier complete no-CAS preflight log has SHA-256
`d2a27a87a7139dc4e14d28813f0c4aa7e5c018b85896c311c211062737e6729a`.

This repair licenses no mathematical inference and no launch by itself.
