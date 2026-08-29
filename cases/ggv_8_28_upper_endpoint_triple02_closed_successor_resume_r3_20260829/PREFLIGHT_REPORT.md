# Closed-successor resume R3: local preflight report

Date: 2026-08-28 (macOS host, pure Python; no Singular/CAS executed).

## What ran locally

1. `python3 -m py_compile` and `python3 -O -m py_compile` over all eight
   packet Python files — pass; `bash -n` over the three shell scripts —
   pass.
2. `prepare_resume.py` (byte-identical to R2) against both real frozen
   archives — pass, including the exact member-census hard gates
   (`R3_ARCHIVE_EXACT_CENSUS=454:391:63`,
   `PROPER_OPEN_ARCHIVE_EXACT_CENSUS=574:490:84`),
   `R3_SELECTED_EXTRACTED_FILE_COUNT=294`,
   `SETTLED_OPEN_EXTRACTED_FILE_COUNT=3`, open-route members excluded,
   archived timeout revalidated, settled-open verdict revalidated.
   Evidence: `preflight/R3_PREPARE.stdout.txt`,
   `preflight/PREPARED_INPUTS.json`.
3. `build_resume.py` (byte-identical to the reviewed R1/R2 builder) —
   pass; the generated witness-replay and node-2 reduce scripts reproduce
   the R1/R2 pins exactly (`27cb8508...59d0d`, `d9e79b42...d8b8`; full
   values under "Pinned outputs" below), so the resumed mathematics is
   unchanged.  Evidence: `preflight/R3_BUILD.stdout.txt`,
   `preflight/generated/`.
4. Archived node-1 probe: exact censuses 454=391+63 and 574=490+84
   reconfirmed against the real archives; the archived
   `NODE_001_STANDARD_BASIS.txt` (`bd95508c...640d`, 14,883 bytes)
   decomposes as exactly three identical copies of a 4,961-byte unit
   (`84872c7a...f575`), and the unit contains exactly one newline, at its
   end — the source anchor of the R3 exact single-line append law.
   Evidence: `preflight/ARCHIVED_NODE1_PROBE.txt`.
5. `generator_selfcheck.py` under `python3` AND `python3 -O` (stdout
   byte-identical) — pass: all R2 fixtures plus the new O-N1/O-N2/O-N6
   hostile fixtures (runner-stdout tamper, nonempty runner stderr,
   doubled and multi-line node standard-basis stacks, identity-record key
   injection) and the new unit controls (single-line stack law,
   runner-log law, archived-unit single-line anchor).  45
   `expect_rejection` call sites / 49 rejection executions + 3 manual
   refusals per interpreter; 46 pass markers.  Evidence:
   `preflight/R3_GENERATOR_SELFCHECK.stdout.txt`.
6. `containment_selfcheck.py` under `python3` AND `python3 -O` (stdout
   byte-identical) — pass: every late-decision fixture now runs through a
   real freeze (complete manifest -> tar -> verified extraction), and the
   R2 hostile review's working O-B1 forgery — rewriting the archived
   verdicts and summaries inside the extraction and re-running
   decision-build over the rewritten tree — refuses on the archive-bytes
   binding, together with extraction edit/deletion/extra/symlink,
   archive/extraction mix-and-match, archive replacement/symlink/
   wrong-digest, fault-latch regression and worker-rc disagreement,
   five-property runtime-limit mutations, and the job-tag stamp schema.
   38 `expect_rejection` call sites / 41 rejection executions + 34 manual
   refusals per interpreter; 32 pass markers.  Evidence:
   `preflight/R3_CONTAINMENT_SELFCHECK.stdout.txt`,
   `preflight/containment_selfcheck.json` (note: its
   `decision_record_sha256` embeds timestamps and is not a usable charge;
   the stdout markers are).
7. `resume_recursor.py` fail-closed dry run under `python3` AND
   `python3 -O` with a full synthetic binding environment (stage runner
   cannot run on macOS): rc 2 with `ADAPTER_FAILURE_NO_VERDICT`, exact
   cause `RuntimeError:STAGE_RESULT_MISSING:witness_replay`, remainder =
   the three node-2 generators at bound 6; both summaries byte-identical.
   Evidence: `preflight/driver_failclosed_dryrun_SUMMARY.json`.
8. Build determinism: prepare+build were run twice into fresh directories;
   all five build products were byte-identical across runs, including the
   rank-census rebuild (`rank_size_6.support.rebuild.json`,
   `bb8f7ee0...8c51`: formal_slots 97020, structural_zero 95920,
   support_matchable 1100, support_entries 36).
9. Schema agreement: the stage runner's emitted result keys, the driver's
   required census, and the classifier's required census are the identical
   19-key set; the runner's identity record and the new
   `IDENTITY_RECORD_KEYS` census are the identical 17-key set; the R3
   runner-stdout law matches the runner's three print statements exactly
   (including the timed-out shape), with a float-repr round-trip control.
   Evidence: `preflight/SCHEMA_AGREEMENT_PROBE.txt`.
10. Source archive replay: 23 file-only members (no directories, links,
    duplicates, traversal, or foreign prefixes), fresh extraction verified
    all 22 `SOURCE_MANIFEST.sha256` entries, sidecar hash verified,
    archive file mode 0444.  Evidence: `preflight/ARCHIVE_REPLAY.txt`.

## Pinned outputs

- Witness replay script SHA-256
  `27cb85082e8ea56a4a9bc8d0cb38b889edc4e981529d6697b0ff2800e0159d0d`
  (unchanged from R1/R2).
- Node-2 reduce script SHA-256
  `d9e79b427dd22718683b2ac3f5f50dbd9839622ee07bf95cb61f02bdd380d8b8`
  (unchanged from R1/R2).
- Source archive SHA-256
  `2f129c2258a6d512bd8fe873db97c142c436bafdf0d7fee37997e4a3086e0bc1`
  (archive file mode 0444; 23 file-only members with inherited member
  modes; every extraction is hash-verified).

## Known local gaps (disclosed)

- No Singular stage was executed locally; the witness replay, all node
  stages, and the two Singular control scripts run for the first time on
  the AWS host.  The worker re-runs every selfcheck on-host before
  production.
- Every custody fixture is pure/parser-level.  The launcher, supervisor,
  stage runner, systemd scope (including RuntimeMaxSec, KillMode, the
  supervisor-death watchdog), and live `/proc` gates were NOT executed;
  they are AWS rehearsal debt, to be discharged by the disposable-instance
  rehearsal in `AWS_PREREGISTRATION.md` (now including the R2 review's
  O-B1 regression, exact systemd read-back, watchdog degradation, and
  runner-log discipline items) before any pilot.
- The exact `RuntimeMaxUSec` renderings accepted for 21600 s are
  `6h`/`21600s`/`21600000000us`; an unexpected honest rendering on the
  live host downgrades (never promotes) until the rehearsal captures the
  live shape.
- The Singular normalized-version and `elim.lib` pins are inherited from
  the reviewed proper-open R5 host; a different AMI fails closed before
  production.  The exact Singular binary digest is measured on-host and
  bound into every stage and the decision record rather than pinned here.
