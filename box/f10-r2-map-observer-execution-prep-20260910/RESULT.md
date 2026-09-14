# Diagnostic worker retired; evidence and EBS retained

Completed 2026-09-10 15:22:49 UTC under DC's explicit idle-worker termination instruction.

The final ephemeral campaign worker i-0a30e221e2d8b2d29 (c7i.xlarge, 4 vCPU, 8 GiB) is TERMINATED. Its root volume vol-010c7206456e5ff17 (100 GiB) is independently AVAILABLE with no attachments. The final jc2fleet=1 query returned no nonterminal instances. The earlier nine-worker retirement and subsequent semantic worker retirement remain closed; eleven workers in total have been retired with their EBS data retained. Coordinator and separate formalization infrastructure were not inspected or controlled.

## Diagnostic outcome, not mathematics

The registered two-refusal observer started 15:11:44 and stopped at 15:12:00 with STOP_NONDECISION: mapped native file not pinned. The first refusal completed; the second reached probe-child observation and recorded /etc/ld.so.cache absent from the native file inventory. This is explicitly UNVALIDATED, non-atomic process metadata, not a coherent loaded-image attestation. It does not identify the unknown pathname in the earlier 14:09 semantic attempt.

No baseline, semantic mutator, controls6/10, positive mathematical checker or solver ran on this worker. The original actual coefficient packet remains checked-but-not-promoted. A future registration can address the observed missing native file with fresh worker-specific hashes; ignoring map checks or unchanged retries is not authorized.

## Custody before termination

Exact SYSTEM MainPID/ControlPID zero, original PID8389 absent, and exact cgroup absent were independently checked before initial custody intake at15:12:15 and again at15:19:34 and15:20:39. Custody was SHA/WHOLE-first; its21 file entries and the working/durable/source inventory were preserved.

The terminal harvest verified all57 hash rows (56 unique files, one repeated custody row), all13 installed input pins, all1225 native file hashes, and a fresh complete native metadata inventory. Files, aliases, directory entries, metadata and counts were identical after excluding only collector start/end timestamps. The native collector performs metadata inspection, not mathematical execution.

The observed cache file was copied post-observation and independently hashed:
abdf8ebc85486a018ad2f8f61d3f31ae829f99f29291d434958b679b7fce388d.
This is the subsequent file's hash, not a claim about its bytes during the process snapshot.

A complete archive of the exact /opt, /run, /var/lib task directories and staging directory was created, tar-compared against its source, made0444 and synced on EBS. It was downloaded, hash-checked, extracted under the new local harvest directory and all57 rows rechecked; the local archive was synced before termination.

- Archive: evidence.tar.gz, 477211 bytes, SHA a924bf36bd0f400e91827795895a11adb82b16a4643f48f21c3c58ff7a9bf765.
- Local extraction: harvest/ under this directory.
- Retained-EBS archive: /home/ubuntu/jc2-r2-map-observer-20260910T1500/evidence.tar.gz.
- CUSTODY.json SHA: 8b1112984ae6d95939669db1f32fb2aa8feacbdd19b56c1eb26dc382bd762678.
- Map record SHA: 191f90071bb5c6f75d0cb4b38e420e942496d4e4e1066aff3719736099bdfea7.
- Harvest script SHA: d0749b0f5a5cfcfb39b70997369cc62238ae749052dc076247cd2595c07a00c0.
- Harvest stdout SHA: 9550df7217579b5891c4b946d798239dbc2aaa526433c84aecc1ad94151bc40d; stderr empty.
- Termination response SHA: 29b00bcff5117e353a680ceb8d06b3986fc3a14724d84f4ebf8255c896e93928.
- Terminal instance status SHA: 28e208e4dce45ac4b6800ea9f3655df75ac5708c3aa228d75d215d308489d312.
- Retained volume status SHA: 23d84e8acd7909e7c0c67295971d4a7faca6cd286097564f63c9943bea6ada0e.

The exact root mapping's DeleteOnTermination=false and API protection=false were rechecked before the explicit one-ID termination at15:22:01. Instance termination and volume availability were independently confirmed15:22:33. Original SYSTEM15:27:15/20 timers were closed after custody; original USER15:35 termination timer was closed after confirmed termination at15:22:49. No deadline was reset, no idle instance retained, no volume deleted.

An initial local post-extraction checksum command used a nonexistent relative list path and failed without modifying evidence; the correctly rooted complete57-row check then passed before termination. All authored scripts and this record used apply_patch. The worker is not restartable; retained EBS and the local archive are recoverable evidence.
