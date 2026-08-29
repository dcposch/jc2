# Producer report: D43 exact sparse-row emitter v3 independent repair

Date: 2026-08-28
Producer: Fable 5 (equal-standing producer lane)
Packet: `cases/d43_exact_sparse_rows_v3_20260828/`
Status: **V3_REPAIRED_LAUNCH_NOT_AUTHORIZED**

Controlling inputs, verified before work began:

| Input | SHA-256 |
|---|---|
| v2 hostile review (charge) | `4f6f6c90e0526ab07591e2ec6a97f475e477b534cb6991085764cd693a99020d` |
| repair assignment | `27d96f092e7beafd1061dbd1690463a1b36f44d4a5102607c5f56725da393b19` |
| immutable v2 seal `SOURCE_V2.sha256` | `83635fe45e6f3a9e19d3c93ef963de769f2721653a7bb5333002dd100172fa73` |
| immutable v1 seal `SOURCE.sha256` | `9b851ede56986fe3154cf962f336fda6185fb7a4a00d07888c93e9b78a06848d` |
| TRIPLE02 R5 custody pattern | `xmodel/triple02-proper-open-resume-r5-hostile-review-fable5-20260828.md` |

Constraints honored: no `jc2-lean` access; no AWS, Singular, msolve, or
heavy/local CAS; v1 and v2 untouched; writes confined to the fresh v3
packet plus this report.  No D43 side jet, D43 row, solver run, or
candidate was produced.

## What v3 is

A new sealed packet that preserves the v2 mathematics byte-for-byte
wherever a change is not forced and repairs all eight launch blockers from
the v2 hostile review.  The heavy flow is unchanged: independently
constructed f and g sides under per-side caps, pair custody proving
same-host/different-PID overlapping construction, the collapsed-D21
band-20 gate, and one process emitting all 19 shards plus the 184-row
merge only after band-20 equality.  It remains an emitter only
(`solve=false`).  A successful future AWS run can claim only the finite
support-specialized raw-J row packet - not a point, not the
E/unit/template extension, not all-depth compatibility, not a Keller map,
and not a JC2 counterexample.

Architecture (following the TRIPLE02 R5 pattern, adapted to this
two-side job rather than copied):

```text
aws_launch_v3.sh (external, hash-pinned; NOT in the archive)
  -> atomic mkdir job namespace + kernel flock held on fd 9
  -> archive outer-SHA check, safe-listing, extraction,
     embedded-manifest replay, contract-level fresh-extraction replay
  -> RUN_LEASE.json (256-bit nonce, launcher identity, lock dev/ino)
  -> containment boundary (systemd scope MemoryMax/MemorySwapMax=0/
     TasksMax, else exact-session setsid fallback)
       run_conditional_pipeline_aws_v3.sh (supervisor, inside boundary)
         sticky monitor (heartbeat, telemetry, peak, write-once latches)
         preflight -> source check -> BUILD_F || BUILD_G (peer-cancel)
         -> pair -> conditional emit -> finalize-candidate
         -> monitor stop -> cleanup + orphan censuses + cgroup census
         -> terminal manifest/archive build + fresh-extraction replay
         -> job_contract terminal decision -> atomic mv TERMINAL.json
  -> launcher post-mortem reap/census; emergency NO_VERDICT only if no
     terminal exists; never overwrites one
```

## The eight repairs (all implemented and independently exercised)

1. **Literal D21 equality.**  `collapsed_d21_gate` decides by literal
   structural equality (`rows != expected` refuses; each HW1, HW2, and
   +42 mutation must be literally distinct from the reference and from
   the candidate).  Digests remain receipts only
   (`digests_are_receipts_only: true`).  Negative tests push all three
   mutations and a single-coefficient perturbation through the actual
   gate and require refusal.
2. **No production asserts.**  Zero `assert` nodes in
   `selected_rows_v3.py`, `aws_preflight_v3.py`, `job_contract_v3.py`
   (AST-census-tested); all checks are explicit `CustodyError` raises.
   All three modules refuse `python -O`/`-OO`/`PYTHONOPTIMIZE` at import,
   which also covers the frozen v1/COMMON dependency asserts; v1 registry
   facts are additionally re-validated explicitly.  The v2 forged
   preflight receipt fixture (schema FORGED, pass=false, wrong hashes) is
   now rejected under both interpreters.
3. **Exclusive one-shot lease.**  Fresh atomic `mkdir` namespace plus a
   nonblocking kernel `flock` held on launcher fd 9 for the job lifetime.
   `RUN_LEASE.json` binds nonce, launcher pid/starttime/uid/digest, lock
   dev/ino, archive digest, and registration digest.  Every stage and the
   terminal decision re-verify the lease including a fresh-descriptor
   held-lock probe; every payload/receipt embeds
   `run_nonce`/`lease_sha256`/`terminal_authority: false`.
4. **Whole-job containment.**  Supervisor, monitor, both side workers,
   emitter, and descendants share one boundary and one JOB_TAG.  First
   side failure cancels and reaps the peer via exact-identity
   `kill-tree`; traps and emergency paths kill and census the boundary.
   Terminal inputs require empty PGID and JOB_TAG censuses and (systemd)
   an empty final cgroup census; the pgid fallback has exact
   session-leader identity, JOB_TAG census, bounded reap, and the same
   mandatory terminal inputs.  The launcher post-mortem reaps and
   censuses after the boundary exits and fail-closed-publishes
   NO_VERDICT if the supervisor died without a terminal.
5. **Aggregate limits + sticky monitor.**  `MemoryMax=962072674304`,
   `MemorySwapMax=0`, `TasksMax=512` on the scope, verified from inside
   against the manifest; host must satisfy `MemTotal <= 1 TiB`, >= 800
   GiB available, zero swap; one pinned core per heavy side (2 and 3).
   The monitor continuously samples host swap, cgroup
   memory/swap/pids/oom_kill, and aggregate RSS (fallback), latching
   violations write-once so a later clean reading can never erase one;
   monitor death/staleness, OOM, whole-job timeout, and final-empty
   censuses are mandatory terminal inputs with peak/heartbeat/telemetry
   receipts.
6. **Single late terminal authority.**  Exactly one `TERMINAL.json`,
   composed by `job_contract_v3.py terminal` from ~28 mandatory
   fail-closed inputs (argparse `required=True`, strict choices) and
   published by atomic rename as the supervisor's last successful action.
   The v2 `VERDICT`/`TERMINAL`/`CURRENT_STAGE=COMPLETE`/
   `FINAL_RECEIPT.json`/`ARTIFACTS.json` writers no longer exist;
   `CURRENT_STAGE` only ever holds `RUNNING_*`; the producer's positive
   authority is replaced by a non-authoritative
   `FINALIZE_CANDIDATE.json` (`CANDIDATE_PENDING_TERMINAL_DECISION`)
   that re-verifies the whole payload chain.  A static census test proves
   only the guarded supervisor/launcher sites can publish the terminal.
7. **Deterministic immutable archives.**  Source archive
   `d43_v3_source.tar.gz` (18 members + census manifest, sorted USTAR,
   zeroed owner/mtime, mode 0444 members, gzip mtime 0; file chmod 444):
   built twice in one run and once in an independent rerun with identical
   outer digest, replayed by fresh private extraction with safe-member
   census and embedded-manifest hash replay, members byte-identical to
   the live tree.  The outer digest is pinned only in the external
   launcher, the packet seal, and future registration - never inside the
   archive or manifest (no self-reference).  The run-time terminal
   archive reuses the same deterministic builder plus manifest-build/
   verify, `sha256sum -c`, fresh-extraction replay, and outer sidecar
   replay, all strictly before the terminal decision.
8. **Bounded hostile tests.**  49 fixtures, all passing (below).

## Tests run (bounded; macOS host; no CAS, no AWS)

* `test_job_contract_v3.py -v`: **30/30 PASS** (~6 s).  Coverage:
  duplicate-launch flock refusal; lease record/verify plus seven lease
  forgeries; released-lease refusal; stale-directory refusal for
  terminal/output/custody/stray/archive/record artifacts; injected-proc
  identity, PGID and JOB_TAG censuses; identity-drift signal refusal;
  kill-tree reap with orphan detection; strict cgroup census (including
  the non-ASCII-digit line); monitor clean run, transient-swap
  stickiness, timeout, OOM, memory-over-max, pids-over-max, unreadable
  cgroup, supervisor-death detection, aggregate-RSS enforcement; terminal
  decision positive case, all 22 single-latch flips, nonempty/missing
  censuses, six candidate forgeries, missing sidecar, lease failure,
  omitted/malformed argument refusals; archive determinism, replay,
  census/hash drift, traversal/absolute/symlink/duplicate/extra/
  missing-manifest/tampered members, corrupt outer bytes; `python -O`
  refusal of all three production modules and identical rejection of the
  v2 forged-receipt fixture under both interpreters.
* `test_selected_rows_v3.py -v`: **19/19 PASS** (~12 s).  Carries the v2
  mathematical surface (432-basis scope, literal a00pp collapse and sign
  mutations, EB refusal, pre-multiplication orbit collapse, exact
  D21-prefix B-block and collapsed-engine regressions, selected-component
  commutation, template bridge symbolic plus both registered modular
  points, 29/155 inventory, 184 cover) and the v3 fixtures (literal gate,
  mutation refusal through the actual gate, unregistered-manifest and
  unheld-lease refusal, no-early-authority and single-terminal-writer
  censuses, zero-assert census, JOB_TAG-aware preflight census).
* `build_source_archive_v3.py` twice: deterministic digest, fresh
  extraction replay, live-tree byte identity.
* `bash -n` on supervisor and launcher; `py_compile` on all Python;
  operational-source-list replay and manifest binding replay.

## Review request

`REVIEW_REQUEST_V3.md` (SHA-256
`0355a664cc22d4ed7127a84b69c5723f19e90fb03c1d5a11705bf488004d51cf`)
charges the eight repairs as roots and adds hostile targets: the v2->v3
mathematical diff (byte-identity intention), the conditional flow, the
terminal-writer census, self-reference, and the macOS fixture gap.

## Residual limitations

* **No live-Linux execution.**  `/proc`, cgroup v2, systemd scopes,
  `setsid`, `sha256sum`, prlimit/taskset/timeout chains, and IMDSv2 were
  exercised via injected-reader fixtures and source inspection only.
  After a hostile PASS and coordinator GO, the first AWS action must be
  staging the sealed archive plus launcher into a fresh namespace on the
  registered idle host and rehearsing preflight/lease/containment before
  any heavy stage.
* The systemd/pgid boundary was not probed against a real user manager;
  the fallback's aggregate-memory enforcement is monitor-latch-based
  rather than kernel-based (disclosed in the manifest containment block).
* The supervisor-in-boundary design means the final self-census excludes
  the finalizing supervisor chain itself; the launcher post-mortem
  census closes that gap after exit, and no path can create a positive
  authority after the supervisor's single rename.
* `finalize-candidate`'s full happy path (Linux-only preflight receipt)
  is unexercised end-to-end off-Linux; its refusal paths and the
  contract-side candidate binding are fixture-tested.
* The 155/29 inventory remains a preregistered forecast; no v3 rows
  exist.

## Hashes

Packet seal `cases/d43_exact_sparse_rows_v3_20260828/SOURCE_V3.sha256`
(34 entries, covering every packet file, the sealed archive, both prior
packet seals, all frozen dependencies, and the controlling reviews):

```text
5423bd88328c338c54072b056d3f64251dc57de6f5112646f9d157f991ab5271  SOURCE_V3.sha256
6497a9dd5c239703e49d0cc110f4e62d5e4ef4bd6d95ffd8fba94977d0b591ed  d43_v3_source.tar.gz (outer, pinned in aws_launch_v3.sh)
611e03fb37ed22340ffc92b739115678ec5523d525682847b18a91e61e435eb2  SOURCE_ARCHIVE_MANIFEST_V3.sha256
bcc7ca64550cea460939ad3d2831707de8bca194b0e2fe6e027e34a5fdb0d416  OPERATIONAL_SOURCE_V3.sha256
d6b9185a809bfb3744e477cea4a5bbbf0a0e70162031a082b09729b38f046ba8  PIPELINE_MANIFEST_V3.json
3a29c8495b03026feda09b3b0629f95a7f69c41fbe9adf89fc6ad44e2945f9da  selected_rows_v3.py
62911609df8872b74a56d385f9c402725a3a8f6faa9138f19dfef47f295e2d9f  job_contract_v3.py
4952cefd18831ee8f1514fb9860b8ab122ca25b34aeb251174590891b4b00365  aws_preflight_v3.py
b7fa2dda8ef167006d86196ebb05d4d1506accc2474733d00bc88b31b65e746b  run_conditional_pipeline_aws_v3.sh
0deefc4209e27291c274c95faf15e75ac91eaa1130d0e575f4f4a9e84a0580ee  aws_launch_v3.sh
94bd3b6dca497ab27e6c547338188484816e6ea69b6b1b36391bb95af4c03347  build_source_archive_v3.py
3416642e32061e6656f49f79ac30027df424e7d413b0f0c5e3596d8f0c9db527  test_job_contract_v3.py
bf98755324f7160b068b35bcda3b693439e9f32f12f74f0711652fa7f46717cf  test_selected_rows_v3.py
17f83b4c2f50a6c742a74b2153eaf8b1d008458da75935989818072b43deb11b  IMPLEMENTATION_REPORT_V3.md
0355a664cc22d4ed7127a84b69c5723f19e90fb03c1d5a11705bf488004d51cf  REVIEW_REQUEST_V3.md
b47f8f4cbbe120446cef752a4d82f4137aae5c9172b773718a421347e258515b  PREREGISTRATION_V3.md
39855047cafe29aee5f48b76662cfc9e74103dd43ea258e03b3dd7786c579eb1  SUPERSESSION.md
4fd167f52b359cc6042a0b61e1ebf13f31b60c441b8e23b1bb1d2a000e3027bb  LEDGER_PATCH_REQUEST.md
```

This report cannot contain its own digest; the coordinator can seal it
with:

```text
shasum -a 256 xmodel/d43-exact-sparse-rows-v3-repair-fable5-20260828.md \
  > xmodel/d43-exact-sparse-rows-v3-repair-fable5-20260828.md.sha256
```

## Authorization statement

**No AWS launch is authorized.**  The packet status is
`V3_REPAIRED_LAUNCH_NOT_AUTHORIZED`; the review manifest is deliberately
AWS-unregistered and every compute entry point refuses it.  Launch
additionally requires, in order: a fresh independent hostile review PASS
of this exact v3 seal, the coordinator's separate GO, and a fresh
immutable host registration binding the manifest, source list, archive,
and launcher digests.  Nothing in this report promotes any v1, v2, or v3
mathematical claim: no D43 v3 jet, row, inventory, point, or verdict
exists.
