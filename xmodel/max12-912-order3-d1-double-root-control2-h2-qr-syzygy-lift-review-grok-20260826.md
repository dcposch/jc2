# Hostile text-only review — control-2 h-squared Q-R filtered syzygy lift V7

| Field | Value |
|---|---|
| Claim under review | One scalar `h^2` correction of the complete Q-R piece of the reconstructed V6 witness: `F1^(7)=F1^(6)+(5/24)h^2`, `F2^(7)=F2^(6)-(2/9)h^2`, `Fi^(7)=Fi^(6)` for `i>=3`, producing a 57-term polynomial whose `h=0` and `h`-linear coefficients are the V6 slices, whose complete `h^2` Q-R component vanishes, and which is uniformly unique-target on `u,v>0`, `T>0` if and only if `eta>=5/2` |
| Overall verdict | **H2_QR_SYZYGY_LIFT_CONFIRMED**. Dual AWS encodings emit certificates that differ only in `tag` and `order`; deleting those fields gives canonical sorted SHA `788fa8de…`. The reconstructed V6 identity is the reviewed 71-term polynomial (SHA `3363e67d…`) with `h=0` slice `W'` (SHA `ddb451c4…`) and 18-term `h`-linear coefficient (SHA `6fee8f42…`). Independent extraction from the frozen V6 records recovers the complete eight-term `h^2` Q-R piece, each of closed-corner pre-`h` margin `-15/2`, SHA `1fbcb804…`. Stored RREF has rank 3, pivots `(0,1,2)`, and free-zero solution `(5/24,-2/9,0,…,0)`. The 57-term polynomial SHA `efe2ebcc…` is an exact identity: lower `h` coefficients are dictionary-equal to V6, the eight named Q-R monomials are deleted, and no new Q-R term appears. Integer arithmetic on all 57 recorded forms proves unique least term `la^20` iff `eta>=5/2`. The eight displayed `h q^2 r` endpoints have positive `u`/`v` margins at equality. `eta<5/2` is a next-lift problem, not a branch survivor |
| Smallest failing identity | none in the frozen V7 source, either harvest tree, either AWS stream, the hash-pinned V6/V5/V4 sources, the frozen V6 records, or the recorded 57-term polynomial |
| Smallest missing hypothesis for a stronger theorem | a `q`-linear multiplier correction of the `eta=5/2` face; a correction for `0<eta<5/2`; scalar-support completeness of the eight-row module; an `h`-adic / formal lift; moving axis or moving loads; another normal direction; a formal arc; the whole double-root fan; D1; or JC2 |
| Evidence tier | SHA-256 of the freeze chain and already-emitted AWS files; `cmp` of harvest copies against package-top source; `json` comparison of the two certificates after deleting `tag` and `order`; integer/rational arithmetic on every recorded `(c,U,V,E)`; V1-format digest of the `h=0` slice; toric canonical digest of the 57-term polynomial, of the 8-term `h^2` Q-R piece, and of the 2-term residual `h^2` coefficient; dictionary comparison of V6 vs V7 slices. No local Singular, Sage, msolve, gfan, Lean, Python algebra, compiler execution, charged reconstruct, or eight-row product replay |
| Reviewer / model | Grok 4.6 (xAI). Text-only tropical / commutative-algebra / CAS-custody referee |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `574e873d4753b57dbaeb0fb83e320fbef3694724` |
| Host | Darwin. V7 compiler, V6 compiler, V5 compiler, V4 compiler, V1 compiler, toric compiler, charged reconstruct, Singular, and every solver were not run |

## What was and was not run

No local substantive computation was run. In particular this review did **not** execute `compile_h2_qr_syzygy_lift_v7.py`, `compile_h_grade5_kernel_lift_v6.py`, `compile_h_qr_syzygy_lift_v5.py`, `compile_h_first_transport_v4.py`, `compile_q2_first_lift.py`, `compile_toric_blowup.py`, `independent_reconstruct.py`, Singular, Sage, msolve, Lean, Gfan, or any other solver, and it did not re-multiply `sum F_i^(7) E_i(h)` or reconstruct the unsubstituted eight rows. Hashes were checked with `shasum -a 256`. File identity was checked with `cmp`. Marker counts used `grep`. Git identity was read with `git rev-parse`. JSON fields were read with Python `json` (no algebra libraries). Canonical SHA-256 values and rational weight forms were recomputed from the already-emitted certificate records (V1 digest format for the `h=0` slice; toric canonical format `[[list(monomial), num, den], ...]` for the 8-term Q-R piece, the 2-term residual `h^2` coefficient, and the 57-term polynomial). Recorded weight forms were checked by the integer identity `2c = 2(la-20)+10(q0+q1+q2)+15(r0+r1+r2)`.

Charged freeze SHA-256, recomputed and matched:

```text
0c5ab55da33f5296cd64a82ddfb03591cc45a6b32415c402a59014af6410475b  FREEZE.sha256
a790c5015f2f7a27fc4681a4e29cf059d775d4a232e16523e0966c19f3bb8335  RESULT.md
efe2ebcc234d836763a8a47f58a228f6a90cc20fd876bb48b1144a60f3e5d6a5  corrected witness
```

Prerequisite V5 Q-R lift review, recomputed and matched:

```text
7ac62c8bd0667340aab5fcdd4d6d35b5e184536fb6e9f5c98f6c9955fdea54c7
  xmodel/max12-912-order3-d1-double-root-control2-h-qr-syzygy-lift-review-grok-20260826.md
f166e2ba9aa8e2c4715f14a4f29ed7dd4296755ed5de551de94784be3e911471
  cases/max12_912_order3_d1_double_root_control2_h_qr_syzygy_lift_v5_20260826/FREEZE.sha256
```

Prerequisite V4 transport freeze, recomputed and matched:

```text
0ff05368ab7a5751617db6a6b9a31e67545439ed5fb688cb15238ef879637b68  FREEZE.sha256
```

V6 identity, charged from frozen V6 source and dual-AWS records (no V6 referee report exists yet; conclusions below are not inherited):

```text
c7d9faed50b93cb7bb3905d8d386d2dc0f670c300baeefa78864d5dd3097dfce
  compile_h_grade5_kernel_lift_v6.py
3363e67da50c953ab37b4c67dc5dfeb77d3cfdf75e31b5d6f97dd87dafc7f833
  71-term V6 witness (records digest)
6fee8f428caa5364b3390a4c835c2a47214e91e2f8d6d6709137f3c428d0d5e3
  V6 18-term h-linear coefficient
```

Every path listed in `FREEZE.sha256` recomputed and matched (23/23). Nested `SOURCE_CLOSURE.sha256` (10/10) and both harvested `result.sha256` manifests (5/5 each) matched from the case root / harvest directory as appropriate. Empty compiler stderr files are the empty-string digest `e3b0c442…`. Both rc files are the two-byte string `"0\n"`, digest `9a271f2a…`.

Read in full before the verdict: every file at
`cases/max12_912_order3_d1_double_root_control2_h2_qr_syzygy_lift_v7_20260826/`
including both harvest trees; the hash-pinned V6 compiler `G1` / `grade5_component`; the hash-pinned V5 compiler `qr_component` / `exact_rref` / `analyze_threshold`; the hash-pinned V4 `coefficient_images` / multipliers; the hash-pinned toric `NAMES` / `canonical` / `digest`; V1 `multipliers` / `digest`; the frozen V6 71-term records far enough to extract the `h^2` Q-R piece and to compare lower-`h` slices; and the V5 review named above. Predecessor conclusions were recomputed, not inherited.

---

## Promotion

**Accept `FOR THE PINNED ORDINARY-TAIL EIGHT-ROW MODULE AT a=1, p=-3, c=2+h, k=nu=0, mu=2/3, FULL Q AND R, STARTING FROM THE V6 SCALAR-h CORRECTED MULTIPLIERS F_i^(6)=F_i'+h g_i WITH (g1,...,g8)=(5/2,-25/18,0,1/4,-1/3,0,0,0), THE REGISTERED DUAL-AWS V7 RUNS EMIT ONE 57-TERM POLYNOMIAL W^(7)=SUM_i F_i^(7) E_i(h) WITH F1^(7)=F1^(6)+(5/24)h^2, F2^(7)=F2^(6)-(2/9)h^2, Fi^(7)=Fi^(6) (i>=3). THIS IS AN EXACT POLYNOMIAL IDENTITY, NOT A CONGRUENCE. ITS h=0 SPECIALIZATION IS THE REVIEWED 37-TERM W' (SHA ddb451c4…). ITS COMPLETE h-LINEAR COEFFICIENT IS THE V6 18-TERM SLICE (SHA 6fee8f42…), WITH VANISHING Q-R AND R-SQUARE/Q-CUBIC PIECES. ITS COMPLETE h-SQUARED Q-R COMPONENT IS ZERO. NORMALIZE wt(la)=L, PUT alpha=15/2, beta=5+u, delta=5+v, eta=wt(h)/L, AND RESTRICT TO u>0, v>0, T>0. THEN W^(7) HAS UNIQUE LEAST-WEIGHT TERM la^20 FOR EVERY SUCH (u,v,T) IF AND ONLY IF eta>=5/2. AT eta=5/2 EVERY CLOSED-CORNER EQUALITY IS STRICT IN THE OPEN QUADRANT: THE EIGHT PRESENT h q^2 r TERMS EACH CARRY A POSITIVE COMBINATION OF u AND v. FOR EVERY 0<eta<5/2 SOME ACTUAL DISPLAYED TERM FALLS BELOW TARGET FOR SUFFICIENTLY SMALL POSITIVE u OR v. THIS IMPROVES THE V6 RANGE eta>=15/4 TO eta>=5/2. THE eta<5/2 CELL IS A NEXT q-LINEAR MULTIPLIER PROBLEM, NOT A BRANCH SURVIVOR.`**

Do not promote this to: completeness of the next polynomial-multiplier support; a classification of `eta<5/2`; an `h`-adic or formal lift; a moving-axis or moving-load theorem; equality-support analysis of the 28-term face beyond the recorded weights; another normal direction; a formal-arc obstruction; a whole double-root fan; D1; or JC2.

---

## Charge 1 — Custody, freeze, dual AWS, source closure, JSON difference

**CONFIRMED. Every freeze entry recomputes. Both registered workers are fail-closed, hash-gated, empty-stderr, sub-cap, pre-GO, and source-closed against the package-root manifest. Opposite traversal orders return certificates that differ only in `tag` and `order`; deleting those two fields gives literally identical sorted JSON of SHA `788fa8defdca08edf0cad5f42fb85f2193dd1bc994af19e054e28395c20c8bf1`.**

Required anchors, recomputed:

```text
a790c5015f2f7a27fc4681a4e29cf059d775d4a232e16523e0966c19f3bb8335  RESULT.md
0c5ab55da33f5296cd64a82ddfb03591cc45a6b32415c402a59014af6410475b  FREEZE.sha256
b2447171490a4b3cd4988bd0be4f603ac94d2bbb23725d7b9a1b36ec8597b296  aws_box03_forward/h2_qr_lift.json
fc80079508a69d76ebb6ca0adb2c9c7217a59eb2c0401a02123287eabe07d838  aws_r6d_reverse/h2_qr_lift.json
efe2ebcc234d836763a8a47f58a228f6a90cc20fd876bb48b1144a60f3e5d6a5  corrected_witness_sha256 (both JSON payloads)
```

Recomputed `FREEZE.sha256` entries, all matched:

```text
a790c5015f2f7a27fc4681a4e29cf059d775d4a232e16523e0966c19f3bb8335  RESULT.md
4ceaee0e0a89c67ae6a882cc5eaa570732bc94844bd1051106399b0b69b76494  PREREGISTRATION.md
7a53b05c9ede6ac83f8c7693912944138e7023bf3e8e4daba40136d307479308  AWS_REGISTRATION.md
bf9dd5b5b45e3a073c0167795b4b6f39b14b68a3b6fb6666a1cafe8ba0fecb31  AWS_LAUNCH_METADATA.md
e0fe9bfddcdf3e9207533419bcc5ee5aba78a594f9b4bfb041d3be209b8a08fd  SOURCE_CLOSURE.sha256
a4500936c83c82ef12d68c145ef6672688d401292c05dab36b95002df4138de3  compile_h2_qr_syzygy_lift_v7.py
43c0206f9ca5e8ba5edc0dda1399cd5b108553ebded822850a974072aac3b340  remote_worker.sh
b2447171490a4b3cd4988bd0be4f603ac94d2bbb23725d7b9a1b36ec8597b296  aws_box03_forward/h2_qr_lift.json
625bb8688f340c11ca3a93d1d07dc81c20a04712582d2c330ac8790eea4e482c  aws_box03_forward/compiler.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_box03_forward/compiler.stderr
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  aws_box03_forward/compiler.rc
7049c1623c037afc8e7cfebda11aeb5bfbc0c7a8fb98068a9f5169785bad7292  aws_box03_forward/compiler.time
69335376981badf1e4a06e79692038f80d02bd30d134e1002d2fb3f7f2366f3a  aws_box03_forward/result.sha256
75c44a72a28feb03ee4829fd0fa0f0e554e06b6aef60a253f449e22918d80f1f  aws_box03_forward/source.check
73294ec5080138e135b028524c285472c6ca143939f25cf3ec96800c3202dbcc  aws_box03_forward/worker.metadata
fc80079508a69d76ebb6ca0adb2c9c7217a59eb2c0401a02123287eabe07d838  aws_r6d_reverse/h2_qr_lift.json
9e44e2765be88a206a10dfac38d4fce2ad9c8ba371c55040c8f867d49dd3202f  aws_r6d_reverse/compiler.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_reverse/compiler.stderr
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  aws_r6d_reverse/compiler.rc
eb12240099a92955723e143119cb194299489ac0322b03e2c4dee1cf15f6d792  aws_r6d_reverse/compiler.time
139d2313df8dbc97e260c918dadc8e45ff1adaf8eda886caa7f44c7fd475ff7e  aws_r6d_reverse/result.sha256
75c44a72a28feb03ee4829fd0fa0f0e554e06b6aef60a253f449e22918d80f1f  aws_r6d_reverse/source.check
6f5f5f51f43c1ad072514eebfab89c96ba87971ee888b5845b705757360b6b7a  aws_r6d_reverse/worker.metadata
```

Source-closure entries, all matched from the package root:

```text
4ceaee0e0a89c67ae6a882cc5eaa570732bc94844bd1051106399b0b69b76494  PREREGISTRATION.md
7a53b05c9ede6ac83f8c7693912944138e7023bf3e8e4daba40136d307479308  AWS_REGISTRATION.md
a4500936c83c82ef12d68c145ef6672688d401292c05dab36b95002df4138de3  compile_h2_qr_syzygy_lift_v7.py
43c0206f9ca5e8ba5edc0dda1399cd5b108553ebded822850a974072aac3b340  remote_worker.sh
c7d9faed50b93cb7bb3905d8d386d2dc0f670c300baeefa78864d5dd3097dfce  ../max12_912_order3_d1_double_root_control2_h_grade5_kernel_lift_v6_20260826/compile_h_grade5_kernel_lift_v6.py
8a963360f16a29c6841050f82e9eb79051005d821c6ec7837d0614ca8ead7366  ../max12_912_order3_d1_double_root_control2_h_qr_syzygy_lift_v5_20260826/compile_h_qr_syzygy_lift_v5.py
3bbf1ebfb9f8b15054fe2f592bea92d8e07b95bce4d6ca131cd81c95f3698306  ../max12_912_order3_d1_double_root_control2_h_first_transport_v4_20260826/compile_h_first_transport_v4.py
c76ef85ac14f81839674368c55a324499832e6cf4b589befa68baf93a42b1490  ../max12_912_order3_d1_double_root_toric_blowup_20260825/compile_toric_blowup.py
0385b0b1e60b3bd37fa5fbee90dd6c17a454722bdbff424ea83c2ab0fa19df45  ../max12_912_order3_d1_double_root_control2_q2_first_lift_v1_20260826/compile_q2_first_lift.py
67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623  ../max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/independent_reconstruct.py
```

Harvested `SOURCE_CLOSURE.sha256` is byte-identical to the top copy on both hosts. Both `source.check` files are identical (`75c44a72…`) and print `OK` on those ten paths. The worker `cd`s to `$run` before `sha256sum -c SOURCE_CLOSURE.sha256`. The compiler locates V6/V5/V4 via `HERE.parents[1]/cases/…`, so `$run` is a `cases/`-child (the package, or a copy sitting as a `cases/` neighbour). Dual AWS both passed the sibling-path hash check. Treating `aws_box03_forward/` or `aws_r6d_reverse/` as a new source root would make those siblings invisible. That is not the charged root.

The compiler pins V6 at `V6_SHA=c7d9faed…` and refuses a non-matching file before import. V6 re-pins V5 at `8a963360…`; V5 re-pins V4 at `3bbf1ebf…`; V4 re-pins toric `c76ef85a…`, V1 `0385b0b1…`, and `independent_reconstruct.py` at `67343b56…`. Tag gates: worker `case` requires prefix `max12_912_order3_d1_double_root_control2_h2_qr_syzygy_lift_v7_20260826T*`; compiler `require_aws` requires Linux, DMI vendor `Amazon EC2`, and tag prefix `max12_912_order3_d1_double_root_control2_h2_qr_syzygy_lift_v7_`. Both refuse non-`forward`/`reverse` orders.

| Check | Box03 forward | r6d reverse |
|---|---|---|
| Public IP / harvested hostname | `98.80.65.144` / `ip-172-30-0-249` | `100.26.198.153` / `ip-172-30-0-45` |
| Tag | `…_v7_20260826T041700Z_box03_forward` | `…_v7_20260826T041700Z_r6d_reverse` |
| Worker PID | `156418` | `223926` |
| Caps | `memory_kib=4194304`, `timeout=900`, `nice -n 10`; `ulimit -v 4194304` | same |
| Order | `forward` (`ell=1..8`) | `reverse` (`ell=8..1`) |
| Started / finished UTC | `2026-08-26T04:18:20Z` / `04:19:00Z` | `04:18:21Z` / `04:19:01Z` |
| Compiler stdout SHA | `625bb868…` | `9e44e276…` |
| Certificate SHA | `b2447171…` | `fc800795…` |
| RSS / swap / exit | 21980 KiB / `Swaps: 0` / 0 | 22104 KiB / `Swaps: 0` / 0 |
| Pre/post `free` swap | `0B` / `0B` | `0B` / `0B` |
| Elapsed | 6.04 s | 5.89 s |
| PASS markers, each once | `PASS_H2_QR_SYZYGY_LIFT_V7_SOLVABLE`, `PASS_REMOTE_WORKER` | same |
| `FAIL_` / `REFUSED` / `FAILED` | none; stderr empty | none; stderr empty |

`AWS_LAUNCH_METADATA.md` mtime is `2026-08-26T04:18:35Z`, after worker start (`04:18:20Z` / `04:18:21Z`) and before GO (`04:18:54Z` / `04:18:55Z`). Content: both workers `WAITING_GO`; “Neither directory contained GO”; source-closure manifest SHA `e0fe9bfd…` matching the frozen file. GO sentinels exist and are empty. DONE mtimes match finish (`04:19:00Z` / `04:19:01Z`). No `REFUSED` or `FAILED`. The 6-second GO-to-DONE window matches the 6.04 s compile plus the post-GO source-hash check.

Harvest copies of compiler, worker, preregistration, AWS registration, and source closure are byte-identical to the package top on both hosts (`cmp`). The two JSON files are **not** byte-identical (68813 vs 68811 bytes; the 2-byte gap is `box03_forward` vs `r6d_reverse` in the tag). Their key sets are equal. The only value differences are the two preregistered custody fields `tag` and `order`. Deleting those fields and dumping with `sort_keys=True, indent=2` plus a trailing newline yields one 68686-byte blob of SHA

```text
788fa8defdca08edf0cad5f42fb85f2193dd1bc994af19e054e28395c20c8bf1
```

on both hosts, matching `RESULT.md` and the charged semantic-equality SHA. Compiler stdout differs only in the preregistered `ORDER=` line and the certificate SHA of the tagged JSON; the algebraic metric block is identical:

```text
STATUS=SOLVABLE
H2_SOLUTION=5/24,-2/9,0,0,0,0,0,0
CORRECTED_WITNESS_SHA256=efe2ebcc234d836763a8a47f58a228f6a90cc20fd876bb48b1144a60f3e5d6a5
ETA_UNIFORM_INFIMUM=5/2
ETA_EQUAL_OPEN_STRICT=1
PASS_H2_QR_SYZYGY_LIFT_V7_SOLVABLE
```

Every extra toric variable `p,c,a,x,y,k,mu,nu` is zero on all 57 recorded terms. Support is exactly `{h,la,tau,q2,q1,q0,r2,r1,r0}`.

---

## Charge 2 — Exact reconstruction of the V6 71-term identity; `h=0` and `h`-linear coefficients before extracting `h^2`

**CONFIRMED. The V7 source reconstructs `W_V6=sum_i (F_i'+h g_i) E_i(h)` from the frozen ordinary rows and the hardcoded scalar-`h` correction `G1=(5/2,-25/18,0,1/4,-1/3,0,0,0)`. Dual AWS both fail-close on the V6 71-term digest `3363e67d…`, the reviewed `h=0` digest `ddb451c4…`, the V6 `h`-linear digest `6fee8f42…`, and vanishing of the `h`-linear Q-R and R-square/Q-cubic pieces. Independent reading of the frozen V6 records recovers those three hashes and that vanishing, and matches `G1` as V6's emitted full scalar-`h` correction.**

Construction, from the hash-pinned V7 compiler, which loads the hash-pinned V6 compiler, which loads the hash-pinned V5/V4/toric/V1 chain:

1. `t.load_charged_source().build()["tails"]` is the eight negative Laurent tails of `independent_reconstruct.py` at `67343b56…`, in names `(a0..a7,k)`. Same charged ordinary-tail source as the reviewed V5 lift and V4 transport.
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

3. Substitute tails; subtract row-3 target `(2/3) la^15` and row-8 target `la^20(1+tau)`; no row-6 `nu` subtraction. Multipliers from V1 with `F1+=q2/12`, `F2+=-q2/9`, then the V6 scalar-`h` correction `F_i^(6)=embed(F_i')+g_i h` with the hardcoded `G1` above.
4. `w6 = sum_ell F_ell^(6) E_ell(h)` over the same `forward`/`reverse` index list. Fail-closed, in this order, before any `h^2` extraction:

```text
digest(project_base(w6|_{h=0})) = ddb451c4…          # reviewed W'
digest(w6)                       = 3363e67d…          # V6 71-term identity
digest([h^1] w6)                 = 6fee8f42…          # V6 h-linear coefficient
qr_component([h^1] w6)           = 0
grade5_component([h^1] w6)       = 0
```

`G1` is the V6 certificate field `full_scalar_h_correction` and the V6 `RESULT.md` vector `(g1,...,g8)`. V7 does not read the V6 JSON; it reconstructs from frozen source plus this pin, then refuses any other 71-term polynomial.

Independent reading of the frozen V6 71 records (not a compiler replay):

- Toric digest of all 71 terms: `3363e67da50c953ab37b4c67dc5dfeb77d3cfdf75e31b5d6f97dd87dafc7f833`. Stored V6 `corrected_witness_sha256` and V7 `w6_sha256` match.
- `h`-exponent histogram `{0:37, 1:18, 2:15, 3:1}`. Maximum `h` is 3; no `h^4`.
- `h=0` slice: 37 terms, dictionary-equal to the reviewed V4 `h=0` slice (empty symmetric difference, empty coefficient mismatch). V1 digest `ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b`. Extra toric variables are zero, so the projection to the V1 ring is literal.
- `h`-linear coefficient: 18 terms, toric digest `6fee8f428caa5364b3390a4c835c2a47214e91e2f8d6d6709137f3c428d0d5e3`. Among those 18, zero terms have Q-degree 1 and R-degree 1; zero have `(q,r)` in `{(0,2),(3,0)}`. The V6 Q-R and grade-5 cancellations are present in the records.

Dual AWS of V7 both exited 0 after those four fail-closed checks, opposite traversal. That is the custody that V7 reconstructed the V6 identity rather than loading a stale certificate. This review did not replay the eight-row product.

---

## Charge 3 — Eight-term `h^2` Q-R component, rank-three row map, RREF/pivots, solution `(5/24,-2/9,0,...,0)`, exact 57-term identity

**CONFIRMED for the preregistered scalar `h^2` correction. The complete Q-R piece of `[h^2]W_V6` is exactly eight monomials, each of closed-corner pre-`h` margin `-15/2`, SHA `1fbcb804…`. Stored RREF of the 9-by-8 system has rank 3 and pivots `(0,1,2)`. The canonical free-zero solution is `(5/24,-2/9,0,0,0,0,0,0)`. Adding `h^2 d_i` preserves every lower-`h` coefficient and cancels the entire named component. The 57-term polynomial SHA `efe2ebcc…` is an exact identity: V7 is V6 minus fourteen monomials, with no coefficient change on the surviving 57.**

The linear system, from the hash-pinned compiler, is

```text
sum_{i=1..8} d_i * QR(E_i(0)) = -QR([h^2] W_V6)
```

over `Q`, with exact RREF and free columns set to zero. `qr_component` keeps a monomial iff `q2+q1+q0=1`, `r2+r1+r0=1`, and every other exponent is zero. Fail-closed: that piece must have eight terms, each of closed-corner value `(la-20)+5(q-sum)+(15/2)(r-sum)=-15/2`.

Independent extraction from the frozen V6 records (15 terms with `h=2`). Among those 15, the Q-degree 1, R-degree 1, no-other-factor subset is exactly eight; there is no `h^2` Q-R term with an extra factor, and there is no `h^2 q0 r0` term. Coefficients and monomials, `h` restored:

```text
-77/162 h^2 q2 r2     c = -15/2
 +8/27  h^2 q2 r1     c = -15/2
 -5/54  h^2 q2 r0     c = -15/2
 +8/27  h^2 q1 r2     c = -15/2
 -5/54  h^2 q1 r1     c = -15/2
 +8/81  h^2 q1 r0     c = -15/2
 -5/54  h^2 q0 r2     c = -15/2
 +8/81  h^2 q0 r1     c = -15/2
```

Stripping the `h^2` factor recovers V7 `h2_qr_terms` as an equal list of toric canonical triples. Recomputed digest `1fbcb8047679987fba12aa681546dfd0bb27134d4e03d08efee6e5742417c275`, matching V7 `h2_qr_sha256`, both JSON payloads, and `RESULT.md`. These are the same eight V6 extremals at eta-infimum `15/4` (`E=2`, `-c/E=15/4`).

`graded_monomials` is the complete 9-element set of bilinear Q-R monomials, sorted as

```text
q0 r0, q0 r1, q0 r2, q1 r0, q1 r1, q1 r2, q2 r0, q2 r1, q2 r2.
```

Target `QR([h^2]W_V6)` is supported on the last eight of these (`q0 r0` coefficient 0). The emitted augmented RREF is 9-by-9:

```text
[ 1  0  0  -4/3   1    0  -10/9   4/3  |  5/24 ]
[ 0  1  0   1    -2/3  0   2/3   -7/9  | -2/9  ]
[ 0  0  1   0     0    0   0      0    |   0    ]
[ 0  0  0   0     0    0   0      0    |   0    ]
  ... five further zero rows ...
```

Pivots, 0-based: columns `0,1,2` (`d1,d2,d3`). Rank 3. Free columns `3,4,5,6,7` (`d4..d8`). The left eight columns are byte-equal, as strings, to the reviewed V5 Q-R RREF; only the last column changed, as required for a new target against the same source matrix. Independently, `row_qr_sha256` is byte-equal to V5's eight source digests. Column 5 (`d6`) is identically zero in RREF; independently, `row_qr_sha256[5]` is the empty-polynomial digest `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945` (`sha256(b"[]")`), so `QR(E_6(0))=0`. Pivot row 2 forces `d3=0`. Setting the five free variables to zero reads

```text
d1 = 5/24,  d2 = -2/9,  d3 = ... = d8 = 0.
```

This is the stored `solution` and the stored `solution_sha256` `cf58253f4850c178a5f05f33116980a5d999c56c4849af5cf7c89f39332fa280` (recomputed from `json.dumps(solution, separators=(",",":"))`). Substituting that vector into every RREF row recovers the last column exactly (9/9). Signs and numbering: compiler does `F_ell^(7) = F_ell^(6) + d_ell h^2` with `ell=1..8`, so

```text
F1^(7) = F1^(6) + (5/24) h^2,
F2^(7) = F2^(6) - (2/9) h^2,
Fi^(7) = Fi^(6)  (i>=3),
```

matching `RESULT.md`. Dual AWS, opposite traversal, emit this same RREF and same solution. The five free-column kernel vectors of this RREF are exactly the V6 published Q-R kernel

```text
( 4/3,-1,0,1,0,0,0,0),
(-1,  2/3,0,0,1,0,0,0),
( 0,  0,0,0,0,1,0,0),
(10/9,-2/3,0,0,0,0,1,0),
(-4/3,7/9,0,0,0,0,0,1),
```

which is the expected kernel of an unchanged source matrix.

Literal residual. Two independent readings, neither of which reconstructs original `A` locally:

1. Compiler fail-closed: after RREF it forms `sum d_i QR(E_i(0))` and refuses unless that equals `-QR([h^2]W_V6)`; then it forms the full product `sum F_i^(7) E_i(h)` and refuses unless `[h^0]` and `[h^1]` equal the V6 slices and `QR([h^2] W^(7))` is empty. Dual AWS both exited 0.
2. Support comparison of the already-emitted polynomials, which does not require `A`. V6 contains exactly the eight `h^2` Q-R monomials of this charge and no other `h^2` Q-R monomial (including no `h^2 q0 r0`). V7 contains none of those eight, no new monomial of any kind, and in particular no `h^2 q0 r0`. Therefore the Q-R component of `[h^2]W^(7)` is the zero polynomial on all nine bilinear monomials. Certificate field `residual_h2_qr_terms=0` matches.

Lower-`h` preservation, dictionary-level, V6 records vs V7 records:

```text
h=0:  37 vs 37, keys equal, coefficient mismatch 0
h=1:  18 vs 18, keys equal, coefficient mismatch 0
```

The V7 `h=0` slice is additionally dictionary-equal to the reviewed V4 37-term `W'` (V1 digest `ddb451c4…`). The V7 `h`-linear slice has toric digest `6fee8f42…` matching V6; among its 18 terms, zero are Q-R and zero are R-square/Q-cubic.

Exact identity vs V6, full support:

```text
only in V6 (14):  the eight Charge-3 Q-R monomials, plus
                    -16/243 h^2 q2^3,
                    +5/162  h^2 q1 q2^2,
                    -8/243  h^2 q1^2 q2,
                    -8/243  h^2 q0 q2^2,
                    +4/81   h^2 r2^2,
                    -8/81   h^3 q2 r2
only in V7 (0):   none
common (57):      57 coefficients equal, 0 coefficients changed
```

V7 is V6 with those fourteen monomials deleted. A congruence modulo `h^3` cannot delete the `h^3` term. Combined with dual-traversal agreement on the full 57-term digest, this is an exact polynomial identity `W^(7)=sum_i (F_i^(6)+d_i h^2) E_i(h)`, not a filtered truncation of `W_V6`. The six non-Q-R deletions are collateral from `E_i(h)` having more than the Q-R piece at `h=0` and from `h`-positive pieces of the rows; they are not a defect in the named cancellation.

Recomputed toric digest of all 57 V7 records: `efe2ebcc234d836763a8a47f58a228f6a90cc20fd876bb48b1144a60f3e5d6a5`. Stored `corrected_witness_sha256` matches on both hosts and is the charged corrected-witness SHA. Residual `[h^2]` has two terms, SHA `d5ae76fe9b6ab90e9b40f94d639869685703ce9037bb9ff0c16a4d952b26c81c`, matching `corrected_c2_sha256` / `corrected_c2_terms=2`. Those two survivors, already present in V6 with the same coefficients, are not Q-R:

```text
-1/486 h^2 q1 q2^3      c=0     E=2
-1/162 h^2 q0 q2 r2     c=-5/2  E=2
```

`h`-exponent histogram of V7: `{0:37, 1:18, 2:2}`. Maximum `h` is 2; the V6 `h^3` term is gone and no `h^4` appears. Roles: one target `la^20` (coefficient `1`) and one positive split `la^20 tau` (coefficient `1`); 55 charged terms. `37+18+2=57`.

Original 9-by-8 entries are not a frozen array; only RREF, the eight source digests, and the two polynomials are frozen. That is the same custody pattern as V5. It is enough to verify this preregistered free-zero scalar solution and its residual. It is **not** enough to classify the kernel as a theorem of this package, to assert that every Q-R syzygy is a combination of `E_1(0)` and `E_2(0)`, or to assert module-support completeness. The firewall string `one scalar h2 QR correction; iterate remaining grades` is the correct scope of this matrix.

---

## Charge 4 — All 57 weight forms; unique-target iff `eta>=5/2`; eight `h q^2 r` endpoints; converse

**CONFIRMED. The new witness is uniformly unique-target on `u>0`, `v>0`, `T>0` if and only if `eta>=5/2`. At `eta=5/2` the eight displayed `h q^2 r` terms reach the closed corner and every one has a positive combination of `u` and `v`. For `eta<5/2` an actual displayed term lies below target for sufficiently small positive `u` or `v`.**

Weight convention, matching the reviewed V5 / V4 / q2 sample after restoring `beta=5+u`, `delta=5+v` and `eta=wt(h)/L`, with `alpha` held at `15/2`:

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

Integer check, all 57 difference-forms against exponents: 57/57. Integer check, all 55 charged constants: the reduced fraction of `2(la-20)+10(q0+q1+q2)+15(r0+r1+r2)` over `2` equals the stored string, and `(U,V,E)=(q0+q1, q2, h)`, 55/55. No charged term has `tau>0` or `rho>0`. No charged term has `U<0`, `V<0`, or `E<0`. The two skipped monomials are `la^20` (target) and `la^20 tau` (strictly above once `T>0`). On the 55 charged terms the recorded form is therefore exact, and `T` enters uniqueness only through the skipped `la^20 tau`.

Histogram of the 55 charged terms by recorded `c`, split by `h`:

```text
c       count    h=0    h=1    h=2
-5/2       9      0      8      1
 0        30     20      9      1
 5/2      11     10      1      0
 5         5      5      0      0
```

`9+30+11+5=55`. Relative to V6, the eight `c=-15/2` `h^2` Q-R terms are gone (they were the V6 maximizers of `-c/E`). Among `h=0` charged terms, 20 have `c=0` and 15 have `c>0` (`10` at `5/2`, `5` at `5`); zero have `c<0`. The old `W'` still does not itself break the open quadrant at this `alpha`.

For a term with `U,V,E >= 0`, uniqueness of least term `la^20` for all `u,v>0` at fixed `eta` holds iff every charged term satisfies either `c+E eta > 0`, or `c+E eta = 0` and `U+V > 0`. (If `c+E eta = 0` and `U=V=0`, the term ties `la^20` throughout the quadrant. If `c+E eta < 0`, sufficiently small positive `u,v` put it below target.) Increasing `u` or `v` cannot create a new below-target term, because `U,V >= 0`.

Verified on the 55 charged records:

- `E=0` and `c<0`: **0**.
- `E=0` and `c=0`: **20**, every one with `U+V > 0` (in fact `U+V in {1,2,3,4}`). These are the 20 old closed-corner threshold monomials of `W'`.
- `E=0` and `c>0`: **15**, strictly above even at the closed corner, for every `eta`.
- `E>0` and `c<0`: **9**. The exact ratio `-c/E` is at most `5/2`, with equality on **exactly 8** terms, all of them `E=1`, `c=-5/2`. No term has `-c/E > 5/2`. The ninth is `-1/162 h^2 q0 q2 r2` with `E=2`, ratio `5/4`.
- At `eta=5/2`: **0** terms with `c+(5/2)E < 0`; **28** with equality (20 old `E=0,c=0` plus 8 new `E=1,c=-5/2`). **0** of those 28 have `U=V=0`. Stored `threshold_face_terms` is this set of 28, key-equal to the independent classification. `eta_equal_infimum_is_strict_on_open_quadrant=true`.

The eight maximizers of `-c/E` are present with coefficients and monomials equal to `RESULT.md`:

```text
 +1/27  h q1 q2 r2     c=-5/2  U=1  V=1  E=1    Δ/L = eta - 5/2 + u + v
 +1/81  h q1 q2 r0     c=-5/2  U=1  V=1  E=1    Δ/L = eta - 5/2 + u + v
 +1/81  h q1^2 r1      c=-5/2  U=2  V=0  E=1    Δ/L = eta - 5/2 + 2u
 -1/81  h q0 q2 r2     c=-5/2  U=1  V=1  E=1    Δ/L = eta - 5/2 + u + v
 +1/54  h q0 q2 r1     c=-5/2  U=1  V=1  E=1    Δ/L = eta - 5/2 + u + v
 +5/162 h q0 q1 r2     c=-5/2  U=2  V=0  E=1    Δ/L = eta - 5/2 + 2u
 +1/162 h q0 q1 r0     c=-5/2  U=2  V=0  E=1    Δ/L = eta - 5/2 + 2u
 +1/162 h q0^2 r1      c=-5/2  U=2  V=0  E=1    Δ/L = eta - 5/2 + 2u
```

Every one has Q-degree 2 and R-degree 1. Every one has `U+V in {2}` and no `tau` or `rho`. At `eta=5/2` the first, second, fourth, and fifth have margin `u+v`; the other four have margin `2u`. On the closed corner `u=v=0` they tie the target; throughout the open quadrant the inequality is strict.

The leftover `c=-5/2` term `-1/162 h^2 q0 q2 r2` has `E=2`, hence at `eta=5/2` sits strictly above by `5/2`. The leftover `c=0` `h^2` term `-1/486 h^2 q1 q2^3` sits above by `5`.

Hence the iff, charged on all 57 terms:

- If `eta > 5/2`, every charged term has `c+E eta > 0` except the 20 old `c=0` terms, which have `c+E eta=0` and `U+V>0`. Unique least term `la^20` throughout the open quadrant.
- If `eta = 5/2`, the same, with the eight new `h q^2 r` terms now on the threshold face; each has margin `U u + V v` with `U+V=2`, so equality at `u=v=0` is strict for `u,v>0`.
- If `0 < eta < 5/2`, each of those eight terms has `c+E eta < 0`. They are present (nonzero coefficients). None carries `tau` or `rho`. Choosing the relevant `u` or `v` in `(0, 5/2-eta)` (and the other coordinate any positive number) puts that term strictly below target.

This is the exact iff, not a statement about a displayed subset. The infimum of uniform unique-target eta is `5/2`, and equality is strict on the open quadrant. Stored `eta_uniform_infimum=5/2` and `eta_equal_infimum_is_strict_on_open_quadrant=true` match.

The 20 old threshold monomials (`c=0`, `E=0`; all `h=0` pieces of reviewed `W'` that tie at the closed corner) are the same twenty already charged in V4/V5:

```text
q2 r2^2, q2 r1 r2, q2 r1^2, q2 r0 r2, q2 r0 r1, q2^4,
q1 r1 r2, q1 r1^2, q1 r0 r2, q1 r0^2, q1 q2^3, q1^2 q2^2, q1^3 q2,
q0 r0 r1, q0 q2^3, q0 q1 q2^2, q0 q1^2 q2, q0^2 q2^2, q0^2 q1 q2, q0^3 q1.
```

Converse, as a present-term argument: fix `0<eta<5/2`. The term `+(1/27) h q1 q2 r2` is present. It has no `tau` and no `rho`. Choose `0 < u,v` with `u+v < 5/2-eta`. Then `Δ/L = eta-5/2+u+v < 0`, so this term lies below target. The same works with any of the eight, using `2u` in place of `u+v` on the four `V=0` terms. No smaller positive eta therefore gives a uniform open-quadrant conclusion from this scalar-`h^2` witness.

The next wall is exactly these eight `h q^2 r` monomials. Canceling them with a scalar `h`-linear correction is impossible: they have Q-degree 2. The next filtered system, as `RESULT.md` states and as this review does not charge, has candidate columns `h q_j E_i(0)` and this eight-term target. That system is open.

---

## Charge 5 — Scope: scalar `h^2` correction only

**CONFIRMED. The licensed theorem is the Promotion paragraph. The next `q`-linear multiplier support, `eta<5/2`, `h`-adic/formal lift, moving source/load, fan, D1, and JC2 remain open.**

Admissible:

- For `eta>=5/2`, this explicit scalar-`h^2`-corrected combination `W^(7)` has unique least term `la^20` uniformly on `u>0`, `v>0`, `T>0`, at the fixed axis/cusp chart `a=1`, `p=-3`, `c=2+h`, loads `k=nu=0`, `mu=2/3`, and full `Q,R` support.
- This improves the V6 range `eta>=15/4` to `eta>=5/2` by one preregistered scalar `h^2` correction of the complete Q-R graded piece of `[h^2]W_V6`.
- For `0<eta<5/2`, the same polynomial does **not** transport uniformly. Eight present `h q^2 r` terms fall below target for sufficiently small positive `u` or `v`. Those cells require a `q`-linear (not scalar) multiplier correction if they are to be charged. They are not surviving branches.

Not admissible, and not claimed by the frozen firewall string
`one scalar h2 QR correction; iterate remaining grades`
and `RESULT.md` §Firewall:

- completeness of the next polynomial-multiplier support (24 candidate columns `h q_j E_i(0)` are named as next work, not as a solved system);
- a classification of `eta<5/2`, or a newly corrected witness on that interval;
- an `h`-adic or formal lift, or any statement about coefficients of `h^3` and higher as a completed jet;
- moving axis, moving loads, or a theorem that the unit-axis map acts on the submitted rows;
- equality-support analysis of the 28 face monomials beyond their recorded weights;
- another normal direction (`p` is fixed at `-3`);
- a formal-arc / formal-lift obstruction;
- the whole double-root fan, D1, or JC2;
- a claim that V4/V5/V6 already settled the `h^2` Q-R cell (they did not; that is this package).

The reviewed V5 lift remains valid as a scalar-`h` Q-R correction of `C_1`. The V6 identity remains the 71-term input of this package. This package classifies only the weight behaviour of one explicit scalar-`h^2` correction of that input.

---

## Nits, not defects

1. Harvest trees contain sentinels, `free.*`, `hostname`, `uname`, `nproc`, UTC stamps, and empty launch stdio, none of which are in `FREEZE.sha256`. They were used as custody, not as a second freeze. Harvest copies of source files that *are* frozen at the package top were `cmp`-identical.
2. `AWS_LAUNCH_METADATA.md` is thinner than the V4/V5 metadata: it does not restate that `$run` is the package under the job root's `cases/`. The compiler's `HERE.parents[1]/cases/…` resolution, the harvested `source.check` OK-lines on the ten sibling paths, and dual-AWS hash agreement pin that layout. The metadata text says `2026-08-26T04:19Z` against file mtime `04:18:35Z`; GO is still after that file and before DONE.
3. V6 has no hostile referee report in-tree. This review re-hashed the V6 compiler, both V6 certificates, and the 71 records, and checked V7's fail-closed reconstruction against those hashes. That is source-dependency custody of the identity used here, not a substitute V6 review of the `eta>=15/4` theorem.
4. Original 9-by-8 Q-R matrix entries are not serialized. RREF, the eight `row_qr_sha256` digests (equal to V5), and the two polynomials are frozen. Same pattern as V5; enough for this free-zero solution; not enough for a kernel-completeness theorem.
5. The compiler's `eta0 = max(-c/E)` loop does not, by itself, inspect `U,V` on the threshold face. The certificate stores the 28 face monomials, all of which have `U+V>0`; this review charged that. The open-quadrant strictness is in the records, not only in the `max` reduction.
6. r6d `free` shows 132 GiB used vs box03 22 GiB; swap is zero on both, and this job's RSS is 22 MiB under a 4 GiB `ulimit -v`. Registration leaves unrelated r6d toric-B PID 185517 untouched. That is not evidence that another campaign job was stopped, and not a defect in this package.
7. Six non-Q-R higher-`h` monomials of V6 are deleted as collateral of the exact product. `RESULT.md` does not claim those deletions as the named target; the named target is the eight-term Q-R piece, which is entirely cancelled. Residual `h^2` has exactly the two stored non-Q-R terms.

No source or certificate repair is required.

H2_QR_SYZYGY_LIFT_CONFIRMED
