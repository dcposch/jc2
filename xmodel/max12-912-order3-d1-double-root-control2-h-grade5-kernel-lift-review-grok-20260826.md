# Hostile text-only review — control-2 eta-five Q-R-kernel grade-5 lift V6

| Field | Value |
|---|---|
| Claim under review | Scalar `h`-correction of the complete closed-corner h-linear R-square/Q-cubic grade inside the full five-dimensional kernel of the rank-three Q-R map, producing a 71-term polynomial whose `h=0` slice is the reviewed q2 witness, whose complete h-linear Q-R and R-square/Q-cubic components both vanish, and which is uniformly unique-target on `u,v>0`, `T>0` if and only if `eta>=15/4` |
| Overall verdict | **H_GRADE5_KERNEL_LIFT_CONFIRMED**. Dual AWS encodings emit certificates that differ only in `tag` and `order`; deleting those fields gives canonical sorted SHA `d476a5dc…`. The Q-R map has rank 3 and a complete five-vector RREF kernel of SHA `ce7ba74b…`. After the free-zero V5 particular solution, the next closed-corner grade is exactly fourteen R-square/Q-cubic terms, SHA `5a8d5aba…`. Their image from the five kernel directions has rank 3, pivots `(0,1,2)`, and free-zero solution `(1/4,-1/3,0,0,0)`. Combining gives `(g1,...,g8)=(5/2,-25/18,0,1/4,-1/3,0,0,0)`. The 71-term identity SHA `3363e67d…` has `h=0` equal to reviewed `W'` (`ddb451c4…`), zero h-linear Q-R, and zero h-linear R-square/Q-cubic. Integer arithmetic on all 71 recorded forms proves unique least term `la^20` iff `eta>=15/4`. The eight displayed `h^2 q r` terms are the unique maximizers of `-c/E`. The cell `0<eta<15/4` is the next filtered correction, not a branch survivor |
| Smallest failing identity | none in the frozen V6 source, either harvest tree, either AWS stream, the hash-pinned V5/V4 source, the reconstructed Q-R kernel, the fourteen-term residual, or the recorded 71-term polynomial |
| Smallest missing hypothesis for a stronger theorem | a correction of the `h`-squared Q-R piece on `0<eta<15/4`; polynomial multiplier-support completeness of the eight-row module; an `h`-adic or formal lift; moving axis or moving loads; another normal direction; a formal arc; the whole double-root fan; D1; or JC2 |
| Evidence tier | SHA-256 of the freeze chain and already-emitted AWS files; `cmp` of harvest copies against package-top source; `jq`/canonical-JSON comparison of the two certificates after deleting `tag` and `order`; integer/rational arithmetic on every recorded `(c,U,V,E)` and on the emitted Q-R / grade-5 RREF matrices; V1-format digest of the `h=0` slice; toric canonical digest of the 71-term polynomial, the 18-term h-linear coefficient, and the 14-term residual. V5 identities used here were reconstructed from V4/V5/V6 records and RREF, not inherited as lemmas. No local Singular, Sage, msolve, gfan, Lean, Python algebra, compiler execution, charged reconstruct, or eight-row product replay |
| Reviewer / model | Grok 4.6 (xAI). Text-only tropical / commutative-algebra / CAS-custody referee |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `574e873d4753b57dbaeb0fb83e320fbef3694724` |
| Host | Darwin. V6 compiler, V5 compiler, V4 compiler, V1 compiler, toric compiler, charged reconstruct, Singular, and every solver were not run |

## What was and was not run

No local substantive computation was run. In particular this review did **not** execute `compile_h_grade5_kernel_lift_v6.py`, `compile_h_qr_syzygy_lift_v5.py`, `compile_h_first_transport_v4.py`, `compile_q2_first_lift.py`, `compile_toric_blowup.py`, `independent_reconstruct.py`, Singular, Sage, msolve, Lean, Gfan, or any other solver, and it did not re-multiply `sum (F_i'+h g_i) E_i(h)` or reconstruct the unsubstituted eight rows. Hashes were checked with `shasum -a 256`. File identity was checked with `cmp`. Marker counts used `grep`. Git identity was read with `git rev-parse`. JSON fields were read with `jq`. Canonical SHA-256 values and rational weight forms were recomputed from the already-emitted certificate records (V1 digest format for the `h=0` slice; toric canonical format `[[list(monomial), num, den], ...]` for the 14-term residual, the 18-term `C_1`, and the 71-term polynomial). Recorded weight forms were checked by the integer identity `2c = 2(la-20)+10(q0+q1+q2)+15(r0+r1+r2)`. Kernel vectors were reconstructed from the emitted V5 RREF by rational arithmetic; the combined correction was checked by hand. No AWS replay was requested: every charged identity is present in the frozen records.

Charged freeze SHA-256, recomputed and matched:

```text
b80a754f32d8e6d0c1aff05f7392c95643628217e3c575e33965d8bb87bc7131  FREEZE.sha256
a69e542e57b33e7961299c658d1652aab9d2dd75dcd165532781f64aabf6cf5a  RESULT.md
3363e67da50c953ab37b4c67dc5dfeb77d3cfdf75e31b5d6f97dd87dafc7f833  corrected 71-term witness
```

Prerequisite V4 transport review, recomputed and matched:

```text
ed70c255ee6809b03e6dd40149766365cac92858b85ac4a881afa73ac3ce1d77
  xmodel/max12-912-order3-d1-double-root-control2-h-first-transport-review-grok-20260826.md
6ddb1343c7b30d0e4e6daf7e5f13ea364205e1a776c60534d02da26a7c529f14  V4 RESULT.md
0ff05368ab7a5751617db6a6b9a31e67545439ed5fb688cb15238ef879637b68  V4 FREEZE.sha256
```

V5 source/custody, recomputed and matched (identities reconstructed below, not inherited):

```text
8a963360f16a29c6841050f82e9eb79051005d821c6ec7837d0614ca8ead7366  compile_h_qr_syzygy_lift_v5.py
c9469bb0041ba34e16732e33b3944f04217009f35473275429b708fc060d680e  V5 RESULT.md
f166e2ba9aa8e2c4715f14a4f29ed7dd4296755ed5de551de94784be3e911471  V5 FREEZE.sha256
```

A separate V5 review file is present and ends `H_QR_SYZYGY_LIFT_CONFIRMED` at SHA `7ac62c8bd0667340aab5fcdd4d6d35b5e184536fb6e9f5c98f6c9955fdea54c7`. This V6 review does not treat that report as a lemma: the Q-R eight-term piece, the rank-three RREF, the five kernel vectors, and the fourteen-term leftover were recomputed from V4/V5/V6 records.

Every path listed in `FREEZE.sha256` recomputed and matched (23/23). Nested `SOURCE_CLOSURE.sha256` (9/9) and both harvested `result.sha256` manifests (5/5 each) matched from the case root / harvest directory as appropriate. Empty compiler stderr files are the empty-string digest `e3b0c442…`. Both rc files are the two-byte string `"0\n"`, digest `9a271f2a…`.

Read in full before the verdict: every file at
`cases/max12_912_order3_d1_double_root_control2_h_grade5_kernel_lift_v6_20260826/`
including both harvest trees; the hash-pinned V5 compiler `qr_component` / `exact_rref` / `analyze_threshold`; the hash-pinned V4 compiler `coefficient_images` / multipliers / `specialize_h_zero` / `divide_h`; the hash-pinned toric `NAMES` / `canonical` / `digest`; V1 `multipliers` / `digest`; V4 and V5 certificate records far enough to extract the h-linear Q-R piece and the leftover R-square/Q-cubic piece; and the V4 review named above. Predecessor conclusions were recomputed, not inherited.

---

## Promotion

**Accept `FOR THE PINNED ORDINARY-TAIL EIGHT-ROW MODULE AT a=1, p=-3, c=2+h, k=nu=0, mu=2/3, FULL Q AND R, STARTING FROM THE REVIEWED Q2-CORRECTED MULTIPLIERS F1'=F1+q2/12, F2'=F2-q2/9, Fi'=Fi (i>=3), THE REGISTERED DUAL-AWS V6 RUNS EMIT ONE 71-TERM POLYNOMIAL W_h'' = SUM_i (F_i' + h*g_i) E_i(h) WITH (g1,...,g8)=(5/2,-25/18,0,1/4,-1/3,0,0,0). THIS IS AN EXACT POLYNOMIAL IDENTITY, NOT A CONGRUENCE. ITS h=0 SPECIALIZATION IS THE REVIEWED 37-TERM W' (SHA ddb451c4…). ITS COMPLETE h-LINEAR Q-R COMPONENT IS ZERO. ITS COMPLETE h-LINEAR R-SQUARE AND Q-CUBIC COMPONENT IS ZERO. THE SCALAR CORRECTION IS THE CANONICAL FREE-ZERO POINT g0=(11/6,-11/12,0,...,0) OF THE RANK-3 Q-R MAP PLUS THE CANONICAL FREE-ZERO POINT (1/4,-1/3,0,0,0) OF THE RANK-3 GRADE-5 MAP ON THE FULL FIVE-DIMENSIONAL Q-R KERNEL, NOT ON A HAND-SELECTED SUBSPACE. NORMALIZE wt(la)=L, PUT alpha=15/2, beta=5+u, delta=5+v, eta=wt(h)/L, AND RESTRICT TO u>0, v>0, T>0. THEN W_h'' HAS UNIQUE LEAST-WEIGHT TERM la^20 FOR EVERY SUCH (u,v,T) IF AND ONLY IF eta>=15/4. AT eta=15/4 EVERY CLOSED-CORNER EQUALITY IS STRICT IN THE OPEN QUADRANT. FOR EVERY 0<eta<15/4 SOME ACTUAL PRESENT TERM FALLS BELOW TARGET FOR SUFFICIENTLY SMALL POSITIVE u OR v. THIS IMPROVES THE V5 RANGE eta>5 TO eta>=15/4. THE CELL 0<eta<15/4 BEGINS WITH THE h-SQUARED Q-R PIECE AND IS THE NEXT FILTERED CORRECTION, NOT A BRANCH SURVIVOR.`**

Do not promote this to: an `eta<15/4` existence statement; polynomial multiplier-support completeness; an `h`-adic or formal lift; a moving-axis or moving-load theorem; equality-support analysis of the 28-term face beyond the recorded weights; another normal direction; a formal-arc obstruction; a whole double-root fan; D1; or JC2.

---

## Charge 1 — Custody, freeze, dual AWS, source closure, JSON difference

**CONFIRMED. Every freeze entry recomputes. Both registered workers are fail-closed, hash-gated, empty-stderr, sub-cap, pre-GO, and source-closed against the package-root manifest. Opposite traversal orders return certificates that differ only in `tag` and `order`; deleting those two fields gives literally identical sorted JSON of SHA `d476a5dc9000ba524d6067242652b4de7c4c8372748071546b4824e67a3c778b`.**

Required anchors, recomputed:

```text
a69e542e57b33e7961299c658d1652aab9d2dd75dcd165532781f64aabf6cf5a  RESULT.md
b80a754f32d8e6d0c1aff05f7392c95643628217e3c575e33965d8bb87bc7131  FREEZE.sha256
3363e67da50c953ab37b4c67dc5dfeb77d3cfdf75e31b5d6f97dd87dafc7f833  corrected 71-term witness
```

Recomputed `FREEZE.sha256` entries, all matched:

```text
a69e542e57b33e7961299c658d1652aab9d2dd75dcd165532781f64aabf6cf5a  RESULT.md
291f68ec1fa6983c1da5d7b7e2bd2d9b0c9d205ef89d76fc72acadf497b768d4  PREREGISTRATION.md
cc2759b7b1a3995a21da7bb1e31ee5234aa7e068d43cd0b649309cd0c562384e  AWS_REGISTRATION.md
6830ff95a56131d7512725c0c83330113b75f92fafbcffc8e21810632336dbf1  AWS_LAUNCH_METADATA.md
cdd6f99c5060682f205d2fd0e9acc2bb78a758eec43135cf29a524bd3e4cba6d  SOURCE_CLOSURE.sha256
c7d9faed50b93cb7bb3905d8d386d2dc0f670c300baeefa78864d5dd3097dfce  compile_h_grade5_kernel_lift_v6.py
423fb4c31780cabe1cccb52a5bbb887c4d7fd1343089defcddbc9a73b45fba1c  remote_worker.sh
26e540ce564877c4435b2ed2bd8a9cb7bafe8265783793e57c91471ecdb7cdd9  aws_box03_forward/h_grade5_lift.json
479b6d45a8aa9d88b6f1ae1c77175cfee3e52ff7ddae9c64e52520d84bc3f556  aws_box03_forward/compiler.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_box03_forward/compiler.stderr
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  aws_box03_forward/compiler.rc
950fd7221a75a635035b1e459497408a3fb5de79cecc22d0bc41083f2a7caf64  aws_box03_forward/compiler.time
d30c90281a90d0b94666522eb3c8679e0de475b8a7c6d8e6de32aeb78cb8b385  aws_box03_forward/result.sha256
a5fc3e68a54db334d716ada1dc296be914028c21a48c6d6bdf86d630573c83cc  aws_box03_forward/source.check
e2dc6527a3fe64b2f215e5dc255ed6cece2a4c8a397b72a365bd440eacfa8da7  aws_box03_forward/worker.metadata
ac4d8643682a4ddb16e6eb4c1b83042f6dff8752e1679bcdec1c03e071c39f1f  aws_r6d_reverse/h_grade5_lift.json
6d8d7d2ba907395d9d960c33e62468a84fca4a60fd3becf868ec588b4bcebd46  aws_r6d_reverse/compiler.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_reverse/compiler.stderr
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  aws_r6d_reverse/compiler.rc
54c9eb626ee4c5cbfddce652792d79058d8a927844726d3d51c99447f73e3515  aws_r6d_reverse/compiler.time
03528c33a0bcda0c7bc4c5cfb93789db59d70de4534c67e864e07e65692fa663  aws_r6d_reverse/result.sha256
a5fc3e68a54db334d716ada1dc296be914028c21a48c6d6bdf86d630573c83cc  aws_r6d_reverse/source.check
070d30085fb4c926e60020e8976f3b0c0ffcb743cdb2a3e1497e3ecf55f143be  aws_r6d_reverse/worker.metadata
```

Source-closure entries, all matched from the package root:

```text
291f68ec1fa6983c1da5d7b7e2bd2d9b0c9d205ef89d76fc72acadf497b768d4  PREREGISTRATION.md
cc2759b7b1a3995a21da7bb1e31ee5234aa7e068d43cd0b649309cd0c562384e  AWS_REGISTRATION.md
c7d9faed50b93cb7bb3905d8d386d2dc0f670c300baeefa78864d5dd3097dfce  compile_h_grade5_kernel_lift_v6.py
423fb4c31780cabe1cccb52a5bbb887c4d7fd1343089defcddbc9a73b45fba1c  remote_worker.sh
8a963360f16a29c6841050f82e9eb79051005d821c6ec7837d0614ca8ead7366  ../max12_912_order3_d1_double_root_control2_h_qr_syzygy_lift_v5_20260826/compile_h_qr_syzygy_lift_v5.py
3bbf1ebfb9f8b15054fe2f592bea92d8e07b95bce4d6ca131cd81c95f3698306  ../max12_912_order3_d1_double_root_control2_h_first_transport_v4_20260826/compile_h_first_transport_v4.py
c76ef85ac14f81839674368c55a324499832e6cf4b589befa68baf93a42b1490  ../max12_912_order3_d1_double_root_toric_blowup_20260825/compile_toric_blowup.py
0385b0b1e60b3bd37fa5fbee90dd6c17a454722bdbff424ea83c2ab0fa19df45  ../max12_912_order3_d1_double_root_control2_q2_first_lift_v1_20260826/compile_q2_first_lift.py
67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623  ../max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/independent_reconstruct.py
```

Harvested `SOURCE_CLOSURE.sha256` is byte-identical to the top copy on both hosts. Both `source.check` files are identical (`a5fc3e68…`) and print `OK` on those nine paths. The worker `cd`s to `$run` before `sha256sum -c SOURCE_CLOSURE.sha256`; `AWS_LAUNCH_METADATA.md` states that each run directory is the package under the job root's `cases/`. The sibling `../max12_…` paths are therefore `cases/`-neighbours, which is how AWS ran and how this review rechecked. Treating `aws_box03_forward/` or `aws_r6d_reverse/` as a new source root would make those siblings invisible. That is not the charged root.

The V6 compiler pins `V5_SHA=8a963360…` before import. V5 pins `V4_SHA=3bbf1ebf…`. V4 pins `TORIC_SHA=c76ef85a…` and `V1_SHA=0385b0b1…`. `t.load_charged_source()` re-pins `independent_reconstruct.py` at `67343b56…`. Tag gates: worker `case` requires prefix `max12_912_order3_d1_double_root_control2_h_grade5_kernel_lift_v6_20260826T*`; compiler `require_aws` requires Linux, DMI vendor `Amazon EC2`, and tag prefix `max12_912_order3_d1_double_root_control2_h_grade5_kernel_lift_v6_`. Both refuse non-`forward`/`reverse` orders.

| Check | Box03 forward | r6d reverse |
|---|---|---|
| Public IP / harvested hostname | `98.80.65.144` / `ip-172-30-0-249` | `100.26.198.153` / `ip-172-30-0-45` |
| Tag | `…_v6_20260826T041000Z_box03_forward` | `…_v6_20260826T041000Z_r6d_reverse` |
| Worker PID | `155376` | `222945` |
| Caps | `memory_kib=4194304`, `timeout=900`, `nice -n 10`; `ulimit -v 4194304` | same |
| Order | `forward` (`ell=1..8`) | `reverse` (`ell=8..1`) |
| Started / finished UTC | `2026-08-26T04:11:18Z` / `04:11:52Z` | `04:11:20Z` / `04:11:54Z` |
| Compiler stdout SHA | `479b6d45…` | `6d8d7d2b…` |
| Certificate SHA | `26e540ce…` | `ac4d8643…` |
| RSS / swap / exit | 22420 KiB / `Swaps: 0` / 0 | 22636 KiB / `Swaps: 0` / 0 |
| Pre/post `free` swap | `0B` / `0B` | `0B` / `0B` |
| Elapsed | 5.98 s | 6.01 s |
| PASS markers, each once | `PASS_H_GRADE5_KERNEL_LIFT_V6_SOLVABLE`, `PASS_REMOTE_WORKER` | same |
| `FAIL_` / `REFUSED` / `FAILED` | none in stdout, stderr, or sentinels; stderr empty | none; stderr empty |

`AWS_LAUNCH_METADATA.md` is timestamped `2026-08-26T04:11:34Z` local mtime (written as `04:12Z` to the minute). That is after worker start (`04:11:18Z` / `04:11:20Z`) and before GO. Content: both workers `WAITING_GO`; “Neither run directory contained GO when metadata was read”; source-closure manifest SHA `cdd6f99c…` matching the frozen file. GO sentinels exist and are empty; local mtimes place GO after that registration (`04:11:46Z` / `04:11:47Z`) and DONE at finish (`04:11:52Z` / `04:11:54Z`). No `REFUSED` or `FAILED`. The 6-second GO-to-DONE window matches the 5.98 s compile plus the post-GO source-hash check.

Harvest copies of compiler, worker, preregistration, AWS registration, and source closure are byte-identical to the package top on both hosts (`cmp`). The two JSON files differ only in the registered `tag` and `order` custody fields (83306 vs 83304 bytes; the two-byte gap is `box03` versus `r6d`). Deleting those two fields and re-emitting `json.dumps(..., sort_keys=True, indent=2)+"\n"` gives byte-identical semantic JSON, SHA

```text
d476a5dc9000ba524d6067242652b4de7c4c8372748071546b4824e67a3c778b.
```

Compiler stdout differs only in the preregistered `ORDER=` line together with the identical metric block

```text
STATUS=SOLVABLE
KERNEL_SOLUTION=1/4,-1/3,0,0,0
FULL_H_CORRECTION=5/2,-25/18,0,1/4,-1/3,0,0,0
CORRECTED_WITNESS_SHA256=3363e67da50c953ab37b4c67dc5dfeb77d3cfdf75e31b5d6f97dd87dafc7f833
ETA_UNIFORM_INFIMUM=15/4
ETA_EQUAL_OPEN_STRICT=1
```

and the per-host `CERTIFICATE_SHA256`. Both print `PASS_H_GRADE5_KERNEL_LIFT_V6_SOLVABLE` once. The worker requires exactly one of `PASS_H_GRADE5_KERNEL_LIFT_V6_(SOLVABLE|COKERNEL)$`; both hosts took the solvable branch.

Canonical hashes, recomputed from the already-emitted records and matched to both JSON payloads, both stdout streams, and `RESULT.md`:

```text
W' SHA-256                      ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b
Q-R kernel basis SHA-256        ce7ba74b70b4895a639970b7acc1a2f4f0f802d4afe7df6955bc8c1eaeb9aa93
grade-5 residual SHA-256        5a8d5aba718de8396363443cd7b951c83ece5bea4707ca4cc063ae5b9dbd89ef
corrected 71-term SHA-256       3363e67da50c953ab37b4c67dc5dfeb77d3cfdf75e31b5d6f97dd87dafc7f833
corrected C_1 SHA-256           6fee8f428caa5364b3390a4c835c2a47214e91e2f8d6d6709137f3c428d0d5e3
semantic JSON SHA-256           d476a5dc9000ba524d6067242652b4de7c4c8372748071546b4824e67a3c778b
```

Records are sorted by `json.dumps(exponents, sort_keys=True)`. Every extra toric variable `p,c,a,x,y,k,mu,nu` is zero on all 71 terms. Support is exactly `{h,la,tau,q2,q1,q0,r2,r1,r0}`. The only `tau` monomial is the skipped `la^20 tau`. No record has `rho>0`.

---

## Charge 2 — Rank-three Q-R map, full five-vector kernel, SHA, annihilation

**CONFIRMED. The scalar-correction map to the complete h-linear Q-R component has rank 3, pivots `(F1,F2,F3)`, and a five-dimensional kernel on free columns `(F4,F5,F6,F7,F8)`. The basis is the standard RREF kernel of every free column, not a hand-selected subspace. Its compact SHA is `ce7ba74b…`. Each of the five vectors annihilates the emitted RREF; F6's Q-R image is independently the empty polynomial.**

Construction, from the hash-pinned V6 compiler, which loads the hash-pinned V5 compiler, which loads the hash-pinned V4 / toric / V1 chain:

1. Rebuild the unchanged V4 witness `W_h = sum_ell F_ell' E_ell(h)` with the reviewed q2 correction `F1'+=q2/12`, `F2'+=-q2/9`, traversal `1..8` or `8..1`. Fail-closed: `W_h|h=0` projected onto the V1 ring must digest `ddb451c4…`.
2. Set `C_1 = ((W_h-W')/h)|_{h=0}` and `row0_ell = E_ell(h)|_{h=0}`.
3. Re-solve the V5 system `A_QR g = -qr(C_1)` by exact RREF. Fail-closed unless status is `SOLVABLE`, the free-zero solution equals the hardcoded `G0=(11/6,-11/12,0,0,0,0,0,0)`, and there are exactly three pivots.
4. Take **every** non-pivot column as a free column and form the standard RREF kernel basis. Fail-closed unless that basis has five vectors, and unless `qr(sum_i v_i row0_i)` is empty for each.

The original 9-by-8 matrix `A_QR` is not serialized (same gap as V5). The V5 certificate does serialize the RREF of `[A_QR | -qr(C_1)]`. That matrix, recomputed from the frozen V5 JSON and independently matching V6's emitted kernel, is 9 rows by 9 columns with exactly three nonzero rows:

```text
[ 1, 0, 0, -4/3,  1,  0, -10/9,  4/3 |  11/6  ]
[ 0, 1, 0,    1, -2/3, 0,   2/3, -7/9 | -11/12 ]
[ 0, 0, 1,    0,    0, 0,     0,    0 |     0  ]
```

Pivots `(0,1,2)`. Last column is the free-zero particular solution `G0`. The V4 h-linear Q-R piece, extracted from the frozen V4 records as the eight terms with `h=1`, `qdeg=rdeg=1`, and no extra variables, is coefficient-and-monomial equal to V5 `c1_qr_terms`, SHA `52bc3441…`:

```text
-88/27 q2 r2,  +11/9 q2 r1,  -22/27 q2 r0,
 +11/9 q1 r2, -22/27 q1 r1,  +11/27 q1 r0,
-22/27 q0 r2, +11/27 q0 r1.
```

No `q0 r0` term. All eight have closed-corner pre-h margin `-15/2`. Dual AWS both re-solved this system and both accepted `G0` with rank 3.

Kernel, from all five free columns `(3,4,5,6,7)=(F4,F5,F6,F7,F8)`, by `v_pivot = -RREF[row, free]`:

```text
k1 = ( 4/3,   -1, 0, 1, 0, 0, 0, 0 )
k2 = (  -1,  2/3, 0, 0, 1, 0, 0, 0 )
k3 = (   0,    0, 0, 0, 0, 1, 0, 0 )
k4 = ( 10/9, -2/3, 0, 0, 0, 0, 1, 0 )
k5 = ( -4/3,  7/9, 0, 0, 0, 0, 0, 1 )
```

This is byte-identical to both V6 certificates. Compact SHA of `json.dumps(qr_kernel_basis, separators=(",", ":"))` recomputes to

```text
ce7ba74b70b4895a639970b7acc1a2f4f0f802d4afe7df6955bc8c1eaeb9aa93.
```

Each vector annihilates the three nonzero RREF rows (hand inner products all zero). Hence each lies in `ker(RREF(A_QR))=ker(A_QR)`. Independently, V5 `row_qr_sha256[5]` (row F6, zero-based index 5) is `sha256(b"[]")` = `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`, so F6's Q-R image is the empty polynomial and `k3=e_6` is in the kernel by a second route. Rank 3 on 8 columns forces `dim ker = 5`; taking every free column therefore spans the full scalar-correction kernel. V6 does not drop F6, nor restrict to `{F4,F5}`, nor otherwise select a subspace.

V6 additionally fail-closes if any kernel vector has a nonempty Q-R image against the unsubstituted `row0`. Dual AWS both passed that check. This review did not replay the eight-row product; the RREF annihilation, the empty F6 digest, the full free-column construction, and the dual-AWS fail-closed loop are the charged evidence.

---

## Charge 3 — Fourteen-term next residual, kernel images, rank three, solution `(1/4,-1/3,0,0,0)`

**CONFIRMED. After applying `g0`, the complete next closed-corner h-linear grade is fourteen pure R-square and Q-cubic monomials, every one of pre-h margin `-5`, SHA `5a8d5aba…`. The five kernel images span a rank-three map on this grade, pivots `(0,1,2)`, and the unique free-zero solution is `(1/4,-1/3,0,0,0)`.**

`grade5_component` retains a monomial of `C_1` if and only if `(qdeg,rdeg)` is `(0,2)` or `(3,0)` and no variable outside `{q2,q1,q0,r2,r1,r0}` appears. For any such pure monomial the closed-corner pre-h margin is

```text
5*(q2+q1+q0) + (15/2)*(r2+r1+r0) + la - 20,
```

which equals `-5` if and only if `la=0`. The filter is therefore exactly the charged grade. There are 6 possible R-squares and 10 possible Q-cubes; the residual contains 14 of them (coefficients of `r0^2` and `q0^3` are zero). Every stored residual monomial has extra-variable support 0 and boundary `-5`. The compiler fail-closes on any boundary drift.

The fourteen terms, already in toric canonical order, SHA recomputed as `json.dumps(canonical, separators=(",", ":"))`:

```text
R-square:
  -17/54 r2^2,  +4/9 r2 r1,  -1/18 r1^2,  -1/9 r2 r0,  +4/27 r1 r0
Q-cubic:
  +25/81 q2^3,  -14/27 q2^2 q1,  +17/81 q2^2 q0,
  +17/81 q2 q1^2,  -8/27 q2 q1 q0,  +1/27 q2 q0^2,
  -4/81 q1^3,  +1/27 q1^2 q0,  -4/81 q1 q0^2.
```

SHA

```text
5a8d5aba718de8396363443cd7b951c83ece5bea4707ca4cc063ae5b9dbd89ef.
```

This 14-term polynomial is coefficient-and-monomial equal to the h-linear R-square/Q-cubic piece of the frozen V5 corrected witness (extracted from V5 records: `h=1`, those bidegrees, no extra variables). That is the reconstructed V5 leftover, not a citation of the V5 review: V5 cancelled Q-R and stopped; V6's `residual0 = C_1 + g0·row0` is V5's `C_1`. The five displayed V5 r-square face terms

```text
-17/54 h r2^2 + 4/9 h r1 r2 - 1/18 h r1^2 - 1/9 h r0 r2 + 4/27 h r0 r1
```

are exactly the R-square block above. The nine Q-cubes are the rest of the same closed-corner grade; they carry positive Q-slope in the open quadrant, but they are in the charged complete grade and must be cancelled.

The five kernel images are not serialized as polynomials; their toric digests are

```text
8c9c079174a631af7e35a3ca4bf36492c6161c25c23611f9c5bd061dc767974d
fb23eccb8542eb5f6c69b240041e7ee6d4b3b8cb079c257c51d63caacc6eaef2
1fcffcb1f487f2eab392fba730fb269d51ba07b08d001185d23b833ae67f7dd4
5f63e8c146525275bcb5d083dea28dc8a25843c4df0ac0ef95e660cd01a81c81
883deebcc2c6174a6cc647ef2491536e4fb8cc3bfeb2f4043bd86507f5b275d6.
```

Both hosts emit the same five SHAs. `exact_rref` is called on those five sources against `-next_piece`, and fail-closes unless the recovered linear combination equals the target. Dual AWS both returned `SOLVABLE`.

The emitted augmented RREF is 16 by 6 (all 16 R-square/Q-cube monomials, including the two zero-target monomials `r0^2` and `q0^3` that appear in kernel images). Exactly three nonzero rows:

```text
[ 1, 0, 0, -4/3,  1 |  1/4 ]
[ 0, 1, 0,    1, -2/3 | -1/3 ]
[ 0, 0, 1,    0,    0 |    0 ]
```

Pivots `(0,1,2)`, matching JSON `grade5_pivots_zero_based` and `grade5_rank=3`. Free-zero solution: last column on the pivot rows, free columns 3 and 4 set to zero, i.e.

```text
(1/4, -1/3, 0, 0, 0).
```

This is unique as a free-zero point, not unique in the five-dimensional Q-R kernel: the leftover kernel of the grade-5 map is two-dimensional, with free-column basis

```text
(4/3, -1, 0, 1, 0),  (-1, 2/3, 0, 0, 1)
```

corresponding to the F7 and F8 directions after reducing by the three grade-5 pivots. The canonical particular solution sets those coordinates to zero. That is the same free-zero convention V5 used on the Q-R map, and it is the charged solution.

---

## Charge 4 — Combined correction `(5/2,-25/18,0,1/4,-1/3,0,0,0)`; 71-term identity; signs; rows

**CONFIRMED. Combining `g0` with `(1/4,-1/3,0,0,0)` on the ordered kernel basis yields exactly `(5/2,-25/18,0,1/4,-1/3,0,0,0)` in 1-based row order `(F1,...,F8)`. The recorded 71-term polynomial has `h=0` equal to reviewed `W'`, empty h-linear Q-R support, and empty h-linear R-square/Q-cubic support. Signs and row numbering match the source.**

Hand combination, kernel ordered as `(k1,...,k5)` in free-column order `(F4,F5,F6,F7,F8)`:

```text
g = g0 + (1/4) k1 + (-1/3) k2

g1 = 11/6 + (1/4)(4/3) + (-1/3)(-1) = 11/6 + 1/3 + 1/3 = 15/6 = 5/2
g2 = -11/12 + (1/4)(-1) + (-1/3)(2/3)
   = -11/12 - 1/4 - 2/9
   = -33/36 - 9/36 - 8/36 = -50/36 = -25/18
g3 = 0
g4 = (1/4)(1) = 1/4
g5 = (-1/3)(1) = -1/3
g6 = g7 = g8 = 0.
```

Source applies `t.monomial(g[ell-1], h=1)` to `fs[ell]` for `ell=1..8`. Thus

```text
F1'' = F1' + (5/2) h,
F2'' = F2' - (25/18) h,
F3'' = F3',
F4'' = F4' + (1/4) h,
F5'' = F5' - (1/3) h,
F6'' = F6',  F7'' = F7',  F8'' = F8'.
```

F2 and F5 are the negative rows. F3 is a Q-R pivot that happens to have zero particular-solution coordinate in both grades. F6 is already in the Q-R kernel and is left at zero. F7 and F8 are the leftover grade-5 kernel and are left at zero by the free-zero convention. Compact SHA of the eight-vector matches JSON `full_scalar_h_correction_sha256=4edd07c9…`.

The 71-term polynomial is reconstructed from the certificate records (coefficient, exponent tuple in toric `NAMES` order) and hashed in toric canonical format. Digest

```text
3363e67da50c953ab37b4c67dc5dfeb77d3cfdf75e31b5d6f97dd87dafc7f833
```

matches both JSON payloads, both stdout streams, `RESULT.md`, and the required anchor. Term count 71; unique monomials 71. `h`-exponent histogram: 37 of `h=0`, 18 of `h=1`, 15 of `h=2`, 1 of `h=3`.

`h=0` slice: 37 terms, coefficient-and-monomial equal to the V4 `h=0` dictionary and to the V5 `h=0` dictionary (empty symmetric difference, empty coefficient mismatch). Recomputed V1 digest of that slice is `ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b`. Dual AWS fail-close if `specialize_h_zero(corrected) != w0`.

H-linear coefficient: the 18 terms with `h=1`, `h` decremented, toric digest `6fee8f428caa5364b3390a4c835c2a47214e91e2f8d6d6709137f3c428d0d5e3`, matching JSON `corrected_c1_sha256` and `corrected_c1_terms=18`. Among those 18:

- Q-R monomials (`qdeg=rdeg=1`, no extra variables): **0**. JSON `residual_qr_terms=0`. The eight V4 extremals are gone and no new Q-R term appears.
- R-square or Q-cubic monomials (no extra variables): **0**. JSON `residual_grade5_terms=0`. The fourteen-term residual is gone.

The compiler fail-closes if either component of `corrected_c1` is nonempty. Dual AWS both passed. This review did not replay the product; the recorded 71-term support is the charged identity.

---

## Charge 5 — Every term weight; exact range `eta>=15/4`; eight `h^2 q r` coefficients; converse; 28

**CONFIRMED. The recorded difference of every non-target monomial from target weight `20L` is exactly `c + U u + V v + E eta`. There is no `rho` term. The only `tau` term is the skipped `la^20 tau`. Integer arithmetic on all 71 records proves: unique least term `la^20` for every `u,v>0`, `T>0` if and only if `eta>=15/4`. The eight displayed `h^2 q r` terms are present with the displayed coefficients, are the unique maximizers of `-c/E`, and have open-quadrant margins `v` or `u` at equality. The converse holds for every `0<eta<15/4`. The closed-corner face has 28 terms.**

Weight convention, matching the reviewed V4/V5 sample after restoring `beta=5+u`, `delta=5+v` and `eta=wt(h)/L`, with `alpha` held at `15/2`:

```text
(wt - 20L)/L
  = (la-20) + (T/L) tau + (H/L) rho
    + (5+v) q2 + (5+u)(q1+q0) + (15/2)(r2+r1+r0) + eta * h.
```

The compiler records, for every monomial,

```text
c = (la-20) + 5(q1+q0) + 5 q2 + (15/2)(r2+r1+r0),
U = q1+q0,  V = q2,  E = h,
```

and skips only `la^20` (the target) and `la^20 tau` (strictly above once `T>0`). Both skips are present with coefficient `1`. No record has `rho>0`. Every other record has `tau=0`. Therefore on the 69 charged terms the recorded form is exact, not a lower bound, and `T` enters the uniqueness statement only through the skipped `la^20 tau`.

Integer check, all 71 difference-forms against exponents: 71/71 match (`eta=h`, `delta=q2`, `beta=q1+q0`, `alpha=r2+r1+r0`, `constant=la-20`, `T_over_L=tau`, `H_over_L=rho`). Integer check, all 69 recorded constants: the reduced fraction of `2(la-20)+10(q0+q1+q2)+15(r0+r1+r2)` over `2` equals the stored string, and `(U,V,E)=(q0+q1, q2, h)`, 69/69. Extra-variable support is empty on all 71 terms.

Histogram of the 69 charged terms by recorded `c`:

```text
c      count   of which E=0   E>0
-15/2      9        0          9
-5         5        0          5
-5/2       9        0          9
 0        30       20         10
 5/2      11       10          1
 5         5        5          0
```

`9+5+9+30+11+5=69`. Among `h=0` charged terms, 20 have `c=0` and 15 have `c>0`; zero have `c<0`. Among `h>0` terms, 23 have `c<0` and 11 have `c>=0`. `20+15=35` old charged plus 2 skipped plus 34 correction equals 71.

Ratios `-c/E` for the 23 terms with `E>0` and `c<0`:

```text
15/4   8 terms   (all E=2, c=-15/2)
 5/2  14 terms
 5/4   1 term
```

Maximum is `15/4`. No term has `-c/E > 15/4`. The nine `c=-15/2` terms split as eight with `E=2` (ratio `15/4`) and one with `E=3`, namely `-8/81 h^3 q2 r2` (ratio `5/2`), which at `eta=15/4` sits strictly above by `15/4`.

For a term with `U,V,E >= 0`, uniqueness of least term `la^20` for all `u,v>0` at fixed `eta` holds iff every charged term satisfies either `c+E eta > 0`, or `c+E eta = 0` and `U+V > 0`. Increasing `u` or `v` cannot create a new below-target term, because `U,V >= 0`.

Verified on the 69 charged records:

- `h=0` and `c<0`: **0**.
- `h=0` and `c=0`: **20**, and every one has `U+V > 0`. These are the twenty old closed-corner threshold monomials of reviewed `W'`, identical to the V4 list.
- `h=0` and `c>0`: **15**, strictly above even at the closed corner, for every `eta`.
- `E>0` and `c<0`: **23**. The exact ratio `-c/E` is at most `15/4`, with equality on **exactly 8** terms (all of them `E=2`, `c=-15/2`).
- At `eta=15/4`: **0** terms with `c+(15/4)E < 0`; **28** with equality (20 old + 8 new); **0** of those 28 have `U=V=0`. Independent face set equals JSON `threshold_face_terms`.

Hence:

- If `eta > 15/4`, every charged term has `c+E eta > 0` or (the 20 old `c=0` terms) `c+E eta = 0` with `U+V>0`. Unique least term `la^20` throughout the open quadrant.
- If `eta = 15/4`, the same, with the eight new terms now on the threshold face; each has margin `U u + V v` with `U+V=1`, so equality at `u=v=0` is strict for `u,v>0`.
- If `0 < eta < 15/4`, each of those eight terms has `c+E eta < 0`. They are present (nonzero coefficients). None carries `tau` or `rho`. Choosing the relevant `u` or `v` in `(0, 15/2-2 eta)` puts that term strictly below target.

The two skipped monomials: `la^20` is the target; `la^20 tau` has extra weight `T>0`. No other `la`-positive term exists. JSON `eta_uniform_infimum=15/4` and `eta_equal_infimum_is_strict_on_open_quadrant=true` match this classification.

Displayed extremals, read from the certificate, coefficients and monomials equal to `RESULT.md`:

```text
-77/162 h^2 q2 r2     c=-15/2  U=0  V=1  E=2    Δ/L = 2 eta - 15/2 + v
 +8/27  h^2 q2 r1     c=-15/2  U=0  V=1  E=2    Δ/L = 2 eta - 15/2 + v
 -5/54  h^2 q2 r0     c=-15/2  U=0  V=1  E=2    Δ/L = 2 eta - 15/2 + v
 +8/27  h^2 q1 r2     c=-15/2  U=1  V=0  E=2    Δ/L = 2 eta - 15/2 + u
 -5/54  h^2 q1 r1     c=-15/2  U=1  V=0  E=2    Δ/L = 2 eta - 15/2 + u
 +8/81  h^2 q1 r0     c=-15/2  U=1  V=0  E=2    Δ/L = 2 eta - 15/2 + u
 -5/54  h^2 q0 r2     c=-15/2  U=1  V=0  E=2    Δ/L = 2 eta - 15/2 + u
 +8/81  h^2 q0 r1     c=-15/2  U=1  V=0  E=2    Δ/L = 2 eta - 15/2 + u
```

There is no `h^2 q0 r0` term. At `eta=15/4` the first three have margin `v` and the other five have margin `u`. On the closed corner `u=v=0` they tie the target; throughout the open quadrant the inequality is strict. These eight are the unique terms with `-c/E = 15/4`.

Converse: fix `0<eta<15/4`. The term `-(77/162) h^2 q2 r2` is present. It has no `tau` and no `rho`. Choose `0 < v < 15/2 - 2 eta` and any `u>0`, `T>0`. Then `Δ/L = 2 eta - 15/2 + v < 0`, so this term lies below target. The same works with any of the last five, using `u` in place of `v`. The interval `(0, 15/2-2 eta)` is nonempty precisely when `eta<15/4`. No smaller positive eta therefore gives a uniform open-quadrant conclusion from this witness.

The 28 closed-corner threshold monomials at `eta=15/4` are the twenty old `W'` corner terms (`E=0`, `c=0`) plus these eight `h^2 q r` terms. That is JSON `threshold_face_terms` and the independent classification.

The twenty old terms, all `h=0`, `c=0`, `U+V>0`, match the V4 face list:

```text
q2 r2^2, q2 r1 r2, q2 r1^2, q2 r0 r2, q2 r0 r1, q2^4,
q1 r1 r2, q1 r1^2, q1 r0 r2, q1 r0^2, q1 q2^3, q1^2 q2^2, q1^3 q2,
q0 r0 r1, q0 q2^3, q0 q1 q2^2, q0 q1^2 q2, q0^2 q2^2, q0^2 q1 q2, q0^3 q1.
```

Successive exact witness ranges, charged on the recorded polynomials:

```text
unchanged W':             eta >= 15/2,
V5 Q-R correction:        eta > 5,
V6 kernel grade-5 lift:   eta >= 15/4.
```

V5 could not claim `>=5` because its leftover r-square terms had `U=V=0`. V6 cancelled that entire grade, so the next face has `U+V=1` and equality is open-strict.

---

## Charge 6 — Scope: two named h-linear grades, not a surviving branch

**CONFIRMED. The licensed theorem is the Promotion paragraph. Completeness is only for scalar `h` corrections through the Q-R grade and the R-square/Q-cubic grade.**

Admissible:

- For `eta>=15/4`, this explicit scalar-corrected combination `W_h''` has unique least term `la^20` uniformly on `u>0`, `v>0`, `T>0`, at the fixed axis/cusp chart `a=1`, `p=-3`, `c=2+h`, loads `k=nu=0`, `mu=2/3`, and full `Q,R` support.
- The correction is the canonical free-zero point of the rank-3 Q-R map plus the canonical free-zero point of the rank-3 grade-5 map on the full 5-dimensional Q-R kernel.
- For `0<eta<15/4`, the same polynomial does **not** transport uniformly. The next obstruction is the displayed `h`-squared Q-R piece. That cell requires the next filtered correction; it is not a branch survivor.

Not admissible, and not claimed by the frozen firewall string
`complete scalar h correction through closed-corner grade -5; iterate remaining grades; polynomial multipliers and h-adic lift open`
or by `RESULT.md` §Firewall:

- any statement for `eta<15/4` other than the negative control on this witness;
- polynomial multiplier-support completeness (the leftover 2-dimensional kernel of the grade-5 map, and all non-scalar multiplier directions, remain open);
- an `h`-adic or formal lift;
- moving axis, moving loads, or a theorem that the unit-axis map acts on the submitted rows;
- equality-support faces (the 28 threshold monomials are listed; their initial-form equalities are not solved);
- another normal direction (`p` is fixed at `-3`);
- a formal-arc / formal-lift obstruction;
- the whole double-root fan, D1, or JC2;
- a claim that V4 or V5 already settled the cusp direction down to `eta=15/4` (they did not; that is this package).

The reviewed q2 lift remains valid on the special fibre `h=0`. The reviewed V4 transport remains the correct classification of the *unchanged* multipliers (`eta>=15/2`). The V5 Q-R correction remains the correct classification of the first scalar `h`-correction (`eta>5`). This package classifies only the weight behaviour of one explicit scalar-corrected witness through the two named h-linear grades.

---

## Nits, not defects

1. Harvest trees contain sentinels, `free.*`, `hostname`, `uname`, `nproc`, UTC stamps, and empty launch stdio, none of which are in `FREEZE.sha256`. They were used as custody, not as a second freeze. Harvest copies of source files that *are* frozen at the package top were `cmp`-identical.
2. Original 9-by-8 Q-R matrix entries and the five grade-5 kernel-image polynomials are not serialized, only RREF / kernel vectors / image SHAs. Dual-AWS RREF, the empty row-6 Q-R digest, the compiler's fail-closed residual and kernel-annihilation checks, and the V4/V5/V6 support comparison jointly verify the maps. A later package that wants an independent reconstruction of the raw matrices must emit the sources.
3. The compiler's `eta0 = max(-c/E)` loop does not, by itself, inspect `U,V` on the threshold face. The certificate stores the 28 face monomials and the boolean `eta_equal_infimum_is_strict_on_open_quadrant=true`; this review charged both. The open-quadrant strictness at `eta=15/4` is in the records, not only in the `max` reduction.
4. `AWS_LAUNCH_METADATA.md` writes `04:12Z` to the minute; the file mtime is `04:11:34Z`, which is the actual pre-GO observation. r6d `free` shows 129 GiB used vs box03 22 GiB; swap is zero on both, and this job's RSS is 22 MiB under a 4 GiB `ulimit -v`. The registration notes the unrelated retained toric-B Singular job on r6d. That is not evidence that another campaign job was stopped, and not a defect in this package.
5. V6 JSON bytes are not identical across hosts, by the preregistered `tag`/`order` fields. The algebraic payload is. That is the correct dual-encoding pattern once the certificate records its own tag.
6. V5 remains a source-pinned producer package in this V6 freeze; a separate V5 review file now ends confirmed. This V6 review reconstructed the V5 Q-R eight-term piece, RREF kernel, and fourteen-term leftover from records rather than treating that report as a lemma.

No source or certificate repair is required.

H_GRADE5_KERNEL_LIFT_CONFIRMED
