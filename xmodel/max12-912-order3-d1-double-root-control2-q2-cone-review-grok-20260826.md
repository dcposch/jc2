# Hostile text-only review — control-2 corrected-`q2` witness cone V3

| Field | Value |
|---|---|
| Claim under review | Complete strict halfspace region of one explicit 37-term membership witness `W'`, and the claim that on the slice `alpha=15/2` this same witness has unique least term `la^20` if and only if `beta>5` and `delta>5` (`T>0`) |
| Overall verdict | **Q2_WITNESS_CONE_CONFIRMED**. Dual AWS opposite-order runs reconstruct the literal reviewed `W'` (canonical SHA `ddb451c4…`) and emit byte-identical certificates. The 35 non-target terms produce exactly the 15 listed strict inequalities; at `alpha=15/2` those collapse to the necessary and sufficient pair `beta>5` and `delta>5`. The premise `delta>beta` is a separately charged control-2 leading-layer interpretation, not an algebraic cone inequality |
| Smallest failing identity | none in the frozen cone source, either AWS stream, the certificate JSON, or the hand weight/slice arithmetic |
| Smallest missing hypothesis for a stronger theorem | a full Gröbner cone or Newton fan; saturation of the faces `beta=5`, `delta=5`, or the corner; moving axis/cusp or loads; another support mask; a formal arc; the whole double-root locus; D1; JC2 |
| Evidence tier | SHA-256 of the freeze chain, source closure, and already-emitted AWS files; `cmp` of harvest copies and of the two certificate JSON files; integer/rational exponent and slice arithmetic on the already-printed 37-term dictionary; recomputation of the V1 canonical witness digest from those terms. No local Singular, Sage, msolve, gfan, Lean, Python algebra, compiler execution, or eight-row product replay |
| Reviewer / model | Grok 4.6 (xAI). Text-only tropical / commutative-algebra / CAS-custody referee |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `574e873d4753b57dbaeb0fb83e320fbef3694724` |
| Host | Darwin. Cone compiler, V2 compiler, V1 compiler, charged reconstruct, Singular, and every solver were not run |

## What was and was not run

No local substantive computation was run. In particular this review did **not** execute the cone compiler, the V2 or V1 compilers, `independent_reconstruct.py`, Singular, Sage, msolve, Lean, Gfan, or any other solver, and it did not re-multiply `sum F_i' E_i`. Hashes were checked with `shasum -a 256` and `sha256sum -c`. File identity was checked with `cmp`. Marker counts used `grep -c`. Git identity was read with `git rev-parse`. AWS streams and the certificate JSON were read as already-emitted text. Exponent sums, target flags, slice quantities `c+q u+d v`, and the 15 distinct forms were recomputed from those printed dictionaries by integer/rational arithmetic. The V1 canonical SHA of `W'` was recomputed from the certificate’s 37 coefficient/exponent records.

Pinned prerequisite, recomputed and matched, and not silently strengthened:

```text
2a2ff048c299a8878ea28211b72f0d0ad98f27216ae5c3462eb3bc076083ac7d
  xmodel/max12-912-order3-d1-double-root-control2-q2-syzygy-lift-review-grok-20260826.md
```

That review’s verdict is `Q2_SYZYGY_LIFT_CONFIRMED`. This cone package is charged as the halfspace list of that same polynomial, not as a new derivation of `W'` or of the eight rows.

Charged package anchors, recomputed and matched:

```text
c54c33be036410957d02ede886e3d237c9bc2675d73493b028c2fd4d4f1ff4de  FREEZE.sha256
0ed5eab56c10e7114850a9cbb915825d9a4f5f2360c97b25a644c8a64c6a14d7  RESULT.md
ee0639963d1d4788e6a4ba04fbf1c6f98246921d19dc29f2822c0cb136eae9c2  each cone_certificate.json
```

Support semantics were read from, and not inherited as a verdict from,

```text
6e86154863020e71fc5a1a69bdcad6912e98b163e32b3b85aa8e44833ef8cd1a
  xmodel/max12-912-order3-d1-control2-slope-uniform-review-grok-20260826.md
91bf351126d7db83ae6a697d67de28ffe4a0370cd73dbe58d48156fea8e2eb3a
  cases/max12_912_order3_d1_double_root_control2_q2_cone_v3_20260826/PREREGISTRATION.md
```

Every path listed in `FREEZE.sha256` recomputed and matched (23/23). Nested `SOURCE_CLOSURE.sha256` (8/8) matched from the case root, including the four sibling sources. Both harvested `result.sha256` manifests (5/5 each) matched from the respective harvest directory. Empty compiler stderr is the empty-string digest `e3b0c442…`. Both rc files are the two-byte string `"0\n"`, digest `9a271f2a…`.

Read in full before the verdict: every file at
`cases/max12_912_order3_d1_double_root_control2_q2_cone_v3_20260826/`
including both harvest trees; V2 `compile_q2_syzygy_lift_v2.py` far enough to see that the cone compiler’s `build_corrected` is the same untruncated eight-row product with the pinned free-zero correction `(g1,g2)=(1/12,-1/9)`; V1 `NAMES`, `digest`, `multipliers`, and `old_witness`; the pinned prerequisite lift review; and the slope-uniform review’s control-2 leading-layer table. Predecessor conclusions were recomputed, not inherited.

---

## Promotion

**Accept `FOR THE PINNED ORDINARY-TAIL EIGHT-ROW MODULE AT a=1, FIXED AXIS/CUSP, k=nu=0, mu=2/3, AND FULL SUPPORT Q=q2 z^2+q1 z+q0, THE REGISTERED DUAL-AWS CONE RUNS RECONSTRUCT THE LITERAL 37-TERM CORRECTED WITNESS W' OF CANONICAL SHA-256 ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b, THE SAME POLYNOMIAL WHOSE MEMBERSHIP W'=sum F_i' E_i WAS CHECKED IN THE PINNED V2 LIFT. NORMALIZE BY wt(la)=L, WRITE alpha=wt(r_i)/L, beta=wt(q1)=wt(q0)/L, delta=wt(q2)/L, t=T/L, h=H/L. THE UNIQUE LEAST-WEIGHT TERM OF THIS W' IS la^20 IF AND ONLY IF EVERY NON-TARGET TERM IS STRICTLY HEAVIER, WHICH IS THE CONJUNCTION OF T>0 WITH THE FIFTEEN DISTINCT STRICT HALFSPACES LISTED IN RESULT.md. AT THE UNIFORM CONTROL-2 SLICE alpha=15/2 THOSE FIFTEEN INEQUALITIES ARE NECESSARY AND SUFFICIENT FOR THE OPEN QUADRANT beta>5 AND delta>5 (STILL WITH T>0): NECESSITY IS FORCED BY PRESENT NONZERO MONOMIALS q1 q0^3 AND THE FIVE OLD q r r TERMS FOR beta, AND BY q2^4 AND THE FIVE NONZERO q2 r r TERMS FOR delta; SUFFICIENCY HOLDS FOR EVERY REPEATED TERM AFTER THE SUBSTITUTION beta=5+u, delta=5+v, BECAUSE EVERY NON-TARGET MARGIN IS c+q u+d v WITH c,q,d>=0 AND EITHER c>0 OR q+d>0. THIS IS THE COMPLETE STRICT HALFSPACE REGION OF ONE EXPLICIT MEMBERSHIP WITNESS, NOT A GRÖBNER CONE, TROPICAL FAN, OR INITIAL-IDEAL CLASSIFICATION. SEPARATELY: IF q1,q0 FORM THE CHARGED LEADING CONTROL-2 Q-LAYER AT VALUATION beta AND q2 IS A LATER ACTIVATING COEFFICIENT, THEN delta>beta. ON THE ALREADY CHARGED WINDOW 5<beta<6 THAT PREMISE IMPLIES delta>5, SO THIS WITNESS EXCLUDES EVERY LATER q2 ACTIVATION IN THIS FIXED SOURCE/LOAD CHART. TOGETHER WITH THE REVIEWED q2=0 WITNESS THERE IS NO GAP BETWEEN IDENTICALLY ZERO q2 AND LATER-ACTIVATING q2 ON THIS CHART. THE FACES beta=5, delta=5, AND THE CORNER beta=delta=5 ARE NOT SETTLED.`**

Do not promote this to: a complete Gröbner cone or Newton fan; an equality-face saturation; a statement at a different `alpha`; moving axis, cusp, or loads; another support mask; a fact that `delta>beta` holds for arbitrary Q-support; a simultaneous-leading `q2` (control-1) chart; a formal-arc obstruction; the whole double-root locus; D1; or JC2.

---

## Charge 1 — Custody, freeze, dual AWS, opposite order

**CONFIRMED. Every freeze entry recomputes. Both registered workers are fail-closed, hash-gated, empty-stderr, sub-cap, and source-closed against the package-root manifest. The two certificate JSON files are byte-identical.**

Recomputed `FREEZE.sha256` entries, all matched:

```text
0ed5eab56c10e7114850a9cbb915825d9a4f5f2360c97b25a644c8a64c6a14d7  RESULT.md
91bf351126d7db83ae6a697d67de28ffe4a0370cd73dbe58d48156fea8e2eb3a  PREREGISTRATION.md
bb6a2491335e308b22aed260e25eff8f40346037b527c5db264f06dd98ee2968  AWS_REGISTRATION.md
deccac3cbf2d14a081e3678849114fa3e807deb15f6c773539d8c90466cf8ae6  AWS_LAUNCH_METADATA.md
9628c8a3ab4404e80a90ac50b699172945d1795f5112957a9f29cebe9d0f32cd  SOURCE_CLOSURE.sha256
8b908fe44f95d89ed8c684f51265cc97a90adf18bf86f0ad7ec7e24af0665ce6  compile_q2_cone_v3.py
d7548aa600c0983ea23c8673e6f5d7932cf2182259b584b483f7a52d39ffad07  remote_worker.sh
ee0639963d1d4788e6a4ba04fbf1c6f98246921d19dc29f2822c0cb136eae9c2  aws_box03_forward/cone_certificate.json
6c98900956e7d8ff20dde47000bf5fdd5a52636ad2cad5f32346634fe7248760  aws_box03_forward/compiler.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_box03_forward/compiler.stderr
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  aws_box03_forward/compiler.rc
a8289a6b1eca0d88795c58b38ee67a627e989becf7698c021930dfed2a8b2b05  aws_box03_forward/compiler.time
e7d3c8d85656a4a145e836f10e764f36dec15dc6c21afdf41db7819149035d76  aws_box03_forward/result.sha256
c8cd4198e3a0deb5c9b0d861ca23623c047311e0bcf55866f06c55d766f8f5dc  aws_box03_forward/source.check
105516d490286a16f1b4f3ae48daf4667938ceddb7ff09ef450d43b857212a3c  aws_box03_forward/worker.metadata
ee0639963d1d4788e6a4ba04fbf1c6f98246921d19dc29f2822c0cb136eae9c2  aws_r6d_reverse/cone_certificate.json
03963def7bc68a15a3b81b986e65d3119369e9285e6e77ac449a2c5fa9900f0d  aws_r6d_reverse/compiler.stdout
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  aws_r6d_reverse/compiler.stderr
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  aws_r6d_reverse/compiler.rc
23190b2ff279d7411d7127b4eb8ef97b6c1319d2e513182013799b5401255ffe  aws_r6d_reverse/compiler.time
09a68720c4b06d754a362663b9ba0e31e62db82212188c67f0c0f8bca267d9a1  aws_r6d_reverse/result.sha256
c8cd4198e3a0deb5c9b0d861ca23623c047311e0bcf55866f06c55d766f8f5dc  aws_r6d_reverse/source.check
1e73c5d53948d9e8eecad35ee6c43fa24805752fd0da2b2f5c3b190c1773e9f4  aws_r6d_reverse/worker.metadata
```

Source-closure entries, all matched from the package root:

```text
91bf351126d7db83ae6a697d67de28ffe4a0370cd73dbe58d48156fea8e2eb3a  PREREGISTRATION.md
bb6a2491335e308b22aed260e25eff8f40346037b527c5db264f06dd98ee2968  AWS_REGISTRATION.md
8b908fe44f95d89ed8c684f51265cc97a90adf18bf86f0ad7ec7e24af0665ce6  compile_q2_cone_v3.py
d7548aa600c0983ea23c8673e6f5d7932cf2182259b584b483f7a52d39ffad07  remote_worker.sh
5c8e74ffa2acee40ab8ab0c2e68c44ddcbc2927722994c0d7488eb6c389f4611  ../max12_912_order3_d1_double_root_control2_q2_syzygy_lift_v2_20260826/compile_q2_syzygy_lift_v2.py
0385b0b1e60b3bd37fa5fbee90dd6c17a454722bdbff424ea83c2ab0fa19df45  ../max12_912_order3_d1_double_root_control2_q2_first_lift_v1_20260826/compile_q2_first_lift.py
67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623  ../max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/independent_reconstruct.py
c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b  ../max12_912_order3_d1_double_root_control2_la20_syzygy_20260826/base_B.sing
```

The V2 compiler hash `5c8e74ffa2…` is both a source-closure entry and the cone compiler’s hardcoded `V2_SHA`. It is the same file charged in the pinned lift review. Harvested `SOURCE_CLOSURE.sha256` is byte-identical to the top copy on both hosts. Both `source.check` files are identical (`c8cd4198…`) and print `OK` on those eight paths. The worker `cd`s to the package root before `sha256sum -c SOURCE_CLOSURE.sha256`; the sibling `../max12_…` paths are therefore `cases/`-neighbours, which is how AWS ran and how this review rechecked. Treating `aws_box03_forward/` or `aws_r6d_reverse/` as a new source root would make those siblings invisible. That is not the charged root.

| Check | Box03 forward | r6d reverse |
|---|---|---|
| Public IP / harvested hostname | `98.80.65.144` / `ip-172-30-0-249` | `100.26.198.153` / `ip-172-30-0-45` |
| Tag | `…_cone_v3_20260826T034000Z_box03_forward` | `…_cone_v3_20260826T034000Z_r6d_reverse` |
| Worker PID | `152186` | `219931` |
| Caps | 2 GiB (`ulimit -v 2097152`) / 600 s; `nice -n 10` | same |
| Started / finished UTC | `03:37:38Z` / `03:38:19Z` | same timestamps |
| Traversal | `ORDER=forward` | `ORDER=reverse` |
| Compiler stdout SHA | `6c989009…` | `03963def…` |
| Certificate SHA | `ee063996…` | `ee063996…` (byte-identical) |
| RSS / swap / exit | 20856 KiB / `Swaps: 0` / 0 | 20392 KiB / `Swaps: 0` / 0 |
| Wall clock | 5.80 s | 5.85 s |
| Pre/post `free` swap | `0B` / `0B` | `0B` / `0B` |
| PASS markers, each once | `PASS_Q2_CONE_V3`, `PASS_REMOTE_WORKER` | same |
| `FAIL_` / `REFUSED` / `FAILED` | none; empty stderr | none; empty stderr |

`AWS_LAUNCH_METADATA.md` is timestamped `2026-08-26T03:37:52Z`, after worker start and before either finish, with state `WAITING_GO` and no GO sentinel then present. PIDs come from `worker.metadata`, not from a launcher `$!`. GO and DONE sentinels exist and are empty. No `REFUSED` or `FAILED`. Harvest copies of compiler, worker, preregistration, AWS registration, and source closure are byte-identical to the package top.

The two certificate JSON files compare equal as bytes (`cmp` silent, common SHA `ee063996…`). Compiler stdout differs in exactly one line, `ORDER=forward` versus `ORDER=reverse`; every other printed field (`W_SHA256`, `TERM_COUNT=37`, `DISTINCT_FORM_COUNT=17`, face-tie counts `6/6/20`, certificate SHA, `PASS_Q2_CONE_V3`) is identical. Opposite traversal is therefore live in the worker metadata and in the compiler’s `--order` argument, and is then canonicalized: records, grouped forms, and face lists are re-sorted before `json.dumps(..., sort_keys=True)`. That is the intended dual-order identity check, not a second derivation.

No diagnostic or custody gap. No AWS replay is required.

---

## Charge 2 — Literal 37-term `W'`, not a silently altered polynomial

**CONFIRMED. The cone compiler reconstructs the same dictionary as V2 `EXPECT`, gates on the pinned canonical SHA, and does not drop, combine, specialize, or rederive a different polynomial. The 37 certificate monomials are exactly the 37 monomials charged in the lift review.**

Construction, from the hash-pinned cone compiler and the pinned V2 source it imports:

1. Refuse non-Linux / non-EC2 / unregistered tag. Load V2 only after `sha256(V2)==5c8e74ffa2…`.
2. `base = v2.load_v1()`, which itself hash-pins V1 `0385b0b1…` and the charged reconstruct `67343b56…`.
3. Rows are the same substituted ordinary tails as V2: `rows[ell] = substitute(tails[ell], coefficient_images()) - target(ell)`, with `q2` present in the coefficient images. This is not a `q2=0` specialization and not a printed-CAS parse.
4. Multipliers start from V1 `multipliers()`. The cone compiler then adds the pinned free-zero correction `F1 += q2/12`, `F2 += -q2/9`, rather than re-solving the weight-52 linear system. That is a pin of the lift review’s unique free-zero solution `(g1,...,g8)=(1/12,-1/9,0,...,0)`, not a silent rederivation of a different combination.
5. `W'` is the untruncated dictionary product `sum_{ell=1}^8 F_ell' * rows[ell]`. Like terms are added; zero coefficients are cleaned. The compiler then fail-closes unless `len(corrected)==37` and `base.digest(corrected)==ddb451c4…`.

The digest is the V1 canonical SHA: sorted monomial tuples in `NAMES=(la,tau,rho,q2,q1,q0,r2,r1,r0)` order, JSON of `{exponents, numerator, denominator}`, SHA-256. Recomputed from the 37 already-printed certificate records, it is again

```text
ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b
```

matching V2 `RESULT.md`, the cone `RESULT.md`, both AWS stdout lines, and the certificate field `corrected_w_sha256`. Collision-resistance of SHA-256 identifies the dictionary. The eight `q2=0` terms of `W'` reproduce V1 `old_witness()` coefficient-for-coefficient (`la^20`, `la^20 tau`, `q1 q0^3`, and the five old `q r r` terms). The remaining 29 monomials are exactly the lift review’s `q2`-positive support.

Reconciliation of the 37 terms:

- 1 target: `la^20`, coefficient `1`, flagged `target`.
- 1 positive-split target: `la^20 tau`, coefficient `1`, flagged `positive_split_target`.
- 35 other terms, every coefficient nonzero in `Q`.

Target flags were recomputed from exponents: `la==20` and total degree 20 for the target; `la==20`, `tau==1`, and total degree 21 for the split. No other record matches either test. No record has `rho`. No non-target record has `la` or `tau`. The compiler therefore did not silently absorb the split target into the target, and did not drop a vanishing-looking but actually nonzero term.

---

## Charge 3 — Weight map, 15 inequalities, 17 forms, 37 terms

**CONFIRMED. The 35 non-target terms yield exactly the 15 distinct strict inequalities in `RESULT.md`. The certificate retains every repetition. The counts 37, 17, and 15 are mutually consistent.**

Normalize by `wt(la)=L`. The actual affine weight used by the compiler and by `PREREGISTRATION.md` is

```text
wt/L = e_q2 * delta + (e_q1+e_q0) * beta
     + (e_r2+e_r1+e_r0) * alpha + e_la
     + (T/L) * e_tau + (H/L) * e_rho.
```

Target subtraction is the comparison `wt/L > 20`, equivalently the difference form

```text
e_q2*delta + (e_q1+e_q0)*beta + (e_r)*alpha + (e_la-20) + t*e_tau + h*e_rho.
```

The compiler stores that difference as
`(delta, beta, alpha, constant, t, h)` with `constant = e_la-20`. Every record’s stored form recomputes from its exponents; zero mismatches. The prompt’s writing `20*e_la` in the absolute `wt/L` slot is not the formula used: `wt(la)=L` contributes `e_la`, and the `20` appears only as the target subtraction. Charging the compiler/preregistration formula, not the slipped `20*e_la`.

The relation `L=3T+H` is **not used** in these inequalities. No non-target term contains `tau` or `rho`. The split target `la^20 tau` is heavier precisely when `T>0`. `H` does not enter uniqueness. Homogeneity of `la = tau^3 rho` is a chart hypothesis of the already-reviewed control-2 split, not a cone generator.

All 35 non-target terms have `e_la=0`, hence `constant=-20`, and `t=h=0`. Each therefore imposes

```text
e_q2 * delta + (e_q1+e_q0) * beta + (e_r) * alpha > 20.
```

Distinct forms, with multiplicity, nonzero coefficients, and the listed halfspace:

| form `(e_q2, e_q1+e_q0, e_r)` | mult. | monomials | inequality |
|---|---|---|---|
| `(0,1,2)` | 5 | `q1 r2 r1` (`1/54`), `q1 r1^2` (`7/108`), `q1 r2 r0` (`1/54`), `q1 r0^2` (`1/108`), `q0 r1 r0` (`-1/54`) | `beta + 2 alpha > 20` |
| `(0,4,0)` | 1 | `q1 q0^3` (`1/243`) | `4 beta > 20` |
| `(1,0,2)` | 5 | `q2 r2^2` (`5/54`), `q2 r2 r1` (`1/9`), `q2 r1^2` (`4/81`), `q2 r2 r0` (`1/162`), `q2 r1 r0` (`1/18`) | `delta + 2 alpha > 20` |
| `(1,1,2)` | 1 | `q2 q1 r2^2` (`-1/243`) | `delta + beta + 2 alpha > 20` |
| `(1,2,1)` | 4 | `q2 q1^2 r2` (`-1/54`), `q2 q1^2 r0` (`-1/486`), `q2 q1 q0 r1` (`1/486`), `q2 q0^2 r2` (`5/486`) | `delta + 2 beta + alpha > 20` |
| `(1,3,0)` | 3 | `q2 q1^3` (`-1/81`), `q2 q1^2 q0` (`-5/243`), `q2 q1 q0^2` (`5/162`) | `delta + 3 beta > 20` |
| `(2,1,1)` | 4 | `q2^2 q1 r2` (`-1/54`), `q2^2 q1 r1` (`-5/162`), `q2^2 q0 r2` (`5/162`), `q2^2 q0 r0` (`1/243`) | `2 delta + beta + alpha > 20` |
| `(2,2,0)` | 3 | `q2^2 q1^2` (`-4/81`), `q2^2 q1 q0` (`1/18`), `q2^2 q0^2` (`-5/243`) | `2 delta + 2 beta > 20` |
| `(2,3,0)` | 1 | `q2^2 q1^3` (`5/2916`) | `2 delta + 3 beta > 20` |
| `(3,0,1)` | 2 | `q2^3 r2` (`1/81`), `q2^3 r1` (`-4/243`) | `3 delta + alpha > 20` |
| `(3,1,0)` | 2 | `q2^3 q1` (`7/162`), `q2^3 q0` (`-2/27`) | `3 delta + beta > 20` |
| `(3,2,0)` | 1 | `q2^3 q1 q0` (`-1/1458`) | `3 delta + 2 beta > 20` |
| `(4,0,0)` | 1 | `q2^4` (`-11/162`) | `4 delta > 20` |
| `(4,1,0)` | 1 | `q2^4 q1` (`19/5832`) | `4 delta + beta > 20` |
| `(5,0,0)` | 1 | `q2^5` (`4/2187`) | `5 delta > 20` |

These are exactly the 15 inequalities printed in `RESULT.md`, in the same generating set, with no extra and no omitted form. Adding the two target forms `(0,0,0,0,0,0)` for `la^20` and `(0,0,0,0,1,0)` for `la^20 tau` gives 17 grouped forms. Multiplicities sum to `5+1+5+1+4+3+4+3+1+2+2+1+1+1+1=35` non-target terms, plus 2 targets = 37. Grouped-form multiplicity in the JSON equals the record count per key. The certificate therefore retains repetitions (five old `q r r`, five `q2 r r`, four mixed cubics of type `(1,2,1)`, and so on) and does not silently discard a vanishing-looking support class: every listed coefficient is nonzero, and the missing monomials `q2 r0^2` and `q2 q0^3` are absent from `W'` already in the lift review, not dropped here.

Why 37, 17, and 15 are consistent: 37 is the support of the polynomial; 17 is the number of distinct difference-forms of that support, including the two target forms which do not impose a halfspace; 15 is the number of remaining forms, each one strict inequality. Repetition does not create new walls and is not permission to drop a wall.

---

## Charge 4 — Slice `alpha=15/2`: necessity and sufficiency of `beta>5` and `delta>5`

**CONFIRMED. On this slice, with `T>0`, unique least term `la^20` if and only if `beta>5` and `delta>5`. Necessity is charged from present monomials. Sufficiency holds for every repeated term. The substitution `beta=5+u`, `delta=5+v` has all margins of the stated shape, all nonnegative, and none identically zero.**

Substitute `alpha=15/2`. The 15 inequalities become:

```text
beta > 5                      (from beta+2 alpha > 20)
beta > 5                      (from 4 beta > 20)
delta > 5                     (from delta+2 alpha > 20)
delta + beta > 5
delta + 2 beta > 25/2
delta + 3 beta > 20
2 delta + beta > 25/2
delta + beta > 10
2 delta + 3 beta > 20
delta > 25/6                  (from 3 delta + alpha > 20)
3 delta + beta > 20
3 delta + 2 beta > 20
delta > 5                     (from 4 delta > 20)
4 delta + beta > 20
delta > 4                     (from 5 delta > 20).
```

**Necessity from present monomials.** Unique least `la^20` requires every non-target term strictly heavier.

- The five old `q r r` terms all have form `beta+2 alpha` and all have nonzero coefficients. At this `alpha` they force `beta>5`. Independently, the present monomial `q1 q0^3` forces `4 beta>20`, hence again `beta>5`, even without using `alpha`. If `beta=5`, those six terms tie with `la^20` (Charge 6). A relaxed list that omitted `q1 q0^3` would still have the five `q r r`; a list that omitted the five `q r r` would still have `q1 q0^3`. Both classes are present.
- The five nonzero `q2 r r` terms all have form `delta+2 alpha` and all have nonzero coefficients. At this `alpha` they force `delta>5`. Independently, the present monomial `q2^4` forces `4 delta>20`, hence again `delta>5`. The monomial `q2^5` only forces `delta>4`, which is **not** the binding wall; necessity of `delta>5` does not come from `q2^5`. If `delta=5`, the five `q2 r r` and `q2^4` tie with `la^20`. Both binding classes are present.

Thus `beta>5` and `delta>5` are necessary. `T>0` is necessary because `la^20 tau` has difference `t`.

**Sufficiency, every repeated term.** Write `beta=5+u`, `delta=5+v`. For a non-target form `(d,q,a)=(e_q2, e_q1+e_q0, e_r)` the exact difference from target weight is

```text
c + q u + d v,
c = -20 + 5 q + 5 d + (15/2) a.
```

Every stored certificate slice triple recomputes (zero mismatches). Hand values:

| form | `c` | `q` | `d` | margin | at `u>0,v>0` |
|---|---|---|---|---|---|
| `(0,1,2)` ×5 | `0` | 1 | 0 | `u` | `>0` |
| `(0,4,0)` ×1 | `0` | 4 | 0 | `4u` | `>0` |
| `(1,0,2)` ×5 | `0` | 0 | 1 | `v` | `>0` |
| `(1,1,2)` ×1 | `5` | 1 | 1 | `5+u+v` | `>0` |
| `(1,2,1)` ×4 | `5/2` | 2 | 1 | `5/2+2u+v` | `>0` |
| `(1,3,0)` ×3 | `0` | 3 | 1 | `3u+v` | `>0` |
| `(2,1,1)` ×4 | `5/2` | 1 | 2 | `5/2+u+2v` | `>0` |
| `(2,2,0)` ×3 | `0` | 2 | 2 | `2u+2v` | `>0` |
| `(2,3,0)` ×1 | `5` | 3 | 2 | `5+3u+2v` | `>0` |
| `(3,0,1)` ×2 | `5/2` | 0 | 3 | `5/2+3v` | `>0` |
| `(3,1,0)` ×2 | `0` | 1 | 3 | `u+3v` | `>0` |
| `(3,2,0)` ×1 | `5` | 2 | 3 | `5+2u+3v` | `>0` |
| `(4,0,0)` ×1 | `0` | 0 | 4 | `4v` | `>0` |
| `(4,1,0)` ×1 | `5` | 1 | 4 | `5+u+4v` | `>0` |
| `(5,0,0)` ×1 | `5` | 0 | 5 | `5+5v` | `>0` |

In every row `c,q,d >= 0`, and either `c>0` or `q+d>0`. No non-target form is the zero form. Every repetition of a form has the same `(c,q,d)`: there is no hidden `tau`/`rho`/`la` on any copy that would change the margin. Therefore `u>0` and `v>0` make every one of the 35 non-target terms strictly heavier than `la^20`. Together with `t>0`, the unique least term is `la^20`.

The two binding walls are exactly `u=0` and `v=0`. No listed inequality cuts a stronger open set (for instance `beta>6` or `delta>6`): at the corner limit `(u,v)→(0,0)` the non-binding forms retain a strictly positive `c` (`5` or `5/2`), and the binding forms become ties rather than reverse inequalities. On the open quadrant the 15 halfspaces are therefore equivalent to the pair `beta>5` and `delta>5`.

---

## Charge 5 — Semantic premise `delta>beta`, separately from the cone

**CONFIRMED as a separately charged control-2 leading-layer interpretation, and only under that hypothesis. It is not an algebraic generator of the witness cone, not a fact about arbitrary support masks, and not a statement on equality faces.**

The algebraic object is the open set of weights for which this one polynomial has unique least term `la^20`. That set, on `alpha=15/2`, is `beta>5`, `delta>5`, `T>0`. The inequality `delta>beta` does not appear among the 15 halfspaces and is not used in the slice arithmetic.

It is licensed only in the following charged situation, read from the slope-uniform control-2 mapping and from `PREREGISTRATION.md`, not re-proved here as Newton geometry:

- The charged leading control-2 Q-layer is linear, `Q = t^{beta}(z-1)`, so the leading coordinates at valuation `beta` are `q1,q0`, both required nonzero on that torus.
- `q2` is *not* a simultaneous leading coordinate of that jet. A simultaneous leading `q2` would be the control-1 (quadratic) support `Q = t^{beta}(z-1)(z+2)`, which is a different mask and is firewalled.
- A later activation of the same coordinate `q2` in this full-support ring is the valuation condition `delta = wt(q2)/L > beta`.

Under that hypothesis, and on the already charged window `5<beta<6`, one has `delta>beta>5`, hence `delta>5`. The algebraic cone then applies, and this witness excludes every later-`q2` activation in the fixed source/load chart `a=1`, `h=0`, `k=nu=0`, `mu=2/3`, `alpha=15/2`. The identically-zero alternative `q2≡0` is the already-reviewed five-coefficient witness (slope-uniform / LPDP `W`), which excludes the same `alpha=15/2`, `5<beta<6` face on the `q2=0` support. There is therefore no gap, in this fixed chart, between “`q2` is identically zero” and “`q2` activates later than the leading `q1,q0` layer.”

What this does **not** say:

- It does not force `delta>beta` on an arbitrary Q-support, or on a mask in which `q2` is allowed to lead.
- It does not settle `delta=beta` (simultaneous leading `q2`, a different chart).
- It does not extend off `5<beta<6` as a control-2 statement; `beta>6` may still make `la^20` the unique least term of this polynomial, but that is not charged control-2 geometry.
- It is not a replacement of the `q2=0` theorem, and not a claim that every omitted higher jet of the same coordinates is visible to `in_w`.

The certificate JSON string packs “in particular `5<beta<6` and later q2 activation `delta>beta`” into the `theorem` field. `RESULT.md` and `PREREGISTRATION.md` keep the algebraic quadrant and the semantic mapping in separate paragraphs. The promotion paragraph above follows the reports, not the compressed JSON field.

---

## Charge 6 — Tie sets and the witness-cone firewall

**CONFIRMED. The three exact tie sets match the certificate, the compiler’s `c=0` tests, and `RESULT.md`. No equality-face, Gröbner-cone, or tropical-fan conclusion is taken.**

On the slice `alpha=15/2`, `T>0`, a non-target term ties with `la^20` precisely when its margin `c+q u+d v` vanishes.

- `beta=5`, `delta>5` (`u=0`, `v>0`): ties are the forms with `c=0` and `d=0`, namely `(0,1,2)` and `(0,4,0)`. Six monomials: `q1 q0^3` and the five old `q r r` terms `q1 r2 r1`, `q1 r1^2`, `q1 r2 r0`, `q1 r0^2`, `q0 r1 r0`. This is the already identified beta face of the `q2=0` witness; restoring `q2` at `delta>5` does not kill it. The five `q2 r r` and `q2^4` stay strictly above.
- `delta=5`, `beta>5` (`v=0`, `u>0`): ties are the forms with `c=0` and `q=0`, namely `(1,0,2)` and `(4,0,0)`. Six monomials: the five nonzero `q2 r r` terms `q2 r2^2`, `q2 r2 r1`, `q2 r1^2`, `q2 r2 r0`, `q2 r1 r0`, and `q2^4`. The term `q2^5` has `c=5` and does **not** tie. The old `q r r` and `q1 q0^3` stay strictly above.
- `beta=delta=5` (`u=v=0`): ties are all forms with `c=0`. Twenty non-target monomials: the union of the two six-term faces (12) plus eight mixed quartics of total `(q,q2)`-degree four,

  ```text
  q2 q1^3, q2 q1^2 q0, q2 q1 q0^2,
  q2^2 q1^2, q2^2 q1 q0, q2^2 q0^2,
  q2^3 q1, q2^3 q0.
  ```

  The eight remaining non-target terms have `c∈{5,5/2}` and stay strictly above, as does `la^20 tau`.

Certificate lists, compiler appends, and this `c=0` classification are the same sets (counts 6, 6, 20). Exact exponent dictionaries are in the JSON.

Firewall, as stated in `RESULT.md` and in the certificate field `witness cone only; equality faces require saturation`:

- this is the complete strict halfspace region of one explicit ideal-membership witness;
- it is not a full Gröbner cone, tropical fan, or classification of `in_w(J)` as a function of the weight;
- it freezes source, axis/cusp, and loads `k=nu=0`, `mu=2/3`;
- it does not cover moving axis/cusp, moving loads, another normal coefficient, equality faces, a formal arc, the whole double-root locus, D1, or JC2;
- the beta ray, delta ray, and corner need full exact initial-ideal / torus saturations if they are geometrically allowed;
- other elements of `J` may add further initial generators; they cannot remove `la^20` from `in_w(J)` on the open quadrant where this `W'` is monomial with initial form `la^20`.

---

## Charge 7 — Licensed theorem

**CONFIRMED. The strongest theorem is the Promotion paragraph. No source or certificate repair is required.**

Admissible:

- reconstruction of the pinned 37-term `W'` as an exact element of the eight-row module;
- the 15 strict halfspaces of that polynomial, with repetitions retained;
- unique least term `la^20` on `alpha=15/2`, `beta>5`, `delta>5`, `T>0`, equivalently the necessity and sufficiency of that pair for this witness;
- under the separate control-2 leading-layer hypothesis, exclusion of every later `q2` activation on `5<beta<6` in this fixed chart, with no gap against the reviewed `q2=0` witness.

Not admissible, and not claimed by the frozen firewall once the JSON `theorem` field is read through `RESULT.md`:

- a complete Gröbner cone or Newton fan;
- any equality-face conclusion;
- `delta>beta` as an algebraic fact, or as a statement on other supports;
- moving axis, cusp, or loads; another normal direction; a formal arc; the whole double-root locus; D1; JC2.

## Nits, not defects

1. `RESULT.md` still says “hostile review of the underlying lift is pending.” The lift review `2a2ff048…` now exists and is `Q2_SYZYGY_LIFT_CONFIRMED`. Timestamp lag, not a contradiction of the identities.
2. The certificate `theorem` string concatenates the algebraic quadrant with the semantic `delta>beta` clause. `RESULT.md` and `PREREGISTRATION.md` already separate them. The promotion paragraph follows the reports.
3. Harvest trees contain sentinels, `free.*`, `hostname`, `uname`, `nproc`, UTC stamps, and launch stdio, none of which are in `FREEZE.sha256`. They were used as custody, not as a second freeze.
4. `L=3T+H` is a chart hypothesis of the control-2 split and is not an input to the 15 inequalities. Harmless, and not claimed as a cone generator.
5. Trailing period after the certificate SHA in `RESULT.md` is punctuation.

No source, certificate, or theorem repair is required. No AWS computation is required: both registered traversals already reconstructed `W'` and emitted identical certificates, and the cone step is finite-support arithmetic on that frozen dictionary.

Q2_WITNESS_CONE_CONFIRMED
