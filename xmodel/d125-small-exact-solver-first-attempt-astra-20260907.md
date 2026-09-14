# First complete D125 unequal/Q exact attempt — timeout, inconclusive

Status: **INCONCLUSIVE / WALL_TIMEOUT / NO BASIS OR CERTIFICATE.** Author `/root/model_productivity`, 2026-09-07. Frozen basis `0d39df3c9fd69c939a8420c54d03228b9077777d`.

The single authorized exact-Q `slimgb(I)` attempt reached its300-second wall cap without emitting a basis block. CAPRUN completed validated TERM/reaping in **300.077379609 seconds**,01:14:54.597813–01:19:54.675188 UTC. Peak sampled group RSS was1,797,402,624 bytes (about1.67GiB), not the16GiB memory ceiling. **No unit/properness conclusion follows.** Conditional lifting was not reached; verification was not launched. No retry, extension, source change or alternate method followed.

## 1. Exact authorization and unchanged client

Read and retained whole frozen registration `box/d125-small-exact-solver-first-attempt-20260907/REGISTRATION.md`, SHA `bb05f3ae6bc82564b5f2f3d8f8e00686496bdcc083f675c88107653ea9dfa0ea`; readiness `readiness-pre-green.json`, SHA `ea399a55dd4167cab3d2749e0bbc9d44faeb88bb7e428426cbefbb23b40c249d`. Neither was changed. Root GREEN SHA `d11aaffa646203766a6c07346006d368d24331f9a1112df286f4a308294bd31f` authorized exactly this one attempt after the strict-parser delta gate and complete-source/engineering gates were accepted.

The charged client is unequal/rational, exactly269 variables and803 literal equations overQ in the original displayed variable order/globaldp:660 J rows,105 negative polynomiality rows,31 fixed-map residuals,7 guards, including249 zeros. There is no coefficient/field split, subset, localization, gauge, compression or variable elimination. Actual source degrees are75/125; partial-u15/25 and partial-v60/100; leaders u15v60/u25v100. Receiver15/25 is not used as a Keller degree pair.

The deterministic frontier output, SHA `71955226bd7d4f4a7a7182c198115afef01910704f7ac210dbeef2a9dd4d8d17`, is `NOT_CLOSED_BY_THIS_GATE`, gcd25/max125. This is inconclusive admissibility, not openness or existence. Full-stream acceptance is root report `318e7d9c12be4a82aadb4d8ad9eedad32a5ba37026e7dffb21f5909ed8e3bff9`, combining Fable's independent mathematics with root's completed all-six traversal; not the reviewer's incomplete initial run alone. Strict delta gate `d943da84709eb67ce80165c502d1021366e9cb702961dd3d15f05a6194c7e183` and actual engineering `c5bfbc8e37882dcd973077697319e7fb8a28f71393a090dcfd4031d0b97672f8` were accepted by root before GREEN. No live gate files were read.

Frozen source prefix `/home/ubuntu/d125-small-source-construction-pilot-20260906/unequal-rational/client-unequal-rational`: JSONL `b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac`; Singular `c089c33301e3889e0c20527386719f411907cf2957ecfad3d93c65f7be24e718`. Both were rehashed before and after and remained unchanged.

## 2. Deployment, command and caps

Only repaired `exact.py` was deployed, SHA `7ca2b24ee5d04ff6d60fd2212a05586c8bba24327a51c7718351434c7eda60e9`. Before that authorized replacement, old bytes were preserved exclusively as `/home/ubuntu/d125-small-exact-solver-20260907/exact.pre-strict-repair-ca7630e3.py`, SHA `ca7630e39cb8c5b4aec671b2a83132502abd716c6826c30a4bbc03014ffdb6b3`. No prior local code/report or source stream changed. Driver remained `7f081576ea72005c2509ef2d575aa63b9fd53416987f3535ed520fd79fdc130d`, CAPRUN `4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2`, Singular `90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4`.

One fresh solver authority, SHA `4d1a0bb81e3716d1fa8ceb24d1546b77f0032c34d3545919da15ec63a5ef6b45`, bound all pins, exact instance/boot/cwd, root GREEN and accepted gates. It began01:14:54.223534 and expired01:22:24.223534. The sole launch in `/home/ubuntu/d125-small-exact-solver-20260907/` was `setsid python3 -I -B driver.py launch --phase decision --authority solver.authority.json`; the unchanged caller invoked CAPRUN and execed `Singular --no-rc -q decision.sing`.

The decision cap was300 wall/inherited CPU seconds including source parsing, import, basis work and any conditional lift;16GiB AS/sampled aggregate RSS; one observed thread;64MiB inherited FSIZE per registered stream and core0. The intended separate120-second exact verification was conditional on a normal complete decision and therefore **not authorized to proceed after this timeout**. No verify.* file exists. CAPRUN does not meter output bytes or provide an instantaneous hard aggregate-RSS ceiling; FSIZE limits each registered stream, not the entire filesystem.

## 3. Terminal receipts before output inspection

Child PID=PGID13062/start_ticks597628, boot `69938ee6-48bb-4e45-bdf2-efb08c655368`. Caller PID=PGID13060 and CAPRUN parent13061 are recorded. The child cgroup was `session-199.scope`, namespace `pid:[4026531836]`; live metadata only was read while running. The frozen launch receipt records caller PID/PGID but not caller start ticks; no unavailable caller tick value is inferred after exit.

Authoritative receipt: `status=WALL_TIMEOUT`, runner rc124, child rc1 after TERM, error null. CAPRUN matched the exact PID/PGID/start identity before TERM at01:19:54.611705, required no KILL, reaped the leader and recorded cleanup complete. The outer SSH/setsid transport returned0; that is not the job return code and was not used as one. Root independently found13060/13061/13062 absent at01:20:10; this lane's01:20:48 check found both owned groups13060/13062 empty before reading terminal output.

Only then were terminal stream framing and input-prefix bytes examined. Stdout629,890 bytes contains `I_SIZE 554`, `I_BEGIN 803`, all803 indexed I lines and `I_END`; it ends with `halt 1` after the cap. It has **no G_BEGIN/G_END, T_BEGIN or END verdict marker**. Stderr is literally empty. There is consequently no completed basis candidate or cofactor certificate to verify, and no evidence here for properness or unitness.

The full707,596-byte ring/ideal prefix of `decision.sing` is byte-identical to the frozen original through the ideal semicolon, SHA `6db6990b283359d5f7ea959175121968e252d4dad56fd55a319eaa421c35ac2a`. Its only added suffix is the accepted I/G/T serialization and single `slimgb`/conditional-lift program. Exact suffix and terminal framing are retained in `terminal-framing.json`; no new source reconstruction or algebraic verification ran during harvest.

## 4. Artifact custody and handoff

All complete and partial attempt files remain under the exact remote execution directory. Twelve files,1,422,354 bytes total, were copied into the owned local box's `evidence/`; every SHA/size matched the remote custody manifest. Original complete JSONL/Singular source streams remain untouched in their earlier EBS directory.

- `decision.sing`:708,539 bytes, SHA `85f182ffbd850eab2f6eb00301b845a9dd741e2913127f742859e93338c65d72`.
- `decision.stdout`:629,890 bytes, SHA `78892c2bd8a460dc3af0ceb4e83cc86be329e2d430aba4cf07af694ffc099f98`.
- `decision.stderr`:0 bytes, SHA `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- `decision.telemetry.json`: `7fcb878a386a9a39aa18e02a42d8f6ef53bceb7d390105fb7d1750af2a90526a`.
- `decision.result.json`: `f59996819a5d92b18c1de47ab9878fdb3a06f07e1b51c2aaf0c44d03a0cccda6`.
- Full metadata/file manifest `terminal-receipt-custody.json`: `9579c8b1b310824bab03373aa39c2edee430379355abf5326757080e4232a4cb`.
- `terminal-framing.json`: `7cdfd0829d754dd4c1ac0c5cce838e0015c00190473b21252395df8f16dfc67a`; `download-verification.json`: `14dd9d7e322a23a419b6ef6f973bc6cdfcfb1358cc26db4666288b981e8d328a`.

Final read-only AWS/host checks still matched running `i-0da0cebfc97c9fd54`, Owner `coordinator-factored-jacobian-20260906`, retained EBS `vol-0eb6450d18ffa89f1`, same boot, swap0,20,205,957,120 free disk bytes and257,359,528KiB available RAM. `DeleteOnTermination=true` remains the sole-copy preservation boundary. Root retains STOP authority; this lane performed no instance start/stop/terminate/retag or unrelated workload action.

The registered single attempt is finished. No mathematical result is promoted and no follow-up computation is authorized by this report. All solver, caller, copy/harvest and local artifact writers are terminal after sealing. **STOP/IDLE; worker custody returned to root.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8280`.
- Body SHA-256:
  `3a3a40eeaf678148f567826104c183a4cb9381acfa6bb0841585bc341c9f1f12`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
