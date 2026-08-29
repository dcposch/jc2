# Closed-successor resume R4: local preflight report

Date: 2026-08-28 (macOS host, pure Python; no Singular/CAS executed).

## What ran locally

1. `python3 -m py_compile` and `python3 -O -m py_compile` over all eight
   packet Python files — pass; `bash -n` over the three shell scripts —
   pass.
2. `prepare_resume.py` (byte-identical to R2/R3) against both real frozen
   archives — pass, including the exact member-census hard gates
   (`R3_ARCHIVE_EXACT_CENSUS=454:391:63`,
   `PROPER_OPEN_ARCHIVE_EXACT_CENSUS=574:490:84`),
   `R3_SELECTED_EXTRACTED_FILE_COUNT=294`,
   `SETTLED_OPEN_EXTRACTED_FILE_COUNT=3`, open-route members excluded,
   archived timeout revalidated, settled-open verdict revalidated.
   Evidence: `preflight/R4_PREPARE.stdout.txt`.
3. `build_resume.py` (byte-identical to the reviewed R1/R2/R3 builder) —
   pass; the generated witness-replay and node-2 reduce scripts reproduce
   the R1/R2/R3 pins exactly (`27cb8508...59d0d`, `d9e79b42...d8b8`; full
   values under "Pinned outputs" below), so the resumed mathematics is
   unchanged.  Evidence: `preflight/R4_BUILD.stdout.txt`,
   `preflight/generated/`.
4. `generator_selfcheck.py` under `python3` AND `python3 -O` (stdout
   byte-identical, 48 lines) — pass, and **byte-identical to the R3 banked
   `R3_GENERATOR_SELFCHECK.stdout.txt`**, so the mathematical generators,
   Singular scripts, rank census and terminal allowlist are unchanged from
   R3.  Evidence: `preflight/R4_GENERATOR_SELFCHECK.stdout.txt`.
5. `containment_selfcheck.py` under `python3` AND `python3 -O` (stdout
   byte-identical, 39 marker lines, empty stderr, rc 0) — pass.  All R3
   controls retained (the R2 review's working O-B1 forgery, extraction
   edit/deletion/extra/symlink, archive/extraction mix-and-match, archive
   replacement/symlink/wrong-digest, fault-latch regression + worker-rc
   disagreement, five-property runtime-limit mutations, job-tag stamp
   schema — every late-decision fixture through a real freeze), **plus the
   new R4 controls**:
   - a structural single-open assertion over the contract source (the R3
     two-open idiom `sha256_path(terminal_archive)` /
     `tarfile.open(terminal_archive)` is absent; `open_frozen_archive`,
     `require_stable_archive_stat`, `fileobj=handle` present; exactly one
     `os.open(terminal_archive)`);
   - a **genuine concurrent-rename regression** (real OS thread renames a
     self-consistent forged archive over the charged path while
     `derive_late_decision` runs) across **9** file-count/window
     configurations plus a deterministic rename-before-open case — all
     fail closed (`DECISION_FRESH_ROOT_BYTES_DRIFT` /
     `DECISION_ARCHIVE_HASH_DISAGREEMENT`), 0 promotions; a no-attacker
     positive control promotes the honest bounded no-verdict and its
     marker digest equals the descriptor digest;
   - a genuine in-place append race plus a direct load-bearing test of the
     pre/post `fstat` stability gate (`DECISION_ARCHIVE_UNSTABLE_DURING_READ`);
   - JSON-boolean fault-latch values refused (`worker_rc`, sticky faults);
   - the hitherto untested `swap_zero` decide_terminal gate (the mutation
     table is now **19** load-bearing gates);
   - a malformed late `--archive-sha256` still publishing the custody
     no-verdict marker (rc 3, `TERMINAL_ARCHIVE_SHA256=NONE`).

   42 `expect_rejection` call sites in the suite.  Evidence:
   `preflight/R4_CONTAINMENT_SELFCHECK.stdout.txt`,
   `preflight/containment_selfcheck.json` (its `decision_record_sha256`
   embeds timestamps and is not a usable charge; the stdout markers and the
   recorded race outcomes are).
6. `resume_recursor.py` fail-closed dry run under `python3` AND
   `python3 -O` with a full synthetic binding environment (stage runner
   cannot run on macOS): rc 2 with `ADAPTER_FAILURE_NO_VERDICT`, exact
   cause `RuntimeError:STAGE_RESULT_MISSING:witness_replay`, remainder =
   the three node-2 generators at bound 6; both summaries byte-identical,
   and every mathematical field (generators, generator hashes, rank bound
   6, scope, `delta_node1_sha256`, settled-open route/verdict, endpoint)
   byte-identical to the R3 banked dry-run summary.  Evidence:
   `preflight/driver_failclosed_dryrun_SUMMARY.json`.
7. Build determinism: the rank-census rebuild reproduces
   `rank_size_6.support.rebuild.json` (`bb8f7ee0...8c51`: formal_slots
   97020, structural_zero 95920, support_matchable 1100, support_entries
   36).
8. Source archive replay: 23 file-only members (no directories, links,
   duplicates, traversal, or foreign prefixes; single `jc2/` prefix), fresh
   extraction verified all 22 `SOURCE_MANIFEST.sha256` entries `OK`, sidecar
   hash verified, `LAUNCH_MANIFEST.sha256` self-consistent (launcher
   self-hash and archive digest present).

## Pinned outputs

- Witness replay script SHA-256
  `27cb85082e8ea56a4a9bc8d0cb38b889edc4e981529d6697b0ff2800e0159d0d`
  (unchanged from R1/R2/R3).
- Node-2 reduce script SHA-256
  `d9e79b427dd22718683b2ac3f5f50dbd9839622ee07bf95cb61f02bdd380d8b8`
  (unchanged from R1/R2/R3).
- Source archive SHA-256
  `a59cdeb1ece45e98912a3617f3b8980c777f4a318a852e693cd98fe38c26aa85`
  (23 file-only members; a byte-different archive from R3 only because the
  packet documents, selfchecks, contract, and shell case paths carry the
  R4 identity — the 8 mathematical/recursion files are byte-identical to
  R3).

## Known local gaps (disclosed)

- No Singular stage was executed locally; the witness replay, all node
  stages, and the two Singular control scripts run for the first time on
  the AWS host.  The worker re-runs every selfcheck on-host before
  production.
- Every custody fixture is pure/parser-level.  The R4 concurrent-rename and
  in-place-mutation regressions use real OS threads and real
  `os.rename`/append against real frozen archives, but still exercise only
  `derive_late_decision` and the contract functions; the launcher,
  supervisor, stage runner, systemd scope (RuntimeMaxSec, KillMode, the
  supervisor-death watchdog), and live `/proc` gates were NOT executed.
  They are AWS rehearsal debt, discharged by the disposable-instance
  rehearsal in `AWS_PREREGISTRATION.md` (now including the R3 review's
  O2-B1 concurrent-rename regression as mandatory step 12) before any
  pilot.
- `FINALIZATION_LATCHES.txt`/`.sha256` is a post-freeze consistency
  sidecar, not an independent authentication (both files are
  same-uid-writable and outside the archive); the load-bearing latch state
  is the in-archive `FAULT_LATCHES_PRE_ARCHIVE.json`.
- The exact `RuntimeMaxUSec` renderings accepted for 21600 s are
  `6h`/`21600s`/`21600000000us`; an unexpected honest rendering on the live
  host downgrades (never promotes) until the rehearsal captures the live
  shape.
- The late authority now streams the whole terminal archive once through a
  single descriptor (outer hash) and compares it member-for-member against
  the extraction; for the expected archive sizes this is seconds and runs
  inside the whole-job budget, and its failure mode is a custody
  no-verdict.
- The Singular normalized-version and `elim.lib` pins are inherited from
  the reviewed proper-open R5 host; a different AMI fails closed before
  production.
