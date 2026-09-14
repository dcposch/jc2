# Prepared-bundle exact binding table

Status: `INTERNAL-UNREVIEWED`, constants-only analysis. The dated `20260911d` bytes are obsolete references, never an active binding. `AUTHORITIES.preallocation.json` is a binder input recipe; its nine objects are not files to preinstall.

## 1. Four prepared filenames and prerequisite order

| Exact prepared-pins key | Construction before holder | Retained late tokens |
|---|---|---|
| `ROOT-REGISTRATION.preholder.json` | Constants-only derivative of charged registration; preserve exact 46-key census/order and prepared false/null states | outer device/inode; each of nine leaf device/inode pairs; eight authority/policy digests |
| `AUTHORITIES.preholder.json` | Constants-only derivative of charged authorities; exact nine-label census and recipes below | `valid.closed_scope.{device,inode}` and `dummy.closed_scope.{device,inode}` remain null until binder; no authority digest is stored here |
| `ROOT-EXECUTION-CARD.preholder.md` | Constants-only corrected derivative of charged card; apply the two proposed card fixes below, bind every EARLY placeholder, retain exact late multiplicities | PID, start, InvocationID, coordinator receipt SHA, final-registration SHA: one each |
| `final-install.preholder.sh` | Constants-only derivative of charged installer; update every dated batch/path/clock literal and bind INSTANCE×2, BOOT×2, CUTOFF×3 | PID×1, start×1, InvocationID×1, install-release×1, final-card×1, install-manifest×1, final-registration×2 |

Hash the four complete bytes only after those early bindings. The prepared-pins JSON must have exactly those four keys and their SHA-256 values. Caller reads those bytes; binder re-hashes all four before parsing. No early enabling is permitted.

## 2. Registration exact census and EARLY classes

Exact top-level keys (46): `schema`, `enabled`, `jobtag`, `exclusive_no_concurrent_writer`, `source_limits`, `limits`, `profiles`, `environment`, `uid`, `gid`, `instance_id`, `hostname`, `boot_id`, `pid_namespace`, `cgroup_path`, `aggregate_cpu_start_usec`, `files`, `pins`, `native_manifest`, `source_native_manifest`, `science_dir`, `wrapper_dir`, `output_mount`, `authority_dir`, `frozen_dir`, `writer_dir`, `durable_dir`, `durable_device`, `outer_argv`, four deadline keys, `phase_policy`, `typed_slot_policy`, `commands`, `source_files`, `source_pins`, `contract_sha256`, `place`, `review_clearance`, `preflight_policy`, `execution_mode`, `allowed_phases`, `closed_scope_first_sha256`, `closed_child_guard`.

| EARLY class | Fields/literals to bind or preserve |
|---|---|
| Static literals | schema/job tag; source limits `900/600/8589934592/134217728`; aggregate limits `3000/2100/8589934592/134217728`; exact five profiles; clean environment; uid/gid 65534; Python/setpriv role paths; `PREFLIGHT_ONLY_9`; ordered nine labels; `phase_policy:null`; `typed_slot_policy:{}`; `aggregate_cpu_start_usec:"0"`; place; review clearance; closed-scope FIRST |
| Required prepared states | `enabled:false`; `exclusive_no_concurrent_writer:false`; `closed_child_guard.root_no_migration:false`; outer device/inode null; all nine guard leaf device/inode pairs null; `durable_device` is the future physical value, not changed late by binder |
| Source-pin | exact five `source_files`; installed science pins; fixed CAPRUN/dispatcher/probe/mutator hashes; source references, contract SHA/path, preflight-policy path/SHA. Never follow the referenced science files in this delta |
| Native/physical/evidence | actual instance, hostname, boot ID, PID namespace; actual Python and setpriv hashes; full-native and source-native manifest hashes; durable device; corresponding card root-volume/physical/native-raw/admin-native/admission-FIRST/final holder/final admission evidence digests |
| Original-clock/batch | choose one fresh `jc2-closedchild-preflight9-YYYYMMDDx` base satisfying binder regex; rewrite every old base/unit/cgroup/output/durable/outer-argv/source-pin installed path consistently; bind admission/mathematical/task/worker UTCs from one original clock, without reset |

The registration has EARLY placeholder counts: instance×1, hostname×1, Python SHA×1, setpriv SHA×1, full-native SHA×1, source-native SHA×1; boot×10 and PID namespace×10 (top level plus nine commands). Those must all be resolved before binder. Late counts are child device×9, nine distinct child inode tokens×1 each, outer device×9, outer inode×9, and eight one-use authority/policy digest tokens. `refuse-hash` has literal 64-zero supplied digest, not a ninth digest token.

## 3. All nine command/authority recipes

Every command is the same exact prefix:

`python -I -S -B caprun --closed-child-cgroup CG/L --closed-child-device <late leaf.dev> --closed-child-inode <late leaf.ino> --closed-outer-cgroup CG --closed-outer-device <late outer.dev> --closed-outer-inode <late outer.ino> --closed-boot-id BOOT --closed-pid-namespace PIDNS --wall-seconds 5 --cpu-seconds 3 --rss-bytes R --rss-sample-seconds 0.05 --term-grace-seconds 1 --stdout-file OUT/L.stdout --stderr-file OUT/L.stderr --telemetry-file OUT/L.telemetry.json --cwd SCIENCE -- setpriv --reuid 65534 --regid 65534 --clear-groups --no-new-privs -- python -E -s -S -B`,

where `R=33554432` only for dummy and `8589934592` otherwise. Exact tails/authority deltas:

| L | Command tail | Prepared authority recipe | Late command digest |
|---|---|---|---|
| refuse-status | `produce.py --registered-job JOB --authorization AUTH/L.json --authorization-sha256 <digest> --output WRITER/L.payload` | general 11-key authority; `status=DISABLED` | SHA of canonical authority |
| refuse-caps | same | general; `status=REGISTERED`; only authority `limits.cpu_seconds="599"` | SHA of canonical authority |
| refuse-inventory | same | general; delete `files["check.py"]` | SHA of canonical authority |
| refuse-source | same | general; set `files["produce.py"]` to 64 zeros | SHA of canonical authority |
| refuse-hash | same with supplied SHA fixed to 64 zeros | unmodified general registered produce authority | literal zero; authority is still emitted at runtime |
| valid | `probe.py --registration FINALREG --policy AUTH/valid.json --policy-sha256 <digest> --mode valid --output WRITER/valid.payload` | exact 10-key root-policy object, control profile, science outcome NONE; closed-scope device/inode initially null | SHA of canonical policy |
| startup-produce | producer tail with `--registered-job WRONG-JOB` | unmodified general registered produce authority | SHA of canonical authority |
| startup-check | `check.py --registered-job WRONG-JOB --authorization ... --authorization-sha256 <digest> --input WRITER/L.payload` | general authority with `mode=check`, artifact SHA=64 zeros | SHA of canonical authority |
| dummy | probe tail, mode dummy | exact 10-key root-policy object, dummy profile, science outcome NONE; closed-scope device/inode initially null | SHA of canonical policy |

General authority exact keys: `job_tag,status,authority,mode,artifact,files,runtime,limits,contract_sha256,source_pins,place`. Seven general objects contain Python SHA×1 and source-native SHA×1 each; bind all seven from the same registration pins. Root-policy exact keys: `schema,root_registration_path,job_tag,label,artifact,science_outcome,source_files,limits,profile,closed_scope`. All paths derive from the same fresh base.

## 4. LATE data and mutation boundary

Only observation/decision supply: holder PID/start/InvocationID; actual instance/hostname/boot/PID namespace equality; outer device/inode; ordered nine leaf `(name,path,device,inode)` identities; coordinator receipt SHA; native-manifest SHA equality; native-list SHA. The first four host values were already frozen EARLY and are comparisons, not late code changes.

Binder alone changes `enabled` and `exclusive_no_concurrent_writer` to true; guard `root_no_migration` to true; outer and leaf identities; `valid`/`dummy` closed-scope identities; and eight command digest slots. It reverses those allowlisted edits and compares the whole parsed objects. Authorities are serialized sorted/compact ASCII+LF; registration preserves prepared insertion order, indent 2, ASCII+LF.

## 5. Text multiplicities and two required card corrections

Binder requires, each exactly once in the card: heading `... — DISABLED\n`; sentence `This is an unformed administrative template, not a release or result.`; sentence `Final registration and holder topology remain unformed in this preholder card.`; PID/start/InvocationID/receipt/final-registration tokens. It also requires the post-EARLY literal substrings `Actual worker <instance>, hostname <hostname>,\n` and `\nboot <boot>,`.

Charged card has every listed item except the `Final registration...` sentence: literal search returns zero, so current bytes deterministically fail `replace_exact` before any candidate output. Minimal proposed insertion, once, without changing binder:

```diff
 Root cgroup2 mount and actual nine initially empty domain leaves must match
 the final registration's positive integer device/inode fields. No additional
 children, subtree delegation, write ACL, inherited cgroup fd, migration,
 replacement, external entrant, restart or concurrent ROOT writer is permitted.
 Mode bits alone are not ACL or complete ownership proof.
+Final registration and holder topology remain unformed in this preholder card.
```

Second concrete semantic mismatch: card says refusal policy `e3c5691f...c7845`, while the prepared registration pins its `preflight-policy.json` as `1a632269...f815`. No charged bytes establish that these are intentionally different. Minimal proposed correction for this prepared bundle is replacement of the card literal with the registration's `1a632269...f815`; do not claim policy contents.

ROOT's frozen replacement card `002d145f...a2ff` implements both corrections without weakening `replace_exact`: it adds the missing sentence exactly once, replaces the obsolete clock path/SHA with one-use EARLY placeholders, and replaces the inconsistent policy literal with one-use `JC2_PREFLIGHT_POLICY_SHA_PLACEHOLDER` plus an equality requirement to the registration pin. Its late token census is unchanged and exact: PID/start/InvocationID/receipt/final-registration each once. Its other EARLY tokens are each once. The three-hunk diff retains the heading, unformed sentence, worker/boot line shapes, nine-phase order, guards and caps. Verdict: **suitable constants-only prepared-card source**, provided ROOT binds the new policy placeholder to the actual registration pin and all other EARLY tokens before hashing. ROOT separately reports that uncharged policy-file metadata hashes to `1a632269...f815`; this review records that only as ROOT-supplied metadata and makes no policy-content claim.

## 6. Installer and final hash chain

Before holder, bind INSTANCE×2, BOOT×2, HOLDER_CUTOFF×3 and every old batch/base/stage/unit/cgroup/holder-argv literal. Retain binder tokens exactly: PID×1, start×1, InvocationID×1, install-release×1, final-card×1, install-manifest×1, final-registration×2. Binder additionally checks `jc2_base=FRESH_BASE`, one `= '<instance>'` line and one `= '<boot>'` line, then refuses any remaining `JC2_*_PLACEHOLDER` anywhere.

Late freeze chain: canonicalize nine authority bytes → insert eight authority hashes and observed identities into registration → hash registration → bind/hash card using holder, receipt and registration SHA → form `FINAL-INSTALL-INPUTS.sha256` as registration SHA, card SHA, native-list SHA in that order → bind installer with registration/card/manifest hashes and holder data → form summary last. Stage builder then commits exactly fourteen files: nine authority JSON plus registration, card, manifest, installer and summary. Only registration/card/manifest/installer plus native list are staged remotely; nine authority files remain expected runtime outputs.
