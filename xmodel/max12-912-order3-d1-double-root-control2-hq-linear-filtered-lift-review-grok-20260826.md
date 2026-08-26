# Hostile text-only review — control-2 24-column hQ filtered lift V8

| Field | Value |
|---|---|
| Claim under review | One 24-column `h q_j` correction of the reconstructed V7 witness: `F1^(8)=F1^(7)-(1/36) h q1`, `F2^(8)=F2^(7)-(1/72) h q0`, `Fi^(8)=Fi^(7)` for `i>=3`, producing a 48-term polynomial whose `h=0` slice is the reviewed q2 witness, whose complete projected h-linear union of Q-R, `R^2/Q^3`, and `Q^2 R` vanishes, and which is uniformly unique-target on `u,v>0`, `T>0` if and only if `eta>=0` |
| Overall verdict | **HQ_LINEAR_FILTERED_LIFT_CONFIRMED**. Dual AWS encodings emit certificates that differ only in `tag` and `order`; deleting those fields gives canonical sorted SHA `7bae4055…`. The reconstructed V7 identity is the reviewed 57-term polynomial (SHA `efe2ebcc…`) with `h=0` slice `W'` (SHA `ddb451c4…`). Independent extraction from the frozen V7 records recovers the complete eight-term h-linear `Q^2 R` piece, each of closed-corner pre-`h` margin `-5/2`, SHA `6c42c451…`. Stored RREF of the 18-by-24 projected system has rank 9, pivots `(0,…,8)`, and free-zero solution with exactly two nonzero coordinates `F1 -= h q1/36`, `F2 -= h q0/72`. The 48-term polynomial SHA `e549fd68…` is an exact identity: the `h=0` slice is dictionary-equal to V7, the eight named `Q^2 R` monomials are deleted, no new `Q^2 R` term appears, and five surviving coefficients change. Integer arithmetic on all 48 recorded forms proves unique least term `la^20` iff `eta>=0`. There is no negative eta-zero corner margin. All 30 non-target equality-face terms have a positive `u` or `v` slope. `la^20 tau` is strict for `T>0`. Negative eta is a next-lift problem, not a branch survivor. The weight theorem is a theorem about this explicit 48-term polynomial; the 24-column RREF is complete only for the stated filtered projection |
| Smallest failing identity | none in the frozen V8 source, either harvest tree, either AWS stream, the hash-pinned V7/V6/V5/V4 sources, the frozen V7 records, or the recorded 48-term polynomial |
| Smallest missing hypothesis for a stronger theorem | a multiplier support other than the 24 columns `h q_j E_i(0)`; a correction of later `h` grades; scalar-support completeness of the eight-row module beyond the stated projection; an `h`-adic / formal lift; moving axis or moving loads; another normal direction; a formal neighbourhood; the whole double-root fan; D1; or JC2 |
| Evidence tier | SHA-256 of the freeze chain and already-emitted AWS files; `cmp` of harvest copies against package-top source; `json` comparison of the two certificates after deleting `tag` and `order`; integer/rational arithmetic on every recorded `(c,U,V,E)` and on the emitted 18-by-25 RREF; dictionary comparison of V7 vs V8 slices; toric canonical digest of the 48-term polynomial, of the 10-term residual `h`-linear coefficient, and of the 8-term input `Q^2 R` piece. No local Singular, Sage, msolve, gfan, Lean, Python algebra, compiler execution, charged reconstruct, or eight-row product replay |
| Reviewer / model | Grok 4.6 (xAI). Text-only tropical / commutative-algebra / CAS-custody referee |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `574e873d4753b57dbaeb0fb83e320fbef3694724` |
| Host | Darwin. V8 compiler, V7 compiler, V6 compiler, V5 compiler, V4 compiler, V1 compiler, toric compiler, charged reconstruct, Singular, and every solver were not run |

## What was and was not run

No local substantive computation was run. In particular this review did **not** execute `compile_hq_linear_filtered_lift_v8.py`, `compile_h2_qr_syzygy_lift_v7.py`, `compile_h_grade5_kernel_lift_v6.py`, `compile_h_qr_syzygy_lift_v5.py`, `compile_h_first_transport_v4.py`, `compile_q2_first_lift.py`, `compile_toric_blowup.py`, `independent_reconstruct.py`, Singular, Sage, msolve, Lean, Gfan, or any other solver, and it did not re-multiply `sum F_i^(8) E_i(h)` or reconstruct the unsubstituted eight rows. Hashes were checked with `shasum -a 256`. File identity was checked with `cmp`. Marker counts used `grep`. Git identity was read with `git rev-parse`. JSON fields were read with Python `json` (no algebra libraries). Canonical SHA-256 values and rational weight forms were recomputed from the already-emitted certificate records (toric canonical format `[[list(monomial), num, den], ...]` for the 8-term `Q^2 R` piece, the 10-term residual `h`-linear coefficient, and the 48-term polynomial). Recorded weight forms were checked by the integer identity `2c = 2(la-20)+10(q0+q1+q2)+15(r0+r1+r2)`. RREF substitution was checked by rational arithmetic on the frozen augmented matrix.

Charged freeze SHA-256, recomputed and matched:

```text
85a6ddb3b72fce2b2cce6399ba69315bd869ad9eae76461de6963a446ed648ff  FREEZE.sha256
7d3973e84c37d158a1f88796fdd5747e32d13e7fabd071ece80f6ea5a4c7942d  RESULT.md
e549fd6879763d9f6804b9fcc17327e114bd54e29180246cc0b2e7c632fff38b  corrected witness
```

Prerequisite V7 source and hostile review, recomputed and matched:

```text
a4500936c83c82ef12d68c145ef6672688d401292c05dab36b95002df4138de3
  compile_h2_qr_syzygy_lift_v7.py
32b63dec622ce24e777f872e898d2004da10f18c2aab49ee695f11d1f7177494
  xmodel/max12-912-order3-d1-double-root-control2-h2-qr-syzygy-lift-review-grok-20260826.md
0c5ab55da33f5296cd64a82ddfb03591cc45a6b32415c402a59014af6410475b
  V7 FREEZE.sha256
```

Prerequisite V6 / V5 / V4, recomputed and matched:

```text
c7d9faed50b93cb7bb3905d8d386d2dc0f670c300baeefa78864d5dd3097dfce
  compile_h_grade5_kernel_lift_v6.py
b80a754f32d8e6d0c1aff05f7392c95643628217e3c575e33965d8bb87bc7131
  V6 FREEZE.sha256
41e0580853ae386623a704cd6227b4cec86966a70e629915c4b54a942c716397
  V6 review
8a963360f16a29c6841050f82e9eb79051005d821c6ec7837d0614ca8ead7366
  compile_h_qr_syzygy_lift_v5.py
f166e2ba9aa8e2c4715f14a4f29ed7dd4296755ed5de551de94784be3e911471
  V5 FREEZE.sha256
7ac62c8bd0667340aab5fcdd4d6d35b5e184536fb6e9f5c98f6c9955fdea54c7
  V5 review
3bbf1ebfb9f8b15054fe2f592bea92d8e07b95bce4d6ca131cd81c95f3698306
  compile_h_first_transport_v4.py
0ff05368ab7a5751617db6a6b9a31e67545439ed5fb688cb15238ef879637b68
  V4 FREEZE.sha256
ed70c255ee6809b03e6dd40149766365cac92858b85ac4a881afa73ac3ce1d77
  V4 review
```

Every path listed in `FREEZE.sha256` recomputed and matched (55/55). Nested `SOURCE_CLOSURE.sha256` (11/11) and both harvested `result.sha256` manifests (5/5 each) matched from the case root / harvest directory as appropriate. Empty compiler stderr files are the empty-string digest `e3b0c442…`. Both rc files are the two-byte string `"0\n"`, digest `9a271f2a…`.

Read in full before the verdict: every file at
`cases/max12_912_order3_d1_double_root_control2_hq_linear_filtered_lift_v8_20260826/`
including both harvest trees; the hash-pinned V7 compiler `G1` / `D2` / `coefficient_h`; the hash-pinned V6 `grade5_component`; the hash-pinned V5 compiler `qr_component` / `exact_rref` / `analyze_threshold`; the hash-pinned V4 `coefficient_images` / multipliers; the hash-pinned toric `NAMES` / `canonical` / `digest`; V1 `multipliers` / `digest`; the frozen V7 57-term records far enough to extract the h-linear `Q^2 R` piece and to compare lower-`h` slices; and the V7/V6/V5/V4 reviews named above. Predecessor conclusions were recomputed, not inherited.

---

## Promotion

**Accept `FOR THE PINNED ORDINARY-TAIL EIGHT-ROW MODULE AT a=1, p=-3, c=2+h, k=nu=0, mu=2/3, FULL Q AND R, STARTING FROM THE REVIEWED V7 MULTIPLIERS F_i^(7) WITH q2-CORRECTION F1+=q2/12, F2+=-q2/9, SCALAR-h CORRECTION (g1,...,g8)=(5/2,-25/18,0,1/4,-1/3,0,0,0), AND SCALAR-h-SQUARED CORRECTION (d1,...,d8)=(5/24,-2/9,0,0,0,0,0,0), THE REGISTERED DUAL-AWS V8 RUNS EMIT ONE 48-TERM POLYNOMIAL W^(8)=SUM_i F_i^(8) E_i(h) WITH F1^(8)=F1^(7)-(1/36) h q1, F2^(8)=F2^(7)-(1/72) h q0, Fi^(8)=Fi^(7) (i>=3). THIS IS AN EXACT POLYNOMIAL IDENTITY, NOT A CONGRUENCE OR A TRUNCATION. ITS h=0 SPECIALIZATION IS THE REVIEWED 37-TERM W' (SHA ddb451c4…). ITS COMPLETE PROJECTED h-LINEAR UNION OF Q-R, R-SQUARE/Q-CUBIC, AND Q-SQUARED-R IS ZERO. NORMALIZE wt(la)=L, PUT alpha=15/2, beta=5+u, delta=5+v, eta=wt(h)/L, AND RESTRICT TO u>0, v>0, T>0. THEN W^(8) HAS UNIQUE LEAST-WEIGHT TERM la^20 FOR EVERY SUCH (u,v,T) IF AND ONLY IF eta>=0. THIS BOUND IS UNIFORM OVER THE OPEN QUADRANT AND SHARP AS A BOUND: AT eta=0 EVERY ONE OF THE 30 NON-TARGET CLOSED-CORNER TERMS HAS A POSITIVE u OR v SLOPE, AND la^20 tau IS STRICT FOR T>0; FOR EVERY eta<0 SOME DISPLAYED h-POSITIVE ZERO-CORNER-MARGIN TERM FALLS BELOW TARGET ONCE ITS POSITIVE u/v MARGIN IS TAKEN SUFFICIENTLY SMALL. THIS IMPROVES THE V7 RANGE eta>=5/2 TO eta>=0. THE eta<0 CELL IS A NEXT-LIFT PROBLEM, NOT A BRANCH SURVIVOR. THE WEIGHT THEOREM IS A THEOREM ABOUT THIS EXPLICIT 48-TERM POLYNOMIAL. THE 24-COLUMN RREF IS COMPLETE ONLY FOR THE STATED FILTERED PROJECTION.`**

Do not promote this to: completeness of any multiplier support other than the 24 columns `h q_j E_i(0)` on the stated three-grade projection; a classification of `eta<0`; an `h`-adic or formal lift; a moving-axis or moving-load theorem; omitted normal directions; a formal neighbourhood; equality-support analysis of the 30 face monomials beyond the recorded weights; another normal direction; a formal-arc obstruction; a whole double-root fan; D1; or JC2.

---

## Charge 1 — Custody, freeze, dual AWS, source closure, JSON difference

**CONFIRMED. Every freeze entry recomputes. Both registered workers are fail-closed, hash-gated, empty-stderr, sub-cap, pre-GO, and source-closed against the package-root manifest. Opposite traversal orders return certificates that differ only in `tag` and `order`; deleting those two fields gives literally identical sorted JSON of SHA `7bae4055e967eaa29831415a1432b04016747759ea56c62b55e4002f1f7e6c0b`.**

Required anchors, recomputed:

```text
7d3973e84c37d158a1f88796fdd5747e32d13e7fabd071ece80f6ea5a4c7942d  RESULT.md
85a6ddb3b72fce2b2cce6399ba69315bd869ad9eae76461de6963a446ed648ff  FREEZE.sha256
574c19699bcd95c282c45c7d70706c9ff9e0ecc830c535a1cbcf7271f020761f  aws_box03_forward/hq_linear_filtered_lift.json
f4fb41f61ed185aba053d0f19fd5b132f04ca0e79516f022ec8159900e7fc666  aws_r6d_reverse/hq_linear_filtered_lift.json
e549fd6879763d9f6804b9fcc17327e114bd54e29180246cc0b2e7c632fff38b  corrected_witness_sha256 (both JSON payloads)
```

Recomputed `FREEZE.sha256` entries, all matched (55/55):

```text
4855ed825f0ca424d107ab4fbad8d1ba9e3c5798bcb415be3f3a3698ca2b949d  AWS_LAUNCH_METADATA.md
d2170f4ea4c4c5d44a1680a913c6057bc86d9bff576ff9850a0d4d14ab1b0039  AWS_REGISTRATION.md
00753f84e87dd91dce8dd0d45e9e0a25ba3d7cdbd1f57c61fa2632b7d1781d9f  PREREGISTRATION.md
7d3973e84c37d158a1f88796fdd5747e32d13e7fabd071ece80f6ea5a4c7942d  RESULT.md
b3b38b28d22320b4c64521912b232b789e859eb4521e664785f4d20ae945827b  SOURCE_CLOSURE.sha256
d2170f4ea4c4c5d44a1680a913c6057bc86d9bff576ff9850a0d4d14ab1b0039  aws_box03_forward/AWS_REGISTRATION.md
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_box03_forward/DONE
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_box03_forward/GO
00753f84e87dd91dce8dd0d45e9e0a25ba3d7cdbd1f57c61fa2632b7d1781d9f  aws_box03_forward/PREREGISTRATION.md
b3b38b28d22320b4c64521912b232b789e859eb4521e664785f4d20ae945827b  aws_box03_forward/SOURCE_CLOSURE.sha256
ea38710ed3b11a58dac050430ba421dcec902def645f59da28c2d9418c60c247  aws_box03_forward/compile_hq_linear_filtered_lift_v8.py
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  aws_box03_forward/compiler.rc
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_box03_forward/compiler.stderr
b13fc17a683c0370b2bd157eefe02cb1ba504fc32b686462eb6ede376c747c63  aws_box03_forward/compiler.stdout
65389db3707bd8b4a0336f670804dc5d29eacf0b93a22f6f7c0ed6a4ed1dbf9e  aws_box03_forward/compiler.time
3e8e252f852faea15abd30cc5079de6eb691c6ae3b7af2e89aaf406062e87564  aws_box03_forward/free.postsolve.txt
3e8e252f852faea15abd30cc5079de6eb691c6ae3b7af2e89aaf406062e87564  aws_box03_forward/free.prelaunch.txt
23a0b561f754d4f5d21c6622293945378cc4d11eeba267fe9b114049b082076a  aws_box03_forward/hostname.txt
574c19699bcd95c282c45c7d70706c9ff9e0ecc830c535a1cbcf7271f020761f  aws_box03_forward/hq_linear_filtered_lift.json
913f5d1da2feaf4deeccc9e55cbb350a20f12b3f507e87be85dbb77fdd3cb9bc  aws_box03_forward/nproc.txt
2c088b57feb6788aef6c59d6d2b5ab1f40e9ad5c21e54af660ab5c1d517bad4a  aws_box03_forward/remote_worker.sh
f5d1b975d0e5d963a060ea940a655dabc0d0684cb1277c558fd9aaf4062058ce  aws_box03_forward/result.sha256
cd14de3f608106e6c4c1321077623997cd7728a6fb36db5ad3215552bee58f8d  aws_box03_forward/source.check
ec10e1128275389639fbf3e3f7a2eff1a30dd52efb8230dec80b563ca0049a01  aws_box03_forward/uname.txt
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_box03_forward/worker.launch.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_box03_forward/worker.launch.stdout
601fb5bc6cca54f61c84f648d5933905e829419610bdf7ce5851c6011a5c0059  aws_box03_forward/worker.metadata
cc4bb6495a82fe4decc477965ed74e150331ea21f88fe33926ec720d22c50c75  aws_box03_forward/worker_finished_utc.txt
a1c5caee972698b41c7cff534086d291a78cd04a29e61aab95be8f3e1a2058b8  aws_box03_forward/worker_started_utc.txt
d2170f4ea4c4c5d44a1680a913c6057bc86d9bff576ff9850a0d4d14ab1b0039  aws_r6d_reverse/AWS_REGISTRATION.md
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_reverse/DONE
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_reverse/GO
00753f84e87dd91dce8dd0d45e9e0a25ba3d7cdbd1f57c61fa2632b7d1781d9f  aws_r6d_reverse/PREREGISTRATION.md
b3b38b28d22320b4c64521912b232b789e859eb4521e664785f4d20ae945827b  aws_r6d_reverse/SOURCE_CLOSURE.sha256
ea38710ed3b11a58dac050430ba421dcec902def645f59da28c2d9418c60c247  aws_r6d_reverse/compile_hq_linear_filtered_lift_v8.py
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  aws_r6d_reverse/compiler.rc
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_reverse/compiler.stderr
b524c003f2224b2f92b48953d38dd5138d1b6f4bbbdb96c82187d11224f0db97  aws_r6d_reverse/compiler.stdout
913231e43080204962d3badba2bd56d6f58fccee6afaf68737a7c3d6aa2349ea  aws_r6d_reverse/compiler.time
35b8f05a8281a2c65906cfd60705fcc8e409c60b407532e0add409a9d7c83d78  aws_r6d_reverse/free.postsolve.txt
acddcb99d8e9d64dede0f67feba78f8d7ca2ee2b228daee302cf0777662c29d5  aws_r6d_reverse/free.prelaunch.txt
e61ff4eb3cdea1fb7ff0e134553fe4175aa0f7e4c88d3ab5afba84b72f174d93  aws_r6d_reverse/hostname.txt
f4fb41f61ed185aba053d0f19fd5b132f04ca0e79516f022ec8159900e7fc666  aws_r6d_reverse/hq_linear_filtered_lift.json
913f5d1da2feaf4deeccc9e55cbb350a20f12b3f507e87be85dbb77fdd3cb9bc  aws_r6d_reverse/nproc.txt
2c088b57feb6788aef6c59d6d2b5ab1f40e9ad5c21e54af660ab5c1d517bad4a  aws_r6d_reverse/remote_worker.sh
77e5a9aac85c56e431b9de9029575ea09dfa8bb997eba43fadd0b9a4d5c086fe  aws_r6d_reverse/result.sha256
cd14de3f608106e6c4c1321077623997cd7728a6fb36db5ad3215552bee58f8d  aws_r6d_reverse/source.check
82749050710280f5c99c0e2f8e3730964493f2592233779aac28e815b8c78c7b  aws_r6d_reverse/uname.txt
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_reverse/worker.launch.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_reverse/worker.launch.stdout
d344ca19c0bb432d4117582f00f19869d40e6e57c7bac5fee899d5fc1166334a  aws_r6d_reverse/worker.metadata
cc4bb6495a82fe4decc477965ed74e150331ea21f88fe33926ec720d22c50c75  aws_r6d_reverse/worker_finished_utc.txt
a1c5caee972698b41c7cff534086d291a78cd04a29e61aab95be8f3e1a2058b8  aws_r6d_reverse/worker_started_utc.txt
ea38710ed3b11a58dac050430ba421dcec902def645f59da28c2d9418c60c247  compile_hq_linear_filtered_lift_v8.py
2c088b57feb6788aef6c59d6d2b5ab1f40e9ad5c21e54af660ab5c1d517bad4a  remote_worker.sh
```

Source-closure entries, all matched from the package root:

```text
00753f84e87dd91dce8dd0d45e9e0a25ba3d7cdbd1f57c61fa2632b7d1781d9f  PREREGISTRATION.md
d2170f4ea4c4c5d44a1680a913c6057bc86d9bff576ff9850a0d4d14ab1b0039  AWS_REGISTRATION.md
ea38710ed3b11a58dac050430ba421dcec902def645f59da28c2d9418c60c247  compile_hq_linear_filtered_lift_v8.py
2c088b57feb6788aef6c59d6d2b5ab1f40e9ad5c21e54af660ab5c1d517bad4a  remote_worker.sh
a4500936c83c82ef12d68c145ef6672688d401292c05dab36b95002df4138de3  ../max12_912_order3_d1_double_root_control2_h2_qr_syzygy_lift_v7_20260826/compile_h2_qr_syzygy_lift_v7.py
c7d9faed50b93cb7bb3905d8d386d2dc0f670c300baeefa78864d5dd3097dfce  ../max12_912_order3_d1_double_root_control2_h_grade5_kernel_lift_v6_20260826/compile_h_grade5_kernel_lift_v6.py
8a963360f16a29c6841050f82e9eb79051005d821c6ec7837d0614ca8ead7366  ../max12_912_order3_d1_double_root_control2_h_qr_syzygy_lift_v5_20260826/compile_h_qr_syzygy_lift_v5.py
3bbf1ebfb9f8b15054fe2f592bea92d8e07b95bce4d6ca131cd81c95f3698306  ../max12_912_order3_d1_double_root_control2_h_first_transport_v4_20260826/compile_h_first_transport_v4.py
c76ef85ac14f81839674368c55a324499832e6cf4b589befa68baf93a42b1490  ../max12_912_order3_d1_double_root_toric_blowup_20260825/compile_toric_blowup.py
0385b0b1e60b3bd37fa5fbee90dd6c17a454722bdbff424ea83c2ab0fa19df45  ../max12_912_order3_d1_double_root_control2_q2_first_lift_v1_20260826/compile_q2_first_lift.py
67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623  ../max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/independent_reconstruct.py
```

Harvested `SOURCE_CLOSURE.sha256` is byte-identical to the top copy on both hosts. Both `source.check` files are identical (`cd14de3f…`) and print `OK` on those eleven paths. The worker `cd`s to `$run` before `sha256sum -c SOURCE_CLOSURE.sha256`. The compiler locates V7 via `HERE.parents[1]/cases/…`, so `$run` is a `cases/`-child (the package, or a copy sitting as a `cases/` neighbour). Dual AWS both passed the sibling-path hash check. Treating `aws_box03_forward/` or `aws_r6d_reverse/` as a new source root would make those siblings invisible. That is not the charged root.

The compiler pins V7 at `V7_SHA=a4500936…` and refuses a non-matching file before import. V7 re-pins V6 at `c7d9faed…`; V6 re-pins V5 at `8a963360…`; V5 re-pins V4 at `3bbf1ebf…`; V4 re-pins toric `c76ef85a…`, V1 `0385b0b1…`, and `independent_reconstruct.py` at `67343b56…`. Tag gates: worker `case` requires prefix `max12_912_order3_d1_double_root_control2_hq_linear_filtered_lift_v8_20260826T*`; compiler `require_aws` requires Linux, DMI vendor `Amazon EC2`, and tag prefix `max12_912_order3_d1_double_root_control2_hq_linear_filtered_lift_v8_`. Both refuse non-`forward`/`reverse` orders.

| Check | Box03 forward | r6d reverse |
|---|---|---|
| Public IP / harvested hostname | `98.80.65.144` / `ip-172-30-0-249` | `100.26.198.153` / `ip-172-30-0-45` |
| Tag | `…_v8_20260826T043000Z_box03_forward` | `…_v8_20260826T043000Z_r6d_reverse` |
| Worker PID | `158757` | `226117` |
| Caps | `memory_kib=4194304`, `timeout=900`, `nice -n 10`; `ulimit -v 4194304` | same |
| Order | `forward` (`ell=1..8`, `F*E`) | `reverse` (`ell=8..1`, `E*F`) |
| Started / finished UTC | `2026-08-26T04:31:11Z` / `04:32:00Z` | `04:31:11Z` / `04:32:00Z` |
| Compiler stdout SHA | `b13fc17a…` | `b524c003…` |
| Certificate SHA | `574c1969…` | `f4fb41f6…` |
| RSS / swap / exit | 22384 KiB / `Swaps: 0` / 0 | 22468 KiB / `Swaps: 0` / 0 |
| Pre/post `free` swap | `0B` / `0B` | `0B` / `0B` |
| Elapsed | 5.92 s | 5.91 s |
| PASS markers, each once | `PASS_HQ_LINEAR_FILTERED_LIFT_V8_SOLVABLE`, `PASS_REMOTE_WORKER` | same |
| `FAIL_` / `REFUSED` / `FAILED` | none; stderr empty; no `REFUSED`/`FAILED` files | none; stderr empty; no `REFUSED`/`FAILED` files |

`AWS_LAUNCH_METADATA.md` local mtime is `2026-08-25T21:31:41 PDT` = `2026-08-26T04:31:41Z`, after worker start (`04:31:11Z`) and after the metadata text's observation stamp `2026-08-26T04:31:34Z`. Content: both workers `WAITING_GO`; “Neither run directory contained a GO sentinel”; source-closure manifest SHA `b3b38b28…` matching the frozen file. GO sentinels exist and are empty. DONE UTC stamps match finish (`04:32:00Z` both). No `REFUSED` or `FAILED`. The 49-second start-to-finish window contains the wait-for-GO loop, the post-GO source-hash check, and the 5.92 s compile.

Harvest copies of compiler, worker, preregistration, AWS registration, and source closure are byte-identical to the package top on both hosts (`cmp`). The two JSON files are **not** byte-identical (75594 vs 75592 bytes; the 2-byte gap is `box03_forward` vs `r6d_reverse` in the tag). Their key sets are equal (30 keys). The only value differences are the two preregistered custody fields `tag` and `order`. Deleting those fields and dumping with `sort_keys=True, indent=2` plus a trailing newline yields one 75461-byte blob of SHA

```text
7bae4055e967eaa29831415a1432b04016747759ea56c62b55e4002f1f7e6c0b
```

on both hosts, matching `RESULT.md` and the charged semantic-equality SHA. Compiler stdout differs only in the preregistered `ORDER=` line and the certificate SHA of the tagged JSON; the algebraic metric block is identical:

```text
STATUS=SOLVABLE
SOLUTION=0,-1/36,0,0,0,-1/72,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
PROJECTED_RANK=9
CORRECTED_WITNESS_SHA256=e549fd6879763d9f6804b9fcc17327e114bd54e29180246cc0b2e7c632fff38b
ETA_UNIFORM_INFIMUM=0
ETA_EQUAL_OPEN_STRICT=1
PASS_HQ_LINEAR_FILTERED_LIFT_V8_SOLVABLE
```

Every extra toric variable `p,c,a,x,y,k,mu,nu` is zero on all 48 recorded terms. Support is exactly `{h,la,tau,q2,q1,q0,r2,r1,r0}`.

---

## Charge 2 — Literal reconstruction of the reviewed V7 witness

**CONFIRMED. The V8 source reconstructs `W^(7)=sum_i (F_i'+h g_i+h^2 d_i) E_i(h)` from the frozen ordinary rows, the reviewed q2 correction, the V6 scalar-`h` correction `G1=(5/2,-25/18,0,1/4,-1/3,0,0,0)`, and the V7 scalar-`h^2` correction `D2=(5/24,-2/9,0,0,0,0,0,0)`. Dual AWS both fail-close on the V7 57-term digest `efe2ebcc…` and the reviewed `h=0` digest `ddb451c4…` before forming any column. The compiler does not read a row JSON and cannot substitute a hand-refactored row system.**

Construction, from the hash-pinned V8 compiler, which loads the hash-pinned V7 compiler, which loads the hash-pinned V6/V5/V4/toric/V1 chain:

1. `t.load_charged_source().build()["tails"]` is the eight negative Laurent tails of `independent_reconstruct.py` at `67343b56…`, in names `(a0..a7,k)`. Same charged ordinary-tail source as the reviewed V7/V6/V5/V4 lifts.
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

3. Substitute tails; subtract row-3 target `(2/3) la^15` and row-8 target `la^20(1+tau)`; no row-6 `nu` subtraction. Multipliers from V1 with `F1+=q2/12`, `F2+=-q2/9`, then `F_i^(7)=embed(F_i')+g_i h+d_i h^2` with hardcoded `G1` loaded from `v7.G1` and hardcoded `D2` matching the reviewed V7 free-zero solution.
4. `w7 = sum_ell F_ell^(7) E_ell(h)` over the same `forward`/`reverse` index list, with opposite multiply order (`F*E` vs `E*F`). Fail-closed, in this order, before any column is formed:

```text
digest(project_base(w7|_{h=0})) = ddb451c4…          # reviewed W'
digest(w7)                       = efe2ebcc…          # V7 57-term identity
qr_component([h^1] w7)           = 0
grade5_component([h^1] w7)       = 0
```

`G1` is the reviewed V6/V7 scalar-`h` vector. `D2` is the reviewed V7 scalar-`h^2` vector. V8 does not read the V7 JSON; it reconstructs from frozen source plus these pins, then refuses any other 57-term polynomial.

Independent reading of the frozen V7 57 records (not a compiler replay):

- Toric digest of all 57 terms: `efe2ebcc234d836763a8a47f58a228f6a90cc20fd876bb48b1144a60f3e5d6a5`. Stored V7 `corrected_witness_sha256` and V8 `w7_sha256` match.
- `h`-exponent histogram `{0:37, 1:18, 2:2}`. Maximum `h` is 2; no `h^3`.
- `h=0` slice: 37 terms, dictionary-equal to the V8 `h=0` slice (empty symmetric difference, empty coefficient mismatch) and to the reviewed V4 `h=0` slice. V1 digest `ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b`. Extra toric variables are zero, so the projection to the V1 ring is literal.
- Among the 18 h-linear terms of V7, the Q-degree 2, R-degree 1, no-other-factor subset is exactly eight. Zero of those 18 are Q-R (`q=1,r=1`) or grade-5 (`(q,r) in {(0,2),(3,0)}`).

Dual AWS of V8 both exited 0 after those fail-closed checks, opposite traversal. That is the custody that V8 reconstructed the V7 identity rather than loading a stale certificate. Recorded `rows_full_sha256` / `rows_h0_sha256` / `v7_multiplier_sha256` are outputs of that reconstruction, not inputs. Row 1 has `rows_full[0]=rows_h0[0]`; row 3's V7 multiplier digest is the empty-polynomial digest `4f53cda1…` (`sha256(b"[]")`), matching `F3^(7)=0`. This review did not replay the eight-row product.

A hand-refactored row system would have to reproduce the charged tails, the V4 images, the two load subtractions, the V1 multipliers, `G1`, and `D2` simultaneously, and still hash to `efe2ebcc…`. The compiler has no alternate row path.

---

## Charge 3 — Exact 24 columns; projected union; eight-term input `Q^2 R`

**CONFIRMED. The 24 columns are exactly `h q_j E_i(0)` for `i=1..8` and `q_j in {q2,q1,q0}` in the stated nested order. The projector is the disjoint union of Q-R, `R^2/Q^3`, and `Q^2 R`. The emitted matrix support is the complete 18-dimensional `Q^2 R` grade; the two earlier grades are included as zero targets. The input h-linear `Q^2 R` piece has exactly eight terms, each of closed-corner pre-`h` margin `-5/2`, SHA `6c42c451…`.**

Column labels, 24 of them, in compiler order `for ell in 1..8 for qvar in (q2,q1,q0)`:

```text
(1,q2), (1,q1), (1,q0), (2,q2), (2,q1), (2,q0),
(3,q2), (3,q1), (3,q0), (4,q2), (4,q1), (4,q0),
(5,q2), (5,q1), (5,q0), (6,q2), (6,q1), (6,q0),
(7,q2), (7,q1), (7,q0), (8,q2), (8,q1), (8,q0).
```

Each source is `projected_union(q_j * E_i(0))` with opposite multiply order. `projected_union` is literally `qr_component + grade5_component + q2r_component`. `q2r_component` keeps a monomial iff `q2+q1+q0=2`, `r2+r1+r0=1`, and every other exponent is zero. `qr_component` is q-degree 1 and r-degree 1; `grade5_component` is `(q,r) in {(0,2),(3,0)}`.

Fail-closed on the target, before RREF: `[h^1] W^(7)` has vanishing Q-R and grade-5, so `target_union = -q2r([h^1] W^(7))`. That piece must have eight terms, each of closed-corner value `(la-20)+5(q-sum)+(15/2)(r-sum)=-5/2`.

Independent extraction from the frozen V7 records (18 terms with `h=1`). Among those 18, the Q-degree 2, R-degree 1, no-other-factor subset is exactly eight; there is no h-linear `Q^2 R` term with an extra factor. Coefficients and monomials, `h` restored:

```text
 +1/162 h q0^2 r1      c = -5/2
 +1/162 h q0 q1 r0     c = -5/2
 +5/162 h q0 q1 r2     c = -5/2
 +1/81  h q1^2 r1      c = -5/2
 +1/54  h q0 q2 r1     c = -5/2
 -1/81  h q0 q2 r2     c = -5/2
 +1/81  h q1 q2 r0     c = -5/2
 +1/27  h q1 q2 r2     c = -5/2
```

Stripping the `h` factor recovers V8 `h_q2r_terms` as an equal list of toric canonical triples. Recomputed digest `6c42c451732eba42d43402f2175510dc87b901fe986d82f500c4bdb9c1b0048b`, matching V8 `h_q2r_sha256`, both JSON payloads, and `RESULT.md`. These are the same eight V7 extremals at eta-infimum `5/2` (`E=1`, `-c/E=5/2`).

Emitted `projected_monomials` is the complete 18-element set of `Q^2 R` monomials (every exponent vector with q-degree 2, r-degree 1, no extra factor), sorted as tuples, and containing no Q-R monomial, no `R^2/Q^3` monomial, and no extra name. The two earlier grades do not appear as rows because they are the zero polynomial on every one of the 24 columns and on the target: multiplying `E_i(0)` by `q_j` sends Q-R into `Q^2 R` and sends `R^2/Q^3` out of the union (`q R^2` and `Q^4`). Including them in the projector still forces any accidental Q-R or grade-5 image to hit a zero target; dual AWS both exited 0 after `target_union == -target_q2r`. Columns 15–17 (row 6, all three `q_j`) have the empty-polynomial source digest `4f53cda1…`, matching the reviewed V5 fact that `QR(E_6(0))=0` and, after `*q_j`, the projected union remains empty.

---

## Charge 4 — RREF rank 9, free-zero solution, only two nonzero additions, projected residual zero

**CONFIRMED. Stored RREF of the 18-by-25 augmented matrix has rank 9 and pivots `(0,1,2,3,4,5,6,7,8)`. The canonical free-zero solution has exactly two nonzero coordinates: `(row 1, q1)=-1/36` and `(row 2, q0)=-1/72`. Adding those `h q_j` terms preserves the `h=0` slice and cancels the entire named projected union. Certificate field `residual_projected_union_terms=0` matches.**

The linear system, from the hash-pinned compiler, is

```text
sum_{i,j} x_{i,q_j} * projected_union(q_j * E_i(0))
  = -projected_union([h^1] W^(7))
  = -Q2R([h^1] W^(7))
```

over `Q`, with exact RREF and free columns set to zero. The emitted augmented RREF is 18-by-25. Nonzero rows:

```text
[ 1  0  0  0  0  0  0  0  0  -4/3  0    0    1    0    0   0 0 0  -10/9  0     0     4/3   0    0  |  0    ]
[ 0  1  0  0  0  0  0  0  0   0   -4/3  0    0    1    0   0 0 0   0    -10/9  0     0     4/3  0  | -1/36 ]
[ 0  0  1  0  0  0  0  0  0   0    0   -4/3  0    0    1   0 0 0   0     0    -10/9  0     0    4/3|  0    ]
[ 0  0  0  1  0  0  0  0  0   1    0    0   -2/3  0    0   0 0 0   2/3   0     0    -7/9   0    0  |  0    ]
[ 0  0  0  0  1  0  0  0  0   0    1    0    0   -2/3  0   0 0 0   0     2/3   0     0    -7/9  0  |  0    ]
[ 0  0  0  0  0  1  0  0  0   0    0    1    0    0   -2/3 0 0 0   0     0     2/3   0     0   -7/9| -1/72 ]
[ 0  0  0  0  0  0  1  0  0   0    0    0    0    0    0   0 0 0   0     0     0     0     0    0  |  0    ]
[ 0  0  0  0  0  0  0  1  0   0    0    0    0    0    0   0 0 0   0     0     0     0     0    0  |  0    ]
[ 0  0  0  0  0  0  0  0  1   0    0    0    0    0    0   0 0 0   0     0     0     0     0    0  |  0    ]
  ... nine further zero rows ...
```

Pivots, 0-based: columns `0..8`, i.e. all three `q_j` on rows 1, 2, and 3. Rank 9. Free columns `9..23` (rows 4 through 8, all three `q_j`). Setting the fifteen free variables to zero reads

```text
x_{(1,q1)} = -1/36,   x_{(2,q0)} = -1/72,
all other x = 0.
```

This is the stored `solution` (24 strings) and the stored `solution_sha256` `30a42126d2ac00d016e25ab1db9b01348a30f90926c91dc9089b515c2cc00b50` (recomputed from `json.dumps(solution, separators=(",",":"))`). Substituting that vector into every RREF row recovers the last column exactly (18/18). Signs and numbering: compiler does `F_ell^(8) = F_ell^(7) + x_{ell,q_j} h q_j` with `ell=1..8`, so the two nonzero additions are

```text
F1^(8) = F1^(7) - (1/36) h q1,
F2^(8) = F2^(7) - (1/72) h q0,
Fi^(8) = Fi^(7)  (i>=3),
```

matching `RESULT.md`. Dual AWS, opposite traversal, emit this same RREF and same solution. Multiplier-correction digests are nonempty only for rows 1 and 2; rows 3–8 are the empty-polynomial digest `4f53cda1…`.

Literal residual. Two independent readings, neither of which reconstructs original `A` locally:

1. Compiler fail-closed: after RREF it forms `sum x_s source_s` and refuses unless that equals `-projected_union([h^1] W^(7))`; then it forms the full product `sum F_i^(8) E_i(h)` and refuses unless `[h^0]` equals the V7 `h=0` slice and `projected_union([h^1] W^(8))` is empty. Dual AWS both exited 0.
2. Support comparison of the already-emitted polynomials, which does not require `A`. V7 contains exactly the eight h-linear `Q^2 R` monomials of Charge 3 and no other h-linear `Q^2 R` monomial. V8 contains none of those eight, no new `Q^2 R` monomial of any `h`-degree except that the V7 leftover `-1/162 h^2 q0 q2 r2` is also deleted, and in particular no h-linear Q-R or `R^2/Q^3`. Certificate field `residual_projected_union_terms=0` matches. Among V8's 10 h-linear terms, zero are Q-R, zero are grade-5, zero are `Q^2 R`.

Original 18-by-24 entries are not a frozen array; only RREF, the 24 source digests, and the two polynomials are frozen. That is the same custody pattern as V5/V7. It is enough to verify this preregistered free-zero solution and its residual. It is **not** enough to classify the 15-dimensional kernel as a theorem of this package, or to assert module-support completeness beyond the stated projection.

---

## Charge 5 — The 48-term polynomial is the exact product, not a truncation

**CONFIRMED. The 48-term polynomial SHA `e549fd68…` is an exact identity `W^(8)=sum_i F_i^(8) E_i(h)`, not a filtered truncation of `W^(7)` and not a congruence. The `h=0` slice is dictionary-equal to V7/`W'`. Five surviving coefficients change. The unique leftover `h^2` term is the V7 monomial `-1/486 h^2 q1 q2^3`. No hidden moving `a,p,c,k,mu,nu,x,y`. Target `la^20` has coefficient `+1`; split `la^20 tau` has coefficient `+1`.**

Lower-`h` preservation, dictionary-level, V7 records vs V8 records:

```text
h=0:  37 vs 37, keys equal, coefficient mismatch 0
```

The V8 `h=0` slice is additionally dictionary-equal to the reviewed V4 37-term `W'` (V1 digest `ddb451c4…`). Compiler fail-closed `coefficient_h(corrected,0)==w0`.

Exact identity vs V7, full support:

```text
only in V7 (9):  the eight Charge-3 h-linear Q^2 R monomials, plus
                   -1/162 h^2 q0 q2 r2
only in V8 (0):  none
common equal (43):  43 coefficients equal
changed (5):
  1/81  h q0 r2^2       -> 1/108
  1/243 h q1^2 q0 q2    -> 1/162
 -2/243 h q0^2 q2^2     -> -1/162
  5/243 h q1^2 q2^2     -> 2/81
 -4/243 h q0 q2^3       -> -1/81
```

V8 is V7 with those nine monomials deleted and five survivors rewritten. A truncation of V7 that only deleted the eight named `Q^2 R` terms would leave the five coefficients and the `h^2 q0 q2 r2` term untouched. Combined with dual-traversal agreement on the full 48-term digest, this is an exact polynomial identity, not a filtered truncation and not a congruence modulo `h^2`. The extra `h^2` deletion and the five coefficient changes are collateral from `E_i(h)` having more than the `h=0` piece; they are not a defect in the named cancellation.

Recomputed toric digest of all 48 V8 records: `e549fd6879763d9f6804b9fcc17327e114bd54e29180246cc0b2e7c632fff38b`. Stored `corrected_witness_sha256` matches on both hosts and is the charged corrected-witness SHA. Residual `[h^1]` has ten terms, SHA `ee12f002fd4b617ac5bb900cc2f6ca4317d042423ecc5e9953c4cf2679b3646e`, matching `corrected_c1_sha256` / `corrected_c1_terms=10`. Residual `[h^2]` has one term, already present in V7 with the same coefficient:

```text
-1/486 h^2 q1 q2^3      c=0     E=2
```

`h`-exponent histogram of V8: `{0:37, 1:10, 2:1}`. Maximum `h` is 2. Roles: one target `la^20` (coefficient `1`) and one positive split `la^20 tau` (coefficient `1`); 46 charged terms. `37+10+1=48`.

Support mask: every recorded exponent of `p,c,a,x,y,k,mu,nu,rho` is zero; `tau` appears only on the split target; `la` appears only on the two target monomials. No hidden moving axis, cusp, or load.

---

## Charge 6 — All 48 weight forms; unique-target iff `eta>=0`

**CONFIRMED. The new witness is uniformly unique-target on `u>0`, `v>0`, `T>0` if and only if `eta>=0`. There is no negative eta-zero corner margin. All 30 non-target equality-face terms have a positive `u` or `v` slope. `la^20 tau` is strict for `T>0`. For `eta<0` an actual displayed `h`-positive zero-corner-margin term lies below target for sufficiently small positive `u` or `v`. The unique `h^2` term sits on that face with slope `u+3v` and does not create a negative-corner obstruction.**

Weight convention, matching the reviewed V7 / V6 / V5 / V4 / q2 sample after restoring `beta=5+u`, `delta=5+v` and `eta=wt(h)/L`, with `alpha` held at `15/2`:

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

Integer check, all 48 difference-forms against exponents: 48/48. Integer check, all 46 charged constants: the reduced fraction of `2(la-20)+10(q0+q1+q2)+15(r0+r1+r2)` over `2` equals the stored string, and `(U,V,E)=(q0+q1, q2, h)`, 46/46. No charged term has `tau>0` or `rho>0`. No charged term has `U<0`, `V<0`, or `E<0`. The two skipped monomials are `la^20` (target) and `la^20 tau` (strictly above once `T>0`). On the 46 charged terms the recorded form is therefore exact, and `T` enters uniqueness only through the skipped `la^20 tau`.

Histogram of the 46 charged terms by recorded `c`, split by `h`:

```text
c       count    h=0    h=1    h=2
 0        30     20      9      1
 5/2      11     10      1      0
 5         5      5      0      0
```

`30+11+5=46`. Relative to V7, the eight `c=-5/2` h-linear `Q^2 R` terms are gone, as is the leftover `c=-5/2` term `-1/162 h^2 q0 q2 r2`. **Zero charged terms have `c<0`.** Among `h=0` charged terms, 20 have `c=0` and 15 have `c>0`; zero have `c<0`. The old `W'` still does not itself break the open quadrant at this `alpha`.

For a term with `U,V,E >= 0`, uniqueness of least term `la^20` for all `u,v>0` at fixed `eta` holds iff every charged term satisfies either `c+E eta > 0`, or `c+E eta = 0` and `U+V > 0`. (If `c+E eta = 0` and `U=V=0`, the term ties `la^20` throughout the quadrant. If `c+E eta < 0`, sufficiently small positive `u,v` put it below target.) Increasing `u` or `v` cannot create a new below-target term, because `U,V >= 0`.

Verified on the 46 charged records:

- `E=0` and `c<0`: **0**. No negative eta-zero corner margin.
- `E=0` and `c=0`: **20**, every one with `U+V > 0` (in fact `U+V in {1,2,3,4}`). These are the 20 old closed-corner threshold monomials of `W'`.
- `E=0` and `c>0`: **15**, strictly above even at the closed corner, for every `eta`.
- `E>0` and `c<0`: **0**. No term has `-c/E` defined in the compiler's `thresholds` list. Stored `eta_uniform_infimum=0` is the `else Fraction(0)` branch of `analyze_threshold`, not a `max(-c/E)`.
- At `eta=0`: **0** terms with `c+E*0 < 0`; **30** with equality (20 old `E=0,c=0` plus 9 new `E=1,c=0` plus the one `E=2,c=0` `h^2` term). **0** of those 30 have `U=V=0`. Stored `threshold_face_terms` is this set of 30, key-equal to the independent classification. `eta_equal_infimum_is_strict_on_open_quadrant=true`.

All 48 recorded monomials, with charged form:

```text
# h=0, c=0 (20 old face)
 5/54    q2 r2^2            U=0 V=1 E=0
 1/9     q2 r1 r2           U=0 V=1 E=0
 4/81    q2 r1^2            U=0 V=1 E=0
 1/162   q2 r0 r2           U=0 V=1 E=0
 1/18    q2 r0 r1           U=0 V=1 E=0
-11/162  q2^4               U=0 V=4 E=0
 1/54    q1 r1 r2           U=1 V=0 E=0
 7/108   q1 r1^2            U=1 V=0 E=0
 1/54    q1 r0 r2           U=1 V=0 E=0
 1/108   q1 r0^2            U=1 V=0 E=0
 7/162   q1 q2^3            U=1 V=3 E=0
-4/81    q1^2 q2^2          U=2 V=2 E=0
-1/81    q1^3 q2            U=3 V=1 E=0
-1/54    q0 r0 r1           U=1 V=0 E=0
-2/27    q0 q2^3            U=1 V=3 E=0
 1/18    q0 q1 q2^2         U=2 V=2 E=0
-5/243   q0 q1^2 q2         U=3 V=1 E=0
-5/243   q0^2 q2^2          U=2 V=2 E=0
 5/162   q0^2 q1 q2         U=3 V=1 E=0
 1/243   q0^3 q1            U=4 V=0 E=0
# h=0, c=5/2 (10)
 1/81    q2^3 r2            U=0 V=3 E=0
-4/243   q2^3 r1            U=0 V=3 E=0
-1/54    q1 q2^2 r2         U=1 V=2 E=0
-5/162   q1 q2^2 r1         U=1 V=2 E=0
-1/54    q1^2 q2 r2         U=2 V=1 E=0
-1/486   q1^2 q2 r0         U=2 V=1 E=0
 5/162   q0 q2^2 r2         U=1 V=2 E=0
 1/243   q0 q2^2 r0         U=1 V=2 E=0
 1/486   q0 q1 q2 r1        U=2 V=1 E=0
 5/486   q0^2 q2 r2         U=2 V=1 E=0
# h=0, c=5 (5)
 4/2187  q2^5               U=0 V=5 E=0
-1/243   q1 q2 r2^2         U=1 V=1 E=0
 19/5832 q1 q2^4            U=1 V=4 E=0
 5/2916  q1^3 q2^2          U=3 V=2 E=0
-1/1458  q0 q1 q2^3         U=2 V=3 E=0
# targets
 1       la^20              target
 1       la^20 tau          positive_split_target
# h=1, c=0 (9 new face)
-1/324   h q2^4             U=0 V=4 E=1
-1/54    h q1 r1 r2         U=1 V=0 E=1
 2/243   h q1 q2^3          U=1 V=3 E=1
 2/81    h q1^2 q2^2        U=2 V=2 E=1
 1/486   h q1^4             U=4 V=0 E=1
 1/108   h q0 r2^2          U=1 V=0 E=1
-1/81    h q0 q2^3          U=1 V=3 E=1
 1/162   h q0 q1^2 q2       U=3 V=1 E=1
-1/162   h q0^2 q2^2        U=2 V=2 E=1
# h=1, c=5/2 (1, outside the projection: Q^3 R)
 2/243   h q1 q2^2 r2       U=1 V=2 E=1
# h=2, c=0 (1, the leftover Q^4 term)
-1/486   h^2 q1 q2^3        U=1 V=3 E=2
```

The unique `h^2` term `-1/486 h^2 q1 q2^3` has `c=0`, `E=2`, `U=1`, `V=3`. It is Q-degree 4, so it is outside the 24-column projection. At `eta=0` it sits on the equality face with open-quadrant margin `u+3v`. It does **not** have negative corner margin. The V7 leftover `-1/162 h^2 q0 q2 r2` (`c=-5/2`, `E=2`, ratio `5/4`) would have been a negative-corner term at `eta=0`; the exact product deleted it as collateral, so no such term remains.

Hence the iff, charged on all 48 terms:

- If `eta > 0`, every charged term has `c+E eta > 0` except the 20 old `c=0` `h=0` terms, which have `c+E eta=0` and `U+V>0`. Unique least term `la^20` throughout the open quadrant. The 10 `h`-positive `c=0` terms sit strictly above by `E eta`.
- If `eta = 0`, the same, with those 10 `h`-positive `c=0` terms now on the threshold face; each has margin `U u + V v` with `U+V in {1,4}`. Every one of the 30 face terms has `U+V>=1`. Equality at `u=v=0` is strict for `u,v>0`. `la^20 tau` remains strictly above by `T>0`.
- If `eta < 0`, each of those 10 `h`-positive `c=0` terms has `c+E eta = E eta < 0`. They are present (nonzero coefficients). None carries `tau` or `rho`. Choosing the relevant `u` or `v` in `(0, |eta| E / max(U,1))` (and the other coordinate any positive number) puts that term strictly below target. The `h^2` term does this with slope `u+3v` against `2|eta|`; any of the nine `h`-linear face terms does it against `|eta|`.

This is the exact iff, not a statement about a displayed subset. The infimum of uniform unique-target eta is `0`, and equality is strict on the open quadrant. Stored `eta_uniform_infimum=0` and `eta_equal_infimum_is_strict_on_open_quadrant=true` match. Negative eta is a next-lift problem: some displayed `h`-positive zero-corner-margin term wins after its positive `u/v` margin is taken sufficiently small. It is not a surviving branch of this chart.

The compiler's `eta0 = max(-c/E)` loop does not, by itself, inspect `U,V` on the threshold face, and with no `c<0` it returns 0 without looking at the `E>0,c=0` terms. The certificate stores the 30 face monomials, all of which have `U+V>0`; this review charged that. The open-quadrant strictness and the converse for `eta<0` are in the records, not only in the `max` reduction.

---

## Charge 7 — Weight theorem versus 24-column completeness; firewall

**CONFIRMED. The licensed theorem is the Promotion paragraph. The 24-column RREF is complete only for the stated three-grade projection of the 24 columns `h q_j E_i(0)`. The weight conclusion scans every term of the resulting full polynomial identity. Moving axis/cusp, moving loads, omitted normal directions, a formal neighbourhood, the whole double-root fan, D1, and JC2 remain open.**

Admissible:

- For `eta>=0`, this explicit 24-column-corrected combination `W^(8)` has unique least term `la^20` uniformly on `u>0`, `v>0`, `T>0`, at the fixed axis/cusp chart `a=1`, `p=-3`, `c=2+h`, loads `k=nu=0`, `mu=2/3`, and full `Q,R` support.
- This improves the V7 range `eta>=5/2` to `eta>=0` by one preregistered 24-column `h q_j` correction of the complete projected h-linear union of Q-R, `R^2/Q^3`, and `Q^2 R`.
- For `eta<0`, the same polynomial does **not** transport uniformly. Ten present `h`-positive zero-corner-margin terms, including the one `h^2` term, fall below target for sufficiently small positive `u` or `v`. Those cells require a further correction if they are to be charged. They are not surviving branches.
- The weight theorem does not require the 24 columns to exhaust the row module. It requires only that this explicit product, whose every coefficient is recorded, have the stated least-weight property. Collateral cancellation of `-1/162 h^2 q0 q2 r2` is a fact about that product, not a claim that `h^2 Q^2 R` was in the linear system.

Not admissible, and not claimed by the frozen firewall string
`exact 24-column h*Q correction through Q-R, R2/Q3, Q2R grades; other multiplier supports and later h grades remain open`
and `RESULT.md` §Firewall:

- completeness of any multiplier support other than the 24 columns `h q_j E_i(0)` (for example `h r_j`, `h^2`, `q_i q_j`, or a different grade);
- a claim that the 24-column search exhausts the eight-row module, or that omitted normal directions have been activated;
- a classification of `eta<0`, or a newly corrected witness on that half-line;
- an `h`-adic or formal lift, a formal neighbourhood, or any statement about coefficients of `h^3` and higher as a completed jet;
- moving axis, moving loads, or a theorem that the unit-axis map acts on the submitted rows (`p` is fixed at `-3`, `c=2+h` is the charged cusp, loads are `k=nu=0`, `mu=2/3`);
- equality-support analysis of the 30 face monomials beyond their recorded weights;
- another normal direction;
- a formal-arc / formal-lift obstruction;
- the whole double-root fan, D1, or JC2;
- a claim that V4/V5/V6/V7 already settled the h-linear `Q^2 R` cell (they did not; that is this package).

The reviewed V7 lift remains valid as a scalar-`h^2` Q-R correction of `[h^2] W_V6`. The V7 identity remains the 57-term input of this package. This package classifies only the weight behaviour of one explicit 24-column `h q_j` correction of that input, and only on the stated projection for the linear algebra.

---

## Nits, not defects

1. Harvest trees contain sentinels, `free.*`, `hostname`, `uname`, `nproc`, UTC stamps, and empty launch stdio, all of which *are* in this package's `FREEZE.sha256` (unlike V7, which froze 23 paths). Local GO/DONE mtimes (`04:35:52Z` / `04:35:54Z` after converting PDT) are about four minutes after the AWS UTC finish stamps `04:32:00Z`; those mtimes are harvest-copy times, not a second GO. The UTC files internally cohere with pre-GO metadata at `04:31:34Z` and a 5.92 s compile.
2. `AWS_LAUNCH_METADATA.md` does not restate that `$run` is the package under the job root's `cases/`. The compiler's `HERE.parents[1]/cases/…` resolution, the harvested `source.check` OK-lines on the eleven sibling paths, and dual-AWS hash agreement pin that layout.
3. V8 does not separately pin the V7 18-term h-linear digest `6fee8f42…`. It pins the full 57-term digest `efe2ebcc…`, which contains that slice, and this review independently extracted the eight-term `Q^2 R` piece from the frozen V7 records.
4. Original 18-by-24 projected-matrix entries are not serialized. RREF, the 24 `column_source_sha256` digests, and the two polynomials are frozen. Same pattern as V5/V7; enough for this free-zero solution; not enough for a kernel-completeness theorem.
5. The compiler's `eta0 = max(-c/E)` loop returns 0 by the empty-threshold branch. The converse for `eta<0` lives in the 10 recorded `E>0,c=0` face monomials, which this review charged. The open-quadrant strictness is in the records, not only in the `max` reduction.
6. r6d `free` shows 137 GiB used vs box03 28 GiB; swap is zero on both, and this job's RSS is 22 MiB under a 4 GiB `ulimit -v`. Registration leaves unrelated r6d work untouched. That is not evidence that another campaign job was stopped, and not a defect in this package.
7. Nine V7 monomials are deleted and five survivors change, as collateral of the exact product. `RESULT.md` does not claim those collateral edits as the named target; the named target is the eight-term h-linear `Q^2 R` piece, which is entirely cancelled, together with vanishing of the two earlier projected grades.
8. The emitted `projected_monomials` list is the complete `Q^2 R` grade only. Q-R and `R^2/Q^3` are in the projector and are the zero polynomial on this column set, so they do not appear as rows. That is the correct matrix of this support, not a silently dropped grade.

No source or certificate repair is required.

HQ_LINEAR_FILTERED_LIFT_CONFIRMED
