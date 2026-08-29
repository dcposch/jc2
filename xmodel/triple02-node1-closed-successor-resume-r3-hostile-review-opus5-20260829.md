# Hostile source review: TRIPLE02 node-1 closed-successor resume R3

Reviewer: Opus 5 (`claude-opus-5`), independent of the R3 producer (Fable 5).
This is the same reviewer that produced the R2 hostile review; it is a
different-model review of the producer, as charged.  Packet label: 20260829.
Review environment date: 2026-08-28, America/Los_Angeles.  Working directory:
`/Users/dc/code/math/jc2`.

## Verdict

**`PASS_SOURCE_FOR_DISPOSABLE_REHEARSAL`**

R3 does what it says on the blocking finding.  I reproduced every charged
hash, rebuilt every seal from outside the packet, replayed both selfcheck
suites and the preparer/builder/driver under `python3` and `python3 -O`, and
ran **77 hostile fixtures of my own construction plus 6 positive controls**
against the real production functions.  The R2 review's working O-B1 forgery
and every one of the five forgery classes named in my charge —
**edit, delete, extra, symlink, mix-and-match** — now fail closed, and the
published marker's archive digest is provably the digest that
`authenticate_frozen_archive` verified.  The mathematics is byte-for-byte the
recursion R1 and R2 were reviewed on, proved by AST comparison and by
re-deriving all five build products.

This review licenses **only** the explicitly preregistered disposable
live-Linux/Singular rehearsal in `AWS_PREREGISTRATION.md` §"Mandatory
disposable-Linux rehearsal" (steps 1–11), and only after a separate
coordinator `GO`.  It licenses **no mathematical pilot, no AWS production
run, and no promotion**, and it is not a mathematical result.

I found one **blocking-before-pilot** defect that the R3 report does not
disclose and no packet fixture reaches, `O2-B1` (§4): the charged archive is
opened **twice by path** — once by `sha256_path` for the digest check and
again by `tarfile.open` for the census — with a full recursive
`walk_fresh_root` of the extraction in between.  A same-uid `rename()` inside
that window substitutes a forged archive for every decision input while the
marker still carries the honest digest.  I demonstrate this **6/6 times with a
genuine concurrent thread and no patched functions** (§4).  This is a
strictly narrower re-instance of the same failure mode as Sol 5.6's C1 and my
own O-B1 — the public marker disagreeing with the archive it names — and it
must be repaired and re-reviewed before any mathematical run.  It does not
make a throwaway rehearsal unsafe, which is why the license above stands.
The repair is one line and is stated in §4.

No AWS or web operation was performed.  No Singular, msolve, Sage, PARI or
other CAS was run.  No commit, push, or canonical-ledger edit was made.  No
producer or canonical file was edited; the R1, R2 and R3 packet directories
and all reports are unmodified (verified by re-hashing, §1).  `jc2-lean` was
not accessed, listed, searched, built, or status-checked, and no
repository-wide search was run.  The only file I created is this report;
bounded scratch lived under `/tmp/t02r3-opus5`.

## 1. Charged hashes — all reproduced this session

Recomputed with `shasum -a 256` from outside the packet.  Every value in the
R3 report's §5 table matched exactly; nothing below is quoted from the
producer.

| object | SHA-256 | R3 claim |
|---|---|---|
| `prepare_resume.py` | `1eb8ed781843fd0efd633722ddd74853266d0e361b6e78a0d7e5ab9e1b302528` | match |
| `build_resume.py` | `3763ac7a5ce2915ede7c21c9d9b8dcb3fc1ab12075c998daa646a375b640f780` | match |
| `resume_recursor.py` | `648d28aa11f4eb2666b4d01654ee73d4069d87c89950598a014ef5ee9c0550f9` | match |
| `classify_resume.py` | `38677c06b1ac22862e59f0026de815bd86c55177a162c7dcde09125820f829bb` | match |
| `generator_selfcheck.py` | `a6f32db0e81d9d8089670c69ed9e42f355c1f5d5564a6875ba084617d8ba4d39` | match |
| `run_singular_stage.py` | `766bebf02496c2bcdd34c575219b819d4d332f404f286cc49dedab793ffe9564` | match |
| `containment_contract.py` | `a44d70228a09e522ed8fc00fde010f7696d390e023337aa7e7eb06fd831a3ab1` | match |
| `containment_selfcheck.py` | `77db3d3966d4ddc70ec6e9b1f8f3dc8e257551266553e640d340f9e68bcf116b` | match |
| `adapter_selfcheck.sing` | `e616b59542a977dd9daa6865dbf18b60feaae06f784d98f72cf8cced27ee4490` | match |
| `diagnostic_hostile.sing` | `01be817524da040ad97eeb52adc461d6556e2d8cd179c9447c4c5101a2f15e02` | match |
| `aws_job_worker.sh` | `58f000c9109fd72448a198a17b4f88ab5ac21f9243aed0651205bca0f612ea1d` | match |
| `aws_supervisor.sh` | `20c806977cf1a55b339b26520ae40e1752ffa427356e19fe15cf8856f8704209` | match |
| `aws_launch_preflight.sh` | `4d252ddfc232592ca07f5f582427c75d636bfc5e9d2914ed4fcd42dd533bd58e` | match |
| `runtime_expectations.env` | `d3dfa8b99a67e82ae35b8574f0a2bcb95567540c9c03df5d80ab52d4a4932ec3` | match |
| `EXPECTED_GENERATED_SCRIPTS.sha256` | `9912dd2279223347d461b5640583b84283216d4873b56e3be34770314f2b5696` | match |
| `SOURCE_MANIFEST.sha256` (22 entries) | `85e75a1352362b86d579d3e454d4909fcf7dbb71cc75c2b20c64259095bcfdac` | match |
| `AWS_PREREGISTRATION.md` | `8147c0b7e1677038d2610f9e69e3df8ec75e87b9545d8b79de49e465d117354c` | match |
| `PREREGISTRATION.md` | `161c3011e1f3b316f8a7315e3aac732ce80207c027fbc22a63727efde3456b61` | match |
| `PREREGISTRATION.sha256` | `849828b4e064920bdd80235707fd1b4a7ca4d11c74291980e6b42fd181ad1844` | match |
| `README.md` | `a680b2bcd5fd1be0dac33b79819d60fafaae9b313f1073144752d38d615bf837` | match |
| `PREFLIGHT_REPORT.md` | `7b02674c9ec97f58f28e1178b6e1766e0d6bed5c348944d1c6e576b9b3716be3` | match |
| `SOURCE_ARCHIVE.sha256` | `21b690037aa9f725f44a15868792259d0ee6b08f84cc15d31b9ba99919564049` | match |
| **`LAUNCH_MANIFEST.sha256`** (6 lines, report-free) | `10fbc308aefbb2dfbe6c45d987feb27a7e930841aa0c76eb853c8e8a9a87dac5` | match — **O-N5 closed, and I charge this value** |
| source archive `custody/ggv_triple02_closed_successor_resume_r3_SOURCE.tar.gz` | `2f129c2258a6d512bd8fe873db97c142c436bafdf0d7fee37997e4a3086e0bc1` | match |
| **`REPORT_BINDING.sha256`** (untabled by construction — charge it) | `197ba45f3b6fab2bab0d9966c31e0c880f6662bb8a916eb4c440042983fea39d` | not claimed |
| R3 producer report (full file) | `4ffa10477238c0726ba8b470a2ce6110671f823f6cebc1501a71bd48f7f97c0c` | equals the single line inside `REPORT_BINDING.sha256` |
| R3 producer report body (lines 1–449) | `ea71583070a6c51c11c6201b8a3f8f74d541652116a880dd8f6ed412c0759f76` | match |

Immutability of the reviewed predecessors, re-hashed this session: R2 report
`c6322ccf5e25c27575c8b0f3e1b8f7b37a5a8add70d2687e9dcf4feb41dc8757`
(body `fbefb5011f91274f00ebe75b472b12cf1422da7f487d66b858f37aac678dd6c0`);
R2 hostile review
`e524ba78a0ebe3468259f85fec148494b5ec6c4f160941333f67013b1dfb518e`
(body `c4f90652eb665dad8b396150704340a12a9bef746e67d17cc5fe83ecab5b451d`);
R1 report `93b894306401e1e2e1965788708b9fe071f93336d4db01446ad7f58c3b0dcca9`;
R1 review `ad25f49675f26128d220a5954c8e7f72580060b929e42868eeefaefd75cfafb2`;
**R2 `LAUNCH_MANIFEST.sha256` still
`ba697115001232b95d58fb54e3102e1a7df28fad5e37849a68757af5b021dc34`**, the
value I charged in the R2 review — the R2 packet was not touched.  All four
frozen dependencies re-verified byte-exact: r5 recursor
`d679a4d7fb4bf2619fbb3ff47ea6f386ba1c75fdc477276cabf3bec8a2b2cd90`,
transcript gate `0e0efd5ada59039a373a731038f2f88a3794b376b208879c2459bff97d0e7316`,
R3 terminal archive `e5bdd2b25cde0dccd8f1e6b8f0e1fcc815d409426308afb49c45df86af53a1e1`,
proper-open R5 terminal archive
`4b8ffc1c16828b22b2e76a3aa92a25e8c1f472190a708f30a7b71ba952cbef7e`.

**Manifest and archive arithmetic, recomputed.**  `SOURCE_MANIFEST.sha256`
has exactly **22** entries and `shasum -a 256 -c` returns **22 OK**.  The 22
are the **18** in-case files plus the **4** frozen dependencies; the 18 are
the 24 case-root files minus the six the README now names
(`aws_launch_preflight.sh`, `SOURCE_MANIFEST.sha256` itself,
`SOURCE_ARCHIVE.sha256`, `PREFLIGHT_REPORT.md`, `LAUNCH_MANIFEST.sha256`,
`REPORT_BINDING.sha256`) with the archive living under `custody/`.  The R2
review's O-N8(i) arithmetic slip is corrected in both the R3 report and the
README.  An independent `tarfile` census of the source archive:
**23 members, 23 regular files, 0 directories, 0 symlinks/hardlinks, 0
duplicates, 0 unsafe names**, single top prefix `jc2`, archive **file** mode
`0444`, member modes the inherited `0600/0644/0444` — which the R3 report and
README now state correctly (O-N8(ii) closed).  A fresh private extraction
yields 23 files / 0 symlinks and verifies **22/22 OK** with member set
exactly `entries ∪ {SOURCE_MANIFEST.sha256}`.  `LAUNCH_MANIFEST.sha256`
verifies **6/6 OK** and contains no reference to any report, so it is fully
determined by the packet and chargeable — the O-N5 repair is real.
`PREREGISTRATION.sha256` (2/2) and `SOURCE_ARCHIVE.sha256` (1/1) verify, and
`REPORT_BINDING.sha256` verifies against the producer report.

## 2. The mathematics is unchanged — proved, not asserted

**AST comparison, every top-level definition, class method and module
constant, R2 vs R3:**

| file | shared symbols | byte-identical | changed | added | removed |
|---|---|---|---|---|---|
| `resume_recursor.py` | 40 | **38** | `Recursor.run_stage`, `identical_copies` | `IDENTITY_RECORD_KEYS`, `expected_runner_stdout`, `require_runner_logs`, `require_single_line_append_stack` | none |
| `classify_resume.py` | 45 | **43** | `Classifier.check_stage`, `Classifier.verify_node_sb` | none | none |
| `prepare_resume.py` | 21 | **21** | — | — | none |
| `build_resume.py` | 23 | **23** | — | — | none |
| `run_singular_stage.py` | 9 | **9** | — | — | none |
| `containment_contract.py` | 49 | **42** | `require_job_tag`, `verify_lease`, `derive_late_decision`, `main`, and the three schema/prefix string constants | `FrozenArchiveView` + 4 accessors, `walk_fresh_root`, `authenticate_frozen_archive`, `verdict_from_bytes`, `parse_sha_sidecar_text`, `validate_lease_record`, `runtime_limits_verified`, `build_runtime_limits_record`, and 6 constants | none |

This is exactly the R3 report's §7 table, and **no definition was removed
anywhere**.  In particular `build_repaired_saturation_script`,
`validate_saturation_script`, `build_repaired_chart_script`,
`validate_chart_script`, `replace_once`, `require_count_markers`,
`require_archived_append_copies`, `Recursor.run`, `Recursor.write_summary`,
`Recursor.replay_witness`, `JobBinding`, `GENERATOR_SHA256`,
`DELTA_NODE1_SHA256`, `WITNESS_REPLAY_MARKERS` and
`ARCHIVED_NODE1_SB_APPEND_COUNT` are byte-identical to the R2 text.  One
prose imprecision: the report's §7 "added definitions" column lists the r3
`LEASE_SCHEMA`/`DECISION_SCHEMA`/`JOB_TAG_PREFIX` strings, which are
*re-pointed constants*, not new symbols.  Immaterial.

The six files claimed byte-identical are byte-identical: `prepare_resume.py`
and `run_singular_stage.py` to R2; `build_resume.py`, `adapter_selfcheck.sing`,
`diagnostic_hostile.sing`, `EXPECTED_GENERATED_SCRIPTS.sha256` to **both** R1
and R2.  `diff PREREGISTRATION.md` R2→R3 is **exactly** the header/status
prose and the appended-copy-law paragraph; there is no other hunk, so the
objective, starting ideal, recursion contract, terminal classifications and
epistemic separations are word-for-word R2.

**I re-ran preparation and the build from the real frozen archives.**  All
gates and pins reproduce, and the stdouts are byte-identical to the packet's
banked `preflight/R3_PREPARE.stdout.txt` and `preflight/R3_BUILD.stdout.txt`:

```
R3_ARCHIVE_EXACT_CENSUS=454:391:63     PROPER_OPEN_ARCHIVE_EXACT_CENSUS=574:490:84
R3_SELECTED_EXTRACTED_FILE_COUNT=294   SETTLED_OPEN_EXTRACTED_FILE_COUNT=3
OPEN_ROUTE_MEMBERS_EXCLUDED_FROM_EXTRACTION=1  ARCHIVED_TIMEOUT_REMAINS_NO_VERDICT=1
27cb85082e8ea56a4a9bc8d0cb38b889edc4e981529d6697b0ff2800e0159d0d  TRIPLE02_NODE1_WITNESS_REPLAY.sing
d9e79b427dd22718683b2ac3f5f50dbd9839622ee07bf95cb61f02bdd380d8b8  NODE_002_REDUCE_EXPECTED.sing
6f61d686f596832464ff64539c1345b55e134da082efe2500c76dc9337383ab5  RESUME_NODE_INPUT.json
d858293846ee3e3f044e8594c93af562e82d74ca09baad94b93f02bc9d02139c  BUILD_MANIFEST.json
bb8f7ee0faabbdb8e40be15bd4d6b3df319acbb5d6d6df7643954a65503d8c51  rank_size_6.support.rebuild.json
```

All five products are byte-identical to `preflight/generated/` and to the R1
pins.  The rank census reproduces `formal_slots 97020, structural_zero 95920,
support_matchable 1100, support_entries 36` — the same numbers I re-derived
independently in the R2 review, so the inherited bound 6 still stands on its
own.  The four-string terminal allowlist is unchanged and identical in
`MATH_TERMINALS`, the classifier's `ALLOWED`, and the worker's `case`; the
three-line marker format is unchanged; the settled-open no-reentry firewalls
are unchanged; and a scan for `jc2`/Jacobian/radical/geometric/whole-stratum
widening in the sources found nothing.

## 3. The O-B1 charge, item by item

My charge was to prove or refute that the late authority (a) recomputes the
charged archive hash, (b) authenticates the full archive member/manifest/
directory census, and (c) binds every decision input to a byte-identical
fresh extraction so the edit / delete / extra / symlink / mix-and-match
forgeries all fail.

**(a) PROVED.**  `authenticate_frozen_archive` refuses unless the archive
path is a regular non-symlink file whose `sha256_path` equals the charged
`--archive-sha256`.  See §4 for the one gap in *how* it re-reads the file.

**(b) PROVED.**  From the archive bytes alone it re-runs the safe-name check,
the include-prefix allowlist, duplicate detection, file/dir-members-only
typing, requires the manifest and directory-list members to exist, replays
`custody/TERMINAL_MANIFEST.sha256` line-by-line (`SHA_LINE.fullmatch`, no
duplicates, non-empty) with `regular == entries ∪ {manifest}`, checks every
per-member SHA-256 against the manifest, and replays
`custody/TERMINAL_DIRS.list` for sortedness, uniqueness and set equality with
the archive's directory members.

**(c) PROVED.**  `walk_fresh_root` walks with `followlinks=False` and refuses
any symlink or non-regular entry anywhere; the file and directory sets must
equal the archive member sets exactly; then every file member is streamed
once and byte-compared against the extraction file (the `live.read(len(block)
or 1)` idiom correctly catches short, long *and* equal-prefix-plus-suffix
files).  The 14 `DECISION_RETAINED_MEMBERS` are held in memory, and a member
absent from the archive raises `DECISION_ARCHIVE_MEMBER_MISSING` rather than
falling back to disk.  I read `derive_late_decision` line by line: after
authentication, the **only** filesystem reads are the two intentionally live
cross-checks — `live_mode_file.read_text()` and `sha256_path(live_lease)`,
both outside the extraction.  Nothing else touches the extraction, and
`custody/CANDIDATE_MATHEMATICAL_VERDICT.txt` is never read.

**The marker binding is real.**  In `main()`, `archive_sha` is literally
`args.archive_sha256` — the same string `authenticate_frozen_archive`
verified — and `decision_ok` (hence any `MATH_TERMINALS` first line) can only
be true if that authentication succeeded.  I confirmed this end-to-end
through the CLI: a clean promotion emits

```
EXACT_ENDPOINT_DEAD_ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR_FINITE_COVER
TERMINAL_ARCHIVE_SHA256=<exactly the digest authenticate_frozen_archive verified>
DECISION_RECORD_SHA256=<sha256 of the archived custody/DECISION_RECORD.json>
```

and the three degraded paths behave as documented: missing late arguments
with `--archive-ready 1` → rc 3, `LATE_DECISION_FAILURE=RuntimeError:
LATE_DECISION_INPUTS_MISSING`, marker `CUSTODY_OR_ADAPTER_FAILURE_NO_VERDICT
/ NONE / NONE`; `--archive-ready 0` → the same custody no-verdict marker.

**My 77 independent hostile fixtures (6 positive controls), all driving the
real production functions through a real freeze
(`build_complete_manifest` → `tar` → `extract_and_verify_archive`):**

| class | fixtures | result |
|---|---|---|
| A. the R2 review's §5 working forgery — rewrite both `VERDICT.txt`, both `SUMMARY.json` `classification` fields, and re-run `decision-build` inside the extraction | 1 | refused, `DECISION_FRESH_ROOT_BYTES_DRIFT:work/production/SUMMARY.json` |
| B. byte-level extraction edits: 1-byte flip (same length), truncate 1 byte, append 1 byte, empty the file, 3 MB replacement crossing the 1 MiB read block | 5 | all `..._BYTES_DRIFT` |
| C. censuses: delete a file, add a file, add an empty directory, add a hidden top-level directory | 4 | all `..._CENSUS_DRIFT` with exact missing/extra lists |
| D. type substitution: file→symlink with **byte-identical** target, directory→symlink to an identical copy, file→FIFO, fresh-root itself a symlink | 4 | `..._SYMLINK` ×2, `..._NOT_REGULAR`, `..._NOT_DIRECTORY` |
| E. archive-side: archive A + clean extraction of a different job B; archive B under A's charged digest; archive overwritten in place; archive path a symlink to the honest archive; one-nibble wrong digest; malformed digest; archive path a directory | 7 | `..._BYTES_DRIFT`, `..._HASH_DISAGREEMENT` ×3, `..._NOT_REGULAR_FILE` ×2, `DIGEST_SCHEMA_FAILURE` |
| F. attacker **re-freezes** a self-consistent archive: drop the fault-latch member; drop the decision record; embedded manifest omitting a member; embedded manifest with one wrong member hash | 4 | `..._MEMBER_MISSING` ×2, `..._MANIFEST_CENSUS_DRIFT`, `..._MANIFEST_HASH_DRIFT` |
| G. live cross-checks and latches: live lease drift; live mode flipped to `pgid`; each of the six sticky faults archived 1 / live 0; live `worker_rc` 1 vs archived 0 | 9 | `DECISION_LEASE_DISAGREEMENT`, `..._CONTAINMENT_MODE_DISAGREEMENT`, `..._FAULT_LATCH_REGRESSION` ×6, `..._FAULT_WORKER_RC_DISAGREEMENT` |
| H. archived runtime limits (each re-frozen, `verified:true` retained): `KillMode=process`, `MemoryMax` infinity/off-by-one, `TasksMax` 4096/infinity, `MemorySwapMax=infinity`, `RuntimeMaxUSec` ∈ {infinity, 5h, 21599s, 21600001us, "", "6h "}, plus `verified:false` with correct values | 13 | all `DECISION_RUNTIME_LIMITS_DISAGREEMENT` |
| I. identity and tag: live worker starttime drift, live supervisor pid drift, 6 malformed job tags, stamp-shaped wrong prefix | 9 | `..._IDENTITY_DISAGREEMENT` ×2, `JOB_TAG_STAMP_SCHEMA_FAILURE` ×4, `JOB_TAG_COMPOSITION_FAILURE` ×3 |
| J. archived shapes: two-line `VERDICT.txt`, malformed decision sidecar | 2 | `VERDICT_FILE_SHAPE`, `SHA_SIDECAR_MALFORMED` |
| L. `decide_terminal` exhaustive single-gate census, all **19** gate parameters | 19 | **19/19 load-bearing**; the clean configuration promotes |
| **positive controls** | 6 | honest DEAD chain promotes; honest bounded no-verdict promotes; live candidate mutation after the freeze is inert; both alternate accepted `RuntimeMaxUSec` renderings (`21600s`, `21600000000us`) promote; clean `decide_terminal` promotes |

Every one of the five named forgery classes fails closed.  The blocking O-B1
finding of the R2 review is **repaired in substance**, not merely in prose.

## 4. `O2-B1` — BLOCKING BEFORE ANY PILOT: the charged archive is opened twice by path

`authenticate_frozen_archive` (`containment_contract.py`, the
`sha256_path(terminal_archive)` check and the later
`with tarfile.open(terminal_archive, "r:gz")`) performs **two independent
`open()` calls on the same path**, with `walk_fresh_root(fresh_root)` — a
full recursive walk of the whole extraction — executed between them.  Nothing
holds the inode: `sha256_path` opens, reads, closes.  A same-uid writer that
`rename()`s a forged archive over `$terminal_archive` inside that window has
the digest check pass on the honest bytes and every decision input read from
the forged bytes.  Because the extraction census and byte comparison are then
performed against the *forged* member set, a matching forged extraction (which
the attacker can prepare at leisure — `$archive_replay_dir` is a plain
writable directory in `$JOB_ROOT`) passes cleanly.

**Demonstrated with genuine concurrency, no patched functions.**  I built an
honest job whose archived answer is
`NO_VERDICT_OPEN_REMAINDER_ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR` and a forged
job carrying the honest job's lease bytes and identities with the dead
string, froze both, started a **separate thread** that sleeps
`1.6 × t_hash + 4 ms` and then `os.rename`s the forged archive over the
honest path, and called the real `derive_late_decision` on the main thread:

```
pad=500   archive 37,892 B   hash 0.0 ms   authenticate 62.6 ms   RACE_RESULT=PROMOTED
pad=500                                    authenticate 63.0 ms   RACE_RESULT=PROMOTED
pad=1500  archive 100,244 B  hash 0.1 ms   authenticate 181.4 ms  RACE_RESULT=PROMOTED
pad=1500                                   authenticate 185.2 ms  RACE_RESULT=PROMOTED
pad=3000  archive 194,161 B  hash 0.1 ms   authenticate 380.7 ms  RACE_RESULT=PROMOTED
pad=3000                                   authenticate 365.3 ms  RACE_RESULT=PROMOTED
```

**6/6 promoted.**  A representative run returned candidate
`EXACT_ENDPOINT_DEAD_ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR_FINITE_COVER` with
decision `91c4e923…9f2e`, while the charged digest that the marker would
print was `c54d92cc…82af` (the honest archive) and the digest actually at the
path afterwards was `6139052d…80c9`.  Under the honest archive the same
inputs derive the bounded no-verdict.  So the published three-line marker
would carry the dead classification alongside `TERMINAL_ARCHIVE_SHA256=<the
honest archive>` and `DECISION_RECORD_SHA256=<the forged record>` — precisely
the archive/marker disagreement Sol 5.6's C1 required to be closed and my own
O-B1 re-opened, now behind a race instead of a leisurely edit.

The window is not theoretical.  It is bounded below by the extraction walk,
which scales with the tree: the *frozen* R3 terminal archive alone has 391
files and 63 directories, and a completed closed-successor job root will be
substantially larger, so a real window of tens to hundreds of milliseconds is
the expected case, and a same-uid attacker can observe the decision process's
open file descriptors to place the rename deterministically.

**Preconditions and severity.**  Identical to O-B1's: an active same-uid
writer inside `$JOB_ROOT` at decision time, which must also have evaded the
pre-freeze PGID/tag/cgroup containment censuses (those are separate
`decide_terminal` gates).  It is therefore *not* a rehearsal hazard, and I
apply the same calibration the R2 review applied to O-B1: blocking before any
mathematical run, not blocking for one disposable throwaway instance.

**Repair (one line, no behavior change).**  Open the archive once and use the
same descriptor for both operations, e.g.

```python
with terminal_archive.open("rb") as handle:
    digest = hashlib.sha256()
    for block in iter(lambda: handle.read(1 << 20), b""):
        digest.update(block)
    if digest.hexdigest() != terminal_archive_sha256:
        raise RuntimeError("DECISION_ARCHIVE_HASH_DISAGREEMENT")
    ...
    handle.seek(0)
    with tarfile.open(fileobj=handle, mode="r:gz") as archive:
        ...
```

optionally with an `os.fstat` inode/dev equality assertion for defence in
depth.  Move `walk_fresh_root` inside the `with` for clarity.  A refusing
fixture is easy: monkeypatch-free, exactly as above, plus a rehearsal item.

**Until this lands**, the strongest defensible reading of any terminal
produced by this packet remains Sol 5.6's fallback — *candidate evidence*,
not an archive-authenticated promoted verdict.

## 5. Independent audit of the remaining charged items

**Five-property runtime record (O-N3) — CONFIRMED.**  `RUNTIME_LIMIT_EXPECTED`
pins `killmode=control-group`, `memory_max=274877906944`, `tasks_max=512`,
`memory_swap_max=0` by exact string, and `RUNTIME_MAX_USEC_21600 =
("6h","21600s","21600000000us")`.  `runtime_limits_verified` is the single
predicate shared by `build_runtime_limits_record` (supervisor CLI) and
`derive_late_decision` (late authority), and the late authority requires
**both** `verified is True` **and** a recomputation from the archived
key/values, so a forged `verified:true` with wrong values is refused (13/13 in
§3.H).  The supervisor's R2 inline three-property heredoc is gone — there is
no `python3 - <<` anywhere in `aws_supervisor.sh` — and the scope is launched
with exactly `MemoryMax=274877906944 TasksMax=512 RuntimeMaxSec=21600
KillMode=control-group MemorySwapMax=0`, matching the read-back set.  Both
alternate renderings promote (positive controls).

**In-archive fault latches (O-N4) — CONFIRMED for the promotion path,
overstated for audit.**  `custody/FAULT_LATCHES_PRE_ARCHIVE.json` is written
by the supervisor immediately before `manifest-build`, so it is inside the
archive; the late authority requires it from archive bytes, requires
schema/tag/nonce/mode binding, requires `worker_rc` equality with the live
flag, and refuses any archived-1 / live-0 regression on all six sticky faults
(9/9 in §3.G).  Two caveats: (i) the archived-1 / live-1 case correctly
downgrades via `decide_terminal`, which I re-verified; (ii) the report's claim
that the post-freeze `FINALIZATION_LATCHES.txt` can be *authenticated* through
"marker → archive digest → latches" is too strong.  `FINALIZATION_LATCHES.sha256`
is a self-sidecar computed from the file it describes, and both files are
post-freeze, same-uid-writable, and not covered by the archive; the archive
digest inside the latch file is a public value an attacker can copy.  The link
is a *consistency* link, useful against corruption and mismatched artifacts,
not an authentication.  The load-bearing latch state is the in-archive one,
and that part is genuinely repaired.

**Exact runner-log law (O-N2) — CONFIRMED.**  `expected_runner_stdout` derives
the three `SINGULAR_STAGE_RETURNCODE/TIMED_OUT/ELAPSED_SECONDS` lines from the
**verified** result record, and `require_runner_logs` additionally requires an
empty stderr.  I checked it against the runner source: `run_singular_stage.py`
has exactly three `print` statements, emitting `returncode`, `int(timed_out)`
and `payload['elapsed_seconds']` in that order, matching the law including the
`int(bool(...))` normalisation; the float round-trips because `json` dumps and
Python's `str()` both use the shortest-round-trip `repr`.  It is enforced in
**both** layers and, importantly, **before** the timeout early-returns — in
`Recursor.run_stage` before `raise StageTimeout`, and in
`Classifier.check_stage` before the `expect_timeout` return — so timed-out
stages are covered.

**17-key identity census (O-N6) — CONFIRMED.**  I extracted the runner's
emitted identity dict by AST and compared it to `IDENTITY_RECORD_KEYS`:
identical 17-key sets (`argv, cap_seconds, expected_pgid, expected_sid,
job_nonce, job_tag, lease_sha256, runner, runner_cgroup, singular,
singular_binary_sha256, singular_cgroup, singular_path,
source_archive_sha256, stage_label, supervisor, worker`), enforced by
`sorted(...) != sorted(...)` in driver and classifier.  Separately I
re-derived the result-record schema three ways (runner payload AST, driver
`STAGE_RESULT_BINDING_KEYS + ("elapsed_seconds",)`, classifier
`STAGE_RESULT_KEYS`): identical 19-key set.  The R2 review's transitive-only
detection of an injected identity key is now direct.

**Exact one-line SB append law (O-N1) — CONFIRMED, non-vacuous.**  Against the
real frozen R3 archive: `output/node_001/NODE_001_STANDARD_BASIS.txt` is
`bd95508c…640d`, 14,883 B = 3 × 4,961, maximal decomposition count **3**, unit
`84872c7a1562c25933964706d65fc4394ca88ca674b41084d5e4109f4b1ef575`, and the
unit contains **exactly one newline, at its end** — the source anchor of the
law.  Running the real `require_single_line_append_stack` on the real archived
bytes: `count=3` accepts; `count=6` and `count=9` — which R2's divisibility
rule accepted — are now **refused**; `count=1` and `count=2` refused; and a
**doubled** file at `count=3` is refused.  On the vacuity question, I traced
the caller: `finish()` passes `max(header_stages, 1)`, and the only path with
`header_stages == 0` is the reduce-stage timeout, which sets
`had_timeout=True` and takes the presence-only branch.  `EXACT_EMPTY_NODE` is
reached after `header_stages += 1`, so it is a genuine `count == 1` exact
check.  O-N1 is closed as claimed.  `identical_copies` is now O(√n) over
divisors with identical semantics (maximal count, same errors), confirmed on
the real 14,883-byte file.

**Stamp enforcement (O-N8v) — CONFIRMED, with a scope note.**
`require_job_tag` now applies `STAMP_RE = ^[0-9]{8}T[0-9]{6}Z$` to the middle
segment; 4 malformed stamps and 3 malformed compositions refuse (§3.I).  Note
it is a **shape** check only: `99999999T999999Z` is accepted.  That matches
what the R2 review asked for and is not a promotion hazard (the launcher
generates the stamp with `date -u`), but the packet documents should not be
read as claiming date validity.

**Manifests / member arithmetic / mode wording — CONFIRMED** (§1).  Freeze-side
hygiene also holds: `manifest_files` refuses any symlink under an include, and
the supervisor's `tar -czf` stores symlinks as symlink members which
`extract_and_verify_archive` refuses as `ARCHIVE_NONREGULAR_MEMBER`.  The
`--include` set passed to the terminal is literally the same `manifest_cli`
array used at freeze, so the census the late authority replays is the census
the freeze built.

**Source-text gates re-verified:** the supervisor has **no** `--candidate`
argument and **no** `mv`-based publication; the stage runner has no
`start_new_session`; the worker still installs `supervisor_death_watchdog`;
`terminal_marker_text` still emits exactly three lines.

## 6. Replay census — everything below was executed by me this session

| run | result |
|---|---|
| `prepare_resume.py` on the real frozen archives | rc 0; stdout **byte-identical** to `preflight/R3_PREPARE.stdout.txt` |
| `build_resume.py` | rc 0; **5/5** products byte-identical to `preflight/generated/` and to the R1/R2 pins |
| `generator_selfcheck.py` under `python3` | rc 0, **48** stdout lines, byte-identical to `preflight/R3_GENERATOR_SELFCHECK.stdout.txt` |
| `generator_selfcheck.py` under `python3 -O` | rc 0, stdout **byte-identical to the normal run** |
| `containment_selfcheck.py` under `python3` | rc 0, **32** stdout lines, byte-identical to `preflight/R3_CONTAINMENT_SELFCHECK.stdout.txt` |
| `containment_selfcheck.py` under `python3 -O` | rc 0, stdout byte-identical |
| driver fail-closed dry run, `python3` and `python3 -O` | both rc 2, `ADAPTER_FAILURE_NO_VERDICT`, cause `RuntimeError:STAGE_RESULT_MISSING:witness_replay`, remainder = 3 generators at bound 6 with the banked generator hashes, `scope`/`settled_open_route`/`delta_node1_sha256` equal to the banked run, **byte-identical `SUMMARY.json` across interpreters** (only `job_binding` differs from the banked file, because my synthetic lease bytes differ) |
| source-archive replay | 23 file-only members, fresh extraction 23 files / 0 symlinks, **22/22 OK**, sidecar OK, `LAUNCH_MANIFEST` **6/6 OK**, archive file mode 0444 |
| terminal-CLI probes | clean promotion binds the authenticated digest into the marker; `LATE_DECISION_INPUTS_MISSING` and `--archive-ready 0` both publish the custody no-verdict marker |
| my own hostile suite | **77 refusals, 6 positive controls, 1 promotable forgery (`O2-B1`), 2 disclosed observations** |

**Fixture counts, obtained by wrapping `expect_rejection` with a counter
rather than by reading prose:**

- `generator_selfcheck.py`: **45 `expect_rejection` call sites → 49 rejection
  executions** per interpreter.  The R3 report's "45 / 49 / +3 manual = 52 /
  46 pass markers (48 stdout lines)" is exact.
- `containment_selfcheck.py`: **38 call sites → 41 rejection executions**,
  32 pass markers.  The report's "38 / 41 / +34 manual = 75" is exact.
- The report's grand total **127 hostile refusals + 38 positive controls per
  interpreter** reconciles arithmetically (52 + 75), and the manual-set
  breakdown (R2's 28 + 5 `runtime-limits-record` refusals + 1
  wrong-archive-digest CLI refusal) checks out against the source: I located
  the five `build_runtime_limits_record` mutation texts and the
  `wrong_sha_args[... "--archive-sha256" ...] = "9"*64` CLI fixture.

**One reproducibility caveat, unchanged from R2 and now correctly disclosed by
the producer:** `preflight/containment_selfcheck.json` differs from a fresh
run in exactly one field, `decision_record_sha256` (banked `75ad41a6…b718`,
mine `18474981…0ed1`, and my two runs differ from each other), because the
decision record embeds `created_utc`.  **That field is not a usable charge**;
the 32 stdout markers are, and they matched byte-for-byte.  The other 15
fields of that JSON are stable and matched.

## 7. Nonblocking findings

- **`O2-N1` Fixture-coverage overclaim on `swap_zero`.**  The R3 report §6
  says the `decide_terminal` mutation table exercises "`swap_zero` and
  `swap_violation` … jointly and singly".  In fact `swap_zero` occurs exactly
  once in `containment_selfcheck.py` — in the clean-gates dict — and
  `--swap-total`/`--swap-free` are only ever passed as `0`/`0`.  The packet's
  18-entry table therefore covers **18 of the 19** gates and leaves
  `swap_zero` unexercised.  The gate itself is fine: my own exhaustive
  single-flip census found **19/19 load-bearing**.  Fix the prose or add the
  19th row.
- **`O2-N2` Fault-latch value typing is looser than its error message.**
  `if archived_fault not in (0, 1)` accepts JSON `true`/`false` (and `0.0`)
  because `False == 0` in Python, so my "archived latch is JSON `false`"
  fixture is **not** refused.  Behaviour is nevertheless safe and identical to
  the integer case (`false`→no fault, `true`→fault, which then requires a live
  fault), and the supervisor writes integers.  Use `isinstance(v, int) and not
  isinstance(v, bool)` if the schema check is meant to be a type check.
- **`O2-N3` `FINALIZATION_LATCHES` is consistency-checked, not
  authenticated** — see §5.  Prose in the R3 report §3 (O-N4) and README
  should say so.
- **`O2-N4` The terminal CLI can exit without writing a marker.**  With
  `--archive-ready 1` and a malformed `--archive-sha256`, `derive_late_decision`
  fails inside the guarded `try`, but the later unguarded
  `require_digest(archive_sha, "terminal-archive")` raises, so the process
  exits rc 1 with **no marker file**.  This is caught at the supervisor level
  (`decision_rc != 0 && != 3` writes the emergency
  `CUSTODY_OR_ADAPTER_FAILURE_NO_VERDICT` marker), so it is fail-closed in
  practice; but the CLI alone is not, and the packet describes the CLI as
  always publishing a marker.
- **`O2-N5` The stamp regex is shape-only** — see §5.  No verdict impact.
- **`O2-N6` The live lease and live containment-mode files are fragile
  decision inputs.**  Any post-freeze byte change to `$JOB_ROOT/LEASE.json` or
  `custody/containment_mode.txt` — including an innocent one — downgrades to a
  custody no-verdict.  That is the correct direction, but it should be listed
  with the other downgrade-only surfaces in §9 of the report so a rehearsal
  operator does not read a no-verdict as evidence of tampering.
- **`O2-N7` Scope statement worth making explicit.**  The archive-bytes
  binding authenticates the marker against the archive; it does **not**, and
  cannot, defend against a job tree that was already forged *before* the
  freeze.  That window is covered instead by the classifier's regeneration,
  byte comparisons and `Ledger` artifact closure plus the containment
  censuses.  The R3 report's §2 reads as if archive authentication closes the
  whole class; it closes the post-freeze half.  I verified the pre-freeze half
  is genuinely defended by other means, so this is a documentation point.

## 8. Rehearsal debt (all Linux/systemd/Singular obligations)

Nothing in this review establishes any behaviour that requires Linux,
`/proc`, systemd, cgroups, or Singular.  **No Singular has run anywhere in
this campaign**: the witness replay, both Singular control scripts and every
node stage execute for the first time on AWS.  The launcher, supervisor, stage
runner, systemd scope, supervisor-death watchdog, PGID cleanup, cgroup
censuses and live `/proc` identity gates have never executed.  Every fixture
in the packet, and every fixture of mine, is pure or parser-level, run on
macOS.  That separation is stated correctly and repeatedly in the R3 report
§9, `PREFLIGHT_REPORT.md` "Known local gaps", both preregistrations and both
selfcheck docstrings, and I found no fixture overclaiming live coverage.

The eleven-step mandatory rehearsal in `AWS_PREREGISTRATION.md` now includes
verbatim-in-substance the four items I added in the R2 review — step 8 (O-B1
regression on the live extraction), step 9 (exact `systemctl --user show`
read-back of all five properties), step 10 (watchdog degradation with the user
manager healthy *and* unavailable), step 11 (real runner-log shapes for a
successful and a timed-out stage) — plus the archived-unit and pivot/residual
capture note.  I endorse steps 1–11 unchanged and **add one**:

12. **`O2-B1` regression.**  After the `O2-B1` repair lands, on the disposable
    instance start a same-uid helper that renames a forged terminal archive
    over `$terminal_archive` while `containment_contract.py terminal` is
    running, and confirm the terminal refuses (`DECISION_ARCHIVE_*`) and
    publishes only a custody no-verdict.  Until the repair lands, record the
    unrepaired behaviour explicitly and treat any marker as candidate
    evidence only.

Also still open and inherently live: the `RuntimeMaxUSec` rendering set (an
honest host rendering outside `6h`/`21600s`/`21600000000us` downgrades, never
promotes — step 9 captures it); the decision-time cost of the extra whole-
archive streaming pass; node-2 saturation cost and reverse bound 64, which
remain preregistered bounded no-verdicts.

## 9. Scope firewall and maximum possible claim

Unchanged from Sol 5.6 and my R2 review, and re-verified: `MATH_TERMINALS`,
the classifier's `ALLOWED`, and the worker's `case` statement are the same
**four** strings, with no radical, geometric, whole-component, whole-stratum
or JC2 widening anywhere in the sources or documents.

- `EXACT_ENDPOINT_DEAD_…_FINITE_COVER` would mean, at most: exact endpoint
  death on the finite chart cover of **only** `V(I_node1 + (Delta_node1))` in
  `Spec Q[q0,q2,c4,c6]`, `dp` order.
- `RING_LEVEL_ENDPOINT_SURVIVOR_…_PENDING_NILPOTENCE_RADICAL` would mean, at
  most: a nonzero endpoint coefficient in the certified saturated quotient on
  **one** closed-successor chart, pending nilpotence, radical and geometric
  analysis.
- The two bounded strings carry **no** mathematical conclusion.

The settled node-1 proper open (`EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY`)
is never combined with them: it is routing provenance, its two products are
never extracted, and the `Delta_node1` hash guard is enforced in builder,
driver and classifier.  **With `O2-B1` unrepaired**, a promoted marker is not
race-free-authenticated by the archive it names, so the maximum defensible
reading of any terminal produced before that repair is *"candidate evidence
for the TRIPLE02 node-1 closed-successor recursion"*, with no authenticated
promoted mathematical verdict.  With `O2-B1` repaired and the rehearsal
discharged, the two bullets above become available at their stated,
chart-local strength — and only then, after a separate coordinator `GO`.

## 10. What this review establishes, and what it does not

Established, at source level and by execution on macOS in pure Python: every
charged hash and seal; the archive censuses, manifests and member/mode
arithmetic; the byte-identity of the mathematical recursion by AST and by
rebuild; the five build-product pins and the rank census; the exact
single-line append law and its anchor on the real archived unit; the runner-log
law against the runner source; the 17-key and 19-key schema agreements; all
19 `decide_terminal` gates; the archive-bytes authentication and every
decision-record equality; the fault-latch monotonicity gate; the five-property
runtime predicate; the lease, nonce, stamp and marker behaviours; and the
source-text gates.

Not established, and not claimed by the producer either: anything requiring
Linux, `/proc`, systemd, or Singular.

Seals.  This report's **body** SHA-256 is the last line below.  Its **full-file**
SHA-256 cannot be embedded in itself; it is published in the delivery summary
accompanying this file and is reproducible with
`shasum -a 256 xmodel/triple02-node1-closed-successor-resume-r3-hostile-review-opus5-20260829.md`.
The subject of this review is the R3 producer report, full
`4ffa10477238c0726ba8b470a2ce6110671f823f6cebc1501a71bd48f7f97c0c`, body
`ea71583070a6c51c11c6201b8a3f8f74d541652116a880dd8f6ed412c0759f76`, and the
R3 packet at source-archive digest
`2f129c2258a6d512bd8fe873db97c142c436bafdf0d7fee37997e4a3086e0bc1` with
launch manifest `10fbc308aefbb2dfbe6c45d987feb27a7e930841aa0c76eb853c8e8a9a87dac5`.

Report-body SHA-256 (all preceding bytes, including the newline immediately before this line): 206ebc55548c7218a4966990050510da38279461a9d9279cc3cc5533f959685c
