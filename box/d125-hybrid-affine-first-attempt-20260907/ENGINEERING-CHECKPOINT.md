# Frozen engineering checkpoint — no production attempt yet

2026-09-07. Engineering-only batch TERMINAL PASS. The eventual attempt report
remains unfinalized. This checkpoint and its referenced evidence are now frozen;
all local/remote writers and controlled groups are terminal. No production GREEN
has been issued to this owner, and no construction/replay/solver was invoked.

Authority: root HYBRID-ENGINEERING-GREEN SHA
12ef766b820b4ef486b4b3286eb0d46f2b41e5630488477f67170874cc2d8a36.
Exact registration1ef0444a0778d13c2bf79fe1df51a82643478532716dd94434a04a412e0f12e6,
instance i-0da0cebfc97c9fd54, boot bef732b9-38e5-4a9a-8f93-77203426d2b8.
Root retains STOP; NEVER terminate/delete retained EBSvol-0eb6450d18ffa89f1.

Exclusive deployment at05:31:58 verified the seven authorized file hashes and
exact source byte-hash b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac.
That was opaque byte hashing only, explicitly permitted by this GREEN. No source
row parsing or coefficient arithmetic occurred. Controls themselves had source
access fenced off. Only the pinned wrapper, constructor/replay/baseline, CAPRUN,
registration and physical GREEN were deployed; controllers/readers ran from stdin.

Controller1536/PGID1536/start58870 dispatched authorize runner1537/start58875 at
05:34:15.810735. Its payload1538/PGID1538/start58879 ran05:34:15.854121–15.923555,
NORMAL_EXIT0,0.069437704s, sampled peak RSS10,194,944 bytes. The real frozen
authorize and tiny normalized Hermite/lift control passed; stdout145 bytes,
stderr0. Its token had9.496787s remaining at spawn. After terminal PASS and group
absence, the spent token was hash-verified and recoverably moved to
engineering/authorize.authority.json, SHA
230a119b6beb6598da34009a3abe90396e8253384bc10d6b061c12d4393b1323.

Conditional RSS runner1541/start58889 dispatched05:34:15.954547; payload1542/
PGID1542/start58894 ran05:34:15.996837–16.568011,0.571174553s. Its descendant1544
ignored TERM as the fixture requires. CAPRUN reported RESOURCE_CAP/rss, runner125,
TERM then KILL with matching start identity, leader reaped and cleanup_complete.
Sampled peak RSS167,108,608 bytes illustrates permitted sampling/allocation
overshoot above the64MiB threshold; it is not labelled a hard RSS ceiling.
Stdout46 bytes, stderr0. The token had9.496668s at spawn. The final RSS token
remains at root/authority.json, SHA
d3a16840b13b51bb503c26416cab1fa79c316599acf1e0d4b9fb9ffb8e0e1f17.
No production upgrade or further token move is authorized by this checkpoint.

Combined batch arithmetic0.792160835s. Actual post-authorize limits were512MiB AS,
10 CPU seconds,128MiB FSIZE per regular file and core0 for both controls. CAPRUN's
wall cap was10s each; RSS thresholds512MiB/64MiB. Every remaining token and source
artifact is preserved. No retry or cap enlargement occurred.

Terminal telemetry was read before result interpretation. Fresh read-only custody
at05:35:34.195532 found all PIDs1536,1537,1538,1541,1542,1544 absent and every member
of groups1536,1538,1542 absent. construction.jsonl and replay-result.json remained
absent. All four deployed payload/CAPRUN pins and the wrapper pin were unchanged.
Compact copied evidence is under evidence/; the moved authorize packet and current
RSS packet both exactly match their issuance hashes. Twenty-one copied files plus
the unchanged pinned wrapper (22 checks) match byte lengths and hashes. The
metadata-only verifier passed normally and−O, including actual limits, dynamic
expiry, output hashes, status and termination checks. It reads no mathematical
source and makes no proof/point/ideal claim.

Frozen checkpoint inputs:

- engineering-custody.json52d4dc9584f74494b25440974a5399eb30072b6daa254d3c213aaa550cbb0fa7
- deploy.py aefb9cbad5cde8cad2cc631c607744e97fea20eb443ad7f5cfe09b8915c284d0
- engineering_batch.py25ef56f4092c4f30b4bedf58a715e559a9e87fd95de8d57026477a3f80cedfe5
- harvest_engineering.py841fee0c7d40509234bc3e3b738397b94ed916ce3d8a4d65120f69627715d587
- verify_engineering.py8921e68106a2a5ff146a2626bf7dbe3ebe0d051d33c30c5228440a4bc1b5ccff

The custody JSON pins all22 remote compact artifacts and records exact metadata;
the original readiness.py/readiness.json/REGISTRATION.md are unchanged. Root may
consume this checkpoint after IDLE and decide a separate production GREEN. Shared
engineering-token scope remains cooperative exact dispatch, not security isolation.
