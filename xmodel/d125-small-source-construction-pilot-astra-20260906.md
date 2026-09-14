# D125 small-source construction/import pilot — all six complete

Status: **ALL_SIX_CONSTRUCTION_IMPORT_COMPLETE; INSTRUMENT ONLY.** Author `/root/model_productivity`, 2026-09-06. Frozen basis `0d39df3c9fd69c939a8420c54d03228b9077777d`.

The registered six sequential clients all completed full construction, strict same-formula JSONL replay and exact-Q/Q(rho) Singular import. Total combined batch wall time was **15.891275749 seconds**, from **23:42:45.952363 to 23:43:01.843624 UTC**, within the single600-second budget. No production cap, failure, retry, code edit, equation reduction or solver occurred. Every full stream retained660 ordinary Jacobian rows and105 negative polynomiality rows.

This is not independent all-row certification, a basis/dimension calculation, a properness result or a JC2 proof/counterexample. Exporter implementation remained provisional under its separate live review. No live review body, code, log or receipt was read. The gate of the actual complete streams is the next required independent step; no additional computation is authorized by this report.

## 1. Authority, host and frontier

Read the whole binding registration `box/d125-small-source-construction-pilot-20260906/REGISTRATION.md`, SHA-256 `82d2db220affc538e5076707061a8b38c57b736a178dcb8c6d368ba5760e918c`. Root—not this lane—started exactly `i-0da0cebfc97c9fd54`. Fresh AWS and SSH/DMI checks matched:

- private IP `172.30.0.56`, current public IP `54.237.229.28`, hostname `ip-172-30-0-56`, Linux / Amazon EC2;
- DMI `board_asset_tag=i-0da0cebfc97c9fd54`, boot `69938ee6-48bb-4e45-bdf2-efb08c655368`;
- Owner `coordinator-factored-jacobian-20260906`, r7i.8xlarge;
- sole disk serial `vol0eb6450d18ffa89f1`, AWS EBS volume `vol-0eb6450d18ffa89f1`, `/dev/nvme0n1p1` ext4 mounted at `/`;
- fresh task directory absent before deployment;20,222,709,760 free disk bytes, approximately263.6GB available RAM, no swap, no inherited campaign arithmetic in the process audit and no campaign timer.

All writes were under fresh remote `/home/ubuntu/d125-small-source-construction-pilot-20260906/` and this task's local box. No earlier worker directory or source artifact was changed. The installed classical gate was copied unchanged and run with **actual source degrees75/125**, not receiver degrees15/25: `NOT_CLOSED_BY_THIS_GATE`, gcd25 and actual maximum125. This is only an inconclusive classical admissibility check, not a global openness assertion. Exact gate output/pin is retained in `evidence/frontier.json` and the deployment manifest.

Unchanged producer pins were checked locally, after deployment, before each case and through the generated manifests: exporter `9fd003e420f3ee069f1ed1c06a365e5b4500d361bc3951f2f8f17ef733ab3703`; baseline `ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53`. Each case authority records exact registration, observed instance/cwd, nonempty registered job, deadline, caps and the normalization/lift/lift-gate pins `cd69c238…`, `433cc2fe…`, `4295593a…`. These actual authority files are retained verbatim. Lambda2/lambda3 remain free, zero allowed; common c,z guards remain; unequal c stays its fixed nonzero field value; no origin guard or extra c=1 gauge was added.

## 2. Fresh runner regression and enforcement

The full reviewed CAPRUN source was read and its immutable SHA matched `4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2`. A fresh no-CAS caller identity test passed, matching its payload PID/PGID to CAPRUN. A separate fresh regression forked a same-group TERM-ignoring descendant while the leader exited. CAPRUN retained the unreaped identity anchor, validated it before TERM and KILL, typed the expected `WALL_TIMEOUT`, killed the descendant, reaped the leader and completed cleanup. Regression group1967 had start ticks44634; elapsed1.271600129s includes the1-second trigger and bounded cleanup. Both controls' groups were subsequently absent. This expected control timeout is not a production failure.

Each builder had180 wall/CPU seconds maximum,8GiB address space and aggregate exact-group RSS, and256MiB aggregate output. Each import had60 wall/CPU seconds maximum and8GiB AS/RSS. The next cap was bounded by remaining combined600-second budget; no cap enlargement occurred. The batch measured construction, replay, import and intervening checks together. RSS telemetry is sampled, not a hard instantaneous RSS bound; AS limits are separately enforced. The import wrapper used `exec` in the registered child PID/PGID, never an extra unrecorded session.

All12 production jobs have CAPRUN `NORMAL_EXIT`, child return0 and null error. Their stderr files are empty. Each import stdout was strictly the registered marker plus an integer (`554`, `599` or `719`); these equal the corresponding nonzero generator counts, not a mathematical ideal verdict. No `std`, `slimgb`, dimension, elimination, solve or msolve command was invoked. Singular package was `1:4.3.2-p10+ds-1.1build1`; its exact binary hash was checked before every import and is pinned in `readiness.json`.

## 3. Complete stream observations

Qrho below means the genuine coefficient field `Q[rho]/(rho^2-3rho+1)`, not split rational-component equations or a chosen numerical embedding. Every case has105 literal negative rows and660 J rows, plus the preflight's fixed-map residuals and guards. Every footer reports **no unused variables**.

| case / field | variables | rows | terms | zero rows | JSONL bytes | Singular bytes |
|---|---:|---:|---:|---:|---:|---:|
| unequal / Q | 269 | 803 | 27,577 | 249 | 1,213,487 | 707,662 |
| unequal / Qrho | 269 | 803 | 29,462 | 249 | 1,284,762 | 776,459 |
| common-3 / Q | 295 | 816 | 32,699 | 217 | 1,397,244 | 806,909 |
| common-3 / Qrho | 295 | 816 | 34,820 | 217 | 1,490,246 | 919,376 |
| common-4 / Q | 371 | 816 | 44,960 | 97 | 1,843,792 | 1,080,176 |
| common-4 / Qrho | 371 | 816 | 47,621 | 97 | 1,961,224 | 1,221,537 |

The zero rows remain explicit in JSONL and literal import text. The Singular in-memory ideal's size omits zero generators; this is why its diagnostic is smaller than803/816. No omitted equation is inferred from the size diagnostic. The authoritative byte streams and their same-formula complete replay are retained for independent examination.

| case / field | construction PGID / seconds / max RSS bytes | import PGID / seconds / max RSS bytes |
|---|---|---|
| unequal / Q | 1997 / 1.748353541 / 22,745,088 | 2031 / 0.241158370 / 21,909,504 |
| unequal / Qrho | 2039 / 1.860185613 / 22,663,168 | 2075 / 0.414523915 / 26,742,784 |
| common-3 / Q | 2086 / 2.097239680 / 23,388,160 | 2127 / 0.182390041 / 27,770,880 |
| common-3 / Qrho | 2134 / 2.152175669 / 22,827,008 | 2175 / 0.183317843 / 27,996,160 |
| common-4 / Q | 2182 / 2.729800228 / 22,876,160 | 2233 / 0.242341890 / 41,005,056 |
| common-4 / Qrho | 2241 / 2.835643444 / 22,937,600 | 2294 / 0.303841284 / 49,819,648 |

Each registered production leader PID equals its PGID. Exact start ticks, UTC start/end, argv hashes, authority files and receipts are in the per-case `construct.telemetry.json`, `import.telemetry.json`, `*.receipt.json` and identity records. Construction includes full self-replay; the table is not a solver timing forecast.

## 4. Exact complete-file paths and hashes

All paths below are under remote `/home/ubuntu/d125-small-source-construction-pilot-20260906/`. Basenames are deliberately unchanged from the exporter. JSONL/Singular files were hashed after construction, rechecked after import and rechecked at final harvest; all matched.

- `unequal-rational/client-unequal-rational.jsonl`: `b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac`.
  `unequal-rational/client-unequal-rational.sing`: `c089c33301e3889e0c20527386719f411907cf2957ecfad3d93c65f7be24e718`.
- `unequal-golden/client-unequal-golden.jsonl`: `ad83add3ccdeb56914cf73ab06fe733f7b89aa984e586bb973dde04ca471613b`.
  `unequal-golden/client-unequal-golden.sing`: `77f127a903152cc52ebb2fd40d8e0d7ca76aeba2fe7306b4e87872189c9c28ec`.
- `common_3-rational/client-common_3-rational.jsonl`: `cb6dd5a002db764412ed5f755d868ef11d91eaa20835a1d981e4fabe9d0eb177`.
  `common_3-rational/client-common_3-rational.sing`: `1cf13975b7b4daea1f895defa38aa777af861d804d051605c610fa61d483f632`.
- `common_3-golden/client-common_3-golden.jsonl`: `7fa9f5d1be4aca6745f67a1e4a3dcc495f10ec6612fa13c9d87b01890643bc2c`.
  `common_3-golden/client-common_3-golden.sing`: `101c4562a87f1ae5cff9745470f63f6a4fc0995ab7f9c54115bcb76f4595a607`.
- `common_4-rational/client-common_4-rational.jsonl`: `276ee6f4c23df9577cbeb832f06e84ae1c06dcf29b960e067d08083d3a0db13e`.
  `common_4-rational/client-common_4-rational.sing`: `0fde2d1d3cfcc3659f31431bbc2dca8ea506a870c6309e73217f4cd12b68ab7c`.
- `common_4-golden/client-common_4-golden.jsonl`: `3e897ad6578a25aa0ce90e16ae8ab68c4ddf94f5bc2426045792982bf9ea892e`.
  `common_4-golden/client-common_4-golden.sing`: `addff558c331a1e963e5a764feb192f6c3dc57a9e2b3a1b37aa355d3bcbd0f7b`.

Each directory also retains its `authority.json`, complete exporter manifest, header/footer copies, `case.result.json`, constructor/import stdout/stderr, telemetry and caller receipts. The root directory retains all immutable code, registration, readiness/frontier results, regression/descendant identities, full batch result and final custody. No large complete stream was pulled to the coordinator host.

## 5. Terminal custody and handoff

Final read-only process audit found **all15 owned groups absent**: controller1957; regression1962/1967; production1997,2031,2039,2075,2086,2127,2134,2175,2182,2233,2241,2294. The regression descendant shared1967. Every leader was terminal/reaped through the runner path; full exact identities are retained. Harvest and evidence-download subprocesses also finished before this report was sealed. No task writer or arithmetic process remains.

Root retains the **RUNNING** instance and sole complete streams on EBS `vol-0eb6450d18ffa89f1`; the final AWS read still matched running state, Owner and volume. `DeleteOnTermination=true` is explicitly recorded: **do not terminate the sole-copy volume**. A root-authorized STOP preserves EBS; public IP may change on restart. This lane neither started, stopped, terminated nor retagged any instance. No other worker, shared ledger, protected project or earlier output was changed.

Compact local custody is in `box/d125-small-source-construction-pilot-20260906/evidence/`;109 compact code/metadata/log/header/footer files were pulled, every pre-existing remote manifest pin matched. Full JSONL/Singular and remote bytecode remain on EBS. Key pins:

- `evidence/custody.json`: `601643fcd066c19a24b04e22a0374c7e9fd5f106b0bfb5be43c695eb8c1b23b9` (all complete-file hashes and exact case telemetry).
- `pull-manifest.json`: `ad299f0e5e212532adb0d599ada97975fa867a5239967cd8f8e4f36e8e9a077f` (compact local file pins).
- `evidence/batch.result.json`: `c967b6424c30379e3b893034997842312c5e81b10c295c9278bf07daa3026045`.
- `evidence/terminal-jobs.json`: `091c1289fefe047ceaf9b8ab6ef6948fbc3f956ee67b995a4972b7e4999c37c1`.
- `evidence/regression.json`: `f35ff7459c615d13d4152d778cb1c813346f7f53d08fd351b9353babaa207eb4`.
- fresh caller `pilot.py`: `aa9a255bfb74d148b0799f5207354a6eda62a6c9b9a9e6430ad7647bbaa7dba5`; import/control `payload.py`: `50df2db28aca0bfcfbb7f926d4cc72bcce3be0bbb61512d3248b1b0488e54a7f`.

**STOP/IDLE.** Required next gate is independent all-row and Singular semantic verification of these exact streams. No mathematical promotion or solver commitment follows from this instrument pilot alone.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11604`.
- Body SHA-256:
  `72daf7656dc12c4444dea874b00a6b6653e362443888b563fd0977a2ee73368f`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
