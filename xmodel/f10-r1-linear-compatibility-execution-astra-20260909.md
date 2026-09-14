# F10 finite generic verifier / installed-API execution

Producer result: **ENGINEERING PASS, GENERIC ONLY**, pending the first
independent runtime-evidence review. One frozen batch completed; there was no
actual-source artifact, source acceptance, solver, full matrix or ideal decision.
No retry, repair, installation, fallback or additional mathematical experiment.
All computation was on the single explicitly authorized worker; local work
was documentary reading, metadata/hash checks and transactional publication.

## 1. Authority, clocks and exact scope

First tool 2026-09-09 22:31:54 UTC found both targets absent. The controlling
publication cap is 23:01:54 UTC (first+30 minutes, earlier than 23:04), with
the last three minutes reserved. ROOT separately fixed mathematics at 22:47,
dispatch task at 22:53 and independent worker STOP at 22:54. None was reset.

Initial activity was documentary only. The compatibility first static gate
d9bf289989d2631f0ab39657b4a3f0c8f7389e21ded388e68e366cd13d7fdc31 and
terminal receipt 782c8ba6096e61c1ec5937b14ca031e70746dd2fc545587f5e44a795194b4715
were pinned, receipt first, then gate WHOLE. Its A–D static confirmation and
parent17z are accepted premises, not runtime evidence. Source custody's 29
entries were current before source reuse. Whole/read-slice/reuse details are
in READ-SCOPE.md. No gate provenance body or unrelated report was followed.

ROOT supplied immutable mode444 files in this box:

- dispatch.registration.json: ba1b374bf803f583ff9baa5617d9d058ca2b1215e98dd69240276fe892f6bc3b.
- ROOT-REGISTRATION.md: 034738126ee5555e55a8080ccfccbdae3f949d689b52577f124ee97198261d4e.

Both were read WHOLE before remote access. The registration's 100 package
pins/module metadata exactly equal environment.json
35a9c3229300816d16b53db6d0795ce9d6fd1de1f8a10ff5689c83543036a34f.
That declared package/ELF dependency set is not a hermetic OS/stdlib closure
or observed import map. No package discovery or installer was run by this lane.

After ROOT's physical confirmation and explicit release, fresh 22:38:10–11
checks confirmed i-08d2a40f272ee9fa2 RUNNING, c7i.4xlarge, private172.30.0.72,
Owner=f10-r1-exact-artifact-validation-20260909, EBSvol-0574e0fa5aed1f5e3,
DMI Amazon EC2/exact instance, hostname ip-172-30-0-72, interpreter a92f0f95...
and installed module2e5f8f17.... The independent ROOT USER stop timer was ACTIVE.
Root started the worker; this lane did not allocate/start/retag it.

The exact remote directory
/home/ubuntu/jc2-f10-r1-linear-compatibility-20260909 was explicitly ABSENT,
then created exclusively. Exactly nine frozen task files and the registration
were transferred. All 110 task/interpreter/native pins plus the registration
(111 hashes) matched before dispatch. No solver.py or mathematical source
artifact was staged. The existing source headers remain unchanged even where
their historical preparation status says UNEXECUTED.

## 2. Actual process and cap custody

One SYSTEM service jc2-f10-linear-compat-runtime-20260909.service started
22:39:21 UTC; invocation2896d5f8ed454902a04791a8396db5db; mainPID7155,
startticks16607; namespace pid:[4026531836]. Its exact Python -I -B vector,
stat, cgroup and properties were captured immediately in launch-and-identity.txt.
Userubuntu, fresh cwd, RuntimeMaxSec300, TimeoutStopSec5, KillModecontrol-group,
MemoryMax3221225472, TasksMax64, LimitFSIZE16777216; LD_LIBRARY_PATH and
LD_PRELOAD explicitly empty, OMP_NUM_THREADS and OPENBLAS_NUM_THREADS equal1.

The unchanged caller issued the seven fixed preflights, then one compatibility
child. Probe caps5wall/3CPU/2GiB; dummy5wall/3CPU/32MiB; compatibility
180wall/170CPU/2GiB. Mathematical aggregate240wall, inherited16MiB files,
15-second admission margin and original stored return cutoff were retained.
No new inner PGID or supervisor was added. CAPRUN is the unchanged4435279d
instrument: RSS is sampled exact-PGID aggregate with possible overshoot;
CPU is inherited per-process RLIMIT_CPU, not aggregate child CPU; wall/cleanup
is not a strict real-time guarantee.

The first status check at22:39:47 found inactive/dead, MainPID0, owned cgroup
absent. Journal shows deactivation22:39:26.349795. No child-tree snapshot was
captured while children were live: the caller was captured immediately, and
child identities come from the retained dispatch/telemetry and dummy stdout.
This distinction is explicit, not an invented live observation.

At22:40:26 the original caller7155 and owned cgroup were absent. Before ANY
payload read, all85 owned remote files were SHA-bound with modes/sizes. All85
transferred bytes matched locally; all110 original runtime pins matched again.
Metadata then identified18 total recorded PIDs and eight child PGIDs. At
22:41:15 every recorded PID and all eight PGIDs were independently absent.
The exact service remained inactive/dead. Only afterward were receipt semantics
read. The PID/start/namespace table is in local-readback-and-identities.txt;
the absence check and exact-unit journal are in terminal-owned-process-check.txt.

## 3. Observed finite preflights and telemetry

| Child | CAPRUN wall seconds | Sampled peak RSS bytes | Outcome |
|---|---:|---:|---|
| gate-disabled | 0.127025306 | 29790208 | ordinary exit1, authority refused |
| gate-wronghost | 0.121034208 | 30068736 | ordinary exit1, host refused |
| gate-argv | 0.122171066 | 30121984 | ordinary exit1, parent argv refused |
| gate-cap | 0.121781541 | 29974528 | ordinary exit1, cap/vector refused |
| gate-missing-input | 0.121806488 | 30220288 | ordinary exit1, input pin refused |
| gate-valid | 0.065099746 | 9166848 | ordinary exit0, sentinel present |
| dummy-descendant | 0.389771827 | 80072704 | expected RSS RESOURCE_CAP125 |
| compatibility | 3.100202855 | 34848768 | NORMAL_EXIT0, resource=null |

The five rejected authorities wrote no postauthorize sentinel. Their exact
stderr reasons respectively are: no active registered authority; not the
registered AWS host; full parent argv differs from registered capped runner;
registration is not the exact required CAPRUN argv; checker input artifact
must be explicitly hash-registered. Valid sentinel bytes are POSTAUTHORIZE plus
newline. These are actual helper-entrypoint tests, not static predicate flips.

Dummy leader7192 exited before its TERM-ignoring child7195; both were inPGID7192
and the same recorded namespace. The actual measured group RSS exceeded32MiB.
The four identity events are MATCH beforeTERM; SENT exact integer15; MATCH
beforeKILL; SENT exact integer9. Both MATCH records agree with PID/PGID7192
and the same boot/startidentity. TERM, KILL, cleanup_complete and leader_reaped
are true. Later independent absence covers both processes. The intentionally
observed RSS cap is the passing cleanup control, not a failed math attempt.

Generic child7206/PGID7206 began22:39:23.193343 and ended22:39:26.293534.
Its stderr is empty. The outer unit journal reports4.923s CPU and5.2M memory
peak; that separate unit-accounting observation is retained verbatim and is
NOT substituted for CAPRUN's group-RSS observations. No per-verifier timing,
per-API timing or actual-source performance is measured or forecast.

## 4. Genuine generic/API receipt

remote/compatibility.receipt.json is5955bytes, SHA
c99eda146afc91cb521a6a27739422ac7f1928c9763586e34a0a1bd590d3e443.
Its status is GENERIC-COMPATIBILITY-PASS-NOT-ACTUAL-SOURCE. Batch PASS is
7982bytes, SHA2e46444f49cd2071f9725228da2b570e32712f1a275488a974c32755a53b57c3.
The actual observed python-flint module path/version/hash match the pinned0.9.0
environment. Its three scalar strings were0,9007199254740993 and
9007199254740993/2. Both2x5 constructors and RREFs returned the registered
exact rows: consistent pivots0,3 and separating pivots0,2, both rank2.
The finite code has23 explicit Python-level fmpq constructions (three scalar,
twenty entries); internal native operations are not counted. Nothing invokes
the actual solver or constructs its217x1856 augmented matrix.

All twelve IN-PROCESS checker.verify calls completed: five positives and seven
expected negatives. They are not checker.main or actual-source acceptance.
All nine literal input rows and dense zero slots remain in each generic wire.

| Fixture | Observed result or exact rejection reason |
|---|---|
| unit-positive | VERIFIED-GENERIC-ZERO-QUOTIENT |
| unit-negative | full 217-coordinate sum h_i f_i equals q^5 |
| separator-zero-positive | VERIFIED-GENERIC-NONZERO-QUOTIENT |
| separator-normalization-negative | dual target normalization equals one |
| separator-T-positive | VERIFIED-GENERIC-NONZERO-QUOTIENT |
| separator-column-negative | dual column annihilation i=0 j=0 ell=0 |
| precision-positive | VERIFIED-GENERIC-ZERO-QUOTIENT |
| high-T30-negative | full 217-coordinate sum h_i f_i equals q^5 |
| rounded-canonical-string-negative | full 217-coordinate sum h_i f_i equals q^5 |
| float-type-negative | canonical rational strings only |
| zero-guard-positive | VERIFIED-GENERIC-ZERO-QUOTIENT |
| zero-guard-false-separator | dual target normalization equals one |

Each fixture was exclusively written/reread/hash-bound by the frozen harness;
the twelve exact fixture hashes and byte sizes are retained in both receipt
and terminal-metadata-check.json. The high-T30 alteration genuinely changes
the full identity. Precision uses K=9007199254740993 and h9=T^20/K against
f9=K*T^5, so the correct product is T^25, not K*T^25. The successful nested
parser received exact K and1/K strings. The rounded canonical denominator
9007199254740992 failed the identity, while the float failed type validation.
This is not merely a generic JSON round-trip claim. Zero guard is deliberately
included and yields the zero localization; it is not a nonzero source witness.

Every fixture coefficient is constant in v. Consequently this batch does NOT
establish runtime coverage of nonconstant B reduction or every finite-product
component. Those limits survive the PASS. No fixture or verifier was replayed
locally. Local postprocessing only compared metadata/bytes/hashes/argv vectors.

## 5. Read-back, cleanup and limitations

terminal-metadata-check.json verifies eight full child vectors, the eight
registered parent vectors including each deliberate defect, CAPRUN child argv
hashes, authority/telemetry hashes, all per-operation input vectors, stream
hashes,15-second margin fields and return-before-stored-cutoff comparisons.
Every one of the twelve fixture hash/size bindings matches the genuine receipt.
No solver flags or rank-only statement was used as an actual ideal proof.
The authority gate is cooperative frozen-file custody, not cryptographic
authentication; source and package checks do not prove hermetic execution.

After collection and exact process absence, STOP was requested for the one
worker; AWS returned RUNNING to STOPPING. A fresh22:41:46 describe positively
confirmed STOPPED with unchanged Owner/EBS. ROOT communicated its independent
22:42:06 STOPPED confirmation, then canceled the22:54 USER backup and confirmed
inactive. No stop duty, allocation, deletion or further execution remains.
All remote files and the retained EBS remain recoverable. No other worker or
protected project was inspected or touched.

This is producer-run engineering evidence, not promotion. The next permitted
action requires separate authority: first independent runtime-evidence intake
of this frozen packet. An actual-source solver/checker batch remains entirely
separate and unauthorized here. No source acceptance was minted and no generic
toy status is transferred to an actual source ideal, point or JC2 conclusion.

## OPEN(S) RAISED and collisions

New scientific OPEN count:0. One existing engineering obligation remains:
independent review of this finite runtime packet. Cheapest test is its exact
current pins, authority/telemetry/fixture binding and receipt scope review;
no mathematical rerun, extra fixture or solver is authorized. Actual-source
decision status remains unmeasured. No exit-price claim is made.

Collision scope: own output targets were absent at first action; ROOT later
shared only its two immutable registration files explicitly. No existing code,
report or input was replaced. No broad collision or protected-tree search.

Own substantive report read WHOLE at22:45:56; quantity/cheapest-test and
own collision checks completed before this marker. All29 local documentary
input pins remained current; the two ROOT registration pins are additionally
recorded in root-input-pins.json. No unresolved publication placeholder or
new scientific OPEN remains. All execution and remote writers are already
terminal; only the mechanical local transaction/custody freeze follows.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12728`.
- Body SHA-256:
  `17842ae6b685435aa623b9c0137496bf9abaf482a3b82f26f9f06a68c2cfa8b9`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
