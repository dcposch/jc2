# First r3 source batch — timeout and worker recovery

Recorded2026-09-11 02:17UTC. Worker i-09bac011c7e8b9368 was TERMINATED
after evidence custody. The exact termination request was02:15:37.742820600;
AWS independently confirmed TERMINATED and an empty nonterminal tagged fleet
at02:16:32. All17 campaign workers are now retired. No idle worker is held
for review. Root100GiB vol-0d25c29e5d1378a76 was independently AVAILABLE with
no attachments at02:16; it is retained. No volume or evidence was deleted;
coordinator and protected infrastructure were untouched.

Before termination, ROOT rechecked exact identity, DeleteOnTermination=false,
API protection=false, all known original PIDs absent, no cgroup and intact
archive. Remote evidence.tar.gz was compared to its source files and fsynced
at02:12:35.410370956. The723935byte archive SHA256 is
0ad12acb76c513326712c643d007dc199e58208a19709216a18111aa090c8945.
Download matched;272 unique regular-file/directory entries in exact approved
paths passed safe-extraction checks, and218 local file pins passed before
fsync at02:14:52.574712643. Local evidence.tar.gz and harvest/ are here.
Retained EBS recovery archive: /home/ubuntu/jc2-r3-source-20260911a/evidence.tar.gz.
Durable original results: /var/lib/jc2-r3-source-20260911a/custody/.
Additional harvest.stdout/harvest.stderr were separately downloaded and pinned.

The first registered13-call batch stopped after9 preflights and its producer.
Producer CAPRUN reports WALL_TIMEOUT,01:54:42.153223–02:09:42.238763UTC,
900.085544615wall seconds, exact-identity TERM15, complete cleanup, no KILL,
empty stdout/stderr and89853952B sampled peak science RSS. No completed
baseline exists. Positive check, mutation and negative check were NOT_RUN.
Custody status STOP_NONDECISION, science_outcome NONE: this is no source
exclusion, rank result, mathematical refutation or JC2 result. No retry,
cap increase or qualification record is licensed by the failed run.

CUSTODY.json SHA256
952a595c7f0b043fcad2c80d4aa8ef6acaa95bad416f06592e518e5cf524bef1.
ROOT independently observed Main0/Control0/failed/failed, cgroup absent and
original8390/8475/8476 absent at02:09:53 BEFORE custody hash FIRST02:10:27
and whole read. The source batch InvocationID is
5241243d3ebe48129cda4a0dd5d92f41. Exact systemd manager journal binds
609705894000ns whole-unit CPU,106471424B peak memory and0swap to that
invocation. The invocation-filtered application journal is empty because
outputs were files; the unit manager journal contains the matching events.

All218 terminal/source/custody pin checks and1226 native-file checks passed
remotely. A fresh full native collector matched every non-timestamp record.
Original SYSTEM03:05/03:05:05 timers closed only after terminal at
02:12:35.318937042; original USER03:11 worker timer closed only after AWS
confirmed termination. No original clock was reset. harvest.sh completed
exit0, stderr empty, with no scientific execution during collection.

Protected retained sole-source vol-0eb6450d18ffa89f1 and older instance-store
archive vol-0be96430c433dfbe2 remain untouched. Storage charges can continue.
