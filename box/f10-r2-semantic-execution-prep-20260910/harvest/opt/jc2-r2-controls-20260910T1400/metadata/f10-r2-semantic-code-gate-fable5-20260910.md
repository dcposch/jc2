# f10-r2 semantic code gate (Fable 5.1, 2026-09-10)

FIRST combined different-model source gate: mutator (controls 6/10) + runtime dispatcher. Reviewer Fable 5.1; producer Astra; executor ROOT/Astra.
Lane start 2026-09-10 13:33:58 UTC; deadline min(13:51:58, 13:52:00) UTC; publication reserve final 3 min.
Status: UNSEALED skeleton. Method: hashes, whole text reads, manual reasoning only. No subprocess/import/compile/test/CAS/network/git.

## Custody (12 frozen inputs, sha256 generated from sha256sum)

| sha256 | basename |
|---|---|
| edd4c71e86d0d5cac2ee277de69199522a2a5bca9381833f19dc078e9759ea19 | CONTRACT.md |
| 17cab2767468f01c1f8ede32a1adbd1f1b608cce88fcbdc4a9c992ab89c05535 | DISABLED-REGISTRATION.json |
| 2a274ac4cf866762bc1f2734b3af8d515ff7be93c0fe0d4500e56dbca2ef093b | authority.py |
| e6bc7cca0d9c776a898bda3f0648af883e17a675f2b81bba52031459f4c640a0 | check.py |
| e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e | check_arithmetic.py |
| 183b63fbf0f75a87f8073815e27e083e741c08ce0e749bf7f64fa99b66b9f25a | dispatch.diff |
| 6c232bb0d1b4ee62fefb62970b1b5a06a092db735cbd6fb47907c54921169c0b | dispatch.py |
| 3bce51215a7c746acb4bd5bc833f2644e5f2b1ac89e8681cdea2c65dfba00b0c | f10-r2-actual-result-gate-fable5-20260910.md |
| 3e9a06cf3aced19aa6a8ab5c742c57ffc1d1da21bb8a0270030a83285720502b | f10-r2-reconstruction-code-gate-fable5-20260910.md |
| 558fa2f1ef15b8477148fc014df4dcbcf783b61bcddae9889213b995bcb86e16 | f10-r2-runtime-gate-fable5-20260910.md |
| a896a8094be9b38f7ffa3a82cab15d340add0d7ab5f513340b2b7f916e489540 | mutate_controls.py |
| 1e3bea3ad995ca64780f77b33792ed09c9843fb3925aae5f64c7a2abcaa0ecde | probe.py |

All 12 match the charged expected pins. Owned outputs verified ABSENT at 13:33:58 UTC before this skeleton.

## Prior involvement disclosure

The three imported prior gates (runtime, reconstruction-code, actual-result) are Fable 5.1 authored: same model as this reviewer. They are imported at their exact stated scope only. check.py / check_arithmetic.py / authority.py are same-byte WHOLE reuse of the accepted reconstruction sources and are re-read here whole, not re-audited mathematically.

<!-- SECTIONS-BEGIN -->

## Read scope

Whole reads at 13:34-13:36 UTC: mutate_controls.py (306 lines), dispatch.py (673, three bounded reads), dispatch.diff (363), CONTRACT.md (131), DISABLED-REGISTRATION.json (31), probe.py (68), authority.py (77), check.py (416, two bounded reads), check_arithmetic.py (208), the three prior gates (91, 63, 81). Every read ended at the file's last line; a fourth dispatch.py read and a second diff read returned empty, confirming no clipping. Nothing executed, imported, compiled or parsed by tool; no provenance link, corpus, Git, network or other lane opened. Line numbers below are the charged files' own.

## A. Mutator fixtures — CONFIRMED

Baseline intake: mutate_controls.py:198-202 reads the input under the 15 MiB cap, requires exactly 1652675 bytes and the dac655a7 digest, parses with duplicate-key, no-number hooks (80-93), runs `validate` (148-196) and requires `dumps(doc) == raw` (202), so the original is proved byte-canonical under sort_keys/compact/ensure_ascii/newline before any edit. `validate` mirrors check.py's structural rules: strict key sets (150,154,166,171,181,193), seven-entry bands list (169), 7-coordinate elements (129-131), canonical integers and reduced rationals with positive denominator (106-122, the same rules as check.py:40-63), exponent bound 16, per-polynomial 4096 and aggregate 50000 term bounds, strictly increasing exponent tuples and no all-zero term (135-146). The aggregate counts the same 103 polynomials as check.py, so a mutator-validated fixture cannot trip the checker's parser or bounds.

Control 6 (203-213): `old_mate = doc['bands'][6]['B_var']` is the gap-7 mate column (list index 6 is h=7 under check.py:220's enumerate from 1). Line 207 requires a term with exponent list ['0','0','0','0','0','2'] (vartheta squared, variable index 5) and value ['1/1'] + six '0/1', which is exactly the unit theta-squared coefficient that check.py:355-357 forces on every accepted packet, so the guard is non-vacuous and cannot fail on the accepted baseline. Only `bands[6]['B_var']` is set to `[]` (208); raw6 is dumped, reloaded, revalidated (209-211; `poly([])` passes), the subtree is put back whole (212) and the bytes must equal the original (213). Genuinely distinct from the baseline (259) and from raw10 (260).

Control 10 (214-257): starts from a fresh `loads(raw)` (214), never from the control-6 object. Selection loops families in the order Psi, K1, K0, then row, term, basis (216-219), parses each coordinate with the mutator's own `rational` (220), skips zeros (`if q`), and keeps the first strictly larger absolute value (221), so ties resolve to the earliest (family, row, term, basis). `new = wire(rational(old) + 1)` (233) emits the reduced `numerator/denominator` string and re-parses it under the 4096-digit bound (124-127). The coordinate is replaced in place (235); deletion happens only when all seven coordinates read '0/1' (236-238), which occurs exactly when old was '-1/1' and the other six were zero. Fallback (223-229): `best is None` iff every row is empty, because validate forbids all-zero terms; line 224 asserts that, and one constant term with value one is appended to the first Psi row. Inverse edit (243-257): the mutated fixture is reloaded and revalidated, then the fallback row is required to be exactly one constant-one term and cleared, a deleted term is reinserted at the recorded index with '-1/1' at the recorded basis, or the coordinate is decremented; the whole re-serialisation must equal the original bytes (257). Receipt booleans (293) merely restate what 213 and 257 already asserted by `need`; my verification is of those lines, not of the flags.

Both outputs are bounded and distinct (258-261), sources are re-pinned and the baseline re-read before writing (262-263) and after (280-282).

## B. Mutator interlock — CONFIRMED

Order: platform, DMI vendor 'Amazon EC2', exact 19-entry argv with the nine flag names at odd positions and the job tag at argv[2], 64-hex non-zero ROOT and self pins (20-37) all precede `import hashlib`/`stat` (39-40); `json` and `Fraction` are imported only at 77-78 after the source pins (73) and the output-collision check (74); the payload is first opened at 198. Paths must be absolute, canonical (realpath equal), newline-free, at most 512 bytes and the seven paths distinct (42-46, 66). `read` opens O_NOFOLLOW, requires a regular file under the cap, reads cap+1 bytes and compares full fstat tuples before and after (48-58). The self pin is the CLI value hashed against the mutator's own bytes (67, 71); the checker and arithmetic pins are literal constants equal to the charged e6bc7cca and e5dd4bcb digests. The ROOT hash is only recorded (285); the mutator never reads a registration, so it is a binding, exactly as the CONTRACT (29-31) states; authority rests on the immutable caller. Output: O_EXCL|O_NOFOLLOW create at 0600, full-write check, fchmod 0444, fsync, directory fsync (265-276); receipt written last (297) after both fixtures are read back (280-281); receipt capped at 32768 bytes (296). Joint reserve 261. Only stdlib modules are imported; no producer, checker or arithmetic module is imported, and coefficient parsing (necessarily local to the mutator for control 10) happens only through its own `rational` after the interlock.

## C. Dispatcher integration and the self-hash token — CONFIRMED

Inherited: the SCIENCE map (28-33) and CAPRUN_SHA (27) are unchanged in the diff; the science listing must be exactly the five names (264) with literal 0444 and SHAs (269-271); the wrapper listing is exactly dispatch.py, probe.py, mutate_controls.py (265). Native closure code is untouched (198-204, 267-287). New: seven roles (176), mutator path fixed to wrapper/mutate_controls.py (184), mutator and baseline 0444 at init and every revalidate (185-186, 249-250), baseline pinned by SHA and byte count (193-194), mutator pinned to the literal a896a809 constant (195), and all role files, the registration, the native manifest and every native file required outside the tmpfs (216-219), which closes the prior runtime gate's item E remark. Caller bindings are unchanged: environment (162), EC2 tag (164-166), host, boot, PID namespace, cgroup and memory.max (167-173), interpreter (177), dispatcher identity (178), cwd (181), live outer argv from /proc (188).

Token: `run` builds the full CAPRUN vector (371-375). For label mutate it requires the registered list to contain the flag `--root-registration-sha256` exactly once and the token `ROOT_REGISTRATION_SHA256` exactly once, the token to sit exactly in the slot after that flag, replaces that slot alone with `self.root_sha` and requires the entire list to equal the freshly built command (376-391); for every other label the token is forbidden as an element (390). `self.root_sha` is the hash of the immutable 0444 registration (156-157), rechecked at every revalidate (248), including directly before Popen (398). The expanded argv is recorded in the pre record (393-396) and in the CAPRUN telemetry binding (441-442). Attack review: no shell or environment expansion exists (list Popen, fixed env, 405); a second token or a token in another command fails closed; a registered element merely containing the token as a substring is not expanded and must still equal the corresponding built element, which is an absolute path or a fixed literal, so it cannot smuggle a value; the mutator receives the same root SHA and echoes it into the receipt, which 472 compares. No registration with enabled true exists; DISABLED-REGISTRATION.json dies at 159.

Unmeasured runtime item, not a defect: the mutator profile is 10 s wall and 9 s soft CPU (36-37), while the mutator performs four loads, four dumps and three full validations of a 1.65 MB document with Fraction construction per coordinate; an overrun is a typed RESOURCE_CAP STOP, never an accept.

End of sections A-C.

## D. Receipt parser, freeze, traceback recognition — CONFIRMED

`fixture_receipt` (462-524) loads only the 32768-byte receipt (466) and requires the exact eleven keys (467-469), literal schema/status/science_outcome NONE/job tag/root SHA (470-473), the three literal assertions (474-475), the exact three-source map keyed by the mutator and science paths with the literal pins (476-478), the exact baseline record with integer byte count (479-481), exactly two ordered output records with the exact key sets (482-488), writer-path binding for each (489-491), typed hash and size fields (492-493), an actual readback of each writer fixture whose size and SHA match and whose SHA differs from the baseline and from the other fixture (494-496), the literal control-6 mutation string, gap '7', 1..4096 old terms and a 64-hex subtree digest (497-501), and the exact selection fields with family, row ceiling by family (2/6/8), term 4095, basis 6, six exponent strings in '0'..'16', bounded canonical rational strings, old != new, the literal fallback record or the '-1/1' to '0/1' deletion pair (502-520). Every field the mutator emits (283-294) matches these predicates key for key. Writer inventory must be exactly the two probe payloads, two fixtures and receipt (521-522). The receipt's paths describe generation in the writer directory; the frozen paths are then named by fixture_pins (603) and by each checker's pre record argv and input hash (392-396), and the result names the frozen receipt hash (618). Minor: the `outcomes` records (613-614) carry the frozen input SHA but not its path string; adding 'path' would make them self-describing. No fixture JSON is ever loaded by the dispatcher; `load` is applied only to registration, manifest, telemetry, receipt, sentinel and dummy events.

Freeze (593-605): for each of mutated6.json, mutated10.json, mutate.receipt.json the frozen target must be absent, the writer bytes are hashed, renamed inside the tmpfs, chowned root, chmod 0444, fsynced, re-hashed through `immutable`, and pinned; then writer/frozen/mount directories are fsynced and frozen becomes 0555 before `revalidate`. Both checkers then go through `run`, which revalidates at 341, 398 (directly before Popen) and 437 (after group quiet), each time re-hashing all three frozen pins, requiring 0444, frozen 0555 and the exact three-name inventory (249-257); the input is additionally hashed before and after through `immutable` (392, 438).

Outcome recognition: both checkers must be NORMAL_EXIT with resource null and child_returncode 1 (610, 459-460), child_signal null, child_exit_code 1, empty stdout (611). `traceback` (526-554) bounds stderr at 8192 bytes, decodes ASCII, requires the literal header, then ordered frames, each a File/line/function line plus the stripped source line, with at most one caret line of spaces, tildes and at least one caret per frame, and the exact final line with nothing after. I traced both fixtures through the unchanged check.py. Control 6: `vvar = poly([])` is empty (306-307), envelope and support checks pass (310-311, 326), `base` at 328 is independent of B_var, and at 329 `oper(7, {}, {})` is empty so the pair is `-tvar = T^4` (324), whose vartheta exponent 4 exceeds 1 and raises 'upper band residual' at 216 inside `residual_pair`; nothing between the start of the h=7 iteration and 329 reads B_var. Frames 416 main(), 412 print(check_file(path)), 329, 216 and the final line match dispatch.py:531-535 letter for letter. Control 10: doc['rows'] is first parsed at 376-378 after all band and Jacobian checks, which do not read rows; a changed Psi coordinate or a deleted Psi term or the fallback constant makes the list comparison at 376 fail and `require` raises 'CHECK FAILED: all three Psi slots' at check_arithmetic.py:208; a changed K1 or K0 row passes 376, then the j=1/j=0 loops reach the mutated index i, where 383 fails before the envelope at 384 (earlier indices are unchanged and pass). Statements at 376 and 383 and the require line agree with dispatch.py:539-544 after leading-whitespace stripping, and the function names are the code names check_file and require. ROOT's two corrected statements hold: 376 compares whole polynomials, so no array-length change is needed; deletion needs all seven coordinates zero (mutate_controls.py:236).

## E. Sequence, profiles, budgets — CONFIRMED

LABELS (38-39) is exactly nine old preflights plus mutate, check6, check10, and `execute` runs them in that order (559-615), with `used_labels` forbidding any repeat (340) and 615 requiring the completed twelve-tuple. PROFILES (36-37): 9 x 5 wall = 45, 10, 2 x 210 = 420, total 475 wall; hard CPU with CAPRUN's soft+1: 9 x 4 + 10 + 2 x 170 = 386. LIMITS 600/500/2 GiB/16 MiB unchanged (34-35), cgroup memory.max literal (173), sampled 480 cutoff in `budget` (245) also inside the live loop (429), +15 admission (343, 398, 430), post-return 600/500 ceiling (439). `size_budget` (309-325): each fixture at most 15 MiB, both together at most TOTAL minus META = 15 MiB, everything else at most 1 MiB, no symlinks, and the baseline is outside the mount (216-217) so it is never counted. No inner process group, retry or cap reset exists; the dummy RSS/TERM/KILL/quiet block (572-587) and `durable_copy` (625-648) are byte-identical in the diff. `identity` still catches only FileNotFoundError (148), so the accepted ESRCH false-STOP race is retained unchanged, not generalised. The caps are registered limits, not measured runtimes.

## F. Scope and next gate

These frozen sources can yield only the literal result at 616-621: status TWO_SEMANTIC_REJECTIONS_CONFIRMED, science_outcome NONE, baseline_sha256 dac655a7 (bound to the actual file by pin, byte count and pre/post hashes, and by the mutator's own 199), mutator_sha256, frozen receipt hash, two outcome records, thirteen other controls NOT_RUN and no positive rerun; exit 0 only for that status (669). Nothing in them states or could state highest regularity, a finite basis, d=35, a source zero/nonzero/point, degree closure or JC2. Conditional approval: the candidate is fit for one ROOT-registered twelve-child batch; no observation is claimed here.

Execution prerequisites: (1) an enabled ROOT registration with the semantic schema, twelve command vectors reproducing 371-375 byte for byte, the mutate vector carrying the single token, pins for the seven roles, five science files and native manifest, literal outer argv, fresh instance/boot/namespace/cgroup and deadlines; (2) mutate_controls.py a896a809 installed root 0444 as the third wrapper file and the baseline dac655a7 root 0444 outside the tmpfs; (3) the six-field native closure and interpreter identity for the actual host; (4) a fresh 16 MiB tmpfs with empty authority/frozen children and a science-owned 0700 writer, outer streams bound on it; (5) an absent durable ext4/xfs target. Specific gaps, all fail-closed: (a) the 9 s CPU mutator profile is unmeasured against three full validations of the baseline; (b) the mutator's 202 requires the baseline to be byte-canonical under Python's sort_keys/compact/ascii/newline encoding, which produce.py is not charged here to prove; (c) CPython traceback formatting is assumed 3.11-3.13 style; a different layout is a typed STOP; (d) live capture of the mutator inside the 50 ms poll is required (456), no retry; (e) the ESRCH race. No syntax, import, test, fixture or runtime success was observed by this gate.

## Verdict table

| item | verdict |
|---|---|
| A two canonical distinct fixtures, exact theta-squared guard, max-abs selection, seven-coordinate deletion, fallback, whole-byte inverse restore | CONFIRMED |
| B interlock order, 19 argv, pins, no-follow/drift, exclusive 0444 fsync, receipt last, binding not authority | CONFIRMED |
| C inherited five science files and CAPRUN, three-file wrapper, outside-tmpfs, caller bindings, single-slot token expansion | CONFIRMED; mutator CPU profile unmeasured |
| D receipt schema, freeze before both checkers, pre/post rechecks, exact four-frame tracebacks 329-216 and 376/383-208 | CONFIRMED; outcomes lack a literal path field |
| E 12 labels, 475/386, 600/500/2 GiB/16 MiB, 15 MiB joint fixtures, 1 MiB metadata, no retry, ESRCH race unchanged | CONFIRMED |
| F only TWO_SEMANTIC_REJECTIONS_CONFIRMED with science_outcome NONE and baseline binding | CONFIRMED conditionally on registration and observed controls |

Smallest blocking correction: none found. Non-blocking: add the frozen path to each outcome record; measure the mutator once under CAPRUN before relying on the 10/9 profile.

End of sections D-F.

## OPEN(S) RAISED

None. No new canonical OPEN; the remaining quantities are the two non-blocking items above and the separately ROOT-registered twelve-child batch, not authorised here.

## COLLISIONS

status: EMPTY

- NONE — own-only check: this lane wrote exactly xmodel/f10-r2-semantic-code-gate-fable5-20260910.md and box/f10-r2-semantic-code-gate-fable5-20260910/custody.sha256, both absent at 13:33:58 UTC; no corpus scan; no other file touched.

## WHOLE check and attestation

All 12 inputs were read whole as itemised in Read scope; the twelve digests were re-computed after the body and equal the box custody file. This report was re-read by tail and heading inventory before the marker; the section order is Custody, Prior involvement, Read scope, A-F, Verdict table, OPEN(S), COLLISIONS, this section. Same-model disclosure: the three imported gates are Fable 5.1 authored and are consumed only at their stated scope; the accepted reconstruction mathematics and CAPRUN were not re-audited. Authoring: every byte of both owned files was written by apply_patch (custody rows piped from sha256sum output into apply_patch's stdin); no Write/Edit tool, no shell redirection into any file, no helper, no source or input edit, no Seal, no charge_basis, no execution, import, AST, syntax, compile, test, CAS, network, AWS, SSH, Git, agents, corpus, shared, protected, other-lane or live file. Timeline: hashes and absence 13:33:58 UTC, skeleton 13:34, whole reads 13:34-13:36, sections A-C 13:41, D-F 13:42, this section before the 13:48:58 reserve, deadline 13:51:58 UTC, never reset. The standalone marker below is the only such line in this file and nothing follows it.

<!-- BODY-END -->
