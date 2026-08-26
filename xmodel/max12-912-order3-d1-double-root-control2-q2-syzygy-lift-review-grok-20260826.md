# Hostile text-only review — control-2 first `q2` syzygy lift V2

| Field | Value |
|---|---|
| Claim under review | Exact first omitted-support witness: a corrected eight-row combination `W'` in the full-`q2` ordinary-tail row ideal, at one charged weight, whose unique least-weight term is `la^20` |
| Overall verdict | **Q2_SYZYGY_LIFT_CONFIRMED**. Dual AWS encodings check the literal polynomial identity `W'=sum_i F_i' E_i(full q2)=W+q2·CORR`. Hand algebra gives `C_52=(1/9)in_52(E2)-(1/12)in_52(E1)=(2/81)GH3-(1/27)GH5+(2/27)GH6` and the free-zero solution `(g1,...,g8)=(1/12,-1/9,0,...,0)`. All 37 terms of `W'` were weight-charged; the unique least term is `la^20` at weight 80. V1 remains only the negative control that the *old* multipliers do not transport |
| Smallest failing identity | none in the frozen V2 source, either compiled encoding, or either AWS stream |
| Smallest missing hypothesis for a stronger theorem | a full Gröbner cone (the 37-term halfspace list is not computed here); all `q2` valuations; moving axis/cusp or moving loads; another support mask; a formal-arc obstruction; the whole double-root fan; D1; or JC2 |
| Evidence tier | SHA-256 of the freeze chain and already-emitted AWS files; `cmp` of harvest copies and of tag/ring-stripped polynomial bodies; unique-anchor extraction of `BASE1..BASE8` against pinned B; term-splitting of already-emitted compiler polynomials; integer weight arithmetic; hand RREF of the six-by-eight weight-52 matrix. No local Singular, Sage, msolve, gfan, Lean, Python algebra, compiler execution, or eight-row product replay |
| Reviewer / model | Grok 4.6 (xAI). Text-only tropical / commutative-algebra / CAS-custody referee |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `574e873d4753b57dbaeb0fb83e320fbef3694724` |
| Host | Darwin. V2 compiler, V1 compiler, charged reconstruct, Singular, and every solver were not run |

## What was and was not run

No local substantive computation was run. In particular this review did **not** execute the V2 or V1 compilers, `independent_reconstruct.py`, Singular, Sage, msolve, Lean, Gfan, or any other solver, and it did not re-multiply `sum F_i' E_i`. Hashes were checked with `shasum -a 256`. File identity was checked with `cmp`. Marker counts used `grep -c`. Git identity was read with `git rev-parse`. AWS streams were read as already-emitted text. Polynomial bodies were split into already-printed terms; exponents were charged by the integer formula `4 la + tau + rho + 23 q2 + 22(q1+q0) + 30(r2+r1+r0)`. Canonical SHA-256 values were recomputed from the V1 `canonical` JSON of those term dictionaries. Hand arithmetic for `C_52`, the GH identity, signs, and the free-zero RREF is recorded under charges 3–5.

Charged freeze SHA-256, recomputed and matched:

```text
994ef6231c4ec705c8b14bda418f046ce0ce45603e6b597141eac6d1884e4c34  FREEZE.sha256
5c81cd8bfaf80d34ad9211fafdc50ab58a4582c68988f5de4c6bdeb593a66213  RESULT.md
f6938514c9d050e45f46a3a37b331d1ef8904d32939acdfc902e21757e81b2d5  SOURCE_CLOSURE.sha256
```

Every path listed in `FREEZE.sha256` recomputed and matched (35/35). Nested `SOURCE_CLOSURE.sha256` (7/7) and both harvested `result.sha256` manifests (9/9 each) matched from the case root / harvest directory as appropriate. Empty compiler/CAS stderr and the hardened stdout-diagnostic files are the empty-string digest `e3b0c442…`. All four rc files are the two-byte string `"0\n"`, digest `9a271f2a…`.

Read in full before the verdict: every file at
`cases/max12_912_order3_d1_double_root_control2_q2_syzygy_lift_v2_20260826/`
including both harvest trees; V1 `compile_q2_first_lift.py` and `RESULT.md`; pinned `base_B.sing`; charged `independent_reconstruct.py` far enough to see that `build()` returns the eight negative Laurent tails; V1 first-lift compiled sources and Box03 correction print; `WITNESS_RESULT.md` of the LPDP `la^20` preimage package; and
`xmodel/max12-912-order3-d1-double-root-control2-la20-witness-review-grok-20260826.md`.
Predecessor conclusions were recomputed, not inherited.

---

## Promotion

**Accept `FOR THE PINNED ORDINARY-TAIL EIGHT-ROW MODULE AT a=1, FIXED AXIS/CUSP, k=nu=0, mu=2/3, AND FULL SUPPORT Q=q2 z^2+q1 z+q0, THE REGISTERED DUAL-AWS V2 RUNS PROVE THE LITERAL POLYNOMIAL IDENTITY W' = F1' E1 + … + F8' E8 = W + q2·CORR IN Q[la,tau,rho,q2,q1,q0,r2,r1,r0], WITH F1'=F1+q2/12, F2'=F2-q2/9, AND F3'=…=F8'=F_i UNCHANGED. THIS IS AN EXACT IDENTITY, NOT A CONGRUENCE MODULO q2^2. AT THE SINGLE CHARGED WEIGHT (L,T,H;D;beta L;alpha L)=(4,1,1;23;22;30) THE UNIQUE LEAST-WEIGHT TERM OF THE 37-TERM POLYNOMIAL W' IS la^20, OF WEIGHT 80. THEREFORE la^20 LIES IN in_w(J) FOR THE EXACT SUBMITTED ROW IDEAL J=(E1,...,E8), THERE IS NO REMAINING BELOW-TARGET LAYER AT THIS WEIGHT, AND THE NINE-COORDINATE TORUS LOCALIZATION OF THAT INITIAL IDEAL IS EMPTY. THE V1 PACKAGE REMAINS ONLY THE NEGATIVE CONTROL THAT THE OLD MULTIPLIERS DO NOT TRANSPORT; IT IS NOT A NO-LIFT THEOREM.`**

Do not promote this to: a complete Gröbner cone; an all-`q2`-valuation statement; a moving axis, cusp, or load theorem; another support mask; a formal-arc obstruction; a whole double-root fan; D1; or JC2. Do not cite the compiler JSON string `iterate if minimum <= 80` as a demand to iterate the target layer: the unique least term *is* the target.

---

## Charge 1 — Custody, freeze, dual AWS, source closure

**CONFIRMED. Every freeze entry recomputes. Both registered workers are fail-closed, hash-gated, empty-stderr, sub-cap, and source-closed against the package-root manifest, not against the harvested subdirectory as a new root.**

Recomputed `FREEZE.sha256` entries, all matched:

```text
5c81cd8bfaf80d34ad9211fafdc50ab58a4582c68988f5de4c6bdeb593a66213  RESULT.md
93a4a2de52e40fd3abecd923850c7aa74c910f2847f3a025b1726be21c81cb9a  PREREGISTRATION.md
89421f3473e3f51b01643afc69be735cc077ff4c260306b6fb333cec822961d6  AWS_REGISTRATION.md
82592672a5603bd19b4aaf91055627044fc54983f12455182647a2c4ec9927f8  AWS_LAUNCH_METADATA.md
f6938514c9d050e45f46a3a37b331d1ef8904d32939acdfc902e21757e81b2d5  SOURCE_CLOSURE.sha256
5c8e74ffa2acee40ab8ab0c2e68c44ddcbc2927722994c0d7488eb6c389f4611  compile_q2_syzygy_lift_v2.py
26339b55b76f169a18a4dde57124dfefbbbd5e9b84f261eca4fbe6cfacd4dfe9  remote_worker.sh
a0a69d7fafd3329e3b06de67995389e70b003df0d98d56e6f8a3e2704709ff6d  aws_box03_A/compiler.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_box03_A/compiler.stderr
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  aws_box03_A/compiler.rc
cafa685fc2219b81180eee892487dd56d5597eaca6dd40dc499bfe46b7b2831e  aws_box03_A/compiled/q2_syzygy_lift_v2_A_dp.sing
11a85cbd99fbb0a0e3df74063142a211fd535e9adb35acbd685d3b1616a5f7c2  aws_box03_A/singular.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_box03_A/singular.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_box03_A/singular.stdout.diagnostics
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  aws_box03_A/singular.rc
6f32076030ef1dc04651c5374147c9e84b90fb7588c9ac469d65204392b68e9c  aws_box03_A/singular.time
7ab1d8ffc7ce4f68b8207306b13202cc746875ceb4dbd911824cf76e4aa7728f  aws_box03_A/result.sha256
0f4193f6de1e1a8472ee279b746c85faa720dc816910319a64d4c46ccbf9ed60  aws_box03_A/source.check
69702f2974a899724215e9826ad3f0368dc2c761a83236ce8405aa153a076b6e  aws_box03_A/solve_source.sha256
44e6bdf8a17dfe6552112fac3bc2b2ac09a1e42083ed5cd5c77f2ac834295a17  aws_box03_A/solve_source.check
be3da5efc9d64d842346adc782949fb93b8a0ca72a675bd1eed7f312fe2756b1  aws_box03_A/worker.metadata
d55e6decdc90cab95e7e68950b662505fb90a7d074778a4d44b6b24969f3368b  aws_r6d_B/compiler.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_B/compiler.stderr
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  aws_r6d_B/compiler.rc
12bc04b6f876974a95d539fc75063800c2de13bd4cf99791f9f1d11455354c2a  aws_r6d_B/compiled/q2_syzygy_lift_v2_B_lpdp.sing
ca117052f0a11b03517692c376b130fafef20a02c6bd5260e4a325b1882505d4  aws_r6d_B/singular.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_B/singular.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_B/singular.stdout.diagnostics
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  aws_r6d_B/singular.rc
0e7222dd654847abbf15e8b19e5e405ac057a9178367fcb65ed292009b35017b  aws_r6d_B/singular.time
1422228ebb96fc34f04227e5e58784e07d2d5d946130afc86d5e4ee47799ad1a  aws_r6d_B/result.sha256
0f4193f6de1e1a8472ee279b746c85faa720dc816910319a64d4c46ccbf9ed60  aws_r6d_B/source.check
07c653239029a71dbeaed729d95eed607bd5b3348e807f02448ef30bc9c90ebf  aws_r6d_B/solve_source.sha256
2447c31ba2fa6160625ad5d955547433643fe6bbdacc9ecb5b567d4faac7f366  aws_r6d_B/solve_source.check
71ba1d56a2c2335303a280cfad1432d8315191ad6627a643c60d23e6ea9f1d96  aws_r6d_B/worker.metadata
```

Source-closure entries, all matched from the package root:

```text
0385b0b1e60b3bd37fa5fbee90dd6c17a454722bdbff424ea83c2ab0fa19df45  ../max12_912_order3_d1_double_root_control2_q2_first_lift_v1_20260826/compile_q2_first_lift.py
67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623  ../max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/independent_reconstruct.py
c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b  ../max12_912_order3_d1_double_root_control2_la20_syzygy_20260826/base_B.sing
```

plus the four package-top files already listed. Harvested `SOURCE_CLOSURE.sha256` is byte-identical to the top copy on both hosts. Both `source.check` files are identical (`0f4193f6…`) and print `OK` on those seven paths. The worker `cd`s to the package root before `sha256sum -c SOURCE_CLOSURE.sha256`; the sibling `../max12_…` paths are therefore `cases/`-neighbours, which is how AWS ran and how this review rechecked. Treating `aws_box03_A/` or `aws_r6d_B/` as a new source root would make those siblings invisible. That is not the charged root.

| Check | Box03 A / global `dp` | r6d B / `(lp(2),dp(8))` |
|---|---|---|
| Public IP / harvested hostname | `98.80.65.144` / `ip-172-30-0-249` | `100.26.198.153` / `ip-172-30-0-45` |
| Tag | `…_v2_20260826T032200Z_box03_A` | `…_v2_20260826T032200Z_r6d_B` |
| Worker PID | `150218` | `217964` |
| Caps | compiler 4 GiB / 900 s; solver 8 GiB / 1800 s; `nice -n 10` | same |
| Started / solve UTC | `03:27:16Z` / `03:28:52Z`–`03:28:52Z` | same timestamps |
| Selected input SHA | `cafa685f…` | `12bc04b6…` |
| Compiler stdout SHA | `a0a69d7f…` | `d55e6decdc…` |
| Singular stdout SHA | `11a85cbd…` | `ca117052…` |
| RSS / swap / exit | 10340 KiB / `Swaps: 0` / 0 | 10264 KiB / `Swaps: 0` / 0 |
| Pre/post `free` swap | `0B` / `0B` | `0B` / `0B` |
| Singular | 4.3.2 (`4330`) | 4.3.2 (`4330`) |
| PASS markers, each once | `PASS_Q2_SYZYGY_LIFT_V2_COMPILER`, `PASS_ALL_EIGHT_BASE_ROWS`, `PASS_FIRST_ORDER_GRADED_CANCELLATION`, `PASS_Q2_SYZYGY_LIFT_V2_A_DP`, `PASS_REMOTE_WORKER` | same with `…_B_LPDP` |
| `FAIL_` / diagnostics | none; three empty files | none; three empty files |

`AWS_LAUNCH_METADATA.md` is timestamped `2026-08-26T03:27:42Z`, after worker start and before either solve, with state `WAITING_COMPILE` and no GO sentinel then present. The documented accidental local `$! → 0` is not used: PIDs come from `worker.metadata`. GO sentinels exist and are empty; `COMPILE_DONE` / `SOLVE_DONE` exist; no `REFUSED`, `COMPILE_FAILED`, or `SOLVE_FAILED`. Harvest copies of compiler, worker, preregistration, AWS registration, and source closure are byte-identical to the package top. Solve-source pins are exactly the selected encoding’s compiled file, and `solve_source.check` is `OK` on each host.

Tag-dependent compiler stdout and selected-input hashes differ, as preregistered. After deleting the four tag/ring/encoding/PASS lines, the two selected `.sing` files are byte-identical (7561 bytes). Every `poly` body, including `EXPECT` and `CORR`, is byte-identical across A, B, and the off-encoding copies compiled on the other host.

Canonical hashes, recomputed from the split `EXPECT` / `CORR` / `C_52` dictionaries and matched to both compiler JSON payloads and to `RESULT.md`:

```text
W' SHA-256                 ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b
(W'-W)/q2 SHA-256          ac7d43b5e71444f5cd487328f7aff6b2312d198649a2c0b001d4a13ef006956c
old first-bad C52 SHA-256  4493daefdd98d9158f556735b8adf50978ec5b8e61295c58fd79e65d1e907b28
```

Both Singular `CORR` prints, despite opposite monomial-order banners, parse to the same 29-term dictionary as compiled `CORR`.

---

## Charge 2 — Eight full-`q2` rows from ordinary tails and pinned B

**CONFIRMED. Rows are substituted ordinary tails with `q2` in the coefficient images. Pinned expanded B is used only as the `q2=0` byte-identity control. The historical factored-A `E8` renderer is not on the source path.**

Construction, from the hash-pinned V1 compiler that V2 imports and whose SHA is both `V1_SHA` and a source-closure entry:

1. Load `independent_reconstruct.py` at `67343b56…`. Its `build()` reconstructs Faber `F6`, `F12`, the inverse root, and the eight *negative Laurent tails* `tails[1..8]`. This is the charged ordinary-tail compiler. It does not import a factored renderer.
2. Substitute those tails by V1 `coefficient_images()`, which are the nine jet images for `(a0,...,a7,k)` and which contain `q2` in three slots (`r2`-image, the fourth image, and the sixth image). Subtract the two rational targets: `(2/3) la^15` on row 3 and `la^20(1+tau)` on row 8.
3. Hash-pin `base_B.sing` at `c905f1b5…` and extract `poly E1..E8` by the unique-anchor regex `^poly E{ell}=(.*);$`. Emit those bodies as `BASE{ell}`. Emit the substituted full-`q2` polynomials as `E{ell}`. Check `subst(E{ell},q2,0)-subst(BASE{ell},s,1)==0` and abort on `FAIL_BASE_ROW_{ell}`.

There is no `base_A`, no `compact_row_string`, and no `factored` token in V2, V1, the worker, or `SOURCE_CLOSURE.sha256`. The invalid factored-A `E8` (identity-control `FAIL_DP_E8`, renderer SHA `2b416cb8…` in the corrected-A review) is therefore not consumed.

Byte identity, not dictionary identity: each compiled `BASE{ell}` body equals the corresponding `poly E{ell}` body of pinned B. Independently, dropping every `q2`-positive term of compiled `E{ell}` recovers `BASE{ell}` at `s=1`, for all eight rows. Both AWS streams print `PASS_ALL_EIGHT_BASE_ROWS` once and no `FAIL_`. Row 8 is the expanded ordinary-tail polynomial whose `q2=0` slice is the reviewed B `E8`, including the target `-la^20 tau - la^20`, not the factored compact form.

---

## Charge 3 — First bad coefficient, two representations, free-zero solution

**CONFIRMED. The two displayed formulae are the same five-term polynomial. The unique free-zero solution of `sum g_i in_52(E_i)=-C_52` is `(1/12,-1/9,0,...,0)`. Signs and 1-based row numbering match `F1'=F1+q2/12`, `F2'=F2-q2/9`.**

Special-fibre initials, read from pinned B (equivalently from `E|q2=0`); only `s^52` terms have affine weight 52:

```text
in_52(E1) = (4/9) q1 r1 + (4/9) q0 r2
in_52(E2) = (4/3) q1 r2 + (4/9) q1 r0 + (4/9) q0 r1
```

(`E2` also has `(2/9) r2^2` of weight 60, excluded from the initial form.)

Row formula:

```text
(1/9) in_52(E2) = (4/27) q1 r2 + (4/81) q1 r0 + (4/81) q0 r1
-(1/12) in_52(E1) = -(1/27) q1 r1 - (1/27) q0 r2
```

so

```text
C_52 = (4/81) q0 r1 - (1/27) q0 r2 + (4/81) q1 r0 - (1/27) q1 r1 + (4/27) q1 r2.
```

GH formula, with the V1 special-fibre generators
`GH3=2 q0 r1 + 2 q1 r0 + 3 q0 r0`, `GH5=q0 r2 + q1 r1`, `GH6=2 q1 r2 - q0 r0`:

```text
(2/81) GH3 = (4/81) q0 r1 + (4/81) q1 r0 + (2/27) q0 r0
-(1/27) GH5 = -(1/27) q0 r2 - (1/27) q1 r1
 (2/27) GH6 = (4/27) q1 r2 - (2/27) q0 r0
```

The `q0 r0` pair cancels, and the remainder is the same five-term polynomial. The V1 negative-control print

```text
(1/81) (4 q0 r1 - 3 q0 r2 + 4 q1 r0 - 3 q1 r1 + 12 q1 r2)
```

is the same element (`-3/81=-1/27`, `12/81=4/27`). Those five terms occur in the V1 Box03 `CORR` print and are absent from V2 `CORR|q2=0`. Canonical digest of this `C_52` is `4493daef…`.

Signs. The linear problem is `sum g_i in_52(E_i) = -C_52`. Substituting the row formula:

```text
-C_52 = (1/12) in_52(E1) - (1/9) in_52(E2).
```

Hence `g1=1/12`, `g2=-1/9` solves it on the first two columns. Compiler `initial52[0]` is `E1`, `initial52[1]` is `E2`; `enumerate(..., start=1)` prints `g1=(1/12)`, `g2=(-1/9)`. Then `F1'=F1+q2 g1=F1+q2/12` and `F2'=F2+q2 g2=F2-q2/9`. Compiled `F1` and `F2` contain exactly those `q2` coefficients on top of the V1 multipliers; `F3,...,F8` are unchanged (`F3=0`, `F4=(-1/24)q1+3/2`, `F5=(-1/24)q0-25/24`, `F6=(1/24)q1`, `F7=3/8`, `F8=-1`).

RREF, charged. The six weight-52 monomials in compiler order are
`q0 r0, q0 r1, q0 r2, q1 r0, q1 r1, q1 r2`. Columns of `in_52(E1..E8)`:

```text
       q0r0  q0r1   q0r2   q1r0   q1r1   q1r2
E1       0     0     4/9     0     4/9     0
E2       0    4/9     0     4/9     0     4/3
E3      4/9    0     8/9     0     8/9   -8/9
E4       0    4/9  -16/27   4/9  -16/27   4/3
E5       0   -8/27   4/9   -8/27   4/9   -8/9
E6       0     0      0      0      0      0
E7       0    8/27 -40/81   8/27 -40/81   8/9
E8       0  -28/81  16/27 -28/81  16/27 -28/27
```

`E3` is the only column with a `q0 r0` component, so rank is at least 3. Direct combinations: `E4=E2-(4/3)E1`, `E5=E1-(2/3)E2`, `E6=0`, `E7=-(10/9)E1+(2/3)E2`, `E8=(4/3)E1-(7/9)E2`. After swapping the `E1`-pivot onto `q0 r2`, scaling, and clearing, the first three pivot columns are 0,1,2 and the reduced right-hand side is `(g1,g2,g3)=(1/12,-1/9,0)`, with free columns 3..7 set to zero. This is the unique free-zero solution. Both AWS JSON payloads report `graded_rank: 3`, the same three zero-based pivots, and the same eight-tuple.

---

## Charge 4 — Exact full polynomial `W'`, not a congruence modulo `q2^2`

**CONFIRMED. `W'` is the untruncated sum `sum F_i' E_i(full q2)`. Both encodings check that identity as a zero polynomial, and `W'-W=q2·CORR` holds as an equality of 29-term dictionaries.**

The compiler never reduces modulo `q2^2`. It forms `corrected_fs[i]=F_i + q2 g_i` and `corrected = sum corrected_fs[i] * rows[i]` by full dictionary multiplication, then requires `specialize_q2_zero(corrected)=W` and exact `q2`-divisibility of `corrected-W`. The emitted Singular source checks, with no truncation,

```text
WQ2 = F1*E1+...+F8*E8
WQ2 - EXPECT == 0
subst(WQ2,q2,0) - W == 0
WQ2 - W - q2*CORR == 0
```

Both AWS streams print `PASS_FIRST_ORDER_GRADED_CANCELLATION` and the encoding PASS, and neither prints `FAIL_EXPECTED_CORRECTED_POLYNOMIAL`, `FAIL_Q2_ZERO_WITNESS`, or `FAIL_CORRECTION_FACTOR`. “First-order” names the *multiplier* correction `F_i |-> F_i + q2 g_i` with constant `g_i`; it does not truncate `W'`. Higher `q2` powers in `W'` are present and checked (the leading compiled term of `CORR` is `(4/2187) q2^4`, so `W'` contains `(4/2187) q2^5`).

Termwise, compiled `EXPECT` has 37 terms, compiled `W` has the eight reviewed special-fibre terms, compiled `CORR` has 29 terms, and `EXPECT - W` equals the exponent shift of `CORR` by one `q2`. The eight `W` terms reappear unchanged in `EXPECT`, which is `subst(W',q2,0)=W`. After cancelling `C_52`, the `q2`-free part of `CORR` has 13 terms of weights `{60,66,74,82}` and empty weight-52 component, as the compiler’s fail-closed check requires.

Canonical hashes of `EXPECT` and `CORR` agree across hosts, encodings, and both ring-dependent Singular prints.

---

## Charge 5 — Every term weight; unique least `la^20`; empty torus

**CONFIRMED. All 37 terms of `W'` were charged at `(L,T,H;D;beta L;alpha L)=(4,1,1;23;22;30)`. The unique least term is `la^20` at weight 80. There is no remaining below-target layer. That monomial is the weighted initial form of an exact element of the submitted row ideal, so it lies in `in_w(J)` and empties the coordinate torus.**

Weight formula used throughout: `w=4 la + tau + rho + 23 q2 + 22(q1+q0) + 30(r2+r1+r0)`. Histogram of the 37 terms of compiled `EXPECT`:

```text
 80: la^20
 81: la^20 tau
 82: q0 r1 r0, q1 r0^2, q1 r1^2, q1 r2 r0, q1 r2 r1
 83: q2 r1 r0, q2 r1^2, q2 r2 r0, q2 r2 r1, q2 r2^2
 88: q1 q0^3
 89: q2 q1 q0^2, q2 q1^2 q0, q2 q1^3
 90: q2^2 q0^2, q2^2 q1 q0, q2^2 q1^2
 91: q2^3 q0, q2^3 q1
 92: q2^4
 97: q2 q0^2 r2, q2 q1 q0 r1, q2 q1^2 r0, q2 q1^2 r2
 98: q2^2 q0 r0, q2^2 q0 r2, q2^2 q1 r1, q2^2 q1 r2
 99: q2^3 r1, q2^3 r2
105: q2 q1 r2^2
112: q2^2 q1^3
113: q2^3 q1 q0
114: q2^4 q1
115: q2^5
```

Counts `1+1+5+5+1+3+3+2+1+4+4+2+1+1+1+1+1=37`. Zero terms of weight `<80`. Unique term of weight 80: `la^20` with coefficient `1`. The five V1 weight-75 terms were `q2·C_52` (`23+52=75`); they are absent.

The eight terms of `W` recover the reviewed LPDP dehomogenized witness and its weights `81,80,88,82,82,82,82,82`. The 29 new terms all carry a positive power of `q2` and therefore weight at least `23+60=83` once `C_52` is gone (linear `CORR` starts at weight 60).

Why this empties the coordinate torus. Let `J=(E1,...,E8)` in `Q[la,tau,rho,q2,q1,q0,r2,r1,r0]` be the exact submitted full-`q2` row ideal. The checked identity `W'=sum F_i' E_i` is membership `W'∈J`. At the charged weight the least-weight homogeneous piece of `W'` is `la^20`, so `in_w(W')=la^20` and therefore `la^20∈in_w(J)`. On the torus where all nine coordinates are units, `la` is a unit, hence `la^20` is a unit, hence the torus localisation of `in_w(J)` is `(1)`. There is no torus-valued point of that initial ideal, and no remaining graded piece of `W'` below the target to iterate at this weight. Other elements of `J` may add further initial generators; they cannot remove `la^20` from `in_w(J)`.

This is a one-polynomial witness obstruction at one weight, not a claim that `in_w(J)` is constant on a cone.

---

## Charge 6 — Licensed theorem and firewall

**CONFIRMED. The strongest theorem is the Promotion paragraph. V1 and V2 answer different questions.**

Admissible:

- V1 negative control, independently re-read: with the old multipliers `F_i`, both V1 AWS encodings check `sum F_i E_i(full q2)=W+q2 C` with five terms of weight 75. The old witness does **not** transport unchanged to this omitted `q2` layer. That is not a surviving branch and not a no-lift theorem.
- V2 existence: a corrected witness `W'` exists at this weight, as an exact element of the eight-row module, with unique least term `la^20`.
- Emptiness of the nine-coordinate torus localisation of `in_w(J)` at this single weight, for this fixed source, axis/cusp, loads `k=nu=0`, `mu=2/3`, and this full `Q` support.

Not admissible, and not claimed by the frozen firewall strings
`FIRST_ORDER_Q2_SYZYGY_LIFT_FIXED_AXIS_LOAD_ONLY_ITERATE_IF_LOW_TERMS_REMAIN` and
`RESULT.md` §Firewall:

- a complete Gröbner cone, or the finite list of strict halfspaces of all 37 terms (named in `RESULT.md` as the next proof-discriminating calculation, not performed here);
- all `q2` valuations, or a statement at weights other than the charged sample;
- moving axis, cusp, or loads;
- another support mask;
- a formal-arc / formal-lift obstruction;
- the whole double-root fan, D1, or JC2;
- a claim that the LPDP `la^20` preimage, with `q2=0` and nine Rees generators including `LT`, already settled this omitted layer (it did not; that is V1).

The reviewed LPDP witness remains valid on the `q2=0` special fibre. This package is the first exact preimage after the `q2` support is restored, at one weight.

---

## Nits, not defects

1. Harvest trees contain sentinels, `free.*`, `hostname`, `uname`, `nproc`, versions, UTC stamps, launch stdio, and the off-encoding compiled file, none of which are in `FREEZE.sha256`. They were used as custody, not as a second freeze.
2. Compiler JSON still says `iterate if minimum <= 80` while reporting `sample_min_weight: 80` uniquely `la^20`. That string would over-iterate the target layer. `RESULT.md` and the Promotion paragraph interpret the endpoint correctly: no below-target remainder.
3. `option(redSB)` is set in both encodings and never used; the jobs are polynomial-identity checks, not Gröbner bases.
4. The dummy variable `s` is in both rings only so `BASE{ell}` can be compared at `s=1`. It does not appear in `E`, `F`, `W`, `EXPECT`, or `CORR`.
5. Launcher displayed `$!` as `0`. PIDs are taken from `worker.metadata`, which matches `RESULT.md`.

No source or certificate repair is required.

Q2_SYZYGY_LIFT_CONFIRMED
