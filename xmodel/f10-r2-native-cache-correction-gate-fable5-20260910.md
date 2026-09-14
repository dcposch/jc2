# f10-r2 native cache correction gate (Fable 5.1, 2026-09-10)

FIRST independent review of the ROOT/Astra two-refusal diagnostic custody and of the minimal fresh native-registration correction. Reviewer Fable 5.1; diagnostic executor ROOT/Astra; correction author ROOT.
Lane first action 2026-09-10 15:34:38 UTC; deadline min(ROOT launch+18 min, 15:54:00 UTC), taken as 15:52:00 UTC because the ROOT runtime started before the first action; final 3 min reserve, never reset.
Status: UNSEALED (no Seal section by instruction); sections A-D complete. Method: sha256sum, whole text reads, manual reasoning only. No subprocess/import/AST/compile/test/CAS/network/AWS/SSH/git/process/agents.

## Custody (8 frozen inputs, sha256 from sha256sum at 15:34:38 UTC)

| sha256 | basename |
|---|---|
| 8b1112984ae6d95939669db1f32fb2aa8feacbdd19b56c1eb26dc382bd762678 | CUSTODY.json |
| 91d0052e07106a847dbffed3565e9c4c21a6125ba16bb222a47ff5a5891ca97c | RESULT.md |
| bd77d02ea15d813a07ddde9ccb3c060dc3f5095473cb2ccceaf0984e18ee51e9 | ROOT-NATIVE-CORRECTION.md |
| 6c232bb0d1b4ee62fefb62970b1b5a06a092db735cbd6fb47907c54921169c0b | dispatch.py |
| 1944f1d87853b35e0efcca72c8097cc35f70947a81a78d7b87b7025832f2c9ae | f10-r2-map-observer-gate-fable5-20260910.md |
| 469fd1c701a2af3149ff7401c7592a4fb313ad7ee64b922105d86c27700eb09b | f10-r2-semantic-code-gate-fable5-20260910.md |
| 191f90071bb5c6f75d0cb4b38e420e942496d4e4e1066aff3719736099bdfea7 | map-rejection.UNVALIDATED.json |
| 1c9e90633abdcb921e23bb505163a04b400ddc4bf859d1500b26913b503a1bd1 | native-metadata.sh |

All 8 match the charged pins; distinct basenames. Both owned targets verified ABSENT at 15:34:38 UTC before this skeleton.

## Prior involvement disclosure

Two charged inputs are Fable 5.1 authored, same model as this reviewer: the semantic code gate (469fd1c7, which FIRST-accepted dispatch.py 6c232bb0 and the mutator) and the map-observer gate (1944f1d8, which FIRST-accepted the observer dispatcher b4cea19b and probe.py 1e3bea3a). Both are consumed at their stated static scope only; their mathematics and instrument reviews are not repeated here. ROOT-NATIVE-CORRECTION.md and RESULT.md are ROOT/Astra authored. The observer dispatcher b4cea19b is not charged; native-metadata.sh is read as a documentary source bound to the retired worker (its line 6 names that instance) and was not executed.

<!-- SECTIONS-BEGIN -->

## Read scope

Whole reads 15:35-15:36 UTC, each ending at the file's last line: ROOT-NATIVE-CORRECTION.md (22 lines), RESULT.md (38), CUSTODY.json (1 line, 21 file entries), map-rejection.UNVALIDATED.json (1 line, 14 keys), native-metadata.sh (75 lines, 73 non-blank), observer gate (98, marker last), semantic gate (107, marker last), dispatch.py (673, ending at the SystemExit line). No clipping. Nothing executed, imported, compiled or parsed by tool; no archive, EBS, corpus, Git, network or other lane opened. Line numbers below are the charged files' own.

## A. Terminal custody supports only the stopped second preflight — CONFIRMED at the ROOT trust boundary

Logical content, read directly from the two charged JSON objects. CUSTODY.json carries result status STOP_NONDECISION with reason 'mapped native file not pinned', schema f10-r2-map-observer-custody/v1, science_outcome NONE, and exactly one runs entry: label refuse-status, status NORMAL_EXIT, resource null, input_sha256 null, runner_live_observed true, actual_python_live_observed true, owned_group_quiet true, at 15:11:45.74 UTC. Its 21 file rows hold the full refuse-status set (pre, runner-live, python-live, post, telemetry, four streams) but for refuse-caps only pre, runner-live, telemetry, runner streams and two empty child streams: no refuse-caps.post.json and no refuse-caps.python-live.json. That is exactly the footprint of a run that passed the first label's refusal checks (a second label cannot start before them, dispatch.py:559-562, 340), emitted the second pre and runner records, and raised inside the child observation before any post record. The map record agrees: label refuse-caps, phase child-observation, role probe-child, rejection_utc 15:11:46.097 UTC, first_rejected raw_path = resolved_path = /etc/ld.so.cache with file_member false, alias_required false, alias_member false, reason 'mapped native file not pinned', status UNVALIDATED_MAP_REJECTION, validation_passed false, non_atomic_proc_reads true, science_outcome NONE. Its snapshot is the authorize-mode probe: argv with the literal --mode authorize, uid/gid 65534 x4, CapEff/Inh/Prm zero, NoNewPrivs 1, pid = pgid 8404, state R, the observer service cgroup, cpu limit 3 soft/4 hard and file size 15728640, matching the control profile and PACKET at dispatch.py:36 and 41. Cross-bindings all agree: the record's root_registration_sha256 f2aa0a04 equals CUSTODY root_sha256; native_manifest_sha256 5003b730 equals runs[0].native_sha256 and card line 8; the authorization digest 463a7d1f inside the snapshot argv equals the CUSTODY row for authority/refuse-caps.json; runs[0].authorization_sha256 5f0d925e and telemetry_sha256 5234d002 equal their rows; runs[0].source_pins equal SCIENCE at 28-33; the record's own row is 3476 bytes with the charged digest 191f9007, and RESULT.md:28-29 names the two charged digests. refuse-status.stderr is 44 bytes, the length of 'REFUSED: no registered ROOT CAPRUN contract' plus newline required at 562; sha256sum of that literal reproduces its row digest 42f168d6, and the four empty streams carry the empty-input digest.

Distinctions. (1) The 14:09 pathname is identified nowhere in the charged inputs (RESULT.md:9, card line 5); the record names a file mapped in the observer's second probe child at 15:11:46, under the same reason string that dispatch.py:299 emits for any unlisted mapping. (2) The post-observation copy digest abdf8ebc (RESULT.md:19-21, card line 12) is a later file hash, not the bytes of the private read-only mapping at the snapshot instant, and is never a pin. (3) The snapshot is assembled from separate /proc reads (identity, 129-147; observation 15:11:46.0965 to .0969) and the record says so. (4) No science: runs has no mutate or check label, every input_sha256 is null, both science_outcome fields are NONE, and no fixture, baseline, receipt or checker file is among the 21 rows.

Inference from the same evidence, stated as inference: the outer observer process passed its own map check at every revalidate, the CAPRUN runner passed twice and the first probe child passed once, yet the second child was caught with /etc/ld.so.cache mapped beside freshly loaded _hashlib and libcrypto. So on this image the loader maps the cache transiently during library search and unmaps it afterwards; the observation is race-dependent, which is why earlier passes did not expose the same genuine omission and why the 14:09 attempt could plausibly, but not demonstrably, have hit the same file.

ROOT physical items: the 57 hash rows, 13 source pins, 1225 native hashes, pre/post inventory identity, archive digest a924bf36, EBS retention, exact-ID termination and local replay (RESULT.md:15-38) are ROOT attestations. I did not observe the worker, cgroup, hashes or archive at runtime and accept them only as stated custody at ROOT trust. They demonstrate custody, not mathematics; no 6/10, baseline or promotion claim exists in any charged file.

## B. Appending /etc/ld.so.cache to the collector root list — CONFIRMED, one uncharged link

Collector side (native-metadata.sh). The explicit root loop is line 64 with six literal roots. An appended /etc/ld.so.cache enters jc2_native_visit: path regex (17), readlink -e canonical form (18-20), ALIAS emitted only if the raw path differs from the real one (21-26), non-directory branch (40): regular-file test (41), dedupe (42), count bound 3000 (45; 1225 becomes about 1226), sha256sum of the real path (46), FILE size/uid/gid/mode line (47). The ldd expansion runs only when file -Lb starts with ELF (49); the cache is not ELF, so no dependency walk, and nothing recurses into /etc because directory recursion (27-39) applies to directory roots only. No wildcard, no inferred library, no dropped mapping. The routine is unchanged; the two literal edits are the appended root at 64 and the instance tag at 6, which a fresh worker forces anyway and which makes the retired collector unrunnable there (set -e, lines 3-6). Every hash and stat is produced on the fresh worker; the retained abdf8ebc digest is never consumed.

Dispatcher side (6c232bb0, unchanged). check_maps (295-301) requires each mapped path to resolve into native['files'] and, when raw differs from resolved, the alias to be registered; it never asks for the parent directory. revalidate (267-268) hashes every native file at every call (233, 341, 398, 437, 605) through immutable with strict False: regular, root-owned, world-readable, not group/other writable, root-owned traversable ancestry (81-98); a 0644 root cache under 0755 /etc passes, and the owner-write bit is tolerated only for native files, not for pins. Directory closure (272-277) runs from registered directories to their children, never from files to parents, so /etc need not be inventoried, as card line 16 says. Aliases (278-281), absent paths (283), sys.path closure (284-285), ps aliases (286-287), manifest pin (199, 288), outside-tmpfs (219) and bounds (204) all remain. Rejections retained: any other unlisted mapping fails at 299, a drifted native file at 268 or 288, a deleted mapping at 138 (RuntimeError, not caught by 148). No allowlist or skip exists anywhere in the file.

Uncharged link: the assembler that turns FILE, ALIAS, DIRECTORY, ENTRY and COUNTS lines into the six-field JSON (line 60 calls it 'the actual caller') is not among the inputs. An unchanged assembler ingests the new sha and FILE lines exactly like the other 1225; a malformed entry fails closed at 202, 204 or 268. Documentation gap, not blocking.

End of sections A-B.

## C. No source change is needed for this one omission — CONFIRMED

The observed omission is registration data: the loader maps /etc/ld.so.cache and the manifest did not list it. The accepted dispatcher already accepts any listed regular native file at any path outside the tmpfs, so registering the file is the whole correction; touching check_maps, revalidate or the collector routine would be hardening beyond the observation and is not requested. Everything else stays mandatory and unchanged in 6c232bb0: ROOT/Linux (155), immutable 0444 registration and its self-hash (156-157, 248), enabled schema, job and exclusivity (159-160), fixed caps and profiles (161, 34-37), exact environment (162), EC2, host, boot, namespace, cgroup and memory.max (164-173), seven roles and interpreter (175-178), literal outer argv (187-188), role, science, CAPRUN, baseline and mutator pins (189-197), six-field native manifest and sys.path closure (198-204), output children, tmpfs, streams, durable target and deadlines (205-230), twelve commands (231), nine preflights, mutator, freeze and two checks in order (556-615), exact traces (526-554), no label repeat (340), STOP_NONDECISION with a 500-character reason on any exception (657-658) and durable custody (662-666). The code itself forces a fresh registration: instance id, boot id, cgroup, deadlines and the native manifest digest are compared live (164-173, 199, 228-230), so no old registration, old worker hash or old manifest can be reused. Only one freshly registered semantic batch fits these lines, after every ROOT prerequisite on card lines 14-20; an unchanged retry has no path, and no new observer run is needed for this correction. A repeat 'mapped native file not pinned' or any other new failure is a STOP without a pathname (658); the card accepts that as a ROOT custody obligation and keeps the observer out of the semantic dispatcher. No claim follows that the correction makes the batch succeed: the mapping is transient, another loader-window file could appear in a mutator or checker child, and the 14:09 pathname remains unidentified.

## D. Scope and authorization — CONFIRMED as bounded preparation; no blocking doubt

The card's plan (lines 14-20) is sufficient to prepare one bounded 6/10 runtime: fresh worker and exact EC2 identity, fresh collector output with the appended root, fresh registration binding the expanded twelve argv, sources, baseline, native digest, physical, namespace, cgroup, uid/gid, environment, paths, ancestry, deadlines and import rules, USER and SYSTEM timers armed before use and never reset, terminal custody, archive, download and early exact-ID termination with DeleteOnTermination false. Literals agree with the charged sources: probe 1e3bea3a and dispatcher 6c232bb0 (semantic gate custody rows; my sha256sum of dispatch.py), mutator a896a809 and CAPRUN 4435279d (dispatch.py:26-27), baseline dac655a7 with 1652675 bytes (24-25), joint 600/500/2 GiB/16 MiB (34-35, 41), sampled 480 stop (245), unchanged child profiles (36-37). Code and caps are unchanged; no local mathematics and no positive rerun are involved, and the baseline is bound by hash and byte count only (193-194), never read for content. The most this runtime can state is TWO_SEMANTIC_REJECTIONS_CONFIRMED with science_outcome NONE and thirteen controls NOT_RUN (616-621); it validates no failed attempt retrospectively and proves no control, baseline, highest regularity, full source or JC2 claim. Blocking doubt: none found; the scoped correction is accepted. Registration quality (an actual fresh collector run on the actual worker and a correct assembler) and package/cache immutability through the batch are ROOT's; ld.so.cache is a generated file that package or ldconfig activity rewrites, and such drift surfaces as a 'current pin' STOP, never an accept. Pre/post whole-manifest hashes plus per-child map checks remain metadata evidence, not a coherent loaded-image proof.

## Verdict table

| item | verdict |
|---|---|
| A terminal custody = first refusal complete, second stopped at probe-child observation of /etc/ld.so.cache at 15:11:46; 14:09 path unknown, post-copy hash not loaded bytes, non-atomic, science NONE; physical items at ROOT trust | CONFIRMED |
| B appended root yields a canonical fresh file/hash/stat/alias entry; dispatcher accepts files outside directory roots, validates mode/owner/hash/aliases, rejects every other unlisted, drifted or deleted mapping; no /etc recursion or wildcard | CONFIRMED; manifest assembler uncharged |
| C no source change; all ROOT, import, native, physical, env, argv, cap, preflight, trace, freeze and custody checks unchanged; one fresh batch only; new failure is STOP | CONFIRMED |
| D plan sufficient for bounded preparation; no retrospective validation or science claim; code and caps unchanged | CONFIRMED, no blocking doubt |

Smallest mandatory correction: append /etc/ld.so.cache to the line-64 root list of a freshly instance-bound collector and register the fresh manifest; nothing else. Non-blocking: the assembler from collector lines to JSON should be charged in the next gate; a repeat semantic map STOP will again carry no pathname.

End of sections C-D.

## OPEN(S) RAISED

None. No new canonical OPEN; the remaining quantities are the ROOT-registered fresh batch and the unobserved 14:09 pathname, neither authorized nor resolved here.

## COLLISIONS

status: EMPTY

- NONE — own-only check: this lane wrote exactly xmodel/f10-r2-native-cache-correction-gate-fable5-20260910.md and box/f10-r2-native-cache-correction-gate-fable5-20260910/custody.sha256, both absent at 15:34:38 UTC; no corpus scan; no other file touched.

## WHOLE check and attestation

All 8 inputs were read whole as itemised in Read scope; the eight digests equal the box custody file, which was generated from sha256sum output. This report was re-read by tail and heading inventory before the marker; section order is Custody, Prior involvement, Read scope, A-D, Verdict table, OPEN(S), COLLISIONS, this section. Disclosure: the two imported gates are same-model (Fable 5.1) and were consumed only at their static scope; their instrument and mathematics reviews were not repeated. ROOT physical custody is a trust boundary; nothing at the worker, cgroup or archive was observed by this lane. Authoring: every byte of both owned files was written by apply_patch (custody rows piped from sha256sum output into its stdin); no Write/Edit tool, no shell redirection into any file, no helper, no source or input edit, no Seal, no charge_basis, no execution, import, AST, syntax, compile, test, CAS, network, AWS, SSH, Git, agents, corpus, shared, protected, other-lane or live file, and the old collector was never executed. Timeline: hashes and absence 15:34:38 UTC, whole reads 15:35-15:36, sections A-B 15:41, C-D and this section before the 15:49:00 reserve, deadline taken as 15:52:00 UTC, never reset. The standalone marker below is the only such line in this file and nothing follows it.

<!-- BODY-END -->
