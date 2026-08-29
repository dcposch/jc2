# Sigray root-aware AWS recensus R1 preregistration

Date: 2026-08-28

## Frozen gate

This is an engine-only exact-arithmetic recensus.  It consumes the reviewed
root-aware cap repair and does not edit canonical prose or any reviewed engine
source.  The mandatory gate documents are:

- producer SHA-256 `93f98e4df5fd67536f3a5ab9c6f948a6bb06bbdbd10b825980596cc865c811d5`;
- hostile re-review SHA-256 `8381659878f039d17cbc4ebb5a3ac364768d690d4a3895d54c29446f7745b060`.

The six reviewed runtime files must have the hashes printed in those reports:

```text
6905f95e6eeca8f3a8a8468b4c5f56fc131dd4206b2827050ac04ea1939ead8f  cases/sheet6_campaign.py
defcaee8367337d9d882e46fbba1b71bc2db0ce48aaffcf5e44a929d391f3e50  cases/h3_check.py
9a7a0fce73d08f243956d64ff8a85c82a15b9c81f0d07d7cacc0162212fcaf3a  cases/hiii_compose.py
b078c88424c566a8dd37c368e57e9e2aa8932f1bbde49d0c58580940eab806f3  cases/twopole_check.py
c37067fd9f923853ef3a7d5d23c255983e7273466c0df29acf44200c5f29426c  cases/monodromy_td.py
0baf1d54328f0f9829126672536673af277068d4b6dda0221fd94b3c0994d212  cases/sigray_rootaware_smoke.py
```

The now-terminal multipole first-exit hostile review is
`ac49c025e3e010d3ecaf3839adf51c40cb88b0088198ae1c5ab1198e07cc8004`.
Its verdict is `PASS-WITH-REPAIR`, with the ambient quotient/orbit attachment
lemma still a blocker.  Therefore no two-pole or L1 capped display in this
recensus is promoted to a general closure.

## Four independent lanes

1. `common`: current smoke and legacy gates; `bash`, `bash5`, a separate
   td=6 digest (`bash6`), `tduniform` through td=80, and selected full
   `tdu_bash` runs at td=3,4,5,6,7,8,9,10,11,12.  Each selected full run has
   a 12-minute subcap.  A subcap is an explicit `OPEN/NO_VERDICT`, never an
   absence certificate.
2. `h3hiii`: H3/SF1 plus ordinary, pinned, and AF2 HIII compositions.  The
   `OPEN_s_tail` ledger is retained separately and is never closed by its
   finite `s<=40` scan.
3. `twopole`: default exact run followed by a deterministic in-memory raised
   diagnostic with `SMAX=8`, `DEPTH=8`, `KMAX=6`, `NUMAX=72`,
   `SMULT_MAX=18`, `NU1MAX=40`, `L1MAX=8`, and
   `L1_MERGE_LMAX=12`.  A separate root-menu parity probe reaches `l=128`.
   Premerge, interior, root, and L1 output remain diagnostic.  The whole lane
   is `NO_VERDICT` because zero-charge/shared-budget completeness is not
   licensed by the blocked multipole review.
4. `invariants`: compare immutable Git-HEAD pre-repair sources with the
   reviewed sources.  Compare the complete td=3..80 singleton-pole entry
   inventories, pinned entries, monodromy census rows, and the depth-7
   `M>=2` certified-nonroot transition graphs for ordinary and AF2 paths.
   Separately require the repaired root/pole negative controls.  Only exact
   equality earns `PASS`; any mismatch is reported without inference.

Every lane writes separate `ROOT`, `IV`, `OPEN`, and `FRONTIER` ledgers plus
raw stdout/stderr.  `DEPTH` is never filtered by `w<1` at a root: case-I root
merges remain live.  The corrected nonroot Proposition 8.4 filter is used
only where nonroot or pole metadata is explicit.  Singleton budgets may use
the reviewed actual-weight and first-exit theorem; no fixed-weight route is
used.

## AWS contract

- AWS Linux only, DMI `sys_vendor == Amazon EC2`, exact IMDS instance ID and
  hostname gate, fresh job-tagged immutable namespace.
- One pinned CPU per lane, 64 GiB address-space cap, two-hour hard lane cap,
  8 GiB file cap, `SwapTotal=SwapFree=0` before and throughout.
- Source and preregistration hashes are replayed before work.  A smoke failure
  or source drift stops the lane.
- The solver has its own recorded PID/PGID/SID/starttime.  Ten-second CPU/RSS,
  disk, and swap telemetry, TERM/KILL timeout, final process census, terminal
  archive, and exact SHA-256 manifests are mandatory.
- Any timeout, adapter error, uncaught assertion, open tail, or frontier is an
  explicit `NO_VERDICT` at that scope.  No endpoint, Keller-map, or geometric
  existence/nonexistence claim is authorized.

