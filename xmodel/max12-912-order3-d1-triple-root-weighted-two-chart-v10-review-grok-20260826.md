# Hostile text-only review — D1 weighted triple-root two-chart V10

| Field | Value |
|---|---|
| Claim under review | Weighted blow-up of `(a,h)=(0,0)` with `wt(a)=1`, `wt(h)=3`. a-chart `h=a^3 s`: literal 48-term V9 universal witness of SHA `53cf4b65…` has vanishing axis coefficients, nonnegative closed-corner margins with histogram `32,11,5` at `0,5/2,5`, and 30 non-target zero-margin terms each with a positive open `u/v/eta/T/H` slope, under `ell=wt(Λ)-wt(a)>0`. Residual cubic `p=-3`, `c=2+s`, discriminant `-27 s(s+4)`, double roots `s=0,-4`. h-chart `h=t^3`, `a=t b`: residual cubic `z^3-3b^2 z+(2b^3+1)`, discriminant `-27(4b^3+1)`; ordinary rows of weight `12+i` including targets 15, 18, 20; squarefree order-20 theorem on `4b^3+1≠0`; overlap `4b^3+1=0 ⇒ s=b^{-3}=-4`; opposite-axis `a'=-a`, `h'=h+4a^3` preserves `(p,c)` |
| Overall verdict | **WEIGHTED_TWO_CHART_V10_CONFIRMED**. Dual AWS encodings emit certificates that differ only in `tag` and `order`; deleting those fields gives identical sorted SHA `25910f14424f0a021b00bf3d440b506b05aafc5c0980ee94beefe58608d5e12b`. Both workers reconstruct the reviewed V9 48-term polynomial of SHA `53cf4b65…` from the frozen V8–V1 chain. With `wt(a)=1`, `wt(h)=3`, the axis-coefficient formula vanishes on 48/48 recorded terms; closed-corner margins are the histogram `32,11,5` at `0,5/2,5`; all slopes are nonnegative integer exponents; every one of the 30 non-target zero-margin terms has a strictly positive `u` or `v` slope. Residual discriminants expand by hand to the displayed polynomials and re-digest to the stored SHAs. Ordinary charged tails are homogeneous of weight `12+i`, including target weights 15, 18, 20. That scaling, with positive rescaled Λ and the exact ordinary-source hypotheses, is sufficient to invoke the reviewed squarefree order-20 theorem on the residual open `4b^3+1≠0`. The overlap identity `s=b^{-3}=-4` and the opposite-axis preservation of `(p,c)` hold by elementary algebra. The two charts cover every noncentral directional case. No hidden moving-load, τ, field-extension, valuation, source-chart, or inverse-substitution mismatch was found |
| Smallest failing identity | none in the frozen V10 source, either harvest tree, either AWS stream, the hash-pinned V9/V8/V7/V6/V5/V4/toric/V1/charged sources, the recorded 48-term universal polynomial, the residual-discriminant expansions `-27s(s+4)` and `-27(4b^3+1)`, the overlap `s=b^{-3}=-4` on `4b^3+1=0`, or the opposite-axis identities for `(p,c)` |
| Smallest missing hypothesis for a stronger theorem | the central arc `a=h=0` identically, or any cell with nonpositive rescaled Λ; moving loads `k,μ,ν` in the V8 witness; another source chart or normal direction; a global landing or accessibility theorem; D1; or JC2 |
| Evidence tier | SHA-256 of the freeze chain and already-emitted AWS files; `cmp` of harvest copies against package-top source; `json` comparison of the two certificates after deleting `tag` and `order`; integer/rational arithmetic on every recorded universal exponent against the axis-coefficient formula, the V8 closed-corner, and the open-slope table; toric canonical digest of both residual discriminants; hand expansion of those discriminants, of `s=h/a^3=b^{-3}`, and of `(a,h)↦(p,c)` under `a'=-a`, `h'=h+4a^3`. No local Singular, Sage, msolve, Lean, Python algebra, compiler execution, charged reconstruct, or eight-row product replay |
| Reviewer / model | Grok 4.6 (xAI). Text-only algebraic-geometry / tropical-weight / source-custody referee |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Host | Darwin. V10 compiler, V9 compiler, V8 compiler, V7 compiler, V6 compiler, V5 compiler, V4 compiler, V1 compiler, toric compiler, charged reconstruct, Singular, and every solver were not run |

## What was and was not run

No local substantive computation was run. In particular this review did **not** execute `compile_weighted_two_chart_v10.py`, `compile_axis_covariance_v9.py`, `compile_hq_linear_filtered_lift_v8.py`, `compile_h2_qr_syzygy_lift_v7.py`, `compile_h_grade5_kernel_lift_v6.py`, `compile_h_qr_syzygy_lift_v5.py`, `compile_h_first_transport_v4.py`, `compile_q2_first_lift.py`, `compile_toric_blowup.py`, `independent_reconstruct.py`, Singular, Sage, msolve, Lean, or any other solver, and it did not re-multiply `sum F_i E_i` or reconstruct the unsubstituted eight rows. Hashes were checked with SHA-256 of file bytes. File identity was checked by byte comparison. Marker counts used exact-line matches. Git identity was read with `git rev-parse`. JSON fields were read with Python `json` (no algebra libraries). Canonical SHA-256 values of the residual discriminants were recomputed from the already-emitted toric triples `[[list(monomial), num, den], ...]` with `separators=(",", ":")`. Axis characters, closed corners, and open slopes of recorded monomials were scored by integer and `Fraction` arithmetic against the displayed formulae.

Charged freeze SHA-256, recomputed and matched:

```text
12ce6fe5b0b98666a62c283fd9ab3d5e84dad26041f85da5525a9cee941f1666  FREEZE.sha256
3d6300ced43c4d358f292538c2247655a7ad4f6f0fa674ada4cb27ed3cddaf03  RESULT.md
a4f5b5fa169115d586f4ed3cbe4fe8c6e1c2b78630f0e5e1f9645d44d859bbba  SOURCE_CLOSURE.sha256
53cf4b656c4415324a74862ec108b902ac8eade22733b2cb3a58cd3e447491e0  universal witness
25910f14424f0a021b00bf3d440b506b05aafc5c0980ee94beefe58608d5e12b  canonical certificate minus tag,order
a736793f95de15cd74b09ab6762ad56bdecee0b0dc6b9c65f569fc81d6a38dad  a-chart residual discriminant
dca78309aeb09bf43aa2990ece43dfcb6a05bf7d11489090582f4be5d3b7c19f  h-chart residual discriminant
```

V9 producer, V9 review, squarefree theorem, and squarefree review, recomputed:

```text
a061aea2bab3abcd9a8e88a3e86f18de233f46515cd2965bafa79ff1516642e2
  V9 RESULT.md
003788e80c359fa715d799f3fe66a35929b105c772d139865e87f123c1a9bda2
  V9 FREEZE.sha256
084cc8ddc9523c7208556bfb12d68e545a81221034e9ed108743127cc9805274
  V9 SOURCE_CLOSURE.sha256
55a27313370722e9ab255b34d3cb3d2ed592c47c32b5461397a8aa26a1a2a8a1
  compile_axis_covariance_v9.py
f81c5b054c2ff331176bd39005ad8f826b92efbfd5e16b1f7f20ae7dcbab7226
  V9 review (UNIT_AXIS_COVARIANCE_CONFIRMED)
1b6e629affdc5a73995e0ab2d7f051ad772d92f75bb61e67362782fcb8f5b4ac
  squarefree order-20 theorem (live file, SOURCE_CLOSURE, compiler, certificates)
6883ef76710176ae9e091249224730e3ff181fa76c66c767b53b26c770c101d5
  squarefree review (CONFIRMED)
```

The review-charge pin `squarefree 1b6e629affdc5a41c5abb7e06d63c8dba026bcc46df0a6f21bfed724589189c5` does **not** match the live theorem file. It appears only in the charge prompt. The live file, V10 `SOURCE_CLOSURE`, V10 compiler constant `SQUAREFREE_SHA`, both certificates, the squarefree review's target SHA, and the squarefree review prompt all agree on `1b6e629affdc5a73995e0ab2d7f051ad772d92f75bb61e67362782fcb8f5b4ac`. This is a prompt-side transcription error, not a package defect. Every other charge pin matched.

Promoted V8 theorem and its hostile review, recomputed and matched:

```text
2c3dbbd50089892197dd5ad5c0fb90776b5c2d2dea4ac2752f3b1a3218cc7d4c
  V8 review (HQ_LINEAR_FILTERED_LIFT_CONFIRMED)
b503f6a70c39c256ba27f27823d5788bf5787badc507efa3079433064eb142e3
  V8 promotion
ea38710ed3b11a58dac050430ba421dcec902def645f59da28c2d9418c60c247
  compile_hq_linear_filtered_lift_v8.py
```

Prerequisite V7 / V6 / V5 / V4 / toric / V1 / charged source, recomputed and matched:

```text
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

Every path listed in `FREEZE.sha256` recomputed and matched (19/19). Nested `SOURCE_CLOSURE.sha256` (20/20 from the case root) and both harvested `result.sha256` manifests (5/5 each) matched. Empty compiler stderr files are the empty-string digest `e3b0c442…`. Both rc files are the two-byte string `"0\n"`, digest `9a271f2a…`. Both harvested remote-tree manifests (42/42 entries each, including five AppleDouble sidecars) matched the files present in that harvest directory. Their SHAs match `RESULT.md` and `FREEZE.sha256`:

```text
de2a59a2afa835dee1d8e444ee3fd2a4f26f60b44b370ed08a4dfebf0fd1f852  Box03
98f5ec6348349a310a9ea4f03ba0087a84d7951f0ab12f26de23b9eb2d620e57  r6d
```

Read in full before the verdict: every file at
`cases/max12_912_order3_d1_triple_root_weighted_two_chart_v10_20260826/`
including both harvest trees; the hash-pinned V9 compiler `reconstruct` / `build_rows` / `fixed_multipliers` / `character_weight` / `transport`; the hash-pinned V8 promotion and review; the hash-pinned squarefree order-20 theorem and its review; the hash-pinned V4 `coefficient_images` / `embed`; the hash-pinned toric `NAMES` / `canonical` / `digest`; and the charged `build()` tail convention. Predecessor conclusions were recomputed, not inherited.

---

## Promotion

**Accept `FOR THE PINNED ORDINARY-TAIL EIGHT-ROW MODULE WITH FIXED LOADS k=ν=0, μ=2/3, AND THE CHARGED SOURCE independent_reconstruct.py AT 67343b56…, STARTING FROM THE REVIEWED V9 UNIVERSAL WITNESS OF SHA 53cf4b65… (THE CLEARED IDENTITY sum_i a^(11-i) F_i^(8)(hat) E_i = a^23 W^(8)(hat) WITH CLEARING POWER THREE) AND THE REVIEWED SQUAREFREE ORDER-20 THEOREM OF SHA 1b6e629affdc5a7399…, THE REGISTERED DUAL-AWS V10 RUNS PROVE THE FOLLOWING DIRECTIONAL WEIGHTED-BLOW-UP COVER OF THE TRIPLE-ROOT POINT (a,h)=(0,0) WITH wt(a)=1, wt(h)=3. IN THE a-CHART h=a^3 s, UNDER THE NORMALIZATION ell=wt(Λ)-wt(a)>0 AND THE REVIEWED V8 OPEN CELL u,v,T>0, EVERY ONE OF THE 48 UNIVERSAL TERMS HAS VANISHING AXIS COEFFICIENT e[a]-3+e[Λ]-20+e[ρ]+3e[h]+4e[q2]+5e[q1]+6e[q0]+7e[r2]+8e[r1]+9e[r0]; EVERY CLOSED-CORNER MARGIN (e[Λ]-20)+e[ρ]+5(q2+q1+q0)+(15/2)(r2+r1+r0) IS NONNEGATIVE WITH HISTOGRAM 32,11,5 AT 0, 5/2, 5; THE TWO DISTINGUISHED ZERO-MARGIN TERMS ARE COEFFICIENT-ONE a^3 Λ^20 AND COEFFICIENT-ONE a^3 Λ^20 τ; AND EACH OF THE OTHER 30 ZERO-MARGIN TERMS HAS A STRICTLY POSITIVE OPEN SLOPE IN AT LEAST ONE OF u,v,eta,T,H, IN FACT A STRICTLY POSITIVE u OR v EXPONENT. THIS IS THE FULL FINITE-AXIS CONE wt(h)≥3 wt(a) FOR THE LITERAL FIXED-LOAD V8 WITNESS, NOT A CHECK AT ONE h GRADE. THE a-CHART RESIDUAL CUBIC IS p=-3, c=2+s WITH EXACT DISCRIMINANT -27 s(s+4) OF SHA a736793f… AND DOUBLE-ROOT VALUES s=0 AND s=-4. IN THE h-CHART, AFTER ADJOINING A CUBIC ROOT WITH h=t^3 AND a=t b, THE RESIDUAL CUBIC IS z^3-3b^2 z+(2b^3+1) WITH EXACT DISCRIMINANT -27(4b^3+1) OF SHA dca78309…. ORDINARY CHARGED TAILS ARE HOMOGENEOUS OF WEIGHT 12+i, INCLUDING THE FIXED TARGETS OF WEIGHTS 15, 18, AND 20. UNDER POSITIVE RESCALED Λ, THAT SCALING TOGETHER WITH THE EXACT ORDINARY-SOURCE HYPOTHESES OF THE REVIEWED SQUAREFREE THEOREM (INCLUDING v(τ)>0) EXCLUDES THE OPEN RESIDUAL LOCUS 4b^3+1≠0. ON 4b^3+1=0 ONE HAS s=b^{-3}=-4, AND THE OPPOSITE-AXIS CHANGE a'=-a, h'=h+4a^3 PRESERVES p=-3a^2 AND c=2a^3+h, SO THAT EXCEPTIONAL DIRECTION IS THE a-CHART BOUNDARY s=-4 ALREADY COVERED ABOVE. THE TWO CHARTS TOGETHER COVER EVERY NONCENTRAL DIRECTIONAL CASE.`**

Do not promote this to: the central arc `a=h=0` identically; nonpositive rescaled Λ; moving loads in the V8 witness; another source chart; a global landing or accessibility theorem; D1; or JC2.

---

## Charge 1 — Custody, freeze, dual AWS, source closure, PID erratum, AppleDouble

**CONFIRMED. Every freeze entry recomputes. Both registered workers are fail-closed, hash-gated, empty-stderr, sub-cap, pre-GO, and source-closed against the package-root manifest. Opposite traversal orders return certificates that differ only in `tag` and `order`; deleting those two fields gives literally identical sorted JSON of SHA `25910f14424f0a021b00bf3d440b506b05aafc5c0980ee94beefe58608d5e12b`. The preserved PID-capture erratum and the AppleDouble sidecars affected neither source identity, nor pre-GO custody, nor execution.**

Required anchors, recomputed:

```text
3d6300ced43c4d358f292538c2247655a7ad4f6f0fa674ada4cb27ed3cddaf03  RESULT.md
12ce6fe5b0b98666a62c283fd9ab3d5e84dad26041f85da5525a9cee941f1666  FREEZE.sha256
a4f5b5fa169115d586f4ed3cbe4fe8c6e1c2b78630f0e5e1f9645d44d859bbba  SOURCE_CLOSURE.sha256
ac7be9dce50c261117c37c8ddba9c477b0560d8a6363acd4adc52a8dedabf3dd  aws_box03_forward/weighted_two_chart.json
9aaa0d14f93b168f12df60aa825bc58c3af03ad7e293cc47a54ebd60c96cf2ab  aws_r6d_reverse/weighted_two_chart.json
53cf4b656c4415324a74862ec108b902ac8eade22733b2cb3a58cd3e447491e0  universal_witness_sha256 (both JSON payloads)
```

Recomputed `FREEZE.sha256` entries, all matched (19/19). Harvest copies of compiler, worker, preregistration, AWS registration, and source closure are byte-identical to the package top on both hosts. Harvested `SOURCE_CLOSURE.sha256` is byte-identical to the top copy. Both `source.check` files are identical (`ac0f74c3…`) and print `OK` on all twenty paths; they are also byte-identical to both `prelaunch_source.check` files. The worker `cd`s to `$run` before `sha256sum -c SOURCE_CLOSURE.sha256`. The compiler locates V9 via `HERE.parents[1]/cases/…`, so `$run` is a `cases/`-child. Dual AWS both passed the sibling-path hash check. Treating `aws_box03_forward/` or `aws_r6d_reverse/` as a new source root would make those siblings invisible. That is not the charged root.

The compiler pins V9 at `V9_SHA=55a27313…` and refuses a non-matching file before import. V9 re-pins V8 at `ea38710e…`; V8 re-pins V7 at `a4500936…`; V7 re-pins V6 at `c7d9faed…`; V6 re-pins V5 at `8a963360…`; V5 re-pins V4 at `3bbf1ebf…`; V4 re-pins toric `c76ef85a…`, V1 `0385b0b1…`, and `independent_reconstruct.py` at `67343b56…`. The compiler additionally hash-checks the squarefree theorem, squarefree review, V8 promotion, and V8 review before algebra. Tag gates: worker `case` requires prefix `max12_912_order3_d1_triple_root_weighted_two_chart_v10_20260826T*`; compiler `require_aws` requires Linux, DMI vendor `Amazon EC2`, and tag prefix `max12_912_order3_d1_triple_root_weighted_two_chart_v10_`. Both refuse non-`forward`/`reverse` orders.

| Check | Box03 forward | r6d reverse |
|---|---|---|
| Public IP / harvested hostname | `98.80.65.144` / `ip-172-30-0-249` | `100.26.198.153` / `ip-172-30-0-45` |
| Tag | `…_v10_20260826T050400Z_box03_forward` | `…_v10_20260826T050400Z_r6d_reverse` |
| Worker PID | `165189` | `232475` |
| Caps | `memory_kib=8388608`, `timeout=1800`, `nice -n 10`; `ulimit -v 8388608` | same |
| Order | `forward` (`ell=1..8`, `F*E`) | `reverse` (`ell=8..1`, `E*F`) |
| Started / finished UTC | `2026-08-26T05:31:39Z` / `05:33:17Z` | `05:31:40Z` / `05:33:17Z` |
| GO released | `2026-08-26T05:33:05Z` | same |
| Compiler stdout SHA | `cbf44d48…` | `6b1d0d06…` |
| Certificate SHA | `ac7be9dc…` | `9aaa0d14…` |
| RSS / swap / exit | 22368 KiB / `Swaps: 0` / 0 | 21932 KiB / `Swaps: 0` / 0 |
| Pre/post `free` swap | `0B` / `0B` | `0B` / `0B` |
| Elapsed | 11.87 s | 11.93 s |
| PASS markers, each once | `PASS_WEIGHTED_TWO_CHART_V10`, `PASS_REMOTE_WORKER` | same |
| `FAIL_` / `REFUSED` / `FAILED` | none; stderr empty; no `REFUSED`/`FAILED` files | none; stderr empty; no `REFUSED`/`FAILED` files |

`AWS_LAUNCH_METADATA.md` records a live fleet audit at `2026-08-26T05:28:21Z` with both workers `WAITING_GO`, neither run directory containing `GO`, `DONE`, or `FAILED`, and source-closure manifest SHA `a4f5b5fa…` matching the frozen file. Both `GO` sentinels were released at exactly `2026-08-26T05:33:05Z` and are empty. Worker start UTC precedes GO; finish UTC is 12 s after GO, matching the 11.87 s compile plus the post-GO source-hash check. Harvest manifests were created at `2026-08-26T05:34:01Z`. No `REFUSED` or `FAILED`.

The two JSON files are **not** byte-identical. Their key sets are equal (13 keys). The only value differences are the two preregistered custody fields `tag` and `order`. Deleting those fields and dumping with `sort_keys=True, indent=2` plus a trailing newline yields one 33109-byte blob of SHA

```text
25910f14424f0a021b00bf3d440b506b05aafc5c0980ee94beefe58608d5e12b
```

on both hosts, matching `RESULT.md` and the charged semantic-equality SHA. Compiler stdout differs only in the preregistered `ORDER=` line and the certificate SHA of the tagged JSON; the algebraic metric block is identical:

```text
STATUS=WEIGHTED_TWO_CHART_DIRECTIONAL_COVER_EXACT_CONDITIONAL_V9_REVIEW
A_CHART_FACE_COUNT=30
A_CHART_DISCRIMINANT_SHA256=a736793f95de15cd74b09ab6762ad56bdecee0b0dc6b9c65f569fc81d6a38dad
H_CHART_DISCRIMINANT_SHA256=dca78309aeb09bf43aa2990ece43dfcb6a05bf7d11489090582f4be5d3b7c19f
PASS_WEIGHTED_TWO_CHART_V10
```

Worker fail-closed conditions, all met on both hosts: `rc=0`, empty stderr, exactly one `PASS_WEIGHTED_TWO_CHART_V10` endpoint. Caps 8 GiB / 1800 s; RSS is 22 MiB; elapsed is 12 s.

Source payload was byte-identical on both hosts (`6c648fa7…  source_payload.tgz`). Prelaunch Python is `3.12.3` on both; remote `py_compile` produced empty stdout and empty stderr. `prelaunch_manifest.sha256` on both hosts is exactly the frozen source-closure digest `a4f5b5fa…`. Registration tags, job directories, caps, nice 10, and the untouched r6d Singular worker PID `185517` match `AWS_REGISTRATION.md` and `AWS_LAUNCH_METADATA.md`. The local macOS fail-closed control at `2026-08-26T05:37Z` is a placement check, not algebra: `require_aws` exits `REFUSE_NON_LINUX` before loading V9. This review did not re-execute that control; the source gate is the displayed `platform.system() != "Linux"` branch.

### PID-capture erratum

The first orchestration-side background-PID capture expanded to the literal value `0`. Both harvest trees preserve that value as `worker.launch.pid.initial_zero` (two-byte `"0\n"`, digest `9a271f2a…`, same as `compiler.rc`) and a one-line erratum. Each waiting worker had already self-recorded `pid=$$` in `worker.metadata` (`165189` Box03, `232475` r6d) under `WAITING_GO` before GO. `worker.launch.pid` was restored from that metadata and matches the RESULT table. The compiler never reads the launch-PID file. Computational state did not depend on the bad field. Pre-GO custody is the self-recorded metadata plus the source-closure check that runs only after GO. The erratum is honest and is not a source, pre-GO, or execution defect.

### AppleDouble sidecars

Both remote-tree manifests list five `._*` AppleDouble files, each 163 bytes, all of SHA `7b7e703638a2c8654bbaeecc7148e1717958bb825d0f1b13593ac3c3cb748c6c`. They sit next to `AWS_REGISTRATION.md`, `PREREGISTRATION.md`, `SOURCE_CLOSURE.sha256`, `compile_weighted_two_chart_v10.py`, and `remote_worker.sh`. They are **not** named by `SOURCE_CLOSURE.sha256` or `FREEZE.sha256`. The compiler imports only the hash-pinned `.py` files through explicit paths. Linux tar reported unsupported provenance xattr while extracting them; `AWS_LAUNCH_METADATA.md` records this. After extraction, every charged source file passed its registered SHA (prelaunch and post-GO `source.check` both `OK` on all twenty paths, both hosts). The sidecars did not affect source identity, pre-GO custody, or execution.

---

## Charge 2 — Literal V9 witness, axis formula, clearing three, `ell>0`, corners, open slopes

**CONFIRMED. V10 reconstructs the reviewed 48-term V9 universal witness of SHA `53cf4b65…` from the frozen V8–V1 ancestry and charged ordinary tails, opposite multiply order. Clearing power is fail-closed at 3. With `wt(a)=1`, `wt(h)=3`, the displayed axis-coefficient formula vanishes on 48/48 recorded terms. Every closed-corner margin is nonnegative, with histogram `32,11,5` at `0,5/2,5`. All open-slope coordinates are nonnegative integer exponents in `[0,5]`. Precisely 30 zero-margin non-target terms have a strictly positive open slope; in fact each of those 30 has a strictly positive `u` or `v` exponent. Python truthiness was not trusted.**

Construction, from the hash-pinned V10 compiler, which loads the hash-pinned V9 compiler, which loads the hash-pinned V8/V7/V6/V5/V4/toric/V1 chain:

1. `t.load_charged_source().build()["tails"]` is the eight negative Laurent tails of `independent_reconstruct.py` at `67343b56…`, same charged ordinary-tail source as the reviewed V9/V8 lifts.
2. `moving_rows = v9.build_rows(t, tails, True)` is the V9 substitution at `p=-3a^2`, `c=2a^3+h`, including the baked row-3 load `(2/3)Λ^{15}` and the row-8 target `Λ^{20}(1+τ)`, with row-6 `ν` unsubtracted.
3. `fs = v9.fixed_multipliers(...)` is the literal V8 combination (V1 multipliers plus q2 corrections plus G1, D2, and the V8 columns `F1 -= h q1/36`, `F2 -= h q0/72`).
4. Deficits `character_weight(m)-(8-ell)` are scored on every fixed-multiplier monomial. V10 refuses any clearing other than 3. Dual AWS both exited 0. This is the V9 least-common-negative-axis-character theorem, re-checked, not a dimensional guess. V9 independently listed the 26-element deficit list with maximum 3, achieved on four monomials; that listing was not replayed here and is used only as already-reviewed ancestry.
5. Cleared multipliers are `transport(fs[ell], 3+(8-ell)) = transport(fs[ell], 11-ell)`. Universal sum is `F*E` forward and `E*F` reverse, with `ell` running `1..8` or `8..1`. Dual AWS both fail-close on `digest(universal)=53cf4b65…`.
6. Row covariance is re-checked: `transport(fixed_rows[ell], 12+ell) == moving_rows[ell]` for `ell=1..8`. Dual AWS both exited 0.

This review did not replay the eight-row product. The dual-traversal dictionary equality on SHA `53cf4b65…`, the V9 confirmation of that same digest as the cleared identity `sum_i a^(11-i) F_i(hat) E_i = a^{23} W^(8)(hat)`, and the 48/48 character constraint `e[a]+char(rest)=23` on the stored records are the custody that the recorded polynomial is that product.

Axis-coefficient formula, charged, on every recorded term:

```text
axis = e[a]-3 + e[la]-20 + e[rho]
     + 3 e[h] + 4 e[q2] + 5 e[q1] + 6 e[q0]
     + 7 e[r2] + 8 e[r1] + 9 e[r0].
```

This is `(e[a] + 3 e[h] + 4 e[q2] + 5 e[q1] + 6 e[q0] + 7 e[r2] + 8 e[r1] + 9 e[r0] + e[la] + e[rho]) - 23`. V9 already proved every universal term has total character 23 under `wt(a)=1`, `wt(h)=3`, `wt(q2)=4`, …, `wt(Λ)=1`, `wt(ρ)=1`, `wt(τ)=0`. Independently of that product replay, the 48 stored exponent vectors satisfy `e[a]+char(rest)=23` (48/48) and therefore `axis=0` (48/48). Stored `axis_coefficient` matches the formula (48/48). Extra toric slots `p,c,x,y,k,μ,ν` are zero on every term. `ρ` is zero on every term. Distinguished terms:

```text
+1  a^3 Λ^20          axis 0, corner 0, all open slopes 0
+1  a^3 Λ^20 τ        axis 0, corner 0, T=1
```

Normalization `ell=wt(Λ)-wt(a)>0`. This is the residual weight of `Λ̂=Λ/a`. The V8 unique-least-term theorem is a statement in units of `L=wt(Λ̂)`. If `ell=0` then `Λ̂` is a unit and the residual is not coefficient-infinity; if `ell<0` the residual Λ pole is not a regular residual arc. Both are outside the charged cell. On the a-chart wall `h=a^3 s` with `s` of weight 0, the physical weight splits as an axis piece (the displayed axis coefficient, already zero) plus an `ell`-piece (the closed corner below). Positive `ell` makes the V8 filtration on the hats a genuine coefficient-infinity filtration and does not reorder the closed axis.

Closed corner, charged:

```text
corner = (e[la]-20) + e[rho]
       + 5 (e[q2]+e[q1]+e[q0])
       + (15/2) (e[r2]+e[r1]+e[r0]).
```

This is the V8 closed cell `α=15/2`, `β=δ=5`, `η=0` for the hats, scored relative to `Λ^{20}`. Stored `ell_corner` matches (48/48). Histogram of the 48 values:

```text
margin 0:   32 terms,
margin 5/2: 11 terms,
margin 5:    5 terms.
```

Zero negative margins. The 32 zero-margin terms are the target, the positive `τ` split, and 30 others. `a`-power histogram of the 48 terms is the V9 histogram `{0:17, 2:10, 3:11, 4:5, 5:3, 6:1, 7:1}`.

Open slopes, charged:

```text
u = e[q1]+e[q0],   v = e[q2],   eta = e[h],   T = e[tau],   H = e[rho].
```

Stored `open_slopes` match (48/48). Range of recorded values, as integers:

```text
u in [0,4],  v in [0,5],  eta in [0,2],  T in [0,1],  H = 0 identically.
```

No negative exponent occurs. Python `any(slopes.values())` on this set is equivalent to positivity, but that equivalence was not assumed: every slope was checked to be a nonnegative integer, and each of the 30 non-target zero-margin terms was checked to have at least one strictly positive coordinate. Face-term slope support:

```text
('u',): 6,   ('v',): 6,   ('u','v'): 8,
('eta','u'): 3,   ('eta','v'): 1,   ('eta','u','v'): 6.
```

Zero of the 30 rely only on `eta`. Zero rely only on `T` or `H`. All 30 have `u>0` or `v>0`. This is the same 30-term V8 equality face, now re-scored in the weighted a-chart: the V8 promotion already recorded that every non-target equality-face term has positive `u` or `v` slope. In the registered open cell `u,v,T>0` (with `eta,H` optional), every non-target face term is strictly above the target, and the split `a^3 Λ^{20} τ` is strict for `T>0`. `H=0` identically is the V9 fact that no recorded term carries `ρ`; it is not a missing slope.

Because the axis coefficient vanishes on the full 48-term polynomial, this is not a check at one numerical grade of `a` or `h`. It is the associated-graded statement of the homogeneous identity on the cone `wt(h)≥3 wt(a)`.

---

## Charge 3 — a-chart residual cubic, discriminant, whole-cone claim, V8/V9 hypotheses

**CONFIRMED. Residual cubic `p=-3`, `c=2+s`. Discriminant identity `-27 s(s+4)` holds by hand and re-digests to SHA `a736793f…`. Double-root values are `s=0` and `s=-4`. Together with Charge 2 this is the whole finite-axis cone `wt(h)≥3 wt(a)` for the literal fixed-load V8 witness, not one h grade.**

Chart substitution `h=a^3 s` into the V9 moving chart `p=-3a^2`, `c=2a^3+h`:

```text
p / a^2 = -3,
c / a^3 = 2 + s.
```

The residual depressed cubic is `z^3 - 3 z + (2+s)`. Discriminant `-4 p^3 - 27 c^2` at these values:

```text
-4 (-3)^3 - 27 (s+2)^2
  = 108 - 27 (s^2 + 4s + 4)
  = 108 - 27 s^2 - 108 s - 108
  = -27 s (s+4).
```

The compiler constructs `-4 p^3 - 27 c^2` from `p=-3`, `c=2+s` (s stored in the toric `x` slot) and requires dictionary equality with `-27 s(s+4)`. Dual AWS both exited 0. Stored expanded polynomial, two terms, `x` at NAMES index 4:

```text
-108 x  +  (-27) x^2.
```

Hand expansion: `-27 s(s+4) = -108 s - 27 s^2`. Equal. Recomputed toric digest from the stored triples with `separators=(",", ":")`:

```text
a736793f95de15cd74b09ab6762ad56bdecee0b0dc6b9c65f569fc81d6a38dad
```

matching both JSON payloads, both stdout lines, and `RESULT.md`. Double-root values: `-27 s(s+4)=0` iff `s=0` or `s=-4`. At `s=0` the residual is `z^3-3z+2=(z-1)^2(z+2)`. At `s=-4` it is `z^3-3z-2=(z+1)^2(z-2)`. Stored `double_root_values=["s=0","s=-4"]`.

Whole-cone versus one h grade. The 48-term analysis is on the V9 universal polynomial, which V9 already proved is an exact identity, not an `h`-truncation (maximum `h` is 2; character-homogeneous of weight 23). Axis coefficients vanish on every term, so the weighted `a`-valuation with `wt(h)=3` equals the target valuation independently of a numerical grade. Closed corners are nonnegative independently of a numerical grade. Face terms lift in the open cell independently of a numerical grade. The residual cubic/discriminant is a separate exact identity about the chart, identifying the double-root walls `s=0` and `s=-4` inside that cone. Together they are the full finite-axis-valuation cone `wt(h)≥3 wt(a)` for this witness.

Hypotheses used from V8/V9, and only these:

- Frozen loads `k=ν=0`, `μ=2/3`, charged ordinary tails at `67343b56…`.
- V9 moving chart `p=-3a^2`, `c=2a^3+h`, Jacobian `-6a` on `D(a)` not needed for the residual-cubic algebra once the chart is granted.
- V9 eight row identities and clearing power three, giving the 48-term polynomial of SHA `53cf4b65…` with distinguished terms coefficient-one `a^3 Λ^{20}` and `a^3 Λ^{20} τ`.
- V8 unique-least-term cell: `α=15/2`, `β=5+u`, `δ=5+v`, `η=wt(h)/L`, unique least term `Λ^{20}` iff `η≥0`, uniformly in `u,v,T>0`; all 30 non-target equality-face terms have positive `u` or `v` slope.
- Character table `Λ:1, τ:0, ρ:1, h:3, q2:4, q1:5, q0:6, r2:7, r1:8, r0:9`.
- New for V10: `wt(a)=1` and `ell=wt(Λ)-wt(a)>0`. V9 explicitly excluded `v(a)>0`; that exclusion is the present cell, not a contradiction.

The residual cubic identities do not need the 48-term witness. The cone claim does.

---

## Charge 4 — h-chart residual cubic, ordinary weights, squarefree invocation

**CONFIRMED. Residual cubic `z^3-3b^2 z+(2b^3+1)` and discriminant `-27(4b^3+1)` hold by hand and re-digest to SHA `dca78309…`. Frozen charged tails are homogeneous of weight `12+i`, including target weights 15, 18, 20. That scaling covariance, with positive rescaled Λ and the exact ordinary-source hypotheses of the reviewed squarefree theorem, is sufficient to invoke that theorem on the residual open `4b^3+1≠0`. No hidden moving-load, τ, field-extension, valuation, source-chart, or inverse-substitution mismatch.**

Substitution `h=t^3`, `a=t b` into `p=-3a^2`, `c=2a^3+h`:

```text
p = -3 t^2 b^2,     p / t^2 = -3 b^2,
c = 2 t^3 b^3 + t^3 = t^3 (2 b^3 + 1),     c / t^3 = 2 b^3 + 1.
```

The residual cubic is `z^3 - 3 b^2 z + (2 b^3 + 1)`. Discriminant:

```text
-4 (-3 b^2)^3 - 27 (2 b^3 + 1)^2
  = 108 b^6 - 27 (4 b^6 + 4 b^3 + 1)
  = 108 b^6 - 108 b^6 - 108 b^3 - 27
  = -27 (4 b^3 + 1).
```

Stored expanded polynomial, `y` at NAMES index 5 as `b`:

```text
-27  +  (-108) y^3.
```

Hand expansion: `-27(4b^3+1)=-108 b^3-27`. Equal. Recomputed toric digest `dca78309aeb09bf43aa2990ece43dfcb6a05bf7d11489090582f4be5d3b7c19f`, matching both JSON payloads, both stdout lines, and `RESULT.md`. Physical discriminant is `Δ=-27 h(4a^3+h)=-27 t^6 (4b^3+1)= t^6 Δ_res`, so they vanish together off `t=0`.

Ordinary homogeneity, from the frozen charged tails, fail-closed on both hosts before any residual cubic is built:

```text
wt(a_i)=9-i (i=0..7),  wt(k)=6,
row ell has weight {12+ell}.
```

Certificate `ordinary_homogeneity={1:13,2:14,3:15,4:16,5:17,6:18,7:19,8:20}`. Target-weight bridge is fail-closed: rows 3, 6, 8 have weights 15, 18, 20. This is the same checksum V9 licensed as a hypothesis of the row identities, now used as the scaling bridge for the eight ordinary equations. Dual AWS both exited 0. This review did not replay `independent_reconstruct.py`; the dual-AWS fail-closed checksum plus the V9 confirmation of the same weights is the custody.

### Sufficiency of the scaling bridge

The reviewed squarefree theorem (live SHA `1b6e629affdc5a7399…`, verdict CONFIRMED) states: in the ordinary isotrivial chart of the charged source, with `Λ=τ^3 ρ`, `kbar=Λ^6 k`, and `r_ell=Λ^{12+ell} γ_ell` for `γ_3=μ`, `γ_6=ν`, `γ_8=1+τ`, no formal or Puiseux arc whose projective common-cubic centre `K_0=z^3+p_0 z+c_0` has `Δ_0≠0` can satisfy the eight equations. It is uniform in `k,μ,ν` including zero loads, and includes Puiseux and finite constant-field extensions. Inverse substitution of `f` for `K` contaminates only at weight 21. The affine origin `(p,c)=(0,0)` is not a projective centre; the projective centre is the leading form in weighted `P(2,3)`.

After `f(z) ↦ t^{-9} f(t z)`, ordinary homogeneity of weight `12+i` sends each physical row to `t^{12+i}` times the residual row, and each target `Λ^{12+i} γ_i` to `t^{12+i} Λ̂^{12+i} γ_i` with `Λ̂=Λ/t`. The residual equations are therefore the ordinary loaded equations in residual coordinates. Positive rescaled Λ, `ell=wt(Λ)-wt(t)>0`, makes the residual arc a coefficient-infinity arc, renormalizable to `v(Λ̂)=1`. The residual cubic is the projective centre of the physical arc approaching `(a,h)=(0,0)`. When `4b_0^3+1≠0` that centre is squarefree, and the squarefree theorem excludes the arc.

That is sufficient. The V9 combination polynomial is not required for this open; it is the tool for the double-root walls. The V9 covariance identity localizes at `a` and is not the bridge used here. The bridge is ordinary source homogeneity, which V10 checks and which does not localize at `a`.

### Hidden-mismatch search

- **Moving load.** Squarefree is uniform in the constants `k,μ,ν`. V8 specializes them to `k=ν=0`, `μ=2/3`, a subcase. Residual `(p,c)` may move with the series `b`; squarefree allows a moving cubic. No mismatch. A moving-load theorem for the a-chart walls remains outside scope because those walls use the V8 combination.
- **τ.** `τ` has character 0, so `τ̂=τ`. Squarefree requires `v(τ)>0` so that `v(1+τ)=0` with leading coefficient 1. V10 states `ell>0` and inherits `v(τ)>0` from the invoked theorem and from the V8 open cell `T>0`. There is no extra `t` factor on row 8. No mismatch.
- **Field extension.** Adjoining `t` with `t^3=h` is a ramified Puiseux extension when 3 does not divide `v(h)`. Squarefree includes Puiseux. The projective centre in `P(2,3)` is well-defined without extracting `t` in the original DVR; the h-chart is a convenience. On `4b^3+1=0`, adjoining a cube root of `-1/4` is a constant-field extension at a double-root point, where squarefree is not invoked. No mismatch.
- **Valuation.** `ell>0` is exactly `v(Λ)>v(t)`. Inverse-substitution contamination at physical weight 21 scales to residual weight 21 and stays off the order-20 cutoff. No mismatch.
- **Source chart.** Same charged ordinary tails `67343b56…` as squarefree and V8/V9. Scaling `f(z)↦ t^{-9} f(t z)` is the ordinary weighted homogeneity of that chart, not a different chart. No mismatch.
- **Inverse substitution.** Squarefree Charge 5: replacing the inverse of `K` by the inverse of `f` changes coefficients only at valuation ≥21. Homogeneous scaling preserves the cutoff. No mismatch.
- **`b=0`.** Residual cubic `z^3+1`, discriminant `-27≠0`, squarefree. This is the axis `p=0`, `c≠0`, which squarefree includes directly. V9's `D(a)` localization is not needed.

The compiler hardcodes the residual `p,c` rather than substituting `a=tb`, `h=t^3` and dividing. The substitution is the two-line identity above and is not a failing identity.

---

## Charge 5 — Overlap, opposite axis, coverage, `s=0` / `s=-4` / cubic-root

**CONFIRMED. On `4b^3+1=0` one has `s=b^{-3}=-4`. The opposite-axis change `a'=-a`, `h'=h+4a^3` preserves `p` and `c`. The two charts cover every claimed noncentral directional case. Neither `s=0`, nor `s=-4`, nor the cubic-root base extension leaves an unacknowledged gap.**

Overlap. On the h-chart with `b≠0`,

```text
s = h / a^3 = t^3 / (t^3 b^3) = b^{-3}.
```

The locus `4b^3+1=0` forces `b^3=-1/4≠0`, hence `b≠0` and `s=(-1/4)^{-1}=-4`. The compiler checks the tautology `-4b^3-1=-(4b^3+1)` rather than this identity; the identity is elementary and holds. Dual AWS both exited 0 on the tautology; the mathematical claim is the displayed algebra, not that tautology.

Opposite axis. `p=-3a^2` depends on `a^2`, so `a'=-a` leaves `p` unchanged:

```text
-3 (-a)^2 = -3 a^2.
```

For `c`:

```text
2 (-a)^3 + (h + 4 a^3) = -2 a^3 + h + 4 a^3 = 2 a^3 + h.
```

The compiler writes `p_original=p_opposite=-3a^2` without substituting (a tautology whose comment is the real identity) and does substitute on `c`. Both identities hold by hand. At `s=-4`, `h=-4a^3`, so `h'=0` and `a'=-a`: this is the opposite double-root axis, already inside the a-chart tropical analysis (Charge 2) and, after the unit-axis change, inside the reviewed V9 theorem on `D(a)` at `h=0`.

Coverage of noncentral directions, with `v` a rank-one valuation:

- `v(h)≥3 v(a)` and `a` not identically zero: a-chart, `s` regular. Includes the wall `v(s)=0` and the interior `v(s)>0`.
- `v(h)<3 v(a)` and `h` not identically zero: then `v(b)=v(a)-v(h)/3>0`, so `b` is regular and vanishes; h-chart interior, toward the h-axis.
- `h≡0`, `a≢0`: `s=0`, a-chart wall, V8/V9 double-root axis.
- `a≡0`, `h≢0`: `b=0`, h-chart, residual `z^3+1` squarefree, excluded by Charge 4.
- `a≡h≡0`: central arc, excluded by firewall.

If `b` poles then `v(s)>0` and one is in the a-chart interior. If `s` poles then `v(b)>0` and one is in the h-chart interior. There is no direction with both `s` and `b` infinite.

`s=0`. Double-root residual `z^3-3z+2`. Squarefree does not apply. Charge 2 applies: on this wall `eta` does not lift, but every non-target face term has positive `u` or `v`, so the V8 open cell still makes the target unique least. Acknowledged, not a gap.

`s=-4`. Opposite double-root. Squarefree does not apply. Charge 2 applies uniformly for `s` a unit, and the opposite-axis change identifies the direction with `h'=0`. Acknowledged overlap, not a gap.

Cubic-root base extension. Adjoining `t` with `t^3=h` is stated in `RESULT.md`. It is Puiseux, already in the squarefree theorem's scope. It is not required to name the projective centre in `P(2,3)`. It does not create an extra double-root or an extra squarefree component. The further cube root of `-1/4` on the exceptional divisor is a constant-field point of the double-root locus already mapped to `s=-4`. No unacknowledged gap.

---

## Charge 6 — Exact identities versus consequence; strongest licensed theorem; firewall

**CONFIRMED. The exact identities are the 48-term reconstruction, the axis/corner/slope arithmetic, both residual discriminants, ordinary weights `12+i`, the overlap `s=b^{-3}=-4`, and the opposite-axis preservation of `(p,c)`. The mathematical consequence is the directional weighted-blow-up cover stated in the Promotion paragraph. No identity failed. The firewall is the frozen one.**

Exact identities (dual AWS, opposite order, plus hand algebra):

1. Reconstruction of the V9 universal polynomial of SHA `53cf4b65…` from frozen V8–V1 source, clearing power exactly 3, eight row-covariance identities.
2. Axis coefficient 0 on 48/48 terms; closed-corner histogram `32,11,5`; 30 non-target zero-margin terms with nonnegative integer open slopes, each with `u>0` or `v>0`.
3. a-chart residual discriminant `-27 s(s+4)`, SHA `a736793f…`; double roots `s=0,-4`.
4. h-chart residual discriminant `-27(4b^3+1)`, SHA `dca78309…`; ordinary weights `12+i` including 15, 18, 20.
5. `4b^3+1=0 ⇒ s=b^{-3}=-4`; `a'=-a`, `h'=h+4a^3` preserves `p` and `c`.

Mathematical consequence, using the reviewed V8 unique-least-term theorem, the reviewed V9 unit-axis covariance, and the reviewed squarefree order-20 theorem, under `ell>0` and `v(τ)>0`:

- On the a-chart cone `wt(h)≥3 wt(a)`, the combination has unique least term a unit times `Λ^{20}` in the registered open cell, so the eight-row module has no solution there.
- On the h-chart open `4b^3+1≠0`, the residual centre is squarefree, so the eight equations have no coefficient-infinity solution.
- On the remaining h-chart divisor `4b^3+1=0`, the direction is the a-chart wall `s=-4`, already obstructed.

Strongest licensed theorem: the Promotion paragraph. Smallest missing hypothesis for any stronger theorem: a statement at the closed point `a=h=0` identically, or at nonpositive rescaled Λ. Next after that: moving V8 loads; another source chart; global landing/accessibility; D1; JC2.

Smallest failing identity: none.

### Firewall (enforced)

Admissible:

- Frozen ordinary common-cubic source, fixed V8 loads `k=ν=0`, `μ=2/3`, charged reconstruct `67343b56…`.
- Positive rescaled Λ and `v(τ)>0`.
- Reviewed V9 48-term identity, reviewed V8 unique-least-term cell, reviewed squarefree order-20 theorem.
- Directional cover of the weighted blow-up of `(a,h)=(0,0)` with weights `(1,3)`, excluding the central arc.

Not admissible, and not claimed by the frozen firewall string
`frozen ordinary common-cubic source only; requires V9 review and positive rescaled Lambda; central a=h=0 arc, moving loads in the V8 witness, other source charts, D1 and JC2 remain open`
and `RESULT.md` §Firewall:

- the central arc `a=h=0` identically;
- nonpositive rescaled Λ (`ell≤0`);
- moving loads `k,μ,ν` in the V8 witness, or a theorem that those coordinates scale;
- another source chart, another passport, or another normal direction;
- a global landing, accessibility, or rational-section theorem;
- D1 or JC2;
- an unlocalized claim that `Λ^{20}` itself is an initial monomial at `a=0` as a polynomial (seventeen universal terms have `a`-exponent 0; that is the V9 firewall, still in force);
- use of the squarefree global-support corollary (`H≠(1) ⇒` reduced projective support is the double-root point); V10 invokes only the order-20 obstruction on the residual squarefree open.

The producer status `WEIGHTED_TWO_CHART_DIRECTIONAL_COVER_EXACT_CONDITIONAL_V9_REVIEW` is discharged: the V9 review is `UNIT_AXIS_COVARIANCE_CONFIRMED` at SHA `f81c5b05…`, pinned in `FREEZE.sha256` as later external ancestry. The V10 endpoint is no longer provisional.

---

## Nits, not defects

1. The review-charge pin of the squarefree theorem is `1b6e629affdc5a41c5…`; the live theorem, SOURCE_CLOSURE, compiler, certificates, and squarefree review are `1b6e629affdc5a7399…`. Prompt transcription error. No source repair.
2. Compiler overlap check is the tautology `-4b^3-1=-(4b^3+1)`. The claimed identity `s=b^{-3}=-4` is elementary and was checked by hand. No source repair.
3. Compiler opposite-axis `p` check writes the same polynomial twice; the comment `-3(-a)^2=-3a^2` is the identity. The `c` check does substitute. No source repair.
4. Residual cubics are hardcoded rather than obtained by substituting the chart into `p=-3a^2`, `c=2a^3+h` and dividing. The two-line substitutions were checked by hand. No source repair.
5. Face positivity in the compiler is `any(slopes.values())`. Independently, every slope is a nonnegative integer and every face term has a strictly positive `u` or `v`. No source repair.
6. `H=e[ρ]` is identically zero on the 48 terms. The open-cell list includes it; it never fires. V9 already recorded that no term carries `ρ`.
7. `FREEZE.sha256` is a 19-entry result pin, not a complete harvest pin. Dual `remote_tree_manifest.sha256` values are in the freeze and were checked 42/42 against the harvest trees. Pre-GO source identity is `SOURCE_CLOSURE.sha256`.
8. Five identical AppleDouble sidecars are in both remote-tree manifests and in the local harvest. They are not in SOURCE_CLOSURE, were not imported, and did not change any charged SHA.
9. Local harvest directories contain `__pycache__/compile_weighted_two_chart_v10.cpython-312.pyc`, absent from the remote-tree manifests. Bytecode of the frozen compiler; not a source file.
10. r6d `free` shows 162 GiB used vs Box03 45 GiB; swap is zero on both, and this job's RSS is 22 MiB under an 8 GiB `ulimit -v`. Registration leaves unrelated r6d work untouched.

No source or certificate repair is required.

WEIGHTED_TWO_CHART_V10_CONFIRMED
