# D43 exact a00pp sparse rows v4: implementation report

**Status:** `V4_REPAIRED_LAUNCH_NOT_AUTHORIZED` - repaired, review-frozen,
AWS-unregistered, and non-launchable.  No D43 jet was built, no exact row
was emitted, no solve was attempted, no CAS ran, and no AWS action was
taken while preparing this revision.  V1, v2, and v3 are unmodified.

## Revision provenance

This packet answers the Opus 5 v3 hostile review
`xmodel/d43-exact-sparse-rows-v3-hostile-review-opus5-20260829.md`
(SHA-256 `6e01e5d7e7852d094559ab57cd7a256c41390fca99e38a6c55fbea8f12209bd9`,
report-body seal
`1b90552abddb14bf5946a2e85f0a5ac26dae05d3049ef578db507c766862bd82`),
which confirmed the v3 mathematical source fidelity within its boundary
and returned REPAIR_REQUIRED on custody.  The producer-side controlling
input is the v3 repair report
`xmodel/d43-exact-sparse-rows-v3-repair-fable5-20260828.md` (SHA-256
`5759cfe81e21e7e4d3967b96152eaed5e789ed0498b039804b17c30853616b75`).
The v3 seal digest
`5423bd88328c338c54072b056d3f64251dc57de6f5112646f9d157f991ab5271` and the
v1/v2 seal digests are carried in the manifest provenance.

## Mathematics: v3 preserved byte-for-byte, machine-checked

`selected_rows_v4.py` differs from `selected_rows_v3.py` **only** in the
module docstring, the two `.v3`->`.v4` schema constants, and the
optimized-Python refusal message.  Every top-level function is
byte-identical (73/73), machine-checked by `math_function_diff_v4.py`.
The same tool closes the v2->v3 diff Opus 5 disclosed as UNADJUDICATED:
39 shared functions - the entire collapsed-arithmetic and jet/row core -
are byte-identical v2->v4, and the 25 differing shared functions decompose
exactly into the five reviewed repair classes (assert->require with
unchanged predicates, lease threading, the literal-D21-gate rewrite,
version-literal strings, explicit v1-fact revalidation), with the two
removed (`finalize_run`, `atomic_text`) and nine added custody functions
pinned.  The sealed adjudication with full unified diffs is
`V2_V4_MATH_FUNCTION_DIFF.md`, deterministically regenerable.  Two inert
v3 literals inside mathematical functions (`cv_mul`'s "exact v3 lane"
message, `build_collapsed_side`'s "D43-v3-" log tag) are retained
byte-for-byte and disclosed rather than renamed.

## The five repairs (Opus 5 R1-R5, all implemented and fixture-tested)

1. **R1 - value-binding terminal** (`job_contract_v4.py::bind_candidate`,
   `decide_terminal`, `load_candidate`).  The terminal authority now
   recomputes or binds every payload-bearing candidate field:

   | Field | Treatment |
   |---|---|
   | `run_nonce` | recomputed from the lease under a fresh-descriptor held-flock probe |
   | `lease_sha256` | rehash of `RUN_LEASE.json` |
   | (lease) `registration_sha256` | rehash of `records/REGISTERED.json` |
   | `manifest_sha256` | rehash + schema check of the manifest file |
   | `claim_boundary` | equality with the rehashed manifest + null-shape check (only the E5/E6 note may be non-null) |
   | `preflight_receipt_sha256` | rehash + `pass`/authority/manifest crosscheck |
   | `pilot_gate_sha256` | rehash + status/nonce/manifest crosscheck |
   | `merge_receipt_sha256` | rehash + schema/status/nonce/lease/manifest/preflight/pilot/payload-name contract |
   | `merge_payload_sha256` | rehash of the payload bytes + receipt crosscheck |
   | `semantic_sha256` | receipt-crossbound under the rehashed merge receipt (producer recomputed it from the rows at finalize; the contract does not unpickle payloads) |
   | `template_bridge_sha256` | receipt-crossbound under the rehashed merge receipt |
   | `exact_inventory` | contract-checked (non-bool ints, 29+155=184, bands {20:10, 30:9, 40:10}, tail degree <= 2, 155 distinct zero targets, exact key census) + receipt-crossbound |

   `load_candidate` enforces the exact 15-key candidate census (missing
   and extra keys alike refuse).  The terminal records per-field
   provenance (`RECOMPUTED_SHA256:...` / `RECEIPT_CROSSBOUND:...` /
   `BOUND_TO_REHASHED_MANIFEST...`) plus a `binding_failures` map; there
   is no unexplained copied digest.  Twelve named binding gates join the
   gate set; the fabricated candidate that reached the v3 positive
   terminal now fails `candidate_lease_digest_bound`,
   `candidate_inventory_contract`, and `archive_sidecar_bound`.
2. **R2 - sidecar archive binding** (`verify_sidecar_archive`).  The
   archive named by the sidecar is resolved relative to the sidecar via
   `safe_relative`, must equal `<job_tag>.terminal.tar.gz`, must be a
   regular non-symlink file, and is rehashed; the terminal's
   `terminal_archive_sha256` is that rehash.  Dangling, drifted,
   foreign-name, and traversal sidecars refuse through
   `archive_sidecar_bound`.
3. **R3 - full-member-set archive census**
   (`extract_and_verify_archive`).  Every non-regular member - directory,
   symlink, hardlink, device, FIFO - is refused outright
   (`ARCHIVE_NONREGULAR_MEMBER`), and exact FULL-member-set equality
   against the embedded manifest (`ARCHIVE_MEMBER_CENSUS_DRIFT`) replaces
   the v3 regular-files-only census.  The extra-directory and
   nested-directory-chain members Opus 5 showed were ACCEPTED in v3 are
   now refused.
4. **R4 - real censuses, no copied gates.**  The launcher starts the
   supervisor under `setsid --wait` in **both** containment modes
   (`setsid` is now a hard requirement before mode selection), the
   containment identity gate requires `sid == pgid == $$` in both, and
   the final census pgid is `$$` unconditionally - the v3
   `cleanup_pgid=0` lane is gone.  The terminal takes mandatory
   `--cleanup-pgid` and `--boundary-mode`, refuses `pgid <= 1`
   (`pgid_census_real`), and refuses mode-inconsistent cgroup values
   (`cgroup_gate_mode_consistent`).  In the fallback the cgroup gate is
   recorded as the string `NOT_APPLICABLE` - never a copied boolean - and
   `gate_provenance` names each gate's evidence source.  Positivity
   accepts only `true` or a mode-legal `NOT_APPLICABLE`.
5. **R5 - authority-bearing launcher post-mortem** (`postmortem-gate`
   subcommand + launcher step 8).  A positive (or unreadable, fail
   closed) terminal paired with a non-zero post-mortem census rc, a
   non-empty census, or a missing census file emits an immutable 0444
   `TERMINAL_POSTMORTEM_FAULT.json` (O_EXCL; the first fault object wins
   and is never overwritten) carrying the terminal digest and the census
   evidence, and the launcher exits 78.  The terminal is never modified;
   its `post_boundary_contract` block names the fault object, its
   location outside the sealed terminal archive, and the voiding rule.
   The launcher post-mortem census now uses the session-leader pgid read
   from `custody/containment_identity.json`, and the fallback
   `kill_boundary` kills that real leader's group (the v3 `-$!` kill
   targeted the setsid wrapper's group).

## Bounded tests executed (macOS, no CAS, no AWS)

* `test_job_contract_v4.py`: **45/45 PASS** (~8 s).  Retains every v3
  fixture intent (duplicate flock, lease forgeries, stale namespace,
  proc/tag/cgroup censuses, kill-tree, monitor latches, archive
  determinism/replay/unsafe members, 22 single-latch flips, shape
  forgeries, omitted/malformed arguments, `python -O` refusal incl. the
  v2 forged-receipt fixture with pinned refusal reasons) and adds the
  commissioned negative controls: value forgery of each of the 8 digest
  fields through its named gate; impossible/bool/string inventories;
  claim-boundary promotion/drop; candidate and artifact mutation after
  producer exit; semantic-receipt mutation retaining valid hex (both the
  rehash-refused and the coordinated crossbind-refused variants);
  dangling/drifted/foreign/traversal sidecars; registration drift;
  vacuous pgid (0/1/-1); copied cgroup gates in both directions;
  fallback `NOT_APPLICABLE` recording; directory and nested-directory
  archive members; post-mortem fault emission, immutability,
  non-overwrite, fail-closed unreadable-terminal handling; `-O` refusal
  of the `terminal` and `postmortem-gate` subcommands.  The happy-path
  fixture is honest: every candidate digest is the real digest of a real
  artifact and the sidecar names a real rehashable archive.
* `test_selected_rows_v4.py`: **21/21 PASS** (~14 s).  Carries the full
  v2/v3 mathematical surface (432-basis scope, literal collapse and sign
  mutations, EB refusal, collapse-before-multiplication, exact D21-prefix
  B-block and collapsed-engine regressions, selected-component
  commutation, literal gate + mutation refusal through the actual gate,
  template bridge symbolic + both registered modular points, 29/155
  inventory, 184 cover, lease/registration refusals, zero-assert census,
  terminal-writer census) plus `test_v4_repair_wiring_census` (static
  census of all five shell-lane repairs) and
  `test_v2_v3_v4_math_function_diff_closed` (pinned diff-closure replay
  including byte-identical report regeneration).
* `math_function_diff_v4.py`: PASS + deterministic report regeneration.
* `build_source_archive_v4.py` twice (each run builds twice out-of-tree):
  identical outer digest
  `9051a3dbfc4d6d8714a6ee3ca53e84517bcadddfab4fc49baf480d65f0dd31ba`,
  20-member census, fresh-extraction replay 20/20, members byte-identical
  to the live tree, zero self-reference, sidecar `sha256 -c` replay.
* `bash -n` on supervisor and launcher; `py_compile` on all Python.

## Residual limitations

* **No live-Linux execution** (unchanged, disclosed by v3 and confirmed
  by Opus 5).  `/proc`, cgroup v2, systemd scopes, `setsid` (including
  the new systemd-mode `setsid` wrapper and its session-leadership
  identity gate), `sha256sum`, prlimit/taskset/timeout chains, and
  IMDSv2 are exercised via injected-reader fixtures and source reading
  only.  The first AWS action after a hostile PASS and coordinator GO
  must be staging plus a lease/containment/preflight rehearsal on the
  registered idle host, explicitly verifying `ps -o sid=,pgid= -p $$`
  leadership inside a real systemd scope, before any heavy stage.
* The terminal binds every candidate field to on-disk artifacts, but a
  coordinated rewrite of the candidate **plus** every referenced artifact
  after producer exit is excluded operationally (empty PGID/JOB_TAG/
  cgroup censuses, the authority-bearing post-mortem, and the one-shot
  lease), not cryptographically; the contract does not recompute semantic
  digests from the row payloads.  Recorded provenance makes this boundary
  explicit per field.
* The 29/155 inventory remains a preregistered forecast that the run can
  only confirm or refuse, never measure (Opus 5 section 2 scoping,
  section 8 narrowing 1); no v4 rows exist.

## Claim tiers (unchanged)

1. A successful reviewed run establishes an exact support-specialized
   a00pp emitter **reproducing the preregistered** 29/155 inventory of
   the finite 184-row raw-J truncation.
2. A later exact solve plus mandatory literal E5/E6 reconstruction replay
   establishes only the displayed finite E5/E6/unit extension.
3. Full residue-A/template membership requires every other applicable
   equation.
4. NF equivalence, all-depth compatibility, a Keller map, and a JC2
   counterexample remain separate and unproved.

## Remaining blockers

* a fresh independent different-model hostile-review PASS of this v4
  seal;
* coordinator GO;
* fresh immutable registration binding manifest, source list, archive,
  and launcher digests on an idle isolated <=1 TiB zero-swap EC2 host;
* a live-Linux staging rehearsal of the lease/containment/session-
  leadership path before the heavy stages.

**No AWS launch is authorized by this packet.**
