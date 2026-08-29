# TRIPLE02 node-1 closed-successor resume: AWS preregistration R1

Date: 2026-08-29 (packet authored 2026-08-28)

Status: `R1_SOURCE_PACKET_LAUNCH_NOT_AUTHORIZED`

No AWS launch is authorized by this document.  Launch requires a passing
independent hostile source review by a different model and a separate
coordinator `GO`.

## Exact scope

This packet computes only on the TRIPLE02 node-1 closed successor
`V(I_node1 + (Delta_node1))` over `R = Q[q0,q2,c4,c6]` with `dp` order, by
the frozen r5 finite chart recursion with global node numbering starting at
node 2 and at most 6 new nodes.  It does not touch the settled node-1 proper
open, the whole TRIPLE02 stratum, any other component, the ambient endpoint
problem, or `jc2-lean`.  The mathematical terminal markers are exactly the
four preregistered classifications in `PREREGISTRATION.md`; everything else
is `CUSTODY_OR_ADAPTER_FAILURE_NO_VERDICT`.

## Frozen inherited inputs

| artifact | SHA-256 |
|---|---|
| R3 terminal archive `cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_complements_r3_20260828/custody/terminals/ggv_endpoint_complement_triple02_r3_20260828T175423Z_i0f089.terminal.tar.gz` | `e5bdd2b25cde0dccd8f1e6b8f0e1fcc815d409426308afb49c45df86af53a1e1` |
| Reviewed proper-open R5 terminal archive `cases/ggv_8_28_upper_endpoint_triple02_proper_open_resume_r1_20260828/custody/terminals/ggv_triple02_proper_open_resume_r5_20260828T233745Z_r6d.terminal.tar.gz` | `4b8ffc1c16828b22b2e76a3aa92a25e8c1f472190a708f30a7b71ba952cbef7e` |
| Frozen r5 recursor `cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_complements_r5_20260828/recurse_component.py` | `d679a4d7fb4bf2619fbb3ff47ea6f386ba1c75fdc477276cabf3bec8a2b2cd90` |
| Frozen transcript gate `cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_complements_r5_20260828/transcript_gate.py` | `0e0efd5ada59039a373a731038f2f88a3794b376b208879c2459bff97d0e7316` |

The preparer verifies both archive hashes, performs a complete member census
(no links, devices, specials, absolute paths, traversal, or duplicate names),
requires a unique exact path and pinned hash for every consumed member, and
refuses to extract the node-1 open-route products
(`NODE_001_OPEN_SAT_STANDARD_BASIS.txt`, `saturation.sing`).  Material R3
member hashes are pinned in `prepare_resume.py`; the archived node-1
saturation record must read cap 900 s, rc 1, `timed_out: true`, with the
exact six-marker prefix and no completion marker, and stays
`TIMEOUT_NO_VERDICT`.  From the proper-open archive only
`output/VERDICT.txt`, `output/SUMMARY.json`, and
`custody/CANDIDATE_MATHEMATICAL_VERDICT.txt` are extracted, all three of
which must read `EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY` with scope
`TRIPLE02_NODE1_D_DELTA_ONLY`; they are routing provenance only.

## Deterministic build and semantic replay

Before production, on the host:

- the builder imports the frozen r5 recursor by pinned hash and reproduces
  the archived node-1 `reduce.sing` **and** `rank_size_6.sing` (and its
  support census JSON) byte-for-byte from the archived `work/base` tree;
- the inherited rank-six bound is re-verified from the pinned rank archive
  inside `work/base` (`b947a2d3...` / member `cc6dc1c4...`);
- the two pre-runnable generated scripts must match the manifest-covered
  pins in `runtime_expectations.env` and `EXPECTED_GENERATED_SCRIPTS.sha256`:
  the node-1 witness replay script and the node-2 reduce script;
- the recursor regenerates the node-2 reduce script at run time and requires
  byte equality with the builder's copy;
- the no-CAS generator selfcheck must reject the preregistered mutation set
  (archive hash, traversal member, open-route member selection, witness delta
  literal, saturation injection, route-guard deletion, ring order, ungated
  power search, reverse-marker deletion, settled-delta reuse in saturation or
  chart, post-base-change repivot, count-gate flips, classifier
  driver-verdict swap, chart residual tamper, plant-marker drop, `node_001`
  directory) and pass the dead/survivor classifier positive controls.

Stage scripts for nodes are generated during the run by the same pinned
builders; each stage's script hash, stdout hash, stderr hash, return code,
and timeout flag are recorded in a per-stage result JSON and re-verified by
the classifier.

## Controls before production

- the hostile invalid-list-slot diagnostic with an expected-diagnostic
  parser (any Singular diagnostic fails a clean gate regardless of rc);
- the clean adapter selfcheck: proper two-containment `(x*y),x,(y)` with zero
  pure-power reductions, strict overideal `(y,x-1)` adversary that passes
  weak predicates but fails reverse containment, empty `(x^3),x` power route
  with exponent 3, reducer adversary, endpoint two-shift plants with the
  innocent `e=-1` case, bordered plant, and the closed-successor separation
  fixture `J=(x*y,y)`: `Delta_parent in J`, `J` proper,
  `sat(J,Delta_parent)` the unit ideal.

## AWS custody and resource contract

Identical in structure to the reviewed proper-open R5 stack, with these
parameters:

- Fresh immutable job namespace (atomic `mkdir` lease), source archive
  installed read-only at mode 0400, source tree `chmod -R a-w`.
- Linux, `/sys/class/dmi/id/sys_vendor == Amazon EC2`, IMDSv2 instance and
  hostname binding, IMDS-visible `CodexJob=$JOB_TAG` instance tag.
- One pinned core; at most 1 TiB physical RAM; 256 GiB process
  virtual-memory limit; 64 GiB file-size limit; zero configured swap before,
  during (10 s telemetry), and after.
- Stage caps: controls 60 s; witness replay 900 s; every node stage
  (reduce, each rank size, saturation, chart) 3,600 s.  Whole supervisor
  budget: 21,600 s with sticky TERM/KILL, exact-PGID or delegated systemd
  scope containment, bounded 10 s launcher reap by PID start time,
  full tagged orphan censuses, and strict `cgroup.procs` content parsing.
- A stage timeout inside the recursion is a *bounded no-verdict* recorded by
  the driver (`STAGE_TIMEOUT:<node>:<stage>`), not a crash; the supervisor
  whole-job timeout and any custody irregularity remain
  `CUSTODY_OR_ADAPTER_FAILURE_NO_VERDICT`.
- Singular normalized-version SHA-256 (random seed normalized):
  `f16fa01f3d3bdb83ac08dc7dbc25ebd84ba147bf3433779a0f5c695cee9ad9ec`.
- `elim.lib` SHA-256:
  `cb39b70a6cff9f1bf6b6397b9de3a597f6bb9d91dad468243bed9bfb2552fcd1`.
- `run_singular_stage.py` never creates a nested session; PGID/SID of every
  Singular child are validated against the worker containment before and
  after launch.

The worker never publishes a terminal.  It banks a classifier candidate only
after the independent classifier re-derives the identical classification from
stage artifacts, the artifact manifest replays, the final zero-swap check
passes, and the scope firewall marker
`CLOSED_SUCCESSOR_RESULT_BANKED_WITHOUT_WHOLE_STRATUM_OR_JC2_PROMOTION` is
written.  The supervisor requires worker rc 0, all sticky latches clean, empty
orphan/tag/cgroup censuses, terminal-manifest build + independent replay, a
fresh-directory archive extraction replay of the embedded manifest, and only
then atomically installs the terminal archive and, as the final action, the
one-line `TERMINAL.marker`.  Candidates outside the four preregistered
classifications are downgraded to `CUSTODY_OR_ADAPTER_FAILURE_NO_VERDICT` by
`containment_contract.py`, which also rejects the settled-open campaign's
candidate string as foreign.

## Launch integration

The archive-external `aws_launch_preflight.sh` (frozen in
`LAUNCH_MANIFEST.sha256` together with the source-archive sidecar) pins the
literal source archive hash, validates every member name/type/prefix and the
exact member count before extraction, installs the archive read-only,
verifies `SOURCE_MANIFEST.sha256`, write-protects the source tree, exports
`EXPECTED_SOURCE_ARCHIVE_SHA256`, and `exec`s the supervisor.  The expected
launch environment is
`SOURCE_ARCHIVE`, `JOB_ROOT`, `JOB_TAG`, `CPU_ID`, `EXPECTED_INSTANCE_ID`,
`EXPECTED_HOSTNAME`.  Job tags use the prefix
`ggv_triple02_closed_successor_resume_r1_`.  No nearby branch, open-route, or
whole-stratum job may be launched from this packet.
