# Hostile text-only review — control-2 first graded transverse-cusp Q-R syzygy lift V5

| Field | Value |
|---|---|
| Claim under review | One scalar `h`-correction of the worst Q-R graded piece of the V4 witness: `F1''=F1'+(11/6)h`, `F2''=F2'-(11/12)h`, `Fi''=Fi'` for `i>=3`, producing a 90-term polynomial whose `h=0` slice is the reviewed q2 witness, whose full `h`-linear Q-R component vanishes, and which is uniformly unique-target on `u,v>0`, `T>0` if and only if `eta>5` |
| Overall verdict | **H_QR_SYZYGY_LIFT_CONFIRMED**. Dual AWS encodings emit certificates that differ only in `tag` and `order`; deleting those fields gives canonical sorted SHA `4726e9ae…`. The extracted worst Q-R piece of V4 `C_1` is exactly eight monomials, each of closed-corner pre-`h` margin `-15/2`, SHA `52bc3441…`. Stored RREF has rank 3, pivots `(0,1,2)`, and free-zero solution `(11/6,-11/12,0,…,0)`. The 90-term polynomial SHA `a4d11309…` is an exact identity, not a congruence: `h=0` is the reviewed 37-term `W'`, the eight V4 Q-R terms are deleted and no new Q-R term appears, and six other coefficients (including one `h^2` term) change. Integer arithmetic on all 90 recorded forms proves unique least term `la^20` iff `eta>5`. The `eta=5` face and `eta<5` are next-lift/full-face problems, not branch survivors |
| Smallest failing identity | none in the frozen V5 source, either harvest tree, either AWS stream, the hash-pinned V4 source, or the recorded 90-term polynomial |
| Smallest missing hypothesis for a stronger theorem | a correction of the `eta=5` r-square face; a correction for `0<eta<=5`; scalar-support completeness of the eight-row module; an `h`-adic lift; moving axis or moving loads; another normal direction; a formal arc; the whole double-root fan; D1; or JC2 |
| Evidence tier | SHA-256 of the freeze chain and already-emitted AWS files; `cmp` of harvest copies against package-top source; `jq`/canonical-JSON comparison of the two certificates after deleting `tag` and `order`; integer/rational arithmetic on every recorded `(c,U,V,E)`; V1-format digest of the `h=0` slice; toric canonical digest of the 90-term polynomial and of the 8-term Q-R piece extracted from frozen V4 records. No local Singular, Sage, msolve, gfan, Lean, Python algebra, compiler execution, charged reconstruct, or eight-row product replay |
| Reviewer / model | Grok 4.6 (xAI). Text-only tropical / commutative-algebra / CAS-custody referee |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `574e873d4753b57dbaeb0fb83e320fbef3694724` |
| Host | Darwin. V5 compiler, V4 compiler, V1 compiler, toric compiler, charged reconstruct, Singular, and every solver were not run |

## What was and was not run

No local substantive computation was run. In particular this review did **not** execute `compile_h_qr_syzygy_lift_v5.py`, `compile_h_first_transport_v4.py`, `compile_q2_first_lift.py`, `compile_toric_blowup.py`, `independent_reconstruct.py`, Singular, Sage, msolve, Lean, Gfan, or any other solver, and it did not re-multiply `sum F_i'' E_i(h)` or reconstruct the unsubstituted eight rows. Hashes were checked with `shasum -a 256`. File identity was checked with `cmp`. Marker counts used `grep`. Git identity was read with `git rev-parse`. JSON fields were read with `jq`. Canonical SHA-256 values and rational weight forms were recomputed from the already-emitted certificate records (V1 digest format for the `h=0` slice; toric canonical format `[[list(monomial), num, den], ...]` for `C_1` Q-R and for the 90-term polynomial). Recorded weight forms were checked by the integer identity `2c = 2(la-20)+10(q0+q1+q2)+15(r0+r1+r2)`.

Charged freeze SHA-256, recomputed and matched:

```text
f166e2ba9aa8e2c4715f14a4f29ed7dd4296755ed5de551de94784be3e911471  FREEZE.sha256
c9469bb0041ba34e16732e33b3944f04217009f35473275429b708fc060d680e  RESULT.md
2741a8e2536b7315f524747b2902be0afdc383bb4095e2d854592cc2d481667b  aws_box03_forward/h_qr_lift.json
92573ef289aa3484e0b35019c0335ebdae48531759fe6fc7c69d40ade12c2350  aws_r6d_reverse/h_qr_lift.json
```

Prerequisite V4 transport, recomputed and matched:

```text
6ddb1343c7b30d0e4e6daf7e5f13ea364205e1a776c60534d02da26a7c529f14  RESULT.md
0ff05368ab7a5751617db6a6b9a31e67545439ed5fb688cb15238ef879637b68  FREEZE.sha256
```

Every path listed in `FREEZE.sha256` recomputed and matched (23/23). Nested `SOURCE_CLOSURE.sha256` (8/8) and both harvested `result.sha256` manifests (5/5 each) matched from the case root / harvest directory as appropriate. Empty compiler stderr files are the empty-string digest `e3b0c442…`. Both rc files are the two-byte string `"0\n"`, digest `9a271f2a…`.

Read in full before the verdict: every file at
`cases/max12_912_order3_d1_double_root_control2_h_qr_syzygy_lift_v5_20260826/`
including both harvest trees; the hash-pinned V4 compiler `coefficient_images` / multipliers / `specialize_h_zero` / `divide_h`; the hash-pinned toric `NAMES` / `canonical` / `digest`; V1 `multipliers` / `digest`; V4 certificate records far enough to extract the `h`-linear Q-R piece; and the V4 review
`xmodel/max12-912-order3-d1-double-root-control2-h-first-transport-review-grok-20260826.md`.
Predecessor conclusions were recomputed, not inherited.

---

## Promotion

**Accept `FOR THE PINNED ORDINARY-TAIL EIGHT-ROW MODULE AT a=1, p=-3, c=2+h, k=nu=0, mu=2/3, FULL Q AND R, STARTING FROM THE REVIEWED Q2-CORRECTED MULTIPLIERS F1'=F1+q2/12, F2'=F2-q2/9, Fi'=Fi (i>=3), THE REGISTERED DUAL-AWS V5 RUNS EMIT ONE 90-TERM POLYNOMIAL W_h' = SUM_i F_i'' E_i(h) WITH F1''=F1'+(11/6)h, F2''=F2'-(11/12)h, Fi''=Fi' (i>=3). THIS IS AN EXACT POLYNOMIAL IDENTITY, NOT A CONGRUENCE. ITS h=0 SPECIALIZATION IS THE REVIEWED 37-TERM W' (SHA ddb451c4…). ITS COMPLETE h-LINEAR Q-R COMPONENT IS ZERO. NORMALIZE wt(la)=L, PUT alpha=15/2, beta=5+u, delta=5+v, eta=wt(h)/L, AND RESTRICT TO u>0, v>0, T>0. THEN W_h' HAS UNIQUE LEAST-WEIGHT TERM la^20 FOR EVERY SUCH (u,v,T) IF AND ONLY IF eta>5. AT eta=5 FIVE PRESENT h r^2 TERMS TIE THE TARGET INDEPENDENTLY OF u,v; NINE PRESENT h-LINEAR Q-CUBIC TERMS REACH THE CLOSED CORNER BUT HAVE POSITIVE Q-SLOPE IN THE OPEN QUADRANT. FOR EVERY 0<eta<5 THOSE r-SQUARE TERMS LIE STRICTLY BELOW TARGET. THIS IMPROVES THE UNCHANGED-WITNESS RANGE eta>=15/2 TO eta>5. THE eta=5 FACE AND eta<=5 ARE NEXT-LIFT / FULL-FACE PROBLEMS, NOT BRANCH SURVIVORS.`**

Do not promote this to: scalar-support completeness; an `h`-adic lift; a moving-axis or moving-load theorem; equality-support analysis of the 34-term face beyond the recorded weights; another normal direction; a formal-arc obstruction; a whole double-root fan; D1; or JC2.

---

## Charge 1 — Custody, freeze, dual AWS, source closure, JSON difference

**CONFIRMED. Every freeze entry recomputes. Both registered workers are fail-closed, hash-gated, empty-stderr, sub-cap, pre-GO, and source-closed against the package-root manifest. Opposite traversal orders return certificates that differ only in `tag` and `order`; deleting those two fields gives literally identical sorted JSON of SHA `4726e9ae886c2b9aef35ed0e48e04229e6b8b1e576fca506ef39e4e2dc49f8fe`.**

Required anchors, recomputed:

```text
c9469bb0041ba34e16732e33b3944f04217009f35473275429b708fc060d680e  RESULT.md
f166e2ba9aa8e2c4715f14a4f29ed7dd4296755ed5de551de94784be3e911471  FREEZE.sha256
2741a8e2536b7315f524747b2902be0afdc383bb4095e2d854592cc2d481667b  aws_box03_forward/h_qr_lift.json
92573ef289aa3484e0b35019c0335ebdae48531759fe6fc7c69d40ade12c2350  aws_r6d_reverse/h_qr_lift.json
```

Recomputed `FREEZE.sha256` entries, all matched:

```text
c9469bb0041ba34e16732e33b3944f04217009f35473275429b708fc060d680e  RESULT.md
bfe7b967eac6846b4682ac38bc9d6c3e3433b876716adf06a4f54b2d00471ffe  PREREGISTRATION.md
aa71dd6faff84025ba1dc51b8ab27d1d1f55112f9a2f30749b9bf5fb24f2b0ca  AWS_REGISTRATION.md
0b30826ee15dab36536c94f2db54e7037ad13b5df96150780357790621f19935  AWS_LAUNCH_METADATA.md
530fb09744f1b7101959e1a9c46e272e306468c63d029876ecaf11d04ab8bd29  SOURCE_CLOSURE.sha256
8a963360f16a29c6841050f82e9eb79051005d821c6ec7837d0614ca8ead7366  compile_h_qr_syzygy_lift_v5.py
31992962db96ac5cb9e6b4947fa851352e4e34e2abae0ffadd03c5ed0c18445d  remote_worker.sh
2741a8e2536b7315f524747b2902be0afdc383bb4095e2d854592cc2d481667b  aws_box03_forward/h_qr_lift.json
9e5ca815374a17e6c4f3fed93fe15d6592086a669f07072a9930eb7d5c5c80c5  aws_box03_forward/compiler.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_box03_forward/compiler.stderr
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  aws_box03_forward/compiler.rc
ec66fb5142110aba485902c5063ae3541b163e5f36e21b2a84d8f4706700b16d  aws_box03_forward/compiler.time
b148f9f8f4c783bde6b0e11914929d968de85bfb27ab8baf976a44f0fefe1ab4  aws_box03_forward/result.sha256
d0eff82e91ff307ad65fcad7e53a23481e9d062555e39e385072f852a6ea88d4  aws_box03_forward/source.check
e7982a235c27b1bf55114d440000707e559f9e307b066f5875f51cf4e1ef05ad  aws_box03_forward/worker.metadata
92573ef289aa3484e0b35019c0335ebdae48531759fe6fc7c69d40ade12c2350  aws_r6d_reverse/h_qr_lift.json
5119c80ee9fbb38b1a70200a2b8ae5ff59b5b9e2822af6a7a2813723bb4cf5ed  aws_r6d_reverse/compiler.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_reverse/compiler.stderr
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  aws_r6d_reverse/compiler.rc
05a1927564a6667e958332cd3ab7f4833ef5af08737d9d167873b8c94ed5ad02  aws_r6d_reverse/compiler.time
a1fcc3e3afab7cf2f2bc8d84043e09f27646f1c444c5975761f0863da377ce38  aws_r6d_reverse/result.sha256
d0eff82e91ff307ad65fcad7e53a23481e9d062555e39e385072f852a6ea88d4  aws_r6d_reverse/source.check
19db9693f130905891937db425abc8006a2587ae78e8ab3d54d18dda01038500  aws_r6d_reverse/worker.metadata
```

Source-closure entries, all matched from the package root:

```text
bfe7b967eac6846b4682ac38bc9d6c3e3433b876716adf06a4f54b2d00471ffe  PREREGISTRATION.md
aa71dd6faff84025ba1dc51b8ab27d1d1f55112f9a2f30749b9bf5fb24f2b0ca  AWS_REGISTRATION.md
8a963360f16a29c6841050f82e9eb79051005d821c6ec7837d0614ca8ead7366  compile_h_qr_syzygy_lift_v5.py
31992962db96ac5cb9e6b4947fa851352e4e34e2abae0ffadd03c5ed0c18445d  remote_worker.sh
3bbf1ebfb9f8b15054fe2f592bea92d8e07b95bce4d6ca131cd81c95f3698306  ../max12_912_order3_d1_double_root_control2_h_first_transport_v4_20260826/compile_h_first_transport_v4.py
c76ef85ac14f81839674368c55a324499832e6cf4b589befa68baf93a42b1490  ../max12_912_order3_d1_double_root_toric_blowup_20260825/compile_toric_blowup.py
0385b0b1e60b3bd37fa5fbee90dd6c17a454722bdbff424ea83c2ab0fa19df45  ../max12_912_order3_d1_double_root_control2_q2_first_lift_v1_20260826/compile_q2_first_lift.py
67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623  ../max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/independent_reconstruct.py
```

Harvested `SOURCE_CLOSURE.sha256` is byte-identical to the top copy on both hosts. Both `source.check` files are identical (`d0eff82e…`) and print `OK` on those eight paths. The worker `cd`s to `$run` before `sha256sum -c SOURCE_CLOSURE.sha256`; `AWS_LAUNCH_METADATA.md` states that each run directory is the package under the job root's `cases/`. The sibling `../max12_…` paths are therefore `cases/`-neighbours, which is how AWS ran and how this review rechecked.

The compiler pins V4 at `V4_SHA=3bbf1ebf…` and refuses a non-matching file before import. V4 in turn re-pins toric `c76ef85a…`, V1 `0385b0b1…`, and `independent_reconstruct.py` at `67343b56…`. Tag gates: worker `case` requires prefix `max12_912_order3_d1_double_root_control2_h_qr_syzygy_lift_v5_20260826T*`; compiler `require_aws` requires Linux, DMI vendor `Amazon EC2`, and tag prefix `max12_912_order3_d1_double_root_control2_h_qr_syzygy_lift_v5_`. Both refuse non-`forward`/`reverse` orders.

| Check | Box03 forward | r6d reverse |
|---|---|---|
| Public IP / harvested hostname | `98.80.65.144` / `ip-172-30-0-249` | `100.26.198.153` / `ip-172-30-0-45` |
| Tag | `…_v5_20260826T035900Z_box03_forward` | `…_v5_20260826T035900Z_r6d_reverse` |
| Worker PID | `154388` | `222147` |
| Caps | `memory_kib=4194304`, `timeout=900`, `nice -n 10`; `ulimit -v 4194304` | same |
| Order | `forward` (`ell=1..8`) | `reverse` (`ell=8..1`) |
| Started / finished UTC | `2026-08-26T04:00:42Z` / `04:01:19Z` | `04:00:43Z` / `04:01:20Z` |
| Compiler stdout SHA | `9e5ca815…` | `5119c80e…` |
| Certificate SHA | `2741a8e2…` | `92573ef2…` |
| RSS / swap / exit | 22544 KiB / `Swaps: 0` / 0 | 22584 KiB / `Swaps: 0` / 0 |
| Pre/post `free` swap | `0B` / `0B` | `0B` / `0B` |
| Elapsed | 5.91 s | 5.87 s |
| PASS markers, each once | `PASS_H_QR_SYZYGY_LIFT_V5_SOLVABLE`, `PASS_REMOTE_WORKER` | same |
| `FAIL_` / `REFUSED` / `FAILED` | none; stderr empty | none; stderr empty |

`AWS_LAUNCH_METADATA.md` is timestamped locally `2026-08-25T21:00:59` PDT = `2026-08-26T04:00:59Z`, after worker start (`04:00:42Z`) and before GO. Content: both workers `WAITING_GO`; “Neither run directory contained a GO sentinel when the worker PID and caps were read”; source-closure manifest SHA `530fb097…` matching the frozen file. GO sentinels exist and are empty; local mtimes place GO after that registration (box03 `04:01:12Z`, r6d `04:01:13Z`) and DONE at finish (`04:01:19Z` / `04:01:20Z`). No `REFUSED` or `FAILED`. The 7-second GO-to-DONE window matches the 5.91 s compile plus the post-GO source-hash check.

Harvest copies of compiler, worker, preregistration, AWS registration, and source closure are byte-identical to the package top on both hosts (`cmp`). The two JSON files are **not** byte-identical (97009 vs 97007 bytes). Their key sets are equal. The only value differences are the two preregistered custody fields `tag` and `order`. Deleting those fields and dumping with `sort_keys=True, indent=2` plus a trailing newline yields one 96883-byte blob of SHA

```text
4726e9ae886c2b9aef35ed0e48e04229e6b8b1e576fca506ef39e4e2dc49f8fe
```

on both hosts, matching `RESULT.md`. Compiler stdout differs only in the preregistered `ORDER=` line and the certificate SHA of the tagged JSON; the algebraic metric block is identical:

```text
STATUS=SOLVABLE
SOLUTION=11/6,-11/12,0,0,0,0,0,0
C1_QR_SHA256=52bc344149c71253a551134e23b5b8f0008e2bd15b6424f13862d2742acfa27b
CORRECTED_WITNESS_SHA256=a4d11309d1f2195a1908c5ba0c4f36935b1c2c48170e30775b8372a4bd20621d
CORRECTED_WITNESS_TERMS=90
ETA_UNIFORM_INFIMUM=5
ETA_EQUAL_OPEN_STRICT=0
PASS_H_QR_SYZYGY_LIFT_V5_SOLVABLE
```

Every extra toric variable `p,c,a,x,y,k,mu,nu` is zero on all 90 recorded terms. Support is exactly `{h,la,tau,q2,q1,q0,r2,r1,r0}`.

---

## Charge 2 — Full `h`-linear coefficient from V4; worst Q-R component; SHA `52bc3441…`

**CONFIRMED. The V4 source constructs `W_h=sum_i F_i' E_i(h)` at `p=-3`, `c=2+h`, full Q and R, empty `kbar`, with the reviewed q2-corrected multipliers. `C_1=[(W_h-W')/h]_{h=0}` is the 45-term `h`-linear slice of that 98-term polynomial. Its closed-corner-worst graded piece is exactly the eight monomials of Q-degree 1, R-degree 1, and no other factor, each of pre-`h` margin `-15/2`. Canonical SHA of that eight-term polynomial is `52bc344149c71253a551134e23b5b8f0008e2bd15b6424f13862d2742acfa27b`, matching V5 `c1_qr_terms` byte-for-byte.**

Construction, from the hash-pinned V5 compiler, which loads the hash-pinned V4 compiler, which loads the hash-pinned toric ring and the hash-pinned V1 compiler:

1. `t.load_charged_source().build()["tails"]` is the eight negative Laurent tails of `independent_reconstruct.py` at `67343b56…`, in names `(a0..a7,k)`. Same charged ordinary-tail source as the reviewed V4 transport and q2 lift.
2. `v4.coefficient_images(t)` specialises the nine jet slots with no `x` (affine `x=1`) and no `a`:

```text
p = -3,  c = 2+h,
a0 = c^3 + c*q0 + r0,
a1 = 3 p c^2 + (p q0 + c q1) + r1,
a2 = 3 p^2 c + (p q1 + c q2) + r2,
a3 = p^3 + 3 c^2 + (q0 + p q2),
a4 = 6 p c + q1,
a5 = 3 p^2 + q2,
a6 = 3 c,
a7 = 3 p,
kbar = {}.
```

3. Substitute tails; subtract row-3 target `(2/3) la^15` and row-8 target `la^20(1+tau)`; no row-6 `nu` subtraction. Multipliers from V1 with `F1+=q2/12`, `F2+=-q2/9`. `W_h = sum_ell F_ell' E_ell(h)`. Fail-closed: `W_h|h=0` projected onto the V1 ring must digest `ddb451c4…`.
4. `C_1 = specialize_h_zero(divide_h(W_h - W'))`. The Q-R extractor keeps a monomial iff `q2+q1+q0 = 1`, `r2+r1+r0 = 1`, and every other exponent is zero. Fail-closed: that piece must have eight terms, each of closed-corner value `(la-20)+5(q-sum)+(15/2)(r-sum) = -15/2`.

Independent extraction from the frozen V4 certificate (98 records; not a compiler replay). Among the 45 terms with `h=1` (the full `C_1` before Q-R filtering), the closed-corner constants are

```text
c       count
-15/2      8
-5        14
-5/2      13
 0         9
 5/2       1
```

The minimum is `-15/2`, achieved on exactly eight terms. Those eight are precisely the monomials of one Q, one R, and no other factor; there is no `h`-linear Q-R term with an extra factor, and there is no `h q0 r0` term. Coefficients and monomials:

```text
-88/27 h q2 r2     c = -15/2
 +11/9 h q2 r1     c = -15/2
-22/27 h q2 r0     c = -15/2
 +11/9 h q1 r2     c = -15/2
-22/27 h q1 r1     c = -15/2
+11/27 h q1 r0     c = -15/2
-22/27 h q0 r2     c = -15/2
+11/27 h q0 r1     c = -15/2
```

Stripping the `h` factor recovers V5 `c1_qr_terms` as an equal list of toric canonical triples. Recomputed digest `52bc344149c71253a551134e23b5b8f0008e2bd15b6424f13862d2742acfa27b`. These are the same eight extremals already charged in the V4 review; V5's claim is that they are the complete worst graded piece of `C_1`, which the 45-term `h`-linear histogram confirms.

---

## Charge 3 — Coefficient matrix, rank/pivots, free-zero solution, residual

**CONFIRMED for the preregistered scalar correction. Stored RREF of the 9-by-8 Q-R system has rank 3 and pivots `(0,1,2)`. The canonical free-zero solution is `(11/6,-11/12,0,0,0,0,0,0)`, including signs and 1-based row numbering. The literal residual on all nine Q-R monomials is zero. Original matrix entries are not serialized; they are pinned by `row_qr_sha256` and by the V4/V5 support comparison. Module-support completeness is not inferred.**

The linear system, from the hash-pinned compiler, is

```text
sum_{i=1..8} g_i * QR(E_i(0)) = -QR(C_1)
```

over `Q`, with exact RREF and free columns set to zero. `graded_monomials` is the complete 9-element set of bilinear Q-R monomials, sorted as

```text
q0 r0, q0 r1, q0 r2, q1 r0, q1 r1, q1 r2, q2 r0, q2 r1, q2 r2.
```

Target `QR(C_1)` is supported on the last eight of these (`q0 r0` coefficient 0). The emitted augmented RREF is 9-by-9:

```text
[ 1  0  0  -4/3   1    0  -10/9   4/3  |  11/6  ]
[ 0  1  0   1    -2/3  0   2/3   -7/9  | -11/12 ]
[ 0  0  1   0     0    0   0      0    |   0    ]
[ 0  0  0   0     0    0   0      0    |   0    ]
  ... six further zero rows ...
```

Pivots, 0-based: columns `0,1,2` (`g1,g2,g3`). Rank 3. Free columns `3,4,5,6,7` (`g4..g8`). Column 5 (`g6`) is identically zero in RREF; independently, `row_qr_sha256[5]` is the empty-polynomial digest `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945` (`sha256("[]")`), so `QR(E_6(0))=0`. Pivot row 2 forces `g3=0`. Setting the five free variables to zero reads

```text
g1 = 11/6,  g2 = -11/12,  g3 = ... = g8 = 0.
```

This is the stored `solution` and the stored `solution_sha256` `7791f85c…`. Substituting that vector into every RREF row recovers the last column exactly (9/9). Signs and numbering: compiler does `F_ell'' = F_ell' + g_{ell} h` with `ell=1..8`, so

```text
F1'' = F1' + (11/6) h,
F2'' = F2' - (11/12) h,
Fi'' = Fi'  (i>=3),
```

matching `RESULT.md`. Dual AWS, opposite traversal, emit this same RREF and same solution.

Literal residual. Two independent readings, neither of which reconstructs original `A` locally:

1. Compiler fail-closed: after RREF it forms `sum g_i QR(E_i(0))` and refuses unless that equals `-QR(C_1)`. Dual AWS both exited 0.
2. Support comparison of the already-emitted polynomials, which does not require `A`. V4 `W_h` contains exactly the eight `h`-linear Q-R monomials of Charge 2 and no other `h`-linear Q-R monomial (including no `h q0 r0`). V5 `W_h'` contains none of those eight, no new monomial of any kind, and in particular no `h q0 r0`. Therefore the Q-R component of `C_1'' = C_1 + sum g_i E_i(0)` is the zero polynomial on all nine bilinear monomials. Certificate field `residual_qr_terms=0` matches.

Original 9-by-8 entries are not a frozen array; only RREF, the eight source digests, and the two polynomials are frozen. That is the same custody pattern as V4 not serializing the eight substituted rows. It is enough to verify this preregistered free-zero scalar solution and its residual. It is **not** enough to classify the kernel, to assert that every Q-R syzygy is a combination of `E_1(0)` and `E_2(0)`, or to assert module-support completeness. The firewall string `one scalar h-syzygy correction of the worst QR grade only` is the correct scope of this matrix.

---

## Charge 4 — Exact identity `F_i''=F_i'+h g_i`; `h=0` slice; Q-R vanishing; 90-term SHA

**CONFIRMED. The source forms `W_h'=sum_i (F_i'+h g_i) E_i(h)` by full polynomial add/multiply with no `h`-adic truncation. The identity is `W_h' = W_h + h*((11/6) E_1(h) - (11/12) E_2(h))` in the polynomial ring, not a congruence. Both traversals emit the same 90-term toric digest `a4d11309d1f2195a1908c5ba0c4f36935b1c2c48170e30775b8372a4bd20621d`. The `h=0` slice is the reviewed 37-term `W'`. The complete `h`-linear Q-R component is empty.**

Source: `corrected_fs[ell] = fs[ell] + g_{ell} h`, then `corrected = sum_ell corrected_fs[ell] * rows[ell]` over the same `forward`/`reverse` index list used for `W_h`. `specialize_h_zero` and `divide_h` are checks, not the construction. Fail-closed: `corrected|h=0` must equal `W_h|h=0`, and `QR(C_1'')` must be empty.

Independent reading of the 90 records:

- Toric canonical digest of all 90 terms: `a4d11309d1f2195a1908c5ba0c4f36935b1c2c48170e30775b8372a4bd20621d`. Stored `corrected_witness_sha256` matches on both hosts.
- `h`-exponent histogram `{0:37, 1:37, 2:15, 3:1}`. Maximum `h` is 3, the same as V4; the construction did not truncate, and the correction introduced no `h^4` monomial in the emitted support.
- `h=0` slice: 37 terms, dictionary-equal to the V4 `h=0` slice (empty symmetric difference, empty coefficient mismatch). V1 digest `ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b`. Stored `w0_sha256` matches. Extra toric variables are zero, so the projection to the V1 ring is literal.
- `h`-linear Q-R component: 0 terms of Q-degree 1, R-degree 1, `h=1`, and no other factor; 0 terms of that bidegree with an extra factor either. Stored `residual_qr_terms=0`.
- `h`-linear coefficient `C_1''` (the 37 terms with `h=1`, `h` decremented): toric digest `c05f2603d0137a91ea8962af46064d08fdb609e7d8c61122c5036cc515119c83`, matching stored `corrected_c1_sha256` / `corrected_c1_terms=37`.

Support comparison against V4 (`98` terms) is the exact-identity witness that this is not “delete eight coefficients of `W_h`”:

```text
only in V4 (8):  the Charge-2 Q-R monomials, coefficients unchanged from V4
only in V5 (0):  none
common (90):     84 coefficients equal, 6 coefficients changed
```

The six coefficient changes, V4 to V5:

```text
h q2^3          1/27  ->  25/81     delta  22/81
h q1 q2^2     -20/81  -> -14/27     delta -22/81
h q1^2 q2       2/27  ->  17/81     delta  11/81
h q0 q2^2       2/27  ->  17/81     delta  11/81
h r2^2         -1/9   -> -17/54     delta -11/54
h^2 q2 r2     -91/162 -> -25/162    delta  11/27
```

The last line is an `h^2` coefficient. A congruence modulo `h^2` cannot change it. Combined with dual-traversal agreement on the full 90-term digest, this is an exact polynomial identity.

Roles: one target `la^20` (coefficient `1`) and one positive split `la^20 tau` (coefficient `1`); 88 charged terms. `37+37+15+1=90`.

---

## Charge 5 — Weights on `alpha=15/2`, `beta=5+u`, `delta=5+v`; unique-target iff `eta>5`

**CONFIRMED. The new witness is uniformly unique-target on `u>0`, `v>0`, `T>0` if and only if `eta>5`. At `eta=5` the five displayed `h r^2` terms tie independently of `u,v`. All nine present `h`-linear Q-cubic corner terms have positive Q-slope. For `eta<5` an actual r-square term lies below target.**

Weight convention, matching the reviewed V4 / q2 sample after restoring `beta=5+u`, `delta=5+v` and `eta=wt(h)/L`, with `alpha` held at `15/2`:

```text
(wt - 20L)/L
  = (la-20) + (T/L) tau + (H/L) rho
    + (5+v) q2 + (5+u)(q1+q0) + (15/2)(r2+r1+r0) + eta * h.
```

The compiler records, for every monomial,

```text
c = (la-20) + 5(q1+q0) + 5 q2 + (15/2)(r2+r1+r0),
U = q1+q0,  V = q2,  E = h.
```

Integer check, all 90 difference-forms against exponents: 90/90. Integer check, all 88 charged constants: the reduced fraction of `2(la-20)+10(q0+q1+q2)+15(r0+r1+r2)` over `2` equals the stored string, and `(U,V,E)=(q0+q1, q2, h)`, 88/88. No charged term has `tau>0` or `rho>0`. The two skipped monomials are `la^20` (target) and `la^20 tau` (strictly above once `T>0`). On the 88 charged terms the recorded form is therefore exact, and `T` enters uniqueness only through the skipped `la^20 tau`.

Histogram of the 88 charged terms by recorded `c`:

```text
c      count
-15/2     9
-5       19
-5/2     14
 0       30
 5/2     11
 5        5
```

`9+19+14+30+11+5=88`. Relative to V4's 96 charged terms, the only count change is `-15/2`: `17` to `9`, equal to the eight canceled Q-R terms. Among `h=0` charged terms, 20 have `c=0` and 15 have `c>0`; zero have `c<0`. The old `W'` still does not itself break the open quadrant at this `alpha`.

The nine remaining `c=-15/2` terms all have `E>=2` (eight with `E=2`, one `-(4/81) h^3 q2 r2` with `E=3`), hence ratios `-c/E` in `{15/4, 5/2}`, both strictly less than 5.

For a term with `U,V,E >= 0`, uniqueness of least term `la^20` for all `u,v>0` at fixed `eta` holds iff every charged term satisfies either `c+E eta > 0`, or `c+E eta = 0` and `U+V > 0`. (If `c+E eta = 0` and `U=V=0`, the term ties `la^20` throughout the quadrant. If `c+E eta < 0`, the term is below target for every `u,v`, or, if `U+V>0`, for sufficiently small positive `u,v`.) Increasing `u` or `v` cannot create a new below-target term, because `U,V >= 0`.

Verified on the 88 charged records:

- `E=0` and `c<0`: **0**.
- `E=0` and `c=0`: **20**, every one with `U+V > 0`. These are the 20 old closed-corner threshold monomials of `W'`.
- `E>0` and `c<0`: **42**. The exact ratio `-c/E` is at most `5`, with equality on **exactly 14** terms, all of them `E=1`, `c=-5`. No term has `-c/E > 5`.
- At `eta=5`: **0** terms with `c+5E < 0`; **34** with equality (20 old `E=0,c=0` plus 14 new `E=1,c=-5`). Stored `threshold_face_terms` is this set of 34, key-equal to the independent classification. `eta_equal_infimum_is_strict_on_open_quadrant=false`.

The 14 maximizers of `-c/E` split as:

Five r-square terms, `U=V=0`, coefficients and monomials equal to `RESULT.md`:

```text
-17/54 h r2^2      c=-5  U=0  V=0  E=1    Δ/L = eta - 5
 +4/9  h r1 r2     c=-5  U=0  V=0  E=1    Δ/L = eta - 5
 -1/18 h r1^2      c=-5  U=0  V=0  E=1    Δ/L = eta - 5
 -1/9  h r0 r2     c=-5  U=0  V=0  E=1    Δ/L = eta - 5
 +4/27 h r0 r1     c=-5  U=0  V=0  E=1    Δ/L = eta - 5
```

There is no `h r0^2` term. These five are present (nonzero). None carries `tau` or `rho`. Their margin at `eta=5` is identically zero for every `u,v`.

Nine `h`-linear Q-cubic terms, all of Q-degree 3, R-degree 0, `U+V = 3 >= 3`:

```text
+25/81 h q2^3           U=0  V=3
-14/27 h q1 q2^2        U=1  V=2
+17/81 h q1^2 q2        U=2  V=1
 -4/81 h q1^3           U=3  V=0
+17/81 h q0 q2^2        U=1  V=2
 -8/27 h q0 q1 q2       U=2  V=1
 +1/27 h q0 q1^2        U=3  V=0
 +1/27 h q0^2 q2        U=2  V=1
 -4/81 h q0^2 q1        U=3  V=0
```

There is no `h q0^3` term. Every one of these nine has positive Q-slope in the open quadrant: at `eta=5` the margin is `U u + V v > 0` for all `u,v>0`. They reach the closed corner `u=v=0` at the same eta, and they do **not** destroy uniqueness on the open quadrant at `eta=5`. The five r-square terms do.

Hence the iff, charged on all 90 terms:

- If `eta>5`, every charged term has `c+E eta > 0` except the 20 old `c=0` terms, which have `c+E eta=0` and `U+V>0`. Unique least term `la^20` throughout the open quadrant.
- If `eta=5`, the five r-square terms satisfy `c+E eta=0` and `U=V=0`, so they tie `la^20` independently of `u,v`. Unique-target fails. The nine Q-cubics remain strictly above for `u,v>0`.
- If `0<eta<5`, each of those five r-square terms has `c+E eta = eta-5 < 0`. They are present. None carries `tau` or `rho`. They lie strictly below target for every `u,v>0`, `T>0`. The same witness cannot give a uniform exclusion on this interval.

This is the exact iff, not a statement about a displayed subset. The infimum of uniform unique-target eta is 5, and equality is not strict. Stored `eta_uniform_infimum=5` and `eta_equal_infimum_is_strict_on_open_quadrant=false` match.

---

## Charge 6 — Scope: one witness, `eta>5` only

**CONFIRMED. The licensed theorem is the Promotion paragraph. The `eta=5` face and `eta<5` are next-lift / full-face problems, not branch survivors.**

Admissible:

- For `eta>5`, this explicit scalar-corrected combination `W_h'` has unique least term `la^20` uniformly on `u>0`, `v>0`, `T>0`, at the fixed axis/cusp chart `a=1`, `p=-3`, `c=2+h`, loads `k=nu=0`, `mu=2/3`, and full `Q,R` support.
- This improves the unchanged-witness V4 range `eta>=15/2` to `eta>5` by one preregistered scalar correction of the worst Q-R graded piece.
- For `eta=5`, the same polynomial is **not** unique-target: five present `h r^2` terms tie independently of `u,v`. That equality face is the next graded correction's input, or a full-face saturation problem. It is not a surviving branch.
- For `0<eta<5`, the same polynomial has present r-square terms below target. Those cells require a further correction if they are to be charged. They are not surviving branches.

Not admissible, and not claimed by the frozen firewall strings
`one scalar h-syzygy correction of the worst QR grade only; iterate remaining low grades; no formal h-adic lift`
and `RESULT.md` §Firewall:

- scalar-support completeness of the eight-row module (the kernel of the 9-by-8 Q-R system is not classified; free columns were set to zero by convention);
- an `h`-adic lift, or any statement about coefficients of `h^2` and higher as a completed jet;
- moving axis, moving loads, or a theorem that the unit-axis map acts on the submitted rows;
- equality-support analysis of the 34 face monomials beyond their recorded weights;
- another normal direction (`p` is fixed at `-3`);
- a formal-arc / formal-lift obstruction;
- the whole double-root fan, D1, or JC2;
- a claim that V4 already settled the cusp direction below `eta=15/2` (it did not; that is this package, and only down to `eta>5`).

The reviewed q2 lift remains valid on the special fibre `h=0`. The reviewed V4 transport remains the correct classification of the *unchanged* multipliers. This package classifies only the weight behaviour of one explicit scalar-corrected witness.

---

## Nits, not defects

1. Harvest trees contain sentinels, `free.*`, `hostname`, `uname`, `nproc`, UTC stamps, and empty launch stdio, none of which are in `FREEZE.sha256`. They were used as custody, not as a second freeze. Harvest copies of source files that *are* frozen at the package top were `cmp`-identical.
2. Original 9-by-8 Q-R matrix entries are not serialized. Dual-AWS RREF, the eight `row_qr_sha256` pins (including the empty row-6 digest), the compiler's fail-closed residual check, and the V4/V5 support comparison jointly verify this free-zero solution. A later package that wants an independent reconstruction of `A` must emit the sources or the raw matrix.
3. The compiler's `eta0 = max(-c/E)` loop does not, by itself, inspect `U,V` on the threshold face. The certificate stores the 34 face monomials and the boolean `eta_equal_infimum_is_strict_on_open_quadrant=false`; this review charged both. The open-quadrant failure at `eta=5` is in the records, not only in the `max` reduction.
4. `AWS_LAUNCH_METADATA.md` records a local heavy-process audit of zero campaign-owned workers. r6d `free` shows 123 GiB used vs box03 17 GiB; swap is zero on both, and this job's RSS is 22 MiB under a 4 GiB `ulimit -v`. That is not evidence that another campaign job was stopped, and not a defect in this package.
5. V5 JSON bytes are not identical across hosts, by the preregistered `tag`/`order` fields. The algebraic payload is. That is the correct dual-encoding pattern once the certificate records its own tag.

No source or certificate repair is required.

H_QR_SYZYGY_LIFT_CONFIRMED
