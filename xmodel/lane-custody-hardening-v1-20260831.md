# LANE-CUSTODY-HARDENING/v1 — immutable charged inputs and truncation-not-loss

- Author: Fable 5 coordinator session (interactive, DC present), 2026-08-31.
- Status: `INTERNAL` implemented software; different-model hostile review
  queued and nonblocking. No mathematical claim is made by this packet.
- Basis at implementation start: campaign content `ec0227b3`, whole-tree
  `d7a2aefc`. Human authorization: DC standing authority confirmed in session,
  including the explicit directive that overflowed output caps and transient
  provider errors must yield truncated banked output, never lost output.

## Motivation

Four external lanes in the preceding ~48 h failed on delivery, not
mathematics: a Grok review quarantined for 274 non-whitespace bytes after
`BODY-END`; a GPT-5.5 review whose analysis lived only in its log
(`report=MISSING`); a Fable review killed by the 64k output cap with no
report; a Fable exit-4/no-report attempt. Separately, two earlier reviews
failed closed because their declared source bases changed during execution.
This packet closes both classes: frozen charged inputs at launch, and
deterministic salvage of every byte a model produced.

## Changes

### `ops/lane.sh` (launcher; focused regression required and performed)

1. **Immutable charged-input snapshots.** Prompt lines
   `charged_input=<repo-relative-path>` are frozen into the lane's
   write-denied custody directory before launch (mode 400, Seatbelt-covered),
   and every literal `{{LANE_INPUTS}}` in the composed model prompt is
   rewritten to that frozen directory, so the model reads pinned bytes no
   matter how the repo moves. Declarations and placeholder must appear
   together; paths must be repo-relative, regular, non-symlink, outside the
   excluded tree, with unique basenames; any violation refuses launch
   (exit 2). Receipts record per-input path, basename, SHA-256, and a
   post-run disposition: `UNCHANGED`, `REPO_DRIFT` (recorded, NOT a
   quarantine — the model read frozen bytes; originals are recoverable from
   the recorded `basis` commit), or `SNAPSHOT_MUTATED` (quarantine, rc=5).
2. **Report-path contract at launch.** A prompt that does not contain the
   literal mandated report path `xmodel/<tag>.md` is refused (exit 2),
   mechanizing the existing protocol rule that killed two lanes when honored
   only by hand.
3. **BODY-END divert — truncation, not loss.** Post-run, the launcher runs
   the snapshotted `ops/seal.py divert` on any nonempty report. A sole
   standalone `<!-- BODY-END -->` with non-whitespace overflow no longer
   quarantines the review: the untouched original is banked at
   `xmodel/<tag>.raw.md`, the exact overflow bytes at `xmodel/<tag>.overflow`
   (both hashed in the receipt), and the charged report is atomically
   truncated to its body. Reports that are clean, or carry a valid canonical
   seal, are untouched. Zero markers under a prompt-declared BODY-END
   contract bank the partial draft and fail closed (rc=7,
   `report_state=PARTIAL_NO_MARKER`); multiple markers are never repaired
   (rc=7, `AMBIGUOUS_MULTI_MARKER`).
4. **Seal tool pinned like the validator.** `ops/seal.py` is snapshotted,
   hash-recorded pre/post, and any mutation during the run quarantines the
   result (rc=5).
5. New receipt fields (schema stays 2, additive; consumers parse by key):
   `seal_tool`, `seal_tool_sha256`, `body_end_contract`, `charged_inputs`,
   `lane_inputs_dir`, `charged_input_<i>{,_basename,_sha256,_post}`,
   `post_seal_tool{,_snapshot}_sha256`, `seal_boundary`, `report_state`,
   `raw_report{,_sha256}`, `overflow{,_sha256}`. Duplicate-tag preflight now
   also covers `<tag>.raw.md` and `<tag>.overflow`.

### `ops/seal.py`

New `divert` subcommand and `divert_path()`/`_write_exclusive()` helpers with
the same anchored-parent, exclusive-create, atomic-replace discipline as
`stamp`. `_body_boundary` is refactored over `_marker_boundaries` with
byte-identical strict behavior for `verify`/`stamp`.

### Prompt contract (for all new lane prompts, enforced where mechanical)

Name the mandated report path (now launch-enforced); instruct one standalone
`<!-- BODY-END -->` terminator (its presence in the prompt arms the marker
contract); instruct the model to write the report incrementally section by
section, never only at the end, so caps and provider kills leave a banked
`PARTIAL_NO_MARKER` draft; declare frozen inputs via `charged_input=` +
`{{LANE_INPUTS}}` for every file whose exact bytes the lane must read.

## Evidence

- `ops/test_lane_fallacy.py`: 7 prior tests preserved (harness split into
  `LaneHarness`; prompt updated to satisfy the new report-path contract) plus
  7 new: repo-drift immunity with frozen-byte readback, five fail-closed
  contract cases, overflow divert with exact hashes, clean-marker pass,
  contract-partial rc=7, no-contract informational, refused pathless prompt.
- `ops/test_seal.py`: 6 new divert tests (clean, canonical-seal untouched,
  exact-hash divert, zero/multi markers unrepaired, exclusive-create refusal,
  `-O` parity).
- Full ops suite: 92 tests pass under ordinary Python, `-O`, and `-OO`
  (79 prior + 13 new). Baseline note: the banked 79-count was reproduced only
  after restoring `sympy` for Homebrew Python 3.14 (user-site install; the
  interpreter bump had emptied site-packages and silently reduced discovery
  to 77 with one loader error).
- Flake note: two of nine full-suite runs failed with one unnamed failure
  that did not recur under captured output (suspected launchd-timing
  sensitivity in `test_lane_detach`, which predates this change and is
  untouched by it); seven consecutive final runs are green, including all
  focused lane/seal runs. Watch and bank the name if it recurs.

## Limitations

- `divert` charges everything above the sole marker; it cannot detect a
  model that placed the marker deliberately early. Hostile review remains the
  semantic gate.
- Charged-input freezing binds only files declared by the prompt author;
  undeclared reads still see the live repo. Reviews must keep declaring
  complete packets.
- The `REPO_DRIFT` disposition assumes drifted originals are recoverable
  from git via the recorded basis; snapshots are custody-temporary and are
  removed with the lane directory.
- `run_schema` stays 2 with additive keys; nothing validates the new keys'
  absence in old receipts.

<!-- BODY-END -->
