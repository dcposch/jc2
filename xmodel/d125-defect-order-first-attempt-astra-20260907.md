# D125 unequal/Q matched three-row-order attempt

Status: **TERMINAL INCONCLUSIVE — WALL_TIMEOUT; no basis/certificate.** 2026-09-07. Exactly one complete-source weighted-order attempt was made. No verifier, retry, alternative order, specialization, gauge, subset, expanded reconstruction or further solver was launched.

## Outcome

The frozen caller charged all **269 variables and 803 original literal equations** to exact-Q Singular slimgb with the approved W1/W2/W3/dp order. It ran from **02:25:25.143136 to 02:30:25.218762 UTC**, 300.075626885 seconds including parsing and cleanup. The outcome was **WALL_TIMEOUT**, not a memory cap: maximum sampled group RSS was **635293696 bytes**, about606 MiB, under the16-GiB cap.

The terminal receipt reports runner124 and child exit1 after the cap's validated TERM. Identity matched immediately before the signal; no KILL was needed; leader reaping and group cleanup completed. Stderr was empty. Stdout contains `I_SIZE 554`, all803 consecutively indexed I rows, `I_END`, then `halt 1`. There is **no G_BEGIN/G_END, T block or terminal decision marker**. No coefficient/certificate arithmetic was performed locally; the post-terminal local check only verified copies and framing.

The earlier same-client dp attempt also reached its300-second cap without a G block, with sampled maximum RSS1797402624 bytes. The present order used less sampled memory in this bounded run but still supplied **no ideal decision**; this does not establish faster convergence or a surviving component. No third order-only solve is authorized.

## Exact authorization and source scope

ROOT GREEN was read and hash-verified before action: `box/d125-0220-root-harvest-20260907/ROOT-GREEN.md`, SHA `da617e166465902ec7c40a9f115d4cfd95cfabcb1a76fdf6ef5a3574212a9e99`. It records acceptance of the complete source, sufficient lift contract, order theorem, Sol instrument delta and actual-engine controls. No live gate body/code/receipt was read.

Fresh local registration `box/d125-defect-order-first-attempt-20260907/REGISTRATION.md`, SHA `eb0e08a8e97fdca7facdac709b9d2d7d455f2e1dfe5b045184f0deda3619f7c5`, and fresh solver authority SHA `888b05c16d69cd971bc2ce8e3247fab04b4a16d762e1ccd55c3d82bd68d09694` were frozen before execution. Authority schema is `jc2.d125-defect-order-solver-authority/v1`, mode solver, interval **02:25:24–02:32:54 UTC**; its exact pins and accepted dependencies are retained in `solver.authority.json`.

The source comprises660 Jacobian,105 lift,31 fixed-map and7 guard rows, including249 literal zeros. Receiver polygons are A:(0,0),(0,15),(9,6),(2,1), B:(0,0),(0,25),(15,10),(1,0), with the entire prescribed faces. The ordinary lifted Keller pair has **actual total degrees75/125**, partial-u15/25 and partial-v60/100, hence finite source support bounds; receiver15/25 is not its actual Keller degree. The fresh classical frontier check returns only **NOT_CLOSED_BY_THIS_GATE**. Its preserved `frontier.json`, SHA `4d06a3e1fafe6ab28be421028987c3e3ec298633160498f2d446dbea7f262c44`, asserts neither existence nor viability.

Source JSONL remains `b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac`; original Singular remains `c089c33301e3889e0c20527386719f411907cf2957ecfad3d93c65f7be24e718`. The source parser still validated its original dp declaration and every literal source equation. Only the executed ring's first line was adapted. Terminal read-only custody compared the complete ideal suffix byte-for-byte: unchanged, SHA `6caad2b2da147f131b26c4002c7e0fcf2167bb1c28dde5b326a46bc9d6b2ccd7`. The new ring line matched `d894d6427d39b774c403165c83bffddbe993b96345ee00d652f5af7a06219bca`, for descriptor `64c212c26a9883d1c0f674b93f0246f67e22a8b742b643c6628fd3c14014db66`.

Frozen code/binary pins were checked remotely before and after: driver `944d5a840b6e4a81e89e5bcfa0ce6e6e54684ece70f182499735b9aa8571faec`, exact checker `f452a1f6a3dfcc534a14a0d2b1f162589fc928973aff5a91f7faaa88921039af`, helper `d5031c04fc7fdfec1fc57285b7538747b4d0aae25fae5ac140439d01dbd99ca3`, CAPRUN `4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2`, Singular `90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4`. None changed.

## Process and artifact custody

Worker: i-0da0cebfc97c9fd54, private172.30.0.56, boot `375d1a40-5988-4999-8cb7-a5427ad3b3a0`; EBSvol-0eb6450d18ffa89f1 remains under root's STOP/never-terminate custody. Only the existing `/home/ubuntu/d125-defect-order-solver-20260907/` frozen instrument and fresh exclusive solver.authority/decision paths were used. No older source or output was overwritten.

Caller PID=PGID2176; CAPRUN parent2177; actual Singular PID=PGID2178/start_ticks167832, cgroup `session-19.scope`, PID namespace4026531836. The live record is SHA `fc68452d7dfabccc47bfa1ca0f3697dd5417fcbf49035fa05feb301b383cec12`. Only process metadata was read while live. Limits were300wall/CPU seconds for decision including conditional lift,16-GiB AS/sampled groupRSS,64-MiB inherited per-stream FSIZE/core0, with the unused optional120-second verification within450total. No normal complete decision existed, so the verifier was not run.

Receipt/telemetry were consumed before terminal output. At **02:31:13.216242 UTC** both owned groups2176/2178 were freshly absent, including their launcher and solver descendants. Root independently confirmed PIDs2176/2177/2178 absent at02:31:55. All required remote reads/writes are finished; root was explicitly told it could STOP the retained worker. This agent made no instance state/tag change and retained every artifact.

Seven attempt artifacts were downloaded under `box/d125-defect-order-first-attempt-20260907/evidence/`; the eighth checked file is the matching local frozen authority. All eight byte counts and full hashes matched the terminal remote custody:

| file | bytes | SHA-256 |
|---|---:|---|
| decision.result.json | 713 | `3001404c7a4379741d1125617b4b9f086a26d22ad5c53baff41a5a923cde2d0f` |
| decision.telemetry.json | 2576 | `f60276864ad8807f46f2f143f6ddbbab3f5cfc3ef3fd41b4cb1a146e55b6a68d` |
| decision.identity.json | 360 | `d6cf4cb73f0dceb534ec6a1246ad12d1d328ca24becf4bf8ab46cb86af9d0da6` |
| decision.launch.json | 715 | `ec4bf488a757f08cb761fd24f856c3e2374e3b76572fa5482415d968e7237ee6` |
| decision.sing | 710365 | `182b72418d36ff4d7a4f583748c23dc2104875333684703d2c6a3b5219817c22` |
| decision.stdout | 630155 | `56071a82036516e02d5bf0211ab7f9189d9256f0e7116a435f133d48da113684` |
| decision.stderr | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| solver.authority.json | 2271 | `888b05c16d69cd971bc2ce8e3247fab04b4a16d762e1ccd55c3d82bd68d09694` |

Additional local custody pins: `terminal-custody.json` `78dc546942577c4866a4865d48cef59a8e56f7675ddc7e09252ec3a0531cfdc0`; `harvest.py` `eff68a1e37b6c72fd2e29e03e3e00e54736b3eafda2138002163f38de015c654`; `framing.py` `723ed38d3996619877fb2eb8ddf1c8ffb83b0befd1bdff6827461253de119f28`; `framing.json` `2146cafcc4ffe4e49a91a5927ba46b84cb6846541eddaf6ead2d7cdcb74b34c4`. The framing replay is bounded30wall/25CPU seconds and512MiB and performs no polynomial parsing/arithmetic. It confirms803 index positions, not a mathematical certificate.

**Final classification:** complete-input attempted, cap-respecting and cleanly harvested; mathematical result **INCONCLUSIVE**. No properness, unit, survivor, point, exclusion or conjecture resolution. No third solve or next-representation preparation was undertaken. **All writers terminal; IDLE.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7524`.
- Body SHA-256:
  `6b538ce32e8ada9748f2f143d795ab818a48aca65493a9b472262bd3b2d334ff`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
