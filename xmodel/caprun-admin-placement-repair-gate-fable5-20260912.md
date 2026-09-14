# caprun-admin-placement-repair-gate-fable5-20260912

Reviewer: Fable 5.1 (different-model hostile reviewer). Lane: caprun admin-placement two-file source repair (Sol).
First action UTC: 2026-09-12T07:22:14Z. Reserve 07:41 UTC, HARD 07:44 UTC 2026-09-12.
Mode: STATIC/MANUAL ONLY. No execution of any charged or generated source. Nine immutable snapshots in /tmp/jc2-lane.ILwBO4/inputs hashed before body reads.

## 0. Input pins (pre-read 07:22:28Z; post-read 07:28:23Z, all nine unchanged)

| basename | sha256 | expected |
|---|---|---|
| caprun-admin-placement-repair-sol-20260912.md | ae02a5b31cdf33c9681ebb50396a5d0dc841bece74b8da08957119398ded9d63 | match |
| setup-pre-admission.template.sh | 39c242aded4ac83448416ffc4f9b51e3420b042c2ed59be0946968d8a4141783 | match |
| preholder-security.template.sh | 13e3653977688fc85a6825318358df74d54df2a534a524edccd1e1843605e63a | match |
| setup-pre-admission.template.sh.diff | 0ad94ab94256fb63cf636e9307aaeecf779349d5489e64c4045424290775f70a | match |
| preholder-security.template.sh.diff | 183c4a80df8adc8c02228425d1b1808cc4dedf5c9c2ef624c7935e272fca30a2 | match |
| BINDING-AND-NEGATIVE-CONTROLS.md | 08bf4806bfb4829f8e86bdbcf2da7404079e2199a8022b7100124f039ce62aeb | match |
| CONTRACT.md | c7399321af5b89a94be3c4183c6f4a605c7083c994ef4f93a5eab5d46b8318d4 | match |
| FROZEN-CONFIG.template.json | bc910f535c64c18c3140c72c763bad67dd3fa208a970626478ade36464d76fe5 | match |
| REMOTE-PREHOLDER-MANIFEST.template.sha256 | 87194a6f0b2c950eb366c099ed1aa431a3112548341de84296e5e700fc71e62d | match |

Each file read whole. Sol seal re-derived: first 4699 bytes end at the BODY-END line and hash to a3fd0678690812bbe667c86089d497136a8da8eeec4a71f1dccb58b05c37aa70 (matches). Diff arithmetic: setup +90/-39, 5 hunks, 96->147 lines; security +45/-6, 2 hunks, 38->77 lines. Every new-side diff line appears verbatim, in order, in the published template; the only template lines outside the diff view are the unchanged inter-hunk regions (setup 10-17, 65, 102, 134-139), i.e. the original identity/deadline/pins/mount guards. S = setup template, P = security template, B = BINDING-AND-NEGATIVE-CONTROLS.md; line numbers are published-template lines.

## 1. Verdicts A-F

**A. CONFIRMED.** S:5-8 retains the self-grep refusal; P:4-7 adds it. Phrases S:9 (`..._CLOSEDCHILD_PRE_ADMISSION`) and P:8 (`..._PREHOLDER_SECURITY_ONLY`) are distinct from each other and from the seven config phrases (FROZEN-CONFIG 5-10, 106-110). The regex text does not match itself (class body contains `[`, `-`, `]`, `+`); if `$0` is not a file, S:9/P:8 still fail closed on the literal placeholder. Retained unchanged: S:10-16 (uid, vendor, asset tag, hostname, boot_id, pid ns, deadline), S:19-20, S:62-67 pins and native.sha256, S:68-105 base install/holder hash/installed manifest/registration absence, S:131-141 durable device/fstype, tmpfs, writer dir, nobody readability; P:22, P:24-39 ancestry and base-recursive predicates, P:69-77 mount emptiness, findmnt, PID-1 namespaces, packages. The only literal-to-placeholder edits are the obsolete batch paths and the cgroup literal (P:23). P has no `date -ud`/deadline comparison, only START/END prints (P:11, P:77). S mutates only by mkdir/install/mkfifo/mount/sync; no systemd-run, no holder start, no write to release.fifo, no ROOT-REGISTRATION.json (S:104-105 assert absence). P is read-only. Nit: regex S:27/P:18 admits `.` and `..`; closed by S:38 (they always exist) and P:25 canonicality.

**B. CONFIRMED.** Direct /opt child S:27/P:18; disjointness both directions S:28-30/P:19-21; `/` and `/opt` canonical, uid 0, no g/o write S:31-36; tree absent and non-link S:37-40; created root:root 0755 S:108; five explicit installs with per-name absence/non-link S:109-113; C-sorted census equals exactly the five names S:114 (order verified: fifo-write < observe-and-leaves < outer-admission < receive < release-check); no non-regular entry at any depth S:115 (so no subtree); each file canonical, non-link, 0:0:555 S:116-120; installed hashes S:121. P repeats tree 0:0:755 (P:42), census/non-regular (P:43-44), per-role canonical/non-link/0:0:555/bound sha (P:45-57), tree in the protected list (P:24). Base predicate unchanged: dirs 0:0:755 P:31-34, files 0:0:444 P:35-38, no symlink P:39; holder stays 0444 (S:100, P:36). Executables live outside base, so recursive 0444 is preserved. Nit: S does not re-stat the tree's own mode after S:108; P:42 does before holder.

**C. CONFIRMED.** Order: five bound program bytes -> hashes -> two manifests (B:17) -> manifest file hashes into S:43-44 and rows S:48-59 -> S bound -> S run -> FIFO_CREATED_ACTUAL (S:130) -> P bound (P:66-67). Nothing charged embeds the hash of S or P; config stores manifest paths, not self-digests (CONTRACT:7). Fiat is mechanically excluded for any template carrying a placeholder: S:45 greps the five staged programs and both admin manifests and exits 2, so an unbound template cannot be the staged/installed program; a placeholder-free template would give bound == unbound by identity, not fiat. Config remote.fixed_paths (FROZEN-CONFIG 95-104) and the eight manifest rows are the same roles in the same order; B:19 keeps holder/installed/native rows unchanged. Authorities: S creates only empty `authority`/`frozen` dirs (S:137, retained); P:69 forbids any regular file under the mount; config authority_disposition = EXPECTED_RUNTIME_OUTPUTS_DO_NOT_PREINSTALL. Binding obligation, not defect: the same values carry different placeholder names across files (S `JC2_ADMISSION_BOUND_SHA` vs manifest `JC2_REMOTE_ADMISSION_SHA256`; S `JC2_SCIENCE_BASE_PATH` vs config `JC2_REMOTE_BASE`; config has no admin-tree or channel field). No charged source cross-checks these; a mismatch fails at the existing caller's remote digest fetch.

**D. Unqualified exact-byte predicate REFUTED; conditional correctness CONFIRMED; no SOURCE fix required.** Manual cases for S:48/S:54 (command substitution strips all trailing LFs on both sides):
1. Valid five LF rows: equal, accepted; no false negative.
2. Five rows, last row without LF: same text after stripping; accepted although not LF-terminated.
3. Five rows plus trailing empty line(s): sed prints rows 1-5 and an empty line 6; stripped; accepted.
4. Five rows, empty line 6, arbitrary lines 7..n: as 3; accepted, lines 7+ never examined by this test.
5. Six non-empty rows, four rows, reorder, CRLF, leading space: rejected.
So S:48/S:54 is a "first six lines modulo trailing LFs" predicate, not the "exactly five LF-terminated rows" predicate stated at B:17 and Sol:13/25. But S:42-44 pin the manifest file hashes to ROOT constants, so any consumed manifest is byte-identical to the file ROOT pinned; the text test only cross-checks ROOT's construction, S:60-61/S:121 still verify every parsed row against real bytes, and S:109-114 install and count a fixed five-name set regardless of manifest length. Whether `sha256sum --strict -c` rejects an empty row is version-dependent and unverified here, which is why exactness must be carried by the pin. Decision: the narrow claim holds CONDITIONAL on ROOT independently constructing and pinning a precisely specified valid five-row manifest (each row 64 hex + two spaces + name + LF, byte length 5x(67+len(name)), nothing else). Required: scope correction of B:17 and Sol:13/25 wording ("first six lines modulo trailing newlines; exactness carried by the pinned hash") plus exact ROOT binding with an independent byte count or `cmp`. No source edit is required or authorized.

**E. CONFIRMED with the declared GAP.** S:123 channel root:root 0700 (absence S:38); S:124 `mkfifo -m 0600` as root; S:125 0:0:600; S:126 exactly one child named release.fifo; S:127 nothing at depth 2; S:128 FIFO type; S:129 non-link; S:130 emits `FIFO_CREATED_ACTUAL %d %i %u %g %a %n`. P:60-68 rechecks 0:0:700, census, no subtree, type, non-link, 0:0:600, then exact string equality of `%d`/`%i` against frozen placeholders; the FIFO is also in P:24's canonical/uid/mode list. Per B:25-27 and Sol:29-31, observer, release check and FIFO writer compare path/type/mode only; repeated device/inode comparison is a GAP covered solely by trusted ROOT exclusive/no-concurrent-writer/no-replacement custody from P completion through release. Not charged, not converted into a mechanism.

**F. CONFIRMED as design controls; UNEXECUTED.** Every B:31 case maps to a line: placeholder S:5/S:45/P:4; phrase S:9/P:8; host/namespace/deadline S:11-16; existing/link target S:37-40, S:110-111; tree form S:27-30, P:18-21; ancestry S:31-36, P:24-28; entry census S:114-115, P:43-44; owner/mode/hash/path/row S:42-44, S:48-59, S:116-121, P:42-57; template-as-bound S:45; registration S:104-105, P:22; cgroup P:23; channel S:126-127, P:61-62; FIFO S:125-129, P:63-67. None executed by Sol (Sol:37) or here. Binding, identities, native closure, original clocks (CONTRACT:23) and 120 s liveness (CONTRACT OPEN2) remain UNMEASURED/UNQUALIFIED. Template review of inert bytes only; not bound review, not runtime evidence.

## 2. Minimal blocking defect

None found in the two derivatives or the contract. The substantive finding is D: an over-stated "exact text" claim about S:48/S:54, resolved by scope correction plus exact ROOT binding, not a source edit. Out of charge: FROZEN-CONFIG 51 hard-codes the caller path while line 70 carries a caller-path placeholder (pre-existing astra template).

## 3. Remaining GAPs (carried)

- Later-phase FIFO device/inode identity (E) rests on trusted ROOT custody.
- Cross-file consistency of differently named placeholders (C) is a ROOT binding obligation; one binding table recommended.
- Empty-row behaviour of `sha256sum --strict -c` unverified; moot once ROOT pins a valid five-row file (D).
- Runtime facts (F): binding, identities, native closure, clocks, 120 s liveness.

## 4. Custody

Post-pins of all nine inputs emitted to stdout at 07:28:23Z, identical to the pre-read pins. Whole readback of this report precedes the standalone BODY-END line, appended as the last edit. No artifact_finalize, no charge_basis; the unchanged launcher owns custody. Disposition: PASS as INERT SOURCE + CONTRACT, with the D wording correction required in B/Sol before ROOT binding; NOT a bound or runtime acceptance.

<!-- BODY-END -->
