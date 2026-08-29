# Hostile review — TD6 V89H12 all-q P12 full normal form

| Field | Value |
|---|---|
| Target | Frozen producer package `cases/td6_c1_c2_c3_allq_mod_f_unitriangular_functional_v89h10_aws_20260826/`; controlling pins `P12_FULL_NORMAL_FORM_RESULT.md`, `P12_FULL_NORMAL_FORM_EVIDENCE.sha256`, `P12_FULL_NORMAL_FORM_FREEZE.sha256`, `PREREGISTRATION_P12_FULL_NORMAL_FORM.md`, `SOURCE_P12_FULL_NORMAL_FORM.sha256`, `source_p12_full_normal_form_r3.tar.gz`, R3 client, H11 free-count erratum, H11 corrective hostile review |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest bad coefficient / denominator / omission | none |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile algebra review. Producer `PASS` banners, dual-host byte identity, and RSS/elapsed lines are custody only |
| Method | SHA-256 of every charged pin and every consumed manifest row; independent local replay of the R3 client into `/tmp/td6_v89h12_review_recompute` (exit 0, 221s) producing byte-identical copies of all thirteen mathematical artifacts; independent rebuild of the 94-element nonpivot complement from the frozen 38-pivot list; flint factorization in `Q[V,U]` of every scalar denominator in the affine pivot map (22,014) and the P12 normal form (2,988); source review of V87 reconstruction, H5 Gaussian inversion, H6 `F=0` chart, H10T/H11 flag, the 95 triangular solves, and literal-P12 substitution. No Singular, Sage, Lean, or `jc2-lean`. The AWS wrapper was not re-run (EC2/Linux gated); the Python client was |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Prompt SHA-256 `6fb50e3ba3a0fbf0eb37ca30adbf1bea3537f0ac6f26b3e41fd2874cddaac155` matched. Independently recomputed SHA-256 of every required primary pin matches. Every path named in `P12_FULL_NORMAL_FORM_FREEZE.sha256` (16/16), `P12_FULL_NORMAL_FORM_EVIDENCE.sha256` (82/82), `SOURCE_P12_FULL_NORMAL_FORM.sha256` (12/12), `SOURCE_P12_FLAG.sha256` (25/25), and `PAYLOAD_CLOSURE.sha256` (56/56) rehashes to the printed digest. Every `SOURCE_P12_FULL_NORMAL_FORM.sha256` and `SOURCE_P12_FLAG.sha256` row exists at the case root and as `source/<path>` inside `source_p12_full_normal_form_r3.tar.gz`, and both copies match. All 56 payload-closure files exist inside the same tarball and on disk and match. Nested compiler hash pins consumed from that archive also match. Producer `TD6-V89H12-ALLQ-P12-FULL-NORMAL-FORM PASS` was not used as algebra. V1, R1, and R2 are pre-result failures and are not used as mathematical evidence. No file other than this review was written. The frozen producer package, campaign ledgers, and `jc2-lean` were not edited.

---

## Verdict

**CONFIRMED.**

On the frozen V89H10T `F=0` specialization over the registered open `D(U*H*B3)`, the R3 client rebuilds genuine literal P12 (2,893 parameter terms) and all 38 original packed FIRST rows, retains the 22 independent untruncated coordinates `q2,...,q14,q16,...,q24`, and omits q15 only as the reviewed target shear of frozen `(p,q)=(t^{15}, t+\cdots+t^{25})`. The raw common source denominator is exactly `U*H=U(C-3U^2)`, coprime to `F`.

The transported kernel has 132 coordinates. The frozen FIRST pivot list has 38 distinct coordinates. The complementary nonpivot set, rebuilt from that pivot list, has **94** labels. The number 17 is the number of nonzero parameter records in the P12 normal form (empty monomial plus 16 singletons), not the quotient dimension. Sixteen of those 94 quotient variables survive in P12; the other 78 cancel exactly.

The 38 FIRST rows are affine-linear in the jet parameters. Their 38-by-38 pivot block `A(q)` is unimodular over the localized q-polynomial ring because the relative matrix `N=A(0)^{-1}A(q)-I` is strictly upper triangular after a *constant* flag change of pivot basis and a constant permutation. The triangular recursion solves the constant equation and each of the 94 nonpivot directions in the original FIRST matrix. Direct substitution recovers the original right-hand side (constant) and annihilates `A p + D e_j` (each direction). Deleting one active pivot-direction component breaks that identity.

Exact substitution of the complete affine pivot map into every literal P12 term yields a unique original-FIRST normal form of 166 nonzero `(parameter monomial, q monomial)` records, parameter degree one, q degree one, and no mixed-q monomial. Parameter support is exactly `(),6,8,9,11,12,13,15,16,17,18,20,21,22,24,25,27`. Q support is exactly `(),q2,...,q14`. Coordinates `q16,...,q24` are present in the constant FIRST solution, the affine pivot map, and the strict-upper `N`, and vanish after the complete 2,893-term reduction. The normal form is separately affine in the surviving quotient variables and in q; terms `q_e*y_j` occur (153 of 166 records), so no joint total-degree-one claim is made.

The empty-parameter coefficient equals frozen H11 exactly, SHA256 `530d3c78df4d1dd43a892976aede83bcc6aefd697a40be71a195e83cbc15a7f8`. The complete pure-q14 class equals frozen V89H6 exactly, SHA256 `56ebf08a3f9814f714920a4fcb3ae7fb0957db0c0f6d231382f9b5efbf3321a2`.

Up to units the output denominators are exactly the charged maxima

```text
affine pivot map: U^7 V^4 (V^2-4U^3)^2
P12 normal form:  U^5 V^4 (V^2-4U^3)^2
```

Every flint factor of every scalar denominator lies in `{U, V, V^2-4U^3}`. Arithmetic is Python/custom exact E3/`QPoly`; `QPoly.inverse` refuses a nonconstant-q element; the triangular solve never inverts a q polynomial. The theorem is the complete canonical P12 normal form modulo original FIRST in this exact `F=0`, all-22-q scope. It is not a common-zero, unit-ideal, source-exclusion, projective-chart, q15, total-Rees, TD6-closure, or JC2 claim.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Frozen pins | controlling hashes | all nine required pins match |
| 0. Manifests | every named file | `P12_FULL_NORMAL_FORM_FREEZE` 16/16, `P12_FULL_NORMAL_FORM_EVIDENCE` 82/82, `SOURCE_P12_FULL_NORMAL_FORM` 12/12, `SOURCE_P12_FLAG` 25/25, `PAYLOAD_CLOSURE` 56/56; tarball copies match |
| 0. Dual AWS R3 | hosts, archive, rc | distinct Box02 / r6d; archive `c5ead84f…`; both `rc=0`; math artifacts and stdout byte-identical |
| 0. Independent replay | local client | exit 0, 221s; all thirteen output files byte-identical to AWS R3 |
| 0. V1 / R1 / R2 | not math evidence | V1 missing `TD6_Q_EXPONENT` pre-algebra; R1 `assert len(free_variables)==17` stop after compile; R2 filename-case `FORM` vs `form`, rc 127 before import. Only R3 supports mathematics |
| 1. Literal scope | P12 2893 terms, 38 FIRST, 22 q, q15 shear, `F=0` | V87 rebuild; `Q_EXPONENTS` skips 15; no `project_first`; untruncated `QPoly` |
| 2. Counts | 132 / 38 / **94** / 17 records | complement rebuilt; 17 is empty plus 16 surviving singletons, not quotient dimension |
| 3. Flag and 94 solves | S, S^{-1}, permutation, original FIRST | H12 flag artifacts byte-identical to H10T/H11; constant plus all 94 directions replay; omission fixture at free 6, position 0 |
| 4. P12 substitution | 2893 terms, unique NF, omission, orientation | scanned 2893; NF support only in the 94; no q-dependent nonpivot rename; module is commutative |
| 5. Full artifact | 166 records, deg 1 / deg 1, support | TSV and local replay confirm SHA `c8a738b6…`; 16 of 94 survive, 78 cancel |
| 6. Q support | `(),q2,...,q14`; q16–q24 vanish after reduction | present in constant solution / affine map / upper N; absent from NF |
| 7. H11 and H6 | empty = H11; q14 class = H6 | byte-identical; H11 correction (94 vs 17 records) is respected |
| 8. Denominator firewall | at most `U^7 V^4 HF^2` and `U^5 V^4 HF^2` | exact maxima; every factor licensed |
| 9. No unsafe Singular qring | Python/E3/`QPoly` only | holds |
| 10. Scope | complete NF modulo original FIRST only | slogans and `P12_FULL_NORMAL_FORM_RESULT.md` keep the firewall |

---

## 1. Charge 1 — frozen manifests, four evidence versions, dual R3, V1/R1/R2 classification

Recomputed SHA-256 of the required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `P12_FULL_NORMAL_FORM_RESULT.md` | `7004c6359eba808c6f5f66ddd0b72c917fc734c1c3a6eea67878d19859ba23ef` | producer result |
| `P12_FULL_NORMAL_FORM_EVIDENCE.sha256` | `c4fc67a51ebabe84576c89868e26eee4c0514f05f09bae48b0ae43268f9cc253` | evidence manifest |
| `P12_FULL_NORMAL_FORM_FREEZE.sha256` | `c7a146ee89ced521cb23544be6a977413c003b17d0a256a26eda6dae9d435a11` | freeze |
| `PREREGISTRATION_P12_FULL_NORMAL_FORM.md` | `6203fab8b4b06499c082c3f473a27964de57aa88ab91803bb963e1d9e9143ba7` | preregistration |
| `SOURCE_P12_FULL_NORMAL_FORM.sha256` | `03682023155e2a9e0b0d631865f2e4ea33891f026009714c3c68a5724fb6088a` | source manifest |
| `source_p12_full_normal_form_r3.tar.gz` | `c5ead84f7ce2611ad90fcc76ac90dd27750ed17882a111e13b83bf95faf29551` | R3 source archive |
| R3 client `replay_v89h12_allq_p12_full_normal_form.py` | `1e277481267a78472737e9d5082433e41d0218fd1ea6b0a1f92fcc0df9592bed` | controlling replay |
| H11 free-count erratum `P12_FLAG_FREE_COUNT_ERRATUM.md` | `c6bc9942ec60b90433f6044d299cce6e2f4e49ffd237d3680d118b73c39babd2` | 94-versus-17 wording |
| H11 corrective review `xmodel/td6-v89h11-free-count-correction-hostile-review-report-20260826.md` | `4fd55fa316106a4b88ce0fc115b6c4beb92f51997f5896d4ffc3960b334726fa` | controlling H11 correction |

Nested compiler pins reached from the frozen H12 client, independently rehashed:

| Pin | SHA-256 |
|---|---|
| H11 parent client | `8b87985d2071c40b295e280fce94a6465826dd06478089adca34e70df123fcba` |
| H10T parent client | `9c7a5eeede117568aa76d4c26bae11f6e78640313cad6ad559b414ee2cf5098c` |
| H10 v1 parent | `4ff99ca9b7d8539aa369b65a953da63dc731d12ba3faf4184678fe8d0b6b9524` |
| H6 parent client | `1301a09f0497abac5197de6b4afc0eba54b5c8de2b05d2cf11db63fab454d757` |
| H5 parent client | `a81c358b58f8b97ec0dfd97128d0f9539782eda70e66a6747a4c2827a1539b9b` |
| V87 parent client | `7c0890abbce996a221f9389372fa3705742d6ecd72531891bfeb5dfc2f1b9463` |
| V86 parent client | `5b160a2bd18434e6142c33be6775e0c212c22ebc67a52d08b246dd0223decd7c` |
| V85 parent client | `ab9753073d694242d4359dc1edc86774724f62d28d15b7c671ba0b796262100e` |
| H7 `H7_RESULT.md` | `49b9dcba0bb5956dfdbb10293b7bdf3e440a39b127929089c2402ffb06db32cd` |
| payload shard `replay_shard.py` | `a4ccd5d81101fdb82ed2f61571c258e2054961d161f4a98461b8f8614d3fd85e` |
| `PAYLOAD_CLOSURE.sha256` | `cbe7e0be9d49f5aa994790332e2fe0368c32780eac81ee3ddededdf7bb3d5cff` |
| wrapper `run_v89h12_allq_p12_full_normal_form.sh` | `e978cf19a2ade7568642d658fbf7aa050fad50865b0617e8383f30ca85ea6c28` |
| host launcher | `49e45b06b5e115063d12829986778b98e126c78178b07408b7fb55e71b6feb63` |
| parent `P12_FLAG_RESULT.md` | `1e418dfeaf600def4cbfaae885b860b5303faa90a2fdaea59fc4003a137fa2a2` |
| parent `P12_FLAG_FREEZE.sha256` | `f4a314481c0de486843b55b2f3fd6d433534e6cfc6c137b242df363f0a784a0d` |
| parent `FLAG_RESULT.md` | `612b57bcfc20228152d37e5acef08ea41539481be99dff5878af8a790e4c6d1f` |
| parent `FLAG_FREEZE.sha256` | `a156f8394a2966effb006cdfdbb7e64a7da5cefa6e586022a67d29776167d2d9` |

`source_p12_full_normal_form_r3.tar.gz` contains 238 members, including AppleDouble `._*` metadata files, and zero bytecode. Every charged `SOURCE_P12_FULL_NORMAL_FORM.sha256`, `SOURCE_P12_FLAG.sha256`, and `PAYLOAD_CLOSURE.sha256` path is present as `source/<path>` and hash-correct.

Box02 (`ip-172-30-0-186`, tag `td6_v89h12_allq_p12_full_normal_form_box02_20260826T210600Z`) and r6d (`ip-172-30-0-45`, tag `…r6d_20260826T210600Z`) are distinct hosts with the same archive `c5ead84f…`. Both R3 `rc` files are the single byte-string `0\n` (SHA `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`). Mathematical stdout SHA `6ab1403c06dc6985bde2a0860f2a0092a6abe0140cea9fa0005aea9b01a2553e` is byte-identical. All thirteen mathematical output files are byte-identical:

| Output | SHA-256 |
|---|---|
| `ALLQ_AFFINE_PIVOT_MAP.tsv` | `cc31df859f8142c00ed7da8858f9c1d4f8a19bc4a0cfe1ee27511a245987bb27` |
| `ALLQ_P12_FULL_NORMAL_FORM.tsv` | `c8a738b6024ac02e56455674efa8c89c37684a87e0312141a5ca4259ca02e4c4` |
| `ALLQ_P12_FULL_NORMAL_FORM_DENOMINATORS.tsv` | `1ace2f9d73e63546b9ab5d15e12c61901b04e8819a46c9aa907a5df593090bd0` |
| `ALLQ_P12_FULL_NORMAL_FORM_RESULT.txt` | `1f843be94ebe5a5675bc0a1292a209b3773bbfe490ccd0ee249524ec2395a3c4` |
| `ALLQ_P12_PURE_Q14_CLASS.tsv` | `56ebf08a3f9814f714920a4fcb3ae7fb0957db0c0f6d231382f9b5efbf3321a2` |
| `H11_COMMON_FLAG_TELEMETRY.tsv` | `89db0510983c95cd5c8b62e6a04ab3675939c62f1f5c2605d9add475cdad12c2` |
| `H11_FLAG_DENOMINATORS.tsv` | `5ebfa2b9d693974a21ae0622bf5e5f1aa701e3b2c802952d56d678c6278b8956` |
| `H11_SCC_FLAG_BASIS.tsv` | `05f9b3df78dc4abcf6ad39c36e1b48c54529b351459664cccfa3cd59d49d1542` |
| `H11_SCC_FLAG_BASIS_INVERSE.tsv` | `30e644c244f65b17cbf9d7a599b60883d1e8c0b1dd6c3fb326c8ae70cda87aac` |
| `H11_STRICT_UPPER_N.tsv` | `946b75e5307941a81696ec68e1ae2fbcb6ce480294cead6076e434d8e819e913` |
| `H11_STRICT_UPPER_ORDER.tsv` | `35e88aa807ba6a4a0e275f946c23e86b0b3e8fa8aa155684103a08ae13cacb6a` |
| `H12_CONSTANT_FIRST_SOLUTION.tsv` | `ea9537bef63e65241978b82b8e08f0653b21751508194725cc9494b798a571a9` |
| `H12_EMPTY_PARAMETER_P12_FUNCTIONAL.tsv` | `530d3c78df4d1dd43a892976aede83bcc6aefd697a40be71a195e83cbc15a7f8` |

The six `H11_*` flag artifacts are additionally byte-identical to frozen V89H10T `ALLQ_*` artifacts under `evidence/flag/box02/output/` and to frozen V89H11 `H11_*` artifacts under `evidence/p12-flag-r1/box02/output/`. Host stderr differs only in `/usr/bin/time` counters (7:31.63 vs 7:26.40; RSS 297032 vs 297336 KiB; both zero swap). `launch.meta`, pids, and finish timestamps differ as they should. Dual-host equality is custody, not the identity.

Independent local replay of the R3 client with the wrapper environment (`TD6_Q_EXPONENT=2`, `TD6_PIVOT_POLICY=ascending`, `TD6_PIVOT_SCOPE=all-staged`, `TD6_Q_SCOPE=q2-q14-q16-q24`, `TD6_F_SPECIALIZATION=exact-C-equals-V2-minus-U3-over-U`, `TD6_NORMAL_FORM_SCOPE=all-94-free-allq`, `AWS_RUN_TAG=td6_v89h12_allq_p12_full_normal_form_review_local`) wrote the same thirteen files with byte-identical contents and printed `all_free_directions_original_FIRST_replay=true` together with the same digests. That replay is the algebraic verification; AWS dual-host identity is not.

### V1 — missing-wrapper-variable pre-algebra launch

Both V1 hosts used archive `68f54cd1dbedc9a9b29eb74b847ef83cf68054dfdc0ff51af62b3e2b19192534` (`source_p12_full_normal_form.tar.gz`), returned `rc=1`, produced empty `output/`, and share stdout SHA `bd818534c1d6029e3d78fde1725d3e0943f8946cead3cc00ce0a588e5dd334ca`. Stderr on both hosts is

```text
File ".../replay_v85tf1_total_f.py", line 32, in <module>
    assert os.environ.get("TD6_Q_EXPONENT") in ("2", "10")
AssertionError
```

User time 0.10s. The V1 run script (`source/run_v89h12_allq_p12_full_normal_form.sh` inside that archive) has no `TD6_Q_EXPONENT` gate. Module initialization of the nested V85 parent therefore fires during `import` of H11, before `main()`, before `build_bands()`, and before any FIRST/P12 construction. `P12_FULL_NORMAL_FORM_V1_LAUNCH_ERRATUM.md` lines 5–15 classify this correctly as deployment-negative evidence that computed no algebra.

### R1 — corrected free-count stop before directional solution / P12 reduction

Both R1 hosts used archive `c1d50ac999d43e4d8d2b60c81a589b64e5c99a0eb17f12c8f382a4d959e6d366` (`source_p12_full_normal_form_r1.tar.gz`), returned `rc=1`, produced empty `output/`, and share stdout SHA `321e1215187c91225f3a49ec542aae92dca9f146b419627bbf1137602f81f309`. Stdout rebuilds literal FIRST/P12 (`literal_P12_parameter_terms=2893`) and then stops. Stderr on both hosts is

```text
File ".../replay_v89h12_allq_p12_full_normal_form.py", line 171, in main
    assert len(free_variables) == 17
AssertionError
```

The R1 client (SHA `c4c16d43e1dc544d17b3fd4087532f00eaccde4889b716d1738ee51b49e0963e`) differs from the R3 client by the two assertions at lines 168–175: R1 demands 17 nonpivots; R3 demands `all_variables == set(range(132))` and `len(free_variables) == 94`. R1 stdout contains no `triangular_solve=` line and no P12 substitution progress. Wall time ~1:54. `P12_FULL_NORMAL_FORM_R1_COUNT_ERRATUM.md` lines 5–20 classify this correctly as a fail-closed structural diagnostic that solved no direction and computed no new P12 normal form.

### R2 — filename-case packaging failure before import

Both R2 hosts used archive `c54ee26ff2d325913388a406f781532d54c424b9c974b97367d78f0b13bcfd94` (`source_p12_full_normal_form_r2.tar.gz`), returned `rc=127`, produced empty stdout (SHA `e3b0c442…`, empty file) and empty `output/`. Stderr on both hosts is

```text
bash: run_v89h12_allq_p12_full_normal_form.sh: No such file or directory
```

The R2 tarball contains `source/run_v89h12_allq_p12_full_normal_FORM.sh` and does not contain the registered lowercase basename. The script *contents* are byte-identical to the R3 wrapper (SHA `e978cf19…`), and the R2 client is byte-identical to the R3 client (SHA `1e277481…`). Linux is case-sensitive; the packaging host was not. Wall time 0.00s. `P12_FULL_NORMAL_FORM_R2_PACKAGING_ERRATUM.md` lines 5–22 classify this correctly as deployment-negative evidence with no mathematical interpretation.

Only R3 supports mathematics.

---

## 2. Charge 2 — 22 coordinates, q15 shear, `F=0`, `D(U*H*B3)`, 38 FIRST, 2,893 P12 terms

V87 `Q_EXPONENTS = tuple(list(range(2, 15)) + list(range(16, 25)))` (`replay_v87tfaq_total_f_allq.py` lines 32–34) has length 22 and does not contain 15. H11 `ALL_Q` is the same tuple (H11 lines 39, 286–287); H12 uses `ALL_Q = h11.ALL_Q` (H12 line 34) and prints `retained_q_exponents=2,3,...,14,16,...,24`. Wrapper `TD6_Q_SCOPE=q2-q14-q16-q24` matches.

`QPoly` is an untruncated sparse ring on that set (class docstring line 41: “with no degree cutoff”). The constructor (lines 52–54) refuses any exponent outside `Q_ORDER`. Multiplication (lines 93–107) concatenates monomials with no degree bound. `inverse` (lines 111–118) fail-closes unless the support is the empty q-monomial.

Why q15 is a reviewed target shear and not a silently omitted source modulus:

- f-transport is built from `{15: 1}` at degree 15 (`replay_v87tfaq_total_f_allq.py` lines 317–320): frozen `p=t^{15}`.
- g-transport is built from `{1: 1, 25: 1}` only (lines 321–324): frozen `q=t+\cdots+t^{25}`.
- Holding the degree-15 coefficient of `q` at zero is the reviewed target shear. The H12 client inherits H11’s asserts `seen[exponent]==1` for every licensed exponent and `events==2` with `len(first)==38` (H12 lines 146–148).

Genuine FIRST is `qd.pack("X-2", qd.first_band_polynomials(f1,g1))` (`compile_first`, V87 lines 250–257). Genuine P12 is the inlined degree-12 raw CURRENT formula `compile_current_degree12` (V87 lines 260–310), not staged CURRENT/PREVIOUS/POLE. H12 rebuilds both live (lines 143–145) and prints `literal_P12_parameter_terms=2893`. H12 does **not** call H5 `project_first` / `project_value`, so q2 through q13 are not specialized to zero before the solve. Local replay printed the same 2,893 and `literal_P12_parameter_degree_at_most_two=true`. H12 line 151 asserts `max(map(len, p12), default=0) <= 2`.

Exact `F=0` is the two-sided chart `SPECIAL_C = (Rat3(V)**2 - Rat3(U)**3) / Rat3(U)` on `D(U)` (`replay_v85tf1_total_f.py` lines 44–47). `F = C*U - V**2 + U**3`. Substituting the chart into `F` is identically zero. On that chart `H = C-3U^2` pulls back to `(V^2-4U^3)/U` and `B3=V^4`, so the registered radical of `U*H*B3` is generated by `U`, `V`, and `V^2-4U^3`. H12 applies `h6.specialize_first` / `h6.specialize_polynomial` (lines 160–161), which coefficientwise replace every E3 scalar coordinate by that chart (`replay_v89h6_q14_mod_f_cokernel.py` lines 30–59; `specialize_e3` at V85 lines 171–176). Before specialization it demands the raw common denominator of P12 and the 38 original sources (H12 lines 152–153):

```text
assert raw_common == U*H and raw_common.gcd(F).total_degree() == 0
```

Stdout records `raw_source_common_denominator=(C*U - 3*U^3)`, which is `U*H`. `U` does not divide `F` in `Q[C,V,U]`. `H=C-3U^2` does not divide `F`. The asserted coprimeness is correct.

No numeric q assignment occurs. H6’s unused `PRIME = 1000003` / `BASE_C, BASE_V, BASE_U` constants are not referenced by H12’s specialize/solve path. No licensed exponent is dropped from `ALL_Q`. No q-degree cap is present in `QPoly`.

---

## 3. Charge 3 — 132 transported-kernel coordinates, 38 pivots, **94** quotient coordinates, 17 nonzero parameter records

V87 `build_bands` (`replay_v87tfaq_total_f_allq.py` lines 337–341) asserts `len(pivots) == 3470` transport pivots and `len(free) == 132` remaining section coordinates. H12 line 171 asserts that the union of variables appearing in specialized FIRST and specialized P12 is exactly `set(range(132))`.

The frozen FIRST pivot list, printed by both AWS R3 and the local replay, is

```text
0,2,1,3,4,5,7,10,14,19,23,26,28,29,30,31,32,33,34,35,39,42,46,52,
57,63,71,78,86,95,103,110,116,121,125,128,130,131
```

That is 38 distinct labels (`replay_v89h12_allq_p12_full_normal_form.py` lines 162–170). The complementary set in `{0,...,131}` is independently rebuilt as

```text
6,8,9,11,12,13,15,16,17,18,20,21,22,24,25,27,36,37,38,40,41,43,
44,45,47,48,49,50,51,53,54,55,56,58,59,60,61,62,64,65,66,67,68,
69,70,72,73,74,75,76,77,79,80,81,82,83,84,85,87,88,89,90,91,
92,93,94,96,97,98,99,100,101,102,104,105,106,107,108,109,111,
112,113,114,115,117,118,119,120,122,123,124,126,127,129
```

This equals the producer free list in `P12_FULL_NORMAL_FORM_RESULT.md` lines 25–31, the `free_variables=` line of `ALLQ_P12_FULL_NORMAL_FORM_RESULT.txt`, and stdout. Cardinality 94. Intersection with the pivot set is empty. Union is `{0,...,131}`.

The number 17 is the number of distinct parameter monomials in `ALLQ_P12_FULL_NORMAL_FORM.tsv`: the empty monomial together with the 16 singletons `(6,)…(27,)` listed in Charge 6. It is not `dim(n)`. `P12_FULL_NORMAL_FORM_RESULT.md` lines 54–55 state this split explicitly. The R3 client never asserts 17 as a free count (lines 170–172 assert 38, 132, and 94). The H11 free-count erratum (`P12_FLAG_FREE_COUNT_ERRATUM.md` lines 5–9) and the H11 corrective review (SHA `4fd55fa3…`) are incorporated: H11 computed the empty-nonpivot coefficient over all 94 nonpivots set to zero, and its algebra does not change.

Any reading of 17 as quotient dimension would be a material failure. No such reading is present in the R3 result, preregistration (lines 51–55), result artifact, or client.

---

## 4. Charge 4 — common flag, triangular recursion, 94 direction solutions, omission fixture

H12 rebuilds `N = A(0)^{-1} A(q) - I` from the specialized 38-by-38 pivot block (lines 178–197) and demands the frozen digest `38fb14e38daa36d597cc7ae1cd2bd5dd402ef2cd1587337321b8c204eeeb7f36` together with `(532, 6069, 1)` nonzero entries / q-terms / total q-degree. That is the V89H10T relative matrix.

`h11.reconstruct_flag` (H11 lines 111–221), called at H12 line 201, repeats the H10T construction:

1. Extract the 13 coefficient matrices of `q2,...,q14` on the 14-node SCC block `range(14)`.
2. Build a constant common invariant flag by successive 1-dimensional common kernels on the quotients of dimensions 14 down to 1. Telemetry (`H11_COMMON_FLAG_TELEMETRY.tsv`) records `common_kernel_dimension=1` at every step.
3. The emitted constant basis `S` and `S^{-1}` are two-sided inverses (H11 lines 154–155).
4. Extend `S` by the identity on the remaining 24 coordinates. Conjugate the *full* all-22-q matrix `N` as `S^{-1} N S` (column convention). Topological order of that conjugated graph (`H11_STRICT_UPPER_ORDER.tsv`) is

```text
14,15,...,36, 0, 37, 1,2,...,13
```

5. The permuted matrix is strictly upper: the TSV has 2,989 q-coefficient terms, 0 on or below the diagonal, 2,989 strictly above. Independently parsed support is exactly `q2,...,q14,q16,...,q24` and does not include `q15`. Total q-degree one, no mixed-q terms.

The six reconstructed files are byte-identical to the frozen V89H10T and V89H11 artifacts and match the H11 custody digests hardcoded at H11 lines 40–46. H12 additionally asserts `W inverse_W = inverse_W W = I` (lines 202–208), where `W[i][j] = S_full[i][order[j]]` and `inverse_W[i][j] = inverse_S_full[order[i]][j]`.

Orientation of the solve. `topological_order` (`replay_v89h5_q14_high_unimodular_total_f_v1.py` lines 278–293) treats `i → j` when `N[i][j] ≠ 0`, i.e. when row `i` of `(I+N)x = b` depends on coordinate `j`. The resulting order places every such `j` after `i`. `solve_upper_labeled` (H12 lines 56–75) walks rows from 37 down to 0, subtracting already-computed later columns, and never divides: the diagonal of `I+upper_N` is 1. It then asserts `(I+upper_N) * solution = rhs` by exact `QPoly` equality.

The flag/permutation change of *pivot* coordinates is inverted before returning to original coordinates:

```text
base_rhs = A0^{-1} * right_side
triangular_rhs = W^{-1} * base_rhs
(I+upper_N) * triangular_solution = triangular_rhs
pivot_solution = W * triangular_solution
```

(H12 lines 210–214). For the constant right-hand side, H12 line 217 asserts `A * constant_solution == rhs` in the original pivot coordinates. The constant-solution file is byte-identical to frozen H11 `ALLQ_ZERO_NONPIVOT_FIRST_SOLUTION.tsv` (SHA `ea9537be…`; 37 nonzero entries, 219 q terms, max q-degree 1, live support all 22 licensed q). Pivot variable 29 (position 13) is the unique zero coordinate of that solution.

For every one of the 94 free variables, H12 lines 231–238 solve `A p = -D e_j` and assert `A p + D e_j = 0` entry by entry in `E3[q]^{38}`. Local replay printed 94 `triangular_solve=free_*` lines, all with `max_q_degree=0`, then `all_free_directions_original_FIRST_replay=true`. AWS R3 stdout is the same. Every free-direction response is therefore q-independent; the constant solution is q-linear. That is a computed fact, not an imposed specialization.

The pivot-direction omission fixture (H12 lines 240–259) zeros one nonzero component of one direction solution and checks that original FIRST fails. Both AWS R3 and the local replay printed

```text
pivot_direction_omission_fixture_free=6;pivot_position=0
pivot_direction_omission_negative_control=true
```

Zeroing position 0 of the `free_6` direction is a genuine failing control: `A * omitted ≠ -D e_6`. It is not a tautology.

`S` has no q support (constant E3 matrix). The permutation is constant. Nonpivot coordinates are not renamed. This is a q-independent change of the 38 pivot coordinates only.

The complete affine pivot map has 1,223 records (SHA `cc31df85…`). Constant pieces carry q-support `(),q2,...,q14,q16,...,q24` and q-degree at most one. Direction pieces are 94 singleton parameter monomials, each with q-support `{()}` only. All 94 free labels appear. Pivot 29 is identically the zero function (absent from the sparse TSV, consistent with the zero constant coordinate and q-independent directions); that is a vanishing, not an omitted licensed pivot.

---

## 5. Charge 5 — complete substitution into literal P12, uniqueness, omission, orientation

Images of jet parameters (H12 lines 283–296):

- each of the 94 nonpivots maps to `{(variable,): QPoly(1)}` — the identity, with no q factor;
- each of the 38 pivots maps to the corresponding affine polynomial `constant(q) + sum_j y_j * direction_j`, with `direction_j` q-independent.

There is no q-dependent renaming of nonpivots. The substitution cannot smuggle a q-dependent change of quotient coordinates into the remainder.

`affine_substitute` (H12 lines 100–123) walks `sorted(polynomial.items())` of specialized P12. For each of the 2,893 parameter monomials it composes the images by `v87.multiply` (concatenation of parameter monomials, no degree cap) and accumulates with `v87.add`. Progress lines fire every 100 terms. Local and AWS R3 both scanned through 2,800 and then printed `full_normal_form_parameter_terms=17` after the final terms; H12 line 299 asserts `scanned == len(specialized_p12)`. Intermediate `normal_form_parameter_terms` peaked at 1,207 and fell to 17: quadratic and most linear contributions cancel rather than being truncated.

H12 line 300 asserts every surviving parameter monomial is supported on the 94-element free set. Line 302 asserts parameter degree at most two (P12 is quadratic); the emitted degree is one, so every quadratic remainder cancelled. With unimodular `A` over the localized ring, the 38 original FIRST generators are equivalent to `p_j - f_j(y)` with `f_j` affine in the 94 nonpivots. Those are a Groebner basis for any monomial order `p > y`, so the remainder in the free variables is unique. E3 and the coefficient ring are commutative; there is no left/right module ambiguity. The same affine space is cut out if one prefers the language of a rank-38 module of linear relations.

The P12 omission fixture (H12 lines 120–122) subtracts the first nonzero substituted contribution from the accumulated normal form and asserts inequality. In a cancellative abelian group this is equivalent to that contribution being nonzero, which is already required by `assert first_nonzero_contribution`. It is weaker than the pivot-direction fixture, which actually breaks original FIRST. Combined with `scanned == 2893` and the independently hashed 166-record output, it still witnesses that a genuine nonzero P12 contribution entered the sum and that dropping it changes the polynomial. It does not claim that every one of the 2,893 source terms is load-bearing after substitution (many substitute to zero or cancel). Not a material failure of the NF identity.

---

## 6. Charge 6 — full artifact SHA `c8a738b6…`: 166 records, degrees, parameter support

Independently hashed `ALLQ_P12_FULL_NORMAL_FORM.tsv` is `c8a738b6024ac02e56455674efa8c89c37684a87e0312141a5ca4259ca02e4c4`. Header `parameter_monomial	q_monomial	coefficient_exact`. Data rows: 166. Local replay emitted the same bytes.

Parsed support:

| Quantity | Value |
|---|---|
| records | 166 |
| distinct parameter monomials | 17 |
| parameter degrees | `{0,1}` |
| distinct q monomials | 14 |
| q degrees | `{0,1}` |
| mixed-q monomials (two distinct q exponents) | none |
| records with `q_e * y_j` | 153 |

Parameter support is exactly

```text
(), (6,), (8,), (9,), (11,), (12,), (13,), (15,), (16,),
(17,), (18,), (20,), (21,), (22,), (24,), (25,), (27,)
```

Those 16 singleton labels are a subset of the 94 nonpivots. The complementary 78 nonpivots — `36,37,38,40,...,129` — do not appear. They cancelled. This is not a 17-dimensional quotient: the quotient has 94 coordinates, of which 16 have nonzero P12 remainder.

`e3_exact` writes an 18-tuple (the ambient E3 rank). Vanishing of an E3-valued polynomial is therefore 18 scalar equations in ambient coordinates. Independently, only E3 coordinates 0 through 7 are ever nonzero in this particular NF (coordinates 8–17 are identically zero; linear-in-`y` terms live only in coordinates 0 and 1). That is a strengthening, not a contradiction: the producer counts the ambient E3 rank, which is 18, and correctly says the remaining problem involves 16 effective quotient variables. It does not treat 17, or 18, as quotient dimension.

Empty-parameter records in the NF (13 rows) equal the body of `H12_EMPTY_PARAMETER_P12_FUNCTIONAL.tsv` after dropping the parameter column.

---

## 7. Charge 7 — q support `(),q2,...,q14`; q16–q24 vanished after reduction; separate-degree statement

NF q-support, independently parsed, is exactly

```text
(), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,), (11,), (12,), (13,), (14,)
```

No `q15`. No `q16,...,q24`. No mixed-q monomial.

Those high-q coordinates were not omitted from the source computation:

- constant FIRST solution live q-exponents are exactly `{2,...,14,16,...,24}` (219 terms; SHA `ea9537be…`);
- affine-map constant pieces have the same 22-q support;
- strict-upper `N` has 2,989 terms whose q-support is the same 22 exponents, including `q16` and `q24`.

They vanish after the complete 2,893-term P12 reduction. Empty-parameter q-support is `(),q3,...,q14` (no `q2`); overall NF q-support includes `q2` from the surviving quotient variables `(24,)` and `(27,)`. Absence of `q2` from the empty coefficient and of `q16,...,q24` from the whole NF is vanishing, not a cutoff.

Separate-degree statement. Parameter degree is one and q degree is one, but 153 records are products `q_e * y_j`. `P12_FULL_NORMAL_FORM_RESULT.md` lines 66–68 state that the NF is separately affine in the 16 surviving quotient variables and in q, and that this is not a claim of joint total degree one. The R3 result artifact prints `full_normal_form_parameter_degree=1` and `full_normal_form_max_total_q_degree=1` as separate facts. No joint total-degree-one slogan is present.

---

## 8. Charge 8 — empty-parameter coefficient = H11; pure-q14 class = V89H6; H11 correction

`H12_EMPTY_PARAMETER_P12_FUNCTIONAL.tsv` SHA `530d3c78df4d1dd43a892976aede83bcc6aefd697a40be71a195e83cbc15a7f8` is byte-identical to frozen V89H11 `ALLQ_EMPTY_PARAMETER_P12_FUNCTIONAL.tsv`. H12 lines 321–328 recompute the empty-nonpivot value by H11’s `empty_parameter_value` (which zeros every monomial containing a non-pivot, over the complete 38-pivot dictionary, not over 17 labels) and assert equality with `normal_form[()]`.

`ALLQ_P12_PURE_Q14_CLASS.tsv` SHA `56ebf08a3f9814f714920a4fcb3ae7fb0957db0c0f6d231382f9b5efbf3321a2` is byte-identical to frozen V89H6 `Q14_MOD_F_POSITIVE_COKERNEL_CLASS.tsv` at `cases/td6_c1_c2_c3_q14_mod_f_cokernel_v89h6_aws_20260826/evidence/r1/box02/output/`. It has 17 rows, q-monomial exactly `(14,)`, and the same 17 parameter monomials as the full NF. H12 lines 331–341 extract the `(14,)` coefficient of every NF parameter monomial that has one.

The H11 correction is respected: 94 quotient variables versus 17 nonzero q14 records. The 17-record q14 class is a coefficient slice of the 94-variable remainder, not a 17-dimensional quotient.

---

## 9. Charge 9 — denominator ledger SHA `1ace2f9d…`

Ledger file SHA `1ace2f9d73e63546b9ab5d15e12c61901b04e8819a46c9aa907a5df593090bd0` matches. Contents:

```text
label                    value_count  allowed  common                          factorization
affine_pivot_map         1223         true     V^8*U^7 - 8*V^6*U^10 + 16*V^4*U^13   (1, [(V^2-4U^3, 2), (V, 4), (U, 7)])
full_P12_normal_form     166          true     V^8*U^5 - 8*V^6*U^8 + 16*V^4*U^11    (1, [(V^2-4U^3, 2), (V, 4), (U, 5)])
```

Independent flint factorization in `Q[V,U]`:

- claimed affine common equals `U^7 V^4 (V^2-4U^3)^2` exactly (content 1, remainder 0);
- claimed NF common equals `U^5 V^4 (V^2-4U^3)^2` exactly;
- every one of 63 distinct affine scalar denominators (22,014 E3 slots) factors as `U^a V^b (V^2-4U^3)^c` with `a ≤ 7`, `b ≤ 4`, `c ≤ 2`, and no other monic factor;
- every one of 31 distinct NF scalar denominators (2,988 E3 slots) factors as `U^a V^b (V^2-4U^3)^c` with `a ≤ 5`, `b ≤ 4`, `c ≤ 2`, and no other monic factor.

Worst-case exponents attain the charged maxima. `denominator_record` (`replay_v89h10t_allq_simultaneous_triangular_flag.py` lines 166–171) takes the monic LCM of scalar denominators and admits a record only if every monic factor lies in `{U, V, V^2-4U^3}`. On `F=0` that is exactly the pullback of the registered radical of `U*H*B3`. No determinant formula is used: `A(0)^{-1}` is Gaussian elimination with a two-sided E3 inverse check (`inverse_constant_matrix`, H5 lines 199–228). `QPoly.inverse` refuses any nonconstant-q element. Flag `S^{-1}` is likewise a constant Gaussian inverse. No unregistered inverse is emitted.

S and `S^{-1}` denominators remain the frozen H10T ledger (`H11_FLAG_DENOMINATORS.tsv`, SHA `5ebfa2b9…`): `U^4 V^4 HF^2` and `U^5 V^4 HF` respectively, both inside the same radical.

---

## 10. Charge 10 — Python/custom exact arithmetic, no unsafe Singular qring

The R3 client and every nested parent are Python. Coefficient arithmetic is `E3` / `Rat3` / `QPoly`. Polynomial addition and multiplication are sparse dicts (`v86.add`, `v87.multiply`). Matrix inversion is Gaussian elimination over E3. The triangular solve subtracts already-computed later columns and never divides by a q polynomial. Flint appears in the producer only as factorization of already-computed `Q[U,V]` denominator LCMs (`v85.factor_list` / `.factor()`), which is ordinary polynomial factorization, not a qring membership test.

No file in the H12 client chain calls Singular, `qring`, `subst` as a Singular command, or `diff` as a Singular command. H12’s only “subst” is the Python function `affine_substitute`. Sage, Lean, and `jc2-lean` are not used. Local replay imported `flint` solely because V85 prints `python_flint_version` through the nested payload; the AWS wrapper’s `import flint` line is a runtime pin, not an algebra engine for the NF.

---

## 11. Charge 11 — scope firewall

`P12_FULL_NORMAL_FORM_RESULT.md` lines 109–117, preregistration lines 45–49, and `ALLQ_P12_FULL_NORMAL_FORM_RESULT.txt` all state:

```text
unit_ideal_claim=false
source_point_claim=false
whole_TD6_killed=false
JC2_resolved=false
```

A pass proves only the complete canonical P12 normal form modulo the original FIRST module in this exact `F=0`, all-22-q scope. It does not prove that the resulting 18 ambient E3 scalar equations have no common zero, prove a unit ideal or source-point exclusion, cover a projective q chart, license q15 as a source coordinate, supply a total-Rees/source map, close TD6, or resolve JC2. The reduction slogan “18 scalar equations involving only 16 effective quotient variables and q2,...,q14” (`P12_FULL_NORMAL_FORM_RESULT.md` lines 77–79) is a description of the remainder problem, not a common-zero verdict. Equivalently: P12 takes values in 18-dimensional E3, FIRST has been eliminated, and 16 of 94 quotient variables remain visible.

---

## Independent local replay

Command: R3 client `replay_v89h12_allq_p12_full_normal_form.py` under the registered wrapper environment, output directory `/tmp/td6_v89h12_review_recompute`. Exit 0 in 221s. All thirteen mathematical artifacts byte-identical to AWS R3 Box02 and r6d. Printed `TD6-V89H12-ALLQ-P12-FULL-NORMAL-FORM PASS` is custody; the identities above are the algebra.

---

## Observations that are not material failures

1. Pivot variable 29 (FIRST pivot position 13) is the zero function on the whole affine FIRST space. The constant solution has 37 nonzero entries; all 94 direction solutions vanish at that coordinate. The sparse affine-map TSV therefore has 37 positions, not 38. This is a vanishing, recorded by omission of zero rows, not a dropped licensed pivot.
2. The P12 omission fixture is a cancellative-group check that the first nonzero substituted contribution is nonzero. The pivot-direction fixture is the genuine failing control.
3. Only E3 coordinates 0–7 of this NF are nonzero (linear-in-`y` terms only in 0 and 1). The producer’s “18 scalar equations” counts ambient E3 rank, not the number of nontrivial coordinate functions. It does not treat 18, or 17, as quotient dimension.

---

## Verdict

**CONFIRMED.**
