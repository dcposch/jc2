# Hostile review request: D43 exact a00pp sparse rows v3

Please return PASS or REPAIR before any AWS registration or launch.  This
revision answers the v2 hostile review (SHA-256
`4f6f6c90e0526ab07591e2ec6a97f475e477b534cb6991085764cd693a99020d`); its
eight required repairs are the charged roots.  The v2 mathematics was
already confirmed and is intended to be byte-identical here; please verify
that intention rather than assume it.

## Charged roots

1. **Literal D21 gate.**  `collapsed_d21_gate` must decide by literal
   structural equality of the canonical collapsed objects and literally
   refuse each HW1, HW2, and +42 mutation; SHA-256 digests must be receipts
   only.  Feed each mutation through the actual gate and require refusal.
2. **No production asserts.**  No authorization, algebra, semantic,
   receipt, or custody `assert` on any production path in
   `selected_rows_v3.py`, `aws_preflight_v3.py`, or `job_contract_v3.py`;
   optimized Python must reject every forged object identically (import
   refusal plus explicit exceptions).  Attack with `python3 -O`.
3. **Exclusive one-shot lease.**  Atomic fresh-namespace `mkdir` plus the
   nonblocking kernel `flock` held on fd 9 for the job lifetime; the
   256-bit run nonce, launcher identity, and lease identity must be bound
   into every receipt and re-verified (including a held-lock probe) at
   every stage and at the terminal decision.  Attack with duplicate
   launches and stale directories.
4. **Whole-job containment.**  Supervisor, monitor, both side workers,
   emitter, and descendants in one boundary; first side failure cancels
   and reaps the peer; every terminal path proves no PGID/JOB_TAG/cgroup
   orphans.  Attack with supervisor death, peer failure, and surviving
   orphans.
5. **Aggregate limits and sticky monitoring.**  `MemoryMax`,
   `MemorySwapMax=0`, `TasksMax` on the scope; continuous host/cgroup
   monitor with write-once violation latches, heartbeat, telemetry, peak,
   OOM, timeout, monitor-death, and final-empty receipts.  Attack with
   transient swap, OOM counts, timeout, and monitor death.
6. **Single late terminal authority.**  Exactly one `TERMINAL.json`,
   published by atomic rename as the last successful action after every
   payload/custody/archive gate; no positive VERDICT, COMPLETE, receipt,
   or marker earlier (all stage artifacts carry
   `terminal_authority: false`).  Inject failures at every finalization
   boundary and confirm only a single NO_VERDICT authority survives.
7. **Deterministic immutable archives.**  The sealed source archive
   (`6497a9dd5c239703e49d0cc110f4e62d5e4ef4bd6d95ffd8fba94977d0b591ed`,
   pinned only in the external launcher, packet seal, and registration)
   and the run-time terminal archive: safe-member census, embedded
   manifest exact-set/hash replay in a fresh private extraction, and outer
   SHA replay before positive publication.  Attack with corrupted and
   unsafe members and rebuild the source archive from
   `build_source_archive_v3.py` expecting byte identity.
8. **Bounded hostile tests.**  `test_job_contract_v3.py` (30 fixtures) and
   `test_selected_rows_v3.py` (19 fixtures) must pass and must genuinely
   cover duplicate launch, stale directory, supervisor death, peer
   failure, orphan survival, timeout, OOM/resource, transient swap,
   monitor death, late finalization boundaries, archive corruption/unsafe
   members, and `python -O`.

## Additional hostile targets

* The v2→v3 mathematical diff: everything outside the forced custody edits
  should be byte-identical in the shared functions; any silent payload
  change is a finding.
* The wrapper conditional flow: f and g independently constructed,
  same-host/different-PID/overlap proved, one process emitting all 19
  shards plus the 184-row merge only after band-20 equality, solve=false.
* The launcher/supervisor terminal-writer census: no path may pair a
  positive authority with a recorded fault or produce two authorities.
* Self-reference: the archive digest must appear nowhere inside the
  archive; the manifest must not pin the archive or census-manifest
  digests.
* The macOS-portable fixture gap: live `/proc`, cgroup, systemd, setsid,
  and IMDSv2 behavior is verified by injected-reader fixtures and source
  inspection only; no live-Linux run exists yet.

Maximum promotion after a real successful run: exact a00pp
support-specialized emission and inventory of the finite 184-row raw-J
truncation.  It is not point existence, full-template existence, NF
equivalence, all-depth compatibility, a Keller map, or a JC2
counterexample.  **No AWS launch is authorized by this packet.**
