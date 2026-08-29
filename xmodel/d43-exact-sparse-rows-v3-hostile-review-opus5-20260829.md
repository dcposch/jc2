# Hostile review: D43 exact a00pp sparse rows v3 — independent repair adjudication

Date: 2026-08-29
Reviewer: Opus 5 (independent source/custody referee lane; producer was Fable 5)
Packet: `cases/d43_exact_sparse_rows_v3_20260828/`
Charge: `xmodel/d43-exact-sparse-rows-v3-repair-fable5-20260828.md` +
`cases/d43_exact_sparse_rows_v3_20260828/REVIEW_REQUEST_V3.md`

## Overall verdict

**REPAIR_REQUIRED**

Mathematical source fidelity is confirmed within the review boundary.  Custody
is not: the single authoritative `TERMINAL.json` copies its payload-binding
fields from the producer's candidate instead of recomputing or re-binding them,
and I reproduced a fabricated candidate that reaches the positive terminal
`EXACT_A00PP_184_RAW_J_ROWS_EMITTED_NO_SOLVE` with `failed_gates == []`.  This
is one blocking defect (Finding 1) plus two non-blocking confirmed defects
(Findings 2, 4) and one refuted allegation with an adjacent confirmed defect
(Finding 3).  Three of the four repairs are one-to-five lines each.

Nothing in this review promotes any D43 mathematical claim.  No v3 jet, row,
inventory, point, or verdict exists.  No AWS launch is authorized.

## Boundary and disclosure

I worked inside the v3 packet, the three charged reports, and this output.  Per
the hard boundary I did not access `jc2-lean`, any sibling project, or any
unrelated path; I ran no repository-wide status/inventory/search/build command
and no Singular, msolve, Sage, or other heavy CAS; no AWS, no web.

**Execution gaps I am disclosing rather than papering over:**

* The **v2→v3 byte-diff of the shared mathematical functions** — a hostile
  target in `REVIEW_REQUEST_V3.md` — was **not performed**.  Reading
  `cases/d43_exact_sparse_rows_v2_20260828/selected_rows_v2.py` is outside my
  stated work boundary.  What I did instead: verified the v2 seal's hash as
  part of the seal replay, and independently exercised the v3 mathematical
  surface through its own 19-fixture suite plus direct source reading of the
  gate and inventory functions.  The producer's byte-identity intention is
  therefore **UNADJUDICATED**, not confirmed.  A successor with v2 access
  should close it; it is cheap.
* This is a macOS host.  Live `/proc`, cgroup v2, systemd scopes, `setsid`,
  and IMDSv2 were exercised only through the production code's injectable
  `proc_root`/`--cgroup-dir` parameters with hand-built fixtures in the exact
  Linux `stat`/`status`/`environ` layout, plus source reading.  I built my own
  fixtures rather than reuse the producer's.  Findings 3 and 4 are therefore
  source-plus-fixture conclusions about Linux behavior, not live-Linux
  observations.  The producer disclosed this same gap; I confirm it is real and
  unclosed.

## 1. Frozen charge: seal replay

All five charged digests replay exactly.

```
$ shasum -a 256 <the five charged paths>
5423bd88328c338c54072b056d3f64251dc57de6f5112646f9d157f991ab5271  cases/.../SOURCE_V3.sha256
6497a9dd5c239703e49d0cc110f4e62d5e4ef4bd6d95ffd8fba94977d0b591ed  cases/.../d43_v3_source.tar.gz
0355a664cc22d4ed7127a84b69c5723f19e90fb03c1d5a11705bf488004d51cf  cases/.../REVIEW_REQUEST_V3.md
5759cfe81e21e7e4d3967b96152eaed5e789ed0498b039804b17c30853616b75  xmodel/d43-...-v3-repair-fable5-20260828.md
4f6f6c90e0526ab07591e2ec6a97f475e477b534cb6991085764cd693a99020d  xmodel/d43-...-v2-hostile-review-gpt56-20260828.md
```

Full seal: `shasum -a 256 -c SOURCE_V3.sha256` → **34/34 OK**, covering every
packet file, the sealed archive, both prior packet seals, all frozen
dependencies, and the controlling reviews.  Re-run after all of my testing:
**0 non-OK lines**; `__pycache__/` unchanged (two producer-era `.pyc` files).
The packet was not modified.

## 2. Mathematical source fidelity — CONFIRMED (within boundary)

| Check | Method | Outcome |
|---|---|---|
| Literal D21 band-20 gate (charged root 1) | read `selected_rows_v3.py:1054-1101` | **CONFIRMED.**  `rows != expected` decides (`:1076`); the three mutations are first proved literally distinct from the reference (`:1071-1075`), then the candidate is proved literally different from each (`:1079-1082`).  Digests are computed *after* the decision and only assert receipt separation (`:1083-1092`).  `digests_are_receipts_only: True`. |
| Zero production asserts (root 2) | my own AST census | **CONFIRMED.**  `ast.Assert` node count = 0 in all three of `selected_rows_v3.py`, `aws_preflight_v3.py`, `job_contract_v3.py`. |
| `python -O` refusal (root 2) | direct import under `python3 -O` | **CONFIRMED.**  All three raise `OPTIMIZED_PYTHON_REFUSED_FAIL_CLOSED` at import, which is what covers the frozen v1/COMMON dependency asserts. |
| Deterministic archive (root 7) | out-of-tree rebuild | **CONFIRMED.**  18 declared members + census; two builds byte-identical; digest = `6497a9dd…0b591ed`, matching the seal; regenerated census byte-identical to `SOURCE_ARCHIVE_MANIFEST_V3.sha256`; fresh-extraction replay 18/18; every member byte-identical to the live tree. |
| No archive self-reference | scanned every member for the outer digest | **CONFIRMED.**  Zero members contain `6497a9dd…`.  It is pinned only in `aws_launch_v3.sh:17`, the packet seal, and (future) registration. |
| Bounded hostile suites (root 8) | `python3 -B -m unittest` | **CONFIRMED.**  `test_job_contract_v3` **30/30 PASS** (7.9 s); `test_selected_rows_v3` **19/19 PASS** (29.9 s).  Matches the producer's claim exactly. |
| Single late terminal authority (root 6) | writer census | **CONFIRMED.**  Exactly three `TERMINAL.json` writers, all existence-guarded: `aws_launch_v3.sh:60-65`, `run_conditional_pipeline_aws_v3.sh:123-127`, and the sole positive-capable site `:623-624`.  The first two emit only `NO_VERDICT_*`.  `CURRENT_STAGE` takes only `RUNNING_*` values (8 distinct, all `RUNNING_`-prefixed). |
| Launch de-authorization | manifest read | **CONFIRMED.**  `PIPELINE_MANIFEST_V3.json` `status = V3_REPAIRED_LAUNCH_NOT_AUTHORIZED`; `aws.registration_status = UNREGISTERED_REVIEW_PACKET_DO_NOT_LAUNCH`; all `expected_*` fields empty; `authorization.solve = false`. |

**One substantive mathematical scoping observation** (not a defect, but it
bounds the promotion): `validate_exact_inventory` (`selected_rows_v3.py:1259-1276`)
does not *measure* the inventory — it **enforces** the preregistration.  It
raises `CustodyError` unless `len(live)==29`, `len(zero)==155`,
`bands == {20:10, 30:9, 40:10}`, and `max_tail_degree <= 2`.  Consequently a
positive terminal can only ever report the forecast values; a run whose true
inventory differs cannot publish that fact, it can only fail closed.  This is
correct fail-closed design, but it means the successful-run claim is
"the emission reproduced the preregistered inventory", not "the emission
measured the inventory."  Section 8 reflects this.

## 3. Finding 1 (BLOCKING) — the terminal copies what it should recompute

**Observation 1: CONFIRMED, exactly as alleged, on all three sub-claims.**

`decide_terminal` (`job_contract_v3.py:832-917`) is the single authority.  It
consumes the producer's candidate through `load_candidate` (`:808-830`), which
checks only: schema, status, `terminal_authority is False`, `run_nonce` equal to
the verified lease's nonce, and that seven named fields are 64-char lowercase
hex.  It performs **no value binding at all**.

What is independently recomputed vs. merely copied:

| Candidate field | Terminal treatment |
|---|---|
| `run_nonce` | **Recomputed/bound** — compared to the lease, which is itself re-verified with a fresh-descriptor held-lock probe (`verify_lease`, `:143-181`). This is the one real binding. |
| `lease_sha256` | **Shape-checked only.**  `decide_terminal` computes the true value at `:892` for its own output and never compares it to the candidate's. |
| `manifest_sha256`, `preflight_receipt_sha256`, `pilot_gate_sha256`, `merge_receipt_sha256`, `merge_payload_sha256`, `semantic_sha256` | **Shape-checked only**, then copied verbatim into `candidate_binding` (`:899-905`).  No referenced file is stat'ed or re-hashed. |
| `exact_inventory` | **Not examined at all** — not even for type.  Copied verbatim into the authoritative record. |
| `template_bridge_sha256`, `claim_boundary` | Not examined; not copied. |
| `terminal_archive_sha256` | Copied from `parse_sidecar_sha256` (`:797-806`), which regex-matches one `<sha>  <name>` line and **never locates, stats, or re-hashes the named archive**. |

**Negative control (bounded, inert temp dir, cleaned up).**  Real held `flock`
lease, all 22 boolean/rc gates clean, empty censuses, and a candidate carrying a
deliberately wrong lease digest, impossible inventory, and a sidecar naming a
file that does not exist:

```text
archive file exists on disk: False
FINAL_CLASSIFICATION=EXACT_A00PP_184_RAW_J_ROWS_EMITTED_NO_SOLVE
decide_terminal rc  = 0
positive            = True
failed_gates        = []
real lease sha      = bfebac330f91b3f0c95a6f594de9fa4bf75d8c6d0e6493382c86d5474e968a43
candidate lease sha = deaddead…dead            <- accepted
terminal lease sha  = bfebac33…8a43            <- same object, contradicts the candidate
candidate_binding   = {"exact_inventory": {"exact_zero_rows": 9999,
                       "live_rows": -7, "total_rows": "one hundred eighty four"}, …}
terminal_archive_sha= deaddead…dead            <- names a nonexistent file
```

The authoritative record contains a lease digest that contradicts its own
neighbouring field, an inventory asserting −7 live rows and 9999 exact-zero
rows out of 184, and an archive digest for a file that was never on disk.

**Scope precision on the third sub-claim.**  An *absent sidecar file* does fail
`archive_outer_sha_present` (`:877`) — the packet's own
`test_missing_sidecar_and_lease_failure` covers that, and I reproduced it.  The
real hole is one level in: the sidecar's *named archive* is never bound.

**Why the existing tests did not catch this.**  The suite's happy-path fixture
(`test_job_contract_v3.py:602-620`) *is itself* a candidate with fabricated
payload digests `"11"*32 … "66"*32`, and `:625-626` writes a sidecar naming
`job-tag-9.terminal.tar.gz`, which is never created.
`test_positive_terminal_only_with_every_gate_clean` (`:665-675`) then asserts
the positive terminal and asserts `terminal_archive_sha256 == "77"*32`.  The
suite **enshrines the copy-through as correct**.  The six "candidate forgeries"
(`:725-744`) are all shape/identity forgeries — schema, status, authority,
nonce, missing key, malformed hex.  **Not one is a value forgery.**

**Severity.**  On an honest run the producer's `finalize_candidate`
(`selected_rows_v3.py:1450-1531`) does re-verify the whole chain, and
`candidate_rc_zero` proves it exited 0.  But the v3 architecture's stated point
(charged root 6) is that the *contract module* holds sole terminal authority.
As built, every payload-binding field in the authoritative record is
**producer-asserted, not contract-computed**, and the terminal cannot detect a
`FINALIZE_CANDIDATE.json` that changed after the producer exited 0 — a window
that spans the entire final-custody and archive-build phase
(`run_conditional_pipeline_aws_v3.sh:415-428` through `:592`).  Composed with
Finding 4, that window is writable by anything still alive in the job.  This is
the same asserted-vs-computed class the v2 review charged under root D
("verify all payloads … final inventory, and archive before publishing it")
and root E ("bind its digest into the single terminal object").  Root D/E are
**partially** repaired: the verification moved to the right place in *time*, but
not to the authority.

**Minimum repair.**  Three checks in `load_candidate`/`decide_terminal`:

1. `require(candidate["lease_sha256"] == sha256_path(Path(args.lease)))` —
   one line; the value is already computed at `:892`.
2. Type- and contract-check `exact_inventory`: `live_rows` and
   `exact_zero_rows` must be non-bool `int`, equal to 29 and 155, summing to 184.
3. In `parse_sidecar_sha256`, resolve the named member relative to the sidecar's
   directory through `safe_relative`, require it be a regular file, and require
   `sha256_path(...) == digest`.

I prototyped exactly these three out-of-tree.  Outcome: forged candidate →
`CANDIDATE_LEASE_DIGEST_MISMATCH`; the packet's own honest fixture shape →
`OK` (so the repair does not break the existing 30 fixtures); honest candidate
with a dangling sidecar → `SIDECAR_ARCHIVE_ABSENT_OR_DRIFTED`.

**Regression test.**  Add a `test_value_forged_candidates_are_refused` mirroring
`:725-744` but mutating *values*: wrong `lease_sha256`; `exact_inventory` with
`live_rows: -7` / `exact_zero_rows: 9999`; `exact_inventory` a string; and a
sidecar whose named archive is absent and one whose named archive exists but
hashes differently.  Each must yield rc 3 and a `NO_VERDICT_*` status.

## 4. Finding 2 (non-blocking) — member-set equality is regular-files-only

**Observation 2: CONFIRMED, narrowed.**  Exact set equality is enforced, but
only over *regular file* members:
`require(regular == set(manifest_entries) | {manifest_name})`
(`job_contract_v3.py:773`).  Directory members land in `names` but never in
`regular` (`:750-758`), are materialized during extraction (`:777-779`), and are
then invisible to the replay because `manifest_files` skips directories
(`:641`).

Bounded control against the real `extract_and_verify_archive`:

```text
extra unmanifested DIRECTORY : ACCEPTED (entries=2)
extra nested DIRECTORY chain : ACCEPTED (entries=2)
extra unmanifested FILE      : REFUSED: ARCHIVE_REGULAR_MEMBER_CENSUS_DRIFT
extra SYMLINK                : REFUSED: ARCHIVE_NONREGULAR_MEMBER:jc2/link.txt
traversal member             : REFUSED: UNSAFE_RELATIVE_PATH:../escape.txt
member outside includes      : REFUSED: ARCHIVE_UNSAFE_DUPLICATE_OR_EXTRA:outside/x.txt
```

So the answer to "is exact member-set equality enforced at every
authority-bearing archive gate" is **no, not over the full member set** — but
the accepted content carries zero bytes.  Any file inside such a directory is
itself a regular member and is caught.  Files, symlinks, hardlinks, traversal,
duplicates, and out-of-include members are all refused.

Additionally, the **source**-archive gate is not exposed at all: the launcher
pins and compares the outer digest *first* (`aws_launch_v3.sh:132-136`,
`EXPECTED_SOURCE_ARCHIVE_SHA256` at `:17`), so no member-set manipulation
survives.  Only the run-time terminal archive — which by construction has no
pinnable expected digest — relies on the census alone, and its builder
(`build_deterministic_archive`, `:696-733`) never emits directory members.  I
classify this as a true member-set inequality that is **not currently
load-bearing**.

One ordering remark for defense in depth: at `aws_launch_v3.sh:150-158` the
launcher runs `tar -xzf` into `$job_root/source` *before* the contract's
`archive-extract-verify`, guarded only by a name-regex listing check that cannot
see member *types*.  The outer-SHA pin covers this today; if that pin is ever
relaxed, the ordering becomes exploitable.

**Minimum repair.**  Extend the census to the full member set — e.g. require
`names - regular` to be exactly the set of directory prefixes implied by
`manifest_entries` — or simply refuse directory members outright, since the
builder never produces them (`require(not member.isdir(), …)`).  The latter is
one line and strictly stronger.
**Regression test.**  Extend `test_unsafe_members_refused` with an extra
top-level directory member and a nested directory chain, both expecting refusal.

## 5. Finding 3 — reparenting is closed; two gates are not real

**Observation 3: REFUTED as literally stated.  Two adjacent defects CONFIRMED.**

The terminal requires both `pgid_census_empty` and `tag_census_empty`
(`job_contract_v3.py:866-867`), fed by `terminate_and_census` (`:369-390`),
which censuses by process group **and** by `JOB_TAG` in
`/proc/<pid>/environ` (`has_job_tag`, `:239-246`).  Fixture run of the real
`process_records` against a hand-built Linux-layout `/proc`:

```text
pgid=1000 (setsid_pgid mode)  pgid_census=[1001, 1002]  tag_census=[1001, 1002, 1003]
pgid=0    (systemd mode)      pgid_census=[]            tag_census=[1001, 1002, 1003]
descendants_deepest_first(supervisor) = [1001, 1000]
```

where 1002 is reparented to init but kept its pgid, 1003 called `setsid`, and
1004 both `setsid`'d and re-exec'd with `JOB_TAG` scrubbed.

* A child **reparented away** keeps its process group — reparenting changes
  `ppid`, not `pgid` — so 1002 is caught by the PGID census.
* A child that **leaves the process group** is caught by the `JOB_TAG` census,
  because `/proc/<pid>/environ` reads the original stack env region and is
  unaffected by `unsetenv`.
* So the stated scenario **cannot** pair a clean census with a live child.  The
  alleged hole is refuted.
* `descendants_deepest_first` (`:312-339`) does miss every reparented process,
  and so therefore does `kill_tree` (`:341-367`) — but `kill_tree` is used only
  for stage/peer cancellation (`run_conditional_pipeline_aws_v3.sh:99-118`);
  the *terminal* inputs come from `terminate_and_census`, which is pgid ∪ tag.
  The prior process appears to have generalized from the `kill_tree` ppid walk
  to the terminal gate.  It does not transfer.

Only 1004 — `setsid` **plus** an exec with a scrubbed environment — escapes both
censuses.  No process this job launches does that, and in systemd mode the
cgroup census still catches it.

**Confirmed adjacent defect 3a — one orphan gate is vacuous in every mode.**
`run_conditional_pipeline_aws_v3.sh:501-502` (and identically `:111-112`) set
`cleanup_pgid=0` unless the mode is `setsid_pgid`.  `process_records` guards
with `if pgid > 1 and …` (`job_contract_v3.py:263`).  Therefore:

* in **systemd_scope** (the primary AWS mode) `pgid_census_empty` is
  **structurally true and never evaluated**;
* in the **setsid_pgid** fallback, `cgroup_final_gate=$cleanup_gate`
  (`:519-521`) is a literal copy of another gate, disclosed in a code comment
  but not in the record.

Safety is preserved in both modes — systemd relies on the kernel cgroup census,
which is strictly stronger than a PGID census, and the fallback relies on the
real pgid ∪ tag census.  The defect is **reporting fidelity**: a positive
`TERMINAL.json` lists two independent-looking orphan gates of which one is
always a vacuous pass, and the record does not say which.  This is the same
vacuous-pass class this program has repeatedly treated as a finding.

**Minimum repair.**  Pass the real supervisor pgid in both modes (`cleanup_pgid=$$`
unconditionally — the supervisor is the process-group leader in both), and record
`cgroup_final_gate` as `NOT_APPLICABLE` rather than a copy in the fallback, with
a `gate_provenance` map in `TERMINAL.json` naming each gate's evidence source.
**Regression test.**  A terminal fixture asserting that no gate reported `true`
was computed with a vacuity-inducing parameter — concretely, assert
`pgid > 1` for any run whose terminal claims `pgid_census_empty`.

## 6. Finding 4 (non-blocking, contradicts a producer disclosure)

The producer's residual limitation #3 states that the supervisor-in-boundary
self-census gap is closed because "the launcher post-mortem census closes that
gap after exit."  **It does not.**

`postmortem()` (`aws_launch_v3.sh:79-98`) runs a genuine independent orphan
census after `kill_boundary`, captures `postmortem_rc` at `:87`, and — per
`grep postmortem_rc` — uses it at exactly one other place, `:95`, where it is
printed into `LAUNCHER_POSTMORTEM.json`.  **Nothing gates on it.**  At `:266-272`
the launcher publishes a `NO_VERDICT` only `if [[ ! -e "$terminal" ]]`; if the
supervisor already renamed a *positive* terminal, a post-mortem that found live
`JOB_TAG` survivors changes nothing.

Worse, `LAUNCHER_POSTMORTEM.json` is written after the supervisor exits, whereas
the terminal archive and `TERMINAL_MANIFEST.sha256` are built *before* the
terminal rename (`run_conditional_pipeline_aws_v3.sh:524-560`).  The final
orphan evidence therefore lands **outside** the sealed archive and outside the
manifest that the archive gates replay.

So a positive terminal **can** coexist with a launcher post-mortem recording
survivors.  Reaching that state requires a process that survived
`terminate_and_census`'s TERM→KILL and escaped the cgroup census, so it is not
easily reachable — but the mechanism the producer cites as the closer is
genuinely absent.

**Minimum repair.**  Either (a) have the launcher, when the terminal is positive
*and* `postmortem_rc != 0`, publish a sibling `TERMINAL_POSTMORTEM_FAULT.json`
and exit non-zero with a loud banner (it must not overwrite the terminal), or
(b) move the census before the supervisor's terminal decision by having the
supervisor exec a small post-boundary reaper.  (a) is the smaller change.
**Regression test.**  A shell-level fixture where the post-mortem census file is
non-empty and the terminal is positive, asserting the launcher exits non-zero
and emits the fault object.

## 7. Minimum repair set

| # | Site | Change | Blocking? |
|---|---|---|---|
| R1 | `job_contract_v3.py` `load_candidate`/`decide_terminal` (`:808-830`, `:877`) | Bind `lease_sha256` to the recomputed value; contract-check `exact_inventory` (int, 29/155/184); resolve + re-hash the archive named by the sidecar | **Yes** |
| R2 | `test_job_contract_v3.py` | Add value-forgery fixtures (wrong lease digest, impossible inventory, dangling/drifted sidecar) | **Yes** (R1 is untested without it) |
| R3 | `job_contract_v3.py:750-758` | Refuse directory members outright, or extend the census to the full member set | No |
| R4 | `run_conditional_pipeline_aws_v3.sh:111-112, 501-502, 519-521` | Real pgid in both modes; `NOT_APPLICABLE` instead of a copied gate; add `gate_provenance` to `TERMINAL.json` | No |
| R5 | `aws_launch_v3.sh:266-272` | Gate on `postmortem_rc`; emit a fault object when a positive terminal coexists with a non-empty post-mortem census | No |

R1+R2 must land before any AWS rehearsal.  R3–R5 should land in the same
revision — they are small — but none of them alone would block.

A successor with v2 access must additionally close the **unadjudicated v2→v3
byte-diff** of the shared mathematical functions before the packet is treated as
mathematically re-confirmed rather than mathematically re-tested.

## 8. Maximum possible claim after a future successful reviewed AWS terminal

After R1–R2 land, a fresh independent hostile PASS of the repaired seal, the
coordinator's separate GO, a fresh immutable host registration, and one
successful run publishing a single positive `TERMINAL.json`, the maximum
supportable claim is:

> On one registered host, under a held one-shot lease and a single containment
> boundary, two independently constructed sides agreed on the collapsed D21
> band-20 object by literal structural equality, and one process then emitted
> all 19 shards and the 184-row raw-J merge for the exact a00pp
> support-specialized truncation, **reproducing the preregistered 29 live /
> 155 exact-zero inventory with live bands {20:10, 30:9, 40:10} and tail degree
> ≤ 2**, with `solve = false`.

Three explicit narrowings:

1. Because `validate_exact_inventory` (`selected_rows_v3.py:1267-1272`)
   *enforces* rather than measures, the run **confirms the preregistration**;
   it does not independently determine the inventory.  A differing true
   inventory can only produce a `NO_VERDICT`.
2. Until R4 lands, the positive record's orphan evidence is one real census
   plus one vacuous gate; the claim should not cite "empty PGID and cgroup
   censuses" as two facts.
3. Until R5 lands, the claim carries no post-boundary orphan assurance.

It remains **not**: exact a00pp raw-J point existence, full residue-A template
point existence, banked NF presentation equivalence, the displayed E5/E6
unit extension, all-depth compatibility, a Keller map, or a JC2 counterexample
— matching `PIPELINE_MANIFEST_V3.json`'s `claim_boundary`, every entry of which
is `null` except the E5/E6 note.

## 9. Commands run

```text
shasum -a 256 <5 charged paths>                                  → all 5 match
shasum -a 256 -c cases/.../SOURCE_V3.sha256                      → 34/34 OK (twice: before and after testing)
python3 -B -m unittest test_job_contract_v3   -v                 → Ran 30, OK (7.9 s)
python3 -B -m unittest test_selected_rows_v3  -v                 → Ran 19, OK (29.9 s)
python3 -O  <import each of the 3 production modules>            → 3/3 OPTIMIZED_PYTHON_REFUSED_FAIL_CLOSED
ast.Assert census over the 3 production modules                  → 0, 0, 0
out-of-tree archive rebuild (staging copy, packet untouched)     → 6497a9dd… twice; census + members byte-identical; 0 self-references
negative control 1: fabricated candidate → decide_terminal       → POSITIVE, rc 0, failed_gates []
negative control 2: 6 member classes → extract_and_verify_archive→ dirs ACCEPTED; file/symlink/traversal/outside REFUSED
negative control 3: 5-process /proc fixture → process_records    → reparent+setsid caught; pgid=0 census vacuous
repair prototype (out-of-tree)                                   → rejects forgery, accepts honest fixture, catches dangling sidecar
```

All temporary directories were inert, under `/tmp`, and removed
(`rm -rf /tmp/nc1_opus5`; confirmed absent).  No packet file was modified, no
canonical file edited, no commit, no push, no AWS action.

<!-- BODY-END -->

## Report-body self-hash

SHA-256 of this report's body, defined as every byte of this file up to and
including the line `<!-- BODY-END -->`:

```text
1b90552abddb14bf5946a2e85f0a5ac26dae05d3049ef578db507c766862bd82
```

Reproduce with:

```sh
python3 -c 'import hashlib,sys;b=open(sys.argv[1],"rb").read();m=b"<!-- BODY-END -->\n";print(hashlib.sha256(b[:b.index(m)+len(m)]).hexdigest())' \
  xmodel/d43-exact-sparse-rows-v3-hostile-review-opus5-20260829.md
```
