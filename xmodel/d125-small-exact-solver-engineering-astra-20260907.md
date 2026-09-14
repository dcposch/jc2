# D125 exact solver engineering controls — actual worker pass

Status: **ALL_ENGINEERING_CONTROLS_PASS / INSTRUMENT ONLY.** Author `/root/model_productivity`, 2026-09-07. Frozen basis `0d39df3c9fd69c939a8420c54d03228b9077777d`.

All seven registered engineering jobs completed as intended on the authorized retained worker. Batch wall time was **3.909354025 seconds**,00:41:32.175667–00:41:36.085012 UTC. Expected RSS/file-limit failures were successful negative controls; no unexpected failure, repair or retry occurred. No full source was parsed, no full-client certificate was computed, and no `slimgb`, `std`, dimension, elimination or msolve call was made.

## 1. Scope, registration and unchanged inputs

Root's explicit GREEN authorized engineering controls only for the named D125 actual-degree75/125 client. It did not authorize a decision or verification phase on that client. The live independent code gate and root's separate live stream gate were not inspected. Registration is `box/d125-small-exact-solver-engineering-20260907/REGISTRATION.md`, SHA `eb5763793862e20fec76373ef8f09bbd0526672dffd545b6cff8a03418986af7`.

Fresh AWS/SSH checks matched running `i-0da0cebfc97c9fd54`, private172.30.0.56/public54.237.229.28, Owner `coordinator-factored-jacobian-20260906`, boot `69938ee6-48bb-4e45-bdf2-efb08c655368`, Linux/Amazon EC2 DMI, and EBS `vol-0eb6450d18ffa89f1` serial `vol0eb6450d18ffa89f1` mounted `/dev/nvme0n1p1` ext4 at `/`. Before deployment the exact new target was absent;20,207,722,496 disk bytes and257,396,972KiB RAM were available, swap0. The only remote writes were fresh `/home/ubuntu/d125-small-exact-solver-20260907/` and its `engineering/` subdirectory.

Deployed and pre/post verified unchanged:

- `driver.py`: `7f081576ea72005c2509ef2d575aa63b9fd53416987f3535ed520fd79fdc130d`.
- `exact.py`: `ca7630e39cb8c5b4aec671b2a83132502abd716c6826c30a4bbc03014ffdb6b3`.
- CAPRUN: `4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2`.
- Singular: `90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4`.

The new isolated harness `engineering.py` has SHA `fd011fe4a0dcacc733e222b47a0418f9d07de470d9f381c41adefa3c370471f4`. Its pre/post pin manifests are byte-identical, SHA `826960bd882e17f6f98ee52caa0098f6bb198287177d6409aff4fbebd9086e7a`. No shared installation or earlier producer stream changed.

## 2. Actual controls

The first control left a TERM-ignoring same-group descendant after the leader exited normally. The child allocated a96MiB buffer (temporary allocation may exceed that), crossing the64MiB sampled RSS cap. CAPRUN recorded **RESOURCE_CAP/rss**, runner rc125, while preserving leader rc0; validated the exact anchor before TERM and KILL; killed the descendant; reaped the leader; and reported cleanup complete. This demonstrates why the exited leader's rc0 alone is not job success. Peak sampled RSS184,700,928 bytes illustrates sampling overshoot; the separate512MiB AS ceiling remained in force.

Each inherited file-limit control imported the unchanged `driver.limits` function in an isolated interpreter, changed only the in-memory `CAPS.stream_bytes` parameter to4096, reapplied that same function, then execed a writer in the same PID/PGID. The execed writer checked inherited FSIZE `(4096,4096)` and core `(0,0)`, set SIGXFSZ to its default action and attempted4096+ bytes on one registered stream. Both runs ended with **SIGXFSZ25** (child rc−25/runner rc153), exactly4096 bytes in the selected stream and0 in the other. This is an actual lower-threshold control of the exact inherited limits path, not a source edit or a claim of whole-directory byte metering.

The frozen driver's `engineering_control` authority executed its10-second/512MiB control phase on actual Singular. Authority SHA is `8381ce10fe203183b6334ee95e83a3f29615c85af66840e80b2c1f9ba24c4093`; the120-second authority deadline was within the permitted450 seconds. It cannot authorize a solver phase. Actual input was `(0,x,0,x,1-x,0)`; no production client was loaded.

Actual Singular returned `size(I)=3`, **`ncols(matrix(I))=6`**, the complete six-entry engine list `(0,x,0,x,-x+1,0)`, and six lift entries `T=(0,0,0,1,1,0)`. Thus the size diagnostic counts nonzero entries here, while leading/interior/trailing zeros and duplicate positions remain in the indexed matrix. Do not extrapolate `size(I)` into a literal-generator count or silently drop those slots.

The exact parser maps this engine list to original zero-based indices `[0,1,0,1,4,0]`, combines duplicate contributions at their first matching original row, and verifies the full six-row identity `x+(1-x)=1`. This does not assume cofactor k is literal row k. Actual I/G/T delimiters, full row list, `CHECK 1` and terminal marker are retained; stdout295 bytes, stderr empty. This is only a toy identity, not a unit result for D125.

A separate10-second/512MiB actual Singular print control used161 rational terms of total degree160 in two long ordinary variable names, plus a70-digit rational numerator. Its23,012-byte stdout was parsed and compared exactly with the original expressions, including the rational coefficient. The complete actual control and long-output replays both passed normally and under `-O`; neither replay regenerated a full source system.

## 3. Terminal telemetry

Each registered job had10 wall/inherited CPU seconds and512MiB AS/RSS, except the deliberate64MiB sampled RSS trigger. Total batch budget120 seconds was not approached. FSIZE production constant remains64MiB per registered stream, with4096 used only in the isolated negative controls. CAPRUN itself does not meter output bytes.

| job | PID=PGID | start ticks | wall seconds | max sampled RSS bytes | outcome |
|---|---:|---:|---:|---:|---|
| descendant RSS | 12305 | 397391 | 0.573489027 | 184,700,928 | expected RESOURCE_CAP/rss |
| stdout limit | 12325 | 397455 | 1.179481877 | 10,702,848 | expected SIGXFSZ |
| stderr limit | 12356 | 397579 | 1.179954023 | 10,711,040 | expected SIGXFSZ |
| actual index/lift | 12387 | 397708 | 0.069156922 | 9,666,560 | NORMAL_EXIT/0 |
| long print | 12392 | 397722 | 0.069259460 | 9,523,200 | NORMAL_EXIT/0 |
| replay normal | 12398 | 397736 | 0.068880545 | 9,572,352 | NORMAL_EXIT/0 |
| replay optimized | 12404 | 397750 | 0.242775946 | 22,876,160 | NORMAL_EXIT/0 |

The intentional controller session was PID=PGID12301/start397382. Descendant12308/start397395 shared PGID12305. Identities retain argv, boot, cgroup `session-185.scope` and PID namespace `pid:[4026531836]`; CAPRUN receipts retain exact child identities and signal checks. At00:43:01.907149 UTC all **eight** owned groups—12301,12305,12325,12356,12387,12392,12398,12404—were absent. No unrelated process or root reviewer job was controlled or read.

## 4. Replay paths, hashes and custody

All remote artifacts are under the single fresh root above; matching local copies are in `box/d125-small-exact-solver-engineering-20260907/evidence/`. Every one of51 downloaded files matched its remote SHA and byte count,219,346 bytes total. Exact commands and authority are in the per-job receipt/launch files. The launch was the registered `setsid python3 -I -B engineering/engineering.py`; every arithmetic child subsequently ran through the pinned CAPRUN or frozen driver's CAPRUN path, without an unrecorded inner session.

Key artifact pins:

- Complete remote file/identity/group manifest `remote-custody.json`: `c93ae086413915547c180879dee960ec1efbc921ebf2c77cf9a14f6c3a22fc2c`.
- Local pull verification `download-verification.json`: `8e7d17a939471b14de2dde6d7a8db85352a01f6eff462570e82d1845c3af48a6`.
- `engineering/batch.result.json`: `8b7503d3443b612698efb325a40d4898c1f463862079ce31b15c77e62eb9d47c`.
- `control.stdout`: `fff5dfd6b2be427844ea898b95c8e159937761085ec2905b0327dc6871939922`; `control.sing`: `6395398474b3c57da1056a721aca7c0d1b0e9f0c38ece56a6e4c924a0c60dd2c`.
- `engineering/long.stdout`: `8dca03766fdfb658419caa9720a9a9c5361d6122c7adad1814114801f5241a78`; long input: `abb4bb69ddfd8e990d269f6833efc0df59b5df2e1aa8b9c5ed4647980909de41`.
- `engineering/rss.telemetry.json`: `6f3c7a5eb78f97ac5db768b6604ed3d116219537af5aa4dbba207fef4f2617a5`.
- stdout-limit/stderr-limit telemetry: `c0c2fde984bea0b50f21922947cfb7ba2bbce76854f780a63921097ef0c4064b` / `157ed1001457a4f0d1e8e91c9bf4ac47a8a2d8cdeb0c0b5bd90ee5464bb80e65`.

Full pre/post memory and disk snapshots are retained. Final disk free20,207,378,432 bytes, available RAM257,350,836KiB, swap0. Final AWS read still matched the same running instance, Owner and EBS attachment with `DeleteOnTermination=true`. Root retains instance custody; this task neither starts nor stops nor terminates nor retags it. Earlier sole-copy complete streams remain untouched on retained EBS.

These controls close the named engineering checks at producer-observed scope, not the independent code or complete-stream gates. Root must accept those gates and issue a fresh explicit solver GREEN before a full-client attempt. No authority expansion or automatic continuation follows. All local/remote writers and harvest processes are terminal; **STOP/IDLE**.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9143`.
- Body SHA-256:
  `58c916803a32a21b9ca6b0d69a7ca04e8c2c18e453302e73336c7a0c38a8ccf3`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
