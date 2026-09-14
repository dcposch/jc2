# D125 normalized physical-J pilot: complete construction and import only

2026-09-06. Producer `/root/model_productivity`. **TERMINAL / INSTRUMENT RESULT ONLY.** One complete normalized original-source construction and strict self-replay succeeded, followed by one successful exact-Q Singular import. No basis computation, dimension query, elimination, solve, unit/properness claim, or counterexample witness occurred.

## Measured outcome

| Stage | Exact terminal outcome | Wall time | Peak sampled process-group RSS |
|---|---|---:|---:|
| Complete construction plus strict whole-stream self-replay | CAPRUN `NORMAL_EXIT`, child 0, empty stderr | 3.470506262 s | 20,692,992 bytes |
| Singular exact-Q import only | CAPRUN `NORMAL_EXIT`, child 0, empty stderr | 15.085384458 s | 7,211,585,536 bytes |

Construction alone used approximately 1.91 s in the exporter's manifest. The import stdout is **exactly** `D125_IMPORT_ONLY_NO_SOLVE` plus newline, 26 bytes, SHA `eda604687fb0698100feeca56069c07feeff4b464eb9918ec6e430485290d3f2`. Both return status and the whole stdout/stderr were inspected; no successful-marker-only inference was used. Import memory is about 6.72 GiB, despite the source stream's small disk footprint. No inference about a later basis computation follows.

The literal stream contains 2,123 variables: 571 P coefficients, 1,551 Q coefficients, and the original degree-guard inverse. Counts are now **measured for this exact export**, not merely previous support bounds:

| Row kind | Emitted rows | Identically zero rows | Literal terms |
|---|---:|---:|---:|
| Original terminal jets | 189 | 0 | 3,266 |
| Five fixed pins | 5 | 0 | 86 |
| All ordinary physical Jacobian slots | 3,792 | 55 | 875,119 |
| Original degree guard | 1 | 0 | 2 |
| Total | 3,987 | 55 | 878,473 |

Thus 3,932 emitted rows are nonzero; this is not a rank or dimension assertion. The 55 zero physical rows remain in both serializations. Physical term count includes the constant `-1/5` target term. The only unused variables are zero-based IDs 378 and 1601, exactly `P_u0_v0` and `Q_u0_v0`; both additive constants remain in the ring. There is no silent variable removal.

## Exact contract and authority

The unchanged exporter is the preflight's literal original-source presentation over Q. Every original terminal jet, all five pins, the positive-Jacobian target `J(P,Q)=1/5`, every physical output coefficient including zeros, and

`Z_degree_guard * P_u15_v60 * Q_u25_v100 - 1`

remain present. Normalized support is the original degree/weight support intersected with the two reviewed pure-vertical-top restrictions. No independent h variables, additional gauge, coefficient elimination, residual subset, pivot assumption, or circuit reinterpretation was introduced. The Singular ring uses the same complete variable order and global `dp` ordering.

Root explicitly authorized this one normalized pilot after its independent code/toy replay and promotion of the normalization at **characteristic-zero field-point/nonemptiness scope**, `AUDIT17(bbbbbbbbbbbbb)`. The charged normalization gate SHA is `b45011178fb282fe4f9093ac34cec2bbece6c66248f1121c067622228c75cb71`. This task relies on root's reviewed license; it did not re-review that proof or read any live 14:35 cross submission. Field-point normalization is not promoted here to equality of the original and normalized ideals or a scheme isomorphism.

The sealed exporter and its conservative `PROVISIONAL_UNLICENSED` header were deliberately **not edited**. Supplemental `authority.json`, SHA `9c326201e42fde2b4f4567994e809d3f69522ebba14b1c63b0b9eb737a73827a`, records the subsequent root license, exact mode, source hashes, instance/cwd and caps. It supplies `root_green:true` and pins:

- Exporter: `a8092908c9f4916306e24fdeca622426f8e6be09ab4f3d0d19e7488e05eca2f9`.
- Source contract: `0c5270a432a6336c17c4693034e36cb496f139c3267843e3ac06628ec8c4b255`.
- Source-contract gate: `a802587179b6f105bb47555ceb0e6a1d20c94c68a76c6ac4a26bbea1fce7b4e4`.
- Normalization producer: `8ea55aaf26acbd4992aee9d14cce8712fda1c7590cd876ee974194c76bb3ad9e`.
- Unchanged reviewed CAPRUN runner: `4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2`.

The exporter/test source and source reports were copied without modification into a fresh worker directory; hashes were rechecked before execution. Payload checks reject the wrong Linux host, EC2 vendor/instance, boot ID, EBS serial, cwd or symlinked task directory, changed source/runner/binary pins, and missing successful construction before import. Actual wrong-host and wrong-cwd controls both failed before production arithmetic or output creation.

## Worker, bounds, and process custody

Only root-started instance `i-0da0cebfc97c9fd54`, private `172.30.0.56`, public `98.86.236.56`, hostname `ip-172-30-0-56`, was used. DMI identifies Amazon EC2 and that exact instance. Owner tag remains `coordinator-factored-jacobian-20260906`. New boot ID is `235391e8-e646-4ac8-b319-8e609c031bf4`. Root retains the instance; this lane performed no start/stop/terminate/retag or other-worker action.

Fresh remote task root is `/home/ubuntu/d125-physical-export-pilot-20260906`, physically on `/dev/nvme0n1p1`, ext4 mounted at `/`, backed by sole disk serial `vol0eb6450d18ffa89f1`. Readiness showed approximately 20.28 GB free disk, 263 GB available memory, zero swap, and no inherited campaign arithmetic/autostart owner. The historical complete-J source files were rehashed against their retained custody pins: `complete_checked.sing` SHA `50792efed4a5ed47cf2da5bf1f0d3b65e4f68efcba8e528b7dc29a541b72e091` and `complete_export.generators.jsonl` SHA `39ea3365c8c83916c5f813be0b7719374dcad131cdd4b10ed24d25516bfae75f` matched. They were not edited or used as D125 inputs.

A custody-I/O incident is retained explicitly: the first read-only audit's local SSH timeout fired after 60 s while remote reader PID/PGID 1421 was D-state reading cold retained artifacts, at about 18 MiB RSS. No solver or production arithmetic had started. That reader subsequently exited without a signal; its absence was checked. A fresh read-only readiness capture then completed in under a second with all hashes exact. This was not a repeated production attempt or an enlarged computation.

The full CAPRUN source, including cleanup/reaping paths, was read and hash checked. Construction and full self-replay shared **one** 600-second wall cap, 8 GiB sampled aggregate RSS cap and inherited 8 GiB address-space limit, plus the exporter's 1 GiB aggregate JSON/Singular byte cap. The subsequent import had one 300-second wall cap, 16 GiB sampled RSS cap and inherited 16 GiB address-space limit. Sampling interval was 0.05 s; sampled RSS is not an exact instantaneous maximum. Neither cap fired; there was no retry or automatic enlargement.

- Construction PID/PGID **1846**, start ticks **45904**, ran `21:41:57.406474Z–21:42:00.876976Z`, session-11 cgroup.
- Import PID/PGID **2070**, start ticks **50275**, ran `21:42:41.114393Z–21:42:56.199772Z`, session-14 cgroup.

Each payload saved PID/PPID/PGID/start ticks, boot, namespace, cwd, cgroup and argv before work. Import used the same PID through `execv` into pinned `/usr/bin/Singular`; its binary SHA is `90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4`, version 4.3.2 (Debian 4.3.2-p10). The retained receipt is pre-exec identity plus the checked exec path and terminal output; there was no separate successfully captured live `/proc/exe` snapshot after exec. Both exact process paths and **all members of both production PGIDs** were absent at terminal harvest.

One existing telemetry caveat must not be concealed: CAPRUN's normal branch calls `process.wait()` and returns the authoritative exit code, but leaves `termination.leader_reaped=false` and `cleanup_complete=null` at their cleanup-path defaults. Here `NORMAL_EXIT`/child 0, the read full source and explicit post-run group/PID absence are the normal-completion evidence; those default fields are not falsely described as true. The runner was not patched in this task.

## Tiny controls and exact retained artifacts

Both local and remote normal/optimized toy suites passed all 17 rejection controls, under their 25-second/512MiB limits. No production arithmetic ran locally. Actual orphan/cap controls used the pinned runner: a leader exited while its TERM-ignoring child stayed; the 0.5-second wall cap produced typed `WALL_TIMEOUT`, validated TERM then KILL, leader reaping and no remaining live same-group member. Local control PGID was 2198104; remote control PGID was 1780. Wrong-host and wrong-cwd payload controls also passed. The original exporter/test files remained unchanged.

The full JSON/Singular inputs remain read-only on the registered EBS volume:

| Remote relative path | Bytes | SHA-256 |
|---|---:|---|
| `complete/literal.jsonl` | 20,560,987 | `8a059438a525a9cc53bb55163dfe74e4931c4dca10f111a2466672ae99fcaf52` |
| `complete/import.sing` | 23,373,677 | `9b6eb808aee27e08f0ee7b263755cefa7e9463c3d8ebd4b03b0664cb57563f4d` |

The combined input size is 43,934,664 bytes. JSON prefix digest is `da8f3cc8339b67566f3fe5a4e63038fafb5dbb2254202a12e68a7b5be00f4b80`; complete manifest SHA is `f7e176b42f9699ebb3d575f0d598a301f2b05ad6646b2ec104f9eec822174937`. Full input hashes were checked after construction, before import and at terminal harvest. Nothing was modified after generation except removing write bits.

Local task root `box/d125-physical-export-pilot-20260906/` contains transport/identity/cap receipts, source pins, wrong-host/cwd failures, tiny controls, and a 624,640-byte metadata archive. `verify_archive.py` verified its hash, safe regular-member paths, custody hash and all 71 small artifact hashes before extracting them under `evidence/`. The only excluded archive files are the two explicit dense inputs above, retained remotely. Charge:

- `evidence/custody.json`: `dcef8e668c08b50d310a71b78f61ca31a12a00edee65dd4f72a9dd682fcdddf8`.
- `evidence.tar`: `262e4aacda074bf7e1c426e454d56d8d06f6ddf079e78a63273dc57b2703ffe8`.
- `archive-verification.json`: `ba1373047534b8210e8a7b685066585d2d12a32fe7b3cbd64642fd1042027225`.
- `evidence/construct.telemetry.json`: `ccf2ffcc0276d99fb97deac2585312711e846780b2a08e908fbc435636ae6e84`.
- `evidence/import.telemetry.json`: `11a4745e8c00080580e6653697e9021de62b086265f2f6aece3763e6322bcd07`.
- `local-controls/result.json`: `d5acff3b3605ed581cb3176d10aacb41ee485e34dbf7fa95bdee877c100f317b`.
- `evidence/remote-controls/result.json`: `16f9d384803bc9bd2f521092f310fa5ab6b3aacbd7009d4d8462373847c1e822`.
- `guard-controls.json`: `9c0f498da0b376d4b6dcb5b37e594b4e24e6e563330c095210a36548409db9e1`.

All production and tiny-control arithmetic writers are terminal, and metadata collection/transfer finished before publication. No prior artifact was overwritten. EBS volume `vol-0eb6450d18ffa89f1` has **DeleteOnTermination=true**: a recoverable instance STOP retains these files; termination would not be safe custody. No important task artifact is on ephemeral storage. Root may perform its own final audit and recoverable stop; this lane has not done so.

## Claim boundary and stop

The result is a measured exact-source exporter/importer instrument: this complete normalized presentation is cheap to construct and fits the bounded exact-Q parser. The strict replay reuses the same coefficient formula; it is **not independent certification of the full stream**. A different-model/source-independent gate remains root's next validation decision. Parser completion is not a unit/properness certificate, an ideal dimension, a polynomial pair, or a JC2 result. No inference transfers from old degree-99 jobs or historical receiver slices. No further computation is launched by this packet.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11803`.
- Body SHA-256:
  `71d43774e899e6ae5da3f66c38156593b30380098da0c6d3a12aefae8e88d260`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
