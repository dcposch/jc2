# LF40 V1 AWS launch record

Lifecycle: **R0 terminated for wrong generated target; no mathematical verdict**

The preregistered sequential exact-QQ test was launched on audited `r6b`
(`i-0f089e64c378f5da3`, `ip-172-30-0-106`) at
`2026-08-27T18:55:50Z`.

```text
tag        = ggv_8_28_lf40_v1_20260827T185316Z_r6b
launcher   = 69170
Singular   = 69209 (initial process; subject to timeout-wrapper lifecycle)
source     = /home/ubuntu/jobs/ggv_8_28_lf40_v1_20260827T185316Z_r6b_source
archive    = /home/ubuntu/jobs/ggv_8_28_lf40_v1_20260827T185316Z_r6b_source.tar.gz
output     = /home/ubuntu/jobs/ggv_8_28_lf40_v1_20260827T185316Z_r6b
stdout     = /home/ubuntu/jobs/ggv_8_28_lf40_v1_20260827T185316Z_r6b.launcher.stdout
stderr     = /home/ubuntu/jobs/ggv_8_28_lf40_v1_20260827T185316Z_r6b.launcher.stderr
```

The final prelaunch check at `2026-08-27T18:55:29Z` found zero live
Singular/msolve/campaign-Python processes, all three target paths absent, and
zero writable files in the staged source tree.  It reverified:

```text
SOURCE_FREEZE.sha256  aae351afe8cefa70a2be13d480dcc4c24ae1721a12909125f25d87dfbcd55d25
source archive        90d5e5ab9bfcc71fb5b3e9952118ba13586c9976f9d5cecc5b34d4eac101a9dc
```

The remote desk gate and compiler replayed byte-identically and printed
`PASS_FACEPIN_CUSTODY_GATE_REVIEWED_REPAIR` and
`PASS-LF40-COMPILER-CUSTODY`.  Singular then passed both synthetic ideal
controls and completed row 0.  At `2026-08-27T19:01:12Z` it was computing the
first nontrivial row-1 standard basis on exactly one thread at nice level 5,
with 746,280 KiB RSS, zero solver stderr, and no swap.

At `2026-08-27T20:57:32Z`, inspection found that the R0 generated Singular
program had dropped the constant `1` from the degree-zero row-17 generator.
The process was terminated immediately and the wrapper failed closed with
solver rc 1, validator rc 90, maximum RSS 3,512,480 KiB, zero swaps, and
elapsed wall time 2:01:36.  Its terminal status
`DEPENDENCY_SOURCE_REPLAY_OR_ENGINE_FAILURE` is operational only and carries
no mathematical verdict.  The complete harvested packet is
`aws_r6b_failed_wrong_target_v0/`; its `RESULT.json` SHA-256 is
`b78e6aad20bd7880d278313e2b161d0a1b511d931518b16c89d687b3dbd0744a`
and its evidence manifest SHA-256 is
`9eef6aa288e52c9837c91642986d8f8bc2b58a251d313fd8f015de9bc065cca3`.

The corrected R1 launch is recorded below after its own immutable freeze and
preflight.  This launch record is a post-freeze coordination record and is
deliberately not an input to either immutable source archive.

## Corrected target-fix R1 launch

The corrected producer lane launched at `2026-08-27T21:10:47Z` from a fresh,
read-only source tree and a fresh output namespace:

```text
tag        = ggv_8_28_lf40_v1_targetfix_r1_20260827T210915Z_r6b
launcher   = 72122
Singular   = 72159 (initial process; subject to timeout-wrapper lifecycle)
source     = /home/ubuntu/jobs/ggv_8_28_lf40_v1_targetfix_r1_20260827T210915Z_r6b_source
archive    = /home/ubuntu/jobs/ggv_8_28_lf40_v1_targetfix_r1_20260827T210915Z_r6b_source.tar.gz
output     = /home/ubuntu/jobs/ggv_8_28_lf40_v1_targetfix_r1_20260827T210915Z_r6b
```

The launch pins are:

```text
SOURCE_FREEZE_TARGETFIX_R1.sha256  70af56340845961625ce43945852da8f2350aa3d0a050532ca6138927d9c3298
target-fix R1 source archive       3895fa95022f1a894695f5e30ea7ae4f3ae62e423748956df791d0201aa42648
replayed Singular program          435c350f8a5be062d9b1e1b7cf57e9483dcf2648400fe250d4edbd13ccf846f7
replayed compiler manifest         787e934d35cf3d458d03f15fe299f475109d198b924851689f8246783411e8a0
```

The runner replayed the complete R1 source freeze, desk gate, compiler, and
compiler evidence before starting Singular.  Both synthetic controls passed;
row 0 completed, and Singular entered the first nontrivial row-1 basis on one
nice-5 thread.  At launch the host had about 490 GiB available and zero swap.

Different-model Fable5 hostile review `e49ef51e...` subsequently reconstructed
all 740 generators independently and passed the target sign, exact-once target,
seven mutation, freeze/archive, and live-replay checks.  It found no
mathematical defect, but observed that the staged files were read-only inside
13 writable source directories.  At `2026-08-27T21:32Z` the coordinator ran
`chmod -R a-w` on the exact registered source tree without touching the output
namespace or running process.  A post-hardening replay checked all 48 entries
of `SOURCE_FREEZE_TARGETFIX_R1.sha256`, and `find . -perm /222` returned no
path.  Singular PID 72159 remained live on one nice-5 core with zero swap.
Any terminal result still requires normal independent output review; no family
exclusion or JC2 conclusion follows from compiler custody.
