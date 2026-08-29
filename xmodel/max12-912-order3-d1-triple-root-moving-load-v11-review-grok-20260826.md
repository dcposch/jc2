# Hostile text-only review — D1 triple-root moving-load discriminator V11

| Field | Value |
|---|---|
| Claim under review | Restore ordinary constant-field loads `kbar=Λ^6 k`, row-3 target `Λ^{15} μ`, row-6 target `Λ^{18} ν`, row-8 target `Λ^{20}(1+τ)` on the literal V8/V9 witness; fail-closed eight full-load row covariances; specialization `(k,μ,ν)=(0,2/3,0)` recovers the frozen 48-term polynomial of SHA `53cf4b65…`. Uniformity of that existing witness over arbitrary constant-field loads in the weighted a-chart `wt(a)=1`, `wt(h)=3`. Retirement of `(p,c)=(0,0)` as the affine `P(2,3)` cone vertex, not a strict coefficient-infinity leading centre. Classification of nominal `v(Λ/a)≤0` as a chart/order issue in this strict associated-graded sector |
| Overall verdict | **MOVING_LOAD_V11_CONFIRMED**. Dual AWS encodings emit certificates that differ only in `tag` and `order`; deleting those fields gives identical sorted SHA `a4f7c47b7f57e6dea9cecd89a74d4b7b4ac80a59abad431dfe3a64260b142477`. Both workers reconstruct the reviewed V9 48-term polynomial of SHA `53cf4b65…` from the frozen V8–V1 chain, restore the four ordinary load rows named above, treat load characters as zero, and fail-close all eight transported full-load covariances. The 62-term full-load witness has SHA `c0f1552c…`; its 14-term load residual has SHA `dbd78a81…`; specializing `(k,μ,ν)=(0,2/3,0)` is dictionary recovery of the frozen 48-term subset, not a nearby normalization. Parameter counts are `k:13`, `μ:0`, `ν:1`. The vanishing of `μ` is the exact identity `F_3≡0` in the literal V8 multiplier list, not a sampling claim. Every load term has strictly positive closed-corner margin (minimum 1). The 30 non-target zero-corner face terms, the coefficient-one target `a^3 Λ^{20}`, and the coefficient-one split `a^3 Λ^{20} τ` are dictionary-equal to the reviewed V9/V10 face. All eight common-cubic graph coefficients vanish at `(p,c)=(0,0)` and re-digest to the stored SHAs; with the reviewed support theorem this is the affine cone vertex and is projectively irrelevant for the strict coefficient-infinity leading problem. On every genuine nonzero discriminant-zero projective point, `p=-3a^2`, `c=2a^3` has `a≠0`, and after `P(2,3)` normalization `a` is a unit, so a positive radial/Rees `Λ` retains `v(Λ/a)>0`. No hidden load-character, multiplier, specialization, face, vertex, or chart/order mismatch was found |
| Smallest failing identity | none in the frozen V11 source, either harvest tree, either AWS stream, the hash-pinned V9/V8/V7/V6/V5/V4/toric/V1/charged sources, the recorded 62-term full-load polynomial, the 14-term load residual, the 48-term fixed specialization, the eight graph-coefficient vanishings at `(p,c)=(0,0)`, the disc-zero parametrization `p=-3a^2`, `c=2a^3`, or the `P(2,3)` unit-normalization of `a` |
| Smallest missing hypothesis for a stronger theorem | formal-series loads `k,μ,ν` (as opposed to constant-field values); a regraded higher-order source stratum whose actual leading coefficient vector is not this associated-graded `P(2,3)` form; a `Λ`-leading chart with `v(Λ)` at most the leading cubic scale; another source chart or normal direction; a global landing or accessibility theorem; D1; or JC2 |
| Evidence tier | SHA-256 of the freeze chain and already-emitted AWS files; byte comparison of harvest copies against package-top source; `json` comparison of the two certificates after deleting `tag` and `order`; toric canonical digest of the 62/14/48 recorded monomials and of the eight graph polynomials; integer/`Fraction` arithmetic on every recorded exponent against the axis-coefficient formula, the V8 closed-corner, and the open-slope table; dictionary comparison of the 48 load-free records to the V10 a-chart records; hand identities `F_3≡0`, `F_6·(−Λ^{18}ν)=−(1/24) q_1 Λ^{18} ν`, the disc-zero parametrization, and `P(2,3)` scaling. No local Singular, Sage, msolve, Lean, Python algebra, compiler execution, charged reconstruct, or eight-row product replay |
| Reviewer / model | Grok 4.6 (xAI). Text-only algebraic-geometry / tropical-weight / source-custody referee |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Host | Darwin. V11 compiler, V10 compiler, V9 compiler, V8 compiler, V7 compiler, V6 compiler, V5 compiler, V4 compiler, V1 compiler, toric compiler, charged reconstruct, Singular, and every solver were not run |

## What was and was not run

No local substantive computation was run. In particular this review did **not** execute `compile_moving_load_v11.py`, `compile_weighted_two_chart_v10.py`, `compile_axis_covariance_v9.py`, `compile_hq_linear_filtered_lift_v8.py`, `compile_h2_qr_syzygy_lift_v7.py`, `compile_h_grade5_kernel_lift_v6.py`, `compile_h_qr_syzygy_lift_v5.py`, `compile_h_first_transport_v4.py`, `compile_q2_first_lift.py`, `compile_toric_blowup.py`, `independent_reconstruct.py`, Singular, Sage, msolve, Lean, or any other solver, and it did not re-multiply `sum F_i E_i` or reconstruct the unsubstituted eight rows. Hashes were checked with SHA-256 of file bytes. File identity was checked by byte comparison. Marker counts used exact-line matches. Git identity was read with `git rev-parse`. JSON fields were read with Python `json` (no algebra libraries). Canonical SHA-256 values of recorded polynomials were recomputed from the already-emitted exponent dictionaries with toric `NAMES` order and `separators=(",", ":")`. Axis characters, closed corners, and open slopes of recorded monomials were scored by integer and `Fraction` arithmetic against the displayed formulae.

The V10 review `xmodel/max12-912-order3-d1-triple-root-weighted-two-chart-v10-review-grok-20260826.md` was read in full and then checked, not inherited: the 48 load-free V11 records were compared dictionary-wise to the V10 a-chart records, and the support theorem was re-read from its own source.

Charged freeze SHA-256, recomputed and matched:

```text
466a0665f8c6a69a318a91ccd585517978767da9bf2b0f8b28ad098d1906d13d  FREEZE.sha256
c7d42e2d38fc8ca3f283c768287a87f7e52dba0678aa41412f6be5b9d62db925  RESULT.md
c170e8cb2343b20bb70a8d3051b64dba72c482789e3fd8e154d049c1496604ba  SOURCE_CLOSURE.sha256
b2b0f44a8fcd09708762ab2b035bd50141a21088ef241207b026fe3b53fecb25  compile_moving_load_v11.py
aad4391c937467240223d8306b4caa87ac61d7d16a1d5da2e5b389e7e99932f3  remote_worker.sh
bbd712444d8b6b3392ed0c2209f99e04f9b8d740b0e7e508a63c3eabdbc93be0  Box03 JSON
0c6aca31fa67b11ad939f015e0786d9e6a72cf1527051a8e437f1bcc23379bcf  r6d JSON
a4f7c47b7f57e6dea9cecd89a74d4b7b4ac80a59abad431dfe3a64260b142477  normalized certificate
c0f1552c06650e321db954ab99788324f59e52dea94fd8e7dfbdfbb3931aeab6  62-term full-load witness
dbd78a81294d473aa043af6e0b0c87ce8050ae3e906a20d07395143d4371d75f  14-term load residual
53cf4b656c4415324a74862ec108b902ac8eade22733b2cb3a58cd3e447491e0  fixed specialization / frozen V9 witness
a274c8d8e0883ce7606f31f69803a293afb15ad48fe9d401191cac1cdbe1daee  reviewed support theorem
f81c5b054c2ff331176bd39005ad8f826b92efbfd5e16b1f7f20ae7dcbab7226  reviewed V9 ancestry
```

Every immutable V11 charge pin matched. Prerequisite compilers named by `SOURCE_CLOSURE.sha256`, recomputed and matched:

```text
55a27313370722e9ab255b34d3cb3d2ed592c47c32b5461397a8aa26a1a2a8a1
  compile_axis_covariance_v9.py
ea38710ed3b11a58dac050430ba421dcec902def645f59da28c2d9418c60c247
  compile_hq_linear_filtered_lift_v8.py
a4500936c83c82ef12d68c145ef6672688d401292c05dab36b95002df4138de3
  compile_h2_qr_syzygy_lift_v7.py
c7d9faed50b93cb7bb3905d8d386d2dc0f670c300baeefa78864d5dd3097dfce
  compile_h_grade5_kernel_lift_v6.py
8a963360f16a29c6841050f82e9eb79051005d821c6ec7837d0614ca8ead7366
  compile_h_qr_syzygy_lift_v5.py
3bbf1ebfb9f8b15054fe2f592bea92d8e07b95bce4d6ca131cd81c95f3698306
  compile_h_first_transport_v4.py
c76ef85ac14f81839674368c55a324499832e6cf4b589befa68baf93a42b1490
  compile_toric_blowup.py
0385b0b1e60b3bd37fa5fbee90dd6c17a454722bdbff424ea83c2ab0fa19df45
  compile_q2_first_lift.py
67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623
  independent_reconstruct.py
```

Every path listed in `FREEZE.sha256` recomputed and matched (19/19). Nested `SOURCE_CLOSURE.sha256` (15/15 from the case root) and both harvested `result.sha256` manifests (5/5 each) matched. Empty compiler stderr files are the empty-string digest `e3b0c442…`. Both rc files are the two-byte string `"0\n"`, digest `9a271f2a…`. Both harvested remote-tree manifests (35/35 entries each, no AppleDouble sidecars) matched the files present in that harvest directory. Their SHAs match `RESULT.md` and `FREEZE.sha256`:

```text
ea47f554dcbf381d699449f81d74674b6bb8e6f45b7afd5b41f0cc7cfc76849b  Box03
bb0ac5f6d29afac55eebf3f45cc555cdc73cbdd6aae1a558f1f759466beba55f  r6d
```

Read in full before the verdict: every file at
`cases/max12_912_order3_d1_triple_root_moving_load_v11_20260826/`
including both harvest trees; the hash-pinned V11 `build_full_rows` / `transport_full` / `specialize_fixed_loads` / `central_boundary_check`; the hash-pinned V9 `CHARACTER` / `coefficient_images` / `build_rows` / `fixed_multipliers` / `character_weight` / `transport`; the hash-pinned V8 `D2` / `HQ` and V7 `G1`; the hash-pinned V1 `multipliers()[3]={}` and `multipliers()[6]=q1/24`; the hash-pinned toric `NAMES` / `kbar=x y k` with `x y = Λ^6` / `target(ell)` / `specialize_zero` / `digest`; the charged `build()` ninth source variable `k`; the reviewed exceptional-support theorem; and the reviewed V9 ancestry. Predecessor conclusions were recomputed, not inherited.

---

## Promotion

**Accept `FOR THE PINNED ORDINARY-TAIL EIGHT-ROW MODULE WITH THE CHARGED SOURCE independent_reconstruct.py AT 67343b56… AND THE LITERAL V8 MULTIPLIERS F_i^(8) (q2-CORRECTION F1+=q2/12, F2+=-q2/9; SCALAR-h CORRECTION G1=(5/2,-25/18,0,1/4,-1/3,0,0,0); SCALAR-h-SQUARED CORRECTION D2=(5/24,-2/9,0,0,0,0,0,0); V8 COLUMNS F1-=h q1/36, F2-=h q0/72; AND IN PARTICULAR F3≡0), STARTING FROM THE REVIEWED V9 UNIVERSAL WITNESS OF SHA 53cf4b65… (THE CLEARED IDENTITY sum_i a^(11-i) F_i^(8)(hat) E_i = a^23 W^(8)(hat) WITH CLEARING POWER THREE; VERDICT UNIT_AXIS_COVARIANCE_CONFIRMED) AND THE REVIEWED EXCEPTIONAL-SUPPORT THEOREM OF SHA a274c8d8… (REDUCED STRICT COEFFICIENT-INFINITY SUPPORT IS THE GRAPH OF C=z^3+p z+c, I.E. WEIGHTED P(2,3)), THE REGISTERED DUAL-AWS V11 RUNS PROVE THE FOLLOWING. REPLACING THE FIXED LOADS BY THE ORDINARY CONSTANT-FIELD LOADS kbar=Λ^6 k, ROW-3 TARGET Λ^{15} μ, ROW-6 TARGET Λ^{18} ν, ROW-8 TARGET Λ^{20}(1+τ), WITH LOAD CHARACTERS ZERO IN THE V9 AXIS TABLE AND WITH ALL EIGHT TRANSPORTED FULL-LOAD ROW COVARIANCES, YIELDS A 62-TERM COMBINATION OF SHA c0f1552c… WHOSE SPECIALIZATION (k,μ,ν)=(0,2/3,0) IS DICTIONARY-EQUAL TO THE FROZEN 48-TERM WITNESS OF SHA 53cf4b65…, NOT A NEARBY NORMALIZATION. THE 14 LOAD-SENSITIVE TERMS HAVE SHA dbd78a81… AND COUNTS k:13, μ:0, ν:1; μ:0 IS THE EXACT VANISHING OF THE ROW-3 MULTIPLIER. EVERY LOAD TERM HAS STRICTLY POSITIVE CLOSED-CORNER MARGIN (MINIMUM 1; THE UNIQUE ν TERM HAS MARGIN 3; THE k TERMS HAVE MARGINS 1, 7/2, OR 6). THE 30 NON-TARGET ZERO-CORNER FACE TERMS REMAIN DICTIONARY-EQUAL TO THE REVIEWED V9/V10 FACE, EACH WITH A STRICTLY POSITIVE u OR v SLOPE; THE DISTINGUISHED TERMS REMAIN COEFFICIENT-ONE a^3 Λ^{20} AND COEFFICIENT-ONE a^3 Λ^{20} τ. THE CLOSED-CORNER HISTOGRAM IS 0:32, 1:10, 5/2:11, 3:1, 7/2:2, 5:5, 6:1 AND THE OBSTRUCTION LIST IS EMPTY. THUS ARBITRARY CONSTANT-FIELD VALUES OF k,μ,ν CANNOT ALTER THE OLD EQUALITY FACE OF THIS WITNESS. THIS IS THE ENDPOINT EXISTING_WITNESS_FULL_CONSTANT_LOAD_UNIFORM. SEPARATELY, ALL EIGHT COMMON-CUBIC GRAPH COEFFICIENTS VANISH AT (p,c)=(0,0). BY THE REVIEWED SUPPORT THEOREM THAT POINT IS THE AFFINE CONE VERTEX AND THE IRRELEVANT POINT OF Proj P(2,3), NOT A STRICT COEFFICIENT-INFINITY LEADING CENTRE. THIS IS NOT THE EXCLUSION OF A HIGHER-ORDER OR REGRADED ARC. ON EVERY GENUINE NONZERO DISCRIMINANT-ZERO PROJECTIVE POINT ONE HAS p=-3a^2, c=2a^3 WITH a≠0, AND AFTER P(2,3) NORMALIZATION a IS A UNIT, SO A POSITIVE RADIAL/REES Λ RETAINS v(Λ/a)=v(Λ)>0. NOMINAL v(Λ/a)≤0 IS THEREFORE A WRONG CHART/ORDER CHOICE IN THIS STRICT ASSOCIATED-GRADED SECTOR, OR THE CHOSEN LEADING VECTOR IS THE VERTEX AND MUST BE REGRADED AT ITS NEXT ACTUAL COEFFICIENT ORDER; IT IS NOT A MISSED LIVE POINT OF THIS CHART.`**

Do not promote this to: loads that are themselves formal series; another source chart; a global landing or accessibility theorem; D1; JC2; a no-arc theorem at the closed point `a=h=0` identically; or a theorem in a `Λ`-leading or regraded filtration.

---

## Charge 1 — Full freeze / source / custody audit

**CONFIRMED. Every freeze entry recomputes. Both registered workers are fail-closed, hash-gated, empty-stderr, sub-cap, pre-GO, and source-closed against the package-root manifest. Opposite traversal orders return certificates that differ only in `tag` and `order`; deleting those two fields gives literally identical sorted JSON of SHA `a4f7c47b7f57e6dea9cecd89a74d4b7b4ac80a59abad431dfe3a64260b142477`. There is no PID-capture erratum and no AppleDouble sidecar in this V11 harvest.**

Required anchors, recomputed:

```text
c7d42e2d38fc8ca3f283c768287a87f7e52dba0678aa41412f6be5b9d62db925  RESULT.md
466a0665f8c6a69a318a91ccd585517978767da9bf2b0f8b28ad098d1906d13d  FREEZE.sha256
c170e8cb2343b20bb70a8d3051b64dba72c482789e3fd8e154d049c1496604ba  SOURCE_CLOSURE.sha256
bbd712444d8b6b3392ed0c2209f99e04f9b8d740b0e7e508a63c3eabdbc93be0  aws_box03_forward/moving_load_v11.json
0c6aca31fa67b11ad939f015e0786d9e6a72cf1527051a8e437f1bcc23379bcf  aws_r6d_reverse/moving_load_v11.json
53cf4b656c4415324a74862ec108b902ac8eade22733b2cb3a58cd3e447491e0  universal_fixed_sha256 / fixed_specialization_sha256
c0f1552c06650e321db954ab99788324f59e52dea94fd8e7dfbdfbb3931aeab6  full_load_universal_sha256
dbd78a81294d473aa043af6e0b0c87ce8050ae3e906a20d07395143d4371d75f  load_residual_sha256
```

Recomputed `FREEZE.sha256` entries, all matched (19/19). Harvest copies of compiler, worker, preregistration, AWS registration, and source closure are byte-identical to the package top on both hosts. Harvested `SOURCE_CLOSURE.sha256` is byte-identical to the top copy. Both `source.check` files are identical (`cb37c87f…`) and print `OK` on all fifteen paths; they are also byte-identical to both `prelaunch_source.check` files. The worker `cd`s to `$run` before `sha256sum -c SOURCE_CLOSURE.sha256`. The compiler locates V9 via `HERE.parents[1]/cases/…` and hash-checks it at `V9_SHA=55a27313…` before import; it additionally hash-checks the V9 review and the support review. Tag gates: worker `case` requires prefix `max12_912_order3_d1_triple_root_moving_load_v11_20260826T*`; compiler `require_aws` requires Linux, DMI vendor `Amazon EC2`, and tag prefix `max12_912_order3_d1_triple_root_moving_load_v11_`. Both refuse non-`forward`/`reverse` orders.

The V9–V1 chain re-pins: V9 pins V8 at `ea38710e…`; V8 pins V7 at `a4500936…`; V7 pins V6 at `c7d9faed…`; V6 pins V5 at `8a963360…`; V5 pins V4 at `3bbf1ebf…`; V4 pins toric `c76ef85a…`, V1 `0385b0b1…`, and `independent_reconstruct.py` at `67343b56…`. Treating `aws_box03_forward/` or `aws_r6d_reverse/` as a new source root would make those siblings invisible. That is not the charged root. Even if the remote `sha256sum -c` path and the compiler `HERE.parents[1]/cases/…` path had been distinct directories, both are hash-gated to the same frozen bytes; dual AWS both exited 0.

| Check | Box03 forward | r6d reverse |
|---|---|---|
| Public IP / harvested hostname | `98.80.65.144` / `ip-172-30-0-249` | `100.26.198.153` / `ip-172-30-0-45` |
| Tag | `…_v11_20260826T054500Z_box03_forward` | `…_v11_20260826T054500Z_r6d_reverse` |
| Worker PID | `168130` | `235150` |
| Caps | `memory_kib=8388608`, `timeout=1800`, `nice -n 10`; `ulimit -v 8388608` | same |
| Order | `forward` (`ell=1..8`, `F*E`) | `reverse` (`ell=8..1`, `E*F`) |
| Started / finished UTC | `2026-08-26T05:49:57Z` / `05:50:32Z` | same |
| GO released | `2026-08-26T05:50:25Z` | same |
| Compiler stdout SHA | `797b411d…` | `72eba3f5…` |
| Certificate SHA | `bbd71244…` | `0c6aca31…` |
| RSS / swap / exit | 22340 KiB / `Swaps: 0` / 0 | 22480 KiB / `Swaps: 0` / 0 |
| Pre/post `free` swap | `0B` / `0B` | `0B` / `0B` |
| Elapsed | 6.46 s | 6.40 s |
| PASS markers, each once | `PASS_MOVING_LOAD_V11`, `PASS_REMOTE_WORKER` | same |
| `FAIL_` / `REFUSED` / `FAILED` | none; stderr empty; no `REFUSED`/`FAILED` files | none; stderr empty; no `REFUSED`/`FAILED` files |

`AWS_LAUNCH_METADATA.md` records a live fleet audit at `2026-08-26T05:48:06Z` with both workers `WAITING_GO`, neither run directory containing `GO`, `DONE`, or `FAILED`, and source-closure manifest SHA `c170e8cb…` matching the frozen file. Both `GO` sentinels were released at exactly `2026-08-26T05:50:25Z` and are empty (digest `e3b0c442…`). Worker start UTC precedes GO; finish UTC is 7 s after GO, matching the 6.4 s compile plus the post-GO source-hash check. Harvest manifests were created at `2026-08-26T05:51:08Z`. No `REFUSED` or `FAILED`. `worker.launch.pid` equals the self-recorded metadata PID on both hosts. The unrelated r6d worker PID `185517` is recorded as untouched.

The two JSON files are **not** byte-identical. Their key sets are equal (21 keys). The only value differences are the two preregistered custody fields `tag` and `order`. Deleting those fields and dumping with `sort_keys=True, indent=2` plus a trailing newline yields one 39137-byte blob of SHA

```text
a4f7c47b7f57e6dea9cecd89a74d4b7b4ac80a59abad431dfe3a64260b142477
```

on both hosts, matching `RESULT.md` and the charged semantic-equality SHA. Compiler stdout differs only in the preregistered `ORDER=` line and the certificate SHA of the tagged JSON; the algebraic metric block is identical:

```text
STATUS=EXISTING_WITNESS_FULL_CONSTANT_LOAD_UNIFORM
FULL_LOAD_UNIVERSAL_SHA256=c0f1552c06650e321db954ab99788324f59e52dea94fd8e7dfbdfbb3931aeab6
LOAD_RESIDUAL_SHA256=dbd78a81294d473aa043af6e0b0c87ce8050ae3e906a20d07395143d4371d75f
LOAD_RESIDUAL_TERMS=14
LOAD_SENSITIVITY={"k": 13, "mu": 0, "nu": 1}
OBSTRUCTION_COUNT=0
PASS_MOVING_LOAD_V11
```

Worker fail-closed conditions, all met on both hosts: `rc=0`, empty stderr, exactly one `PASS_MOVING_LOAD_V11` endpoint. Caps 8 GiB / 1800 s; RSS is 22 MiB; elapsed is 6.4 s.

Source payload was byte-identical on both hosts (`4627164b…  source_payload.tgz`). Prelaunch Python is `3.12.3` on both; remote `py_compile` produced empty stdout and empty stderr. `prelaunch_manifest.sha256` on both hosts is exactly the frozen source-closure digest `c170e8cb…`. Registration tags, job directories, caps, nice 10, and the untouched r6d Singular worker PID `185517` match `AWS_REGISTRATION.md` and `AWS_LAUNCH_METADATA.md`.

Both remote-tree manifests list 35 files and match those files 35/35. Neither manifest lists an AppleDouble sidecar; none is present in either harvest. `AWS_LAUNCH_METADATA.md` records Linux tar warnings about unsupported macOS provenance xattrs and the absence of AppleDouble; every charged file passed its registered SHA before and after the run. Local harvest directories contain `__pycache__/compile_moving_load_v11.cpython-312.pyc`, absent from the remote-tree manifests. Bytecode of the frozen compiler; not a source file.

---

## Charge 2 — Source reconstruction

**CONFIRMED. The compiler restores exactly `kbar=Λ^6 k`, row-3 target `Λ^{15} μ`, row-6 target `Λ^{18} ν`, and row-8 `Λ^{20}(1+τ)`. Load characters are zero in the V9 axis table. All eight transported full-load row covariances are fail-closed on both hosts. Specialization `(k,μ,ν)=(0,2/3,0)` recovers the frozen 48-term V9 witness by dictionary identity of SHA `53cf4b65…`, not a nearby normalization.**

Construction, from the hash-pinned V11 compiler, which loads the hash-pinned V9 compiler, which loads the hash-pinned V8/V7/V6/V5/V4/toric/V1 chain:

1. `t.load_charged_source().build()["tails"]` is the eight negative Laurent tails of `independent_reconstruct.py` at `67343b56…`. The charged source ring is `a0,…,a7,k`; the ninth source variable is ordinary `k`, and `g = F_{12}(f) + k F_6(f)`.
2. V9 `coefficient_images` returns nine images, the last of which is `{}` (kbar killed). V11 `build_full_rows` copies that list and replaces the last image by `t.monomial(la=6, k=1)`. The toric parent writes `kbar = x y k` with `x y = Λ^6`, hence `kbar = Λ^6 k`. That is the restoration, not a different load convention.
3. Full-load row targets, subtracted after substituting the tails:

```text
rows[3] -= Λ^{15} μ
rows[6] -= Λ^{18} ν
rows[8] -= Λ^{20} + Λ^{20} τ
```

This is the toric `target(ell)` convention (`ell=3: Λ^{15}μ`, `ell=6: Λ^{18}ν`, `ell=8: Λ^{20}(1+τ)`), not V9's baked `(2/3)Λ^{15}` with `ν` unsubtracted. Row 8 is the same as V9.
4. Load characters. V9

```text
CHARACTER = {la:1, tau:0, rho:1, h:3, q2:4, q1:5, q0:6, r2:7, r1:8, r0:9}
```

does not contain `k`, `μ`, `ν`. Both `character_weight` and V11 `full_character_weight` use `CHARACTER.get(name, 0)`, so those three coordinates contribute 0 to the axis power. V9 `character_weight` *forbids* `k,μ,ν` in the multipliers; V11 `full_character_weight` forbids only `p,c,a,x,y` in the fixed rows, because the restored loads are allowed in the rows. Constant-field loads therefore do not shift the transported `a`-power. (The physical Rees weights `w(k)=6`, `w(μ)=15`, `w(ν)=18` of the support theorem are the weights of the *unscaled* load coordinates; after writing `kbar=Λ^6 k` with `k` constant, the weight sits on `Λ`.)
5. Covariance. For `ell=1..8`, V11 fail-closes on

```text
transport_full(fixed_full_rows[ell], 12+ell) == moving_full_rows[ell]
```

and records eight row SHAs, identical in both certificates. Dual AWS both exited 0. This review did not replay the eight substitutions.
6. Fixed-load reconstruction is the V9 path: `build_rows` with baked `(2/3)Λ^{15}`, no `ν` subtraction, empty kbar image, clearing power fail-closed at 3, universal product `F*E` forward and `E*F` reverse. Dual AWS both fail-close on `digest(universal)=53cf4b65…`.
7. Specialization of the *full* polynomial:

```text
drop every monomial with k>0 or ν>0;
multiply the coefficient by (2/3)^{e[μ]} and set e[μ]=0.
```

This is exactly `(k,μ,ν)=(0,2/3,0)`. Dual AWS both fail-close on dictionary equality with the reconstructed V9 polynomial. Independently, the 48 load-free recorded monomials re-digest, in toric canonical form, to

```text
53cf4b656c4415324a74862ec108b902ac8eade22733b2cb3a58cd3e447491e0
```

and are dictionary-equal (coefficient, core exponents, axis, corner, open slopes, role) to the 48 V10 a-chart records. Because `μ` never occurs, the factor `(2/3)^{e[μ]}` never fires; recovery is by deleting the 14 load monomials, not by rescaling the old 48. Target and split-target remain coefficient-one. That is the frozen witness, not a nearby normalization.

Clearing power is re-checked at 3 before any full-load algebra. Dual AWS both exited 0.

---

## Charge 3 — Uniformity of all 62 records, especially the 14 load-sensitive ones

**CONFIRMED. Independently scored 62/62 recorded monomials. Counts `k:13`, `μ:0`, `ν:1`. The vanishing of `μ` is the exact identity `F_3≡0`. Every load term has strictly positive closed-corner margin, minimum 1. The old 30-term non-target face, the target, and the split target are unchanged. Arbitrary constant-field load values cannot alter that face.**

Axis-coefficient formula, charged, on every recorded term:

```text
axis = e[a]-3 + e[la]-20 + e[rho]
     + 3 e[h] + 4 e[q2] + 5 e[q1]
     + 6 e[q0] + 7 e[r2] + 8 e[r1] + 9 e[r0].
```

Stored `axis_coefficient` matches (62/62). All 62 vanish. Extra toric slots `p,c,x,y` are zero on every term. `ρ` is zero on every term. `μ` is zero on every term.

Closed corner, charged:

```text
corner = (e[la]-20) + e[rho]
       + 5 (e[q2]+e[q1]+e[q0])
       + (15/2) (e[r2]+e[r1]+e[r0]).
```

Stored `ell_corner` matches (62/62). Histogram of the 62 values:

```text
0:32,  1:10,  5/2:11,  3:1,  7/2:2,  5:5,  6:1.
```

Zero negative margins. Splitting by load support: the 48 load-free terms reproduce the V9/V10 histogram `0:32, 5/2:11, 5:5`; the 14 load terms are exactly `1:10, 3:1, 7/2:2, 6:1`. Canonical digest of all 62 recorded terms is `c0f1552c…`; of the 14 load terms, `dbd78a81…`; of the 48 load-free terms, `53cf4b65…`. All three match the certificates, `RESULT.md`, and the charge pins.

Open slopes, charged:

```text
u = e[q1]+e[q0],   v = e[q2],   eta = e[h],   T = e[tau],   H = e[rho].
```

Stored `open_slopes` match (62/62). Every coordinate is a nonnegative integer. Python `any(slopes.values())` was not trusted: positivity was checked as a strictly positive integer coordinate.

Target and split target, unique, coefficient-one, corner 0:

```text
+1  a^3 Λ^{20}          axis 0, corner 0, all open slopes 0
+1  a^3 Λ^{20} τ        axis 0, corner 0, T=1
```

Non-target zero-corner face: 30 terms, matching the certificate field. Dictionary-equal to the V10 a-chart face (30/30), including coefficients and open slopes. Face-term slope support, unchanged:

```text
('u',): 6,   ('v',): 6,   ('u','v'): 8,
('eta','u'): 3,   ('eta','v'): 1,   ('eta','u','v'): 6.
```

All 30 have `u>0` or `v>0`. Zero of the 30 rely only on `eta`, `T`, or `H`. Obstruction list empty (0/0). No load monomial lies on this face.

### Why `μ:0` is exact, not sampled

The only source of `μ` is the subtracted row-3 target `Λ^{15} μ`. The literal V8 multiplier of that row is empty:

```text
V1 multipliers()[3] = {}
q2-correction is only on ell=1,2
G1[2] = 0
D2[2] = 0
HQ has no ell=3 column
```

Hence `F_3≡0` and `F_3 · (−Λ^{15} μ) = 0`. The charged tails do not contain `μ`. Therefore no recorded monomial can carry `μ`. Dual AWS both report `mu:0`. This is an identity in the frozen multiplier list.

The unique `ν` term is the companion identity on row 6. V1 `multipliers()[6] = (1/24) q_1`, with `G1[5]=D2[5]=0` and no HQ, so

```text
F_6 · (−Λ^{18} ν) = −(1/24) q_1 Λ^{18} ν.
```

The emitted load record is exactly that monomial, coefficient `-1/24`, corner

```text
(18-20) + 5·1 = 3.
```

The 13 `k` terms are the image of ordinary `k` through `kbar=Λ^6 k` in the charged tails, multiplied by the nonzero `F_i`. No mixed `(k,μ)`, `(k,ν)`, or `(μ,ν)` monomial occurs.

### Load margins, including the two slope-zero `k` terms

Minimum load corner is 1. Breakdown:

- ten `k` terms at margin 1, including the two with all open slopes zero

```text
+1/12   a^2 Λ^6 r2 r1 k     corner (6-20)+(15/2)·2 = 1, slopes 0
-1/36   a^3 Λ^6 r2^2 k      corner (6-20)+(15/2)·2 = 1, slopes 0
```

- one `ν` term at margin 3, displayed above, with `u=1`
- two `k` terms at margin `7/2`
- one `k` term at margin 6: `Λ^6 q2^3 q1 k`, corner `(6-20)+5·4=6`

Those two slope-zero terms are **not** a tie at the equality face: they sit strictly above it at the closed corner. In the associated-graded closed cell they vanish relative to `Λ^{20}`. They cannot cancel a face term, and they cannot become leading for any constant `k`. The other twelve load terms have a strictly positive `u` or `v` as well, which is surplus.

Consequently every constant-field value of `(k,μ,ν)` — including values that make some load coefficients large — leaves the 32 zero-margin terms, and in particular the 30-term non-target face, coefficientwise unchanged. That is uniformity of the *existing* witness, not a new combination.

---

## Charge 4 — Central vertex / projective irrelevance

**CONFIRMED. The reviewed `P(2,3)` support theorem, together with the exact vanishing of all eight graph coefficients at `(p,c)=(0,0)`, makes this point the affine cone vertex and the irrelevant point of `Proj`. It is not a strict coefficient-infinity leading centre. This is distinct from excluding a higher-order or regraded arc.**

The pinned review
`xmodel/max12-912-order3-d1-weighted-infinity-exceptional-support-review-grok-20260825.md`
at SHA `a274c8d8…`, verdict CONFIRMED, identifies the reduced affine support of the eight-tail exceptional ideal with the graph

```text
B_7=3p,     B_6=3c,      B_5=3p^2,     B_4=6p c,
B_3=p^3+3c^2,  B_2=3p^2 c,  B_1=3p c^2,  B_0=c^3
```

(`c` is the theorem's `r`). In the weighted projective space of the `B_i` this is `P(2,3)`. The theorem distinguishes three origin-objects: the affine origin as a point of the cone; an origin-supported embedded component, which saturation may drop; and the irrelevant point of `Proj`, which is not a point of the weighted projective exceptional divisor. A coefficient-infinity leading centre is a *projective* point of that divisor, i.e. a nonzero leading `(p,c)` up to the `P(2,3)` action.

V11 independently checks the eight graph polynomials, in that order, by `specialize_zero` at `{p,c}` (equivalently: evaluate at `(0,0)`). Every monomial of each of the eight has positive `p` or `c` exponent, so all eight vanish. Their toric canonical digests, recomputed from the displayed monomials, match the certificate:

```text
e484c96028c5835703b269bc40acc860c3a878ffb495ae0d167633044bc13cc6  c^3
2ebdde8b5e4da8a41575292aadb24a2f44e5df1f6175acd50e03b3661ad70aac  3 p c^2
ebcccc41f9ddeddc5e5cd8e5fceb9a012e540a184be0bb614e590030af46c331  3 p^2 c
edfa49410d2950405169112676bf55a2181970e21823cb3e8cf7d9b879e670df  p^3 + 3 c^2
8e85247a3026f73d69482f0a9912bc0cd39462988206f8366dcca4ac32f6bdaa  6 p c
e10b34be144c5f5ba35e2689411fde9daeb2bce6f9ad688ef896b735d3024b45  3 p^2
1c385fe1af9dc44aeb722188bd036bc2ec55f5ff94850c2328a3b9de0f40cc11  3 c
8121446965089fc556723404481d1efc344f2827067b3eda3f9ac414b057b2a0  3 p
```

Dual AWS both exited 0. Combined with the reviewed reduced-support theorem, `(p,c)=(0,0)` is the affine cone vertex. It is the triple-root cube `C=z^3`, and it is not a point of `Proj P(2,3)`. No separate central `a=h=0` elimination is live *as a leading centre of this associated-graded chart*.

This is **not** the exclusion of a higher-order or regraded arc. If an actual arc has vanishing leading `(B_i)` in this weighting, the chosen associated-graded vector is zero and the arc must be regraded at the next actual coefficient order. That is a different leading problem. The support theorem also does not classify embedded `m`-primary thickness, does not lift along `τ`, and does not exclude D1. Those remain outside the charged cell.

---

## Charge 5 — Nonpositive rescaled `Λ`

**CONFIRMED as a chart/order statement in this strict associated-graded sector. No live nonzero discriminant-zero projective point was missed. Regraded and `Λ`-leading strata remain, and are named.**

Hand identities.

A depressed cubic `z^3 + p z + c` has a multiple root at `a` if and only if `3a^2+p=0` and `a^3+p a+c=0`, hence

```text
p = -3 a^2,     c = 2 a^3.
```

The discriminant vanishes identically on this parametrization:

```text
-4 p^3 - 27 c^2
  = -4 (-3a^2)^3 - 27 (2a^3)^2
  = 108 a^6 - 108 a^6
  = 0.
```

Affine origin `(p,c)=(0,0)` if and only if `a=0`. That is Charge 4's vertex, already retired.

Every genuine *nonzero* discriminant-zero projective point therefore has `a≠0`. The `P(2,3)` action is `(p,c) ↦ (λ^2 p, λ^3 c)`. Taking `λ=1/a` sends the point to `(-3:2)`. (The representative `(-3:-2)` is the same `P(2,3)` point, because `λ=-1` flips the odd-weight coordinate `c`.) In residual coordinates the normalized double-root location is `a'=1`, a unit. A positive radial/Rees `Λ` still has `v(Λ)>0`, hence

```text
v(Λ/a) = v(Λ) - v(a) = v(Λ) > 0
```

after that normalization. Equivalently, in `P(2,3)` there is a unique discriminant-zero point, the class of `(-3:2)`; it is not an axis point (`p=0` or `c=0` forces `Δ≠0` off the origin), and it is not the vertex.

Therefore a cell with `v(Λ/a)≤0` cannot be a coefficient-infinity arc whose *leading* cubic is a genuine nonzero discriminant-zero projective point of this chart. Two exhaustive alternatives:

1. After projective normalization of a nonzero leading `(p,c)`, `a` is a unit, so `v(Λ/a)≤0` means `v(Λ)≤0`. That is not coefficient-infinity in this filtration; it is a finite-`Λ` or `Λ`-leading (wrong-order) chart.
2. The leading `(p,c)` is the vertex. Then the chosen associated-graded coefficient vector is zero and the arc must be regraded at its next actual coefficient order. That is Charge 4's remainder, not a missed V10 direction.

No live point of this strict associated-graded discriminant-zero projective chart was missed. What remains, and is not claimed, is listed in Charge 6.

This inference is elementary once the reviewed `P(2,3)` support theorem and the disc-zero parametrization are granted. It is not an extra AWS identity, and it is not a global no-arc theorem.

---

## Charge 6 — Scope

**CONFIRMED. The exact identities are the reconstruction, the 62-term uniformity arithmetic, the eight graph vanishings, the disc-zero parametrization, and the `P(2,3)` unit-normalization of `a`. The mathematical consequence is the Promotion paragraph. The firewall is the frozen one. Nothing beyond it is licensed.**

Exact identities (dual AWS, opposite order, plus hand algebra):

1. Restoration of `kbar=Λ^6 k`, row-3 target `Λ^{15}μ`, row-6 target `Λ^{18}ν`, row-8 target `Λ^{20}(1+τ)`; load characters zero; eight full-load row covariances; clearing power 3; specialization `(k,μ,ν)=(0,2/3,0)` dictionary-equal to the frozen 48-term polynomial of SHA `53cf4b65…`.
2. 62-term witness of SHA `c0f1552c…`; 14-term residual of SHA `dbd78a81…`; counts `k:13`, `μ:0`, `ν:1` with `μ:0` from `F_3≡0`; every load corner `≥1`; 30-term face, target, and split target unchanged; empty obstruction list.
3. Eight graph coefficients vanish at `(p,c)=(0,0)` and re-digest to the stored SHAs.
4. Disc-zero parametrization `p=-3a^2`, `c=2a^3`; `P(2,3)` normalization `λ=1/a` sends every nonzero such point to `(-3:2)` with `a` a unit.

Mathematical consequence, using the reviewed V9 unit-axis covariance, the reviewed V8 unique-least-term cell on the unchanged face, and the reviewed exceptional-support theorem:

- The existing V8 combination remains unique-least `Λ^{20}` in the registered open cell, uniformly in constant-field `(k,μ,ν)`.
- `(p,c)=(0,0)` is not a strict coefficient-infinity leading centre of this associated-graded chart.
- Nominal `v(Λ/a)≤0` is not a live point of this strict projective disc-zero chart.

### What is proved, for arbitrary constant-field loads

On the pinned ordinary common-cubic eight-row module, with the literal V8 multipliers and the charged tails at `67343b56…`, every constant-field triple `(k,μ,ν)` leaves the V8 equality face coefficientwise unchanged and strictly above it at every load monomial. Combined with the already-reviewed V8/V9/V10 directional cover of the noncentral weighted blow-up (fixed-load a-chart cone, h-chart squarefree open already uniform in loads by the squarefree theorem, overlap `s=-4`), the existing witness remains an obstruction in that cover after the loads are restored as constants.

### What is not proved

| Non-claim | Why it is open |
|---|---|
| Formal-series loads | `k,μ,ν` as elements of the DVR, or as series in the chart parameters, change the associated-graded rows. The firewall is constant-field only. |
| Other source charts | Same charged ordinary tails `67343b56…` only. A different passport, a different normal direction, or a non-ordinary chart is a different module. |
| Landing / accessibility | No inverse-function, rational-section, or global-landing theorem is used or produced. |
| D1 | The classical degree split and this associated-graded sector are not a D1 exclusion. |
| JC2 | Explicitly declined. |
| No-arc theorem at `a=h=0` identically | Charge 4 retires the vertex as projectively irrelevant for *this* leading problem. A regraded arc whose actual leading form appears at a finer order is a different problem. |
| `Λ`-leading / `v(Λ)≤` leading scale | Charge 5 classifies that cell as the wrong order for this coefficient-infinity filtration, not as excluded. |
| Embedded thickness of `I_inf` | The support theorem is reduced support only. |
| Squarefree global-support corollary | Not invoked. V11 does not replay the V10 h-chart squarefree argument; that argument remains V10's, already uniform in constant loads. |

The producer status `EXISTING_WITNESS_FULL_CONSTANT_LOAD_UNIFORM` is discharged. The V9 review consumed as ancestry is `UNIT_AXIS_COVARIANCE_CONFIRMED` at SHA `f81c5b05…`. The support review consumed as ancestry is CONFIRMED at SHA `a274c8d8…`. Independently of V10's verdict token, the 48 load-free V11 records match the V10 a-chart records, and V10's named remainders — moving constant loads, the central vertex as a leading centre, and nonpositive rescaled `Λ` as a point of this chart — are the three items just charged.

---

## Nits, not defects

1. Face positivity in the compiler is `any(slopes.values())`. Independently, every slope is a nonnegative integer and every face term has a strictly positive `u` or `v`. Load terms never hit the `corner==0` branch. No source repair.
2. `specialize_zero` drops monomials with positive `p` or `c` rather than substituting. For polynomials this is evaluation at `(0,0)`. All eight graph monomials have positive `p` or `c`. No source repair.
3. The certificate field `all_boundary_coefficients_zero_at_p_c_zero` is the literal `True` written after the fail-closed check, not a recomputed specialized polynomial. The eight SHAs of the *un*specialized graph polynomials are the custody, and they re-digest. No source repair.
4. `specialize_fixed_loads` drops `k` and `ν` monomials rather than substituting 0, and multiplies by `(2/3)^{e[μ]}`. With `μ:0` the factor never fires. Dictionary equality with the reconstructed V9 polynomial is the custody. No source repair.
5. The compiler does not emit a separate `F_3` digest. The identity `F_3≡0` is read from the frozen V1/V7/V8 multiplier list; `μ:0` on 62/62 records is the observable. The unique `ν` term matches `F_6·(−Λ^{18}ν)` by hand. No source repair.
6. Two `k` terms have all open slopes zero. Both have closed-corner margin 1, so they are not a face tie. No source repair.
7. Charge 5 is a hand inference from the reviewed `P(2,3)` theorem plus the disc-zero parametrization, not an extra AWS polynomial identity. Dual AWS do not score `v(Λ/a)`. The inference is elementary and is firewallled as a chart/order statement. No source repair.
8. `FREEZE.sha256` is a 19-entry result pin, not a complete harvest pin. Dual `remote_tree_manifest.sha256` values are in the freeze and were checked 35/35 against the harvest trees. Pre-GO source identity is `SOURCE_CLOSURE.sha256`.
9. Local harvest directories contain `__pycache__/compile_moving_load_v11.cpython-312.pyc`, absent from the remote-tree manifests. Bytecode of the frozen compiler; not a source file.
10. r6d `free` shows 165 GiB used vs Box03 50–51 GiB; swap is zero on both, and this job's RSS is 22 MiB under an 8 GiB `ulimit -v`. Registration leaves unrelated r6d work untouched.
11. Unlike V10, this payload has no AppleDouble sidecar. Linux tar still warned about unsupported provenance xattrs. Every charged SHA passed before and after the run.

No source or certificate repair is required.

MOVING_LOAD_V11_CONFIRMED
