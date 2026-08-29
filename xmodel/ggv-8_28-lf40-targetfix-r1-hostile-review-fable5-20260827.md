# Hostile different-model review: GGV `8_28` LF40 target-fix R1

Date: 2026-08-27  
Reviewer: Fable 5, hostile different-model referee (compiler-custody scope)  
Solicitation: `xmodel/ggv-8_28-lf40-targetfix-r1-hostile-review-sol-ultra-20260827.md`  
Scope: repaired exact-Q compiler custody only.  This is **not** a family
exclusion, not a promotion of any Singular outcome, and not a JC2 result.
No heavy local CAS was used; the only sustained algebra is the AWS lane.

## Verdict

**CONFIRMED — PASS TO RESTART on the R1 freeze; no blocker; concur with the
Sol Ultra review.**  I independently derived the target sign from the frozen
lower-chart identity, rebuilt the entire 41-row system and its FACEPIN
substitution from `RAW_INPUT.json` with my own code (no producer module was
imported and `with_target()` was never used to define an expectation),
compared every ordered generator of all three compressed ledgers and of the
generated Singular program, exercised seven mutations against my independent
regression (all rejected), verified the R1 freeze/archive, and inspected the
live `r6b` replay over SSH.  49/49 independent checks pass.  R0 produced no
mathematical conclusion of any kind; its last completed row was row 0, and
the defective equation lives at row 17, which it never reached.

One new nonblocking observation (§8, GAP-1): the staged R1 source tree on
`r6b` has writable *directories* (files are read-only); the runner's
immutability gate checks files only.  R0's staging had zero writable
directories.  This does not affect the frozen bytes or the launch-time hash
gates and is fixable at harvest time.

## 1. Fail-closed hash gate (all three required, all matched)

```text
f95d4926407bf35e90841e3e2cdb6c25543715a0e9efe1724868a6af755a8c2e  xmodel/ggv-8_28-lf40-targetfix-r1-hostile-review-sol-ultra-20260827.md
828f819e78ba36cf019e7014263148a4ee53ffd5b77ef77fee310637b82fc719  cases/.../compile_lf40.py
435c350f8a5be062d9b1e1b7cf57e9483dcf2648400fe250d4edbd13ccf846f7  cases/.../compiled/lf40_sequential_QQ.sing
```

## 2. Independent target-sign derivation — CONFIRMED

Hand derivation from the frozen lower chart `x = tau^-4 xi, y = tau,
F = tau^8 f, G = tau^12 g`.  Chain rule with `xi = x y^4`:

```text
f_x = tau^-4 F_xi
f_y = tau^-9 (4 xi F_xi - 8 F) + tau^-8 F_tau
g_x = tau^-8 G_xi
g_y = tau^-13 (4 xi G_xi - 12 G) + tau^-12 G_tau
```

The `4 xi F_xi G_xi` cross terms cancel in `f_x g_y - f_y g_x`, leaving

```text
J(f,g) = tau^-17 [ -12 F_xi G + 8 F G_xi + tau (F_xi G_tau - F_tau G_xi) ].
```

Hence `Dtil := 12 F_xi G - 8 F G_xi - tau(F_xi G_tau - F_tau G_xi)
= -tau^17 J(f,g)`, and expanding by tau-rows reproduces the preregistered
recurrence `Dtil_n = sum_(r+s=n) ((12-s) F_r' G_s + (r-8) F_r G_s')`
coefficient-for-coefficient, so the preregistration's formula and its target
are mutually consistent.  With the frozen orientation `J(f,g) = 1`:

```text
Dtil_17 = -1,   Dtil_n = 0 (n != 17).
```

Singular generators are set equal to zero, so the required row-17 degree-zero
generator is `Dtil-coefficient - (-1)`, i.e. the constant enters as `+1`.
The only degree-zero row-17 pairs with nonzero mapped scalar `-(i*l - j*k)`
are `f_0_1*g_1_0 -> +1` and `f_1_0*g_0_1 -> -1` (the `(0,0)x(1,1)` and
`(1,1)x(0,0)` pairs have zero scalar), so the exact required generator is

```text
1 + f_0_1*g_1_0 - f_1_0*g_0_1,
```

which is exactly the R1 output.  Machine confirmation, independent of the
producer's code (script SHA-256
`622d6d7bc091f64923a2b78aa96896ebe6df2218b29a952740d039323fa086d4`,
staged at `/tmp/lf40_review/audit_lf40_fable5.py`):

1. **Laurent identity check.**  With all 442 slots specialized to random
   integers (two seeds), the full rebuilt row system, summed as
   `sum Dtil[row][deg] xi^deg tau^row`, equals `-tau^17 * J(f,g)` computed
   directly in `(x,y)` and pushed through the chart.  PASS twice.
2. **Tiny witness.**  For `f = x, g = y` (a `J = 1` pair) the only surviving
   bucket is `Dtil[17][0] = -1`.  PASS.
3. **Anchor evaluations** at the `J = 1` witness `f_1_0 = g_0_1 = 1`:
   correct generator evaluates to `0`; omission mutant `-1`; sign-flip mutant
   `-2` (matching `mutation_results.json`'s recorded anchors `0 / -2`).

Row-0 consistency anchor: on FACEPIN (`F_0 = aK^2, G_0 = bK^3`) row 0 dies
identically because `12*2 = 8*3`; my rebuild kills all 34 raw row-0
generators, confirming the relative `(12, -8)` normalization independently.

## 3. Independent parse and full rebuild of all artifacts — CONFIRMED

My own direct-coordinate engine (sign `-(i*l - j*k)`, row `17 - 4p + q`) and
my own tau-recurrence engine agree, and reproduce **every** generator of
`raw_recurrence_rows.jsonl.gz`, `raw_direct_rows.jsonl.gz`, and (after my own
binomial FACEPIN expansion of `a xi^2 (xi-rho)^14`, `b xi^3 (xi-rho)^21`,
matching all 37 relations of `facepin_substitution.json`)
`facepin_rows.jsonl.gz`, both as sparse polynomials and as serialized
strings.  Findings, each independently recomputed:

```text
41 rows in each ledger; slot windows 141 F + 301 G verified against my formulas
raw census 774 = [34,35,34,...,1,0]; six structural-zero positions absent
post-FACEPIN census 740 = [0,35,34,...,1,0]; row 0 killed 34 -> 0
numeric constants in untargeted coefficients: none (all three ledgers)
numeric constants in target generators: exactly [(17,0,+1)] in all three ledgers
program constant inventory over ROW_1..ROW_40: exactly [(17,0,+1)]
ROW_17 first generator: 1+f_0_1*g_1_0-f_1_0*g_0_1; whole-program occurrences: 1
row 39 = 8*f_0_8*g_1_15-12*f_1_11*g_0_12 (single generator); row 40 = structural 0
ring: char 0, dp, 409 variables == my (weight, side, i, j, name) sort == ring_variables.txt
ROW_0 never declared; ROW_1..ROW_40 declared exactly once each, in order
cumulative markers = my prefix sums, 41 values, ending 740
stop printers: per-row cumulative+1; terminal LF40_LISTED_EQUATIONS_AT_STOP=741
Rabinowitsch: ideal J=w*a*b*rho*f_0_8*g_0_12-1 exactly once; no other saturator
forbidden imports (X^8-1, ideal H=, ring R=655): absent
ideal declarations limited to CONTROL_*, J, G, ROW_1..40
row/cumulative SHA-256 chains of all three ledgers verify; arrays in
  compiler_result.json match my recomputation
```

Frozen row-17 ledger digests, recomputed by me and equal to the Sol review's:

```text
recurrence row 17  bf7b3522a63ea3008f886a8f99d0b4b182b3a66498e387944d9d3974c97e7ac9
direct row 17      03f985c5fc0d63f467315c285ffc61eefe636904f996b86d8fb2ff403a435d70
FACEPIN row 17     a6d7d9621b54292ba223d6534781eaeacad7db150e5ec6dffe6e61589c82bef7
```

This excludes an omitted, doubled, wrong-degree, wrong-row, or sign-reversed
target in the frozen R1 artifact, by independent reconstruction rather than
by trusting `with_target()`.

## 4. Mutation regression — CONFIRMED (all rejected)

My regression takes the independent target map `{(17,0): -1}`, rebuilds every
residual generically as `Dtil_coefficient - target`, and requires complete
ordered semantic equality with both the JSON ledger and the parsed program.
Against it:

```text
omission (R0 line)            REJECTED  (row 17 generator 0 semantic mismatch)
opposite sign (-1+...)        REJECTED  (row 17 generator 0 semantic mismatch)
doubled target (2+...)        REJECTED  (row 17 generator 0 semantic mismatch)
sign-flipped polynomial       REJECTED  (row 17 generator 0 semantic mismatch)
wrong row (constant on 16)    REJECTED  (row 16 generator count 24 != 23)
wrong degree (constant on (17,1))  REJECTED  (row 17 semantic mismatch)
JSON-side sign flip, program correct  REJECTED  (JSON mismatch at (17,0))
```

The unmutated frozen artifacts pass the same regression exactly.  This
discharges, for the frozen R1 bytes, the Sol review's §6 concern that the
compiler's own row-17 guard is self-referential (it derives its expectation
via `with_target()`).  I confirm that guard weakness exists in
`compile_lf40.py` and agree it is nonblocking now; adopting an engine-free
`audit_lf40_serialization.py` equivalent to my script before the next
compiler refactor remains the right fix.

## 5. R0/R1 diff, freeze, and archive — CONFIRMED

* R0 replay dir vs local `compiled/`: exactly two files differ
  (`lf40_sequential_QQ.sing`, `COMPILER_EVIDENCE.sha256`).  The Singular
  content diff is exactly the single line
  `ideal ROW_17=f_0_1*g_1_0-f_1_0*g_0_1,` →
  `ideal ROW_17=1+f_0_1*g_1_0-f_1_0*g_0_1,`; the manifest diff changes only
  that program digest.  The other eight payloads are byte-identical.
* `SOURCE_FREEZE_TARGETFIX_R1.sha256`
  (`70af56340845961625ce...` — full value below): 48 entries, **48/48 OK**
  locally.
* R1 archive `GGV_8_28_LF40_v1_targetfix_r1_source_20260827.tar.gz`
  (`3895fa95...`): 49 members = the 48 frozen files + the freeze manifest,
  zero directory entries, **zero `jc2-lean` members**; member set equals the
  freeze set exactly.  Matches `SOURCE_ARCHIVE_TARGETFIX_R1.sha256`.
* R1 compile replay telemetry (`targetfix_compile_r1_aws/`): exit 0,
  `PASS-LF40-COMPILER-CUSTODY`, wall 5.31 s, max RSS 361,512 KiB, swaps 0.
* R0 freeze/archive (`aae351af...` / `90d5e5ab...`) retained unchanged as
  historical evidence, matching the launch registration.
* Pinned upstream inputs verified: `RAW_INPUT.json = 28b9b05c...`; the
  charged spec `94c10fd8...` and its hostile review `681357ce...` are in the
  verified freeze.

Key hashes (all verified by me):

```text
compiler (R1)                  828f819e78ba36cf019e7014263148a4ee53ffd5b77ef77fee310637b82fc719
Singular program (R1)          435c350f8a5be062d9b1e1b7cf57e9483dcf2648400fe250d4edbd13ccf846f7
Singular program (R0)          73789f7d19362627b05823e3d8a0f6c24b9f9ea83aa23e496413fb87f6a6b382
compiler_result.json           84ae569bef4719cfabfafc0b8eb8a9e367a674b954e3edb903e3ef477faeb618
facepin_rows.jsonl.gz          a83a9d6550107cdcc395fb21ea7e8fcfd5e9818042f2fbbd8edcf07220261ee1
COMPILER_EVIDENCE.sha256       787e934d35cf3d458d03f15fe299f475109d198b924851689f8246783411e8a0
SOURCE_FREEZE_TARGETFIX_R1     70af56340845961625ce43945852da8f2350aa3d0a050532ca6138927d9c3298
R1 source archive              3895fa95022f1a894695f5e30ea7ae4f3ae62e423748956df791d0201aa42648
R0 SOURCE_FREEZE               aae351afe8cefa70a2be13d480dcc4c24ae1721a12909125f25d87dfbcd55d25
R0 source archive              90d5e5ab9bfcc71fb5b3e9952118ba13586c9976f9d5cecc5b34d4eac101a9dc
R0 RESULT.json                 b78e6aad20bd7880d278313e2b161d0a1b511d931518b16c89d687b3dbd0744a
R0 EVIDENCE.sha256             9eef6aa288e52c9837c91642986d8f8bc2b58a251d313fd8f015de9bc065cca3
RAW_INPUT.json                 28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876
```

## 6. Live `r6b` replay under the registered tag — CONFIRMED (SSH performed)

SSH to `ubuntu@34.204.74.226` (key `~/.ssh/claude-cli.pem`) at
`2026-08-27T21:26Z`, read-only inspection of tag
`ggv_8_28_lf40_v1_targetfix_r1_20260827T210915Z_r6b`:

* Host `ip-172-30-0-106`, DMI `Amazon EC2`, Singular 4.3.2 — all as
  preregistered.  Load average 1.00; zero swap configured; ~525 GB available.
* `launch_registration.txt` matches the preregistered envelope exactly
  (caps 503316480 KiB / 43200 s / 42600 s, workers 1, nice 5, freeze
  `70af5634...`, archive `3895fa95...`).
* Process tree live: launcher PID 72122 → outer timeout → `/usr/bin/time -v`
  → inner timeout → `Singular -q` PID 72159, state RN at nice 5, 99.9 % CPU
  on one thread, RSS 1,146,480 KiB, elapsed ~937 s at inspection.
* Remote hashes: staged `compile_lf40.py = 828f819e...`; staged frozen
  program and the **regenerated** program actually being executed
  (`run` replay dir) both `435c350f...`; replayed
  `COMPILER_EVIDENCE.sha256 = 787e934d...`; staged freeze `70af5634...`;
  staged archive `3895fa95...`.  Freeze replay 48/48 OK; compiler hash
  replay 9/9 OK; desk-gate hash replay 4/4 OK; banners
  `PASS_FACEPIN_CUSTODY_GATE_REVIEWED_REPAIR` and
  `PASS-LF40-COMPILER-CUSTODY` present; solver stderr empty so far.
* The live program's row-17 line is the corrected
  `ideal ROW_17=1+f_0_1*g_1_0-f_1_0*g_0_1,`.
* Progress at 21:26Z: headers + `LF40_SYNTHETIC_CONTROLS=PASS` + row 0
  complete (`LF40_CUMULATIVE_TARGET_GENERATORS=0`, `size(G)=1`); computing
  the row-1 standard basis.  No terminal marker yet; the lane remains
  producer-unreviewed with no verdict, as expected.

## 7. R0 impact — CONFIRMED: no wrong mathematical conclusion; last completed row 0

From the fail-closed packet `aws_r6b_failed_wrong_target_v0/` (RESULT.json
`b78e6aad...`, EVIDENCE `9eef6aa2...`, 30/30 manifest entries replay OK):

* `run/solver.stdout` ends at `LF40_STAGE_ROW_0_END` followed by `halt 1`
  (the termination).  **The last completed row was row 0**; R0 was ~2 h into
  the row-1 `slimgb` when killed (wall 2:01:36, max RSS 3,512,480 KiB,
  swaps 0).
* The defective equation sits at row 17.  R0's program is byte-identical to
  R1 except for that one row-17 line, so every prefix ideal R0 ever touched
  (Rabinowitsch + rows 1–16, of which it had completed none beyond row 0)
  coincides with the corrected lane.  It printed no basis, emitted no
  inconsistency or fixture marker, and serialized nothing reusable.
* Terminal record `status DEPENDENCY_SOURCE_REPLAY_OR_ENGINE_FAILURE`,
  solver rc 1, validator rc 90 is operational only.  There is **nothing to
  retract**; retiring R0 and importing nothing is correct containment, and
  the R1 lane in fact re-derives row 0 and row 1 from scratch.

## 8. Validator and residual gaps

Validator semantics — CONFIRMED as analyzed by Sol: rc 124/137/143 map to
`RESOURCE_CAP_NO_VERDICT`; any other nonzero rc, missing header, `LF40_FATAL_`,
`?`, contradictory or missing terminal markers, nonsequential completion, or
wrong stop counts fail closed (rc 90); the count convention 740 + 1 is
correct; a row-17/row-24 prefix can never be a terminal fixture by the
stop-marker logic.  I also confirm Sol's two nonblocking limitations (target
metadata trusted from `compiler_result.json`; per-row cumulative markers not
individually validated), mitigated by the runner's byte-identical-manifest
regeneration gate.

* **GAP-1 (new, nonblocking): writable staged-source directories on the live
  lane.**  `find -type d -perm /222` counts 13 writable directories in the R1
  staged source tree versus 0 in R0's; all files are `-r--r--r--` and the
  runner's gate checks files only (`-type f -perm /222`).  With writable
  directories, read-only files can in principle be unlinked and replaced
  after the launch-time hash gates.  No evidence of any such event; the
  running Singular process already holds its input, and the harvested packet
  is re-hashed.  Recommendation: `chmod -R a-w` the staged tree (as R0's
  staging did) and re-run `sha256sum -c` of the freeze at harvest time before
  crediting any terminal status.
* **GAP-2 (confirmed from Sol §6, nonblocking for the frozen bytes): the
  compiler's row-17 guard is self-referential.**  Independent regression now
  exists (this review, §4); it should be committed as
  `audit_lf40_serialization.py` and wired into the AWS runner before any
  compiler refactor.
* **Inherited-scope note (not a defect):** `RAW_INPUT.json` carries
  `control_id = R0_ARTIFICIAL_CUSP_CONTROL`; LF40 consumes only its slot
  support list and re-derives the lower grading, which I verified against my
  own window formulas (141 F + 301 G).  The family provenance (actual `8_28`
  raw pre-final pair, non-simple edge, `gamma = 7` single-root pin) rests on
  the pinned S1 spec `94c10fd8...` and its Opus5 hostile review `681357ce...`
  plus the reviewed desk gate, and is outside this custody review.

## 9. Itemized verdicts

```text
V1  three frozen inputs hash-match, fail-closed gate            CONFIRMED
V2  target sign Dtil_17 = -1; generator 1+f_0_1*g_1_0-f_1_0*g_0_1
    derived independently of with_target()                      CONFIRMED
V3  chart identity Dtil = -tau^17 J (hand + random Laurent
    specializations + f=x,g=y witness)                          CONFIRMED
V4  independent full rebuild == all three JSON ledgers ==
    Singular program (ordered, semantic and string)             CONFIRMED
V5  row 0: 34 raw generators FACEPIN-killed; no ROW_0 declared  CONFIRMED
V6  row 17 degree zero: unique numeric constant (17,0,+1);
    injected exactly once; ledger digests match frozen values   CONFIRMED
V7  cumulative counts: prefix sums to 740; stop counts +1;
    terminal 741; row 39 single generator; ROW_40=0             CONFIRMED
V8  Rabinowitsch saturation exactly w*a*b*rho*f_0_8*g_0_12-1,
    once; no foreign import or normalization                    CONFIRMED
V9  sequential std-basis semantics and synthetic controls       CONFIRMED
V10 validator fail-closed semantics (with 2 known nonblocking
    limitations)                                                CONFIRMED
V11 omission/opposite-sign (+5 more) mutations rejected by an
    independent regression                                      CONFIRMED
V12 R0->R1 diff exactly one Singular line + one manifest digest CONFIRMED
V13 R1 freeze 48/48 OK; archive = 48 files + manifest, no
    jc2-lean member                                             CONFIRMED
V14 live r6b replay under ggv_8_28_lf40_v1_targetfix_r1_
    20260827T210915Z_r6b: identity, envelope, staged hashes,
    regenerated program, corrected row-17 line, progress        CONFIRMED
V15 R0 produced no wrong mathematical conclusion; last
    completed row = 0; nothing importable                       CONFIRMED
V16 writable staged-source directories on live R1 lane
    (runner gate covers files only)                             GAP (nonblocking)
V17 self-referential row-17 compiler guard                      GAP (nonblocking,
                                                                 regression supplied)
```

No REFUTED items.  The restart license is for the preregistered producer
lane only; any eventual Singular terminal status remains producer-unreviewed
until independently replayed, and a proper full fixture would be only a lower
necessary-system survivor.

## Scope disclosure

Confined to the LF40 case directory, its `compiled/`, `desk_gate/`,
`aws_r6b_failed_wrong_target_v0/`, `targetfix_compile_r1_aws/`, the pinned
`RAW_INPUT.json`, `ops/FLEET.md`/`ops/status.sh` (SSH convention only), the
named `xmodel` solicitation, and read-only SSH inspection of the registered
`r6b` paths.  I did not enter, list, read, search, build, status, or modify
`jc2-lean`, and no accidental traversal occurred (archive listings were also
checked to contain no `jc2-lean` member).  Scratch scripts live in
`/tmp/lf40_review/` (audit script SHA-256
`622d6d7bc091f64923a2b78aa96896ebe6df2218b29a952740d039323fa086d4`); the
only repository file created by this review is this report.
