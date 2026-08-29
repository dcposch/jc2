# Closed-successor resume R2: local preflight report

Date: 2026-08-28 (macOS host, pure Python; no Singular/CAS executed).

## What ran locally

1. `python3 -m py_compile` and `python3 -O -m py_compile` over all eight
   packet Python files — pass; `bash -n` over the three shell scripts —
   pass.
2. `prepare_resume.py` against both real frozen archives — pass, including
   the new exact member-census hard gates
   (`R3_ARCHIVE_EXACT_CENSUS=454:391:63`,
   `PROPER_OPEN_ARCHIVE_EXACT_CENSUS=574:490:84`),
   `R3_SELECTED_EXTRACTED_FILE_COUNT=294`,
   `SETTLED_OPEN_EXTRACTED_FILE_COUNT=3`, open-route members excluded,
   archived timeout revalidated, settled-open verdict revalidated.
   Evidence: `preflight/R2_PREPARE.stdout.txt`,
   `preflight/PREPARED_INPUTS.json`.
3. `build_resume.py` (byte-identical to the reviewed R1 builder) — pass;
   the generated witness-replay and node-2 reduce scripts reproduce the R1
   pins exactly (`27cb8508...59d0d`, `d9e79b42...d8b8`), so the resumed
   mathematics is unchanged.  Evidence: `preflight/R2_BUILD.stdout.txt`,
   `preflight/generated/`.
4. Archived-standard-basis decomposition: the archived
   `NODE_001_STANDARD_BASIS.txt` (`bd95508c...640d`, 14,883 bytes) was
   independently decomposed as exactly three identical concatenated copies
   of a 4,961-byte unit, confirming the appended-copy law that repairs the
   R1 witness-replay comparison.
5. `generator_selfcheck.py` under `python3` AND `python3 -O` — pass: all
   validator-level mutations, the strict-classifier dead/survivor/restore
   positive controls (with real regenerated stage scripts and a full
   synthetic job binding), and the new hostile classifier fixtures
   (missing/copied identities, fabricated one-line script, wrong
   cap/binary/source/nonce, artifact-set extra, fabricated no-verdict
   reason, remainder/stage-record/binding tampers, witness-SB
   full-archive submission).  Evidence:
   `preflight/R2_GENERATOR_SELFCHECK.stdout.txt` (38 pass markers).
6. `containment_selfcheck.py` under `python3` AND `python3 -O` — pass:
   18-way `decide_terminal` mutation table (including the new
   systemd-runtime-fault, pgid-mode, runtime-limits, lease, and decision
   gates), foreign-candidate rejection, nonce/lease/decision-record
   controls, candidate swaps before/after archive freeze, the
   live-candidate-never-read control, copied decision record,
   no-replace terminal collision, directory-exact archive controls with
   the empty-directory negative fixture, and the three-line marker
   binding.  Evidence: `preflight/R2_CONTAINMENT_SELFCHECK.stdout.txt`
   (25 pass markers), `preflight/containment_selfcheck.json`.
7. `resume_recursor.py` fail-closed dry run under `python3` AND
   `python3 -O` with a full synthetic binding environment (stage runner
   cannot run on macOS): rc 2 with `ADAPTER_FAILURE_NO_VERDICT`, exact
   cause `RuntimeError:STAGE_RESULT_MISSING:witness_replay`, remainder =
   the three node-2 generators at bound 6; both summaries byte-identical.
   Evidence: `preflight/driver_failclosed_dryrun_SUMMARY.json`.
8. Build determinism: prepare+build were run twice into fresh directories;
   all five build products were byte-identical across runs.
9. Result-record schema agreement: the stage runner's emitted result keys,
   the driver's required key census, and the classifier's required key
   census were independently extracted and are identical.
10. Source archive replay: 23 file-only members (no directories, links,
    duplicates, traversal, or foreign prefixes), fresh extraction verified
    all 22 `SOURCE_MANIFEST.sha256` entries, sidecar hash verified.
    Evidence: `preflight/ARCHIVE_REPLAY.txt`.

## Pinned outputs

- Witness replay script SHA-256
  `27cb85082e8ea56a4a9bc8d0cb38b889edc4e981529d6697b0ff2800e0159d0d`
  (unchanged from R1).
- Node-2 reduce script SHA-256
  `d9e79b427dd22718683b2ac3f5f50dbd9839622ee07bf95cb61f02bdd380d8b8`
  (unchanged from R1).
- Source archive SHA-256
  `183ab5e0139cf6b68482f58ed72e63262f3423c6ffa3f3b5568a014c44a65987`
  (mode 0444, 23 file-only members).

## Known local gaps (disclosed)

- No Singular stage was executed locally; the witness replay, all node
  stages, and the two Singular control scripts run for the first time on
  the AWS host.  The worker re-runs every selfcheck on-host before
  production.
- Every custody fixture is pure/parser-level.  The launcher, supervisor,
  stage runner, systemd scope (including RuntimeMaxSec, KillMode, the
  supervisor-death watchdog), and live `/proc` gates were NOT executed;
  they are AWS rehearsal debt, to be discharged by the disposable-instance
  rehearsal in `AWS_PREREGISTRATION.md` before any pilot.
- The Singular normalized-version and `elim.lib` pins are inherited from
  the reviewed proper-open R5 host; a different AMI fails closed before
  production.  The exact Singular binary digest is measured on-host and
  bound into every stage and the decision record rather than pinned here.
