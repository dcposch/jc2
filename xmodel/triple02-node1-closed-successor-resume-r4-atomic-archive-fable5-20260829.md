# TRIPLE02 node-1 closed-successor resume R4 — atomic-archive-authentication producer report

Author: Fable 5 (source producer, not reviewer; same model as the R3
producer).  Date: 2026-08-28 (packet dated 20260829).  Working directory:
`/Users/dc/code/math/jc2`.

Deliverable: the fresh directory
`cases/ggv_8_28_upper_endpoint_triple02_closed_successor_resume_r4_20260829/`
and this report.  R3 was treated as the immutable predecessor: the R3
source archive (`2f129c22...0bc1`), `containment_contract.py`
(`a44d7022...3a3ab1`), `LAUNCH_MANIFEST.sha256` (`10fbc308...9dac5`), the
R3 producer report (`4ffa1047...f97c0c`) and the R3 Opus hostile review
(`1110c09d...53397a`) were all re-hashed this session and are unmodified.
Nothing was launched, no CAS was run, no canonical file was edited, nothing
was committed, `jc2-lean` was not accessed, no repository-wide command was
run, and no web/AWS operation was performed.  Bounded scratch replays ran
under `/tmp/triple02-r4-preflight`.

## Verdict

**`SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW`**

The only next action this report licenses is a hostile source review of this
R4 packet by a different model.  R4 does **not** authorize an AWS launch, a
mathematical pilot, a rehearsal, or promotion; after a passing review, the
disposable-instance rehearsal in `AWS_PREREGISTRATION.md` (now including the
R3 review's O2-B1 concurrent-rename regression as mandatory step 12) and a
separate coordinator `GO` remain mandatory.

## 1. Charge

This packet repairs the one blocking-before-pilot finding and the adjacent
nonblocking findings of the Opus 5 hostile review of R3
(`xmodel/triple02-node1-closed-successor-resume-r3-hostile-review-opus5-20260829.md`,
full `1110c09d8528b536c231eb48e7fdae7c69869d042d0c292d6221ff9c0153397a`,
body `206ebc55548c7218a4966990050510da38279461a9d9279cc3cc5533f959685c`,
verdict `PASS_SOURCE_FOR_DISPOSABLE_REHEARSAL`), keeping the R1/R2/R3
mathematical recursion byte-for-byte fixed:

- **`O2-B1` (blocking before any pilot)**: the R3 late authority opened the
  charged archive **twice by path** — `sha256_path(terminal_archive)` for
  the digest, then `tarfile.open(terminal_archive)` for the census, with a
  full `walk_fresh_root` between them.  The review demonstrated **6/6**
  genuine-thread promotions of a forged archive `rename()`d over the path
  inside that window.
- **`O2-N2`**: `if archived_fault not in (0, 1)` accepted JSON `true`/`false`
  (bool is an int subclass).
- **`O2-N4`**: the terminal CLI could exit rc 1 markerless on a malformed
  late `--archive-sha256` (the guarded `derive` failed, then an unguarded
  `require_digest` raised).
- **`O2-N1`**: the `swap_zero` decide_terminal gate was never exercised by a
  packet fixture (18 of 19 gates covered).

The R3 review's non-blocking observations `O2-N3` (FINALIZATION_LATCHES is a
consistency sidecar, not an authentication), `O2-N5` (stamp regex is
shape-only), `O2-N6`/`O2-N7` (fragile-input / pre-freeze scope notes) are
adopted as honest documentation; none required a code change.

## 2. The `O2-B1` repair: the charged archive is opened exactly once

`containment_contract.py` now authenticates the terminal archive through a
**single open descriptor**:

1. `open_frozen_archive(terminal_archive)` opens the path **once** with
   `O_RDONLY | O_NOFOLLOW | O_NONBLOCK | O_CLOEXEC`.  `O_NOFOLLOW` refuses a
   symlink at the `open()` itself (no second content read); `O_NONBLOCK`
   means a FIFO planted at the path cannot block the decision; an `fstat`
   **on the returned descriptor** requires `S_ISREG`.  It returns the open
   file object.
2. `authenticate_frozen_archive` streams the outer SHA-256 from that
   descriptor, compares it to the charged digest, `handle.seek(0)`, and
   hands the **same open object** to `tarfile.open(fileobj=handle,
   mode="r:gz")`.  The extraction walk, the member-safety / embedded-manifest
   / directory censuses, the member-for-member byte binding of the fresh
   extraction, and every retained-member read all run while that one
   descriptor is held.  **No archive path is reopened anywhere on the
   authenticated decision path** — proved structurally by the selfcheck,
   which fails closed if `sha256_path(terminal_archive)` or
   `tarfile.open(terminal_archive)` reappears or if `os.open(terminal_archive)`
   is not called exactly once.  A concurrent same-uid `rename()`/replacement
   of the path therefore cannot redirect any decision read: the held
   descriptor still points at the original inode.
3. `require_stable_archive_stat` compares the descriptor's `fstat`
   `(st_dev, st_ino, st_size, st_mtime_ns, st_ctime_ns)` **before** the
   first hashed byte and **after** the last authenticated read; an in-place
   write/truncate of the inode moves `st_ctime`/`st_size` (ctime cannot be
   back-dated without root), so it fails closed with
   `DECISION_ARCHIVE_UNSTABLE_DURING_READ`.
4. `derive_late_decision` returns the digest actually computed from the
   descriptor (`view.archive_sha256`); `main()` binds the marker's
   `TERMINAL_ARCHIVE_SHA256` to that value, never to the CLI string.  Because
   `decide_terminal` can emit a mathematical first line only when
   `decision_ok` is true, every mathematical marker is descriptor-bound.

**Regression, executed this session with genuine concurrency and no patched
functions.**  The selfcheck builds an honest bounded-no-verdict job and a
**self-consistent forged job** (the honest tree with verdicts/summaries
rewritten to the dead string and the decision record rebanked, so its lease
and identities are byte-identical to the honest job — exactly the forgery
the R3 review promoted).  A real `threading.Thread` `os.replace`s the forged
archive over the charged path while `derive_late_decision` runs on the main
thread, across **9** file-count/read-window configurations (1/3/6 padded
members × 4 KiB/64 KiB/256 KiB pads × delays 0–2.5 ms) plus one deterministic
rename-before-open case.  **All 10 fail closed** — the descriptor stays
honest so the forged extraction fails the member byte-binding
(`DECISION_FRESH_ROOT_BYTES_DRIFT`), or the attacker wins the open and the
forged bytes fail the outer hash (`DECISION_ARCHIVE_HASH_DISAGREEMENT`); **0
promotions**.  A no-attacker positive control promotes the honest bounded
no-verdict and its marker digest equals the descriptor digest.  The genuine
in-place append race plus the direct `fstat`-gate test both fail closed.

## 3. Adjacent findings closed

- **O2-N2 — fault-latch typing.**  `derive_late_decision` now checks
  `isinstance(v, int) and not isinstance(v, bool)` for `worker_rc` and each
  of the six sticky faults, so archived JSON `true`/`false` (and any
  non-int) is refused with `DECISION_FAULT_LATCH_SCHEMA`.  Three refusing
  fixtures added (`worker_rc: true`, `systemd_runtime_fault: true`,
  `swap_violation: false`).
- **O2-N4 — always publish a marker.**  `main()` computes the marker's
  archive field from `verified_archive_sha` when the decision authenticated,
  else from `args.archive_sha256` **only if it matches** `DIGEST_RE`, else
  `NONE`; the unguarded `require_digest(archive_sha, ...)` is gone.  A
  malformed late `--archive-sha256` now yields the custody no-verdict marker
  (`TERMINAL_ARCHIVE_SHA256=NONE`, rc 3), verified end-to-end through the CLI.
- **O2-N1 — swap_zero gate.**  The decide_terminal mutation table gains a
  `swap_zero_violation` row, so all **19** gate parameters are now exercised
  (the clean configuration still promotes).
- **O2-N3 — honest FINALIZATION_LATCHES.**  The README, `AWS_PREREGISTRATION.md`
  and `PREFLIGHT_REPORT.md` now state that `FINALIZATION_LATCHES.txt`/`.sha256`
  is a post-freeze same-uid-writable **consistency sidecar, not an
  authentication**; the load-bearing latch state is the in-archive
  `FAULT_LATCHES_PRE_ARCHIVE.json`.

## 4. What is mathematically unchanged (verified, not asserted)

The eight mathematical/recursion files are **byte-identical** to R3 (same
SHA-256 as the R3 §5 table and the review §1 table): `prepare_resume.py`
(`1eb8ed78...`), `build_resume.py` (`3763ac7a...`), `resume_recursor.py`
(`648d28aa...`), `classify_resume.py` (`38677c06...`),
`run_singular_stage.py` (`766bebf0...`), `adapter_selfcheck.sing`
(`e616b595...`), `diagnostic_hostile.sing` (`01be8175...`),
`EXPECTED_GENERATED_SCRIPTS.sha256` (`9912dd22...`).

**AST comparison, every top-level definition/method/constant, R3 vs R4:**

| file | shared | identical | changed | added | removed |
|---|---|---|---|---|---|
| `resume_recursor.py` | 43 | **43** | none | none | none |
| `classify_resume.py` | 45 | **45** | none | none | none |
| `build_resume.py` | 23 | **23** | none | none | none |
| `prepare_resume.py` | 21 | **21** | none | none | none |
| `generator_selfcheck.py` | 26 | 25 | `FIX_TAG` (fixture tag prefix r3→r4) | none | none |
| `containment_contract.py` | 68 | 59 | `LEASE_SCHEMA`, `DECISION_SCHEMA`, `FAULT_LATCH_SCHEMA`, `JOB_TAG_PREFIX`, `FrozenArchiveView(.__init__)`, `authenticate_frozen_archive`, `derive_late_decision`, `main` | `open_frozen_archive`, `require_stable_archive_stat` | none |

`MATH_TERMINALS` (the four-string terminal allowlist), the classifier's
`ALLOWED`, the worker's `case`, `GENERATOR_SHA256`, `DELTA_NODE1_SHA256`,
`WITNESS_REPLAY_MARKERS`, `ARCHIVED_NODE1_SB_APPEND_COUNT`, the recursion
contract, the three no-reentry firewalls, and the three-line marker format
are all in the AST-identical set.  **No definition was removed anywhere.**

**Re-ran preparation and the build from the real frozen archives.**  The
five build products reproduce the R1/R2/R3 pins exactly:
`TRIPLE02_NODE1_WITNESS_REPLAY.sing` `27cb8508...59d0d`,
`NODE_002_REDUCE_EXPECTED.sing` `d9e79b42...d8b8`, `RESUME_NODE_INPUT.json`
`6f61d686...83ab5`, `BUILD_MANIFEST.json` `d8582938...2139c`,
`rank_size_6.support.rebuild.json` `bb8f7ee0...8c51` (formal_slots 97020,
structural_zero 95920, support_matchable 1100, support_entries 36).
`generator_selfcheck.py` stdout (48 lines, both interpreters) is
**byte-identical to the R3 banked `R3_GENERATOR_SELFCHECK.stdout.txt`**, and
the driver fail-closed dry-run reproduces every mathematical field of the R3
banked summary (rank bound 6, scope, `delta_node1_sha256 = 84b4c2c4...`, the
three open-remainder generators and hashes, settled-open route/verdict,
endpoint).  `PREREGISTRATION.md` differs from R3 **only** in its
header/status block (verified by `diff`); the objective, starting ideal,
recursion contract, terminal classifications, append law and every literal
binding are word-for-word R3.

## 5. Packet contents and hashes

Case dir `cases/ggv_8_28_upper_endpoint_triple02_closed_successor_resume_r4_20260829/`:

| file | SHA-256 | vs R3 |
|---|---|---|
| `prepare_resume.py` | `1eb8ed781843fd0efd633722ddd74853266d0e361b6e78a0d7e5ab9e1b302528` | identical |
| `build_resume.py` | `3763ac7a5ce2915ede7c21c9d9b8dcb3fc1ab12075c998daa646a375b640f780` | identical |
| `resume_recursor.py` | `648d28aa11f4eb2666b4d01654ee73d4069d87c89950598a014ef5ee9c0550f9` | identical |
| `classify_resume.py` | `38677c06b1ac22862e59f0026de815bd86c55177a162c7dcde09125820f829bb` | identical |
| `generator_selfcheck.py` | `96cb4a103741a94cef345425604c41fe1b92ea9c74c471ecd787ecd160a4f44a` | FIX_TAG only |
| `run_singular_stage.py` | `766bebf02496c2bcdd34c575219b819d4d332f404f286cc49dedab793ffe9564` | identical |
| `containment_contract.py` | `506aae791eacf781461945c72693d67b5e4b61ce85e8d38fead87dbdd4a797e6` | O2-B1 repair |
| `containment_selfcheck.py` | `639e9fcc5b7b4d8c145a3e6159629e3397ddefde3241b6168958da6f2ba8f52d` | R4 fixtures |
| `adapter_selfcheck.sing` | `e616b59542a977dd9daa6865dbf18b60feaae06f784d98f72cf8cced27ee4490` | identical |
| `diagnostic_hostile.sing` | `01be817524da040ad97eeb52adc461d6556e2d8cd179c9447c4c5101a2f15e02` | identical |
| `aws_job_worker.sh` | `158072c019426e9b49322a349cedc215c31b5095bb99b7069b469c50099b1f8f` | case_rel r3→r4 |
| `aws_supervisor.sh` | `110ea0a029403fa88697ae37f57edd2f18680a118101e32065f98b7b317b0a06` | case_rel + latch schema |
| `aws_launch_preflight.sh` | `80dda64ce78378d1423f29d84bd63c732d515c4c0d630825a6e6b99ca1f0362f` | archive name/sha/case/prefix |
| `runtime_expectations.env` | `1ce21051c363e29b6c4897fa569eaef8273546b6b74ab5cede0a51d3778ba67f` | prereg pin |
| `EXPECTED_GENERATED_SCRIPTS.sha256` | `9912dd2279223347d461b5640583b84283216d4873b56e3be34770314f2b5696` | identical |
| `SOURCE_MANIFEST.sha256` (22 entries) | `31daea20299a8e25d22b5734e496a96519d47454f16e1d583a8df8c758f1374e` | — |
| `AWS_PREREGISTRATION.md` | `c69288d1c185463004387b4305995339d4efc01f54f6f07050f7ec3b9aec992c` | O2-B1/O2-N3 prose |
| `PREREGISTRATION.md` | `f4eb6ab94bc0a4ca0458f4eb2fe62b3e7b8548a496f90019b16988e6ca52b648` | header only |
| `PREREGISTRATION.sha256` | `14f2ee061a0d6e318ddbd8e4451d6af0184c4a8df6560810931317cc05e1f151` | — |
| `README.md` | `26d23c6b12df3c895339506520f9c3351ddd030e7b811c940245b0a2536cfe7f` | R4 prose |
| `PREFLIGHT_REPORT.md` (excluded from archive) | `f08c3be885e5079e02373706c97aada9896f9177ebd854c028f67c8d3d3826db` | R4 |
| `SOURCE_ARCHIVE.sha256` | `0e447ac37e9645433369cb736dcfb7fff9b9690fabd39f9fa633faf66df1c074` | — |
| **`LAUNCH_MANIFEST.sha256`** (6 lines, report-free) | `61277f052a9542c43bf14d0af9b56141c85c5e972939ceed0c237b48c884b8b6` | O-N5 retained |
| source archive `custody/ggv_triple02_closed_successor_resume_r4_SOURCE.tar.gz` (23 file-only members) | `a59cdeb1ece45e98912a3617f3b8980c777f4a318a852e693cd98fe38c26aa85` | — |

`REPORT_BINDING.sha256` is written immediately after this report (it lists
this report's full-file hash, so it cannot be tabled here); the reviewer
charges this report's hash independently.  `LEASE_SCHEMA`/`DECISION_SCHEMA`/
`FAULT_LATCH_SCHEMA`/`JOB_TAG_PREFIX` are bumped to `..._r4_...`, so no R3-era
lease, decision record, tag, or latch record can be replayed into an R4 job.
The launcher pins `expected_archive_sha = a59cdeb1...aa85`.

**Archive arithmetic (recomputed this session).**  `SOURCE_MANIFEST.sha256`
has exactly **22** entries and `sha256sum -c` returns **22 OK**; the 22 are
the **18** in-case files (all packet files except `aws_launch_preflight.sh`,
`SOURCE_MANIFEST.sha256` itself, `SOURCE_ARCHIVE.sha256`,
`PREFLIGHT_REPORT.md`, `LAUNCH_MANIFEST.sha256`, `REPORT_BINDING.sha256`, and
the archive) plus the **4** frozen dependencies.  An independent `tarfile`
census of the source archive: **23 members, 23 regular files, 0 directories,
0 symlinks/hardlinks, 0 duplicates**, single top prefix `jc2`, member set
exactly `entries ∪ {SOURCE_MANIFEST.sha256}`.  `PREREGISTRATION.sha256`
(2/2), `SOURCE_ARCHIVE.sha256` (1/1) and `LAUNCH_MANIFEST.sha256` (6/6)
verify; the launcher's own hash and the archive digest are both present in
the launch manifest.  The four frozen-dependency hashes
(`d679a4d7...`, `0e0efd5a...`, `e5bdd2b2...`, `4b8ffc1c...`) re-verify
byte-exact against the repository.

## 6. Local verification (all pass; exact commands and counts)

1. `python3 -m py_compile` and `python3 -O -m py_compile` over all eight
   packet Python files; `bash -n` over the three shell scripts — all pass.
2. `prepare_resume.py` against the real frozen archives (census gates
   454:391:63 and 574:490:84, 294 + 3 extracted files, open-route exclusion,
   archived-timeout and settled-open revalidation) — pass;
   `build_resume.py` reproducing all five R1/R2/R3 pins.
3. `generator_selfcheck.py` under `python3` and `python3 -O`: stdout
   byte-identical across interpreters (48 lines) **and byte-identical to the
   R3 banked stdout**; rc 0.
4. `containment_selfcheck.py` under `python3` and `python3 -O`: stdout
   byte-identical across interpreters, **39 marker lines** (32 R3 + 7 new
   R4), empty stderr, rc 0.  **42 `expect_rejection` call sites.**  New R4
   controls: `SINGLE_OPEN_ARCHIVE_SOURCE_PASS`,
   `CONCURRENT_RENAME_FORGERY_FAIL_CLOSED_PASS` (9 race configs + 1
   deterministic pre-open + 1 honest positive control, 0 promotions),
   `IN_PLACE_MUTATION_FAIL_CLOSED_PASS`, `ARCHIVE_STABILITY_FSTAT_GATE_PASS`,
   `FAULT_LATCH_BOOLEAN_TYPING_REJECTED`, `SWAP_ZERO_GATE_EXERCISED` (19-gate
   table), `MALFORMED_ARCHIVE_DIGEST_MARKER_PUBLISHED`.
5. `resume_recursor.py` fail-closed dry runs under `python3` and `python3 -O`
   with a full synthetic binding environment: both rc 2,
   `ADAPTER_FAILURE_NO_VERDICT`, exact cause
   `RuntimeError:STAGE_RESULT_MISSING:witness_replay`, remainder = 3
   generators at bound 6, `SUMMARY.json` byte-identical across interpreters
   and math-field-identical to the R3 banked dry-run.
6. Source archive: build, 23-file-only-member census, fresh extraction with
   22/22 manifest `OK`, sidecar `OK`, launch-manifest 6/6 `OK`.
7. AST comparison R3→R4 of all recursion and contract sources (§4 table).
8. R3 predecessor immutability: the R3 source archive, `containment_contract.py`,
   `LAUNCH_MANIFEST.sha256`, the R3 producer report, and the R3 hostile
   review all re-hash to their charged values.

## 7. R3 → R4 diff inventory

Byte-identical files (8): the eight mathematical/recursion files listed in
§4.

Changed files and their exact deltas:

| file | change | finding |
|---|---|---|
| `containment_contract.py` | single-open `open_frozen_archive` + `require_stable_archive_stat`; `authenticate_frozen_archive` streams+seeks one descriptor into `tarfile(fileobj=...)`; `FrozenArchiveView.archive_sha256`; `derive_late_decision` returns it + integer-typed fault latches; `main` binds marker to descriptor digest and never raises on a malformed late digest; r4 schema/prefix constants | O2-B1, O2-N2, O2-N4 |
| `containment_selfcheck.py` | single-open source assertion; genuine concurrent-rename regression (9 configs + pre-open + honest control); in-place mutation race + fstat-gate test; swap_zero gate row; fault-latch boolean fixtures; markerless-CLI test; r4 tags | O2-B1, O2-N1, O2-N2, O2-N4 |
| `generator_selfcheck.py` | `FIX_TAG` r3→r4 only | rename |
| `aws_supervisor.sh` | `case_rel` r3→r4; fault-latch schema string r3→r4 | rename |
| `aws_job_worker.sh` | `case_rel` r3→r4 | rename |
| `aws_launch_preflight.sh` | archive name/sha, `case_rel`, `job_tag_prefix`, allowed prefix r3→r4 | rename, archive |
| `runtime_expectations.env` | `EXPECTED_PREREG_SHA256` re-pinned to the R4 `AWS_PREREGISTRATION.md` | doc chain |
| `README.md`, `PREREGISTRATION.md`, `AWS_PREREGISTRATION.md` | R4 status/prose; O2-B1 single-open description; honest FINALIZATION_LATCHES wording; rehearsal step 12 | docs |
| manifests/sidecars/archive | regenerated from the R4 source | derived |

No definition was removed anywhere.

## 8. Repair crosswalk (review finding → R4 repair → evidence)

| finding | repair | evidence |
|---|---|---|
| **O2-B1** (blocking): archive opened twice by path; 6/6 concurrent-rename promotions | single open descriptor (`O_NOFOLLOW`/`O_NONBLOCK`, regular-file `fstat`), outer hash + `seek(0)` + `tarfile(fileobj=...)`, no path reopen, pre/post `fstat` stability gate, descriptor-bound marker | `SINGLE_OPEN_ARCHIVE_SOURCE_PASS`, `CONCURRENT_RENAME_FORGERY_FAIL_CLOSED_PASS` (10/10 fail closed, 0 promotions), `IN_PLACE_MUTATION_FAIL_CLOSED_PASS`, `ARCHIVE_STABILITY_FSTAT_GATE_PASS`, honest positive control promotes with descriptor-bound digest |
| O2-N2: JSON bool passed as int | `isinstance(v, int) and not isinstance(v, bool)` for worker_rc + six faults | `FAULT_LATCH_BOOLEAN_TYPING_REJECTED` (3 fixtures) |
| O2-N4: markerless exit on malformed late digest | marker archive field from descriptor digest or `DIGEST_RE`-validated CLI else `NONE`; no unguarded re-check | `MALFORMED_ARCHIVE_DIGEST_MARKER_PUBLISHED` (rc 3, `...=NONE`) |
| O2-N1: swap_zero gate untested | mutation-table `swap_zero_violation` row | `SWAP_ZERO_GATE_EXERCISED` (19-gate table) |
| O2-N3: FINALIZATION_LATCHES overclaimed | honest "consistency sidecar, not authentication" wording | README / AWS_PREREGISTRATION / PREFLIGHT_REPORT prose |
| O2-N5/N6/N7 (no code impact) | documented as-is | packet documents |

## 9. Scope firewall and maximum possible claim

Unchanged from Sol 5.6 and the R2/R3 reviews, and re-verified: `MATH_TERMINALS`,
the classifier's `ALLOWED`, and the worker's `case` are the same **four**
strings, with no radical, geometric, whole-component, whole-stratum or JC2
widening anywhere in the sources or documents.  `EXACT_ENDPOINT_DEAD_…_FINITE_COVER`
would mean, at most, exact endpoint death on the finite chart cover of only
`V(I_node1 + (Delta_node1))` in `Spec Q[q0,q2,c4,c6]`, `dp` order;
`RING_LEVEL_ENDPOINT_SURVIVOR_…_PENDING_NILPOTENCE_RADICAL` a nonzero
endpoint coefficient on one closed-successor chart pending nilpotence,
radical and geometric analysis; the two bounded strings carry no mathematical
conclusion.  R4 licenses **only** another hostile review; it does not
authorize AWS, a rehearsal, a mathematical pilot, or promotion, and it is not
a mathematical result.

## 10. Residual-risk ledger (for the reviewer)

1. **No Singular ran locally** (unchanged); the witness replay and node
   stages first run on AWS.  Every custody fixture is pure/parser-level;
   the R4 concurrent-rename/in-place regressions use real threads and real
   `os.rename`/append but still exercise only the contract functions.  The
   launcher, supervisor, stage runner, systemd scope, watchdog, and live
   `/proc` gates have never executed — rehearsal steps 1–12 remain
   mandatory (step 12 replays the O2-B1 race on a live extraction).
2. **In-place-mutation detection is best-effort by timing, backstopped by
   the fstat gate.**  On the local host the gate fired
   (`DECISION_ARCHIVE_UNSTABLE_DURING_READ`).  The gate assumes ctime cannot
   be back-dated without root and that the extraction lives on a filesystem
   with honest `st_ctime_ns`/`st_mtime_ns`; a truly atomic single-inode
   in-place rewrite that preserves size and all timestamps is not
   detectable by stat alone — but such a rewrite is not the R3 exploit
   (which was a path `rename()`, fully closed here) and requires a same-uid
   writer already inside `$JOB_ROOT` past the containment censuses.
3. **Decision-time cost**: the single descriptor is streamed once for the
   outer hash and its members are read once for the byte-binding; for the
   expected archive sizes this is seconds inside the whole-job budget;
   failure mode is a custody no-verdict.
4. **FINALIZATION_LATCHES** is a consistency sidecar only (O2-N3); the
   load-bearing latch state is the in-archive `FAULT_LATCHES_PRE_ARCHIVE.json`.
5. **RuntimeMaxUSec rendering set** (`6h`/`21600s`/`21600000000us`),
   **stamp regex shape-only** (O2-N5), and the **fragile live lease/mode
   inputs** (O2-N6) are unchanged downgrade-only surfaces.
6. **Pre-freeze scope** (O2-N7): archive-bytes authentication defends the
   post-freeze half; a job tree forged before the freeze is covered instead
   by the classifier regeneration/byte-comparison and the containment
   censuses, unchanged from R3.
7. **Performance unknowns** (node-2 saturation cost, reverse bound 64) are
   unchanged preregistered bounded no-verdicts.

## 11. Session evidence

Local preflight evidence is under the packet's `preflight/` directory
(prepare/build stdouts, both selfcheck stdouts, the containment fixture JSON
with the recorded race outcomes, the fail-closed dry-run summary, and the
five build products).  The R4 source archive replayed cleanly (sidecar hash,
23-file-only-member census, 22/22 embedded-manifest verification, 6/6
launch-manifest self-check).  The R1/R2/R3 packet directories, the R1/R2/R3
reports, the hostile reviews, and every canonical file are unmodified; this
packet directory and this report (plus the post-report `REPORT_BINDING.sha256`)
are the only additions, plus the bounded `/tmp/triple02-r4-preflight` scratch.

Report-body SHA-256 (all preceding bytes, including the newline immediately before this line): e464c71531369cd0ad3719e7111addf70584a23a2ee53bc4e5af2df1f78a074a
