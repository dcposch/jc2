# Hostile different-model review — global fresh elimination and 176-coordinate Kuranishi map

| Field | Value |
|---|---|
| Producer | `xmodel/as-b9-9-12-common-cubic-global-fresh-elimination-producer-20260825.md` (SHA-256 `524a56ddfc04a7990f009e8fe781c0b1df694771c747bb40f396490f8eaac94f`) |
| Frozen case | `cases/as_b9_9_12_common_cubic_global_row22_20260825/` |
| Parent family | reviewed `independent_common_core.py` SHA-256 `460199584e128bc2c5f3196871a34437ebdfd7d674ccf0bcc2f52b9db8ace6b8` (`xmodel/as-b9-9-12-common-cubic-3p11-review-grok-20260825.md`, overall **CONFIRMED**) |
| Global chart | `global_row22_v1.py` / `global_row22.py` SHA-256 `b16912cd1b6146a35736e9bb872d96bfa640e1bb920e04b7c5a9e13256d12a3f` |
| Fresh-block compiler | `compile_fresh_block.py` SHA-256 `ce3e3a8e9d0a3d1368e4928c8225d9a0a3a6bbe3b62d881e78e2d80856cf0e3d` |
| Map emitter | `emit_kuranishi_map.py` SHA-256 `1d6dbd671e6652592d9de76a74c86034f8f2e9177703c3410c8a05e533963edf` |
| Overall verdict | **CONFIRMED** |
| Mathematics | **CONFIRMED**. Constancy of the `205 x 55` block is a source/valuation identity on all 299 rows, not a sample. Rank/kernel/quotient `29/26/176` are identities of the frozen payload. Vanishing of the compiled map `K : F_3^{95} -> F_3^{176}` is equivalent to existence of a `3^{12}` lift inside this one chart |
| Source typing | **CONFIRMED** |
| Software | **CONFIRMED** (non-blocking notes below) |
| Custody | **CONFIRMED** of the frozen Box02 fresh block, the three-host overlapping map emission (Box02, Box03, r6d), the Box02 full 176-row formula, and the Box02 aggregate. No residual-family replay was launched for this review |
| Wording / scope | **CONFIRMED**. Solver firewall and the 447-point diagnostic firewall are load-bearing and are not over-read |
| Mathematical defects | none |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Evidence | line-by-line source audit of the parent residual, the `17+78+55` chart, the fresh-block compiler, the QF_BV emitter, and the aggregate; independent SHA-256 of freeze/manifest/sources/gzip/SMT/results; independent `F_3` RREF of the frozen `205 x 55` block, its stored kernel and left quotient, the `205 x 299` left cokernel, and the composed `176 x 299` map; overlap/coverage check of stored coordinate hashes; diagnostic scan of all 447 elimination records. No local `residual` replay, no canonical-family re-execution, no Z3/Boolector/CaDiCaL launch |
| Git HEAD | `f96845eecaa073110d1526e0b08117205a4dcf30` (producer, this case, and the parent 3p11 package uncommitted) |
| Review window | 2026-08-25 |

## Verdict

**CONFIRMED**

Inside the reviewed complete common-cubic family of the one fixed B9 mod-243 parent, the next-digit operator at modulus `3^{12}` is family-constant of shape `299 x 149`, rank 94, kernel 55, and left cokernel 205. After projection to that cokernel, dependence on the final 55 fresh-kernel coordinates is one constant affine block

```text
A_fresh : F_3^{55} -> F_3^{205},
rank 29, kernel 26, left quotient 176,
```

serialized at SHA-256 `9b1ae5b0f64bb3d7fccd27f7d8a3d2cae141c297fd531fd6fff1c302a48fb7d5`. Constancy is licensed by 3-adic order, on determinant rows and on the 23 cubic/quartic common-core rows: predecessor motion starts at coefficient order `3^5`, final fresh-kernel motion at order `3^{10}`, and every predecessor/fresh cross term has order at least `3^{15}`, hence vanishes after division by `3^{11}` modulo 3. The 447 sampled rank-29/UNSAT controls are not that proof.

Existence of a simultaneous `3^{12}` lift of a predecessor point, inside this 149-digit chart, is therefore equivalent to vanishing of one exact map

```text
K : F_3^{17+78} = F_3^{95} -> F_3^{176}
```

compiled from the literal 299-row integer residual modulo `3^{12}`, with chronological division by `3^{10}` then `3^{11}`, after the canonical left quotient has killed the 55-dimensional fibre. Setting those 55 coordinates to zero in the circuit is evaluation of a fibre-invariant functional, not a claim that the zero section lifts.

The three-host overlapping emission covers rows `0..175` with matching overlaps `30--31`, `60--61`, `90--91`, `120--121`, `150--151`, common structural hash `557123112e5c3e4ea5d3a5a95709d816254080e0eeef2d995d028013db468b48`, and full-formula SHA-256 `108cfdaae0c897ab66518e18d5e38d0969a1f8f936eeb488fd9144e4fbfe0f4c`. No SAT model and no UNSAT certificate for `K` is in the freeze. Stopped or resource-exhausted solvers are not this theorem.

## Strongest exact claim

Fix the displayed B9 parent of source SHA-256 `f1b50bb2c3e21369da205ebcf1ba028eede20c89d5ad863253fdfec4d6d28c5d` and the reviewed complete common-cubic parameterization of SHA-256 `46019958…`, with canonical coordinates `17` active plus `78` spectator-kernel plus `55` final fresh-kernel. Write `F` for the 299 integer rows (276 determinant coefficients of `det J(P,Q)-1` in total degree `≤22`, plus 10 coefficients of `P9 - P_{(0,9)} H^3` and 13 of `Q12 - Q_{(0,12)} H^4`). At every family point, `F ≡ 0 (mod 3^{11})`. The `F_3` Jacobian of `F` for a values-increment of size `3^6` (coefficient increment `3^{11}`) is independent of the 150 family coordinates and has rank 94. After left projection to its 205-dimensional cokernel, the increment in the 55 fresh-kernel directions is the constant rank-29 block `A_fresh` above.

A predecessor `(a,s) ∈ F_3^{17} × F_3^{78}` therefore admits a digit `u ∈ F_3^{149}` with

```text
F(v(a,s,f) + 3^6 u) ≡ 0 (mod 3^{12})
```

for some fresh-kernel parameter `f` if and only if `K(a,s) = 0` in `F_3^{176}`. Quadratic increments of `u` have coefficient order `3^{22}` and do not contribute modulo `3^{12}`, so the linear next-digit equation is exact at this modulus. `K` is the circuit of `emit_kuranishi_map.py` at SHA-256 `1d6dbd67…`, not an interpolated polynomial, and not a solver status.

## Sharpest non-claim

A finite-depth reduction of one parent’s displayed `3^{11}` common-cubic chart to a 95-variable, 176-coordinate obstruction modulo `3^{12}`. Not emptiness of that obstruction, not a SAT lift, not survival past `3^{12}`, not an inverse-limit/`Z_3` point, not a characteristic-zero Keller map, not a Q8 landing, not complete earlier-parent coverage, not a maximum-twelve theorem, not a counterexample, and not JC2. The 447 predecessor controls are a sampled negative diagnostic. Boolector 1.5.118 rejecting `define-fun`, and any Z3 run outside this freeze, are not a decision of `K`.

---

## Evidence layers (do not collapse)

1. **Parent residual and chart (already reviewed).** `independent_common_core.py` constructs the 299-row integer residual on 149 coordinates from the pinned linear-window parent `fb4f16d8…`, stages through `3^{10}` with family dimensions `55,81,99,116,133`, splits `133 = 17+116` by a `GL(133,Z)` change, and records fresh rank/kernel/cokernel `94/55/205` with spectator rank 38 in the cokernel. That audit stands; this review does not re-execute it.
2. **Source/valuation constancy of `A_fresh`.** The block compiler evaluates the 55 fresh directions only at the origin of the 95-chart. Constancy on the whole chart is the order calculation in Charge 2, applied to all 299 rows. The 447 identical-matrix records are corroboration, not the proof.
3. **Independent linear algebra of the frozen payload.** Decompressing `fresh_block.json.gz` (gzip SHA-256 `f7f473c5…`, uncompressed `6b972339…`) and ranking over `F_3` reproduces shape/rank/kernel/quotient `205 x 55`, `29`, `26`, `176`, byte-identity of the stored kernel and left quotient with the RREF bases, `fresh_left · A_fresh = 0`, rank 205 of the stored `205 x 299` left cokernel, and rank 176 of the composed `176 x 299` map with support histogram `{1:154, 2:12, 3:5, 4:2, 5:2, 6:1}`.
4. **Three-host circuit emission.** Box02, Box03, and r6d consumed one pinned emitter, one pinned `global_row22_v1.py`, one pinned parent compiler, and one pinned gzip. Overlap hashes and the full-formula SHA match the freeze. This is custody that the audited constructors ran, plus a structural-hash cross-check, not a second residual algorithm.
5. **Solver layer unused.** `solve_kuranishi_z3.py` exists. No SAT model, DRAT, or independently checked UNSAT certificate is in `FREEZE.sha256`. None is consumed.

---

## Charge 1 — pinned SHAs and dimensions `17+78+55`

**CONFIRMED**

Independently recomputed SHA-256, matching the freeze and the AWS `SOURCE.sha256` files:

| Object | SHA-256 |
|---|---|
| `independent_common_core.py` (parent Box02 and every AWS copy) | `460199584e128bc2c5f3196871a34437ebdfd7d674ccf0bcc2f52b9db8ace6b8` |
| `global_row22_v1.py` / `global_row22.py` | `b16912cd1b6146a35736e9bb872d96bfa640e1bb920e04b7c5a9e13256d12a3f` |
| `compile_fresh_block.py` (tree and AWS Box02 copy) | `ce3e3a8e9d0a3d1368e4928c8225d9a0a3a6bbe3b62d881e78e2d80856cf0e3d` |
| `emit_kuranishi_map.py` (tree and Box02/Box03/r6d) | `1d6dbd671e6652592d9de76a74c86034f8f2e9177703c3410c8a05e533963edf` |
| `fresh_block.json.gz` | `f7f473c5781f610dd0f96112981e8f3b3c7757467d42b7c465a3dfde5c80e8af` |
| linear-window parent | `fb4f16d808dfba754582fb1b5fe10dfa0e69bca0888b38f92586e1f5534724e2` |

The emitter and the block compiler both `assert` the parent SHA `b16912cd…` before `exec`. V1 asserts the independent compiler SHA `46019958…`. The independent compiler asserts the linear-window parent `fb4f16d8…`. Byte identity holds between the live tree, `AWS_BOX02_FRESH_BLOCK/`, and the three Kuranishi `SOURCE.sha256` lists.

Dimensions, from the frozen parent result and from V1/block/map metadata, with tautological rank-nullity:

```text
stages at 3^6..3^{10}: family 55,81,99,116,133
active / spectator split: 17 + 116 = 133
spectator rank in fresh cokernel: 38, kernel 116-38 = 78
fresh operator: 299 x 149, rank 94, kernel 149-94 = 55, cokernel 299-94 = 205
complete chart: 17 + 78 + 55 = 150
predecessor chart: 17 + 78 = 95
```

Combinatorial residual inventory is unchanged from the parent review: `10·11/2 = 55` P-monomials, `13·14/2 = 91` Q-monomials, three `H` digits, `55+91+3 = 149`; determinant ambient `23·24/2 = 276`; top forms `10+13 = 23`; total 299 rows. The 146 map coordinates are the `allowed` `(P≤9,Q≤12)` slice of the D12 `91+91` box, in the same total-degree-then-`x`-power order that `emit_kuranishi_map.py` writes as `support_p` then `support_q`.

---

## Charge 2 — source/valuation constancy; rank 29, kernel 26, quotient 176

**CONFIRMED**

`compile_fresh_block.py` builds `A_fresh` by finite difference of the projected next carry along the 55 stored fresh-kernel directions at the origin of the 150-chart, with a twice-control of affinity in each direction. It does not loop over the 95 predecessor coordinates. That is the correct compilation of a *constant* block only if the block is source-constant. It is.

Write a family point in values-coordinates as

```text
v = v_pred(a,s) + 3^5 (fresh_particular(a,s) + K f),
```

so coefficients move by `243 v = 3^5 v`. After the `GL(133,Z)` split, active directions are visible modulo 3 and spectator directions vanish modulo 3. Coefficient orders are therefore

```text
active predecessor     :  3^5
spectator predecessor  :  3^6
final fresh-kernel     :  3^5 · 3^5 = 3^{10}.
```

The integer residual `F` is polynomial in those coefficients.

**Determinant (bilinear).** A predecessor increment `ΔC_pred = O(3^5)` changes the Jacobian linearly by `O(3^5)`. Pairing that change with a fresh-kernel increment `ΔC_fresh = O(3^{10})` produces a cross term of order `3^{15}`. After division by `3^{11}` the cross term is `O(3^4)` and vanishes modulo 3. The pure fresh-fresh bilinear is `O(3^{20})`. The `F_3` fresh Jacobian itself depends only on `C mod 3`, which is the shared B9 parent, so the 55 kernel directions are likewise family-constant.

**Common-core, `H^3` (10 rows).** `H = y^3 + 3^4 ĥ` with `ĥ = (1+3 v_{146}) x y^2 + 3 v_{147} x^2 y + 3 v_{148} x^3`. Then

```text
H^3 = y^9 + 3^5 y^6 ĥ + 3^9 y^3 ĥ^2 + 3^{12} ĥ^3.
```

The `i=0` row `P_{(0,9)} - P_{(0,9)} · 1` is identically zero. For `i≥1` the `H^3` coefficients begin at order `3^5`. Differentiating in a fresh-kernel `H`-digit gives `3 H^2 ΔH` with `ΔH = O(3^{10})`, hence order `3^{11}` at leading term, as required for a `3^{11}`-divisible increment. Predecessor motion of `H` is `O(3^5)` in coefficients (the parent `81` is fixed; it is not a family parameter), so the mixed derivative is again `O(3^{15})`.

**Common-core, `H^4` (13 rows).** Expanding `(y^3 + 81 x y^2)^4` produces a parent term `4·81 x y^{11} = 324 x y^{11}` of order `3^4`. That term is constant on the whole family. Predecessor deformations of `H` still begin at `3^5`, and

```text
H^4 = y^{12} + 324 x y^{11} + O(3^5).
```

The mixed increment `12 H^2 ΔH_pred ΔH_fresh` is `O(3^{16})` after the explicit factor `12=4·3`. After `/3^{11}` it vanishes modulo 3. Kernel membership of `K` supplies the extra `3` that makes the *linear* fresh increment divisible by `3^{11}` rather than only `3^{10}`; that extra `3` is the parent-level Jacobian condition, hence is likewise predecessor-independent.

The next Jacobian at order `3^{11}` (values-increment `3^6`, coefficient increment `3^{11}`) is family-constant for the same reason: it depends on `C mod 3`. Computing `next_matrix` at the first carry-zero control `basis_4_2`, as V1 does, therefore supplies the same 205-dimensional left cokernel as at the origin. The block compiler’s use of that cokernel is licensed.

Independent RREF of the frozen gzip:

```text
rank A_fresh            = 29
dim ker A_fresh         = 26   (equals the stored kernel, as a set of 55-vectors)
dim ker A_fresh^T       = 176  (equals the stored left quotient, as a set of 205-vectors)
fresh_left · A_fresh    = 0
rank next_left (205x299)= 205
rank (fresh_left · next_left) = 176
support histogram       = {1:154, 2:12, 3:5, 4:2, 5:2, 6:1}
zero rows in the 176x299 composition: none
all entries in {0,1,2}
```

The 447 elimination records all store matrix SHA-256 `9b1ae5b0…`, rank 29, and `consistent_after_fresh_elimination = false`. That is a sampled identity of one matrix and 447 inconsistent right-hand sides. It is not the constancy proof, and it is not emptiness of `K`.

---

## Charge 3 — `emit_kuranishi_map.py` versus the integer residual

**CONFIRMED**

The emitter `exec`s the pinned V1 chart, then rebuilds `F` as a 20-bit residue DAG. Against `independent_common_core.residual` and `replay.py:jac`:

- **RREF / `17+78` chart.** `rref_transform` is the same first-nonzero, scale-to-1, eliminate algorithm as V1 `fixed_solver`. It recovers spectator pivots/kernel `38/78` and fresh pivots/kernel `94/55`, and asserts equality with the parent kernels. Active inputs are 17 trits; spectators are the 78-dimensional RREF kernel; the 55 final fresh-kernel parameters are passed as the empty list to `symbolic_solve`. Scope is exactly 95 declared names `a_0..a_16`, `s_0..s_77`, each bounded `bvult _ bv3 2`.
- **276+23 rows.** `slots` is the parent D12 ambient (276). Jacobian accumulation is `factor = i·ℓ - j·k` at bidegree `(i+k-1, j+ℓ-1)`, which is `P_x Q_y - P_y Q_x` with integer derivatives, matching `jac`. `H` is `[1, 81+243 v_{146}, 243 v_{147}, 243 v_{148}]`. Homogeneous convolution of the 4-tuple implements `(y^3 + h_1 x y^2 + h_2 x^2 y + h_3 x^3)^{3,4}`. Top-form rows are `P_{(i,9-i)} - P_{(0,9)} (H^3)_i` and `Q_{(i,12-i)} - Q_{(0,12)} (H^4)_i`. Assert `len(rows)==299`.
- **Signs and chronological divisors.** Fresh right-hand side is `-F/3^{10}`; next right-hand side is `-F/3^{11}`; both use `fneg = ×2 (mod 3)`. The SMT contains 299 divisibility asserts by `(_ bv59049 20)` (`3^{10}`) on predecessor rows and 299 by `(_ bv177147 20)` (`3^{11}`) on final rows, plus 205 spectator equations and 299 fresh-particular equations. Two-bit zero-asserts total `205+299+176 = 680`.
- **Modulus `3^{12}=531441`.** `cm` reduces Python integers into `{0,…,531440}` before emission. `madd`/`mmul` take 20-bit residues, zero-extend to 40 bits, reduce by `(_ bv531441 40)`, and extract 19:0. Unreduced product of two residues is at most `531440^2 = 282429673600 < 2^{40}`. Sums are far smaller. `mneg` special-cases 0 so the unreduced constant `531441` is never used as a residue. `(_ bv531441 20)` appears in the three definitions `madd`, `mmul`, `mneg` and is never passed through `value % MODULUS`. There is no `bvurem` by `(_ bv0 20)`. This is the V2 zero-divisor bug, not repeated.
- **Composition `176 ∘ 205`.** `combined = fresh_left · next_left` over `F_3`, then `κ_i = combined_i · next_rhs`. Independent RREF of the stored matrices confirms rank 176 and the asserted support histogram. The hard-coded histogram assert in the emitter is a fingerprint of that composition.
- **Zeroing the 55 fibre.** `fresh_left · A_fresh = 0`, so `κ` is invariant along the 55-dimensional fibre. The circuit may evaluate at `f=0` without cutting the locus. If `κ=0`, some `f` makes the 205-obstruction vanish, and the rank-94 next Jacobian then supplies a 55-dimensional affine space of next digits `u`. The producer’s wording that this is “not a choice of a representative asserted to lift” is exact.
- **Embedded controls.** Divisibility of all 299 predecessor rows by `3^{10}` and of all 299 final rows by `3^{11}`; reconstruction of the 205 spectator equations and of the 299-row fresh particular; trit bounds; no extra map coordinates.

The `correction`/`allowed` embedding of the 146 map digits is the identity on `support_p ∥ support_q` with P-degree `10..12` held at zero. Direct monomial assignment in the circuit therefore matches the integer residual.

Degree firewall: the emitter records that canonical `bvudiv`/`bvurem` carry gates need not preserve ordinary `F_3` ANF degree. No quadratic/quartic ANF bound is claimed.

Non-blocking structural note: the 176 composed rows are linearly independent as forms on the 299 residual, but the recursive DAG hashes of the 176 `κ`-nodes take only 111 distinct values, with one node repeated on the consecutive block of coordinates `96..161`. That is circuit CSE of distinct linear forms once they are restricted to the image of `next_rhs` on the 95-chart. It does not change the zero locus of `K` and does not reduce the linear-algebra quotient dimension 176.

---

## Charge 4 — AWS row-block metadata

**CONFIRMED**

Every Kuranishi `result.json` on Box02, Box03, and r6d stores the same pinned hashes `b16912cd…` (V1) and `f7f473c5…` (gzip). The three `SOURCE.sha256` files additionally pin the emitter `1d6dbd67…` and the parent compiler `46019958…`. Job tags share the prefix `as_b9_common_cubic_kuranishi_map_20260825T185653Z_` with host suffixes `_box02`, `_box03`, `_r6d`.

Coverage and overlaps, checked against the Box02 full 176-row hash list and against each block’s stored `coordinate_hashes`:

| Host | Block | Rows | Overlap partners |
|---|---|---|---|
| Box02 | `b000_032` | 0..31 | Box03 at 30--31 |
| Box03 | `b030_062` | 30..61 | r6d at 60--61 |
| r6d | `b060_092` | 60..91 | Box02 at 90--91 |
| Box02 | `b090_122` | 90..121 | Box03 at 120--121 |
| Box03 | `b120_152` | 120..151 | r6d at 150--151 |
| r6d | `b150_176` | 150..175 | — |
| Box02 | `full_000_176` | 0..175 | all of the above |

Rows `0..175` are covered with empty complement. Each specified overlap pair agrees byte-for-byte, including the duplicate-hash pair `120--121` and `150--151`. Every block, and the Box02 aggregate, stores

```text
all_coordinate_hashes_sha256 =
  557123112e5c3e4ea5d3a5a95709d816254080e0eeef2d995d028013db468b48
```

Independently recomputing SHA-256 of the canonical JSON list of 176 hashes reproduces that digest. The full formula is 2,024,323 bytes, SMT SHA-256 `108cfdaae0c897ab66518e18d5e38d0969a1f8f936eeb488fd9144e4fbfe0f4c`, matching the stored `smt_sha256`, the freeze line, and the aggregate. DAG node count is 34,555 on every block. Arithmetic modulus 531441 and chronological divisors `[59049, 177147]` are stored and match the SMT header. Wall times are 11.7--12.1 s, RSS 67--70 MiB, exit status 0, Linux `/usr/bin/time -v` on all seven emission jobs.

`FREEZE.sha256` (10 lines) and `MANIFEST.sha256` (189 lines) were rehashed: every freeze line matches, and every manifest line matches. Aggregate result SHA-256 `351f2049…` matches the freeze.

---

## Charge 5 — solver layer kept separate

**CONFIRMED**

The producer, the Kuranishi preregistration, the emitter `refusal_scope`, and the aggregate `refusal_scope` all refuse to promote a SAT model without integer reconstruction of the eliminated fresh fibre, a 149-digit next solve, and literal replay of all 299 rows modulo `3^{12}`, and refuse to promote an UNSAT solver return without an independently checked proof or finite-field certificate. This freeze contains neither object.

The 447 controls (origin, 190 signed basis vectors of the 95-chart, 256 seeded mixed points) are recorded as rank-29 / SAT-count-0. The producer states, and this review repeats: they do not classify the zero locus of `K`. Origin already has a 31-sparse nonzero projected right-hand side, so `K` is not the zero map; that is the most that sampling licenses.

Boolector 1.5.118 rejecting SMT-LIB `define-fun` is a parser negative control. Any Z3 4.16 race is declared outside the freeze. `solve_kuranishi_z3.py` is an AWS-only endpoint for one pinned formula; it is not a certificate.

No all-depth lifting, nonexistence, maximum-12, counterexample, or JC2 statement is licensed. The finite chart `K=0` is the next object, not a restatement of the one-point `[x^2 y^2]` obstruction.

---

## Independently recomputed hashes

| Object | SHA-256 |
|---|---|
| producer note | `524a56ddfc04a7990f009e8fe781c0b1df694771c747bb40f396490f8eaac94f` |
| this review’s prompt | `9648d5110ad5bcfeda3b70510d395b309ea7e08149feb069713810e9218f752f` |
| independent compiler | `460199584e128bc2c5f3196871a34437ebdfd7d674ccf0bcc2f52b9db8ace6b8` |
| V1 global chart | `b16912cd1b6146a35736e9bb872d96bfa640e1bb920e04b7c5a9e13256d12a3f` |
| fresh-block compiler | `ce3e3a8e9d0a3d1368e4928c8225d9a0a3a6bbe3b62d881e78e2d80856cf0e3d` |
| map emitter | `1d6dbd671e6652592d9de76a74c86034f8f2e9177703c3410c8a05e533963edf` |
| aggregate script | `4b31bce21743a7e5a236f480f4e089fe83216656f33b36a7177f560657eb5480` |
| fresh-elimination script | `8951a907473f7195398e0f3c7f915e0867a4784a97a317d54be924544cbea713` |
| `A_fresh` JSON | `9b1ae5b0f64bb3d7fccd27f7d8a3d2cae141c297fd531fd6fff1c302a48fb7d5` |
| quotient payload uncompressed | `6b972339a1ad402229fc03b878a8ae80f2620c1441e4103226613ee6241b6946` |
| `fresh_block.json.gz` | `f7f473c5781f610dd0f96112981e8f3b3c7757467d42b7c465a3dfde5c80e8af` |
| fresh-block `result.json` | `266092010e0617483763b6025b1571907649b4aa71cfe6a7af23962acf947ffa` |
| all-coordinate structural hash | `557123112e5c3e4ea5d3a5a95709d816254080e0eeef2d995d028013db468b48` |
| full formula `map.smt2` | `108cfdaae0c897ab66518e18d5e38d0969a1f8f936eeb488fd9144e4fbfe0f4c` |
| aggregate `result.json` | `351f2049b11adc1e4cbe30911f989dd817eba7bac00f0add46af469757790293` |
| ordered 447-record stream | `c066603aca9e2c432a96ff6f0a6f513a11dfd91b326feaaf6491b709fca15dfe` |
| `MANIFEST.sha256` (189 lines, all match) | `d64c69c43a21d0163920c47b24ef04be18fa00c6155f72c11d301b5453b2ea1f` |
| `FREEZE.sha256` (10 lines, all match) | `5f7a9e713fb06c46d02b6e108c2aeda2d86382e8d975a767a8499144fa53a9db` |
| linear-window parent | `fb4f16d808dfba754582fb1b5fe10dfa0e69bca0888b38f92586e1f5534724e2` |
| B9 W5 replay | `f1b50bb2c3e21369da205ebcf1ba028eede20c89d5ad863253fdfec4d6d28c5d` |
| parent independent result | `fad73f36b609363f0ee8cde84f9ffd89233913ec9e036b00441ee11de5e8307f` |
| parent empty ANF | `2a65d00367451476f31941426f086de0fef53bc0b73478e4eb9fa87fb2cf913e` |

---

## Software / custody notes (non-blocking)

- This review did not re-run `residual`, `canonical_family_point`, or the QF_BV emitter. Independent residual reconstruction of the 299-row family remains the parent Box02 compiler plus its already-confirmed review. Linear algebra here is of the frozen gzip and of stored metadata.
- Box02/Box03/r6d are three hosts running one emitter against one gzip. They are dual/triple custody of the circuit construction, not a second 299-row algorithm.
- `compile_fresh_block.py` evaluates `A_fresh` only at the origin. The missing predecessor loop is not a defect once Charge 2 is granted; it would have been a defect without that valuation.
- Sixty-six consecutive `κ`-nodes share one DAG digest. Report 176 as the left-quotient dimension, not as 176 distinct circuit functions on the 95-chart.
- V1’s 557-point `[x^2 y^2]` diagnostic, including the inconsistent next gate at `basis_4_2`, is a one-row sample. It is not this reduction theorem and is not used as one.

## Exact defects or missing premises

None on the provisional producer theorem as written. The following premises remain missing for any stronger statement, and the producer does not claim them:

1. a SAT model of `K` together with integer reconstruction of `f`, the next 149 digits, and a 299-row replay modulo `3^{12}`;
2. an independently checked UNSAT proof or exact finite-field certificate that `K` has empty zero locus;
3. any lift past `3^{12}`, any inverse-limit point, any characteristic-zero identification, any maximum-twelve theorem, any counterexample, or JC2.
