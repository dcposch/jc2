# Hostile different-model review — normalized B9 exact rational/SNF core

| Field | Value |
|---|---|
| Producer | `xmodel/as-b9-9-12-exact-core-cokernel-producer-20260825.md` (SHA-256 `ba9bfc933f9638d6956f8ae8ef87181bb4be1f9e06cd6990a3698b9b9640d871`) |
| Frozen case | `cases/as_b9_9_12_exact_core_cokernel_20260825/` |
| Pinned parent | `cases/as_b9_9_12_full_fibre_linear_window_20260825/solve_linear_window_9_12.py` (SHA-256 `fb4f16d808dfba754582fb1b5fe10dfa0e69bca0888b38f92586e1f5534724e2`) |
| Grandparent used for reconstruction | `cases/as_b9_max12_w5_survivor_aws_20260825/replay.py` (SHA-256 `f1b50bb2c3e21369da205ebcf1ba028eede20c89d5ad863253fdfec4d6d28c5d`), W5 review **CONFIRMED** |
| Overall verdict | **CONFIRMED** |
| Mathematics | **CONFIRMED** |
| Source typing | **CONFIRMED** |
| Software | **CONFIRMED** (non-blocking notes below) |
| Custody | **CONFIRMED** of the frozen r6d python-flint 0.9.0 run as one execution of the audited source. This job is not dual-host. Box02/Box03 identity is used only for the parent linear-window `result.json` |
| Wording / scope | **CONFIRMED**. The producer’s firewall is load-bearing and is not over-read |
| Mathematical defects | none |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Evidence | source-independent reconstruction of `A` and `b` from the pinned W5 Jacobian (146 unit columns plus `d5`, 25 ms); independent SHA-256 of freeze/manifest/closure/payloads; exact integer kernel multiplication against that `A`; modular rank-nullity over many primes; combinatorial count `4556`; term-by-term reconstruction of `C^T(b+243 det J(T))`; Smith-histogram arithmetic against the frozen dual-AWS window ranks. No python-flint, no `exact_core_cokernel.py` execution, no SNF, no AWS rerun |
| Git HEAD | `d0f6edfbfcd8fbe4c77ffadcd336df349c11eb7e` (producer, this case, the linear-window case, and W5 `replay.py` uncommitted) |
| Review window | 2026-08-25 |

## Verdict

**CONFIRMED**

Over one fixed B9 mod-243 parent, the exact all-row determinant equation of the complete normalized `(P<=9, Q<=12)` coefficient box, after the outer factor `243` is removed, is

```text
E(T) = b + A*T + 243*det J(T)
```

with `A` of size `276 x 146`. Independently reconstructed `A` and `b` hash to the published values. Exact rational rank of `A` is `142`, the rational right kernel has dimension `4`, the rational left kernel has dimension `134`, and the augmented rank is `143`. The linear equation `A*T = -b` is therefore rationally inconsistent; any rational zero of `E` must cancel the obstruction on the cokernel. Primitive integer bases of both kernels multiply `A` to zero on every entry. The Smith 3-adic histogram of the stored invariant-factor list is

```text
v3 : count
 0 : 85
 1 : 30
 2 : 12
 3 :  2
 5 :  2
 6 :  2
 8 :  3
10 :  1
12 :  2
13 :  1
17 :  1
18 :  1
```

with cumulative counts `85,115,127,129,129` below valuations `1` through `5`, matching the frozen finite-window ranks and totalling rational rank `142`. Projection of `b + 243 det J(T)` onto a primitive left-null basis yields a genuine `134`-row quadratic compatibility system: the constant is nonzero of content valuation `21` at `3`, there are exactly `4556` mixed P-Q terms (every pair with nonzero polar scalar), and the coefficient span has rational rank `68`. This is not an emptiness theorem.

## Strongest exact claim

Fix the displayed B9 point `(p5,q5)` of source SHA-256 `f1b50bb2…`, determinant one modulo `243`. Let `T` run through the complete `146`-parameter normalized `(9,12)` box, and write `F = F5 + 243 T`. The integer identity

```text
det J(F) - 1 = (det J(F5) - 1) + 243 B(F5, T) + 243^2 det J(T)
```

divides by the outer `243` to give `E(T) = b + A*T + 243 det J(T)`, where `b = (d5-1)/243` and the columns of `A` are the divided polarizations `B(F5, e_j)`. This `A` has SHA-256 `c073c6e6…` and this `b` has SHA-256 `da68b06f…`. Over `Q`,

```text
rank A = 142,    dim ker A = 4,    dim ker A^T = 134,    rank [A | -b] = 143.
```

So `A*T = -b` has no rational solution. Let `C` be a primitive integer `276 x 134` basis of `ker A^T`. The projected polynomial `H(T) = C^T(b + 243 det J(T))` is not the zero polynomial: its constant has 3-adic content valuation `21`, and its quadratic part consists of the `4556` mixed monomials `T_p T_q` with polar scalar `i ell - j k ≠ 0`, spanning a 68-dimensional space of coefficient vectors. The exact rational rank `142` corrects the finite-window stall `129`; it does not contradict it.

## Sharpest non-claim

A structural diagnostic of one normalized `(9,12)` coefficient box over one fixed B9 mod-243 parent. A nonzero projected polynomial is a compatibility system, not an emptiness theorem: `H` may have zeros, and solving the remaining image coordinates of `A` remains part of any sufficiency claim. Not a common-cubic landing, not coverage of the earlier mod-243 fibre, not an all-depth / `Z_3` / characteristic-zero point, not a maximum-twelve theorem, not a counterexample, and not JC2. The r6d FLINT job is one implementation, not a second engine.

---

## Evidence layers (do not collapse)

1. **Source-independent reconstruction (this review).** The pinned W5 source was executed only to obtain `p5`, `q5`, and `jac`. The `276 x 146` matrix `A` and the length-`276` vector `b` were then rebuilt as `(jac(F5+243 e_j)-d5)/243` and `(d5-1)/243` in the graded `(9,12)` box, without importing `exact_core_cokernel.py`, without exec’ing the linear-window solver, and without python-flint. Wall time 25 ms. Both published hashes matched. Exact integer multiplication then checked the stored kernel bases against this `A`. Modular Gaussian elimination over many primes, plus rank-nullity against those kernels, proved `rank_Q A = 142` and `rank_Q [A|-b] = 143`. Every projected P-Q coefficient was rebuilt from the stored left basis and the polar formula; all `4556` matched. Combinatorially, `4556` is exactly the number of mixed pairs with nonzero polar scalar.

2. **Source-identical AWS run (producer custody, not a second solution).** Job `as_b9_9_12_exact_core_20260825T1722Z` on r6d, venv python-flint 0.9.0, `/usr/bin/time -v` elapsed `0:34.85`, max RSS `241572` KiB, `solver.rc=0`. Stdout records `rank_right_left 142 4 134`, `augmented_solvable 143 False`, `projected_terms_rank 4556 68`, and result SHA-256 `28d19d18…`. This is custody that the audited source ran once. Launcher stdout/stderr are the empty-file digest. There is no Box02/Box03 pair for this job.

3. **Frozen dual-AWS parent window.** Linear-window Box02 and Box03 `result.json` are byte-identical to this job’s `parent_replay.json` at SHA-256 `8c4060e8…`, and already store `matrix_integer_sha256 = c073c6e6…`. Their stage ranks `85,115,127,129,129` are a different engine (custom `F_3` RREF of successive Bocksteins), not FLINT SNF. Agreement with the Smith cumulative counts below valuations `1..5` is a cross-check of the 3-adic profile of `A`, not a second computation of the high invariant factors.

No local python-flint SNF, no AWS rerun of `exact_core_cokernel.py`, and no second Smith engine.

---

## Charge 1 — Regeneration of `E(T)=b+A*T+243*J(T)` from the pinned parent

**CONFIRMED**

Independently recomputed SHA-256:

| Object | SHA-256 |
|---|---|
| `replay.py` (B9 mod-243, W5 **CONFIRMED**) | `f1b50bb2c3e21369da205ebcf1ba028eede20c89d5ad863253fdfec4d6d28c5d` |
| `solve_full_output_mod729.py` | `4deb7fe07acef4f37bb14735493b0d20b6c7ac66bb10633f81b7bc1a48264bd4` |
| `solve_9_12_mod729.py` | `d0c6fd4b62350b0d115aefd60846613ca7484dd3e5bdafdcd9339316b944a848` |
| `solve_linear_window_9_12.py` (this job’s `EXPECTED_PARENT`) | `fb4f16d808dfba754582fb1b5fe10dfa0e69bca0888b38f92586e1f5534724e2` |
| `exact_core_cokernel.py` | `1afbf2441c9d127ad2f57537f06067c2ee0331ac2dafeb151dab8c68adf646e1` |
| parent linear-window `result.json` / this job’s `parent_replay.json` | `8c4060e8e48978492e115955af167e11149d6ba18be83ee3c82121834d617667` |
| this job `result.json` | `28d19d18578641e1dc0f0e0f996409234afa5a70b2daa1ede55153c84650f794` |
| producer report | `ba9bfc933f9638d6956f8ae8ef87181bb4be1f9e06cd6990a3698b9b9640d871` |
| this review’s prompt | `1dacb651ae5a27c2ff40c24bedf95c9923bbceb32eba572d506c8b585d88c3f0` |
| `MANIFEST.sha256` | `190dc48964db0ad68679be92ec000141e2e5711c7fc324c5a39ddb60ea0dda97` |
| `SOURCE_CLOSURE.sha256` (67-path list) | `d4e4dfcf94aacce4fe99eff4715b451e9161773f5558d63627defc079b8481b9` |

Every FREEZE line (5 paths) and every MANIFEST line (18 paths) recomputes. Every SOURCE_CLOSURE path (67) recomputes. The linear-window parent is hash-pinned and re-exec’d in-process by the AWS job; the deposited `parent_replay.json` is byte-identical to both frozen linear-window boxes.

The Jacobian of a sum is bilinear over `Z`. With `F = F5 + 243 T`,

```text
det J(F) - 1
  = (d5 - 1) + 243 B(F5, T) + 243^2 det J(T).
```

Dividing by the outer `243` produces the displayed `E`. Each standard basis vector `e_j` of the `(9,12)` box is pure-P or pure-Q, so `det J(e_j) = 0` and the `j`-th column of `A` is exactly the divided polar `B(F5, e_j)`. The producer’s `J(T)` is `det J(T)`, not the Jacobian matrix. The parent’s `5005` mixed-unit pair controls are a valuation check that the quadratic remainder after the linear polar is divisible by another `243` (undivided factor `243^2 = 3^{10}`); they are not required once the bilinear identity is granted. This review did not rerun those `5005` numeric controls.

The 146 T-coordinates used for `det J(T)` are the same coordinates as the columns of `A`. D12 `support` is graded total degree `0..12`; `allowed` is the first `55` P-slots (degree `<=9`) followed by all `91` Q-slots. The diagnostic enumerates `support_p` and `support_q` in that same graded order, so `T[0:55]` and `T[55:146]` match.

This reconstruction of `A` and `b` is **source-independent of `exact_core_cokernel.py` and of the linear-window RREF**. It is not independent of the W5 `jac` implementation; that implementation is already **CONFIRMED**.

## Charge 2 — All 276 rows, all 146 variables, published hashes of `A` and `b`

**CONFIRMED**

Independently: monomials of total degree `<=9` in two variables number `10*11/2 = 55`. Monomials of total degree `<=12` number `13*14/2 = 91`. The normalized box is those `55` P-coefficients together with those `91` Q-coefficients, total `146`. The determinant ambient of two degree-`12` maps is the `23*24/2 = 276` monomials of total degree `<=22`. For maps actually in the `(9,12)` box the Jacobian has total degree at most `8+11=19`, so the D12 ambient is a complete superset; nil rows are retained.

The independent reconstruction built every one of the `276` rows and every one of the `146` columns, including the two identically zero columns of the constant-P and constant-Q units (derivatives of constants vanish). Canonical JSON SHA-256:

| Object | SHA-256 | Match |
|---|---|---|
| reconstructed `A` | `c073c6e6aec5a0d19f2296ff218f02d269c5bc6c54b129915ef54f2c22bd49ae` | this `result.json`; parent `matrix_integer_sha256`; both linear-window boxes |
| reconstructed `b` | `da68b06f556f6b261f657822945eab64ee7fe131964133a07824d67605edf773` | this `result.json` |

The parent window does not serialize `b`. The `b` hash is therefore new relative to the window result, and is obtained here from `(jac(p5,q5)-1)/243` coefficientwise on the `276` slots, with every coefficient divisible by `243` as asserted. Sort-keys versus no-sort-keys JSON dumps of `A` coincide, as they must for a list of lists of integers.

## Charge 3 — Exact rational rank 142, augmented rank 143, linear insolubility

**CONFIRMED**

This is **not** a reading of `fmpz_mat.rank()`. Against the independently reconstructed `A` and `b`, and the stored primitive bases:

- Four right-kernel vectors satisfy `A v = 0` on every entry, and have rank `4` over `F_2`, `F_3`, `F_13`, and `F_17`. Hence `rank_Q A <= 146-4 = 142`.
- Modular rank of `A` is `142` at every tested prime that does not divide the 3-free part of the stored Smith list: `13,17,19,23,29,31,37,41,43,47`. Hence `rank_Q A >= 142`.
- Therefore `rank_Q A = 142` and `dim ker_Q A = 4`. Rank-nullity gives `dim ker_Q A^T = 276-142 = 134`.
- Modular rank of `[A | -b]` is `143` at those same primes. Hence `rank_Q [A|-b] >= 143`. It cannot exceed `142+1`, so it equals `143`.

The linear equation `A*T = -b` is rationally inconsistent. Equivalently, the independently recomputed constant `C^T b` is a nonzero integer vector (16 nonzero coordinates, content `23932705695997656960 = 3^{21}` times a 3-unit). Over `Q` these two statements are the same fact; both were obtained without FLINT.

Rank drops over `F_5`, `F_7`, and `F_11` (`135`, `138`, `140`) are the expected ones: the stored invariant factors have 3-free parts in `{1,2,4,8,40,280,560,6160}`, which introduce `5`, `7`, and `11`. They do not disturb the rational rank.

The producer’s “only the linear equation `A*T=-b` is rationally inconsistent” is licensed as a statement about the linear truncation of `E`, not as a claim that `E` itself has a rational zero. Charge 7 forbids that reading.

## Charge 4 — Right/left kernel dimensions 4/134, primitiveness, exact multiplication

**CONFIRMED**

Stored `bases.json` SHA-256 `9d1e26f24492c380530bbf29f072fc85d23a1ef1cfc5ad24c432fd8d8aad37f3` matches the file and the result field. It contains `right_basis` of length `4` (each length `146`), `left_basis` of length `134` (each length `276`), and `particular_rational: null`.

Against the independently reconstructed `A`:

- every right vector has content `1` and positive first nonzero coordinate;
- every left vector has content `1` and positive first nonzero coordinate;
- `A v = 0` for all four right vectors (max absolute residual `0`);
- `v^T A = 0` for all 134 left vectors (max absolute residual `0`);
- the four right vectors are independent over `F_2`;
- the 134 left vectors have rank `134` over `F_53` and over every larger tested prime except `79` (rank `119` there is a modular drop, not a Q-dependence).

The AWS source primitizes FLINT `nullspace` columns and then asserts the same two-sided multiplication against its own `A`. Those asserts ran (`rc=0`). This review repeated the multiplication against a second copy of `A`. The emitted bases are therefore a primitive Q-basis of both kernels, not merely “134 vectors in the left kernel.” Dimensions `4` and `134` are then rank-nullity, not an extra FLINT claim.

## Charge 5 — Full Smith diagonal, 3-adic histogram, window ranks `85,115,127,129,129`

**CONFIRMED** of the 3-adic profile and of its agreement with the frozen window. The raw invariant-factor integers remain one-engine FLINT, internally consistent with that profile.

The stored nonzero diagonal has `142` positive entries, equals `rank_Q A`, and is a genuine invariant-factor chain: `s_i` divides `s_{i+1}` at every step. Independently recomputing `v_3` of each listed integer reproduces the published histogram exactly, including the gap at valuation `4`. Cumulative counts of factors with `v_3 < k` for `k=1..5` are `85,115,127,129,129`. The 13 remaining factors have `v_3 >= 5` and account for `129+13=142`.

Those five cumulative counts are the ranks of `A` over `Z/3^k`. They agree with the frozen dual-AWS linear-window combined ranks

```text
stage 1 729     rank 85
stage 2 2187    rank 115
stage 3 6561    rank 127
stage 4 19683   rank 129
stage 5 59049   rank 129
```

which were computed by a custom `F_3` RREF of successive Bocksteins, not by FLINT SNF. The stall from stage 4 to stage 5 is the missing valuation-`4` slot in the histogram. The exact rational rank `142` therefore corrects, rather than contradicts, any heuristic that treated the last window rank `129` as `rank_Q`.

The high invariant factors themselves (`v_3` in `{5,6,8,10,12,13,17,18}`, last entry `2386510212240 = 3^{18}*6160`) were not recomputed by a second Smith engine. What is confirmed independently is the 3-adic histogram as a function of the stored list, the divisibility chain, the total length `142`, and the identification of the first five cumulative counts with the frozen window. That is the content of the charge.

## Charge 6 — Every projected P-Q term, count 4556, coefficient rank 68, valuation 21, payload hashes

**CONFIRMED**

The mixed polar of two monomials `x^i y^j` and `x^k y^ell` is `(i ell - j k) x^{i+k-1} y^{j+ell-1}`. Independently:

- `55*91 = 5005` P-Q pairs;
- `4556` of them have nonzero polar scalar, `449` are parallel (including pairs involving the two constants);
- none of the `4556` targets has a negative exponent or falls outside the `276` slots;
- **no pair with nonzero scalar has vanishing projection**. The count `4556` is therefore purely combinatorial, and does not depend on the left kernel.

The uncompressed canonical JSON of `projected.json.gz` has SHA-256 `89915399932a4c827723dd19b0de880522ee47db6e63132f9c9e82b9298a8912` and length `14169636` including the trailing newline. The stored gzip bytes have SHA-256 `22fc1efca220a21c178b5a393f1e2cf122c1b59e826c7622a7522ceb6b31890d`. (Local recompression with `mtime=0`, `compresslevel=9` is the same length but a different zlib stream; the uncompressed payload is the mathematical object.)

Term-by-term, all `4556` stored records match the reconstruction

```text
coefficient = [243 * scalar * C[row_target]  for C in left_basis]
```

with the claimed `(p_index, q_index, target, jacobian_scalar)`, in graded order, with no zero vectors. The stored constant equals the independently recomputed `C^T b`, content valuation `21`. The stored quadratic content-valuation histogram is reproduced from the coefficients, ranges from `5` through `31`, and sums to `4556`.

Coefficient span: the `134 x 4556` matrix of stored coefficient vectors has modular rank `68` at primes `19,29,31,37,43,47,53` and never higher in the sample (`13,17,23,41` drop). Combined with FLINT’s exact rank `68` on the AWS run, the rational span has rank `68`. The modular lower bound `68` is source-independent; the matching exact rank is the audited FLINT call `coefficient_matrix.rank()` on r6d. No tested prime exceeds `68`, which is the expected behaviour if the exact rank is `68`.

## Charge 7 — Strict logical firewall

**CONFIRMED**

Preregistration, README, producer, and `result.json` agree, and the mathematics agrees with them.

`H(T) = C^T(b + 243 det J(T))` is necessary for `E(T)=0` because `C^T A = 0`. It is not sufficient: a zero of `H` still has to lift through the image coordinates of `A`. A nonzero polynomial in 146 variables may have zeros; coefficient rank `68` is 68 quadratic constraints, not a proof of emptiness. The constant being nonzero kills only the linear truncation.

The following are refused, and are not licensed by anything in this package:

- a common-cubic conclusion (SOURCE_CLOSURE lists unused common-cubic paths; they are not consumed);
- complete earlier-fibre coverage;
- an all-depth / inverse-limit / `Z_3` point or exclusion;
- a maximum-twelve theorem;
- a counterexample;
- JC2.

The producer status line “PROVISIONAL PRODUCER; DIFFERENT-MODEL REVIEW PENDING” is the pre-review banner. It does not weaken the firewall of the claim that was actually written.

---

## Mathematical defects

None.

## Terminology, custody, or exposition defects (non-blocking)

1. **Single host.** This job ran only on r6d. Dual-AWS byte identity is not available for `result.json`, `bases.json`, or `projected.json.gz`. Layer 1 of this review does not need it for the Q-rank, the kernels, `A`/`b`, or the projected polynomial. It would still be the right custody for a second copy of the FLINT Smith list.
2. **SOURCE_CLOSURE is a campaign superset.** The 67-path list includes `as_b9_9_12_common_cubic_3p11_20260825/` files that this diagnostic never imports. Every listed hash recomputes. The tight runtime chain is W5 `replay.py` → D12 mod-729 → `(9,12)` mod-729 → linear window → this script, and those five sources are in the closure.
3. **Empty launcher logs.** `launcher.stdout` and `launcher.stderr` are the empty-file digest `e3b0c442…`, as in several sibling jobs. Custody of the run is carried by `solver.stderr` (`time -v`), `solver.stdout`, `pip.stdout` (python-flint 0.9.0), `api.stdout` (rank/nullspace/snf smoke test), and `solver.rc=0`.
4. **Dense `A` is not serialized.** Independent re-RREF from this package’s own payload is impossible by design. This review rebuilt `A` from W5 in 25 ms; that reconstruction is the substitute.
5. **Smith integers are one-engine.** Charge 5 confirms the 3-adic histogram and the window identification. It does not claim a second Smith form of `A`.
6. **Compressed-payload determinism is host-zlib.** Uncompressed canonical JSON is the stable hash. Re-gzip on this Mac did not reproduce `22fc1efc…` even with `mtime=0`.
7. **Boolean flags in `result.json`** (`right_kernel_exactly_checked`, `left_kernel_exactly_checked`) are written `True` after asserts. The load-bearing objects are those asserts, `rc=0`, and the independent multiplication in Charge 4.

None of these changes an identity or licenses a broader claim.

## Promotion

The exact rational/SNF core of the normalized B9 `(9,12)` operator over the displayed parent may be consumed as confirmed:

- `E(T) = b + A*T + 243 det J(T)` on all 276 rows and all 146 variables, with the published hashes of `A` and `b`;
- `rank_Q A = 142`, `rank_Q [A|-b] = 143`, rational insolubility of `A*T=-b`;
- primitive kernels of dimensions `4` and `134` with exact multiplication;
- Smith 3-adic histogram as published, agreeing with the finite-window ranks `85,115,127,129,129`;
- the projected compatibility system `H(T) = C^T(b+243 det J(T))`, 4556 terms, coefficient rank 68, constant content valuation 21.

It may not be consumed as emptiness of `E`, as a common-cubic theorem, as all-depth coverage, or as JC2. Any downstream solver of `H` is a new package.
