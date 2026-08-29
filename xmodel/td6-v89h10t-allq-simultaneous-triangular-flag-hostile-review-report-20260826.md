# Hostile review — TD6 V89H10T all-q simultaneous triangular flag

| Field | Value |
|---|---|
| Target | V89H10T `FLAG_RESULT.md`, `FLAG_FREEZE.sha256`, `FLAG_EVIDENCE.sha256`, `SOURCE_FLAG.sha256`, `source_flag.tar.gz`, client; parent V89H10G `GRAPH_RESULT.md` and `GRAPH_FREEZE.sha256`; both flag AWS evidence trees |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest bad coefficient / denominator / omission | none |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile algebra review. Producer `PASS` banners, dual-host byte identity, and RSS/elapsed lines are custody only |
| Method | SHA-256 of every charged pin and every consumed manifest row; flint identities in `Q(V,U)` on the displayed `S`, `S^{-1}`, GRAPH affine `N`, and the strict-upper artifact; independent re-run of the recursive flag algorithm over `Q` at four points of `D(U*V*(V^2-4U^3))`. No Singular, Sage, Lean, or `jc2-lean`. The AWS client was not re-executed (wrapper gated to Amazon Linux); the exact matrices are recovered from the pinned source plus the frozen artifacts |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Prompt SHA-256 `db1474e24732e592c205d038605877b67326159abaaf42c15c54330799f6f5a9` matched. Independently recomputed SHA-256 of every required primary pin matches. Every path named in `FLAG_FREEZE.sha256` (11/11), `FLAG_EVIDENCE.sha256` (26/26), `SOURCE_FLAG.sha256` (18/18), and `PAYLOAD_CLOSURE.sha256` (56/56) rehashes to the printed digest. Parent `GRAPH_FREEZE.sha256` is 9/9 and `GRAPH_EVIDENCE.sha256` is 34/34. Every `SOURCE_FLAG.sha256` row exists at the case root and as `source/<path>` inside `source_flag.tar.gz`, and both copies match. All 56 payload-closure files exist inside the same tarball and on disk and match. Nested compiler hash pins consumed from that archive also match. Producer `TD6-V89H10T-ALLQ-SIMULTANEOUS-TRIANGULAR-FLAG PASS` was not used as algebra. No file other than this review was written. The frozen producer package was not edited.

---

## Verdict

**CONFIRMED.**

On the frozen V89H10G `F=0` specialization over the registered open `D(U*H*B3)`, the client rebuilds all 38 literal FIRST rows with the 22 licensed independent variables `q2,...,q14,q16,...,q24` and does not compile or divide P12. The relative pivot matrix `B=A(0)^{-1}A(q)` yields `N=B-I` with exact digest `38fb14e38daa36d597cc7ae1cd2bd5dd402ef2cd1587337321b8c204eeeb7f36`, 532 nonzero entries, 6,069 affine-q terms, total q-degree 1, and no q15. That digest was independently rebuilt from the frozen GRAPH affine-edge table.

The unique 14-node SCC is `(0,...,13)`. Its entries involve only `q2,...,q14`. The thirteen coefficient matrices admit a complete common invariant flag: the emitted constant basis `S` and displayed inverse are exact two-sided inverses over `Q(V,U)` (79 nonzero entries each), and flint conjugation `S^{-1} M_e S` is strictly upper for every `e=2,...,14`. Extending `S` by the identity on the other 24 coordinates and applying the emitted topological order makes the full all-22-q matrix `N` strictly upper; the independently conjugated matrix equals the frozen artifact of 2,989 q-coefficient terms entrywise. Hence `N^{38}=0` as a matrix identity over the localized q-polynomial coefficient ring, and

```text
(I+N)^{-1} = I - N + N^2 - ... + (-N)^{37}
```

is an exact two-sided polynomial inverse. The series is a theorem from nilpotence; it was not expanded.

Every displayed denominator of `S` and `S^{-1}` factors as a product of `U`, `V`, and `V^2-4U^3` only, with common denominators

```text
S:       U^4 V^4 (V^2-4U^3)^2
S^{-1}:  U^5 V^4 (V^2-4U^3)
```

up to units of `Q`. After `F=0`, `U*H=V^2-4U^3` and `B3=V^4`, so these are exactly the specialized `D(U*H*B3)` factors. `det(S)=-1` at three independent points of that open, so the determinant inverts no nonunit of `Q[U,V]`.

No q variable was specialized in the flag construction or the full-matrix check. Both AWS flag runs returned rc 0 with byte-identical stdout and mathematical artifacts.

This producer theorem does not reduce P12, extend the reviewed H7/H8 functionals to arbitrary low q, prove a unit ideal or source-point exclusion, license q15 as a source coordinate, supply a total-Rees map, close TD6, or resolve JC2.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Frozen pins | hashes | all required pins match, including parent V89H10G `GRAPH_RESULT.md` / `GRAPH_FREEZE.sha256` |
| 0. Manifests | every named file | `FLAG_FREEZE` 11/11, `FLAG_EVIDENCE` 26/26, `SOURCE_FLAG` 18/18, `PAYLOAD_CLOSURE` 56/56, `GRAPH_FREEZE` 9/9, `GRAPH_EVIDENCE` 34/34; tarball copies match |
| 0. Dual AWS flag | hosts, archive, rc | distinct Box02 / r6d; archive `6fb15850…`; both `rc=0`; math artifacts and stdout byte-identical |
| 1. Literal FIRST / 22 q / `F=0` / no truncation | 38 rows, `q2..q14,q16..q24`, exact chart, untruncated `QPoly` | holds |
| 2. `A(0)`, `A(q)`, `B=A(0)^{-1}A(q)`, `N=B-I` | orientation, digest, affine-linear | holds; digest rebuilt from GRAPH edges; columns of `N` supported only on the SCC |
| 3. Recursive common-invariant flag | completed basis, quotient action, common kernel, independence, previous invariance | holds; no counterexample; generic kernel dimension 1 at each of 14 steps |
| 4. `S`, `S^{-1}` two-sided; 13 conjugations; SCC q-support | exact identities over `Q(V,U)` | holds; SCC entries use only `q2..q14` |
| 5. Identity extension, permutation, `N^{38}=0`, Neumann inverse | full all-q strict-upper, two-sided finite sum | holds; 2,989-term artifact matches independent conjugation |
| 6. Denominator ledger | only `U`, `V`, `V^2-4U^3`; no hidden extra inverse | holds on displayed matrices and `det(S)` |
| 7. No Singular `qring`/`==0`/`subst`/`diff` | Python/custom exact field arithmetic | holds |
| 8. Scope | no P12, no H7/H8 extension, no unit ideal, no q15 source, no total-Rees, no TD6/JC2 | slogans and `FLAG_RESULT.md` keep the firewall |

---

## 1. Custody

Recomputed SHA-256 of the required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `FLAG_RESULT.md` | `612b57bcfc20228152d37e5acef08ea41539481be99dff5878af8a790e4c6d1f` | producer result |
| `FLAG_FREEZE.sha256` | `a156f8394a2966effb006cdfdbb7e64a7da5cefa6e586022a67d29776167d2d9` | freeze |
| `FLAG_EVIDENCE.sha256` | `69ebde85ff4ea117f887d9f56d9ef53da3a3676b0b4726bb653efa3bb6be022c` | evidence manifest |
| `SOURCE_FLAG.sha256` | `67a94374f3ca2585713480477f7aa93caf82c1a79192ecd3d33773c9bc2cdcde` | source manifest |
| `source_flag.tar.gz` | `6fb15850c4e6c4b92039c584c30700295602f2a1c65f048724789cda8a19cb9c` | flag source archive |
| client `replay_v89h10t_allq_simultaneous_triangular_flag.py` | `9c7a5eeede117568aa76d4c26bae11f6e78640313cad6ad559b414ee2cf5098c` | controlling replay |
| `GRAPH_RESULT.md` | `d07b2258d83cb0dfe48193abcf773ccc8a2d943001873858ae0cad58cd5292f0` | parent topology result |
| `GRAPH_FREEZE.sha256` | `39973cb2bd9a215b5dda1d1c32837855aaa08f4c4edaf3bb75aea811fdd09cd4` | parent freeze |

Nested pins reached from the frozen FLAG client and `SOURCE_FLAG.sha256`, independently rehashed:

| Pin | SHA-256 |
|---|---|
| parent H10 v1 client | `4ff99ca9b7d8539aa369b65a953da63dc731d12ba3faf4184678fe8d0b6b9524` |
| H6 parent client | `1301a09f0497abac5197de6b4afc0eba54b5c8de2b05d2cf11db63fab454d757` |
| H5 parent client | `a81c358b58f8b97ec0dfd97128d0f9539782eda70e66a6747a4c2827a1539b9b` |
| V87 parent client | `7c0890abbce996a221f9389372fa3705742d6ecd72531891bfeb5dfc2f1b9463` |
| V86 parent client | `5b160a2bd18434e6142c33be6775e0c212c22ebc67a52d08b246dd0223decd7c` |
| V85 parent client | `ab9753073d694242d4359dc1edc86774724f62d28d15b7c671ba0b796262100e` |
| GRAPH client | `38ebb6bd417408ef024b64660119691e89af09ac5996dd641c32d311a59fc162` |
| `PREREGISTRATION_FLAG.md` | `44cc17efd41bd057abe394ddb1e1f8daf11ec8ee8f7563fcaf60e3368e03c3e7` |
| wrapper `run_v89h10t_allq_simultaneous_triangular_flag.sh` | `9e27dbfec092170ac1e6d5e9709cd27659a51404883b3450b397125cd3bdb65a` |
| `launch_flag_host.sh` | `407ba26ffa21b7630afcae67858d6ea243bee60c765abb81236744667618d530` |
| `PAYLOAD_CLOSURE.sha256` | `cbe7e0be9d49f5aa994790332e2fe0368c32780eac81ee3ddededdf7bb3d5cff` |
| H7 `RESULT.md` (custody pin only) | `49b9dcba0bb5956dfdbb10293b7bdf3e440a39b127929089c2402ffb06db32cd` |
| H8 `RESULT.md` (custody pin only) | `646dd1162cc2e6aa36c3fe72bea5c64a44e19361323593a12fc4c7f137cc0292` |
| generic parent shard | `a4ccd5d81101fdb82ed2f61571c258e2054961d161f4a98461b8f8614d3fd85e` |
| V85 source inventory | `9a612bb64ee974a506a1f3b7fcb471fb8924220ca6d24320af0fc9b8a7de6b7a` |
| F-raw P12 certificate | `8e892ffa914e0f93969abb9722f926486843f59cf77f5861c5ce3d3438281482` |

Byte-identical mathematical stdout is `554a5d43f5c1b484b8f62ee92c067c439cee47bb9e6ab77a6e4bb19667b6e8f9` on both flag hosts. Mathematical output files:

| Output | SHA-256 |
|---|---|
| `ALLQ_COMMON_FLAG_TELEMETRY.tsv` | `89db0510983c95cd5c8b62e6a04ab3675939c62f1f5c2605d9add475cdad12c2` |
| `ALLQ_SCC_FLAG_BASIS.tsv` | `05f9b3df78dc4abcf6ad39c36e1b48c54529b351459664cccfa3cd59d49d1542` |
| `ALLQ_SCC_FLAG_BASIS_INVERSE.tsv` | `30e644c244f65b17cbf9d7a599b60883d1e8c0b1dd6c3fb326c8ae70cda87aac` |
| `ALLQ_STRICT_UPPER_ORDER.tsv` | `35e88aa807ba6a4a0e275f946c23e86b0b3e8fa8aa155684103a08ae13cacb6a` |
| `ALLQ_STRICT_UPPER_N.tsv` | `946b75e5307941a81696ec68e1ae2fbcb6ce480294cead6076e434d8e819e913` |
| `ALLQ_FLAG_DENOMINATORS.tsv` | `5ebfa2b9d693974a21ae0622bf5e5f1aa701e3b2c802952d56d678c6278b8956` |

Box02 (`ip-172-30-0-186`, pid 321437, tag `…box02_20260826T201600Z`, finished `2026-08-26T20:15:24Z`) and r6d (`ip-172-30-0-45`, pid 337674, tag `…r6d_20260826T201600Z`, finished `2026-08-26T20:15:15Z`) are distinct hosts with the same archive `6fb15850…`, both `rc=0`, and zero swap. Mathematical stdout and all six output files are byte-identical. Host stderr differs only in `/usr/bin/time` counters (3:06.39 vs 3:01.95; RSS 296720 vs 297124 KiB). `launch.meta`, pids, and finish timestamps differ as they should. Dual-host equality is custody, not the identity.

Parent GRAPH R1 is likewise dual-host with byte-identical stdout `859332b79367f134ce11c8e36ed310c59eb43b5b47e5cfd8a937f995d24aab49` and affine-edge artifact `f72294bd4e5d74627c3b5877dd8d6830a8a96d061294063df2a145ed3de00263`; both GRAPH R1 `rc=0`. GRAPH V1 is a packaging-negative run and is not used as mathematical evidence; `SOURCE_FLAG.sha256` pins `GRAPH_V1_LAUNCH_ERRATUM.md` only.

`source_flag.tar.gz` contains 200 members, of which 100 are AppleDouble `._*` metadata, and no bytecode. Every charged `SOURCE_FLAG.sha256` and `PAYLOAD_CLOSURE.sha256` path is present as `source/<path>` and hash-correct. The 75 non-AppleDouble files include the 18 source-manifest rows plus nested payload copies.

---

## 2. Charge 1 — hashes, dual AWS, artifacts, source custody

All charged controlling hashes match, as do every freeze/evidence/source/payload row. Both flag `rc` files contain `0`. The six mathematical artifacts plus stdout are byte-identical across Box02 and r6d; `wrapper.log` is the empty-file digest `e3b0c442…` on both hosts. Parent GRAPH freeze and evidence manifests rehash. Archive SHA in both `launch.meta` files equals `source_flag.tar.gz`.

This is custody. Algebra below does not use the `PASS` line.

---

## 3. Charge 2 — 38 FIRST rows, 22 licensed q, exact `F=0`, no truncation

V87 `Q_EXPONENTS = tuple(list(range(2, 15)) + list(range(16, 25)))` (`replay_v87tfaq_total_f_allq.py` lines 32–34) has length 22 and does not contain 15. Parent H10 v1 copies that set as `ALLOWED_Q` (`replay_v89h10_allq_mod_f_unitriangular_functional_v1.py` line 30). The FLAG client asserts `set(seen) == set(p.ALLOWED_Q)` and `seen[exponent] == 1` for every licensed exponent (client lines 188–189), together with `events == 2 and len(first) == 38` (line 187).

`QPoly` is an untruncated sparse ring on that set (class docstring line 41; constructor lines 52–54 refuse any exponent outside `Q_ORDER`; `__mul__` at lines 93–107 concatenates monomials with no degree cutoff; `inverse` at lines 111–118 fail-closes unless the support is the empty q-monomial). FLAG never calls `QPoly.inverse` on a nonconstant q polynomial: the only inverses are `E3.inverse` on constant pivot blocks (`h5.inverse_constant_matrix`, `nullspace`).

Genuine FIRST is `qd.pack("X-2", qd.first_band_polynomials(f1, g1))` (`replay_v87tfaq_total_f_allq.py` lines 250–257). FLAG rebuilds it live (client lines 185–186) after `v87.build_bands()`. Transport is the frozen pair `(p,q)=(t^{15}, t+…+t^{25})` with g-degree 15 held at zero (`build_bands` lines 317–324). That is the reviewed target shear, not a silently omitted source modulus.

Exact `F=0` is the two-sided chart `SPECIAL_C = (V^2-U^3)/U` on `D(U)` (`replay_v85tf1_total_f.py` lines 44–47), applied coefficientwise by `h6.specialize_first` (`replay_v89h6_q14_mod_f_cokernel.py` lines 30–59; FLAG line 195). No other specialization is imposed. Wrapper environment `TD6_F_SPECIALIZATION=exact-C-equals-V2-minus-U3-over-U` and `TD6_Q_SCOPE=q2-q14-q16-q24` (`run_v89h10t_allq_simultaneous_triangular_flag.sh` lines 11–12; `launch_flag_host.sh` lines 30–35) match this split.

Raw unspecialized FIRST common denominator is printed `raw_FIRST_common_denominator=(C*U - 3*U^3)` (stdout line 94), which is `U*H`. `v87.assert_denominators_allowed` (lines 440–445) demands that this common denominator is coprime to `F`. FLAG does not assign a numeric value to any q indeterminate.

P12 compilation is skipped: FLAG prints `P12_compile_and_division_skipped=true` (client line 183) before FIRST rebuild and never calls `compile_current_degree12`. `build_bands` still constructs the underlying f/g charts used for FIRST; it does not extract or divide degree-12 CURRENT.

This is not a low-q unit chart, an independent q15 source modulus, a total-Rees lift, an H7/H8 functional extension, or a TD6 statement.

---

## 4. Charge 3 — `A(0)`, `A(q)`, `B`, `N`, orientation, affine-linearity

FLAG constructs (client lines 196–211)

```text
A0[i][j] = specialized_row_i[pivot_j].constant()
A[i][j]  = specialized_row_i[pivot_j]
B        = A0^{-1} A          # h5.matmul_constant_q
N        = B - I
```

with `h5.base_pivot_columns` producing 38 distinct constant-term pivots (`replay_v89h5_q14_high_unimodular_total_f_v1.py` lines 167–197). `inverse_constant_matrix` (lines 199–228) is ordinary row-augmented Gauss–Jordan over `E3` and returns the right inverse of that row matrix; `matmul_constant` / `matmul_constant_q` / `matmul_q` (lines 231–268) are the matching left-row / right-column products.

This is the same construction as GRAPH (`replay_v89h10g_allq_transported_first_topology.py` lines 110–126) and as H6 `invert_full_q_pivot`. `B = A(0)^{-1} A(q)` means `A(q) = A(0) B` as row-blocks, so `N` acts on the same side as the subsequent conjugations `S^{-1} N S` (column convention: new basis vectors are the columns of `S`). A left/right reversal would send the conjugated SCC block to strictly *lower* triangular form and would fail the producer assert at client lines 278–283 and the independent flint check below. It does not.

GRAPH writes every nonzero coefficient of `N` with `assert len(monomial) == 1` (lines 137–141), so `N` has no constant term and no mixed q-monomials: it is affine-linear in the 22 licensed q's. FLAG asserts `(n_entries, n_terms, n_degree) == (532, 6069, 1)` and the frozen digest (client lines 209–211). Independently hashing the GRAPH affine-edge table in `matrix_stats` order rebuilds

```text
38fb14e38daa36d597cc7ae1cd2bd5dd402ef2cd1587337321b8c204eeeb7f36
```

with 532 nonzero entries, 6,069 terms, exponents exactly `{2,...,14,16,...,24}`, no q15, no constants. Nonzero columns of `N` are only `0,...,13` (the SCC); all 38 rows appear. High-q terms therefore live in those same 14 columns and cannot create an SCC outside `(0,...,13)`, matching GRAPH topology.

---

## 5. Charge 4 — recursive common-invariant-flag algorithm

The algorithm (client lines 122–132, 223–264) is the standard column-flag construction over a field:

1. `complete_basis(flag, 14)` places already-found flag vectors as the first columns and completes by standard basis vectors that preserve independence (`columns_matrix` at lines 111–112 writes those as columns).
2. Conjugation `P^{-1} M P` puts an invariant subspace `W = span(first k columns)` into block form with zero lower-left. The asserted zeros (lines 232–237) are exactly `transformed[row][column] = 0` for `row >= k` and `column < k`, which is `M W ⊂ W` in column convention.
3. The lower-right blocks of all thirteen coefficient matrices are stacked and `nullspace` is computed over `E3` (lines 67–108). Gauss–Jordan is full (every row is reduced); back-substitution sums only over free columns, which is valid in RREF; each returned vector is checked against the original stacked matrix.
4. The first kernel vector is lifted by the chosen complement (`lifted_coordinates = [0]*k + quotient_vector`, then `vector = P * lifted`). If `[v]` lies in the common kernel of the induced maps on `V/W`, then `M(v) ∈ W` for every coefficient matrix, so `W' = W + span(v)` remains invariant and the new diagonal entry is zero (strictly upper, not merely triangular). Independence of the lift is asserted (line 258).

The algorithm does not require kernel dimension 1 in code; it records it and takes `kernel[0]`. Telemetry and stdout both say dimension 1 at every successive quotient 14 down to 1. That was not trusted.

Independent checks, using GRAPH `N` and the displayed `S`, not producer telemetry:

- Flint conjugation `S^{-1} M_e S` over `Q(V,U)` is strictly upper for every `e = 2,...,14`. That is the exact 14-step flag: columns of `S` satisfy `M_e S_k ∈ span(S_0,...,S_{k-1})` identically. There is therefore no counterexample to the claimed flag.
- The same recursive algorithm, run over `Q` at four points of `D(U*V*(V^2-4U^3))`

  ```text
  (V,U) = (4,1), (5,2), (7,3), (3,1)
  ```

  with `HF = V^2-4U^3` equal to `12, -7, -59, 5`, produces a 14-step flag with common-kernel dimension exactly `[1,1,1,1,1,1,1,1,1,1,1,1,1,1]` at every point, and previously built subspaces remain invariant. Kernel dimension of a matrix over `Q(V,U)` at generic points is the generic dimension; numeric dimension 1 at four independent points implies the function-field kernel is 1-dimensional at each step. Displayed `S` columns satisfy the flag property at the same four points.

No exact smallest counterexample exists. The 14-step flag is the columns of the emitted `S`.

Completion of the basis by standard vectors is a choice of complement and does not change the intrinsic common kernel in the quotient; the lift through that complement is still a genuine common-invariant extension. The last 1-by-1 step having kernel dimension 1 means the last diagonal of every coefficient matrix is zero, as required for strictly upper form.

---

## 6. Charge 5 — `S` and `S^{-1}` two-sided inverses; 13 conjugations; SCC q-support

Displayed `ALLQ_SCC_FLAG_BASIS.tsv` and `ALLQ_SCC_FLAG_BASIS_INVERSE.tsv` have 79 nonzero entries each, all with only the first `E3` coordinate nonzero (they lie in `Q(V,U)`). Flint matrix products over `Q(V,U)`:

```text
S * S^{-1} = I_14
S^{-1} * S = I_14
```

with zero mismatches. Producer asserts the same at client lines 268–273.

For each `e = 2,...,14` the SCC coefficient matrix `M_e` extracted from GRAPH `N` satisfies `S^{-1} M_e S` strictly upper. Upper-triangle nonzero counts after conjugation:

| q | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| upper nnz | 24 | 21 | 22 | 21 | 20 | 19 | 18 | 17 | 14 | 10 | 6 | 3 | 1 |

SCC support of `N` is exactly `{2,...,14}`: zero high-q terms in the 14-by-14 block, and every low-q exponent appears. Charge 5's request that SCC entries involve only `q2..q14` holds on the frozen `N`.

---

## 7. Charge 6 — identity extension, permutation, `N^{38}=0`, Neumann inverse

Client lines 292–314 extend `S` by the identity to 38 coordinates (`S_full[i][j] = S[i][j]` on the SCC, else `δ_{ij}`), conjugate the full q-polynomial `N` by `S_full^{-1} (- ) S_full`, topologically order the support graph, and demand the permuted matrix is strictly upper (`upper[i][j] = 0` for all `j <= i`).

Because `N` has nonzero columns only in `0,...,13`, conjugation by `S_full = blkdiag(S, I_{24})` yields

```text
S_full^{-1} N S_full = [ S^{-1} N_{11} S    0 ]
                       [ N_{21} S           0 ]
```

High-q lives in `N_{21}` (and not in `N_{11}`). The emitted order

```text
14,15,...,36, 0, 37, 1,2,...,13
```

is a valid topological linearization of that DAG (acyclic nodes first, with `0` becoming ready before `37`). Independently applying that permutation to the flint-conjugated matrix produces 2,989 q-coefficient terms, zero entries on or below the diagonal, and exact entrywise agreement with `ALLQ_STRICT_UPPER_N.tsv` (2,989 terms, same 22 licensed exponents, no q15). Four-point evaluation of the full 38-by-38 conjugated-and-permuted matrix is likewise strictly upper, with 416 nonzero entries after summing q's.

A strictly upper 38-by-38 matrix over a commutative ring has `N^{38}=0`: the `(i,j)`-entry of `N^k` is a sum of products along strictly increasing index sequences of length `k`, which cannot exist for `k >= 38`. The producer does not claim a tighter index and does not expand the series (`expanded_polynomial_inverse_emitted=false`, client line 352).

The finite Neumann sum is then a two-sided identity over the coefficient ring of q-polynomials with coefficients in `Frac(Q[V,U])` localized at `U*V*(V^2-4U^3)`:

```text
(I+N) (I - N + ... + (-N)^{37}) = I - N^{38} = I
```

and likewise on the left, because powers of a single matrix commute. `S_full` is constant in q and invertible over that localization, so nilpotence of the conjugate is equivalent to nilpotence of `N`. In particular `B = I+N` is unimodular in the 22 q variables on the specialized registered open, without expanding the inverse.

---

## 8. Charge 7 — denominator ledger

Independently parsing every nonzero entry of displayed `S` and `S^{-1}` and factoring its denominator with flint yields only the monic factors `U`, `V`, and `V^2-4U^3`. No extra factor appears in any single entry. The LCM of those denominators is

```text
S:       V^8 U^4 - 8 V^6 U^7 + 16 V^4 U^{10} = U^4 V^4 (V^2-4U^3)^2
S^{-1}:  V^6 U^5 - 4 V^4 U^8               = U^5 V^4 (V^2-4U^3)
```

matching `ALLQ_FLAG_DENOMINATORS.tsv` and `FLAG_RESULT.md` lines 41–45. `SPECIAL_ALLOWED_MONIC` in the client (lines 36–37) is exactly those three.

After `F=0`, `H = C-3U^2 = ((V^2-U^3)/U) - 3U^2 = (V^2-4U^3)/U`, so `U*H = V^2-4U^3`. Frozen `B3 = V^4`. The specialized open `D(U*H*B3)` is `D(U*V*(V^2-4U^3))`. Every inverted factor in the displayed basis is already a unit there.

`det(S)` evaluates to `-1` at `(V,U) = (4,1), (5,2), (7,3)`, where `U`, `V`, and `V^2-4U^3` take multiplicatively independent values. Any candidate `det(S) = c\, U^a V^b (V^2-4U^3)^d` that is `-1` at all three points must have `a=b=d=0` and `c=-1`. The determinant therefore inverts no nonunit of `Q[U,V]`. Combined with the entrywise factorization, no hidden extra polynomial factor survives in the displayed pair `(S, S^{-1})`.

Gauss–Jordan intermediates of `inverse_constant_matrix` over `E3` were not re-traced symbolically. Intermediate primes in the *numeric* GE pivots at those three points are evaluations of `U`, `V`, `V^2-4U^3` and integer content; they are not extra polynomial factors. Because the displayed matrices already multiply to `I` over `Q(V,U)` with only licensed denominators, any cancelled intermediate factor would not restrict the open on which the theorem is stated. The theorem is restricted to the frozen specialized `D(U*H*B3)` context.

---

## 9. Charge 8 — no Singular semantics

The FLAG client and its loaded parents are Python. Arithmetic is `QPoly` over V85 `E3` / `Rat3` (custom exact polynomial-field arithmetic) plus flint only as the AWS runtime's `E3` backend. There is no Singular `qring`, no `==0` test on a quotient ring, no `subst`, and no `diff` in the FLAG client. The two `singular_*` strings in H5/H6 are assert labels on vanishing pivots, not a CAS. Independent verification in this review used python-flint `fmpq_mpoly` over `Q(V,U)` on the frozen artifacts, not Singular.

---

## 10. Charge 9 — scope

`FLAG_RESULT.md` lines 5 and 65–68, `PREREGISTRATION_FLAG.md` lines 21–26, and client lines 183, 352–353 keep the firewall:

- P12 is not compiled or divided.
- The reviewed H7/H8 functionals are not extended to arbitrary low q. H7/H8 result files are hash-pinned as parent custody and are not consumed as algebra.
- No unit ideal, source-point exclusion, or `1 ∈ (P12, FIRST, F)` is claimed.
- q15 is not licensed as a source coordinate; it is absent from `Q_EXPONENTS` and from `N`.
- No total-Rees chart is supplied.
- TD6 is not closed and JC2 is not resolved.
- The finite Neumann inverse is not expanded.

The theorem is an exact producer-tier transported-FIRST statement: on the specialized registered open, the relative FIRST pivot matrix is unimodular in the 22 licensed q variables because it is conjugate-permutation-equivalent to a strictly upper 38-by-38 matrix.

---

## Orientation note

Column convention is used throughout: `B = A(0)^{-1} A(q)`, flag vectors are columns of `S`, conjugation is `S^{-1} N S`, and strictly upper means zeros on and below the diagonal. GRAPH `N` conjugated by the displayed `S` with that convention reproduces the frozen strict-upper artifact. A row/column reversal would have produced a strictly lower matrix and would have falsified both the producer assert and the independent identity. It does not occur.

---

## Conclusion strength

This is a complete common invariant flag for the thirteen low-q SCC coefficient matrices, plus a topological strict-upper form for the full all-22-q `N`, on the frozen specialized `D(U*H*B3)`. It proves unimodularity of the relative FIRST pivot matrix in those q variables without expanding the inverse. It is not a P12 reduction, a unit-ideal theorem, a source exclusion, a q15 source statement, total-Rees, whole TD6, or JC2.

**CONFIRMED**
