# Hostile review — TD6 V89H11 all-q literal-P12 flag functional

| Field | Value |
|---|---|
| Target | Frozen producer package `cases/td6_c1_c2_c3_allq_mod_f_unitriangular_functional_v89h10_aws_20260826/`; controlling pins `P12_FLAG_RESULT.md`, `P12_FLAG_EVIDENCE.sha256`, `P12_FLAG_FREEZE.sha256`, `PREREGISTRATION_P12_FLAG.md`, `SOURCE_P12_FLAG.sha256`, `source_p12_flag_r1.tar.gz`, R1 client, parent `FLAG_RESULT.md` / `FLAG_FREEZE.sha256` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest bad coefficient / denominator / omission | none |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile algebra review. Producer `PASS` banners, dual-host byte identity, and RSS/elapsed lines are custody only |
| Method | SHA-256 of every charged pin and every consumed manifest row; independent local replay of the R1 client into `/tmp/td6_v89h11_review_recompute` (exit 0, 121s) producing byte-identical copies of all ten mathematical artifacts; flint factorization in `Q[V,U]` of every functional and pivot denominator; source review of V87 reconstruction, H5 constant inversion, H6 `F=0` chart, H10T flag, and the H11 triangular solve / P12 substitution. No Singular, Sage, Lean, or `jc2-lean`. The AWS wrapper was not re-run (EC2/Linux gated); the Python client was |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Prompt SHA-256 `e7b13084ae539bbf13cef69424afe67ba3854b815e08f986a78199a0d5271006` matched. Independently recomputed SHA-256 of every required primary pin matches. Every path named in `P12_FLAG_FREEZE.sha256` (11/11), `P12_FLAG_EVIDENCE.sha256` (48/48), `SOURCE_P12_FLAG.sha256` (25/25), `FLAG_FREEZE.sha256` (11/11), and `PAYLOAD_CLOSURE.sha256` (56/56) rehashes to the printed digest. Every `SOURCE_P12_FLAG.sha256` row exists at the case root and as `source/<path>` inside `source_p12_flag_r1.tar.gz`, and both copies match. All 56 payload-closure files exist inside the same tarball and on disk and match. Nested compiler hash pins consumed from that archive also match. Producer `TD6-V89H11-ALLQ-P12-FLAG-FUNCTIONAL PASS` was not used as algebra. V1 is a deployment-negative launch (`rc=1`, `t.Rat3` attribute-path error during module initialization, no algebraic construction) and is not used as mathematical evidence. No file other than this review was written. The frozen producer package, campaign ledgers, and `jc2-lean` were not edited.

---

## Verdict

**CONFIRMED.**

On the frozen V89H10T `F=0` specialization over the registered open `D(U*H*B3)`, the R1 client rebuilds genuine literal P12 (2,893 parameter terms) and all 38 original packed FIRST rows, retains the 22 independent untruncated coordinates `q2,...,q14,q16,...,q24`, and omits q15 only as the reviewed target shear of frozen `(p,q)=(t^{15}, t+\cdots+t^{25})`. The raw common source denominator is exactly `U*H=U(C-3U^2)`, coprime to `F`.

The 38 FIRST rows are affine-linear in the jet parameters by construction. Their 38-by-38 pivot block `A(q)` is unimodular over the localized q-polynomial ring because the relative matrix `N=A(0)^{-1}A(q)-I` is strictly upper triangular after a *constant* flag change of pivot basis and a constant permutation, so `I+N` is unipotent. Setting every nonpivot parameter to zero and solving `A(q) p = rhs(q)` by strict-upper back-substitution therefore yields the unique pivot value `p0` of the original FIRST affine space at empty nonpivots. Direct substitution recovers the original right-hand side entry by entry. Substituting that `p0` into literal P12 equals the empty-nonpivot coefficient of the unique original-FIRST normal form. There is no q-dependent change of the 17 nonpivot coordinates, no confusion of row reduction with a different ideal, and no left/right module issue.

The exact pivot solution has 37 nonzero entries, 219 q terms, total q degree one, and digest `ea9537bef63e65241978b82b8e08f0653b21751508194725cc9494b798a571a9`. It carries every licensed q including `q2` and `q16,...,q24`. The empty-parameter P12 functional has digest `530d3c78df4d1dd43a892976aede83bcc6aefd697a40be71a195e83cbc15a7f8`, exactly 13 terms, total q degree one, no mixed-q terms, and support exactly `(), q3, q4, ..., q14`. Absence of `q2` and `q16,...,q24` is vanishing after the full 2,893-term literal substitution, not a cutoff or omitted licensed term. The pure-q14 E3-coordinate-0 value equals the promoted V89H7 functional

```text
N / [V^3 (V^2-4U^3)^2]
```

with the same nonzero `N` and with `gcd(N, den)=1`. Under `q2=...=q13=0` the entire positive-q support is exactly pure q14.

Up to units the output denominators are exactly the charged maxima

```text
pivot solution:             U^7 V^4 (V^2-4U^3)^2
empty-parameter functional: U^5 V^4 (V^2-4U^3)^2
```

Every flint factor of every scalar denominator lies in `{U, V, V^2-4U^3}`. Arithmetic is Python/custom exact E3/`QPoly`; `QPoly.inverse` refuses a nonconstant-q element; the triangular solve never inverts a q polynomial. The theorem is one empty-nonpivot quotient functional only.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Frozen pins | controlling hashes | all nine required pins match |
| 0. Manifests | every named file | `P12_FLAG_FREEZE` 11/11, `P12_FLAG_EVIDENCE` 48/48, `SOURCE_P12_FLAG` 25/25, `FLAG_FREEZE` 11/11, `PAYLOAD_CLOSURE` 56/56; tarball copies match |
| 0. Dual AWS R1 | hosts, archive, rc | distinct Box02 / r6d; archive `51575970…`; both `rc=0`; math artifacts and stdout byte-identical |
| 0. Independent replay | local client | exit 0; all ten output files byte-identical to AWS R1 |
| 0. V1 deployment-negative | not math evidence | both V1 `rc=1`; `t.Rat3` `AttributeError` at import line 35; no algebra; erratum accurate |
| 1. Literal scope | P12 2893 terms, 38 FIRST, 22 q, q15 shear, `F=0` | V87 rebuild; `Q_EXPONENTS` skips 15; no `project_first`; untruncated `QPoly` |
| 2. Flag reconstruction | V89H10T S, order, strict-upper N, back-sub direction | H11 artifacts byte-identical to H10T; orientation is strictly upper; solve from last row |
| 3. `A(q) p = rhs(q)` | original coordinates | asserted by exact `QPoly` equality; independent local replay passed |
| 4. Quotient argument | unimodular affine FIRST, empty-n coefficient of unique NF | holds; constant pivot-basis change only; nonpivots unmoved |
| 5. Pivot solution | 37 nonzero, 219 terms, deg 1, digest `ea9537be…` | TSV and local replay confirm; live support is all 22 q |
| 6. Empty-parameter functional | digest `530d3c78…`, 13 terms, deg 1, support `(),q3..q14` | TSV and local replay confirm; not a truncation |
| 7. Pure q14 coord-0 vs H7 | exact `N/den`, nonzero; tail support exactly q14 | flint identity; `gcd(N,den)=1` |
| 8. Denominator firewall | at most `U^7 V^4 HF^2` and `U^5 V^4 HF^2` | exact maxima; every factor licensed |
| 9. No unsafe Singular qring | Python/E3/`QPoly` only | holds |
| 10. Scope | one empty-nonpivot functional | slogans and `P12_FLAG_RESULT.md` keep the firewall |

---

## 1. Charge 1 — frozen manifests, source archive, dual R1, V1 negative

Recomputed SHA-256 of the required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `P12_FLAG_RESULT.md` | `1e418dfeaf600def4cbfaae885b860b5303faa90a2fdaea59fc4003a137fa2a2` | producer result |
| `P12_FLAG_EVIDENCE.sha256` | `3a01bd8e2fe0b4ae6825c6452021e76e765da5be928398dad902b7706e0f36cb` | evidence manifest |
| `P12_FLAG_FREEZE.sha256` | `f4a314481c0de486843b55b2f3fd6d433534e6cfc6c137b242df363f0a784a0d` | freeze |
| `PREREGISTRATION_P12_FLAG.md` | `5cb871da3a3bf32ae755c5692af92c50d8c983f19b64b88f0da49a35f0be23f8` | preregistration |
| `SOURCE_P12_FLAG.sha256` | `ac37d22986ab4257f95c50eef593865ef90b603cda97886ffe6fda500390eba8` | source manifest |
| `source_p12_flag_r1.tar.gz` | `51575970a5d7ba2cc6056a0a70ecd744d88d571bd9c2995f1a65ba38fdc4f0fa` | R1 source archive |
| R1 client `replay_v89h11_allq_p12_flag_functional.py` | `8b87985d2071c40b295e280fce94a6465826dd06478089adca34e70df123fcba` | controlling replay |
| parent `FLAG_RESULT.md` | `612b57bcfc20228152d37e5acef08ea41539481be99dff5878af8a790e4c6d1f` | V89H10T theorem |
| parent `FLAG_FREEZE.sha256` | `a156f8394a2966effb006cdfdbb7e64a7da5cefa6e586022a67d29776167d2d9` | V89H10T freeze |

Nested compiler pins reached from the frozen H11 client, independently rehashed:

| Pin | SHA-256 |
|---|---|
| H10T parent client | `9c7a5eeede117568aa76d4c26bae11f6e78640313cad6ad559b414ee2cf5098c` |
| H10 parent (H10T's parent) | `4ff99ca9b7d8539aa369b65a953da63dc731d12ba3faf4184678fe8d0b6b9524` |
| H6 parent client | `1301a09f0497abac5197de6b4afc0eba54b5c8de2b05d2cf11db63fab454d757` |
| H5 parent client | `a81c358b58f8b97ec0dfd97128d0f9539782eda70e66a6747a4c2827a1539b9b` |
| V87 parent client | `7c0890abbce996a221f9389372fa3705742d6ecd72531891bfeb5dfc2f1b9463` |
| V86 parent client | `5b160a2bd18434e6142c33be6775e0c212c22ebc67a52d08b246dd0223decd7c` |
| V85 parent client | `ab9753073d694242d4359dc1edc86774724f62d28d15b7c671ba0b796262100e` |
| H7 `H7_RESULT.md` | `49b9dcba0bb5956dfdbb10293b7bdf3e440a39b127929089c2402ffb06db32cd` |
| payload shard `replay_shard.py` | `a4ccd5d81101fdb82ed2f61571c258e2054961d161f4a98461b8f8614d3fd85e` |
| `PAYLOAD_CLOSURE.sha256` | `cbe7e0be9d49f5aa994790332e2fe0368c32780eac81ee3ddededdf7bb3d5cff` |

`source_p12_flag_r1.tar.gz` contains 216 members, including 108 AppleDouble `._*` metadata files, and zero bytecode. Every charged `SOURCE_P12_FLAG.sha256` and `PAYLOAD_CLOSURE.sha256` path is present as `source/<path>` and hash-correct.

Box02 (`ip-172-30-0-186`, tag `td6_v89h11_allq_p12_flag_functional_box02_20260826T203400Z`) and r6d (`ip-172-30-0-45`, tag `…r6d_20260826T203400Z`) are distinct hosts with the same archive `51575970…`. Both R1 `rc` files are the single byte-string `0\n`. Mathematical stdout SHA `5b8bd72496314e97bc80296fdefa07703021bfa40f59ea9040221dc3f2eceeda` is byte-identical. All ten mathematical output files are byte-identical:

| Output | SHA-256 |
|---|---|
| `ALLQ_EMPTY_PARAMETER_P12_FUNCTIONAL.tsv` | `530d3c78df4d1dd43a892976aede83bcc6aefd697a40be71a195e83cbc15a7f8` |
| `ALLQ_P12_FLAG_FUNCTIONAL_RESULT.txt` | `591d6ac5ffe86ffd11a2aea99f94814f4c4ae5cf64a489709e6a99314b132101` |
| `ALLQ_P12_FUNCTIONAL_DENOMINATORS.tsv` | `b4113c145223061669954852fcfa7e5a5a8392fa070135c79e6ee0624c4d9151` |
| `ALLQ_ZERO_NONPIVOT_FIRST_SOLUTION.tsv` | `ea9537bef63e65241978b82b8e08f0653b21751508194725cc9494b798a571a9` |
| `H11_COMMON_FLAG_TELEMETRY.tsv` | `89db0510983c95cd5c8b62e6a04ab3675939c62f1f5c2605d9add475cdad12c2` |
| `H11_FLAG_DENOMINATORS.tsv` | `5ebfa2b9d693974a21ae0622bf5e5f1aa701e3b2c802952d56d678c6278b8956` |
| `H11_SCC_FLAG_BASIS.tsv` | `05f9b3df78dc4abcf6ad39c36e1b48c54529b351459664cccfa3cd59d49d1542` |
| `H11_SCC_FLAG_BASIS_INVERSE.tsv` | `30e644c244f65b17cbf9d7a599b60883d1e8c0b1dd6c3fb326c8ae70cda87aac` |
| `H11_STRICT_UPPER_N.tsv` | `946b75e5307941a81696ec68e1ae2fbcb6ce480294cead6076e434d8e819e913` |
| `H11_STRICT_UPPER_ORDER.tsv` | `35e88aa807ba6a4a0e275f946c23e86b0b3e8fa8aa155684103a08ae13cacb6a` |

The six `H11_*` flag artifacts are additionally byte-identical to the frozen V89H10T `ALLQ_*` artifacts under `evidence/flag/box02/output/`. Host stderr differs only in `/usr/bin/time` counters (4:21.11 vs 4:21.81; RSS 298100 vs 297532 KiB; both zero swap). `launch.meta`, pids, and finish timestamps differ as they should. Dual-host equality is custody, not the identity.

Independent local replay of the R1 client with the wrapper environment (`TD6_Q_EXPONENT=2`, `TD6_PIVOT_POLICY=ascending`, `TD6_PIVOT_SCOPE=all-staged`, `TD6_Q_SCOPE=q2-q14-q16-q24`, `TD6_F_SPECIALIZATION=exact-C-equals-V2-minus-U3-over-U`, `TD6_FUNCTIONAL_SCOPE=empty-parameter-allq`) wrote the same ten files with byte-identical contents and printed `original_FIRST_zero_nonpivot_solution_replay=true` together with the same digests. That replay is the algebraic verification; AWS dual-host identity is not.

V1 (both hosts `rc=1`, archive `c538b4d1237b002133e77a1664368d579d3d714af172637c999e3a415030123a`) failed at import

```text
File ".../replay_v89h11_allq_p12_flag_functional.py", line 35, in <module>
    QPoly, E3, Rat3 = t.QPoly, t.E3, t.Rat3
AttributeError: module 'td6_v89h11_flag_parent' has no attribute 'Rat3'
```

(`evidence/p12-flag-v1/box02/stderr` lines 2–5; r6d the same error at its path). User time 0.45s. V1 stdout is byte-identical across hosts (`c2e4eb1bb1c77fbb3ea6dcdf43202d8fe7537bc70b916340a5bd181ad74688cd`), ends after `PAYLOAD_CLOSURE` checksums, and contains no producer banner and no `PASS`. V1 `output/` is empty. The R1 client differs from the V1 client by the single attribute path `t.Rat3` → `h6.Rat3` (`replay_v89h11_allq_p12_flag_functional.py` line 35). `P12_FLAG_V1_LAUNCH_ERRATUM.md` lines 5–9 classify this correctly as deployment-negative evidence that computed no algebra.

---

## 2. Charge 2 — literal P12, 38 FIRST rows, 22 coordinates, q15 shear, `F=0`

V87 `Q_EXPONENTS = tuple(list(range(2, 15)) + list(range(16, 25)))` (`replay_v87tfaq_total_f_allq.py` lines 32–34) has length 22 and does not contain 15. H11 `ALL_Q` is the same tuple (client lines 39, 286–287). Wrapper `TD6_Q_SCOPE=q2-q14-q16-q24` matches.

`QPoly` is an untruncated sparse ring on that set (class docstring line 41: “with no degree cutoff”). The constructor (lines 52–54) refuses any exponent outside `Q_ORDER`. Multiplication (lines 93–107) concatenates monomials with no degree bound. `inverse` (lines 111–118) fail-closes unless the support is the empty q-monomial.

Why q15 is a reviewed target shear and not a silently omitted source modulus:

- f-transport is built from `{15: 1}` at degree 15 (`replay_v87tfaq_total_f_allq.py` lines 317–320): frozen `p=t^{15}`.
- g-transport is built from `{1: 1, 25: 1}` only (lines 321–324): frozen `q=t+\cdots+t^{25}`.
- Holding the degree-15 coefficient of `q` at zero is the reviewed target shear. The H11 client asserts `seen[exponent]==1` for every licensed exponent and `events==2` with `len(first)==38` (lines 285–287).

Genuine FIRST is `qd.pack("X-2", qd.first_band_polynomials(f1,g1))` (`compile_first`, lines 250–257). Genuine P12 is the inlined degree-12 raw CURRENT formula `compile_current_degree12` (lines 260–310), not staged CURRENT/PREVIOUS/POLE. H11 rebuilds both live (lines 282–284) and prints `literal_P12_parameter_terms=2893`. H11 does **not** call H5 `project_first` / `project_value`, so q2 through q13 are not specialized to zero before the solve.

Exact `F=0` is the two-sided chart `SPECIAL_C = (Rat3(V)**2 - Rat3(U)**3) / Rat3(U)` on `D(U)` (`replay_v85tf1_total_f.py` lines 44–47). `F = C*U - V**2 + U**3`. Substituting the chart into `F` is identically zero. H11 applies `h6.specialize_first` / `h6.specialize_polynomial` (client lines 297–298), which coefficientwise replace every E3 scalar coordinate by that chart (`replay_v89h6_q14_mod_f_cokernel.py` lines 30–59; `specialize_e3` at V85 lines 171–176). Before specialization it demands the raw common denominator of P12 and the 38 original sources (H11 lines 288–291):

```text
assert raw_common == U*H and raw_common.gcd(F).total_degree() == 0
```

Stdout records `raw_source_common_denominator=(C*U - 3*U^3)`, which is `U*H`. `U` does not divide `F` in `Q[C,V,U]`. `H=C-3U^2` does not divide `F`. The asserted coprimeness is correct.

No numeric q assignment occurs. No licensed exponent is dropped from `ALL_Q`. The only q15 appearance in `Q_PRIME` is `Q_PRIME[15] = 16 q16` for exponent 16 (`configure_qd` lines 234–236), which is the standard degree-shift of a licensed high-q coordinate, not a q15 source modulus.

---

## 3. Charge 3 — V89H10T flag, orientation, `A(q)p=rhs(q)`

H11 rebuilds `N = A(0)^{-1} A(q) - I` from the specialized 38-by-38 pivot block (lines 301–316) and demands the frozen digest `38fb14e38daa36d597cc7ae1cd2bd5dd402ef2cd1587337321b8c204eeeb7f36` together with `(532, 6069, 1)` nonzero entries / q-terms / total q-degree. That is the V89H10T relative matrix.

`reconstruct_flag` (lines 111–221) repeats the H10T construction:

1. Extract the 13 coefficient matrices of `q2,...,q14` on the 14-node SCC block `range(14)`.
2. Build a constant common invariant flag by successive 1-dimensional common kernels on the quotients of dimensions 14 down to 1. Telemetry (`H11_COMMON_FLAG_TELEMETRY.tsv`) records `common_kernel_dimension=1` at every step.
3. The emitted constant basis `S` and `S^{-1}` are two-sided inverses (lines 154–155). Both TSV files have 79 nonzero entries, matching `FLAG_RESULT.md` lines 32–33.
4. Extend `S` by the identity on the remaining 24 coordinates. Conjugate the *full* all-22-q matrix `N`. Topological order of that conjugated graph (`H11_STRICT_UPPER_ORDER.tsv`) is

```text
14,15,...,36, 0, 37, 1,2,...,13
```

5. The permuted matrix is strictly upper: the TSV has 2,989 q-coefficient terms, 0 on or below the diagonal, 2,989 strictly above. Independently parsed support includes `q2`, `q14`, `q16`, and `q24`, and does not include `q15`. Total q-degree one, no mixed-q terms.

The six reconstructed files are byte-identical to the frozen V89H10T artifacts and match the H10T custody digests hardcoded at H11 lines 40–46.

Orientation of the solve. `topological_order` (`replay_v89h5_q14_high_unimodular_total_f_v1.py` lines 278–293) treats `i → j` when `N[i][j] ≠ 0`, i.e. when row `i` of `(I+N)x = b` depends on coordinate `j`. The resulting order places every such `j` after `i`. `solve_upper` (H11 lines 224–242) therefore walks rows from 37 down to 0, subtracting already-computed later columns, and never divides: the diagonal of `I+upper_N` is 1. It then asserts `(I+upper_N) * triangular_solution = triangular_rhs` by exact `QPoly` equality.

The flag/permutation change of *pivot* coordinates is inverted before returning to original coordinates:

```text
W[i][j] = S_full[i][order[j]]
inverse_W[i][j] = inverse_S_full[order[i]][j]
```

Both products `W inverse_W` and `inverse_W W` are asserted to be the identity (lines 326–327). Then

```text
base_rhs = A0^{-1} * rhs
triangular_rhs = W^{-1} * base_rhs
(I+upper_N) * triangular_solution = triangular_rhs
pivot_solution = W * triangular_solution
assert A * pivot_solution == rhs
```

(lines 331–335). Algebraically `I+upper_N = P^{-1} S^{-1} (I+N) S P` and `W = S P`, so the last assert is `A p = rhs` in the original pivot coordinates. The independent local replay reached this assert and exited 0 with the frozen pivot digest. That is an entry-by-entry identity in `E3[q]^{38}`, not a residual check.

`S` has no q support (constant E3 matrix). The permutation is constant. This is a q-independent change of the 38 pivot coordinates only.

---

## 4. Charge 4 — key quotient argument

Write `R` for the coefficient ring `E3_D[q_2,...,q_14,q_16,...,q_24]` localized at the registered open `D(U*H*B3)` after `F=0`. Jet parameters split as 38 pivots `p` and 17 nonpivots `n`.

Each FIRST row is stored as an affine-linear polynomial in the jet parameters: `source_polynomial` (`replay_v86tfq2_total_f_q2.py` lines 242–248) emits only the empty monomial `()` and linear monomials `(variable,)`. H11 line 289 asserts `len(monomial) <= 1` on those parameter keys. So the 38 generators are

```text
L_i(p, n) = (A(q) p + B(q) n - rhs(q))_i  ∈  R[p, n],
```

affine-linear, not a Groebner slice of a higher-degree ideal.

Unimodularity of `A` over `R`. `A(0)` is inverted over E3 by Gaussian elimination (`inverse_constant_matrix`, H5 lines 199–228) with a two-sided E3 inverse check. Relative `B = A(0)^{-1} A = I+N`. After a *constant* invertible change of pivot basis and a constant permutation, `N` is strictly upper triangular as a matrix over `R` (2,989 terms, zero on and below the diagonal). Hence `I+N` is unipotent, `det(I+N)=1` as a polynomial in the q variables, and `A^{-1}` lies in `M_{38}(R)`: no nonconstant-q element is inverted. `QPoly.inverse` would refuse any such inversion in any case (V87 lines 111–118). The triangular solve itself divides by nothing.

Unimodular row operations with coefficients in `R` therefore take `{L_i}` to the equivalent generating set

```text
p_j - f_j(n),    f_j affine in n with coefficients in R.
```

These generate the same ideal of `R[p,n]`. With any monomial order `p > n` they are a Groebner basis, so every polynomial has a unique remainder in `R[n]`, obtained by substituting `p = f(n)`. That remainder is the unique original-FIRST normal form. (The same affine space is cut out if one prefers the language of a rank-38 module of linear relations; for a polynomial function such as P12, evaluation on that affine space is well-defined either way. There is no noncommutative left/right module here: E3 and `R` are commutative.)

The empty-nonpivot coefficient of that unique normal form is the constant term of `P12(f(n), n)` as a polynomial in `n`. For any polynomial, that constant term equals `P12(f(0), 0)`. And `f(0)` is the unique solution of `A p = rhs`. Therefore substituting the computed zero-nonpivot pivot solution into literal P12, and killing any remaining monomial that contains a nonpivot, is exactly that coefficient.

This identification would fail if the 17 nonpivot coordinates were replaced by a q-dependent linear combination, because “the empty monomial in the new coordinates” would mix the old constant term with old positive-n terms. That does not happen. The flag matrix `S` and the permutation act on the 38-dimensional *pivot* index space. The 17 nonpivot variables are never renamed. They are simply set to zero. After the triangular solve, `W` maps back to the original pivot coordinates *before* substitution into P12 (`empty_parameter_value`, lines 245–266, using `h5.base_pivot_columns` from line 299).

Row reduction of `A` is not a different operation from ideal reduction in this setting: it is the unimodular `R`-linear change of generators that produces the Groebner basis `p_j - f_j(n)`. Because the inverse is polynomial in q, one does not invert `det A` in `Frac(R)` and thereby change the ideal over `R`.

The implementation computes only `P12(p0, 0)`, not the remaining 17-parameter polynomial `P12(f(n), n) - P12(p0, 0)`. That is the stated theorem, not a hidden full normal form.

---

## 5. Charge 5 — pivot solution

Independent parse of `ALLQ_ZERO_NONPIVOT_FIRST_SOLUTION.tsv` plus the local replay:

| Claim | Observed |
|---|---|
| digest | `ea9537bef63e65241978b82b8e08f0653b21751508194725cc9494b798a571a9` |
| q terms | 219 |
| nonzero entries | 37 of 38; index 13 is identically zero |
| total q degree | 1 |
| mixed-q terms | none |
| q support | `(), q2, q3, ..., q14, q16, ..., q24` (all 22 licensed exponents plus the empty monomial; no q15) |

The live q-support of the pivot solution includes `q2` and `q16,...,q24`. Those coordinates were computed, not dropped.

---

## 6. Charge 6 — empty-parameter P12 functional

Independent parse of `ALLQ_EMPTY_PARAMETER_P12_FUNCTIONAL.tsv` plus the local replay of the full 2,893-term substitution:

| Claim | Observed |
|---|---|
| digest | `530d3c78df4d1dd43a892976aede83bcc6aefd697a40be71a195e83cbc15a7f8` |
| q terms / support count | 13 / 13 |
| support | `(), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,), (11,), (12,), (13,), (14,)` |
| mixed-q terms | 0 |
| total q degree | 1 |
| `q2` present | no |
| `q15` present | no |
| `q16,...,q24` present | no |

`write_qpoly` (client lines 102–108) emits every nonzero coefficient with no exponent filter. `empty_parameter_value` (lines 245–266) scans every parameter monomial of specialized P12; telemetry records scans through 2,750 of 2,893 terms with 221 retained, then `literal_P12_retained_pivot_only_terms=245` after the rest. Intermediate `current_q_terms` rose to 23 and collapsed to 13, which is cancellation in the sum, not an omitted scan. Because the pivot solution itself carries `q2` and `q16,...,q24`, their absence from the 13-term result is vanishing after the full literal computation.

`QPoly` has no degree cutoff, so total q-degree one is a computed vanishing of higher products of degree-one pivot coordinates, not a truncation.

---

## 7. Charge 7 — pure q14 E3-coordinate-0 versus V89H7

Coordinate 0 of the `(14,)` row of the functional TSV is exactly

```text
N / [V^7 - 8 V^5 U^3 + 16 V^3 U^6]
```

with

```text
N = 3856216/375 V^{10} U^2
  + 1625866424/375 V^8 U^5
  + 30525031264/375 V^6 U^8
  - 10638708808/375 V^4 U^{11}
  - 4168187296/75 V^2 U^{14}
  + 710528/15 U^{17}.
```

Flint identities:

- `V^7 - 8 V^5 U^3 + 16 V^3 U^6 = V^3 (V^2-4U^3)^2`
- TSV numerator equals this `N`
- `N ≠ 0`
- `gcd(N, den) = 1`

This is the displayed V89H7 functional (`H7_RESULT.md` lines 38–50; H11 expected value at lines 373–381). The client compares `Rat3.coerce(scalar_coordinates(q14_empty)[0])` to that value and asserts both equality and nonzeroness (lines 370–385). The local replay passed those asserts.

Under `q2=...=q13=0`, the functional support `{(), q3,...,q14}` retains only `()` and `q14`. The positive-q support is exactly pure q14. Equivalently, the client’s `tail_positive` set with `TAIL=(14,16..24)` is asserted equal to `{(14,)}` (lines 364–369). High q were present in the pivot solution and in `N` before this comparison.

---

## 8. Charge 8 — denominator ledger

`denominator_record` (`replay_v89h10t_allq_simultaneous_triangular_flag.py` lines 166–171) takes the monic LCM of scalar denominators and factors it. A record is allowed only if every monic factor lies in `{U, V, V^2-4U^3}` (`SPECIAL_ALLOWED_MONIC`, H10T lines 37–38). On `F=0`, `H=(V^2-4U^3)/U` and `B3=V^4`, so this is exactly the pullback of the registered radical of `U*H*B3`.

Emitted ledger (`ALLQ_P12_FUNCTIONAL_DENOMINATORS.tsv`):

```text
pivot_solution             V^8 U^7 - 8 V^6 U^{10} + 16 V^4 U^{13}   = U^7 V^4 (V^2-4U^3)^2
empty_parameter_functional V^8 U^5 - 8 V^6 U^8 + 16 V^4 U^{11}     = U^5 V^4 (V^2-4U^3)^2
```

Both match the charged maxima exactly, not a larger set. Flag-basis ledgers remain the frozen H10T values `U^4 V^4 (V^2-4U^3)^2` and `U^5 V^4 (V^2-4U^3)`.

Hostile factorization of *every* scalar denominator appearing in the functional TSV (23 distinct denominators, 89 nonzero E3 coordinates) and the pivot TSV (45 distinct denominators, 219 terms): each flint factor is `U`, `V`, or `V^2-4U^3` up to units, and each denominator divides the corresponding claimed common polynomial. No unregistered factor.

Inversion sites:

- `E3.inverse` (`c1_c2_c3_trivariate.py` lines 419–422) requires a two-sided inverse (`self * result == E3(1)`), so it inverts units of E3, not zero-divisors.
- `inverse_constant_matrix` uses only those E3 inverses, on `A(0)` and on `S`.
- `QPoly.inverse` refuses nonconstant q.
- `solve_upper` never inverts: diagonal 1.
- No determinant of a q-matrix is inverted in H11. Unimodularity of `I+N` is by strict-upper triangularity, not by an adjugate over `Frac(R)`.

Output denominators therefore cannot hide an unregistered inverted q-polynomial. Intermediate E3 inverses that cancel identically in the output would have to be units on `D(U*H*B3)` after specialization; anything that remains is in the ledger, and the ledger is licensed. The local replay’s `functional_denominators_registered=true` is the same check on independently recomputed values.

---

## 9. Charge 9 — Python/custom exact arithmetic

The H11 client and every parent it executes are Python. Coefficient arithmetic is E3 / `Rat3` / `QPoly`. Equality is exact coefficient-dictionary equality (`QPoly.__eq__`, V87 lines 140–141; E3 `__eq__`). There is no Singular session, no `qring`, no Singular `std`, no Singular `subst` or `diff`, and no Sage. The two hits of the string `singular` in the case Python files are assert labels `singular_base_pivot_block` and `singular_prime_FIRST`, i.e. fail-closed rank checks, not a Singular driver. H11 never takes the H6 finite-prime path.

---

## 10. Charge 10 — scope

`P12_FLAG_RESULT.md` lines 63–67, `PREREGISTRATION_P12_FLAG.md` lines 37–41, and the result artifact lines

```text
full_17_parameter_normal_form_computed=false
unit_ideal_claim=false
source_point_claim=false
whole_TD6_killed=false
JC2_resolved=false
```

state the firewall. The computation is the empty-nonpivot coefficient of one quotient functional of literal P12. It does not compute the full normal form in the 17 free jet parameters, prove a unit ideal or source-point exclusion, cover a unit-q chart, license q15 as a source coordinate, supply a total-Rees map, close TD6, or resolve JC2. Sibling files in the same case directory that are not named in `P12_FLAG_FREEZE.sha256` are outside this frozen theorem.

---

## Custody note on local replay

The independent replay wrote only under `/tmp/td6_v89h11_review_recompute`. It used the frozen R1 client and nested parents in place, with `v85.restore_base_qd_state()` at exit. The producer package, campaign ledgers, and `jc2-lean` were not modified.
