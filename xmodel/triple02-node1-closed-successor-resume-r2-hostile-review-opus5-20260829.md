# Hostile source review: TRIPLE02 node-1 closed-successor resume R2

Reviewer: Opus 5 (`claude-opus-5`), independent of the R2 producer (Fable 5)
and of the R1 hostile reviewer (`gpt-5.6-sol`).  Packet label: 20260829.
Review environment date: 2026-08-28, America/Los_Angeles.  Working directory:
`/Users/dc/code/math/jc2`.

## Verdict

**`PASS_FOR_DISPOSABLE_LIVE_LINUX_REHEARSAL`**

The R2 packet is source-complete and, on every check I could run without a
CAS or a Linux host, materially better than R1.  R1 blockers C1, C2 and C3
are repaired in substance, not just in prose: I reproduced every charged
hash, rebuilt every seal outside the packet, replayed both selfcheck suites
under `python3` and `python3 -O`, and ran **258 independent hostile fixtures
of my own construction** against the real production functions.  The
mathematical recursion is verifiably byte-identical to the one R1's review
confirmed, and the producer's self-found archived-standard-basis defect is
real, correctly diagnosed and correctly repaired.

The only action this review licenses is **one disposable-instance
live-Linux/Singular rehearsal** per `AWS_PREREGISTRATION.md` §"Mandatory
disposable-Linux rehearsal", extended by the four items in §8 below.  No AWS
mathematical run, pilot, or promotion is authorized, and nothing here
constitutes a mathematical result.

I found one **blocking-before-pilot** defect, `O-B1`, that the R2 report does
not disclose and the R2 fixture suite does not reach: the late terminal
authority authenticates the *fresh extraction directory*, not the frozen
archive bytes, so a same-uid writer inside `$JOB_ROOT` during the window
between `archive-extract-verify` and the `terminal` call can publish a
`TERMINAL.marker` that disagrees with the archive it names.  I demonstrate a
working promotion of a bounded no-verdict to the dead string in §5.  This is
a strictly narrower re-instance of the failure mode Sol 5.6 named in C1
("the public marker can also disagree with the reviewed archive"), and it
must be repaired and re-reviewed before any mathematical run.  It does not
make a throwaway rehearsal unsafe, which is why the license above stands.

No AWS or web operation was performed.  No Singular, msolve, Sage, PARI or
other heavy CAS was run.  No commit, push, or canonical-ledger edit was made.
`jc2-lean` was not accessed, listed, searched, built, status-checked or
controlled, and no repository-wide Git or workspace-wide search was run.  The
only file I created or modified is this report; bounded scratch lived under
`/tmp/t02r2-opus5`.

## 1. Charged hashes (all reproduced this session)

Recomputed with `shasum -a 256` from outside the packet.  Every value in the
R2 report's §5 table matched exactly; nothing is quoted from the producer.

| object | SHA-256 | R2 claim |
|---|---|---|
| `xmodel/…r2-repair-fable5-20260829.md` (this review's subject) | `c6322ccf5e25c27575c8b0f3e1b8f7b37a5a8add70d2687e9dcf4feb41dc8757` | matches `LAUNCH_MANIFEST` line |
| its body hash (lines 1–390, incl. trailing newline) | `fbefb5011f91274f00ebe75b472b12cf1422da7f487d66b858f37aac678dd6c0` | match |
| `xmodel/…r1-fable5-20260829.md` | `93b894306401e1e2e1965788708b9fe071f93336d4db01446ad7f58c3b0dcca9` | match |
| `xmodel/…r1-hostile-review-sol56-20260829.md` | `ad25f49675f26128d220a5954c8e7f72580060b929e42868eeefaefd75cfafb2` | match |
| `prepare_resume.py` | `1eb8ed781843fd0efd633722ddd74853266d0e361b6e78a0d7e5ab9e1b302528` | match |
| `build_resume.py` | `3763ac7a5ce2915ede7c21c9d9b8dcb3fc1ab12075c998daa646a375b640f780` | match, byte-identical to R1 |
| `resume_recursor.py` | `f3a069495afcb7f4eef95cb0de4b1aa05f2dfde61ce598576098ac45defdb84e` | match |
| `classify_resume.py` | `a8887f05d59a3b1fae45491fac8eaa076ffa679cbf7fc8fb0ce0ef1e0d9fe345` | match |
| `generator_selfcheck.py` | `6ea8bd981f31ceea9d50d867fd7989f004017043849cfeafd1e0ebf3ff6ea3de` | match |
| `run_singular_stage.py` | `766bebf02496c2bcdd34c575219b819d4d332f404f286cc49dedab793ffe9564` | match |
| `containment_contract.py` | `0f47a460ec8c579b5e9782292b4d2ab92758996ada8e6cb7df2d038ee7b1ed55` | match |
| `containment_selfcheck.py` | `f285b577d76f181384999327536a3b80cb25f34caa5a80323404021ec91627b8` | match |
| `adapter_selfcheck.sing` | `e616b59542a977dd9daa6865dbf18b60feaae06f784d98f72cf8cced27ee4490` | match, byte-identical to R1 |
| `diagnostic_hostile.sing` | `01be817524da040ad97eeb52adc461d6556e2d8cd179c9447c4c5101a2f15e02` | match, byte-identical to R1 |
| `aws_job_worker.sh` | `e34f4fe2b8d3c2c32e83a3ff1a27e7bcabc9c37b4de35835475775224b601039` | match |
| `aws_supervisor.sh` | `62e68a6d3de7da61116eaf19e79a3ecfb6dd2c0fddf33851fe8be10a2a23d31d` | match |
| `aws_launch_preflight.sh` | `fce26e922f2ebfa797436d6894840b092dc224226d6cfac5d2a7893309892851` | match |
| `runtime_expectations.env` | `d4bfe8cb6d8223b2939c3afe503f7b1283449022c6efcbc481387465afa4ba32` | match |
| `EXPECTED_GENERATED_SCRIPTS.sha256` | `9912dd2279223347d461b5640583b84283216d4873b56e3be34770314f2b5696` | match, byte-identical to R1 |
| `SOURCE_MANIFEST.sha256` (22 entries) | `cd4e47ee6f9c0fc48c49b4718a0aa762e946b90efd85b28aa1736c9ab5d05733` | match |
| `PREREGISTRATION.md` | `95100ac755991d1a7f0d83ca3d33f9cebd80f2746b3885de8de0bea71640b67a` | match |
| `PREREGISTRATION.sha256` | `ed66a65aeaaca13cabf208b3ccaf29b21949c8046d2798de47ce4fa4b0d7a8f8` | match |
| `AWS_PREREGISTRATION.md` | `c1a906b42f3fd14a0f7d26af8dd0d47cf13f69285ece9a45bd4b942f65beb216` | match |
| `README.md` | `4297eb105be4f76e0fdab9c444c6cadb97ef057f878a20ff334cd47c0f7867fb` | match |
| `PREFLIGHT_REPORT.md` | `22316004c500f0ebedabf1bdf239f62d9d07e2936f792cd7d24ccc6818f69503` | match |
| `SOURCE_ARCHIVE.sha256` | `c58a5f678cd4b89c3c5c048e597a8f9e452a0f4de13b9f285bd1732b8944baf9` | match |
| source archive `custody/ggv_triple02_closed_successor_resume_r2_SOURCE.tar.gz` | `183ab5e0139cf6b68482f58ed72e63262f3423c6ffa3f3b5568a014c44a65987` | match |
| **`LAUNCH_MANIFEST.sha256`** (untabled by the producer — charge it) | `ba697115001232b95d58fb54e3102e1a7df28fad5e37849a68757af5b021dc34` | not claimed |
| frozen r5 recursor | `d679a4d7fb4bf2619fbb3ff47ea6f386ba1c75fdc477276cabf3bec8a2b2cd90` | match |
| frozen transcript gate | `0e0efd5ada59039a373a731038f2f88a3794b376b208879c2459bff97d0e7316` | match |
| R3 terminal archive | `e5bdd2b25cde0dccd8f1e6b8f0e1fcc815d409426308afb49c45df86af53a1e1` | match |
| proper-open R5 terminal archive | `4b8ffc1c16828b22b2e76a3aa92a25e8c1f472190a708f30a7b71ba952cbef7e` | match |

Archive facts, recomputed with an independent `tarfile` census: the source
archive has **23 members, 23 regular files, 0 directories, 0 duplicates, 0
unsafe names**, single top-level prefix `jc2`.  The archive *file* is mode
`0444`; member modes are the inherited `0444/0600/0644` and are not
normalized (harmless — extraction is hash-verified, but the R2 report's
"(23 file-only members, mode 0444)" reads as a member-mode claim and is not
one).  A fresh private extraction verified **22/22** `SOURCE_MANIFEST.sha256`
entries with `missing []`, `extra ['…/SOURCE_MANIFEST.sha256']` — i.e. the
member set is exactly the 22 manifest entries plus the manifest.  The loose
in-case and frozen-dependency copies also verified 22/22.

The two corrected frozen-archive censuses are **confirmed against the real
archives**: R3 `members=454 files=391 dirs=63 dup=0 unsafe=0`; proper-open
`members=574 files=490 dirs=84 dup=0 unsafe=0`.  R1's `437/374` and `565`
prose was stale; R2 is right and now enforces both as preparer hard gates.

`LAUNCH_MANIFEST.sha256` lists the launcher, the archive sidecar, the
archive, `SOURCE_MANIFEST.sha256`, both preregistrations, and the R2 report
hash `c6322ccf…8757`, which matches the file.

## 2. The mathematics really is unchanged — proved, not asserted

The R2 report claims the recursion is byte-identical to R1's.  I checked
this at the level of parsed definitions rather than by reading prose.

Parsing both `resume_recursor.py` files and comparing every top-level
definition and module constant textually:

- **23 of 23** shared top-level definitions/constants are **byte-identical**,
  including `build_repaired_saturation_script`, `validate_saturation_script`,
  `build_repaired_chart_script`, `validate_chart_script` and `replace_once`;
- `Recursor.run` — the entire node loop, route guards, descent rule and
  terminal branches — is **byte-identical**;
- exactly four methods changed (`__init__`, `run_stage`, `write_summary`,
  `replay_witness`) and six symbols were added (`NONCE_RE`,
  `ARCHIVED_NODE1_SB_APPEND_COUNT`, `STAGE_RESULT_BINDING_KEYS`,
  `identical_copies`, `require_archived_append_copies`, `JobBinding`).  All
  are custody bindings plus the standard-basis comparison.

`build_resume.py`, `adapter_selfcheck.sing`, `diagnostic_hostile.sing` and
`EXPECTED_GENERATED_SCRIPTS.sha256` are byte-identical files.  The
`PREREGISTRATION.md` diff is exactly the appended-copy law, the two exact
censuses, and status wording — no mathematical widening.  `prepare_resume.py`
adds only the two census constants, their two hard gates, and two prints
(printed *after* the gates, so they are not producer-authored banners).

I re-ran preparation and the build from the real frozen archives.  All five
build products reproduce the R1 pins and the packet's own `preflight/`
evidence byte-for-byte:

```
27cb85082e8ea56a4a9bc8d0cb38b889edc4e981529d6697b0ff2800e0159d0d  TRIPLE02_NODE1_WITNESS_REPLAY.sing
d9e79b427dd22718683b2ac3f5f50dbd9839622ee07bf95cb61f02bdd380d8b8  NODE_002_REDUCE_EXPECTED.sing
6f61d686f596832464ff64539c1345b55e134da082efe2500c76dc9337383ab5  RESUME_NODE_INPUT.json
d858293846ee3e3f044e8594c93af562e82d74ca09baad94b93f02bc9d02139c  BUILD_MANIFEST.json
bb8f7ee0faabbdb8e40be15bd4d6b3df319acbb5d6d6df7643954a65503d8c51  rank_size_6.support.rebuild.json
```

Preparation markers reproduced exactly: `R3_ARCHIVE_EXACT_CENSUS=454:391:63`,
`PROPER_OPEN_ARCHIVE_EXACT_CENSUS=574:490:84`,
`R3_SELECTED_EXTRACTED_FILE_COUNT=294`,
`SETTLED_OPEN_EXTRACTED_FILE_COUNT=3`,
`OPEN_ROUTE_MEMBERS_EXCLUDED_FROM_EXTRACTION=1`.

**Independent re-derivation of the inherited rank bound.**  I recomputed the
structural bound from the archived node-1 residual without trusting either
producer or the archived certificate: **36 support entries**, global maximum
bipartite matching **6**, size-7 minors **0 / 39600** support-matchable,
size-6 minors **1100 / 97020**.  My rebuilt census equals the archived
`rank_size_6.support.json` exactly (`formal_slots 97020, structural_zero
95920, support_matchable 1100, support_entries 36`).  The inherited bound 6
therefore stands on its own.  The archived `reduce.sing` is byte-reproduced
by the frozen builder (`FROZEN_SOURCE_RECONSTRUCTION_PASS`), which I
re-verified directly.

## 3. The self-found standard-basis defect: confirmed real, correctly fixed

This is the strongest part of the R2 packet and I could reproduce all of it.

- The archived `NODE_001_STANDARD_BASIS.txt` is `bd95508c…640d`, **14,883
  bytes = 3 × 4,961**, and the three 4,961-byte blocks are byte-identical
  (unit SHA-256 `84872c7a1562c25933964706d65fc4394ca88ca674b41084d5e4109f4b1ef575`).
- The count 3 is *derived*, not guessed: `node_header` in the frozen r5
  recursor contains exactly one `write("NODE_{n:03d}_STANDARD_BASIS.txt", …)`
  and is included by `build_reduce_script`, `build_rank_size_script`,
  `build_saturation_script` and `build_chart_script`.  The archived node-1
  directory ran reduce, rank_size_6 and saturation, and **all three stdouts
  contain `NODE_REDUCER_FIXTURES_PASS=1`**, which the frozen header prints
  *after* the write — so all three appends landed, including the one from the
  saturation stage that later timed out (cap 900 s, rc 1, `timed_out: true`).
- The stage-unique files are single-copy, as R2 says: pivots 1,208 B / 96
  lines (1 header + 95), residual 1,853 B / 111 lines (1 header + 110), and
  neither admits a nontrivial identical-copy decomposition.
- The witness-replay script calls `r5.node_header(...)` exactly once, so it
  writes one copy; and the header block of the regenerated witness replay is
  **byte-identical to the archived `reduce.sing` header block in all 18 lines
  except the leading `//` comment** — same ring declaration, same
  `NODE_IDEAL`, same `std`, same write.  So `archived == produced * 3` is the
  right law and is satisfiable, subject only to Singular determinism on the
  live host (rehearsal debt).
- R1's rule `produced == archived` was therefore **unconditionally
  unsatisfiable**: the R1 job was guaranteed to end
  `ADAPTER_FAILURE_NO_VERDICT` at the witness replay.  R2's diagnosis is
  correct and the R1 review did not reach it.

`require_archived_append_copies` is exact: it accepts the honest single copy
and refuses the full-archive resubmission, a double copy, an empty produced
file, and `count = 0`.

**Independent write-set derivation (the probe the R2 report §7.5 invites).**
I regenerated all four node-2 stage scripts from the frozen builders and the
packet's repaired templates and extracted every literal `write()` target,
resolving `string` variables.  The classifier's `stage_singular_writes` set
is **exactly right for all four stage types — no missing name, no extra
name** — and each stage writes the node standard basis **exactly once**:

| stage | write targets (occurrences) | vs. classifier expected set |
|---|---|---|
| reduce | SB×1, REDUCE_PIVOTS×2, REDUCE_RESIDUAL×2 | exact |
| rank_size_6 | SB×1, SIZE_6_MINORS×1101, SIZE_6_WITNESS×1101 | exact |
| saturation | SB×1, OPEN_SAT_SB×1, REV_ATTEMPTS×2, REV_WITNESSES×2, EMPTY_OPEN_CERT×1, NEXT_SB×1 | exact |
| chart | SB×1 + 11 chart artifacts | exact |

This also validates two structural choices I attacked separately: the
saturation-exhausted branch correctly *drops* `EMPTY_OPEN_POWER_CERTIFICATE`
and `NEXT_STANDARD_BASIS` from the required set (the script `quit`s before
both writes), and the reverse-containment TSV headers are written before the
`OPEN_UNIT_NF!=0` guard, matching the classifier's zero-record census on the
empty branch.  `CHART_ACTIVE_STANDARD_BASIS` and `OPEN_SAT_STANDARD_BASIS`
are each written once by a single distinct stage, so the classifier's
byte-exact cross-stage comparison of the two is legitimate.

## 4. Replays and exact test counts

Everything below was executed by me this session.

**Packet suites (both interpreters).**

| run | result |
|---|---|
| `prepare_resume.py` on the real archives | rc 0; stdout byte-identical to `preflight/R2_PREPARE.stdout.txt` |
| `build_resume.py` | rc 0; 5/5 products byte-identical to `preflight/generated/` and the R1 pins |
| `generator_selfcheck.py` under `python3` | rc 0, 40 stdout lines, byte-identical to `preflight/R2_GENERATOR_SELFCHECK.stdout.txt` |
| `generator_selfcheck.py` under `python3 -O` | rc 0, stdout **byte-identical to the normal run** |
| `containment_selfcheck.py` under `python3` | rc 0, 25 stdout lines, byte-identical to `preflight/R2_CONTAINMENT_SELFCHECK.stdout.txt` |
| `containment_selfcheck.py` under `python3 -O` | rc 0, stdout byte-identical |
| driver fail-closed dry run, `python3` and `python3 -O` | both rc 2, `ADAPTER_FAILURE_NO_VERDICT`, cause `RuntimeError:STAGE_RESULT_MISSING:witness_replay`, remainder = 3 generators at bound 6 with the three charged hashes, **byte-identical `SUMMARY.json`** |

Fixture counts, obtained by wrapping `expect_rejection` with a counter rather
than by reading the producer's prose:

- `generator_selfcheck.py`: **34 `expect_rejection` call sites → 38 rejection
  executions** per interpreter (two sites are 3-way loops), plus 3 manual
  refusal controls = **41 hostile refusals**, and 38 stdout markers (37 ending
  `=1`, one `CHART_COUNT_GATE_MUTATIONS_REJECTED=2`).  The R2 report's
  "34 call sites / 38 executions / 41 refusals / 38 pass markers" is exact.
- `containment_selfcheck.py`: **25 `expect_rejection` call sites → 25
  rejection executions**, 25 stdout markers.  The claimed additional "28
  manual refusals" reconcile arithmetically (18 `decide_terminal` mutations +
  foreign candidate + wrong PGID + launcher starttime + hung-reap + six
  terminal-CLI refusals) and I did not find that count inflated.

One reproducibility caveat: `preflight/containment_selfcheck.json` records
`decision_record_sha256`, which embeds `created_utc` timestamps and therefore
differs on every run (mine: `8f2062c2…` and `39e65934…`; packet:
`3cae3381…`).  **That field is not a usable charge**; the 25 stdout markers
are, and they matched byte-for-byte.

**My own hostile fixtures — 258 refusals, 3 disclosed gaps, 22 positive
controls.**  All drive the real production functions.

| suite | construction | result |
|---|---|---|
| O1 `decide_terminal` exhaustive | all 19 gate parameters flipped singly (19) and in all 171 unordered pairs, plus foreign and `None` candidate (2) | **192/192 → `CUSTODY_OR_ADAPTER_FAILURE_NO_VERDICT`**; clean configuration promotes.  Every one of the 19 gates is load-bearing; no pairwise leak |
| O2 C1 late authority | full synthetic job trees driven through `build_decision_record` + `derive_late_decision` | **15/15 refused**: archived classifier verdict swap; both verdicts+summaries swapped with stale record; hand-edited record candidate with refreshed sidecar; record copied from another job; `decision-build` in pgid mode; archived mode flipped to pgid; four runtime-limit mutations (infinity / `verified:false` / `KillMode=process` / swap allowed); foreign proper-open candidate; live lease ≠ archived lease; supervisor starttime drift; artifact-manifest tamper; sidecar mismatch.  Positive controls: honest NO_VERDICT and honest DEAD chains promote; **mutating and deleting the live `CANDIDATE_MATHEMATICAL_VERDICT.txt` after the freeze are both inert** |
| O3 archive/manifest/publication | real tarballs and roots built by me | **11/11 refused**: unmanifested empty directory at manifest-verify *and* at archive-extract-verify; unmanifested regular file; member outside the includes; symlink member; traversal member; duplicate member name; stale embedded manifest with valid outer bytes; unsorted directory list; pre-existing extraction destination; second `publish_no_replace` (`TERMINAL_ALREADY_PUBLISHED`, first marker survives byte-for-byte) |
| O4 append-copy law / node SB census / nonce+tag fuzz | direct calls | **23 refused** (4 append-copy, 1 empty-artifact, 4 node-SB census, 9 nonce, 5 tag), 11 correct acceptances; **3 disclosed acceptances** — see O-N1 |
| O5 classifier mutations on a real regenerated fixture | 13 mutations I wrote, on the packet's own strict dead fixture (real regenerated scripts, full synthetic binding) | **11 refused**: extra file in `witness_replay/`; stray `node_099`; stray non-node directory; duplicated success marker; identity record with an injected key (caught transitively via `DRIVER_STAGE_RECORD_DISAGREEMENT`); nonempty stage stderr with rehash; reversed `NODE_INPUT` generator order; node SB reduced to one copy; 1-byte witness pivot tamper; tag/nonce mismatch in the binding; wrong slow-cap in the binding.  **2 accepted** — see O-N1, O-N2.  Baseline and post-mutation restore both classify DEAD |
| O6 source-text gates | my own mutations of copies of the shell/runner sources | **6/6 fired**: reintroduced `mv` marker publication; reintroduced `--candidate`; `RuntimeMaxSec=21600` removed; `start_new_session=True` in the stage runner; `supervisor_death_watchdog` removed from the worker; `MemorySwapMax=0` removed.  Clean copies pass before and after |
| O7 extraction TOCTOU | see §5 | **1 promotable forgery** — `O-B1` |

I also re-derived the stage result-record schema three ways — from the
runner's emitted `payload` dict (AST), from the driver's
`STAGE_RESULT_BINDING_KEYS + ("elapsed_seconds",)`, and from the classifier's
`STAGE_RESULT_KEYS` — and all three are the identical 19-key set.  The R2
report's schema-agreement probe is correct.

## 5. `O-B1` — BLOCKING BEFORE ANY PILOT: the late authority authenticates the extraction directory, not the archive

`aws_supervisor.sh` extracts the frozen archive into
`$JOB_ROOT/.terminal_archive_replay.$$`, verifies it with
`archive-extract-verify` plus `sha256sum -c`, hard-links the archive into
place, and then calls `containment_contract.py terminal --fresh-root
"$archive_replay_dir"`.  `derive_late_decision` re-reads that directory.  It
never re-verifies the manifest at read time, never re-extracts the decision
record from `$terminal_archive`, and never ties `--fresh-root` to
`--archive-sha256`; the extraction is a plain, writable directory inside the
job root, and the archive digest is carried into the marker straight from a
shell variable.

Concrete attack, executed:

1. Build an honest job whose archived answer is
   `NO_VERDICT_OPEN_REMAINDER_ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR`.
   `derive_late_decision` returns that string, decision `f8190518…`.
2. As the same uid, inside the extraction: rewrite `output/VERDICT.txt`,
   `work/production/VERDICT.txt` and both `SUMMARY.json` `classification`
   fields to the dead string, then re-run `decision-build` over the rewritten
   tree (the lease, identities, mode, runtime limits and artifact manifest
   are untouched and still self-consistent).
3. `derive_late_decision` now returns
   `EXACT_ENDPOINT_DEAD_ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR_FINITE_COVER`
   with decision `750dfebe…`, every gate clean.

The published three-line marker would then carry the dead classification and
`TERMINAL_ARCHIVE_SHA256=<the honest archive>` alongside
`DECISION_RECORD_SHA256=<the forged record>` — i.e. exactly the
archive/marker disagreement Sol 5.6's C1 required to be closed, reachable in
a narrower window.  Unlike R1's C1, this needs an active same-uid writer
rather than a mere rerun or race, which is why it is blocking for a pilot
rather than for a rehearsal.

Required repair (any one suffices, all cheap):

- re-run `verify_complete_manifest(fresh_root, …)` as the first act of
  `derive_late_decision`; **and/or**
- re-open `$terminal_archive`, re-check its outer digest against
  `--archive-sha256`, and extract `custody/DECISION_RECORD.json` from the
  archive itself for the content-address check; **and/or**
- extract to a directory made non-writable after verification and assert that
  property at decision time.

Until then, the strongest defensible reading of any future terminal remains
Sol 5.6's fallback: *candidate evidence*, not an archive-authenticated
promoted verdict.

## 6. Adjudication of R1 blockers C1–C3 and the subsidiary findings

**C1 — REPAIRED IN SUBSTANCE, with `O-B1` residual.**  The `terminal`
subparser has no `--candidate` argument at all (I read the parser, and my own
source-gate mutation confirms `containment_selfcheck` refuses if `--candidate`
reappears anywhere in the supervisor).  The candidate is derived inside
`build_decision_record` from the equality of the production and classifier
`VERDICT.txt`, cross-checked against both `SUMMARY.json` `classification`
fields and both job-binding blocks, and re-derived at the late stage from the
archived record plus the archived verdicts.  My 15 attacks (§4, O2) all
refused, and live-candidate mutation *and* deletion after the freeze are both
inert.  The public marker is three lines binding archive and decision
digests, published by `ln(2)`.  Residual: `O-B1`, plus `O-N4` below.

**C2 — REPAIRED.**  Verified independently: the 19-key result-record schema
agrees across runner, driver and classifier; the classifier regenerates the
witness replay, the node-2 reduce, every rank-size script, and the repaired
saturation and chart scripts, and byte-compares each; it requires the
identity record and its hash from every result and checks tag, nonce, lease,
source, binary, path, argv, cap, PGID/SID, uid, worker/supervisor
pid+starttime, and runner/child cgroup equality; it regenerates each rank
census JSON and byte-compares it; the exact-artifact `Ledger` closes every
production directory, and I confirmed its expected write sets against the
frozen builders (§3) with no discrepancy.  Bounded no-verdicts are genuinely
re-derived: the classifier computes `derived`/`derived_reason` from the node
evidence and then requires equality with the driver's `no_verdict_reason`,
remainder literals, remainder hashes, bound, and full `stage_records` list;
a fabricated reason without a timed-out stage, and a timed-out stage without
a matching reason, are both refused, as is a second timed-out stage.  Note
that `MAX_NODES`/`START_NODE`/`FINAL_NODE` are hard-coded in the classifier
and would disagree with any driver run under different `--max-nodes`.

**C3 — REPAIRED AT SOURCE LEVEL; ALL LIVE BEHAVIOR UNTESTED.**  The
NO_VERDICT-only PGID fallback is triple-protected and I verified all three
independently: the worker writes `PGID_FALLBACK_PRODUCTION_SKIPPED.marker`
and `exit 0`s *before* the watchdog, any stage, or any production;
`build_decision_record` raises `DECISION_REQUIRES_SYSTEMD_SCOPE`; and
`derive_late_decision` requires recorded == archived == live mode
`systemd_scope` with a verified runtime-limit record.  The scope is launched
with `RuntimeMaxSec=21600 KillMode=control-group MemoryMax=274877906944
TasksMax=512 MemorySwapMax=0`, probed first with a 30 s throwaway scope, and
read back with `systemctl --user show`.  See `O-N3` for the read-back's exact
scope.  The supervisor-death watchdog is a design, not evidence.

**Subsidiary findings.**  Nonce schema `^[a-z0-9]{8,32}$` and tag composition
are enforced in launcher, contract, supervisor, worker, stage runner and
classifier; my 14-case nonce/tag fuzz found no acceptance of empty, short,
long, uppercase, punctuated, spaced, unicode or newline-suffixed values, nor
of the R1 empty-suffix tag.  No-replace publication verified by real
collision (first marker survives).  Directory-exact archive verification
verified by *my own* empty-directory fixtures at both manifest-verify and
archive-extract-verify.  Launcher self-binding verified by reading the
launcher (self-hash line match, archive line match, 23-member census, prefix
allowlist, read-only self-copy, lease build) — see `O-N5` for its limit.  The
stale censuses are corrected and now hard gates.  Fixture-realism labelling is
explicit and, as far as I can tell, honest: I found no fixture that claims
live process coverage.

## 7. Nonblocking findings

- **`O-N1` Node standard-basis census enforces divisibility, not equality.**
  `Classifier.verify_node_sb` requires `count % header_stage_count == 0`.  I
  confirmed at the real classifier that a node with 3 header stages passes
  with 3, 6 or 9 copies, and that doubling the fixture's node SB is accepted;
  1, 2 and 4 copies are refused.  The R2 report §3 and `PREREGISTRATION.md`
  both say "matching the completed header-writing stage count" / "one copy per
  completed node stage", which is stronger than the code.  Impact is small —
  the node SB is not used for any mathematical conclusion, the stage scripts
  are byte-regenerated, and the `Ledger` already closes the directory — but
  either the check or the prose should be tightened.  (The divisibility is
  presumably there to tolerate an internally periodic unit; `count ==
  header_stage_count * m` where `unit_true = unit^m` can be pinned exactly by
  comparing against `identical_copies` of a single regenerated write.)
  Related: in the `EXACT_EMPTY_NODE` branch the census is vacuous
  (`max(header_stages,1) == 1`).
- **`O-N2` Stage-runner log contents are unbound.**  `runner_files()` requires
  `<label>.runner.stdout.txt` and `<label>.runner.stderr.txt` to exist and
  archives them, but their bytes are hashed into nothing and inspected by
  nobody.  I replaced a runner stdout with `FATAL_ANYTHING\nrc=99\n` and the
  classifier still returned DEAD.  Cheap fix: require the runner stdout to be
  exactly the three `SINGULAR_STAGE_*` lines consistent with the result
  record, and the runner stderr to be empty.
- **`O-N3` The systemd read-back verifies three of five recorded properties.**
  `record["verified"]` (and the identical predicate in `derive_late_decision`)
  requires `killmode == "control-group"`, `runtime_max_usec` truthy and
  `!= "infinity"`, and `memory_swap_max == "0"`.  `memory_max` and `tasks_max`
  are recorded but never checked, and `runtime_max_usec` is not required to
  equal 21600 s.  The R2 report's "the supervisor reads the live scope's
  properties back … and latches `systemd_runtime_fault` if any is missing,
  `infinity`, or wrong" overstates this.  Exposure is small (the probe would
  have failed if the host rejected the properties, and both omitted values are
  resource caps, not promotion-safety gates), but the read-back should assert
  the exact `RuntimeMaxUSec` and the two caps.
- **`O-N4` Custody fault latches live outside the reviewed archive.**
  `FINALIZATION_LATCHES.txt`, `terminal_decision.stdout.txt` and
  `TERMINAL.marker` are written after `manifest-build`/freeze and are not in
  `manifest_includes`.  The archived `custody/` does contain the scope,
  containment and census markers and `systemd_runtime_limits.json`, but the
  sticky shell-variable faults (`worker_rc`, `swap_violation`,
  `whole_timeout`, `containment_preflight_failure`, `launcher_reap_failure`,
  `systemd_final_fault`, `systemd_runtime_fault`) are not recoverable from the
  archive.  A fault can only downgrade, so this is an audit-transparency gap
  rather than a promotion hazard — but a later reviewer of the archive alone
  cannot confirm which gates were clean.
- **`O-N5` The launch manifest is self-referential unless charged separately.**
  The launcher checks that *its own* hash appears in whatever file
  `$LAUNCH_MANIFEST` names; the lease then records that file's hash.  Nothing
  inside the archive pins it.  The real anchor is the launcher's own literal
  `expected_archive_sha=183ab5e0…`, so charging the launcher hash alone is
  sufficient — but the coordinator should also charge
  `LAUNCH_MANIFEST.sha256 = ba697115001232b95d58fb54e3102e1a7df28fad5e37849a68757af5b021dc34`
  (computed above; the R2 report charges only the launcher).
- **`O-N6` Identity-record key set is not closed.**  The result record is
  key-censused exactly (19 keys) in both driver and classifier; the identity
  record is only field-checked.  In practice an injected key is caught
  transitively (my M5 fixture refused via
  `DRIVER_STAGE_RECORD_DISAGREEMENT`), so this only matters against a
  compromised runner *and* a consistently rewritten driver summary.  A key
  census would close it for free.
- **`O-N7` `identical_copies` is Θ(len(data)) Python-level iterations.**  It
  loops `count` from `len(data)` down to 1, skipping non-divisors by integer
  modulo.  Correct, but a multi-megabyte node standard basis costs seconds of
  pure-Python looping inside the whole-job budget; iterating over divisors
  would be O(√n).  Failure mode is a whole-job timeout, i.e. conservative.
- **`O-N8` Small prose slips in the R2 report.**  (i) §5's description of the
  22 manifest entries as "the 18 in-case files (everything above except
  `SOURCE_ARCHIVE.sha256`, `PREFLIGHT_REPORT.md`, `LAUNCH_MANIFEST.sha256`,
  and the archive itself)" also silently excludes `aws_launch_preflight.sh`
  and `SOURCE_MANIFEST.sha256`; the arithmetic only works with all five
  exclusions.  (ii) "23 file-only members, mode 0444" is true of the archive
  file, not of its members (three distinct member modes).  (iii) §4/§6 call
  the `decide_terminal` mutation table "18-way"; the function has **19** gate
  parameters (`swap_zero` and `swap_violation` share one named mutation) — I
  covered all 19 and all 171 pairs.  (iv) `mode_ok`, `runtime_ok`, `lease_ok`
  and `decision_ok` are assigned together from one `try` block in the
  `terminal` CLI, so at the live level those four `decide_terminal` gates
  collapse to a single condition; the underlying checks are still performed
  inside `derive_late_decision`.  (v) `require_job_tag` enforces
  prefix + `_<nonce>` but not the `YYYYMMDDTHHMMSSZ` stamp shape, which lives
  only in the launcher — a direct supervisor entry could use a malformed
  stamp.  None of these change a verdict.

## 8. Mandatory rehearsal items

The seven-point plan in `AWS_PREREGISTRATION.md` already covers Sol 5.6's
minimum list plus the PGID-refusal and marker-collision cases, and I endorse
it unchanged.  Add these four:

1. **`O-B1` regression.**  On the disposable instance, after
   `archive-extract-verify` and before `terminal`, inject the §5 forgery into
   `$JOB_ROOT/.terminal_archive_replay.*` and confirm — *after the repair* —
   that the terminal refuses and publishes only a custody no-verdict.  Until
   the repair lands, record the unrepaired behavior explicitly.
2. **Exact systemd read-back.**  Capture `systemctl --user show` for the real
   worker scope and confirm `RuntimeMaxUSec` equals 21600 s (not merely
   non-`infinity`), `MemoryMax=274877906944`, `TasksMax=512`,
   `MemorySwapMax=0`, `KillMode=control-group`, and that
   `custody/systemd_runtime_limits.json` records them all.
3. **Watchdog degradation.**  `supervisor_death_watchdog` `exit 0`s after a
   single `systemctl --user kill … || true`.  Rehearse supervisor `SIGKILL`
   with a healthy user manager *and* with the user manager made unavailable,
   and confirm the scope's own `RuntimeMaxSec` still bounds the tree in the
   second case (or add a PGID-kill fallback inside the watchdog).
4. **Runner-log discipline (`O-N2`).**  Capture real `*.runner.stdout.txt`
   for a successful stage and a timed-out stage and record their exact shape,
   so the classifier can be tightened to require it.

Also worth capturing during the rehearsal, since they are cheap once a host
exists: the byte-identity of the witness replay's produced
`NODE_001_STANDARD_BASIS.txt` against the 4,961-byte archived unit (this is
the single live assumption the whole §3 repair rests on), and the archived
`NODE_001_REDUCE_PIVOTS.tsv` / `NODE_001_REDUCE_RESIDUAL.tsv` byte
comparisons.

## 9. Maximum possible claim after any future positive terminal

Unchanged from Sol 5.6, and I re-verified the allowlist is still exactly four
strings in `MATH_TERMINALS`, `ALLOWED` and the worker's `case` statement, with
no radical, geometric, whole-component or JC2 widening anywhere.

- `EXACT_ENDPOINT_DEAD_…_FINITE_COVER` would mean, at most: **exact endpoint
  death on the finite chart cover of only** `V(I_node1 + (Delta_node1))` in
  `Spec Q[q0,q2,c4,c6]`, `dp` order.
- `RING_LEVEL_ENDPOINT_SURVIVOR_…_PENDING_NILPOTENCE_RADICAL` would mean, at
  most: a nonzero endpoint coefficient in the certified saturated quotient on
  **one** closed-successor chart, pending nilpotence, radical and geometric
  analysis.
- The two bounded strings (`NO_VERDICT_OPEN_REMAINDER_…`,
  `REVERSE_CONTAINMENT_SEARCH_EXHAUSTED_…`) carry **no** mathematical
  conclusion; they are verified bounded outcomes only.

None of the four can spell a whole-TRIPLE02, ambient-endpoint,
geometric-existence, radical or JC2 statement, and the settled node-1 proper
open (`EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY`) is never combined with
them: it is routing provenance, its two products are never extracted, and the
`Delta_node1` hash guard is enforced in the builder, the driver and the
classifier.

**With `O-B1` unrepaired**, a promoted marker is not authenticated by the
archive it names, so the maximum defensible reading of any terminal produced
before that repair remains *"candidate evidence for the TRIPLE02 node-1
closed-successor recursion"*, with no authenticated promoted mathematical
verdict.  With `O-B1` repaired and the rehearsal discharged, the archive would
authenticate the marker and the two bullets above become available at their
stated, chart-local strength — and only then, after a separate coordinator
`GO`.

## 10. Source semantics vs. rehearsal debt

Established by this review, at source level and by execution on macOS in pure
Python: all hashes and seals; the archive censuses and manifests; the
byte-identity of the mathematical recursion; the rank bound 6; the
appended-copy law and its derivation; the stage write sets; the schema
agreement; the classifier's regeneration, artifact closure and no-verdict
re-derivation; every `decide_terminal` gate; the decision-record and
late-authority equalities; the lease, nonce, no-replace and
directory-exactness behavior; and the six source-text gates.

Not established, and not claimed by the producer either: **anything that
requires Linux, `/proc`, systemd, or Singular.**  No Singular has run in this
campaign — the witness replay, both Singular control scripts and every node
stage execute for the first time on AWS.  The launcher, supervisor, stage
runner, systemd scope, supervisor-death watchdog, PGID cleanup, cgroup
censuses and live `/proc` identity gates have never executed anywhere.  Every
custody fixture in the packet, and every fixture of mine, is pure or
parser-level.  That separation is stated correctly and repeatedly in the R2
report §7.2, `PREFLIGHT_REPORT.md`, both preregistrations and both selfchecks,
and I found no fixture overclaiming live coverage.

Report-body SHA-256 (all preceding bytes, including the newline immediately before this line): c4f90652eb665dad8b396150704340a12a9bef746e67d17cc5fe83ecab5b451d
