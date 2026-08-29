# D43 exact a00pp sparse rows v3: implementation report

**Status:** `V3_REPAIRED_LAUNCH_NOT_AUTHORIZED` - repaired, review-frozen,
AWS-unregistered, and non-launchable.  No D43 jet was built, no exact row
was emitted, no solve was attempted, no CAS ran, and no AWS action was
taken while preparing this revision.  V1 and v2 are unmodified.

## Revision provenance

This packet answers the v2 hostile review
`xmodel/d43-exact-sparse-rows-v2-hostile-review-gpt56-20260828.md`
(SHA-256 `4f6f6c90e0526ab07591e2ec6a97f475e477b534cb6991085764cd693a99020d`),
which confirmed the v2 mathematical payload and returned REPAIR on the
fail-closed operational contract.  The repair assignment digest is
`27d96f092e7beafd1061dbd1690463a1b36f44d4a5102607c5f56725da393b19`.
The v2 seal (`SOURCE_V2.sha256`) digest
`83635fe45e6f3a9e19d3c93ef963de769f2721653a7bb5333002dd100172fa73` and the
v1 seal digest
`9b851ede56986fe3154cf962f336fda6185fb7a4a00d07888c93e9b78a06848d` are
carried in the manifest provenance.

## Mathematics: v2 preserved byte-for-byte where not forced

`selected_rows_v3.py` carries every v2 mathematical function - the
collapsed K0[W1,W2] arithmetic, `convert_a_orbit`, `collapsed_gm_jet2`,
`collapsed_b_block`, `build_collapsed_side`, `selected_source_rows`,
`expected_collapsed_d21_band20`, the template bridge, the modular replay,
and the 29/155 inventory contract - with these forced edits only:

* every production `assert` became an explicit `CustodyError`/`require`
  check (the algebraic identities in `template_bridge_spec` included);
* the collapsed D21 gate decides by **literal structural equality** and
  literally refuses each mutation (digests are receipts only);
* every payload and receipt binds `run_nonce`, `lease_sha256`, and
  `terminal_authority: false`;
* v1-module facts guarded only by v1's own asserts are re-validated
  explicitly (`require_registry`, `require_sparse_free_support`,
  target/support census);
* `finalize` (which published positive `VERDICT`/`TERMINAL`/`COMPLETE`/
  `FINAL_RECEIPT.json` before custody completed) is replaced by
  `finalize-candidate`, which re-verifies the whole payload chain and
  writes only a non-authoritative candidate;
* schema strings moved to `.v3` and stage entry points take `--lease`.

The conditional flow is unchanged: f and g are independently constructed
under per-side caps, pair custody proves same-host/different-PID with
overlapping closed intervals, and one process emits all 19 shards plus the
184-row merge only after band-20 equality.  `solve=false`; no solver
exists in the packet.

## The eight repairs

1. **Literal D21 gate** (`selected_rows_v3.py::collapsed_d21_gate`): the
   decision is `rows != expected -> refuse`, plus literal inequality of
   each of HW1-negative, HW2-negative, and +42-omitted against both the
   reference and the candidate.  Negative tests feed each mutation and a
   single-coefficient perturbation through the actual gate.
2. **No production asserts**: `ast`-census test proves zero `assert`
   nodes in the three production modules; all three refuse `python -O` at
   import (`OPTIMIZED_PYTHON_REFUSED`), which also covers the frozen v1/
   COMMON dependency asserts; the v2 forged-receipt fixture is now
   rejected under both interpreters.
3. **Exclusive lease** (`aws_launch_v3.sh` + `job_contract_v3.py`):
   atomic `mkdir` job namespace plus nonblocking kernel `flock` held on
   fd 9 for the job lifetime; `RUN_LEASE.json` binds a 256-bit nonce,
   launcher identity/digest, lock dev/ino, archive digest, and
   registration digest.  Every stage and the terminal decision re-verify
   the lease including a held-lock probe; receipts embed the nonce.
4. **Whole-job containment** (`aws_launch_v3.sh` +
   `run_conditional_pipeline_aws_v3.sh`): the supervisor itself runs
   inside the boundary (systemd user scope, or exact-session `setsid`
   fallback); the first side failure cancels and reaps the peer via
   exact-identity `kill-tree`; terminal paths require empty PGID and
   JOB_TAG censuses and (systemd) an empty final cgroup census; the
   launcher performs a post-boundary reap/census and publishes the
   NO_VERDICT authority if the supervisor died without one.
5. **Aggregate limits + sticky monitor**: scope properties
   `MemoryMax=962072674304`, `MemorySwapMax=0`, `TasksMax=512` (verified
   from inside against the manifest); `job_contract_v3.py monitor`
   continuously samples host swap, cgroup memory/swap/pids/oom, and (pgid
   mode) aggregate RSS, writes telemetry/heartbeat/peak receipts, and
   latches violations write-once - a later clean reading can never erase
   one.  Monitor death, staleness, OOM, timeout, and final swap are
   mandatory terminal inputs.
6. **Single late terminal authority**: exactly one `TERMINAL.json`,
   written by `job_contract_v3.py terminal` from ~28 mandatory
   fail-closed inputs and published by atomic rename as the supervisor's
   last successful action.  All earlier artifacts carry
   `terminal_authority: false`; `CURRENT_STAGE` only ever holds
   `RUNNING_*` values; the v2 `VERDICT`/`FINAL_RECEIPT.json`/
   `ARTIFACTS.json` files no longer exist anywhere.
7. **Deterministic immutable archives**: the sealed source archive
   `d43_v3_source.tar.gz` (18 members + census manifest, gzip mtime 0,
   zeroed metadata, mode 0444) at outer digest
   `6497a9dd5c239703e49d0cc110f4e62d5e4ef4bd6d95ffd8fba94977d0b591ed`,
   reproducible via `build_source_archive_v3.py` (two builds in one run
   plus an independent rerun produced identical bytes) and replayed
   member-by-member against the live tree.  The digest is pinned only in
   the external launcher, the packet seal, and future registration -
   never inside the archive or manifest (no self-reference).  The
   run-time terminal archive uses the same builder plus census
   manifest-build/verify, `sha256sum -c`, fresh private extraction
   replay, and outer sidecar replay, all before the terminal decision.
8. **Bounded hostile tests**: 30 fixtures in `test_job_contract_v3.py`
   and 19 in `test_selected_rows_v3.py`, all passing; coverage listed in
   the review request.

## Bounded tests executed (macOS, no CAS, no AWS)

* `test_job_contract_v3.py -v`: 30/30 PASS (~6 s);
* `test_selected_rows_v3.py -v`: 19/19 PASS (~12 s, includes the exact
  D21-prefix and B-block regressions carried from v2);
* `build_source_archive_v3.py` twice: deterministic outer digest, fresh
  extraction replay, members byte-identical to live tree;
* `bash -n` on the supervisor and launcher; `py_compile` on all Python.

Execution gap (disclosed): live `/proc`, cgroup v2, systemd scopes,
`setsid`, IMDSv2, and `sha256sum` behavior is exercised through
injected-reader fixtures and source inspection only; no Linux host ran
this packet.  The first Linux action after a hostile PASS and coordinator
GO must be staging plus preflight on the registered idle host, not the
heavy build.

## Claim tiers (unchanged from v2)

1. A successful run establishes an exact support-specialized a00pp emitter
   and exact inventory for the finite 184-row raw-J truncation.
2. A later exact solve plus mandatory literal E5/E6 reconstruction replay
   establishes only the displayed finite E5/E6/unit extension.
3. Full residue-A/template membership requires every other applicable
   equation.
4. NF equivalence, all-depth compatibility, a Keller map, and a JC2
   counterexample remain separate and unproved.

## Remaining blockers

* a fresh independent hostile-review PASS of this v3 seal;
* coordinator GO;
* fresh immutable registration binding manifest, source list, archive, and
  launcher digests on an idle isolated <=1 TiB zero-swap EC2 host;
* a live-Linux staging rehearsal of the lease/containment path before the
  heavy stages.

**No AWS launch is authorized by this packet.**
