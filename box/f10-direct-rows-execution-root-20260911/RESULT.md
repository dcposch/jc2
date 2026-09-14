# Direct-row r3 batch — internal term-cap stop and worker recovery

Recorded2026-09-11 05:18UTC. JC2 remains unresolved. The batch produced no
baseline, source agreement, rank witness or source-exclusion result.

The producer exited1 normally after218.021168898wallseconds, from
05:03:41.735535 to05:07:19.756697UTC. Its exact traceback reaches
produce.py274 (inverse-chart transformed-polynomial addition), then
arithmetic.py204/169: ValueError STOP_INTERNAL_TERM_CAP. The actual guard
rejects len(poly)>100000. This is not a wall/CPU/RSS exhaustion, a mathematical
anomaly or a source refutation. The traceback does not identify which of the
two inverse-chart iterations exceeded the guard or the eventual final support.
Sampled producer RSS peak67461120B; stdout empty; no completed payload.
Positive checker, T mutator and negative checker were NOT_RUN.

All seven frozen refusal triples matched exactly. ROOT-policy valid and
the dummy descendant RSS/TERM15/KILL9/identity/cleanup predicates passed their
metadata comparisons. All ten recorded commands matched registration, and
all ten runner captures were present. The fast startup-produce Python capture
was missed and is disclosed; the actual scientific producer capture exists.
These facts do not qualify a scientific baseline. See ROOT-TERMINAL-PREDICATES.json.
No local scientific replay or extra AWS science was performed during harvest.

Dispatcher InvocationID2c97ab475b254ff8ae8b2b091118c53b ran05:03:31–05:07:20,
ending2 with custody STOP_NONDECISION / unexpected control/phase outcome and
science_outcome NONE. Matching manager journal records153100505000ns whole-unit
CPU,102072320B peak memory and zero swap peak. These are not model billing.
ROOT independently established Main0/Control0/failed, original8570/8663/8664
absent, cgroup absent and no matching scientific/wrapper process at05:08:53,
BEFORE custody hash-FIRST/full metadata intake. CUSTODY.json21912B SHA256:
46194928c58f2b271adaca4d0bce3cfdd6a3a0d740fddcfd48b93bf824c9194f.

All103working+103durable+custody+17installed=224pins passed remotely and locally.
All1226native file pins passed; fresh full collection matched every
non-timestamp record. The exact metadata-only harvest port completed exit0,
stderr empty; original remote science timers closed AFTER terminal at
05:12:27.960097329, with no clock reset. The752150B evidence.tar.gz was
compared to every archived source and fsynced at05:12:28.057809700UTC.
Archive SHA256 fd5a486b0eae21f082d432889e7bca83829a2649cd0faf37a0b19c698a076a3c.
Download matched; all285unique archive entries were regular files/directories
inside the explicit allowed paths, then extracted to fresh harvest/.
The224local pin checks were repeated fail-closed/quiet before retirement;
local archive and extracted evidence were fsynced.

Worker i-031b57c489417e1d1 launched04:48:33UTC. Exact termination request
05:14:05.023501758 followed fresh identity/boot/quiet/archive checks and
observed DeleteOnTermination=false/API-protection=false. AWS independently
reported TERMINATED at05:15:35, rootvol-0d500f329b88c6152 AVAILABLE/unattached,
100GiB, and an EMPTY tagged nonterminal fleet. All18campaign workers are now
retired per this and prior recovery records. Original06:16 exact-ID backup
timer closed05:16:05.737131777 only after termination confirmation.

Retained EBS archive path: /home/ubuntu/jc2-r3-directrows-20260911a/evidence.tar.gz.
Original durable evidence: /var/lib/jc2-r3-directrows-20260911a/custody/.
Local evidence.tar.gz, harvest/ and separately pinned harvest.stdout/.stderr
are beside this record. No volume/evidence deletion or protected-infrastructure
action occurred. Protected sole-source vol-0eb6450d18ffa89f1 and older archive
vol-0be96430c433dfbe2 remain untouched; storage can continue to incur charges.

Next work is a bounded STATIC inverse-representation design, not a retry or
cap increase. It must retain both entire inverse polynomials/windows/poles,
every diagnostic and the complete25-row circuit. No new implementation,
execution or rank-client release follows from this failed run.
