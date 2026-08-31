# Systems custody-hardening software review

## Scope and input verification

Review scope is limited to the five charged frozen inputs. I did not inspect
`jc2-lean`. Before reading source, I recomputed SHA-256 for every frozen file;
all five digests matched the values in the charge exactly:

| Frozen input | Verified SHA-256 |
|---|---|
| `lane.sh` | `2a48df3188b931832511bccf0c192a18f2dedffacdbfd85e5d80304c5e24b0d7` |
| `seal.py` | `3096dc47ca24eee147207f6d0e8a8a98095e97ada161c014cc6a27577cd69df3` |
| `lane_detach.py` | `310b33b4ef8d9ba3f01c702405338a387b6654aa8fba62579eb0070e84ad9e3c` |
| `test_lane_fallacy.py` | `fb8c8ef9fa062110b95296f42878b2c9200c4f9166813f9b911029420c26859c` |
| `test_seal.py` | `5b7ec2b6a76410429d982441fedca2de3cd99cd67055ab96a9f1346d37298106` |

This is a hostile systems review of the claimed custody properties, not a
mathematical review. Line references below are to these frozen copies.

## Executive assessment

The implementation is **not safe to use as receipt-backed custody evidence**.
It does preserve ordinary, quiescent outputs, and several boundary cases are
handled carefully, but hostile or merely concurrent execution breaks the core
claim. In particular, excluded files can enter the charged snapshot through
lexical aliases; the sandbox does not prevent a lane from reading the mutable
originals; noncanonical bytes after an otherwise valid seal are called
`CLEAN_SEALED`; detached status trusts files the lane can alter; and receipt
writes are neither checked nor committed atomically. Several of those defects
permit a terminal-looking status or `report_state=BODY_SEALED` while the bytes
on disk do not satisfy the claimed boundary.

I use **BLOCKER** for a path that can admit forbidden/unaccounted bytes or make
custody state materially false, **MAJOR** for a violated hardening contract or
non-atomic failure that normally fails visibly, and **MINOR** for narrower
portability or recovery weaknesses.

## Findings

Related race variants are grouped where they need the same fix.

## Divert boundary and filesystem behavior

### D1 — BLOCKER: arbitrary post-seal bytes are accepted as `CLEAN_SEALED`

**Lines:** `seal.py:227-255, 411-419`; `lane.sh:419-428`.

`verify_bytes` looks for one matching bytes/hash/basis declaration but never
requires the post-marker bytes to equal the canonical seal and never rejects
unmatched prefix or suffix text. Therefore a valid seal followed by, for
example, `503 upstream timeout\n` verifies; `divert_path` returns
`CLEAN_SEALED`, creates neither raw nor overflow artifact, and `lane.sh` writes
`report_state=BODY_SEALED`. I confirmed this behavior directly against the
frozen module. This defeats the stated purpose of banking transient provider
errors.

**Minimal fix:** after extracting the basis, compare the complete tail against
one explicitly supported canonical serialization (with a deliberate CRLF
policy); any extra byte must take the `DIVERTED` path. Add a sealed-plus-suffix
test. `test_seal.py:281-289` covers only a seal with no suffix—and its helper's
free-form “Body definition” demonstrates that the alleged canonical form is
not currently enforced.

### D2 — MAJOR: an unterminated EOF marker produces contradictory custody state

**Lines:** `seal.py:200-217, 395-410`; `lane.sh:425-428`.

`divert` calls marker detection with `require_newline=False`, so a report ending
in the marker bytes with no newline is `CLEAN` and becomes `BODY_SEALED`.
The same file is rejected by `verify`/`stamp`, whose body definition requires
the marker's terminating newline. Thus “sealed” is not a stable predicate even
within this tool.

**Minimal fix:** require LF or CRLF in `divert`, or return a distinct
`UNTERMINATED_MARKER` contract failure and map it to rc 7. The verify test at
`test_seal.py:87-97` rejects this input, but no `DivertTest` exercises it, so it
would not catch the contradictory `report_state`.

### D3 — MAJOR: diversion is not failure-atomic or durably committed

**Lines:** `seal.py:357-378, 428-466`; `test_seal.py:331-339`.

Final sidecar names are created and written directly. Raw is published first,
then overflow, then the report is atomically replaced. If overflow already
exists, the command returns failure but leaves a newly created raw file. The
existing test constructs exactly that case yet omits
`assertFalse(raw.exists())`. Disk-full or SIGKILL can leave a read-only,
partially written final sidecar; a kill after report replacement leaves a
truncated report and a still-`RUNNING` receipt. Directory-fsync errors are also
silently discarded at lines 373-375 and 463-465. A same-tag retry is then
refused by `lane.sh:101-107`.

There is also a data-loss race at `seal.py:452-456`: bytes appended after the
last comparison but before replacement are in neither the saved raw bytes nor
overflow and are discarded. Early `CLEAN`/`CLEAN_SEALED` returns similarly do
not revalidate the path after classification.

**Minimal fix:** require writer quiescence/cooperative locking, stage and fsync
all artifacts under temporary names, publish a transaction manifest last, and
make recovery idempotent. Clean artifacts created by any pre-commit failure;
surface directory-sync failure as a typed non-success as `stamp` already does.

### Boundary audit (not additional findings)

- LF and CRLF marker lines are byte-accounted correctly, including both CRLF
  bytes. `test_seal.py:134-147` covers CRLF verification, but not CRLF divert.
- Every exact standalone marker counts even inside a Markdown code fence. Two
  such lines yield `MULTI_MARKER`; this conservative byte rule is consistent
  with the stated format, but the fenced case is untested.
- Multiple ordinary markers are left untouched and reported, covered by
  `test_seal.py:309-329`; lane-level rc/state mapping is not covered.
- Inline mentions and marker lines with extra spaces do not count, as intended.

## Snapshot, path validation, and launch custody

### S1 — BLOCKER: charged-path exclusion is bypassable before the sandbox

**Lines:** `lane.sh:228-287`; `test_lane_fallacy.py:399-440`.

The check is lexical, case-sensitive, and applies `-L` only to the final
component. All of these pass validation and are then opened by hash/copy before
Seatbelt starts:

- `charged_input=./jc2-lean/secret.md` (the exclusion pattern does not match);
- `charged_input=JC2-LEAN/secret.md` on case-insensitive APFS;
- `charged_input=refs/alias/secret.md` where `alias` is a symlink to the
  excluded tree or anywhere outside the repository.

There is also a check/open race: a regular leaf can be swapped to a symlink
after lines 263-267 and retained through the separate hash and `cp` opens at
274-275. The copied bytes can therefore come from an excluded or external
inode. The existing tests cover only literal lowercase `jc2-lean/...` and a
literal `..` component. They would catch none of these scenarios.

The purported ASCII check is locale-dependent shell pattern matching. Under
`en_US.UTF-8` on this host, characters including `é`, `ø`, and `å` collate
inside `[A-Za-z]` and pass lines 244-255. Absolute paths and consecutive `..`
are rejected. Sequential ASCII case-only basename collisions are noticed by
`-e` on default case-insensitive APFS, but uniqueness is not normalized by the
code and therefore changes on case-sensitive APFS.

**Minimal fix:** byte-validate under a forced `LC_ALL=C`; reject `.` as well as
`..` components; case-fold the excluded name and basename uniqueness key; and
walk from an opened repository dirfd with `openat`/`O_NOFOLLOW`, rejecting every
symlink component. Hash and copy from that one opened regular-file descriptor.

### S2 — BLOCKER: the model can read mutable originals after they are frozen

**Lines:** `lane.sh:263-310, 318-327, 500-518`.

The profile is `allow default`. It protects the snapshot from writes, but does
not deny reads of `$repo_root/$charged_rel`; the original declaration and path
also remain in the delivered prompt. A source can change after snapshot, then
the model can deliberately read the changed repository path rather than
`{{LANE_INPUTS}}`. The receipt records `REPO_DRIFT` while the comment at
500-501 assumes, without enforcement, that “the model read frozen bytes.” A
hash proves which snapshot was offered, not which bytes were consumed.

**Minimal fix:** run the provider with a read allowlist rooted in immutable
custody and explicitly required runtime/configuration paths, or at least deny
every charged original and alias. Publish only the snapshot locations in the
model prompt. Add a test whose adapter successfully tries both the snapshot and
the original after drift; the latter must be denied. The current drift test at
`test_lane_fallacy.py:367-397` reads only the snapshot.

### S3 — BLOCKER: executed adapter and verification tools are mutable provenance

**Lines:** `lane.sh:62-65, 87-99, 174-179, 375-380, 413-483`;
`lane_detach.py:51-64, 225-229, 437-480`.

Unlike the prompt, seal tool, and validator, the adapter is hashed at line 175
but executed later from its live pathname. Replace it after hashing, execute
the replacement, and restore it before line 477: the final receipt claims the
original adapter digest. Detached launch adds a longer path-check/hash/launchd
reopen window.

Security-critical `python3`, SHA tools, and `sh` are also resolved repeatedly
from inherited `PATH`, which detach deliberately forwards. A hostile adapter
can write a fake `python3` or `sha256sum` into an earlier writable PATH
directory before it exits. The parent can then accept a fake `status=CLEAN` or
arbitrary digest text (the digest is not validated as 64 hex), producing a
successful false receipt.

**Minimal fix:** snapshot the adapter through one no-follow fd and execute that
immutable copy; pin and attest absolute system interpreters/tools in a sanitized
environment (prefer one trusted supervisor implementation); and validate every
digest's syntax. Add adapter ABA and poisoned-PATH tests. No current test
mutates the adapter or parent toolchain.

### S4 — MAJOR: report-path launch validation is only a substring test

**Lines:** `lane.sh:214-219`; `test_lane_fallacy.py:357-365`.

A prompt saying only “write `xmodel/tag.md.bak`”, quoting the path as a code
example, or explicitly saying not to write it passes `grep -F`. The promised
exact report-path contract is therefore not established before an expensive
launch; the lane later fails only if no report happens to appear.

**Minimal fix:** require one machine-readable declaration such as
`report_path=xmodel/<tag>.md` and parse it exactly. Add `.md.bak`, prefix,
negation, duplicate, CRLF, and code-example negatives; the existing test covers
only total absence.

### S5 — MAJOR: contract violations do not consistently return rc 7

**Lines:** `lane.sh:216-219, 239-280, 433-455`;
`test_lane_fallacy.py:357-365, 399-440, 498-516`.

Missing report-path and charged-input violations exit 2, and their tests
explicitly require 2. Post-run missing/multiple-marker violations become 7
only when the adapter had returned zero; an adapter rc 1 plus a markerless
declared-contract report remains rc 1. This contradicts the stated typed rc 7
contract and prevents reliable orchestration by failure class.

**Minimal fix:** route every hardening-contract failure through one `exit 7`
path and make boundary violations override/preserve the provider result in a
separate receipt field. Update the tests to require 7, including a nonzero
adapter plus malformed report.

### S6 — MAJOR: output creation follows dangling symlinks and mutable parents

**Lines:** `lane.sh:84-107, 335-382`; `seal.py:52-78`.

`mkdir -p` accepts symlinked `xmodel`/`.lane-locks`; `[ -e ]` misses dangling
symlinks; and shell `>`/`>>` follows them. A dangling
`xmodel/tag.run.v2 -> /chosen/path` passes duplicate detection and causes the
receipt to be created outside `xmodel`; log creation has the same defect.
`seal.py` resolves parent symlinks before checking them, so its apparent
parent-symlink rejection sees only the canonical target. Retargeting the
lexical parent can make emitted paths name different bytes.

**Minimal fix:** reject symlinks in every directory component, open trusted
directories once, and create all outputs with anchored
`O_EXCL|O_NOFOLLOW`. Keep and verify their inode identities through final
commit. Add dangling-final, symlink-parent, and parent-retarget tests; the seal
symlink test at `test_seal.py:238-246` covers only the final component.

## Receipts and detach lifecycle

### R1 — BLOCKER: the provider can alter other lanes' permanent evidence

**Lines:** `lane.sh:318-327, 375-380`;
`test_lane_fallacy.py:264-278`.

Seatbelt allows all writes except the excluded tree, custody temp, and the
current run file. A provider in lane A may overwrite any prior report,
`.run.v2`, raw, overflow, or log; delete/rename the `xmodel` parent; or pre-seed
future-tag symlinks. Mode 400 is no defense against unlink/replacement by the
same owner in a writable directory. The test probes only a direct overwrite of
the current receipt and therefore gives false confidence about the evidence
store as a whole.

**Minimal fix:** the provider must write only inside a fresh per-run staging
directory. Deny all provider writes to permanent `xmodel`, `.lane-jobs`, and
lock state; after provider teardown, let the trusted parent validate and
atomically publish report, log, sidecars, and receipt. Test writes to a prior
and predicted-future tag plus parent-directory rename.

### R2 — BLOCKER: a background descendant makes `report_state` false

**Lines:** `lane.sh:375-384, 399-457, 521-566`;
`lane_detach.py:447-450`.

The wrapper waits only for the direct `sandbox-exec` PID. An adapter can write a
clean marked report, start a delayed background writer, and exit. While the
wrapper seals and finalizes, that descendant still has permission to rewrite
the report. It can act after `CLEAN` but before line 545, yielding one receipt
with `report_state=BODY_SEALED`, `final_status=DONE`, and a hash of markerless
bytes; acting after line 545 instead leaves a stale hash. A child that creates a
new session/process group can survive launchd's same-process-group cleanup too.
This also makes the final compare/replace race in D3 exploitable.

**Minimal fix:** contain the provider in a dedicated killable job/process
group, prevent daemonization or enumerate and reap every descendant, and prove
the writer set empty before validation. Only then publish provider staging into
a write-denied evidence directory. No current fake adapter backgrounds a
writer, so the clean/divert receipt tests cannot catch this.

### R3 — BLOCKER: the lane can forge detached supervisor state

**Lines:** `lane.sh:318-327`; `lane_detach.py:232-274, 293-305,
595-630`.

The sandbox permits writes to `.lane-jobs`. A still-running lane can create
`.lane-jobs/<tag>/unloaded.v1.json`; `parse_launchd` trusts mere existence and
returns `UNLOADED` without querying launchd. `unload` then skips `bootout` and
prints success while the lane remains live. The lane can also unlink and
replace `launch.v1.json`; `load_record` does not recompute the canonical label
or domain or verify the recorded file hashes.

**Minimal fix:** place supervisor state outside provider reach and anchor every
open; validate label/domain and content digests. An unload marker must be a
validated record installed only after confirmed successful `bootout`, and
status must still confirm service absence. There are no detach tests; the
current receipt-write test does not touch this plane.

### R4 — BLOCKER: a successful process can leave a missing/torn/fabricated receipt

**Lines:** `lane.sh:283-284, 335-373, 382, 521-569`;
`lane_detach.py:348-360, 525-549`.

The input-manifest append, initial receipt block, child-PID append, and terminal
receipt append are unchecked. They are direct writes to the authoritative
pathname, with no fsynced atomic commit. ENOSPC or a write/permission failure
can leave a receipt at `initial_status=RUNNING` (or no receipt), yet line 569
still exits with the provider's zero and launchd reports `SUCCEEDED`.

The line format is injectable too. Prompt paths are not CR/LF validated but are
emitted raw at line 342; a legal filename containing
`\nfinal_status=DONE` plants that key in the initial receipt. If the lane then
dies before finalization, a consumer can see a fabricated terminal field;
duplicate-key parsers can disagree after finalization.

**Minimal fix:** use a structured, duplicate-rejecting encoding; reject control
characters; build a complete terminal receipt in a staged file, fsync it and
the directory, then atomically install it. Any publication/hash failure must
force non-success. Add ENOSPC/short-write/kill and newline-filename tests.

### R5 — MAJOR: detached status treats brittle heuristics as process truth

**Lines:** `lane_detach.py:281-363, 479-513, 525-558`.

The parser regexes human-readable `launchctl print` output—explicitly not a
stable API—and ignores terminating-signal/terminal-state variants. An inactive
signal-killed job without the exact `last exit code = N` line becomes
`STARTING` forever. If `launchctl print` fails, unauthenticated `pgrep -f`
matching argv is promoted to `RUNNING` with a PID; an unrelated process can
spoof it. Conversely, `command_launch` returns zero and prints the supervision
reassurance even if its immediate parsed state is `MISSING_JOB`.

**Minimal fix:** represent parse/visibility uncertainty as `UNKNOWN`, never as
`RUNNING`, `STARTING`, or terminal success; bind a PID to uid, start time,
executable, and launchd job identity; handle signal termination; and require a
confirmed post-bootstrap state before returning success. Use mocked output for
format variants, stale/dead PID, argv spoofing, and bootstrap timeout.

### R6 — MAJOR: cancellation and supervisor setup are not failure-atomic

**Lines:** `lane.sh:122-155, 250-287, 386-397`;
`lane_detach.py:172-181, 414-477, 561-575`.

A TERM/HUP/INT during pre-launch preparation sets `caught_signal` while
`child_pid` is empty, then the script can continue and launch the lane anyway;
it labels the result cancelled only after the provider finishes. SIGKILL after
lock creation leaves a stale lock and partial temp snapshot because traps
cannot run. Detached `write_exclusive` similarly exposes final JSON names while
writing: kill/ENOSPC leaves a corrupt tag directory that blocks retry, and one
corrupt valid-tag record makes `iter_records` abort listing every other active
lane.

**Minimal fix:** make traps phase-aware and abort before spawn; use a bounded
whole-group TERM/KILL protocol; give locks recoverable owner/start identity;
and stage/fsync/rename supervisor records. Listing should emit a typed
`CORRUPT` entry and continue. Existing cleanup tests exercise catchable normal
exits only; there are no signal, kill-mid-write, or corrupt-list tests.

## Test-suite coverage

The most consequential gaps are not redundant with existing tests:

| Untested edge/regression | Would an existing test catch it? |
|---|---|
| Valid seal plus one provider-error byte remains `CLEAN_SEALED` | No. `test_seal.py:281-289` has no suffix and accepts a noncanonical fixture. |
| EOF marker without newline becomes lane `BODY_SEALED` | No. `test_seal.py:87-97` catches verifier acceptance, not divert/lane acceptance. |
| CRLF divert body/overflow byte boundary | No. `test_seal.py:134-147` covers verify only. |
| Standalone marker inside a code fence; second marker at unterminated EOF | No. Inline and ordinary-double-marker tests do not exercise either. |
| Non-UTF-8 overflow is banked byte-exactly | No. `test_seal.py:248-252` checks verifier rejection only. |
| Occupied overflow leaves a raw artifact after failure | No. `test_seal.py:331-339` creates the defect but never asserts raw absence. |
| Kill/ENOSPC/fsync failure during raw, overflow, report, receipt, or supervisor sidecar commit | No. Stamp-only mocks do not cover divert/receipt/detach transactions. |
| `./jc2-lean`, uppercase APFS alias, ancestor symlink, leaf swap, absolute input, Unicode locale, or case-folded basename pair | No. `test_lane_fallacy.py:399-440` covers literal lowercase exclusion, missing file, and literal `..` only. |
| Model reads drifted original instead of snapshot | No. `test_lane_fallacy.py:367-397` asks it to read only the snapshot. |
| `.md.bak`/negated report-path mention | No. `test_lane_fallacy.py:357-365` tests total absence only. |
| Provider writes prior/future custody files or renames their parent | No. `test_lane_fallacy.py:264-278` probes only the current run-file pathname. |
| Background writer changes report after boundary classification | No adapter in the suite backgrounds or daemonizes. |
| Adapter ABA replacement or provider-poisoned `PATH` | No executable/tool provenance test exists. |
| Contract violation following provider rc nonzero | No. The marker test uses provider rc 0; launch-contract tests actually entrench rc 2. |
| Same-tag concurrent detach, forged unload marker, corrupt sidecar, launchd format variants, dead/spoofed PID, bootstrap uncertainty | No charged test imports or invokes `lane_detach.py` at all. |

One positive result: under cooperative state, atomic creation of
`.lane-jobs/<tag>` followed by the lane lock makes an ordinary same-tag race
unlikely to double-start the adapter. That protection is not sufficient in the
actual threat model because the provider can mutate both supervisor/lock
namespaces, and setup/kill recovery is not transactional.

## Verdict

**UNSOUND** for the campaign's reliance on receipts as custody evidence.

The conclusion does not depend on speculative power-loss behavior: S1 admits
forbidden input bytes, D1 affirmatively misclassifies provider overflow, R1 and
R3 let the provider alter the evidence/control planes, and R2 constructs a
completed receipt whose boundary state disagrees with its own report bytes.
Any one defeats promotion.

Promotion requires, at minimum: provider-only staging with no write access to
persistent evidence or supervisor state; component-safe no-follow snapshots
and enforced use of them; frozen adapter plus trusted post-processing tools;
writer quiescence; exact and transactionally durable diversion; and an atomic,
structured terminal receipt. The new tests must exercise hostile paths,
concurrency, signals, and launchd uncertainty—not only cooperative fixtures.

<!-- BODY-END -->
