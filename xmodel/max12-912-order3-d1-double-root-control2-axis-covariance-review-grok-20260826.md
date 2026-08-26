# Hostile text-only review — D1 V8 unit-axis covariance V9

| Field | Value |
|---|---|
| Claim under review | Exact unit-axis / fixed-load covariance of the promoted V8 eight-row combination: row identities `E_i(a,h,Q,R,Λ,ρ,τ)=a^(12+i) E_i(1,h/a^3,q2/a^4,q1/a^5,q0/a^6,r2/a^7,r1/a^8,r0/a^9,Λ/a,ρ/a,τ)` at `p=-3a^2`, `c=2a^3+h`; least common negative axis character of the literal V8 multipliers exactly `-3`; cleared polynomial identity `sum_i a^(11-i) F_i^(8)(hat) E_i(a,h,Q,R)=a^23 W^(8)(hat)`; discriminant `Δ=-27h(4a^3+h)`; Jacobian `-6a`; transport of the V8 unique-least-term theorem on `D(a)` |
| Overall verdict | **UNIT_AXIS_COVARIANCE_CONFIRMED**. Dual AWS encodings emit certificates that differ only in `tag` and `order`; deleting those fields gives canonical sorted SHA `1375bd72…`. The reconstructed V8 identity is the reviewed 48-term polynomial (SHA `e549fd68…`) with `h=0` slice `W'` (SHA `ddb451c4…`). Ordinary source tails are homogeneous of weight `12+i`. All eight substituted rows, including the baked row-3 load `(2/3)Λ^15` and the row-8 target `Λ^20(1+τ)` and with row-6 `ν` unsubtracted, satisfy the displayed covariance as dictionary identities. Independently listing every V8 multiplier monomial yields axis deficits whose maximum is exactly `3`, achieved on four monomials, so clearing power three is sufficient and minimal. After clearing, both sides of the combination identity are one 48-term polynomial of SHA `53cf4b65…`. Zeroing `a` recovers the V8 records coefficientwise (48/48). Every universal term has `a`-exponent `23-char(rest)`. Distinguished terms are coefficient-one `a^3 Λ^20` and coefficient-one `a^3 Λ^20 τ`. This is a polynomial identity in `a,h,Q,R,Λ,τ`, not a congruence and not an `h` truncation. `Δ=-4p^3-27c^2` expands to `-27h^2-108 a^3 h`. The Jacobian of `(a,h)↦(p,c)` is `-6a`. On `D(a)` with `wt(a)=0`, multiplication by the unit `a^3` (as an element of the localized ring, not as a polynomial GCD of the 48 terms) and the weighted coordinate automorphism transport the V8 monomial-initial obstruction to the normalized hat variables. Etale/`D(a)` descent transfers nonexistence and the unit-initial-ideal conclusion to the smooth discriminant. Positive axis valuation is excluded |
| Smallest failing identity | none in the frozen V9 source, either harvest tree, either AWS stream, the hash-pinned V8/V7/V6/V5/V4/toric/V1/charged sources, the recorded 48-term universal polynomial, or the hand lemmas `Δ=-27h(4a^3+h)` and `Jac=-6a` |
| Smallest missing hypothesis for a stronger theorem | moving loads `k,μ,ν`; the triple-root point `a=0` or any cell with `v(a)>0`; the other discriminant factor `4a^3+h=0`; another source chart or normal direction; a formal neighbourhood; the whole double-root fan; D1; or JC2 |
| Evidence tier | SHA-256 of the freeze chain and already-emitted AWS files; `cmp` of harvest copies against package-top source; `json` comparison of the two certificates after deleting `tag` and `order`; integer/rational arithmetic on every recorded universal exponent against the preregistered character table; dictionary comparison of the `a=1` slice to the frozen V8 48-term records; independent character arithmetic on every V8 multiplier monomial; hand expansion of `Δ` and of `det D(p,c)/D(a,h)`. No local Singular, Sage, msolve, gfan, Lean, Python algebra, compiler execution, charged reconstruct, or eight-row product replay |
| Reviewer / model | Grok 4.6 (xAI). Text-only algebraic-geometry / commutative-algebra / source-custody referee |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `574e873d4753b57dbaeb0fb83e320fbef3694724` |
| Host | Darwin. V9 compiler, V8 compiler, V7 compiler, V6 compiler, V5 compiler, V4 compiler, V1 compiler, toric compiler, charged reconstruct, Singular, and every solver were not run |

## What was and was not run

No local substantive computation was run. In particular this review did **not** execute `compile_axis_covariance_v9.py`, `compile_hq_linear_filtered_lift_v8.py`, `compile_h2_qr_syzygy_lift_v7.py`, `compile_h_grade5_kernel_lift_v6.py`, `compile_h_qr_syzygy_lift_v5.py`, `compile_h_first_transport_v4.py`, `compile_q2_first_lift.py`, `compile_toric_blowup.py`, `independent_reconstruct.py`, Singular, Sage, msolve, Lean, Gfan, or any other solver, and it did not re-multiply `sum F_i E_i` or reconstruct the unsubstituted eight rows. Hashes were checked with `shasum -a 256`. File identity was checked with `cmp`. Marker counts used `grep`. Git identity was read with `git rev-parse`. JSON fields were read with Python `json` (no algebra libraries). Canonical SHA-256 values were recomputed from the already-emitted certificate records (toric canonical format `[[list(monomial), num, den], ...]`). Axis characters of recorded monomials and of the hash-pinned V1/V7/V8 multiplier support were scored by integer arithmetic against the preregistered table.

Charged freeze SHA-256, recomputed and matched:

```text
003788e80c359fa715d799f3fe66a35929b105c772d139865e87f123c1a9bda2  FREEZE.sha256
a061aea2bab3abcd9a8e88a3e86f18de233f46515cd2965bafa79ff1516642e2  RESULT.md
53cf4b656c4415324a74862ec108b902ac8eade22733b2cb3a58cd3e447491e0  universal witness
e549fd6879763d9f6804b9fcc17327e114bd54e29180246cc0b2e7c632fff38b  a=1 / V8 witness
1375bd72024baefab039da3afc7d84c0ad76604df3dbc3cc60e6ed6e935d5e72  canonical certificate
```

Promoted V8 theorem and its hostile review, recomputed and matched:

```text
2c3dbbd50089892197dd5ad5c0fb90776b5c2d2dea4ac2752f3b1a3218cc7d4c
  xmodel/max12-912-order3-d1-double-root-control2-hq-linear-filtered-lift-review-grok-20260826.md
b503f6a70c39c256ba27f27823d5788bf5787badc507efa3079433064eb142e3
  xmodel/max12-912-order3-d1-double-root-control2-hq-linear-filtered-lift-promotion-20260826.md
7d3973e84c37d158a1f88796fdd5747e32d13e7fabd071ece80f6ea5a4c7942d
  V8 RESULT.md
85a6ddb3b72fce2b2cce6399ba69315bd869ad9eae76461de6963a446ed648ff
  V8 FREEZE.sha256
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

Every path listed in `FREEZE.sha256` recomputed and matched (55/55). Nested `SOURCE_CLOSURE.sha256` (12/12) and both harvested `result.sha256` manifests (5/5 each) matched from the case root / harvest directory as appropriate. Empty compiler stderr files are the empty-string digest `e3b0c442…`. Both rc files are the two-byte string `"0\n"`, digest `9a271f2a…`.

Read in full before the verdict: every file at
`cases/max12_912_order3_d1_double_root_control2_axis_covariance_v9_20260826/`
including both harvest trees; the hash-pinned V8 compiler `D2` / `HQ` construction and V7 `G1`; the hash-pinned V4 `coefficient_images` / `embed`; the hash-pinned V1 `multipliers` / targets; the hash-pinned toric `NAMES` / `canonical` / `digest` / `load_charged_source`; the charged `build()` tail extraction; the promoted V8 theorem and its review named above; and the design note
`xmodel/max12-912-order3-d1-double-root-discriminant-coordinate-action-design-20260826.md`.
Predecessor conclusions were recomputed, not inherited.

---

## Promotion

**Accept `FOR THE PINNED ORDINARY-TAIL EIGHT-ROW MODULE WITH FIXED LOADS k=ν=0, μ=2/3, AND THE CHARGED SOURCE independent_reconstruct.py AT 67343b56…, STARTING FROM THE REVIEWED V8 MULTIPLIERS F_i^(8) (q2-CORRECTION F1+=q2/12, F2+=-q2/9; SCALAR-h CORRECTION G1=(5/2,-25/18,0,1/4,-1/3,0,0,0); SCALAR-h-SQUARED CORRECTION D2=(5/24,-2/9,0,0,0,0,0,0); AND THE V8 COLUMNS F1-=h q1/36, F2-=h q0/72), THE REGISTERED DUAL-AWS V9 RUNS PROVE THE EIGHT EXACT ROW IDENTITIES E_i(a,h,Q,R,Λ,ρ,τ)=a^(12+i) E_i(1, h/a^3, q2/a^4, q1/a^5, q0/a^6, r2/a^7, r1/a^8, r0/a^9, Λ/a, ρ/a, τ) AT p=-3a^2, c=2a^3+h, INCLUDING THE ROW-3 LOAD (2/3)Λ^15 AND THE ROW-8 TARGET Λ^20(1+τ), WITH ROW-6 ν UNSUBTRACTED. THE LEAST COMMON NEGATIVE AXIS CHARACTER OF THE LITERAL V8 MULTIPLIER SUPPORT IS EXACTLY -3, ACHIEVED ON FOUR MONOMIALS, SO CLEARING POWER THREE IS SUFFICIENT AND MINIMAL. AFTER CLEARING, sum_i a^(11-i) F_i^(8)(hat) E_i(a,h,Q,R) = a^23 W^(8)(hat) IS AN EXACT 48-TERM POLYNOMIAL IDENTITY OF SHA 53cf4b65…, NOT A CONGRUENCE AND NOT AN h-TRUNCATION. ITS a=1 SPECIALIZATION IS DICTIONARY-EQUAL TO THE REVIEWED V8 48-TERM POLYNOMIAL (SHA e549fd68…). THE DISTINGUISHED TERMS ARE COEFFICIENT-ONE a^3 Λ^20 AND COEFFICIENT-ONE a^3 Λ^20 τ. THE ELEMENTARY MAP (a,h)↦(p,c)=(-3a^2, 2a^3+h) HAS JACOBIAN DETERMINANT -6a AND IS ETALE ON D(a). ITS DISCRIMINANT IS Δ=-4p^3-27c^2=-27h(4a^3+h). ON AN ARC CENTRED AT h=0 WITH a A UNIT, 4a^3+h IS A UNIT, HENCE v(Δ)=v(h). ON D(a), WITH wt(a)=0, THE REVIEWED V8 UNIQUE-LEAST-TERM THEOREM APPLIES TO THE NORMALIZED VARIABLES h/a^3, q2/a^4, q1/a^5, q0/a^6, r2/a^7, r1/a^8, r0/a^9, Λ/a, ρ/a, τ, AND THE INITIAL MONOMIAL a^3 Λ^20 IS A UNIT TIMES Λ^20. FAITHFULLY FLAT / ETALE BASE CHANGE ALONG THE a-CHOICE TRANSFERS NONEXISTENCE AND THAT UNIT-INITIAL-IDEAL CONCLUSION TO THE SMOOTH DISCRIMINANT LOCUS.`**

Do not promote this to: the triple-root point `a=0`, or any statement with `v(a)>0`; an unlocalized claim that `Λ^20` itself is an initial monomial of the combination as a polynomial in `a`; moving loads; another source chart or normal direction; a formal neighbourhood; the whole double-root fan; D1; or JC2.

---

## Charge 1 — Custody, freeze, dual AWS, source closure, JSON difference

**CONFIRMED. Every freeze entry recomputes. Both registered workers are fail-closed, hash-gated, empty-stderr, sub-cap, pre-GO, and source-closed against the package-root manifest. Opposite traversal orders return certificates that differ only in `tag` and `order`; deleting those two fields gives literally identical sorted JSON of SHA `1375bd72024baefab039da3afc7d84c0ad76604df3dbc3cc60e6ed6e935d5e72`.**

Required anchors, recomputed:

```text
a061aea2bab3abcd9a8e88a3e86f18de233f46515cd2965bafa79ff1516642e2  RESULT.md
003788e80c359fa715d799f3fe66a35929b105c772d139865e87f123c1a9bda2  FREEZE.sha256
b74c8609fad7910c00766a7b7758e51cda0242c358f1d6d9cb161385ebcf42aa  aws_box03_forward/axis_covariance.json
31be54bd064e652c539afb1fffa8267341e895b3a07fe506437fc995a7a1cd04  aws_r6d_reverse/axis_covariance.json
53cf4b656c4415324a74862ec108b902ac8eade22733b2cb3a58cd3e447491e0  universal_witness_sha256 (both JSON payloads)
e549fd6879763d9f6804b9fcc17327e114bd54e29180246cc0b2e7c632fff38b  a_one_specialization_sha256 / w8_sha256 (both)
```

Recomputed `FREEZE.sha256` entries, all matched (55/55):

```text
081bab6349cadc8981bb30f4a278b0a5f68e42d32b72988cb2afa35cdc85ee10  AWS_LAUNCH_METADATA.md
47ffb498ff4cfe9f4cce0495046287a45633164b867093df51ca60959772464f  AWS_REGISTRATION.md
c9f765d4ee841f5a4a143b0f3a39a88c33f26152de737923156a1d89d71beae5  PREREGISTRATION.md
a061aea2bab3abcd9a8e88a3e86f18de233f46515cd2965bafa79ff1516642e2  RESULT.md
084cc8ddc9523c7208556bfb12d68e545a81221034e9ed108743127cc9805274  SOURCE_CLOSURE.sha256
47ffb498ff4cfe9f4cce0495046287a45633164b867093df51ca60959772464f  aws_box03_forward/AWS_REGISTRATION.md
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_box03_forward/DONE
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_box03_forward/GO
c9f765d4ee841f5a4a143b0f3a39a88c33f26152de737923156a1d89d71beae5  aws_box03_forward/PREREGISTRATION.md
084cc8ddc9523c7208556bfb12d68e545a81221034e9ed108743127cc9805274  aws_box03_forward/SOURCE_CLOSURE.sha256
b74c8609fad7910c00766a7b7758e51cda0242c358f1d6d9cb161385ebcf42aa  aws_box03_forward/axis_covariance.json
55a27313370722e9ab255b34d3cb3d2ed592c47c32b5461397a8aa26a1a2a8a1  aws_box03_forward/compile_axis_covariance_v9.py
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  aws_box03_forward/compiler.rc
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_box03_forward/compiler.stderr
4eface0522a3a7923ccc90e063cedf089d349b8f5296c10f9d0f73671b55a545  aws_box03_forward/compiler.stdout
c9cb89acd1d742129e32922316424edbc7f2f1715dfd999025f66298e0223aec  aws_box03_forward/compiler.time
e53837e2054e7dfef33a8ffdb513c05923e418fa5dfad8472241c3729b4f9785  aws_box03_forward/free.postsolve.txt
7fe9b66befa3a299018e959eb0fb4b14b800627c9616a9cb9e4b3455ba2e97ae  aws_box03_forward/free.prelaunch.txt
23a0b561f754d4f5d21c6622293945378cc4d11eeba267fe9b114049b082076a  aws_box03_forward/hostname.txt
913f5d1da2feaf4deeccc9e55cbb350a20f12b3f507e87be85dbb77fdd3cb9bc  aws_box03_forward/nproc.txt
058ba0991a5ce0b45fac2d68aa7755f2dcc029e4e91fe35601f68d6167cf81ad  aws_box03_forward/remote_worker.sh
3299b60ce9e80aa9577729b1e56874d9726304e82f1ee1e21ebdf2b16898fc04  aws_box03_forward/result.sha256
fd53e4d87cebc996394a41bb3ea38e5645d772bb2e1b5adc33fd50a2b9781f93  aws_box03_forward/source.check
ec10e1128275389639fbf3e3f7a2eff1a30dd52efb8230dec80b563ca0049a01  aws_box03_forward/uname.txt
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_box03_forward/worker.launch.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_box03_forward/worker.launch.stdout
734bf2ef441e0c1c38839b0fe6899bba34a22998e7fd677a139bff9ad6d2fafd  aws_box03_forward/worker.metadata
04d257057070aa8cb80a0fd638b1c63b363eb200b15d669cba2a154543b64ec0  aws_box03_forward/worker_finished_utc.txt
4652c947547d021e963ded9c827cdb08bbadce8e58499fe31bafbdd09c8c165a  aws_box03_forward/worker_started_utc.txt
47ffb498ff4cfe9f4cce0495046287a45633164b867093df51ca60959772464f  aws_r6d_reverse/AWS_REGISTRATION.md
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_reverse/DONE
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_reverse/GO
c9f765d4ee841f5a4a143b0f3a39a88c33f26152de737923156a1d89d71beae5  aws_r6d_reverse/PREREGISTRATION.md
084cc8ddc9523c7208556bfb12d68e545a81221034e9ed108743127cc9805274  aws_r6d_reverse/SOURCE_CLOSURE.sha256
31be54bd064e652c539afb1fffa8267341e895b3a07fe506437fc995a7a1cd04  aws_r6d_reverse/axis_covariance.json
55a27313370722e9ab255b34d3cb3d2ed592c47c32b5461397a8aa26a1a2a8a1  aws_r6d_reverse/compile_axis_covariance_v9.py
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  aws_r6d_reverse/compiler.rc
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_reverse/compiler.stderr
78365475385d43586c3110cfab43709a8a66ba647e4c0d9273aaaff66552c565  aws_r6d_reverse/compiler.stdout
7781b57391dd8e5a26d0dd0946496a490c71827e4b13ad09d8d7791d93662a88  aws_r6d_reverse/compiler.time
5fb9c56a235d83abbbfd30b8708b0dbbb83f459e0af913cf58758941e2a5b261  aws_r6d_reverse/free.postsolve.txt
17a3d37b39eed20f7df02e779d22a3e7d61df8aa1d99bac7895411f2c11144c6  aws_r6d_reverse/free.prelaunch.txt
e61ff4eb3cdea1fb7ff0e134553fe4175aa0f7e4c88d3ab5afba84b72f174d93  aws_r6d_reverse/hostname.txt
913f5d1da2feaf4deeccc9e55cbb350a20f12b3f507e87be85dbb77fdd3cb9bc  aws_r6d_reverse/nproc.txt
058ba0991a5ce0b45fac2d68aa7755f2dcc029e4e91fe35601f68d6167cf81ad  aws_r6d_reverse/remote_worker.sh
6270741191b333dc5b658e401028f92db6e359a2d54033c2becaed93e2db6f10  aws_r6d_reverse/result.sha256
fd53e4d87cebc996394a41bb3ea38e5645d772bb2e1b5adc33fd50a2b9781f93  aws_r6d_reverse/source.check
82749050710280f5c99c0e2f8e3730964493f2592233779aac28e815b8c78c7b  aws_r6d_reverse/uname.txt
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_reverse/worker.launch.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_reverse/worker.launch.stdout
27898ef96c29defbb3b81881d115fe5990eed45f798f151758a11587e648de31  aws_r6d_reverse/worker.metadata
04d257057070aa8cb80a0fd638b1c63b363eb200b15d669cba2a154543b64ec0  aws_r6d_reverse/worker_finished_utc.txt
4652c947547d021e963ded9c827cdb08bbadce8e58499fe31bafbdd09c8c165a  aws_r6d_reverse/worker_started_utc.txt
55a27313370722e9ab255b34d3cb3d2ed592c47c32b5461397a8aa26a1a2a8a1  compile_axis_covariance_v9.py
058ba0991a5ce0b45fac2d68aa7755f2dcc029e4e91fe35601f68d6167cf81ad  remote_worker.sh
```

Source-closure entries, all matched from the package root:

```text
c9f765d4ee841f5a4a143b0f3a39a88c33f26152de737923156a1d89d71beae5  PREREGISTRATION.md
47ffb498ff4cfe9f4cce0495046287a45633164b867093df51ca60959772464f  AWS_REGISTRATION.md
55a27313370722e9ab255b34d3cb3d2ed592c47c32b5461397a8aa26a1a2a8a1  compile_axis_covariance_v9.py
058ba0991a5ce0b45fac2d68aa7755f2dcc029e4e91fe35601f68d6167cf81ad  remote_worker.sh
ea38710ed3b11a58dac050430ba421dcec902def645f59da28c2d9418c60c247  ../max12_912_order3_d1_double_root_control2_hq_linear_filtered_lift_v8_20260826/compile_hq_linear_filtered_lift_v8.py
a4500936c83c82ef12d68c145ef6672688d401292c05dab36b95002df4138de3  ../max12_912_order3_d1_double_root_control2_h2_qr_syzygy_lift_v7_20260826/compile_h2_qr_syzygy_lift_v7.py
c7d9faed50b93cb7bb3905d8d386d2dc0f670c300baeefa78864d5dd3097dfce  ../max12_912_order3_d1_double_root_control2_h_grade5_kernel_lift_v6_20260826/compile_h_grade5_kernel_lift_v6.py
8a963360f16a29c6841050f82e9eb79051005d821c6ec7837d0614ca8ead7366  ../max12_912_order3_d1_double_root_control2_h_qr_syzygy_lift_v5_20260826/compile_h_qr_syzygy_lift_v5.py
3bbf1ebfb9f8b15054fe2f592bea92d8e07b95bce4d6ca131cd81c95f3698306  ../max12_912_order3_d1_double_root_control2_h_first_transport_v4_20260826/compile_h_first_transport_v4.py
c76ef85ac14f81839674368c55a324499832e6cf4b589befa68baf93a42b1490  ../max12_912_order3_d1_double_root_toric_blowup_20260825/compile_toric_blowup.py
0385b0b1e60b3bd37fa5fbee90dd6c17a454722bdbff424ea83c2ab0fa19df45  ../max12_912_order3_d1_double_root_control2_q2_first_lift_v1_20260826/compile_q2_first_lift.py
67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623  ../max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/independent_reconstruct.py
```

Harvested `SOURCE_CLOSURE.sha256` is byte-identical to the top copy on both hosts. Both `source.check` files are identical (`fd53e4d8…`) and print `OK` on those twelve paths. The worker `cd`s to `$run` before `sha256sum -c SOURCE_CLOSURE.sha256`. The compiler locates V8 via `HERE.parents[1]/cases/…`, so `$run` is a `cases/`-child (the package, or a copy sitting as a `cases/` neighbour). Dual AWS both passed the sibling-path hash check. Treating `aws_box03_forward/` or `aws_r6d_reverse/` as a new source root would make those siblings invisible. That is not the charged root.

The compiler pins V8 at `V8_SHA=ea38710e…` and refuses a non-matching file before import. V8 re-pins V7 at `a4500936…`; V7 re-pins V6 at `c7d9faed…`; V6 re-pins V5 at `8a963360…`; V5 re-pins V4 at `3bbf1ebf…`; V4 re-pins toric `c76ef85a…`, V1 `0385b0b1…`, and `independent_reconstruct.py` at `67343b56…`. Tag gates: worker `case` requires prefix `max12_912_order3_d1_double_root_control2_axis_covariance_v9_20260826T*`; compiler `require_aws` requires Linux, DMI vendor `Amazon EC2`, and tag prefix `max12_912_order3_d1_double_root_control2_axis_covariance_v9_`. Both refuse non-`forward`/`reverse` orders.

| Check | Box03 forward | r6d reverse |
|---|---|---|
| Public IP / harvested hostname | `98.80.65.144` / `ip-172-30-0-249` | `100.26.198.153` / `ip-172-30-0-45` |
| Tag | `…_v9_20260826T044900Z_box03_forward` | `…_v9_20260826T044900Z_r6d_reverse` |
| Worker PID | `162034` | `229414` |
| Caps | `memory_kib=8388608`, `timeout=1800`, `nice -n 10`; `ulimit -v 8388608` | same |
| Order | `forward` (`ell=1..8`, `F*E`) | `reverse` (`ell=8..1`, `E*F`) |
| Started / finished UTC | `2026-08-26T04:49:36Z` / `04:50:27Z` | `04:49:36Z` / `04:50:27Z` |
| Compiler stdout SHA | `4eface05…` | `78365475…` |
| Certificate SHA | `b74c8609…` | `31be54bd…` |
| RSS / swap / exit | 22936 KiB / `Swaps: 0` / 0 | 22504 KiB / `Swaps: 0` / 0 |
| Pre/post `free` swap | `0B` / `0B` | `0B` / `0B` |
| Elapsed | 6.12 s | 6.04 s |
| PASS markers, each once | `PASS_AXIS_COVARIANCE_V9`, `PASS_REMOTE_WORKER` | same |
| `FAIL_` / `REFUSED` / `FAILED` | none; stderr empty; no `REFUSED`/`FAILED` files | none; stderr empty; no `REFUSED`/`FAILED` files |

`AWS_LAUNCH_METADATA.md` local mtime is `2026-08-25T21:50:10 PDT` = `2026-08-26T04:50:10Z`, after worker start (`04:49:36Z`) and after the metadata text's observation stamp `2026-08-26T04:50:00Z`. Content: both workers `WAITING_GO`; “Neither run directory contained a GO sentinel”; source-closure manifest SHA `084cc8dd…` matching the frozen file. GO sentinels exist and are empty; their local mtimes are `04:50:20Z`. DONE UTC stamps match finish (`04:50:27Z` both). No `REFUSED` or `FAILED`. The 51-second start-to-finish window contains the wait-for-GO loop, the post-GO source-hash check, and the 6.12 s compile.

Harvest copies of compiler, worker, preregistration, AWS registration, and source closure are byte-identical to the package top on both hosts (`cmp`). The two JSON files are **not** byte-identical (47713 vs 47711 bytes; the 2-byte gap is `box03_forward` vs `r6d_reverse` in the tag). Their key sets are equal (25 keys). The only value differences are the two preregistered custody fields `tag` and `order`. Deleting those fields and dumping with `sort_keys=True, indent=2` plus a trailing newline yields one 47588-byte blob of SHA

```text
1375bd72024baefab039da3afc7d84c0ad76604df3dbc3cc60e6ed6e935d5e72
```

on both hosts, matching `RESULT.md` and the charged semantic-equality SHA. Compiler stdout differs only in the preregistered `ORDER=` line and the certificate SHA of the tagged JSON; the algebraic metric block is identical:

```text
STATUS=UNIT_AXIS_COVARIANCE_EXACT
CLEARING_POWER=3
UNIVERSAL_WITNESS_SHA256=53cf4b656c4415324a74862ec108b902ac8eade22733b2cb3a58cd3e447491e0
UNIVERSAL_WITNESS_TERMS=48
DISCRIMINANT_SHA256=e0afed585954d2dc9df4250499dd25d699e956a5e4ba990a7427ff9fd5ca726a
PASS_AXIS_COVARIANCE_V9
```

Worker fail-closed conditions, all met on both hosts: `rc=0`, empty stderr, exactly one `PASS_AXIS_COVARIANCE_V9` endpoint. Caps 8 GiB / 1800 s; RSS is 22 MiB; elapsed is 6 s.

---

## Charge 2 — Literal V8 ancestry, homogeneity `12+i`, scaling orientation, eight row identities

**CONFIRMED. V9 reconstructs the reviewed V8 multipliers and the charged ordinary-tail rows from frozen source. Ordinary tails are homogeneous of weight `12+i`. Coefficient images are character-homogeneous of weights `wt(a_i)=9-i` under the source scaling `f(z)↦a^{-9}f(a z)`. All eight substituted rows, including the two targets and with `ν` unsubtracted, satisfy the displayed covariance. Loads `k,μ,ν` are specialized to the frozen constants and are not scaled. `ρ` has character `1`, `τ` has character `0`.**

Construction, from the hash-pinned V9 compiler, which loads the hash-pinned V8 compiler, which loads the hash-pinned V7/V6/V5/V4/toric/V1 chain:

1. `t.load_charged_source().build()["tails"]` is the eight negative Laurent tails of `independent_reconstruct.py` at `67343b56…`, in names `(a0..a7,k)`. Same charged ordinary-tail source as the reviewed V8/V7/V6/V5/V4 lifts. `build()` takes `[w^{-ell}] g(z(w))` for `ell=1..8` and scales by `-1`.
2. Ordinary-homogeneity checksum, before substitution, requires every monomial of `tails[ell]` to have weight `{12+ell}` under `wt(a_i)=9-i` (`i=0..7`) and `wt(k)=6`. Dual AWS both fail-close on this. Certificate `ordinary_homogeneity={1:13,…,8:20}`. This is the same checksum the V4 review licensed as a checksum, now used as a hypothesis of the row identities.
3. `coefficient_images(t, moving_axis=False)` is byte-level the V4/V8 specialization: affine `x=1`, empty `k`-slot, `p=-3`, `c=2+h`. `moving_axis=True` replaces only those two assignments by `p=-3a^2`, `c=2a^3+h`. Jet formulae are the toric `K^3+K Q+R` coefficients with `x=1`:

```text
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

4. Targets, after substitution, identical to V8: row 3 subtracts `(2/3) Λ^15`; row 8 subtracts `Λ^20(1+τ)`; row 6 does **not** subtract `ν Λ^18`. `μ=2/3` is baked as a coefficient, not kept as a variable. `k=ν=0`.
5. Multipliers, identical to the promoted V8 combination: V1 `multipliers()` plus `F1+=q2/12`, `F2+=-q2/9`, plus `v7.G1[ell-1]*h`, plus `v8.D2[ell-1]*h^2`, plus the V8 columns `F1+=-(1/36) h q1`, `F2+=-(1/72) h q0`.

Fail-closed, in this order, before any moving product: `digest(sum F_i E_i(fixed))=e549fd68…` and `digest(project_base([h^0]))=ddb451c4…`. Dual AWS both exited 0 after those checks, opposite traversal. That is the custody that V9 reconstructed the V8 identity rather than loading a stale certificate.

Fixed-multiplier SHA ancestry against the frozen V8 certificate:

```text
row  F_i^(7) (V8 v7_multiplier)     F_i^(8) (V9 fixed_multiplier)
  1  1b6c8c37…  (then HQ on row 1)   7654e4a1…   # changed, as required
  2  16ccf27a…  (then HQ on row 2)   e7a68019…   # changed, as required
  3  4f53cda1…  (empty)              4f53cda1…   # empty, F3=0
  4  28f56b54…                       28f56b54…
  5  bac8d128…                       bac8d128…
  6  a41bb5f7…                       a41bb5f7…
  7  bef382a5…                       bef382a5…
  8  6fe9972e…                       6fe9972e…
```

Rows 3–8 are literally the reviewed V7/V8 multipliers (empty corrections). Rows 1–2 differ by exactly the two V8 columns. Empty-polynomial digest is `sha256(b"[]")=4f53cda1…`.

Coefficient scaling orientation, charged against the source map of the design and of the V4 checksum. The physical / unit-axis relation is

```text
K_new(z) = a^{-3} K(a z)     ⇒  p_phys = a^2 p_unit,  c_phys = a^3 c_unit,
Q_new(z) = a^{-6} Q(a z)     ⇒  (q2,q1,q0)_unit = (q2/a^4, q1/a^5, q0/a^6),
R_new(z) = a^{-9} R(a z)     ⇒  (r2,r1,r0)_unit = (r2/a^7, r1/a^8, r0/a^9),
f_new(z) = a^{-9} f(a z).
```

With `p_unit=-3` and `c_unit=2+h/a^3` this is `p_phys=-3a^2`, `c_phys=2a^3+h`. Each jet slot is character-homogeneous of weight `9-i`:

```text
a0: c^3, c q0, r0                         chars 9, 9, 9
a1: p c^2, p q0, c q1, r1                 chars 8, 8, 8, 8
a2: p^2 c, p q1, c q2, r2                 chars 7
a3: p^3, c^2, q0, p q2                    chars 6
a4: p c, q1                               chars 5
a5: p^2, q2                               chars 4
a6: c                                     char  3
a7: p                                     char  2
```

matching `wt(a_i)=9-i`. The identity is written in the physical-equals-weight-times-invariant orientation

```text
E_i(a, h, Q, R, Λ, ρ, τ)
  = a^(12+i) E_i(1, h/a^3, q2/a^4, …, Λ/a, ρ/a, τ),
```

which is the inverse of “source scaling sends `E_i` to `a^{-(12+i)} E_i`”. Both are the same covariance.

Targets and loads, character by character:

- Row 3. Toric target is `μ Λ^15`. V9/V8 bake `μ=2/3`, so the subtracted monomial is `(2/3)Λ^15` of character `15=12+3`. Prefactor `a^15` times `(Λ/a)^15` recovers `Λ^15`. `μ` is a constant (character 0), not a moving load.
- Row 6. Toric target is `ν Λ^18` of character `18=12+6`. V9 does not subtract it. That is the frozen load `ν=0`, not a claim that a moving `ν` would scale.
- Row 8. Target `Λ^20(1+τ)`. Character of `Λ^20` is 20; `τ` has character 0, so `Λ^20 τ` has character 20. Prefactor `a^{20}` recovers both. `τ` is the ratio coordinate in `Λ=τ^3 ρ` (toric comments), hence weight 0.
- `ρ` has character 1, forced by `Λ=τ^3 ρ` together with `char(Λ)=1` and `char(τ)=0`. No recorded V8 or V9 term carries `ρ`. The character is declared so a later cone analysis cannot silently assign it weight 0.
- `k` sits in the ninth jet slot of weight 6 and is specialized to the empty image. It does not scale because it is zero, not because a nonzero `k` would be invariant. A moving-`k` theorem is outside scope.

The eight row identities. The compiler transports each fixed row monomial of character `w` to `a^(12+i-w)` times that monomial, refuses a negative exponent, and requires dictionary equality with the moving-axis substituted row. Dual AWS both exited 0; the eight `row_covariance_sha256` values agree. Independently of that product replay: if the unsubstituted tails are homogeneous of weight `12+i` (fail-closed checksum) and the jet images are character-homogeneous of weights `9-i` (hand, above), substitution yields a character-homogeneous moving row of weight `12+i`. The `a=1` slice is the fixed row. Inserting `a^(12+i-w)` on each fixed monomial is exactly the reconstruction of that homogeneous moving row from its `a=1` specialization. The two targets are themselves homogeneous of weights 15 and 20 and contain no `a`, so they transform correctly. This is why the eight identities hold, including row 3 and row 8, and why row 6 needs no `ν` correction at the frozen load. V9 `row_covariance_sha256` are digests of the *moving* rows and are not comparable to V8 `rows_full_sha256` (the fixed rows); the fixed-row custody is the V8 product digest `e549fd68…`.

`character_weight` refuses any multiplier monomial supported on `{p,c,a,x,y,k,μ,ν}`. The V1 multipliers and the V6/V7/V8 corrections live in `{h,q2,q1,q0,r2,r1,r0}` plus constants, so the refusal does not fire.

---

## Charge 3 — Least common negative axis character exactly `-3`; powers `a^(11-i)` and `a^23`

**CONFIRMED. Listing every monomial of the literal V8 multipliers and scoring `char(m)-(8-i)` produces a 26-element deficit list whose maximum is `3`, achieved four times. Clearing power three is therefore sufficient and minimal for this combination, not a dimensional guess. The cleared multipliers are `a^(11-i) F_i(hat)`; the cleared combination is `a^23 W^(8)(hat)`.**

Preregistered characters:

```text
Λ:1, τ:0, ρ:1, h:3, q2:4, q1:5, q0:6, r2:7, r1:8, r0:9.
```

V1 multipliers, plus the reviewed corrections, monomial by monomial. Deficit `= char-(8-i)`:

```text
# F1, 8-i=7
 +1/108 q1^2          char 10   def +3
 -7/72  r2            char  7   def  0
 +1/8   r1            char  8   def +1
 -5/18  q1            char  5   def -2
 +1/8   q0            char  6   def -1
 +115/24              char  0   def -7
 +1/12  q2            char  4   def -3     # q2 correction
 +5/2   h             char  3   def -4     # G1
 +5/24  h^2           char  6   def -1     # D2
 -1/36  h q1          char  8   def +1     # V8 HQ
# F2, 8-i=6
 +1/12  q1            char  5   def -1
 -5/36  q0            char  6   def  0
 -29/9                char  0   def -6
 -1/9   q2            char  4   def -2
 -25/18 h             char  3   def -3
 -2/9   h^2           char  6   def  0
 -1/72  h q0          char  9   def +3     # V8 HQ
# F3 empty
# F4, 8-i=4
 -1/24  q1            char  5   def +1
 +3/2                 char  0   def -4
 +1/4   h             char  3   def -1
# F5, 8-i=3
 -1/24  q0            char  6   def +3
 -25/24               char  0   def -3
 -1/3   h             char  3   def  0
# F6, 8-i=2
 +1/24  q1            char  5   def +3
# F7, 8-i=1
 +3/8                 char  0   def -1
# F8, 8-i=0
 -1                   char  0   def  0
```

Twenty-six deficits. Sorted:

```text
[-7, -6, -4, -4, -3, -3, -3, -2, -2, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 1, 1, 1, 3, 3, 3, 3]
```

This is the stored `axis_deficits` on both hosts. Maximum `3`. Four monomials achieve it, so the bound is sharp:

```text
F1:  a^{8-1} (q1/a^5)^2 /108     = a^{-3} q1^2 /108
F2:  a^{8-2} (h/a^3)(q0/a^6)/(-72)= a^{-3} h q0 /(-72)
F5:  a^{8-5} (q0/a^6)/(-24)       = a^{-3} q0 /(-24)
F6:  a^{8-6} (q1/a^5)/24          = a^{-3} q1 /24
```

No multiplier monomial produces `a^{-4}` or worse. Clearing `a^3` is exactly the least common denominator of `a^{8-i} F_i(hat)`. The compiler sets `clearing_power=max(0, deficits)` and refuses any value other than 3. Dual AWS both exited 0.

Cleared-multiplier prefactor is `clearing_power+(8-i)=11-i`. That is the source of `a^(11-i)` in the displayed identity, not a separate ansatz. Combination weight: row prefactor `12+i` plus multiplier prefactor `11-i` is `23`, which is `clearing_power+20` because the V8 output weight is 20 (`Λ^{20}`). The compiler transports `W^(8)` with prefactor `23` and requires dictionary equality with `sum (transported F_i)(transported E_i)`. Dual AWS both exited 0, opposite multiply order.

Row 6 fixed-multiplier SHA equals cleared-multiplier SHA (`a41bb5f7…`): `F6=(1/24)q1` has character 5, cleared prefactor `11-6=5`, so the inserted `a`-power is 0. Row 3 remains empty. Both facts match the table.

---

## Charge 4 — 48-term coefficientwise identity, SHA `53cf4b65…`, `a=1` SHA `e549fd68…`, coefficient-one targets

**CONFIRMED. The recorded universal polynomial has 48 terms, toric digest `53cf4b65…`. Zeroing `a` is dictionary-equal to the reviewed V8 48-term polynomial (SHA `e549fd68…`, 48/48 keys, 48/48 coefficients). Every universal term has `a`-exponent `23-char(rest)`. Targets `a^3 Λ^{20}` and `a^3 Λ^{20} τ` have coefficient `1`. This is the exact product identity, not a congruence modulo `(a-1)` or `h^N`, and not a truncation of `W^(8)`.**

Recomputed toric digest of the stored `universal_witness` canonical triples: `53cf4b656c4415324a74862ec108b902ac8eade22733b2cb3a58cd3e447491e0`. Stored `universal_witness_sha256` matches on both hosts. Term count 48.

`a=1` specialization, formed by zeroing the `a`-slot of those 48 triples and combining like terms: still 48 terms, digest `e549fd6879763d9f6804b9fcc17327e114bd54e29180246cc0b2e7c632fff38b`. Stored `a_one_specialization_sha256` and `w8_sha256` match. Against the frozen V8 records (48 terms, SHA `e549fd68…`): key sets equal, coefficient mismatch 0. `h`-exponent histogram of the `a=1` slice is `{0:37, 1:10, 2:1}`, the V8 histogram. Maximum `h` is 2; there is no hidden `h^3`.

Character check on all 48 recorded universal monomials, against `a`-exponent `= 23 - char(rest)`: 48/48. Recorded `difference_from_a3_la20` recovers the exponents: 48/48. Extra toric variables `p,c,x,y,k,μ,ν` are zero on every term. `ρ` is zero on every term. `τ` appears only on the split target.

Distinguished terms, from the records:

```text
+1  a^3 Λ^20
+1  a^3 Λ^20 τ
```

Stored `target_coefficient="1"` and `split_target_coefficient="1"` match. These are the V8 targets `Λ^{20}` and `Λ^{20}τ` of character 20, transported with prefactor 23.

`a`-power histogram of the 48 terms:

```text
a^0 : 17     (rest character 23)
a^2 : 10     (rest character 21)
a^3 : 11     (rest character 20; includes both targets)
a^4 :  5     (rest character 19)
a^5 :  3     (rest character 18)
a^6 :  1     (rest character 17)
a^7 :  1     (rest character 16)
```

`17+10+11+5+3+1+1=48`. Minimum `a`-exponent is 0. The leftover V8 monomial `-1/486 h^2 q1 q2^3` has character `6+5+12=23` and survives as an `a^0` term. Seventeen character-23 V8 monomials do likewise. Consequently `a^3` does **not** divide the 48-term polynomial in `Q[a,h,Q,R,Λ,τ]`. The phrase “common factor `a^3`” in `RESULT.md` refers to the multiplier-denominator clearing and to the distinguished initial monomial `a^3 Λ^{20}`, not to a polynomial GCD. That distinction is load-bearing for Charge 6 and is already in the frozen firewall (“does not make `Λ^{20}` an unlocalized initial monomial at `a=0`”). It is not a failing identity.

Exact identity versus congruence or truncation:

- Dual AWS, opposite multiply order, fail-close on `sum (moved F_i)(moved E_i) == transport(W^(8), 23)` as dictionaries. A congruence modulo `(a-1)` would survive `a=1` specialization and fail this equality at generic `a`. A finite-`h` truncation of `W^(8)` would drop or alter the unique `h^2` term `-1/486 h^2 q1 q2^3`, which is present at `a^0` in the universal records and in the V8 records with the same coefficient.
- Term count 48 equals the V8 count. Support after dropping `a` is exactly the V8 support. Collateral `h`-degree is 2, not a cutoff.
- The character constraint `a^{23-w}` on every term is stronger than “some polynomial that specializes to `W^(8)`”. A random lift of the 48 V8 monomials with other `a`-powers would specialize correctly and fail the constraint; zero of 48 fail it.

This review did not replay the eight-row product. The dual-traversal dictionary equality, the V8-slice dictionary equality, and the 48/48 character constraint are the custody that the recorded polynomial is that product.

---

## Charge 5 — `p=-3a^2`, `c=2a^3+h`, `Δ=-27h(4a^3+h)`, Jacobian `-6a`, and `v(Δ)=v(h)`

**CONFIRMED. The moving chart is exactly `p=-3a^2`, `c=2a^3+h`. The discriminant identity holds as a two-term polynomial of SHA `e0afed58…`. The Jacobian determinant is `-6a` by hand. On an arc centred at `h=0` with `a` a unit, `v(Δ)=v(h)`.**

Chart, from the hash-pinned compiler, matching the double-root normal form `z^3+p z+c=(z+a)^2(z-2a)` up to the sign convention `a=-α` of `(z-α)^2(z+2α)`:

```text
p = -3 a^2,     c = 2 a^3 + h.
```

At `h=0` this is a double root at `z=-a`. At `a=1` it is the promoted V8 chart `p=-3`, `c=2+h`.

Discriminant. Compiler constructs `-4p^3-27c^2` from those images and requires dictionary equality with `-27 h (4a^3+h)`. Dual AWS both exited 0. Stored expanded polynomial, two terms:

```text
-27 h^2  +  (-108) a^3 h.
```

Hand expansion: `-27h(4a^3+h)=-108 a^3 h-27 h^2`. Equal. Recomputed toric digest `e0afed585954d2dc9df4250499dd25d699e956a5e4ba990a7427ff9fd5ca726a`, matching both JSON payloads, both stdout lines, and `RESULT.md`. Working ring is `Q` (`Fraction`); `-27` and `-108` are units.

Jacobian of `φ:(a,h)↦(p,c)=(-3a^2, 2a^3+h)`:

```text
∂(p,c)/∂(a,h)  =  | -6a    0 |
                   |  6a^2   1 |,     det = -6a.
```

This is not a compiled field; it is a two-by-two derivative. On `D(a)` the value `-6a` is a unit in characteristic zero. Hence `φ` is etale on `D(a)` (smooth sources and targets of equal dimension, invertible derivative). At `a=0` the derivative vanishes and the map ramifies; that is the triple-root point, excluded.

Why `v(Δ)=v(h)` on an arc centred at `h=0` with `a` a unit. Write `Δ=-27 h (4a^3+h)`. Characteristic zero, so `v(-27)=0`. Unit `a` means `v(a)=0`, hence `v(4a^3)=0`. An arc centred at `h=0` means `h` vanishes on the closed point, so `v(h)>0`. Then `v(4a^3+h)=0` (the unit `4a^3` dominates), therefore `v(Δ)=v(h)`. If `v(h)=0` the arc is not centred at the double-root locus. If `4a^3+h=0` one is on the other discriminant factor, which at `h=0` forces `a=0`, the triple root. Both are outside the charged cell.

---

## Charge 6 — Transport on `D(a)`; etale / faithfully flat descent; normalized valuations; no positive axis valuation

**CONFIRMED, with the exact normalized variables and with `wt(a)=0` stated as a hypothesis rather than a conclusion. Multiplication by `a^3` as a unit of `O(D(a))`, together with the weighted coordinate automorphism, preserves the V8 monomial-initial obstruction. After the etale `a`-choice, nonexistence and the unit-initial-ideal conclusion descend to the smooth discriminant. Positive axis valuation is not smuggled in.**

Normalized valuation variables, the hats of Charge 2:

```text
ĥ   = h  / a^3,
q̂2  = q2 / a^4,    q̂1 = q1 / a^5,    q̂0 = q0 / a^6,
r̂2  = r2 / a^7,    r̂1 = r1 / a^8,    r̂0 = r0 / a^9,
Λ̂   = Λ  / a,      ρ̂  = ρ  / a,      τ̂  = τ.
```

The reviewed V8 theorem is a statement about the 48-term polynomial `W^(8)` in `(h,Q,R,Λ,τ)` at `a=1`: unique least term `Λ^{20}` for `η=wt(h)/L≥0`, uniformly in `u,v,T>0`, with `α=15/2`, `β=5+u`, `δ=5+v`, `L=wt(Λ)`. After the identity of Charge 4, the same polynomial in the hats is `a^{-23}` times the universal combination. Equivalently, the combination equals `a^{23} W^(8)(hats)`. Under the V8 weighting of the *hats*, with the additional rule `wt(a)=0`, the unique least term of the right-hand side is `a^{23}·Λ̂^{20}=a^{23}(Λ/a)^{20}=a^3 Λ^{20}`. Coefficient 1, split `a^3 Λ^{20} τ` strictly above once `T>0`.

On `D(a)`, `a` is a unit, so `v(a)=0` and `wt(a)=0` is the same condition. Then:

- each hat has the same valuation as the corresponding physical variable (`v(h/a^3)=v(h)`, `v(Λ/a)=v(Λ)`, …);
- `a^3` is a unit of `O(D(a))`, so `a^3 Λ^{20}` is associate to `Λ^{20}` in that local ring;
- vanishing of the combination is unaffected by multiplying by the unit `a^3`;
- the weighted coordinate automorphism (physical variables) `↔` (hats) is an automorphism of the associated graded on `D(a)`, hence preserves the property that the initial ideal of the combination is the unit ideal in the V8 cone (unique least term a unit times `Λ^{20}`).

That is the transport of the V8 unique-least-term theorem, not merely of three filtered grades. The identity is the full 48-term polynomial.

Do not confuse this with the `a`-adic initial form. Charge 4 records seventeen terms of `a`-exponent 0. Those are the V8 monomials of character 23. In the `a`-adic filtration they are the initial form of the universal polynomial, and that initial form is **not** `a^3 Λ^{20}`. The V8 theorem is a statement in the hat-weighting with `wt(a)=0`, not in the `a`-adic weighting. Assigning `v(a)>0` mixes the two filtrations: hat variables acquire extra negative valuation, `a^3 Λ^{20}` is no longer guaranteed least, and `4a^3+h` need not remain a unit. Positive axis valuation is a separate weighted-cone problem. It is not a corollary, and `RESULT.md` does not claim it.

Etale `a`-choice and descent. The map `φ: Spec Q[a,a^{-1},h] → A^2_{p,c}`, `(a,h)↦(-3a^2, 2a^3+h)`, is etale on `D(a)` by Charge 5. Its image of `{h=0}∩D(a)` is the smooth discriminant `{Δ=0} \ {(0,0)}`: on `Δ=0` one has `p=0` iff `c=0`, so every smooth double-root point has `p≠0` and admits a geometric square root `a` of `-p/3`. Over a DVR this square root may require a quadratic etale extension of the scalar ring; that is the “etale `a`-choice”.

Nonexistence transfers along *any* base change, etale or not: a solution downstairs would push to a solution upstairs. Contrapositively, emptiness of the obstruction scheme after the `a`-choice implies emptiness downstairs on the image. The image of `D(a)` is exactly the smooth discriminant, so this is the charged locus and not the triple root. Faithful flatness of an etale cover of the smooth locus supplies surjectivity on geometric points, which is the existence of the `a`-choice, not an extra vanishing argument.

Unit-initial-ideal transfers because the initial form `a^3 Λ^{20}` is a unit times `Λ^{20}` after localizing at `a`, and etale localization does not create or destroy the unit ideal. This is a statement about the associated graded of the V8 weighting after the coordinate change, not about Gröbner bases in another monomial order.

Residue characteristic. The Jacobian `-6a` and the factor `-27` are units only in characteristics other than 2 and 3. The compiler is over `Q`. No characteristic-`p` claim is licensed.

---

## Charge 7 — Firewall

**CONFIRMED. The licensed theorem is the Promotion paragraph. Fixed loads, frozen charged source, and the promoted V8 cell only. Triple-root `a=0`, moving loads, other normal directions, the whole fan, D1, and JC2 remain open.**

Admissible:

- On `D(a)`, with loads `k=ν=0`, `μ=2/3`, and the pinned ordinary-tail source, the reviewed V8 combination is covariant under the displayed axis scaling, and the cleared identity is the 48-term polynomial of SHA `53cf4b65…`.
- Clearing power three is exact for these multipliers.
- For `η≥0` in the V8 cone, evaluated on the hats with `wt(a)=0`, the combination has unique least term a unit times `Λ^{20}`. Equivalently `a^3 Λ^{20}` before localizing at `a`.
- On an arc centred at `h=0` with `a` a unit, `v(Δ)=v(h)`.
- The etale chart `(a,h)↦(p,c)` carries that obstruction to the smooth discriminant.

Not admissible, and not claimed by the frozen firewall string
`localize at a; fixed loads and charged source; triple root and moving loads remain open`
and `RESULT.md` §Firewall:

- the triple-root point `a=h=0`, or any cell with `v(a)>0`;
- an unlocalized assertion that `Λ^{20}` lies in the row ideal, or that `a^3` divides the 48-term polynomial;
- moving loads `k`, `μ`, `ν`, or a theorem that those coordinates scale;
- another source chart, another normal direction, or the other discriminant factor `4a^3+h=0`;
- a formal neighbourhood, an `h`-adic completion, or coefficients of `h^3` and higher as a completed jet;
- equality-support analysis of the V8 face monomials beyond the already-promoted V8 theorem;
- the whole double-root fan, D1, or JC2;
- a claim that V4’s ordinary-homogeneity checksum was already this theorem (it was not; that is this package).

The promoted V8 theorem remains the unique-least-term statement at `a=1`. This package is the coordinate-action identity that moves that statement onto `D(a)` at the same normalized inequalities.

---

## Nits, not defects

1. Seventeen universal terms have `a`-exponent 0, so `a^3` is not a polynomial factor of the 48-term identity. `RESULT.md`’s “common factor `a^3` is a unit” is correct only after localizing at `a` and only in the hat-weighting with `wt(a)=0`. The firewall already blocks the unlocalized reading. No source repair.
2. The Jacobian `-6a` is a hand lemma, not a certificate field. It is the two-by-two derivative of the displayed chart and does not require a compiler.
3. V9 does not emit fixed-row SHA-256 values. Fixed-row custody is the fail-closed V8 product digest `e549fd68…` together with source identity of `coefficient_images(…, False)` with V4/V8. Moving-row SHAs are not comparable to V8 `rows_full_sha256`.
4. Harvest GO/DONE mtimes convert to `04:50:20Z` / `04:50:27Z` and cohere with the UTC files and with pre-GO metadata at `04:50:00Z`. That is not a second GO.
5. `AWS_LAUNCH_METADATA.md` does not restate that `$run` is the package under the job root’s `cases/`. The compiler’s `HERE.parents[1]/cases/…` resolution, the harvested `source.check` OK-lines on the twelve sibling paths, and dual-AWS hash agreement pin that layout.
6. r6d `free` shows 155 GiB used vs box03 35 GiB; swap is zero on both, and this job’s RSS is 22 MiB under an 8 GiB `ulimit -v`. Registration leaves unrelated r6d work untouched. That is not evidence that another campaign job was stopped, and not a defect in this package.
7. Row-3 SHA `4f53cda1…` is the empty polynomial, matching `F3^(8)=0`. Covariance of the zero multiplier is vacuous and is not a missing identity.
8. The design note `xmodel/max12-912-order3-d1-double-root-discriminant-coordinate-action-design-20260826.md` is not in the V9 freeze. The compiled source and the frozen certificates are the charged objects; the design was read as orientation, not as a second freeze.

No source or certificate repair is required.

UNIT_AXIS_COVARIANCE_CONFIRMED
