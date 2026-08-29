# Hostile review: D43 exact a00pp sparse rows v4 — independent repair adjudication

Date: 2026-08-29
Reviewer: Opus 5 (independent source/custody referee lane; producer was Fable 5)
Packet: `cases/d43_exact_sparse_rows_v4_20260829/`
Charge: `REVIEW_REQUEST_V4.md` +
`xmodel/d43-exact-sparse-rows-v4-repair-fable5-20260829.md`
Prior: I authored the v3 hostile review
(`6e01e5d7…09bd9`, body `1b90552a…62b82`) that returned REPAIR_REQUIRED.
I did not assume any of its five repairs was implemented correctly.

## Overall verdict

**PASS_FOR_DISPOSABLE_LIVE_LINUX_REHEARSAL**

Every charged root — R1, R1-sidecar, R3, R4, R5, the v2→v3/v4
mathematical byte-diff, the preserved v3 confirmations, and the bounded
hostile suites — is closed in the actual source and under adversarial
fixtures I built myself.  My v3 blocking finding is dead: the fabricated
candidate that reached the positive terminal in v3 now fails three named
gates, and I could not construct any *un*coordinated forgery that reaches
a positive terminal.  I found **no blocking defect**.

Four non-blocking findings follow (§5): a genuinely one-sided post-mortem
rule (new, not disclosed), an available-but-unused cryptographic
narrowing of the post-exit rewrite window, five non-discriminating test
fixtures, and a short list of reporting/metadata nits.  None of them can
manufacture a false positive terminal.

This PASS licenses only a **small disposable AWS rehearsal of the
process/custody paths**.  It does not authorize the heavy emitter job, a
mathematical terminal, or any D43 promotion.  No v4 jet, row, inventory,
point, or verdict exists.

## Boundary and disclosure

I worked inside the v4 packet, the two charged reports, the three pinned
prior producer/seal files named in `SOURCE_V4.sha256`, and this output.
Per the hard boundary I did not access, list, search, build, status, or
control `jc2-lean`; I ran no `git status` or other workspace-wide command;
no Singular, msolve, Sage, PARI, or other heavy CAS; no web; no AWS; no
canonical edit; no commit; no push.  I modified no packet file and no
producer report — every test ran either read-only against the packet, in
`/tmp` staging, or in a private mirrored tree (§9).

**Execution gaps I disclose rather than paper over.**  This is a macOS
host.  Live `/proc`, cgroup v2, systemd user scopes, `setsid --wait`,
`systemd-run --scope`, `ps -o sid=,pgid=`, IMDSv2, and `prlimit`/`taskset`
chains were exercised only through the production code's injectable
`proc_root`/`--cgroup-dir` parameters with fixtures I built in the exact
Linux layout, plus source reading.  §6 is therefore a source-semantics
adjudication, not a live-Linux observation.  I did **not** run the
producer's `build_source_archive_v4.py` — it writes into the packet — so I
re-implemented its staging out of tree instead (§4).

## 1. Frozen charge: seal and report replay

Both charged reports replay at full-file and body hash, using the
`<!-- BODY-END -->` convention each declares (not a guessed marker):

```text
6e01e5d7e7852d094559ab57cd7a256c41390fca99e38a6c55fbea8f12209bd9  v3 hostile review (full)
1b90552abddb14bf5946a2e85f0a5ac26dae05d3049ef578db507c766862bd82  v3 hostile review (body)
3dd246020803afd7ac2b855841bab139fe1f6490a46a5d010569340dbc3d3732  v4 repair report (full)
8ffe97d5f3e5c13f111c0165e8e26d4b63b7c3d421886dcad425f25c3e5218ff  v4 repair report (body)
```

`shasum -a 256 -c SOURCE_V4.sha256` from the repository root: **39/39 OK**,
covering every packet file, the sealed archive, all three prior packet
seals, the pinned v2/v3 producers, all frozen dependencies, and the
controlling reviews.  Seal own digest
`dd05d82fcc0f8cd71af173bdef7420811c188ac1111265ac842b0b5437fd81f1`
— matches the producer report.  **Re-replayed after all of my testing:
39/39 OK, zero non-OK lines, no `__pycache__`, no new files.**

## 2. R1 — value-binding terminal: CONFIRMED CLOSED

`bind_candidate` (`job_contract_v4.py:970-1157`) is real binding, not
relabelled copying.  I read every one of the twelve gates and then attacked
them with fixtures built from scratch — I deliberately did **not** reuse
the producer's fixture, and my honest chain reaches the positive terminal,
so the refusals below are discriminating, not blanket.

| Candidate field | v3 treatment | v4 treatment (verified by me) |
|---|---|---|
| `run_nonce` | bound | bound (held-flock probe, `:175-215`) |
| `lease_sha256` | **shape only** | `sha256_path(RUN_LEASE.json)` `:1000` |
| lease `registration_sha256` | absent | `sha256_path(records/REGISTERED.json)` `:1007` |
| `manifest_sha256` | **shape only** | rehash + `MANIFEST_SCHEMA` check `:1018-1027` |
| `claim_boundary` | not examined | manifest equality **+ null-shape** `:1030-1039` |
| `preflight_receipt_sha256` | **shape only** | rehash + `pass`/authority/manifest `:1041-1055` |
| `pilot_gate_sha256` | **shape only** | rehash + status/nonce/manifest `:1057-1070` |
| `merge_receipt_sha256` | **shape only** | rehash + 9-field contract `:1072-1096` |
| `merge_payload_sha256` | **shape only** | rehash **of the bytes** + receipt crossbind `:1098-1108` |
| `semantic_sha256` | **shape only** | receipt-crossbound under rehashed receipt `:1110-1121` |
| `template_bridge_sha256` | not examined | receipt-crossbound `:1123-1134` |
| `exact_inventory` | **not examined at all** | receipt-crossbound `:1136-1142` **and** contract-checked `:844-877` |

Key census (`CANDIDATE_KEYS`, `:54-58`, enforced `:933`) refuses both
missing and extra keys.  Provenance is recorded per field in
`candidate_binding`, and `binding_failures` records the refusing exception.

**The v3 exploit, rebuilt.**  My independent reproduction of the exact v3
attack (wrong lease digest, `live_rows: -7` / `exact_zero_rows: 9999`,
sidecar naming a nonexistent archive):

```text
v3:  FINAL_CLASSIFICATION=EXACT_A00PP_184_RAW_J_ROWS_EMITTED_NO_SOLVE, rc 0, failed_gates []
v4:  positive=False  status=NO_VERDICT_ARCHIVE_SIDECAR_BOUND  rc 3
     failed_gates=[archive_sidecar_bound, candidate_inventory_contract,
                   candidate_inventory_crossbound, candidate_lease_digest_bound,
                   candidate_merge_payload_digest_bound, candidate_merge_receipt_digest_bound,
                   candidate_semantic_crossbound, candidate_template_bridge_crossbound]
```

**Per-field value forgeries — all eight, each caught by its named gate:**

```text
lease_sha256              -> candidate_lease_digest_bound
manifest_sha256           -> candidate_manifest_digest_bound  (+ claim/preflight/pilot cascade)
preflight_receipt_sha256  -> candidate_preflight_digest_bound
pilot_gate_sha256         -> candidate_pilot_gate_digest_bound
merge_receipt_sha256      -> candidate_merge_receipt_digest_bound
merge_payload_sha256      -> candidate_merge_payload_digest_bound
semantic_sha256           -> candidate_semantic_crossbound
template_bridge_sha256    -> candidate_template_bridge_crossbound
```

**Inventory census (12 fixtures, all refused through
`candidate_inventory_contract` unless noted):** `-7/9999`; `30/154`
(sums to 184 but violates 29/155); `live_rows: True` (bool is refused —
`exact_int`, `:839-841`); bands `{11,9,9}`; `max_tail_degree: 3`;
`max_tail_degree: True`; 154 zero targets (undersized); 155 duplicated
targets; a bool inside a target pair; an extra `total_rows` key;
inventory drifting from the receipt only (→ `candidate_inventory_crossbound`);
a **string** inventory (→ `candidate_schema_valid`, refused at `load_candidate`).

**Claim boundary — this one is stronger than the producer claims.**
Promotion is refused *even when the manifest is rewritten to match and the
whole preflight/pilot/receipt/candidate digest chain is recomputed*,
because the null-shape rule (`:879-892`) is a **source constant**, not a
comparison against on-disk data:

```text
keller_map=True (candidate+manifest+full chain)   -> candidate_claim_boundary_bound
jc2_counterexample="yes" (full chain)             -> candidate_claim_boundary_bound
E5/E6 note dropped to null (full chain)           -> candidate_claim_boundary_bound
E5/E6 note emptied to "" (full chain)             -> candidate_claim_boundary_bound
promotion in the candidate only                   -> candidate_claim_boundary_bound
```

I ran the same check against the *real* `PIPELINE_MANIFEST_V4.json`
boundary (8 keys, exactly one non-null: the E5/E6 note): accepted as
shipped, refused under every promotion.  One precision: the null-shape
rule pins the *values of present keys*, not the key set, so a coordinated
rewrite could **delete** a null key.  That weakens the published list of
explicit non-claims; it cannot create a claim.

**Registration:** drifted and absent `records/REGISTERED.json` both →
`candidate_registration_digest_bound`.

## 3. R1-sidecar, R3, R4, R5 — each CONFIRMED CLOSED

**Sidecar archive binding** (`verify_sidecar_archive`, `:894-919`).
Thirteen fixtures, all refused, each with a distinguishing reason:
dangling, drifted digest, drifted *content*, foreign name (pointing at a
real, correctly-hashed sibling archive), `../` traversal, absolute path,
symlink, directory, two-line sidecar, missing sidecar, malformed line,
uppercase hex.  The terminal's `terminal_archive_sha256` is the **rehash**,
and `terminal_archive_member` names the resolved member.

**Full-member-set archive census** (`extract_and_verify_archive`,
`:777-824`).  My own tarballs, built member-class by member-class:

```text
regular members only ................ ACCEPTED (2 entries)
extra top-level DIRECTORY ........... REFUSED ARCHIVE_NONREGULAR_MEMBER:jc2/extradir   <- v3 ACCEPTED
nested DIRECTORY chain .............. REFUSED ARCHIVE_NONREGULAR_MEMBER:jc2/x          <- v3 ACCEPTED
root prefix DIRECTORY jc2/ .......... REFUSED ARCHIVE_NONREGULAR_MEMBER:jc2
SYMLINK / HARDLINK / FIFO / CHARDEV . REFUSED ARCHIVE_NONREGULAR_MEMBER
extra unmanifested FILE ............. REFUSED ARCHIVE_MEMBER_CENSUS_DRIFT
manifest line dropped ............... REFUSED ARCHIVE_MEMBER_CENSUS_DRIFT
traversal member .................... REFUSED UNSAFE_RELATIVE_PATH:../escape.txt
member outside include .............. REFUSED ARCHIVE_UNSAFE_DUPLICATE_OR_EXTRA
duplicate member .................... REFUSED ARCHIVE_UNSAFE_DUPLICATE_OR_EXTRA
directory shadowing a manifested file REFUSED ARCHIVE_UNSAFE_DUPLICATE_OR_EXTRA
```

My v3 Finding 2 is fully repaired, and the equality is now over the
**full** member set (`:806`), because non-regular members are refused
before the census is taken (`:794-795`).

**Real censuses, no copied gates.**  `pgid_census_real` refuses
`cleanup_pgid ∈ {0, 1, -1}` and non-`int`; `2` and `4242` pass.  Mode
consistency is exact in both directions:

```text
systemd_scope + cgroup "1" ........... positive; gate True;  KERNEL_CGROUP_PROCS_CENSUS provenance
systemd_scope + cgroup "0" ........... NO_VERDICT_CGROUP_FINAL_GATE
systemd_scope + "NOT_APPLICABLE" ..... NO_VERDICT; cgroup_gate_mode_consistent False
setsid_pgid   + "NOT_APPLICABLE" ..... positive; gate value is the STRING, never true
setsid_pgid   + cgroup "1" ........... NO_VERDICT; mode-inconsistent (the v3 copied-gate lane is dead)
setsid_pgid   + cgroup "0" ........... NO_VERDICT; mode-inconsistent
```

The `all`-style evaluation cannot be spoofed by other truthy strings:
`gate_passes` (`:1239-1240`) accepts only `is True` or the exact
`NOT_APPLICABLE` string, `--cgroup-final-gate` is argparse-restricted to
`{"0","1","NOT_APPLICABLE"}`, and a type census of an honest positive
terminal shows **41 gates, all `bool`, zero strings** — the only route to a
string value is the mode-legal fallback lane.

**Authority-bearing post-mortem** (`postmortem_gate`, `:1310-1381`).
Nine fixtures:

```text
positive + clean census ................ rc 0,  no fault object
positive + nonzero census rc ........... rc 79, fault written 0444
positive + non-empty pgid census ....... rc 79, fault written 0444
positive + non-empty tag census ........ rc 79, fault written 0444
positive + unreadable census ........... rc 79, fault written 0444
NO_VERDICT + dirty census .............. rc 0,  no fault object
unreadable terminal .................... rc 79, fail closed
positive:true with NO_VERDICT status ... rc 79  (the OR at :1327-1329 catches both markers)
positive status with positive:false .... rc 79
double-fault attempt ................... first fault byte-identical; terminal byte-unchanged
```

The 0444 mode genuinely blocks an owner rewrite through `open(w)`
(`PermissionError`), the fault embeds the terminal digest and both census
contents/digests, and `O_EXCL` makes the first fault win.  The launcher
wiring is real: `postmortem_gate_rc=$?` (`aws_launch_v4.sh:308`) →
`exit 78` (`:330`) with a loud banner.

## 4. Independent v2/v3/v4 diff and mathematical fidelity — CONFIRMED

I did **not** trust `math_function_diff_v4.py`'s categories.  I wrote my
own AST segmenter and censused every removed line by hand.

**v3 → v4.**  My AST diff: 73 shared top-level functions/classes,
**73 byte-identical, 0 differing**; 31 shared module assignments, exactly
2 differing (`SCHEMA`, `MANIFEST_SCHEMA`, `.v3`→`.v4`); no added or removed
functions.  Stronger than the producer's claim, a **whole-file** `diff -u`
of `selected_rows_v3.py` against `selected_rows_v4.py` is exactly four
hunks: the module docstring, the `-O` refusal message, and the two schema
strings.  Nothing hides outside the AST segments.  **Zero mathematical
change v3 → v4.**

**v2 → v4.**  My independent counts reproduce the producer's exactly:
64 shared, **39 byte-identical**, 25 differing, 2 removed
(`atomic_text`, `finalize_run`), 9 added, 2 differing assignments,
4 added assignments.  The 39 identical functions contain the entire
arithmetic/jet/row core: every `cp_*`, `cv_add/scale/constant`, `cs_*`,
`cj_*`, `rc_k3`, `collapse_vexpr`, `convert_a_orbit`, `collapsed_gm_jet2`,
`collapsed_b_block`, `_selected_product`, `selected_source_rows`,
`evaluate_cp_mod`, `evaluate_cvexpr_mod`, and every canonicalization and
semantic-digest function.

I censused all **169 removed lines** across the 25 differing functions.
83 are `assert` heads, 22 are `ValueError` raises, and I read each of the
remaining 64 individually.  My classification, derived from the diffs and
not from the tool's table:

* `collapse_r1_ring_element`, `expected_collapsed_d21_band20`,
  `assert_raw_b_orbits`, `template_bridge_spec`, `banked_pin_audit`,
  `_load_pickle_after_hash`, `registered_modular_replay`,
  `template_bridge_modular_gate`, `validate_cover`,
  `validate_exact_inventory`, `verify_operational_sources`,
  `load_manifest` — `assert`→`require` / `ValueError`→`CustodyError`
  with **literally identical predicates**.  `CustodyError` subclasses
  `ValueError` (`selected_rows_v4.py:40`), so no `except` contract changes.
* `assemble_pair`, `build_side`, `load_pair`, `load_side_receipt`,
  `load_shard_receipt`, `conditional_emit_all`, `validate_preflight_receipt`,
  `main` — lease threading: signature extension plus **added**
  `require_lease_binding` / `run_nonce` checks.  I verified no predicate is
  dropped (e.g. `load_pair` keeps every v2 check and adds `run_nonce` to
  the pair custody digest).
* `collapsed_d21_gate` — the reviewed charged-root-1 rewrite: the decision
  is now `rows != expected` structural equality, digests are computed after
  and only assert receipt separation.  Identical to what I confirmed in v3.
* `cv_mul`, `build_collapsed_side`, `assert_operational_registration` —
  version literals only.  `build_collapsed_side` additionally gains two
  revalidation calls (`require_registry`, `require_sparse_free_support`)
  and its `"D43-v3-%s"` string is the `tag` argument of
  `collapsed_gm_jet2`, which I traced to a single `print()` (`:509-510`) —
  it enters no digest and no arithmetic.
* `print_registry` — added `require_registry`.
* `load_manifest` — one genuine **predicate change**: the inline v2
  resource-contract dict became the `RESOURCE_CONTRACT` constant.  I
  compared them: the constant is a strict superset, identical on all ten
  shared keys, adding six whole-job containment keys.  It is a
  *strengthening* of the manifest requirement and touches no mathematical
  parameter (`D`, depth, support, registry hash, coefficient algebra are
  all unchanged and still required).  The producer's blanket phrase "checks
  only added, never removed" is slightly imprecise here; the effect is in
  the safe direction and I verified the shipped manifest matches the
  constant exactly.

**No numeric or algebraic expression changed anywhere in v2 → v4.**  The
removed `finalize_run` is confirmed to be the v2 early-positive publisher
(it wrote `VERDICT`, `TERMINAL`, `CURRENT_STAGE=COMPLETE`, and
`FINAL_RECEIPT.json`); in v4 the producer writes no positive marker — my
own grep of `selected_rows_v4.py` finds only `*_COMPLETE` *stage* strings
and `CANDIDATE_PENDING_TERMINAL_DECISION`, and all eight `CURRENT_STAGE`
values in the supervisor are `RUNNING_`-prefixed.

The tool itself runs clean (`V2_V3_V4_MATH_DIFF_CLOSED`) with correct pins,
and `--write-report` to `/tmp` regenerates `V2_V4_MATH_FUNCTION_DIFF.md`
byte-identically (`fb5b220a…c295b812f`, matching the seal).  Two notes on
the tool are in Finding 4.

**Preserved v3 confirmations, re-verified by me:**

| Check | Result |
|---|---|
| Zero production asserts | my own `ast.Assert` census: 0 in all five packet Python modules |
| `python -O` refusal | all five modules refuse at import; **and** per subcommand: `terminal`, `postmortem-gate`, `cleanup`, `archive-extract-verify` all raise `OPTIMIZED_PYTHON_REFUSED_FAIL_CLOSED` |
| Deterministic archive | out-of-tree rebuild from two independent stagings → `9051a3db…dd31ba` both times, **matching the seal**; census regenerates byte-identically; fresh-extraction replay 20/20; every member byte-identical to the live tree |
| Zero self-reference | scanned every archive member for the outer digest: **0 hits**.  Pinned only in `aws_launch_v4.sh:21`, the packet seal, the sidecar, and the two reports |
| Single late terminal authority | my own census: exactly 3 `TERMINAL.json` writers (`run_conditional_pipeline_aws_v4.sh:129`, `:648`; `aws_launch_v4.sh:71`), all existence-guarded; only `:648` can be positive; both emergency publishers hard-code `"positive": false` and a `NO_VERDICT_` prefix |
| `solve=false` firewall | `load_manifest` requires exact equality of the whole `authorization` dict, so any `solve: true` manifest is refused at load; shipped manifest has `solve: false` |
| Launch de-authorization | `status = V4_REPAIRED_LAUNCH_NOT_AUTHORIZED`, `registration_status = UNREGISTERED_REVIEW_PACKET_DO_NOT_LAUNCH`, all `expected_*` blank; `assert_operational_registration` **refuses the shipped manifest**, so every compute entry point fails closed (verified by calling it) |
| Bounded suites | `test_job_contract_v4` **45/45 OK** (8.17 s); `test_selected_rows_v4` **21/21 OK** (13.9 s) — matching the producer's claim |
| Honest fixture | verified: every rehashed digest in the v4 happy-path candidate is `sha256_path()` of a real on-disk artifact and the sidecar names a real archive.  The two constant-looking values (`"5e"*32`, `"7a"*32`) are the receipt-crossbound pair and appear identically in a real `MERGE_RECEIPT.json`, which is what the contract binds them to.  The v3 suite's fabricated `"11"*32 … "66"*32` chain is gone |

**Do the tests bind, or merely pass?**  I ran a 23-mutation battery against
`job_contract_v4.py` in a private mirrored tree with a clean 45/45
baseline.  **Seventeen mutations are caught**, including every one that
disables a load-bearing R1/R2/R3/R4/R5 predicate that the suite advertises.
Six survive; I checked each behaviourally and **none is a code defect**
(two are equivalent mutants, four are test gaps — Finding 3).

## 5. Findings, in severity order

### Finding 1 (non-blocking; terminal authority) — the post-mortem rule is one-sided

`postmortem_gate` writes a fault object only on the *unclean* path
(`:1337-1340` returns 0 and writes nothing when clean), and the terminal's
`post_boundary_contract.rule` is stated one-directionally:
`A_POSITIVE_TERMINAL_IS_VOID_IF_THE_LAUNCHER_POSTMORTEM_FAULT_OBJECT_EXISTS`.
Consequently **the absence of the fault object does not attest that the
post-mortem ran.**  Two concrete paths produce a positive terminal with no
fault object and no post-mortem evidence:

* the launcher's `on_exit` trap (`aws_launch_v4.sh:129-139`) runs
  `kill_boundary`/`postmortem` **only** `if [[ ! -e "$terminal" ]]`; once
  the supervisor has renamed a positive terminal, a launcher `TERM`
  (`trap 'exit 143' TERM`) exits without any census;
* a launcher `SIGKILL` after the supervisor's rename leaves nothing at all.

`records/LAUNCHER_POSTMORTEM.json` is written inside `postmortem()`, so it
too is absent in those paths, and it is outside the sealed terminal archive
in every path (the archive is built at `:563` before the terminal decision
at `:610`).  This is the residue of my v3 Finding 4: the fault side is now
genuinely authority-bearing, but the clear side is not attested.

**Minimum repair.**  Have `postmortem-gate` write an immutable 0444
`TERMINAL_POSTMORTEM_CLEAR.json` (same `O_EXCL` discipline, embedding the
terminal digest, both census digests, and `postmortem_rc = 0`) on the clean
path, and restate the terminal rule two-sidedly: *a positive terminal is
void if the fault object exists **or** if the clear object is absent*.
The gate already computes every input; this is a few lines.
**Regression test.**  A positive terminal with neither object present must
be classified void by whatever reads the pair.

### Finding 2 (non-blocking; defense in depth) — two available bindings are unused

The terminal binds every candidate field to on-disk artifacts, so an
*un*coordinated post-exit edit is dead (I confirmed: a payload-file swap
with untouched metadata → `candidate_merge_payload_digest_bound`).  A
**coordinated** rewrite of the candidate *and* every referenced artifact
does still reach a positive terminal.  I reproduced it and measured
exactly what it can and cannot move:

```text
coordinated rewrite (payload bytes + receipt + candidate) -> positive=True
  published semantic_sha256   = attacker value    <-- moves
  published inventory         = 29/155            <-- CANNOT move (source constant)
  published claim_boundary    = unpromoted        <-- CANNOT move (source constant)
  lease / nonce / registration                    <-- CANNOT move (held flock + rehash)
```

So the residual is confined to *payload identity*
(`semantic_sha256`, `template_bridge_sha256`, `merge_payload_sha256`).
The producer discloses this as "excluded operationally, not
cryptographically", which is accurate, and no contract can fully close it
without unpickling attacker-controlled row data in the authority — which
would be worse.  But two cheap bindings are available and unused:

1. **The sealed archive already witnesses the candidate.**  The supervisor
   builds `custody/TERMINAL_MANIFEST.sha256` at `:545` — before the archive
   (`:563`) and before the terminal (`:610`) — over `--include output`, so
   it records the digests of `output/FINALIZE_CANDIDATE.json`,
   `output/MERGE_RECEIPT.json`, and the payload as of that moment, and it
   is sealed into the terminal archive.  `decide_terminal` never reads it
   (my grep: `TERMINAL_MANIFEST` appears in `job_contract_v4.py` only
   inside the manifest builder/verifier and their banners).  Requiring
   `candidate_sha256` and the three payload digests to equal the entries in
   that manifest would make the post-archive-build rewrite window a
   machine-checked gate instead of an audit-by-inspection.
2. **`pgid_census_real` is a shape check, not a binding.**  It requires
   only `cleanup_pgid > 1` (`:1220-1221`); nothing in the contract checks
   that the supplied pgid is the caller's real process group.  The link to
   reality lives entirely in the supervisor shell (`cleanup_pgid=$$` at
   `:516` plus the `ps -o sid=,pgid=`-derived identity gate at `:185-189`).
   Since the terminal runs as a child of the supervisor in the same process
   group (neither script sets `set -m`; I verified pgid inheritance
   through an intermediate `bash`), `require(args.cleanup_pgid ==
   os.getpgid(0))` is a one-line true binding.

Neither is blocking: with the shipped, digest-pinned code both properties
hold on the honest path, and §6 establishes that no source path issues a
positive terminal without a real census.

### Finding 3 (non-blocking; test strength) — five non-discriminating fixtures

Six of my 23 mutations survive the 45-test suite.  Two are **equivalent
mutants**, correctly: making `gate_passes` return `bool(value)` changes
nothing while gate values are only bools or the exact `NOT_APPLICABLE`
string; and deleting the archive full-member-set equality still refuses the
extra-file case one line later, via `TERMINAL_MANIFEST_CENSUS_DRIFT` in
`verify_complete_manifest` (I confirmed both).

The other four are genuine coverage gaps.  In each case **the code is
correct** — I verified it with my own fixture — but the suite would not
notice if the specific predicate were deleted, because a different gate
fires first in the producer's fixture:

| Deleted predicate | Suite | My fixture proving the code is correct |
|---|---|---|
| `validate_claim_boundary` null-shape (`:889-892`) | still OK | coordinated promotion `keller_map=True` → refused |
| `validate_claim_boundary` note check (`:885-887`) | still OK | coordinated empty note → refused |
| inventory receipt crossbind (`:1137-1140`) | still OK | inventory drifting from receipt only → refused |
| merge-payload **file** rehash (`:1099-1101`) | still OK | payload bytes swapped, metadata untouched → refused |
| sidecar exact-name check (`:911`) | still OK | foreign, correctly-hashed sibling archive → refused |
| sidecar symlink/regular check (`:914`) | still OK | archive replaced by a symlink → refused |

The producer's negative-control table is not wrong — those fixtures do
refuse through the named gate — but for these six sub-checks the named gate
is reached by a different internal predicate, so the sub-check itself is
untested.  **Minimum repair:** add the six fixtures above (each is a
two-line variant of an existing test).

### Finding 4 (harmless metadata and reporting fidelity)

* **Three inert `v3` literals in `selected_rows_v4.py`, two disclosed.**
  The producer discloses `cv_mul:300` and `build_collapsed_side:546`;
  `assert_operational_registration:654` also raises
  `"v3 manifest is review-only and AWS-unregistered"` from the v4 module.
  All three are inert (log tag / raise messages) and are retained
  deliberately to keep the v3→v4 function diff empty — a defensible
  tradeoff — but the report's "Two inert v3 literals" undercounts by one.
  Additionally `build_source_archive_v4.py:2` still says "sealed v3 source
  archive" and `:66` stages under `prefix="d43v3stage."`.  Cosmetic.
* **The `NO_VERDICT_` headline names the alphabetically first failed
  gate**, not the root cause (`failed = sorted(...)`, `:1243`;
  `status = NO_VERDICT_PREFIX + failed[0].upper()`, `:1248`).  With an
  unheld lease I observed `FINAL_CLASSIFICATION=NO_VERDICT_CANDIDATE_
  CLAIM_BOUNDARY_BOUND` while the actual cause,
  `LEASE_LOCK_NOT_HELD`, sat correctly in `lease_failure`.  No information
  is lost in the record; an operator reading only the banner is misled
  about *why*.  It can never turn a NO_VERDICT into a positive.
* **`math_function_diff_v4.py` Check 3 is tautological.**  `MATH_CORE`
  (`:63-73`) is defined as a subset of `EXPECTED_IDENTICAL` (`:50-61`), so
  `MATH_CORE - EXPECTED_IDENTICAL` is empty by construction and the check
  can only fail if someone edits the constants.  Likewise the
  `EXPECTED_DIFFERING` repair-class labels (`:88-115`) are asserted
  metadata: apart from `cv_mul` (genuinely machine-normalized, `:212-217`),
  the tool never verifies that a function's diff belongs to its claimed
  class.  The *set* arithmetic (Checks 1, 2, 5) is real and I reproduce it
  independently; the *classification* is producer-asserted, and I confirmed
  it by reading all 25 diffs myself (§4) rather than by trusting the table.

## 6. `setsid --wait` / PGID / SID / cgroup source audit

Adjudicated by source semantics; live-Linux behaviour remains rehearsal
debt.

* **`setsid` is required before mode selection** (`aws_launch_v4.sh:221`)
  and wraps the supervisor in **both** branches — `:257` inside
  `systemd-run --user --scope --wait`, `:261` in the fallback.  My own
  count confirms exactly two `setsid --wait bash "$supervisor"` sites.
  The supervisor is therefore a session/PGID leader in both modes, and
  cgroup membership is inherited independently of the session, so the
  systemd scope still contains it.
* **The leadership assumption is checked, not assumed.**
  `run_conditional_pipeline_aws_v4.sh:185-189` reads
  `ps -o sid= -p $$` and `ps -o pgid= -p $$` and sets `session_leader=1`
  only on `sid == pgid == $$`; the terminal requires
  `containment_identity_gate == "1"` for positivity.  If `ps` is missing or
  lacks `-o sid=`, the substitution is empty, the gate is 0, and the run
  can only reach a NO_VERDICT.  Fail-closed.
* **No vacuous-pgid source path survives.**  My grep finds
  `cleanup_pgid=$$` at `:114` (peer-cancellation) and `:516` (final census)
  and **no** `cleanup_pgid=0` anywhere; the v3 lane is deleted.  The
  terminal independently refuses `pgid <= 1`.  Composing: a positive
  terminal implies the identity gate fired, which implies `$$` really is
  the group leader, which implies the census parameter is real.  Adding
  the always-real `JOB_TAG`-environ census (`process_records`, `:280-300`,
  unchanged from v3 and re-confirmed there), **I find no source path that
  can issue a positive terminal without a real census in either mode.**
* **The fallback cgroup gate is never a copy.**  `:534-538` writes a
  `NOT_APPLICABLE` census file and sets the gate to the literal string;
  the terminal's mode-consistency gate refuses any other combination in
  either direction (§3), and `gate_provenance` names the evidence source
  for every gate.
* **`kill_boundary` now targets the right group.**  `aws_launch_v4.sh:88-100`
  reads the session leader from `custody/containment_identity.json`
  (written at `:211-215`, before any heavy stage) and kills `-$leader`; the
  v3 `-$!` group kill targeted the `setsid`/`systemd-run` wrapper.  The
  launcher is in a different session, so it cannot sweep itself.  If the
  identity file is absent the leader resolves to 0 and only the always-real
  `JOB_TAG` census runs — degraded, but in the fail-closed direction, and
  unreachable on any path that produced a positive terminal.
* **Rehearsal item, not a defect:** only `command -v setsid` is probed, not
  `--wait` support (util-linux ≥ 2.24).  On an older `setsid` the
  invocation fails, no supervisor runs, and no terminal exists → NO_VERDICT.
* **Genuinely new Linux assumption in v4:** `setsid --wait` nested inside
  `systemd-run --user --scope --wait`, and session leadership as read by
  `ps`.  The producer discloses this; I confirm it is the one new
  live-behaviour dependency and it must be the first thing the rehearsal
  exercises.

## 7. Maximum possible claim after a future successful reviewed AWS terminal

Unchanged from my v3 §8, with narrowings 2 and 3 now **retired** (R4 and R5
landed) and narrowing 1 retained and now preregistered verbatim by the
producer:

> On one registered host, under a held one-shot lease and a single
> containment boundary, two independently constructed sides agreed on the
> collapsed D21 band-20 object by literal structural equality, and one
> process then emitted all 19 shards and the 184-row raw-J merge for the
> exact a00pp support-specialized truncation, **reproducing the
> preregistered 29 live / 155 exact-zero inventory** with live bands
> {20:10, 30:9, 40:10} and tail degree ≤ 2, with `solve = false`.

Retained narrowing: `validate_exact_inventory`
(`selected_rows_v4.py:1259-1276`, byte-identical to v3) **enforces** rather
than measures, and `validate_inventory_contract` enforces the same numbers
a second time in the terminal.  A run whose true inventory differs can only
fail closed; it cannot publish a different inventory.  The run therefore
**confirms the preregistration**; it does not determine the inventory.
`PREREGISTRATION_V4.md` and `LEDGER_PATCH_REQUEST.md` both state this
correctly.

New narrowing from Finding 1: until the clear object lands, a positive
terminal with no fault object carries *no affirmative* post-boundary orphan
attestation, only the absence of a negative one.

It remains **not**: exact a00pp raw-J point existence, full residue-A
template point existence, banked NF presentation equivalence, the displayed
E5/E6 unit extension, all-depth compatibility, a Keller map, or a JC2
counterexample — matching `PIPELINE_MANIFEST_V4.json`'s `claim_boundary`,
every entry of which is `null` except the E5/E6 note, and which the
terminal now enforces structurally.

## 8. Exact launch boundary

**No mathematical AWS launch is authorized by this review.**

Authorized by this PASS, and nothing more:

* a **small, disposable, single-host rehearsal** on a fresh idle registered
  Linux instance, exercising only the process/custody paths: archive
  staging and replay, `flock` lease acquisition and one-shot exclusivity,
  the containment-mode probe, `systemd-run --scope` + `setsid --wait`
  session/PGID leadership confirmed by `ps -o sid=,pgid= -p $$` from inside
  the boundary, the identity gate, monitor start/stop, the final PGID/tag/
  cgroup censuses, the terminal decision on a synthetic candidate, and the
  launcher post-mortem gate;
* the rehearsal must run with `solve=false` and **must not** run any heavy
  stage (`build_side`, `assemble_pair`, `conditional_emit_all`), and must
  be torn down afterwards.

Before **any** heavy emitter stage or mathematical terminal, all of the
following are additionally required, in order:

1. Findings 1 and 3 landed (Finding 2 is recommended in the same
   revision; none of the three is blocking for the rehearsal itself);
2. a fresh packet seal and a fresh independent different-model hostile
   review PASS of that exact seal;
3. the coordinator's separate explicit GO;
4. a fresh immutable host registration binding the manifest,
   operational-source list, archive, and launcher digests — the shipped
   manifest is deliberately `UNREGISTERED_REVIEW_PACKET_DO_NOT_LAUNCH` and
   every compute entry point refuses it today.

Nothing in this review promotes any v1, v2, v3, or v4 mathematical claim.

## 9. Commands run

```text
shasum -a 256 <both charged reports>                          -> both full hashes match
python3 -c '<BODY-END recipe>' <both reports>                 -> both body hashes match
shasum -a 256 -c SOURCE_V4.sha256   (before and after)        -> 39/39 OK twice
python3 -B -m unittest test_job_contract_v4  -v               -> Ran 45, OK (8.17 s)
python3 -B -m unittest test_selected_rows_v4 -v               -> Ran 21, OK (13.9 s)
python3 -O  <import all 5 modules; 4 subcommands>             -> 9/9 OPTIMIZED_PYTHON_REFUSED_FAIL_CLOSED
my own ast.Assert census over 5 modules                       -> 0,0,0,0,0
my own AST segment diff v3->v4                                -> 73/73 identical, 2 schema assigns
diff -u selected_rows_v3.py selected_rows_v4.py               -> 4 hunks, all non-mathematical
my own AST segment diff v2->v4                                -> 39 identical / 25 differ / 2 removed / 9 added
my own removed-line census over the 25 differing functions    -> 169 lines, all individually justified
python3 -B math_function_diff_v4.py                           -> V2_V3_V4_MATH_DIFF_CLOSED
python3 -B math_function_diff_v4.py --write-report /tmp/...   -> byte-identical to the sealed fb5b220a...
out-of-tree archive rebuild, two independent stagings         -> 9051a3db... twice; census + 20 members identical; 0 self-refs
negative control: v3 forged candidate -> decide_terminal      -> NO_VERDICT, 8 named gates fail
negative control: 8 per-field digest forgeries                -> 8/8 refused by their named gates
negative control: 12 inventory forgeries                      -> 12/12 refused
negative control: 5 claim-boundary forgeries (incl. coordinated) -> 5/5 refused
negative control: 3 key-census / authority forgeries          -> 3/3 refused
negative control: 2 registration forgeries                    -> 2/2 refused
negative control: 13 sidecar fixtures                         -> 13/13 refused, distinct reasons
negative control: 14 archive member classes                   -> dirs/symlinks/hardlinks/fifo/chardev/extra/dup/traversal all REFUSED
negative control: 5 pgid values, 6 mode/cgroup combinations   -> only mode-legal combinations positive
negative control: 9 postmortem-gate fixtures + double fault   -> as specified; 0444 immutability confirmed
negative control: 5 lease forgeries                           -> 5/5 refused
negative control: full coordinated post-exit rewrite          -> positive (Finding 2), inventory + claim boundary immovable
23-mutation battery vs a clean 45/45 mirrored baseline        -> 17 caught, 2 equivalent, 4 test gaps (Finding 3)
bash -n on supervisor and launcher                            -> both OK
```

All temporary directories were inert, under `/tmp`
(`/tmp/nc_opus5_v4/`, `/tmp/opus5v4*`), and are removed.  No packet file
was modified — the seal re-replays 39/39 and the directory listing is
unchanged, with no `__pycache__`.  No canonical file edited, no commit, no
push, no AWS action, no `jc2-lean` access, no workspace-wide command.

<!-- BODY-END -->

## Report-body self-hash

SHA-256 of this report's body, defined as every byte of this file up to and
including the line `<!-- BODY-END -->`:

```text
12bd3893632706993762795af9b22a83f46d164b7a834893c4286826d15a36c5
```

Reproduce with:

```sh
python3 -c 'import hashlib,sys;b=open(sys.argv[1],"rb").read();m=b"<!-- BODY-END -->\n";print(hashlib.sha256(b[:b.index(m)+len(m)]).hexdigest())' \
  xmodel/d43-exact-sparse-rows-v4-hostile-review-opus5-20260829.md
```

Full-file SHA-256 (computed after the body hash was substituted above):

```sh
shasum -a 256 xmodel/d43-exact-sparse-rows-v4-hostile-review-opus5-20260829.md
```
