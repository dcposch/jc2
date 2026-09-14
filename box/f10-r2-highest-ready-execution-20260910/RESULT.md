# Highest-certificate batch: evidence and worker recovery

2026-09-10, recorded17:47 UTC. Worker i-05b82c8e457c586ce is TERMINATED;
100GiB gp3 root vol-036bd8601bfa8db53 is retained AVAILABLE/unattached.
No EBS was deleted. Fourteen campaign workers retired in total; live tagged
nonterminal fleet query17:43 returned an empty list. Protected infrastructure
was not inspected or changed.

The c7i.xlarge worker launched17:17:15 and executed the registered13-call
batch17:25:02–17:25:13. Result HIGHEST_CHECKED_NEGATIVE_CONFIRMED, scienceNONE:
10.538040129 wall seconds /8.93415 cgroup CPU seconds. The354-byte highest
candidate passed its independent checker; a354-byte one-cofactor mutation
was rejected at the exact mathematical identity branch. FIRST result review
is pending; this is not a full-source unit, source exclusion or JC2 resolution.
The [ROOT report](../../xmodel/f10-r2-highest-ready-actual-root-20260910.md)
is SHA272f2b4b460a51a9478f2e393b4c295a0531286cfce16ec68d44a00349959bd4;
expected transaction43d38fb6241034851f85c2b2e91ce290acf7649afd347b5637c85fbe57235ef0
VERIFIED17:43. CUSTODY.json SHA
f8fc2182a7eb3ce888f639e6ce4030f18b8bed0532d46e0604042dada4f10f10.

Independent SYSTEM terminal MainPID/ControlPID0 and original process/cgroup
absence17:25:28 and17:25:56 preceded custody intake. Complete remote281
terminal +21 installed pins and1226 native checks were retained. Original
harvest.sh had an oldT1620 timer-name typo: it failed AFTER postchecks but
BEFORE archive. The retained harvest-complete.sh rechecked custody, native
comparison and quiet state, closed the correct T1720 timers17:28:43.295593450,
and archived without rerunning science or resetting any cap.

Recovery archive: /home/ubuntu/jc2-r2-highest-ready-20260910T1720/evidence.tar.gz
on vol-036bd8601bfa8db53; same evidence.tar.gz is saved in this local directory.
Archive SHA e91ba628c5643a346003673ce110dd3e8bf0f0dc4228c719c174105b70798fdd,
2209751bytes. Remote tar comparison and fsync completed17:28:43.666314287.
Local safe extraction into harvest/ checked351 unique regular-file/directory
entries in four exact roots, then302 mapped file hashes and fsync BEFORE
one-ID termination17:30:33.088800303. See local-extracted-files.sha256,
local-extracted-files-recheck.log, termination-request.txt,
termination-confirmed.json and retained-volume-confirmed.json.

TERMINATED/AVAILABLE confirmed17:31 and17:33. Original USER worker-termination
timer closed17:32:15.540923424 after confirmation. No restart, process monitor,
worker timer or paid idle compute remains. Sole-source vol-0eb6450d18ffa89f1
and former instance-store archive vol-0be96430c433dfbe2 remain protected data.
