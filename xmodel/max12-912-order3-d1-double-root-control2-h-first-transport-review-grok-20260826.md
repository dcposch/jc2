# Hostile text-only review — control-2 first transverse-cusp `h` transport V4

| Field | Value |
|---|---|
| Claim under review | Exact weight behaviour of the unchanged corrected eight-row witness after restoring one cusp coordinate `h` via `p=-3`, `c=2+h`: unique least term `la^20` uniformly for all `u,v>0`, `T>0` if and only if `eta>=15/2`; below that threshold the same polynomial is only a negative control |
| Overall verdict | **H_FIRST_TRANSPORT_CONFIRMED**. Dual AWS encodings emit one byte-identical 98-term certificate. The `h=0` slice is the literal reviewed 37-term `W'` (`ddb451c4…`). Integer arithmetic on all 98 recorded forms proves the iff. The eight `h`-linear extremals have open-quadrant margins `v` or `u` at `eta=15/2`. `OLD_CORRECTED_WITNESS_DOES_NOT_TRANSPORT_UNIFORMLY` for `0<eta<15/2` is a negative result about this witness, not a surviving branch |
| Smallest failing identity | none in the frozen V4 source, either harvest tree, or either AWS stream |
| Smallest missing hypothesis for a stronger theorem | a newly corrected `h`-witness (new multipliers) on the low-eta cells; moving axis or moving loads with independently proved target/load transformations; equality-support faces; another normal direction; a formal arc; the whole double-root fan; D1; or JC2 |
| Evidence tier | SHA-256 of the freeze chain and already-emitted AWS files; `cmp` of harvest copies against package-top source and of the two certificates; integer arithmetic on every recorded `(c,U,V,E)`; text-split dictionary equality of the `h=0` slice against reviewed V2 `EXPECT`; canonical-JSON hashes of that slice and of the 61-term `h`-correction. No local Singular, Sage, msolve, gfan, Lean, Python algebra, compiler execution, charged reconstruct, or eight-row product replay |
| Reviewer / model | Grok 4.6 (xAI). Text-only tropical / commutative-algebra / CAS-custody referee |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `574e873d4753b57dbaeb0fb83e320fbef3694724` |
| Host | Darwin. V4 compiler, V1 compiler, toric compiler, charged reconstruct, Singular, and every solver were not run |

## What was and was not run

No local substantive computation was run. In particular this review did **not** execute `compile_h_first_transport_v4.py`, `compile_q2_first_lift.py`, `compile_toric_blowup.py`, `independent_reconstruct.py`, Singular, Sage, msolve, Lean, Gfan, or any other solver, and it did not re-multiply `sum F_i' E_i(h)`. Hashes were checked with `shasum -a 256`. File identity was checked with `cmp`. Marker counts used `grep -c`. Git identity was read with `git rev-parse`. JSON fields were read with `jq`. Recorded weight forms were checked by integer arithmetic (`2c = 2(la-20)+10(q0+q1+q2)+15(r0+r1+r2)`). Canonical SHA-256 values of the already-emitted `h=0` slice (V1 digest format) and of the `h`-decremented correction (toric canonical format) were recomputed from the frozen certificate records. The reviewed V2 `EXPECT` body was split as text and compared as a dictionary of `(coefficient, monomial)` pairs.

Charged freeze SHA-256, recomputed and matched:

```text
0ff05368ab7a5751617db6a6b9a31e67545439ed5fb688cb15238ef879637b68  FREEZE.sha256
6ddb1343c7b30d0e4e6daf7e5f13ea364205e1a776c60534d02da26a7c529f14  RESULT.md
93dd031f5d523085d166d7382490f05652261af1ccd281a51aeb88994baeb425  each h_transport.json
```

Prerequisite q2-lift review, recomputed and matched:

```text
2a2ff048c299a8878ea28211b72f0d0ad98f27216ae5c3462eb3bc076083ac7d
  xmodel/max12-912-order3-d1-double-root-control2-q2-syzygy-lift-review-grok-20260826.md
```

Every path listed in `FREEZE.sha256` recomputed and matched (23/23). Nested `SOURCE_CLOSURE.sha256` (7/7) and both harvested `result.sha256` manifests (5/5 each) matched from the case root / harvest directory as appropriate. Empty compiler stderr files are the empty-string digest `e3b0c442…`. Both rc files are the two-byte string `"0\n"`, digest `9a271f2a…`.

Read in full before the verdict: every file at
`cases/max12_912_order3_d1_double_root_control2_h_first_transport_v4_20260826/`
including both harvest trees; the hash-pinned V1 compiler `coefficient_images` / `multipliers`; the hash-pinned toric `NAMES` / `canonical` / `load_charged_source`; charged `independent_reconstruct.py` far enough to see that `build()` returns eight negative Laurent tails in `(a0..a7,k)`; V2 compiled `EXPECT`; and the prerequisite review named above. Predecessor conclusions were recomputed, not inherited.

---

## Promotion

**Accept `FOR THE PINNED ORDINARY-TAIL EIGHT-ROW MODULE AT a=1, p=-3, c=2+h, k=nu=0, mu=2/3, FULL Q AND R, AND THE UNCHANGED CORRECTED MULTIPLIERS F1'=F1+q2/12, F2'=F2-q2/9, Fi'=Fi (i>=3), THE REGISTERED DUAL-AWS V4 RUNS EMIT ONE 98-TERM POLYNOMIAL W_h WHOSE h=0 SPECIALIZATION IS THE REVIEWED 37-TERM W' (SHA ddb451c4…). NORMALIZE wt(la)=L, PUT alpha=15/2, beta=5+u, delta=5+v, eta=wt(h)/L, AND RESTRICT TO u>0, v>0, T>0. THEN W_h HAS UNIQUE LEAST-WEIGHT TERM la^20 FOR EVERY SUCH (u,v,T) IF AND ONLY IF eta>=15/2. AT eta=15/2 EVERY CLOSED-CORNER EQUALITY IS STRICT IN THE OPEN QUADRANT. FOR EVERY 0<eta<15/2 SOME ACTUAL PRESENT TERM FALLS BELOW TARGET FOR SUFFICIENTLY SMALL POSITIVE u OR v. THE TOKEN OLD_CORRECTED_WITNESS_DOES_NOT_TRANSPORT_UNIFORMLY APPLIES ONLY ON THAT OPEN SUB-THRESHOLD INTERVAL AND ONLY TO THIS UNCHANGED WITNESS.`**

Do not promote this to: a low-eta existence statement; a newly corrected `h`-witness; a moving-axis or moving-load theorem; an equality-support face; another normal direction; a formal-arc obstruction; a whole double-root fan; D1; or JC2. The ordinary row-homogeneity checksum and the displayed unit-axis covariance are checksums, not that theorem.

---

## Charge 1 — Custody, freeze, dual AWS, source closure

**CONFIRMED. Every freeze entry recomputes. Both registered workers are fail-closed, hash-gated, empty-stderr, sub-cap, pre-GO, and source-closed against the package-root manifest. Opposite traversal orders returned byte-identical certificates.**

Required anchors, recomputed:

```text
6ddb1343c7b30d0e4e6daf7e5f13ea364205e1a776c60534d02da26a7c529f14  RESULT.md
0ff05368ab7a5751617db6a6b9a31e67545439ed5fb688cb15238ef879637b68  FREEZE.sha256
93dd031f5d523085d166d7382490f05652261af1ccd281a51aeb88994baeb425  aws_box03_forward/h_transport.json
93dd031f5d523085d166d7382490f05652261af1ccd281a51aeb88994baeb425  aws_r6d_reverse/h_transport.json
```

Recomputed `FREEZE.sha256` entries, all matched:

```text
6ddb1343c7b30d0e4e6daf7e5f13ea364205e1a776c60534d02da26a7c529f14  RESULT.md
a4a254891a2e60378c6ae8cc068740376a6768c0f31bba8576f2636b51163188  PREREGISTRATION.md
6102c79f353a640eba0a571309886c89f16633bd445b8862cfeed631b896a17f  AWS_REGISTRATION.md
d71342c1c60206b33068bebb03643ce020da46a3383dcdcd332b1316178a1b9f  AWS_LAUNCH_METADATA.md
817f45ebc4b87beaff940124994b79294472aba89f392a8ce41c20641d1abc12  SOURCE_CLOSURE.sha256
3bbf1ebfb9f8b15054fe2f592bea92d8e07b95bce4d6ca131cd81c95f3698306  compile_h_first_transport_v4.py
7b192697f862386daa328c088b4c827b2a9baa069e55cd86a732c4fcf70d9425  remote_worker.sh
93dd031f5d523085d166d7382490f05652261af1ccd281a51aeb88994baeb425  aws_box03_forward/h_transport.json
1bdd9e87d9defce728301ff9eecfb675012edf9fe8e6894d3430917c9563eb2a  aws_box03_forward/compiler.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_box03_forward/compiler.stderr
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  aws_box03_forward/compiler.rc
b62acdfb8e5ec890cc00fd7393f10a3095a12690ebe76a954b82fde076103f6e  aws_box03_forward/compiler.time
01efaa20391fa07836cbf7b451258cc4c53cfcd2a533586d6c32583622adc02a  aws_box03_forward/result.sha256
25b9201b64d9002b7791646259b69a09019c4dc230e07455fc9610753aa06a7e  aws_box03_forward/source.check
277cf9e202994c00d0981d834ff1eaeb1ae4d2e9f295672b30e4a51bf6be2c66  aws_box03_forward/worker.metadata
93dd031f5d523085d166d7382490f05652261af1ccd281a51aeb88994baeb425  aws_r6d_reverse/h_transport.json
7482e535d71f8f5244e57c42cc9c18917ae63bc1bf3699101f651f0f34f78abb  aws_r6d_reverse/compiler.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_reverse/compiler.stderr
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  aws_r6d_reverse/compiler.rc
74cf47f07f9fd96c041fdaaf3134e4a74c9f4eb6b734ee08732f773eb5e6a773  aws_r6d_reverse/compiler.time
4795f4f1f7f24e345cbc3fb5a799711ae3372406410321e5acc3bb2f41769fd1  aws_r6d_reverse/result.sha256
25b9201b64d9002b7791646259b69a09019c4dc230e07455fc9610753aa06a7e  aws_r6d_reverse/source.check
f57c281541d16956a15f0dbbefce5de99de8ba918018a0e05a73e186d8a7f365  aws_r6d_reverse/worker.metadata
```

Source-closure entries, all matched from the package root:

```text
a4a254891a2e60378c6ae8cc068740376a6768c0f31bba8576f2636b51163188  PREREGISTRATION.md
6102c79f353a640eba0a571309886c89f16633bd445b8862cfeed631b896a17f  AWS_REGISTRATION.md
3bbf1ebfb9f8b15054fe2f592bea92d8e07b95bce4d6ca131cd81c95f3698306  compile_h_first_transport_v4.py
7b192697f862386daa328c088b4c827b2a9baa069e55cd86a732c4fcf70d9425  remote_worker.sh
c76ef85ac14f81839674368c55a324499832e6cf4b589befa68baf93a42b1490  ../max12_912_order3_d1_double_root_toric_blowup_20260825/compile_toric_blowup.py
0385b0b1e60b3bd37fa5fbee90dd6c17a454722bdbff424ea83c2ab0fa19df45  ../max12_912_order3_d1_double_root_control2_q2_first_lift_v1_20260826/compile_q2_first_lift.py
67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623  ../max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/independent_reconstruct.py
```

Harvested `SOURCE_CLOSURE.sha256` is byte-identical to the top copy on both hosts. Both `source.check` files are identical (`25b9201b…`) and print `OK` on those seven paths. The worker `cd`s to `$run` before `sha256sum -c SOURCE_CLOSURE.sha256`; `AWS_LAUNCH_METADATA.md` states that each run directory is the package under the job root's `cases/`. The sibling `../max12_…` paths are therefore `cases/`-neighbours, which is how AWS ran and how this review rechecked. Treating `aws_box03_forward/` or `aws_r6d_reverse/` as a new source root would make those siblings invisible. That is not the charged root.

The compiler pins the same two hashes as source closure (`TORIC_SHA=c76ef85a…`, `V1_SHA=0385b0b1…`) and refuses a non-matching file before import. `t.load_charged_source()` re-pins `independent_reconstruct.py` at `67343b56…`. Tag gates: worker `case` requires prefix `max12_912_order3_d1_double_root_control2_h_first_transport_v4_20260826T*`; compiler `require_aws` requires Linux, DMI vendor `Amazon EC2`, and tag prefix `max12_912_order3_d1_double_root_control2_h_first_transport_v4_`. Both refuse non-`forward`/`reverse` orders.

| Check | Box03 forward | r6d reverse |
|---|---|---|
| Public IP / harvested hostname | `98.80.65.144` / `ip-172-30-0-249` | `100.26.198.153` / `ip-172-30-0-45` |
| Tag | `…_v4_20260826T034500Z_box03_forward` | `…_v4_20260826T034500Z_r6d_reverse` |
| Worker PID | `153321` | `221060` |
| Caps | `memory_kib=4194304`, `timeout=900`, `nice -n 10`; `ulimit -v 4194304` | same |
| Order | `forward` (`ell=1..8`) | `reverse` (`ell=8..1`) |
| Started / finished UTC | `2026-08-26T03:46:44Z` / `03:47:22Z` | same timestamps |
| Compiler stdout SHA | `1bdd9e87…` | `7482e535…` |
| Certificate SHA | `93dd031f…` | `93dd031f…` (byte-identical file) |
| RSS / swap / exit | 22476 KiB / `Swaps: 0` / 0 | 22444 KiB / `Swaps: 0` / 0 |
| Pre/post `free` swap | `0B` / `0B` | `0B` / `0B` |
| Elapsed | 5.86 s | 5.87 s |
| PASS markers, each once | `PASS_H_FIRST_TRANSPORT_V4`, `PASS_REMOTE_WORKER` | same |
| `FAIL_` / `REFUSED` / `FAILED` | none; stderr empty | none; stderr empty |

`AWS_LAUNCH_METADATA.md` is timestamped `2026-08-26T03:46:56Z`, after worker start (`03:46:44Z`) and before GO. Content: both workers `WAITING_GO`; “Neither had a GO sentinel when PID/caps were read”; source-closure manifest SHA `817f45eb…` matching the frozen file. GO sentinels exist and are empty; local mtimes place GO after that registration (`~03:47:15Z` PDT offset) and DONE at finish (`03:47:22Z`). No `REFUSED` or `FAILED`. The 7-second GO-to-DONE window matches the 5.86 s compile plus the post-GO source-hash check.

Harvest copies of compiler, worker, preregistration, AWS registration, and source closure are byte-identical to the package top on both hosts (`cmp`). The two `h_transport.json` files are byte-identical to each other (`cmp`; 108001 bytes) despite opposite traversal orders. Compiler stdout differs only in the preregistered `ORDER=` line (forward vs reverse) together with the identical metric block

```text
W0_SHA256=ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b
WH_TERM_COUNT=98
H_CORRECTION_TERM_COUNT=61
H_CORRECTION_SHA256=3ef3c9c2e950f2e8508f86d2b474608ed4a277eea5b210cf67569661b3f7d58f
ETA_THRESHOLD=15/2
BAD_SMALL_ETA_TERMS=50
THRESHOLD_FACE_TERMS=28
CERTIFICATE_SHA256=93dd031f5d523085d166d7382490f05652261af1ccd281a51aeb88994baeb425
PASS_H_FIRST_TRANSPORT_V4
```

Canonical hashes, recomputed from the already-emitted records and matched to both JSON payloads, both stdout streams, and `RESULT.md`:

```text
W' SHA-256                 ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b
(W_h-W')/h SHA-256         3ef3c9c2e950f2e8508f86d2b474608ed4a277eea5b210cf67569661b3f7d58f
certificate SHA-256        93dd031f5d523085d166d7382490f05652261af1ccd281a51aeb88994baeb425
```

Records are sorted by `json.dumps(exponents, sort_keys=True)`. Every extra toric variable `p,c,a,x,y,k,mu,nu` is zero on all 98 terms. Support is exactly `{h,la,tau,q2,q1,q0,r2,r1,r0}`.

---

## Charge 2 — Source construction, `h=0` specialization, 98/61, correction SHA

**CONFIRMED. Images are `p=-3`, `c=2+h`, full `Q` and `R`, empty `kbar`. Multipliers are the V1 list with `F1+=q2/12`, `F2+=-q2/9`. The `h=0` slice is the literal reviewed 37-term `W'`. Correction has 61 terms and SHA `3ef3c9c2…`.**

Construction, from the hash-pinned V4 compiler, which loads the hash-pinned toric ring and the hash-pinned V1 compiler:

1. `t.load_charged_source().build()["tails"]` is the eight negative Laurent tails of `independent_reconstruct.py` at `67343b56…`, in names `(a0..a7,k)`. This is the same charged ordinary-tail source as the reviewed q2 lift. It does not import a factored renderer.
2. `coefficient_images(t)` specialises the nine jet slots with no `x` (affine `x=1`) and no `a`:

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

Hand expansion at `h=0` recovers V1 `coefficient_images()` termwise: `(8+2 q0+r0, -36-3 q0+2 q1+r1, 54-3 q1+2 q2+r2, -15+q0-3 q2, -36+q1, 27+q2, 6, -9, {})`.
3. Substitute tails through `t.source_power_table` / `t.substitute`. Subtract the two rational targets, specialised at the fixed loads: row 3 minus `(2/3) la^15` (`mu=2/3`); row 8 minus `la^20(1+tau)`; no row-6 `nu` subtraction (`nu=0`). No `a` appears in the images, so the axis is the unit chart `a=1`.
4. Multipliers from V1 `multipliers()`, then the reviewed correction:

```text
F1 = (1/108) q1^2 - (7/72) r2 + (1/8) r1 - (5/18) q1 + (1/8) q0 + 115/24,
F2 = (1/12) q1 - (5/36) q0 - 29/9,
F3 = 0,
F4 = (-1/24) q1 + 3/2,
F5 = (-1/24) q0 - 25/24,
F6 = (1/24) q1,
F7 = 3/8,
F8 = -1,
F1' = F1 + q2/12,  F2' = F2 - q2/9,  Fi' = Fi (i>=3).
```

`W_h = sum_ell F_ell' E_ell(h)` with `ell` traversed `1..8` or `8..1`. Fail-closed: `W_h|h=0` projected onto the V1 ring must have 37 terms and digest `ddb451c4…`; `W_h-W'` must be `h`-divisible and nonzero.

The `h=0` slice of the frozen certificate is a 37-term dictionary, coefficient-and-monomial equal to the reviewed V2 compiled `EXPECT` body (text-split; empty symmetric difference; empty coefficient mismatch). Recomputed V1 digest of that slice is `ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b`. Counts: 98 terms in `W_h`, of which 37 have `h=0` and 61 have `h>=1` (max `h`-exponent 3). Decrementing the 61 `h`-positive monomials by one `h` and hashing in the toric canonical format `[[list(monomial), num, den], ...]` yields `3ef3c9c2e950f2e8508f86d2b474608ed4a277eea5b210cf67569661b3f7d58f`.

This package does not pin `base_B.sing` and does not emit row-by-row `q2=0` identities. The `h=0` control is the reviewed polynomial `W'` itself, which is the correct control for an unchanged-witness transport. Dual AWS agreement plus the digest check is the custody that the eight-row product was formed; this review does not replay that product.

---

## Charge 3 — All 98 weight forms; the iff at `eta=15/2`

**CONFIRMED. The recorded difference of every non-target monomial from target weight `20L` is exactly `c + U u + V v + E eta`. There is no `rho` term. The only `tau` term is the skipped `la^20 tau`. Integer arithmetic on all 98 records proves: unique least term `la^20` for every `u,v>0`, `T>0` if and only if `eta>=15/2`.**

Weight convention, matching the reviewed q2 sample `(L,T,H; D; beta L; alpha L)=(4,1,1; 23; 22; 30)` after restoring the two missing directions as `beta=5+u`, `delta=5+v` and introducing `eta=wt(h)/L`, with `alpha` held at `15/2`:

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

and skips only the two monomials `la^20` (the target) and `la^20 tau` (strictly above once `T>0`). Both skips are present with coefficient `1`. No record has `rho>0`. Every other record has `tau=0`. Therefore on the 96 charged terms the recorded form is exact, not a lower bound, and `T` enters the uniqueness statement only through the skipped `la^20 tau`.

Integer check, all 98 difference-forms against exponents: 98/98 match (`eta=h`, `delta=q2`, `beta=q1+q0`, `alpha=r2+r1+r0`, `constant=la-20`, `t=tau`, `H_over_L=rho`). Integer check, all 96 recorded constants: the reduced fraction of `2(la-20)+10(q0+q1+q2)+15(r0+r1+r2)` over `2` equals the stored string, and `(U,V,E)=(q0+q1, q2, h)`, 96/96.

Closed-corner value at `eta=15/2` is the integer `2c + 15 E` over 2. Histogram of the 96 charged terms by recorded `c`:

```text
c      count   of which E=0   E>0
-15/2     17        0         17
-5        19        0         19
-5/2      14        0         14
 0        30       20         10
 5/2      11       10          1
 5         5        5          0
```

`17+19+14+30+11+5=96`. Among `h=0` charged terms, 20 have `c=0` and 15 have `c>0` (`10` at `5/2`, `5` at `5`); zero have `c<0`. Among `h>0` terms, 50 have `c<0` and 11 have `c>=0` (`10` at `c=0` plus the one `c=5/2` correction term). `20+15=35` old charged plus 2 skipped plus 61 correction equals 98.

For a term with `U,V,E >= 0`, uniqueness of least term `la^20` for all `u,v>0` at fixed `eta` holds iff every charged term satisfies either `c+E eta > 0`, or `c+E eta = 0` and `U+V > 0`. (If `c+E eta = 0` and `U=V=0`, the term ties `la^20` throughout the quadrant. If `c+E eta < 0`, sufficiently small positive `u,v` put it below target.) Increasing `u` or `v` cannot create a new below-target term, because `U,V >= 0`.

Verified on the 96 charged records:

- `h=0` and `c<0`: **0**. The old `W'` does not itself break the open quadrant at this `alpha`.
- `h=0` and `c=0`: **20**, and every one has `U+V > 0` (in fact `U+V in {1,2,3,4}`). These are the 20 old closed-corner threshold monomials.
- `h=0` and `c>0`: **15**, strictly above even at the closed corner, for every `eta`.
- `E>0` and `c<0`: **50**. The exact ratio `-c/E` is at most `15/2`, with equality on **exactly 8** terms (all of them `E=1`, `c=-15/2`). No term has `-c/E > 15/2`.
- At `eta=15/2`: **0** terms with `c+(15/2)E < 0`; **28** with equality (20 old + 8 new); **0** of those 28 have `U=V=0`.

Hence:

- If `eta > 15/2`, every charged term has `c+E eta > 0` or (the 20 old `c=0` terms) `c+E eta = 0` with `U+V>0`. Unique least term `la^20` throughout the open quadrant.
- If `eta = 15/2`, the same, with the eight new terms now on the threshold face; each has margin `U u + V v` with `U+V=1`, so equality at `u=v=0` is strict for `u,v>0`.
- If `0 < eta < 15/2`, each of those eight terms has `c+E eta < 0`. They are present (nonzero coefficients). None carries `tau` or `rho`. Choosing the relevant `u` or `v` in `(0, 15/2-eta)` puts that term strictly below target.

The two skipped monomials: `la^20` is the target; `la^20 tau` has extra weight `T>0`. No other `la`-positive term exists.

This is the exact iff, charged on all 98 terms, not on a displayed subset.

The 20 old threshold monomials (`c=0`, `E=0`; all `h=0` pieces of reviewed `W'` that tie at the closed corner):

```text
q2 r2^2, q2 r1 r2, q2 r1^2, q2 r0 r2, q2 r0 r1, q2^4,
q1 r1 r2, q1 r1^2, q1 r0 r2, q1 r0^2, q1 q2^3, q1^2 q2^2, q1^3 q2,
q0 r0 r1, q0 q2^3, q0 q1 q2^2, q0 q1^2 q2, q0^2 q2^2, q0^2 q1 q2, q0^3 q1.
```

The 15 old strictly-above monomials (`h=0`, `c>0`):

```text
c=5/2: q2^3 r2, q2^3 r1, q1 q2^2 r2, q1 q2^2 r1, q1^2 q2 r2, q1^2 q2 r0,
       q0 q2^2 r2, q0 q2^2 r0, q0 q1 q2 r1, q0^2 q2 r2;
c=5:   q2^5, q1 q2 r2^2, q1 q2^4, q1^3 q2^2, q0 q1 q2^3.
```

Together with `la^20` and `la^20 tau` these are the 37 terms of `W'`.

---

## Charge 4 — Eight `h`-linear extremals, margins, converse, 50 and 28

**CONFIRMED. The eight displayed terms are present with the displayed coefficients. At `eta=15/2` their margins are `v` or `u`. They are the unique maximizers of `-c/E`. The converse holds for every `0<eta<15/2`. Counts 50 and 28 match the certificate and the independent classification of all 61 correction terms.**

Displayed extremals, read from the certificate, coefficients and monomials equal to `RESULT.md`:

```text
-88/27 h q2 r2     c=-15/2  U=0  V=1  E=1    Δ/L = eta - 15/2 + v
 +11/9 h q2 r1     c=-15/2  U=0  V=1  E=1    Δ/L = eta - 15/2 + v
-22/27 h q2 r0     c=-15/2  U=0  V=1  E=1    Δ/L = eta - 15/2 + v
 +11/9 h q1 r2     c=-15/2  U=1  V=0  E=1    Δ/L = eta - 15/2 + u
-22/27 h q1 r1     c=-15/2  U=1  V=0  E=1    Δ/L = eta - 15/2 + u
+11/27 h q1 r0     c=-15/2  U=1  V=0  E=1    Δ/L = eta - 15/2 + u
-22/27 h q0 r2     c=-15/2  U=1  V=0  E=1    Δ/L = eta - 15/2 + u
+11/27 h q0 r1     c=-15/2  U=1  V=0  E=1    Δ/L = eta - 15/2 + u
```

There is no `h q0 r0` term. At `eta=15/2` the first three have margin `v` and the other five have margin `u`. On the closed corner `u=v=0` they tie the target; throughout the open quadrant the inequality is strict.

These eight are the unique terms with `-c/E = 15/2`. The other nine terms with `c=-15/2` have `E=2` (eight of them) or `E=3` (the single `-(4/81) h^3 q2 r2`), hence ratios `15/4` and `5/2`, and at `eta=15/2` sit strictly above by `15/2` and `15` respectively.

Converse: fix `0<eta<15/2`. The term `-(88/27) h q2 r2` is present. It has no `tau` and no `rho`. Choose `0 < v < 15/2-eta` and any `u>0`, `T>0`. Then `Δ/L = eta-15/2+v < 0`, so this term lies below target. The same works with any of the eight, using `u` in place of `v` on the last five. No smaller positive eta therefore gives a uniform open-quadrant conclusion from this unchanged witness.

Counts, independently classified from the 98 records and matched to JSON / stdout / `RESULT.md`:

- 50 terms with `E>0` and `c<0` = `terms_bad_for_some_positive_eta` (the potentially bad correction terms: below target at the closed corner for some positive eta).
- 11 correction terms with `c>=0` (never below at the closed corner). `50+11=61`.
- 28 closed-corner threshold monomials at `eta=15/2`: 20 old (`E=0,c=0`) and 8 new (`E=1,c=-15/2`). JSON `threshold_face_monomials` is this set, including the eight new `h q2 r2, h q2 r1, h q2 r0, h q1 r2, h q1 r1, h q1 r0, h q0 r2, h q0 r1`.

---

## Charge 5 — Ordinary homogeneity checksum; unit-axis covariance not a theorem

**CONFIRMED as a checksum. Not promoted.**

The compiler, before substitution, requires that every ordinary source monomial of `tails[ell]` have weight `{12+ell}` under `wt(a_i)=9-i` (`i=0..7`) and `wt(kbar)=6`. JSON reports `ordinary_homogeneity = {1:13,...,8:20}`, which is `12+ell`. Dual AWS both passed this check (else `TransportFailure` and nonzero rc). The charged source is the same `independent_reconstruct.py` at `67343b56…` whose tails are 9-tuples in `(a0..a7,k)`: `build()` scales `[w^{-ell}] g(z(w))` by `-1` for `ell=1..8`. This review did not re-run `build()`. The check is the ordinary D1 row-homogeneity of that source, independent of the `h` substitution.

The displayed unit-axis map

```text
f(z) -> a^{-9} f(a z),  Lambda -> a^{-1} Lambda,  rho -> a^{-1} rho,
q2,q1,q0 -> a^{-4} q2, a^{-5} q1, a^{-6} q0,
r2,r1,r0 -> a^{-7} r2, a^{-8} r1, a^{-9} r0,
tau, k, mu, nu unchanged
```

is consistent with the `K^3 + K Q + R` scaling on the unit-leading degree-9 chart: `Q_new(z)=a^{-6} Q(a z)` and `R_new(z)=a^{-9} R(a z)` produce exactly those `q` and `r` weights, and `K_new(z)=a^{-3} K(a z)` produces the `K^3` factor `a^{-9}`. That is a covariance checksum of coefficient weights, written into the certificate as `axis_unit_normalization`. It is **not** a proof that the eight substituted rows, the two targets, and the loads transform as a moving-axis family. `RESULT.md` does not promote it; this review does not either. A moving-axis theorem still requires independently proved target and load transformations.

---

## Charge 6 — Scope: negative control, not a surviving branch

**CONFIRMED. The licensed theorem is the Promotion paragraph. The sub-threshold token is a negative result about this witness.**

Admissible:

- For `eta>=15/2`, this explicit unchanged corrected combination `W_h` has unique least term `la^20` uniformly on `u>0`, `v>0`, `T>0`, at the fixed axis/cusp chart `a=1`, `p=-3`, `c=2+h`, loads `k=nu=0`, `mu=2/3`, and full `Q,R` support.
- For `0<eta<15/2`, the same polynomial does **not** transport uniformly. The token `OLD_CORRECTED_WITNESS_DOES_NOT_TRANSPORT_UNIFORMLY` is the correct label of that fact. It is evidence that the old multipliers plus the q2 correction, used unchanged, leave below-target correction terms on the low-eta cells. Those cells require a new graded syzygy correction if they are to be charged.
- Ordinary homogeneity of the charged tails, as a checksum supporting a later moving-axis reduction, not as that reduction.

Not admissible, and not claimed by the frozen firewall strings
`unchanged corrected multipliers only; low terms trigger syzygy lift` and
`RESULT.md` §Firewall:

- a surviving arc, branch, or low-eta existence statement;
- a newly corrected `h`-witness (new `F_i(h)`);
- moving axis, moving loads, or a theorem that the unit-axis map acts on the submitted rows;
- equality-support faces (the 28 threshold monomials are listed; their initial-form equalities are not solved);
- another normal direction (`p` is fixed at `-3`);
- a formal-arc / formal-lift obstruction;
- the whole double-root fan, D1, or JC2;
- a claim that the reviewed q2 lift already settled the cusp direction (it did not; that is this package).

The reviewed q2 lift remains valid on the special fibre `h=0`. This package classifies only the weight behaviour of one explicit corrected witness after restoring one cusp coordinate.

---

## Nits, not defects

1. Harvest trees contain sentinels, `free.*`, `hostname`, `uname`, `nproc`, UTC stamps, and empty launch stdio, none of which are in `FREEZE.sha256`. They were used as custody, not as a second freeze. Harvest copies of source files that *are* frozen at the package top were `cmp`-identical.
2. Preregistration uses the shorter token `OLD_CORRECTED_WITNESS_DOES_NOT_TRANSPORT` without `UNIFORMLY` and without the interval. `RESULT.md` is the precise statement, and is the one licensed above.
3. The recorded form omits `(T/L) tau` and `(H/L) rho`. On this certificate that is exact: no `rho` support, and the only `tau` monomial is skipped. A later package that emits `tau`- or `rho`-positive correction terms would have to carry those summands or fail closed.
4. `AWS_LAUNCH_METADATA.md` records a local heavy-process audit of zero campaign-owned workers. r6d `free` shows 115 GiB used vs box03 10 GiB; swap is zero on both, and this job’s RSS is 22 MiB under a 4 GiB `ulimit -v`. That is not evidence that another campaign job was stopped, and not a defect in this package.
5. The compiler’s `eta0 = max(-c/E)` loop does not, by itself, inspect `U,V` on the threshold face. The certificate stores the 28 face monomials, all of which have `U+V>0`; this review charged that. The open-quadrant strictness is in the records, not only in the `max` reduction.

No source or certificate repair is required.

H_FIRST_TRANSPORT_CONFIRMED
