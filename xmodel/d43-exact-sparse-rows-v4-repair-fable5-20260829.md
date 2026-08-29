# Producer report: D43 exact sparse-row emitter v4 independent repair

Date: 2026-08-29
Producer: Fable 5 (repair commission; same producer lane as v3)
Packet: `cases/d43_exact_sparse_rows_v4_20260829/` (fresh immutable packet;
v1, v2, and v3 untouched and never resealed)
Status: **V4_REPAIRED_LAUNCH_NOT_AUTHORIZED**

## Verdict

**SOURCE_V4_READY_FOR_DIFFERENT_MODEL_REVIEW**

All five Opus 5 v3-review repairs (R1-R5) are implemented and
negative-control-tested through named gates, the v2->v3/v4
mathematical-function byte-diff that Opus 5 disclosed as UNADJUDICATED is
closed machine-checkably with zero drift beyond the reviewed changes, the
confirmed v3 mathematics is preserved byte-for-byte at the function level,
and the packet is sealed, deterministic, and de-authorized.  No D43 v4
jet, row, inventory, point, or verdict exists; no AWS launch is
authorized.

## Controlling inputs, verified before work began

| Input | SHA-256 | Verified |
|---|---|---|
| v3 packet `cases/d43_exact_sparse_rows_v3_20260828/` seal `SOURCE_V3.sha256` | `5423bd88328c338c54072b056d3f64251dc57de6f5112646f9d157f991ab5271` | file digest replayed |
| Opus 5 v3 hostile review `xmodel/d43-exact-sparse-rows-v3-hostile-review-opus5-20260829.md` | `6e01e5d7e7852d094559ab57cd7a256c41390fca99e38a6c55fbea8f12209bd9` | file digest + report-body seal `1b90552abddb14bf5946a2e85f0a5ac26dae05d3049ef578db507c766862bd82` replayed with the review's own recipe |
| v3 repair report `xmodel/d43-exact-sparse-rows-v3-repair-fable5-20260828.md` | `5759cfe81e21e7e4d3967b96152eaed5e789ed0498b039804b17c30853616b75` | file digest replayed |
| v2 seal `SOURCE_V2.sha256` / `selected_rows_v2.py` (diff-closure inputs only) | `83635fe45e6f3a9e19d3c93ef963de769f2721653a7bb5333002dd100172fa73` / `9fc9bd7a365827ddba2c1ba45cbb34870d6f2d71c9d3eecb6b242d46e00990b2` | seal digest replayed; producer line matches the seal |

Constraints honored: no repository-wide status/inventory/search/build
command; no `jc2-lean` access of any kind; no web, AWS, Singular, msolve,
Sage, or heavy CAS; bounded Python tests plus inert `/tmp` staging only;
no canonical ledger edited; no commit; no push.  Writes were confined to
`cases/d43_exact_sparse_rows_v4_20260829/` and this report.

## Mandatory repair set: implementation

**1. Value-binding terminal (Opus Finding 1, blocking).**
`job_contract_v4.py::load_candidate` now enforces the exact 15-key
candidate census (missing and extra keys refuse), and `bind_candidate` /
`decide_terminal` recompute or bind every payload-bearing field:

* `run_nonce`: recomputed from the lease under a fresh-descriptor
  held-flock probe (the one binding v3 already had);
* `lease_sha256`: rehash of `RUN_LEASE.json`;
* lease `registration_sha256`: rehash of `records/REGISTERED.json`;
* `manifest_sha256`: rehash + schema check of the on-disk manifest;
* `claim_boundary`: equality with the rehashed manifest's boundary plus a
  null-shape check (every key must be null except the pinned E5/E6 note,
  which must be a non-empty string - a claim can never silently promote);
* `preflight_receipt_sha256`, `pilot_gate_sha256`,
  `merge_receipt_sha256`, `merge_payload_sha256`: rehash of the exact
  named artifacts plus content contracts (pass/authority, pilot status +
  nonce, merge schema/status/nonce/lease/manifest/preflight/pilot/payload
  name);
* `semantic_sha256`, `template_bridge_sha256`, `exact_inventory`:
  cross-bound under the rehashed merge receipt (recorded as
  `RECEIPT_CROSSBOUND`, since the contract deliberately does not unpickle
  row payloads);
* `exact_inventory` additionally contract-checked: `live_rows` and
  `exact_zero_rows` non-bool integers with `29+155=184`, bands exactly
  `{"20": 10, "30": 9, "40": 10}` summing to 29, `max_tail_degree` a
  non-bool integer `<= 2`, and 155 distinct integer zero-target pairs.

The terminal records per-field `candidate_binding` provenance
(`RECOMPUTED_SHA256:...` vs `RECEIPT_CROSSBOUND:...` vs
`BOUND_TO_REHASHED_MANIFEST...`) and a `binding_failures` map; there is
no unexplained copied digest.  Twelve named binding gates join the gate
set.  Opus's fabricated candidate (wrong lease digest, -7/9999 inventory,
dangling sidecar) now fails `candidate_lease_digest_bound`,
`candidate_inventory_contract`, and `archive_sidecar_bound` instead of
reaching the positive terminal.

**2. Sidecar archive binding.**  `verify_sidecar_archive` resolves the
named member relative to the sidecar through `safe_relative`, requires
the exact name `<job_tag>.terminal.tar.gz`, requires a regular
non-symlink file, rehashes it, and requires digest equality before any
positive terminal; `terminal_archive_sha256` is that rehash (gate
`archive_sidecar_bound`, replacing v3's presence-only
`archive_outer_sha_present`).

**3. Full-member-set archive census.**  `extract_and_verify_archive`
refuses every non-regular member outright - directories included
(`ARCHIVE_NONREGULAR_MEMBER`) - and enforces exact full-member-set
equality against the embedded manifest (`ARCHIVE_MEMBER_CENSUS_DRIFT`),
at both authority-bearing replays (launcher source replay, supervisor
terminal-archive replay) and the builder's own replay.  The extra
directory and nested directory chain Opus showed ACCEPTED in v3 are now
refused by name.

**4. Real censuses, no copied gates.**  The launcher starts the
supervisor under `setsid --wait` in **both** containment modes (`setsid`
is a hard requirement before mode selection), making the supervisor the
session/process-group leader in both; the containment identity gate
verifies `sid == pgid == $$` in both modes; the final census pgid is `$$`
unconditionally - the v3 `cleanup_pgid=0` lane no longer exists.  The
terminal takes mandatory `--cleanup-pgid` and `--boundary-mode`, refuses
`pgid <= 1` (`pgid_census_real`), and refuses mode-inconsistent cgroup
values (`cgroup_gate_mode_consistent`).  In the setsid fallback the
cgroup gate is recorded as the string `NOT_APPLICABLE` with provenance
`NOT_APPLICABLE_NO_CGROUP_IN_SETSID_PGID_FALLBACK...` - never a copied
boolean - and positivity accepts only `true` or that mode-legal string.
A `gate_provenance` map in the terminal names each gate's evidence
source.  (Note: Opus's suggested `cleanup_pgid=$$ unconditionally` was
only safe to adopt because of the added systemd-mode `setsid` wrapper;
without it the supervisor inside a `systemd-run --scope` shares the
launcher's process group and a pgid census would sweep the launcher.
The identity gate makes the leadership assumption checked, not assumed.)

**5. Authority-bearing launcher post-mortem.**  New contract subcommand
`postmortem-gate`: a positive (or unreadable - fail closed) terminal
paired with a non-zero post-mortem census rc, a non-empty census, or a
missing/unreadable census file writes an immutable 0444
`TERMINAL_POSTMORTEM_FAULT.json` beside the terminal via `O_EXCL` (the
first fault object wins and is never overwritten), embedding the terminal
digest, both census contents and digests, and the rc; it returns 79 and
the launcher exits 78 with a loud banner.  The terminal is never
modified; its `post_boundary_contract` block names the fault object, its
location outside the sealed terminal archive, and the voiding rule, so
the terminal/archive contract links the evidence without overwriting the
original terminal.  The launcher post-mortem census now uses the real
session-leader pgid read from `custody/containment_identity.json`, and
the fallback `kill_boundary` kills that leader's group (the v3 `-$!`
group kill targeted the setsid wrapper's group, an adjacent launcher-only
fix disclosed here and charged to review).

**6. v2->v3/v4 mathematical byte-diff closure (Opus's UNADJUDICATED
item).**  `math_function_diff_v4.py` pins all three producer files by
whole-file SHA-256 (`9fc9bd7a...`, `3a29c849...`, `3b3519f8...`) and
proves, exiting non-zero on any drift:

* **v3->v4: zero function change.**  All 73 top-level
  functions/classes byte-identical; the only module-level assignment
  diffs are the two `.v3`->`.v4` schema strings; the module docstring
  and optimized-Python refusal message are the only other file diffs.
* **v2->v4: 39 shared functions byte-identical**, containing the entire
  collapsed-arithmetic and jet/row core (`cp_*`, `cv_add/scale/constant`,
  `cs_*`, `cj_*`, `collapse_vexpr`, `convert_a_orbit`,
  `collapsed_gm_jet2`, `collapsed_b_block`, `_selected_product`,
  `selected_source_rows`, `evaluate_*`, every canonicalization/semantic
  digest function).
* **The 25 differing shared functions decompose exactly** into the five
  reviewed repair classes: assert->require with unchanged predicates
  (checks only added, never removed), lease threading, the
  literal-D21-gate rewrite (v3 charged root 1, confirmed by Opus within
  its boundary), version-literal strings only (`cv_mul` is additionally
  machine-normalized and compared byte-exactly), and explicit v1-fact
  revalidation.  Removed: `finalize_run` + `atomic_text` (the v2
  early-positive publisher).  Added: the nine custody functions of the
  reviewed v3 repair set.  No numeric or algebraic expression changed
  anywhere.
* The sealed adjudication with full unified diffs,
  `V2_V4_MATH_FUNCTION_DIFF.md`, regenerates byte-identically
  (`--write-report` replay compared in-suite).

Two inert v3 literals inside mathematical functions are retained
byte-for-byte to keep the v3->v4 math diff empty, and disclosed:
`cv_mul`'s "exact v3 lane" message and `build_collapsed_side`'s
"D43-v3-" log tag.

**7. Preserved confirmed mathematics.**  Literal collapsed-D21
structural equality with digests as receipts only
(`digests_are_receipts_only: true`), HW-before-multiplication (HW1/HW2
collapsed into the 432-term radical quotient before jet multiplication),
independent f/g construction with pair custody, one 19-shard/184-row
emission after band-20 equality, `solve=false` everywhere, zero
production asserts (AST census in-suite), and optimized-Python
fail-closed import refusal in all production modules including the new
`terminal` and `postmortem-gate` subcommands - all carried unchanged and
re-tested.

## Required negative controls: census

All run through the production code paths and refuse through their named
gates; all old v3 fixture intents retained.

| Commissioned control | Fixture | Named gate / refusal |
|---|---|---|
| each wrong candidate digest value (8 fields) | `test_value_forged_candidate_digest_fields_are_refused` | `candidate_lease_digest_bound`, `candidate_manifest_digest_bound`, `candidate_preflight_digest_bound`, `candidate_pilot_gate_digest_bound`, `candidate_merge_receipt_digest_bound`, `candidate_merge_payload_digest_bound`, `candidate_semantic_crossbound`, `candidate_template_bridge_crossbound` |
| wrong lease digest | same | `candidate_lease_digest_bound` |
| impossible/string/bool inventory | `test_impossible_inventory_refused` + `test_shape_forged_candidates_are_refused` | `candidate_inventory_contract` (-7/9999, 30/154, bool counts, wrong bands, degree 3, bool degree, short/duplicate zero targets, key census) / `candidate_schema_valid` (string inventory) |
| dangling and drifted archive sidecar | `test_dangling_and_drifted_archive_sidecar_refused` | `archive_sidecar_bound` (dangling, drifted, foreign-name, traversal) |
| extra directory and nested directory chain | `test_directory_members_refused` | `ARCHIVE_NONREGULAR_MEMBER` |
| vacuous pgid input (0, 1, -1) | `test_vacuous_pgid_refused` | `pgid_census_real` |
| copied cgroup gate (both directions) | `test_copied_cgroup_gate_refused` + `test_fallback_mode_not_applicable_cgroup_is_recorded` | `cgroup_gate_mode_consistent`; fallback positive records the string `NOT_APPLICABLE`, never `true` |
| positive terminal + failing launcher post-mortem | `PostmortemGateTest` (3 fixtures) | rc 79 -> launcher exit 78; immutable 0444 fault object; terminal byte-unchanged; unreadable terminal fail-closed; fault never overwritten |
| candidate mutation after producer exit | `test_candidate_mutation_after_producer_exit_refused` | named binding gates with `candidate_rc = 0` held |
| semantic receipt changed retaining valid hex | `test_semantic_receipt_mutation_with_valid_hex_refused` | receipt-only variant: `candidate_merge_receipt_digest_bound`; coordinated variant (candidate receipt digest updated to match): `candidate_semantic_crossbound` |
| registration drift (added) | `test_registration_drift_refused` | `candidate_registration_digest_bound` |
| claim-boundary promotion/drop (added) | `test_claim_boundary_forgeries_refused` | `candidate_claim_boundary_bound` |

Ordinary vs optimized Python: the full suites run under ordinary
`python3 -B`; under `-O` every production module and both
authority-bearing subcommands refuse at import
(`OPTIMIZED_PYTHON_REFUSED_FAIL_CLOSED`, tested per subcommand), which is
the fail-closed behavior for every gate above, and the v2
forged-receipt fixture now pins its refusal reason per interpreter leg so
it can never pass vacuously.

## Tests, determinism, seal

* `test_job_contract_v4.py`: **45/45 PASS** (~8 s).
* `test_selected_rows_v4.py`: **21/21 PASS** (~14 s), including the
  diff-closure replay and the shell-lane repair-wiring census.
* `math_function_diff_v4.py`: `V2_V3_V4_MATH_DIFF_CLOSED`, report
  regeneration byte-identical.
* Source archive `d43_v4_source.tar.gz`: 20 members + census manifest,
  sorted USTAR, zeroed metadata, mode 0444, gzip mtime 0.  Built by
  three independent builder runs (each staging in a fresh private `/tmp`
  directory - out of tree - and building twice internally): identical
  outer digest every time, fresh-extraction replay 20/20, every member
  byte-identical to the live tree, **zero self-reference** (the outer
  digest appears in no member; it is pinned only in `aws_launch_v4.sh`,
  the packet seal, and future registration).  The archive gained the two
  new frozen inputs (the Opus 5 v3 review and the v3 repair report) as
  members, matching the 18-path operational list.
* Packet seal `SOURCE_V4.sha256`: 39 entries covering every packet file,
  the sealed archive, all three prior packet seals, the pinned v2/v3
  producers, all frozen dependencies, and the controlling reviews;
  replayed **39/39 OK** from the repository root, re-replayed clean
  after all testing and after the final builder run (which is itself the
  proof the rebuild reproduced the sealed bytes).
* `bash -n` on supervisor and launcher; `py_compile` on all Python; no
  `__pycache__` left in the packet.

## Exact files and hashes

Packet seal `cases/d43_exact_sparse_rows_v4_20260829/SOURCE_V4.sha256`,
own digest
`dd05d82fcc0f8cd71af173bdef7420811c188ac1111265ac842b0b5437fd81f1`:

```text
9051a3dbfc4d6d8714a6ee3ca53e84517bcadddfab4fc49baf480d65f0dd31ba  d43_v4_source.tar.gz (outer, pinned in aws_launch_v4.sh)
d26ef9847ab05b62c293e1706bdb271c8be87075b018c2fcb89f7608cc633d69  SOURCE_ARCHIVE_MANIFEST_V4.sha256
11208fc9b2b5d88612a30971d0432dc235d48555417888d7ae3de468b5474613  OPERATIONAL_SOURCE_V4.sha256
076aa949242b69fef78743793acf78a2b298f5f70ac7918272135e24db17a527  PIPELINE_MANIFEST_V4.json
3b3519f86df300ce46109b18546fe1c84edf68a0c0606849bca1c5d4e47971c5  selected_rows_v4.py
879e2dc3448776377048be251c89c6615630c855dba89535b481c213147f9c24  job_contract_v4.py
9f8d67ecec566fa674cbd8289d2339b6fc92d3bd4df50b98ee8baeb51fd5593a  aws_preflight_v4.py
33a137306f99a95f958cafdc6cec88e6f190ac3c4c795ed77a2044aecb5f7e0e  run_conditional_pipeline_aws_v4.sh
ac26aed0b7a4267701136029c924a014a8b38e798a1cd2df5e0250ca85f14749  aws_launch_v4.sh
73bf8aa993ea1a47ccc7c6ecea0b9636f861506925ae9b5e8c6d65657eea38b0  build_source_archive_v4.py
718342b82930d84f6c22055fd5878bb51ddf25d91ff45980c27ca3c5ca9f5345  math_function_diff_v4.py
fb5b220aa76b85ea457de0e67e8cb74e975b599aab3aa79e7c768ac1295b812f  V2_V4_MATH_FUNCTION_DIFF.md
e90aafafcdf5810b252dea98c4efef4068588170054da918e766c04a6d0fdbe2  test_job_contract_v4.py
79c7f9fe41cb30a72eee339ea39374278037efcff106615fb25b554b91738d5f  test_selected_rows_v4.py
6ec457dcab681dfc4b48a29a29eca01ff8c26e70a4c34300b14c84cf430fc15b  IMPLEMENTATION_REPORT_V4.md
cebe606bfa5b7054adf95c3011149c58d064eb86ab1c720a71d7543b20844b4c  REVIEW_REQUEST_V4.md
7fc6476ccfad6d09d548582ceb892ecf4113c982a9f968e1f003f09e46651e3f  PREREGISTRATION_V4.md
9bfa918b2d749b6904ee1b5a2a5386e4ec82dd541d480c2507936ea05349420c  SUPERSESSION.md
a26ed8819bad727a8e11efa3954c3fbd8d8b724ea868d75e5eaf9a746e9a5852  LEDGER_PATCH_REQUEST.md
a25cf871292acffd88f1c1440eeec1c0695c01136fac480b887cb88c22293cb7  d43_v4_source.tar.gz.sha256
```

## Remaining live-Linux debt (disclosed, unchanged in kind from v3)

Live `/proc`, cgroup v2, systemd user scopes, `setsid` (now including
the new systemd-mode `setsid --wait` wrapper and its session-leadership
identity gate - the one genuinely new Linux-behavior assumption of v4),
`sha256sum`, prlimit/taskset/timeout chains, and IMDSv2 were exercised
only through injectable-reader fixtures in exact Linux layouts plus
source reading; no Linux host has run this packet.  After a hostile PASS
and coordinator GO, the first AWS action must be staging plus a
lease/containment/preflight rehearsal on the registered idle host -
explicitly confirming `ps -o sid=,pgid= -p $$` leadership inside a real
`systemd-run --scope setsid` chain - before any heavy stage.  Also
disclosed: the terminal binds every candidate field to on-disk
artifacts, but a coordinated post-exit rewrite of the candidate plus
every referenced artifact is excluded operationally (censuses, one-shot
lease, authority-bearing post-mortem), not cryptographically; and the
29/155 inventory remains a preregistered forecast the run can only
confirm or refuse, never measure.

## Authorization statement

**No AWS launch is authorized.**  The packet status is
`V4_REPAIRED_LAUNCH_NOT_AUTHORIZED`; the review manifest is deliberately
AWS-unregistered (`UNREGISTERED_REVIEW_PACKET_DO_NOT_LAUNCH`, all
`expected_*` fields empty, `authorization.solve = false`) and every
compute entry point refuses it.  Launch additionally requires, in order:
a fresh independent different-model hostile review PASS of this exact v4
seal, the coordinator's separate GO, and a fresh immutable host
registration binding the manifest, source list, archive, and launcher
digests.  Nothing in this report promotes any v1, v2, v3, or v4
mathematical claim.

<!-- BODY-END -->

## Report-body self-hash

SHA-256 of this report's body, defined as every byte of this file up to
and including the line `<!-- BODY-END -->`:

```text
8ffe97d5f3e5c13f111c0165e8e26d4b63b7c3d421886dcad425f25c3e5218ff
```

Reproduce with:

```sh
python3 -c 'import hashlib,sys;b=open(sys.argv[1],"rb").read();m=b"<!-- BODY-END -->\n";print(hashlib.sha256(b[:b.index(m)+len(m)]).hexdigest())' \
  xmodel/d43-exact-sparse-rows-v4-repair-fable5-20260829.md
```
