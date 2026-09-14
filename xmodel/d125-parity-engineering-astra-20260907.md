# D125 parity actual-host engineering: terminal PASS

2026-09-07. **Exactly two authorized engineering controls passed; no source access, production constructor/metadata/replay, CAS or solver ran.** Root GREEN was `box/d125-0220-root-harvest-20260907/PARITY-ENGINEERING-GREEN.md`, SHA `4e38e81907b4e3c14e5a7b790ae8afbd1065121e68dff49f3e780d7cce5ac981`. This report does not authorize the subsequent construction pilot.

## Host, scope and execution

Fresh readiness at03:39:26 confirmed Linux/Amazon EC2 `i-0da0cebfc97c9fd54`, hostname `ip-172-30-0-56`, boot `1a830d1e-1fa2-47f3-98bc-8c26c8cb8453`, EBS serial `vol0eb6450d18ffa89f1`, ext4 root mount `/dev/nvme0n1p1`, zero swap, approximately251385MiB available memory and19703484KiB disk free. Owner and AWS attachment were root-verified in GREEN. Python and prlimit hashes matched it. Only standard user services and this diagnostic session were present. The new directory was absent before creation.

Deployed only the six unchanged registered files, exact REGISTRATION.md (`9435f425ddd135846480dd1cdb08674de3b376803a1f73e93804a546c5b5d107`) and frozen engineering/host_control.py (`f91a2c250689330a6d8155a5704ca1b703179cb342df686d683442c858798860`) into `/home/ubuntu/d125-parity-compression-pilot-20260907`. No older artifact was overwritten. Batch orchestration was supplied over SSH stdin and is preserved locally as batch.py; no extra remote code file was installed.

Each fresh engineering authority had the exact boot, job, code/registration/source/symmetry/gate pins, engineering-only schema/path,10-second CPU/wall and512MiB AS caps. The prlimit prefix and authorize both gave **128MiB FSIZE per regular file**, core0. No aggregate log bound is inferred. Source hashes were carried as authority data; **the source input was not opened or hashed**.

| Control | UTC start–end | Payload PID/PGID | Result | Elapsed | Peak sampled group RSS |
|---|---|---|---|---:|---:|
| authorize |03:41:00.955159–03:41:01.024598|1698/1698|NORMAL_EXIT, child0|0.069443052s|10104832 bytes|
| descendant RSS |03:41:01.098180–03:41:01.669401|1702/1702|RESOURCE_CAP/rss, runner125|0.571223873s|161075200 bytes|

The batch, including receipt checks, took0.792121869 seconds, below30. There was one attempt per control and no retry. Authorize ran the real frozen authorize plus only tiny Q arithmetic, with production=false. Its132-byte stdout reports construction_invoked=false/source_read=false. Both stderr files are literally empty.

The RSS fixture's parent exited0 while descendant1704 remained in group1702, ignored TERM and allocated96MiB. CAPRUN verified boot/start identity before TERM and KILL, sent both, reaped its leader and recorded cleanup_complete. The64MiB RSS threshold is sampled; observed transient overshoot to161075200 bytes is disclosed, not mislabeled as a strict memory ceiling. Both phases had512MiB AS limits. Normal-exit CAPRUN leaves the termination-only leader_reaped field false; its normal branch's authoritative wait, child0 and subsequent absence establish normal completion, not that unused field.

## Exact custody and verification

Controller1696 had start_ticks31573 and group1696. Runner PIDs1697/1701 had start_ticks31577/31591. Payloads1698/1702 had31581/31596; descendant1704 had31601. All identities record boot, cgroup `0::/user.slice/user-1000.slice/session-8.scope`, PID namespace `pid:[4026531836]`, hostname, argv, UTC and actual limits. Exact commands, authority hashes and starts are in the two launch records; no live output was interpreted.

Receipt-first terminal harvest copied21 files and verified every byte size/hash against the worker. A separate tiny local checker passed normally and under `-O`, including actual argv digests, limit maps, authority/registration pins, stream hashes, statuses and descendant cleanup. Fresh03:42:10 read-only custody found **all six task PIDs and groups1696/1698/1702 absent**. Post-pins of all deployed charged files matched. `authority.json`, `construction.jsonl` and `replay-result.json` at the worker root are absent.

Key immutable evidence under `box/d125-parity-engineering-20260907/evidence/engineering/`:

- Authorize authority: `10e1aff627240690c5ff70519707b26af74591bf83895f78016d3bd0cdc0edc9`; telemetry: `4ef65f88cadc3e761738c38bf6f5bc81ddeb559988af75a7cf86286496e8eded`.
- RSS authority: `caf761c415cddbfa4b9151b337b71d022282a802628ebe173cce27b361cd5b5d`; telemetry: `af207480323419bf81c5381cdb9b29a8ac2be9460a552abb5d50e2cbef994713`.
- Batch result: `64b803194c31dd368eb9055dfc73f26e4d87bd46ecac864d16dcfeb2393e267b`.

The owned pins.json, remote-custody.json, custody.json and local-replay.json retain the complete file/hash/process record. The input source remains on retained EBS `vol-0eb6450d18ffa89f1` with DeleteOnTermination=true: **never terminate or delete it**. Root retains instance custody and STOP authority. No instance-control action was taken. All required remote reads/writes and local subprocesses are finished; all writers idle on publication. **Engineering instrument PASS only; no mathematical result or production GREEN follows.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5124`.
- Body SHA-256:
  `84a50bb5719cad50ac003357030cca043d8f72494edfda577d3c1254bc480d16`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
