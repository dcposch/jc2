# Hostile different-model review — normalized B9 first quadratic full-family gate at `3^11`

| Field | Value |
|---|---|
| Producer | `xmodel/as-b9-9-12-full-fibre-quadratic-3p11-producer-20260825.md` (SHA-256 `0b4d7a586e3d749d7716a3e56b3461357ee5a3522031d3ac5c39c575e257ca31`) |
| Frozen case | `cases/as_b9_9_12_full_fibre_quadratic_3p11_20260825/` |
| Parent solver | `cases/as_b9_9_12_full_fibre_linear_window_20260825/solve_linear_window_9_12.py` (SHA-256 `fb4f16d808dfba754582fb1b5fe10dfa0e69bca0888b38f92586e1f5534724e2`) |
| Overall verdict | **CONFIRMED** |
| Mathematics | **CONFIRMED** |
| Source typing | **CONFIRMED** |
| Software | **CONFIRMED** (non-blocking notes below) |
| Custody | **CONFIRMED** of the frozen dual-AWS run. Box02 and Box03 are two executions of one implementation, not two implementations |
| Wording / scope | **CONFIRMED** of the licensed finite-set claim. “Measured modulo the target” overstates the compiler’s unreduced `tdeg`/`dydeg` call; the residue claim is independently true |
| Mathematical defects | none |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Evidence | source audit of the quadratic compiler and of the hash-pinned parent chain; independent SHA-256 of freeze/manifest/result/ANF/SMT/closure; independent combinatorial counts `55+91=146` and `276`; independent rank-nullity of the stored parent stage table; independent face-coefficient argument for degree pairs `(9,12)` modulo `177147`; no local compiler, CAS, or Jacobian replay |
| Git HEAD | `d0f6edfbfcd8fbe4c77ffadcd336df349c11eb7e` (producer, this case, the linear-window case, and the mod-729 case uncommitted) |
| Review window | 2026-08-25 |

## Verdict

**CONFIRMED**

Over one fixed B9 mod-243 parent, the complete normalized coefficient family with `deg(P)<=9` and `deg(Q)<=12` of `3^145` predecessor digit-tuples at modulus `3^10` has a complete quadratic transition to modulus `3^11=177147`. After the outer `243` predivision already stored in `base_integer` and `matrix_integer`, the remaining exact divisor of the linear carry is `3^5`, and the first nonlinear term is `det J(T)`. The fresh operator is `276×146` of rank `85`; an invertible change of the `145` predecessor coordinates splits them into `17` directions visible modulo three and `128` spectators of rank `44` in the `191`-dimensional left cokernel. Coefficientwise containment of the full constant/linear/quadratic span (raw rank `15`) in that spectator image leaves **zero** reduced equations. The displayed parameterization therefore has exactly `3^101` liftable predecessors and `3^61` fresh lifts each, cardinality `3^162` as an `F_3`-digit count. One zero-active witness replays all `276` integer determinant coefficients modulo `177147` on AWS, with honest degree pairs `(9,12)`. This is not a scheme theorem, not a mod-`3^12` result, and not coverage of the earlier mod-243 fibre.

## Strongest exact claim

Fix the displayed B9 point `(p5,q5)` of source SHA-256 `f1b50bb2c3e21369da205ebcf1ba028eede20c89d5ad863253fdfec4d6d28c5d`, determinant one modulo `243`. Let `T` run through the complete `145`-parameter normalized `(9,12)` family produced by the linear-window solver at modulus `3^10`, and write

```text
F = F5 + 243 T + 3^10 W,
```

with `W` an unrestricted `146`-digit `(9,12)`-box correction. The integer identity

```text
det J(F5 + 243 T) - 1 = D5 + 243 A T + 3^10 det J(T)
```

makes every family through modulus `3^10` linear. The first divided carry to modulus `3^11` is the quadratic congruence

```text
(D5 + 243 A T)/3^10 + det J(T) + A W ≡ 0  (mod 3),
```

equivalently, after the stored `/243` predivision of `D5` and `A`,

```text
(base_integer + matrix_integer T)/3^5 + det J(T) + A W ≡ 0  (mod 3).
```

On this congruence, after eliminating `W` by the rank-`85` left cokernel and eliminating the `128` spectators of rank `44`, every active assignment in `F_3^17` lifts. The displayed `F_3`-digit parameterization of solutions has cardinality `3^101` on the predecessor projection and `3^162` after adjoining the `61`-dimensional fresh kernel. One explicit point, the zero active assignment with a `10`-nonzero spectator particular and a `33`-nonzero fresh particular, has `det J(P,Q)-1` vanishing on all `276` slots modulo `177147`, with actual partial-`y` and total-degree pairs both `(9,12)` at that modulus.

## Sharpest non-claim

A finite-depth parameterized count over **one** B9 mod-243 parent and **one** consumed `3^10` normalized `(9,12)` family. Not the complete earlier mod-243 fibre, not a mod-`3^12` or inverse-limit/`Z_3` point, not a characteristic-zero map, not a maximum-twelve theorem, not a common-cubic landing, not a scheme-theoretic fibre dimension, not a counterexample, and not JC2. The empty SMT is not an independent elimination proof. Box02 and Box03 do not supply a second implementation.

---

## Evidence layers (do not collapse)

1. **Source/compiler correctness.** The quadratic compiler, the `(9,12)` linear-window parent, the `(9,12)` mod-729 restriction, the D12 mod-729 parent, and the W5 B9 replay were read. The divided equation, the `/243` then `/3^5` arithmetic, the `GL(145,Z)` coordinate change, the left-cokernel construction, the char-3 polarization (squares stored as `det J(d_i)`, crosses as the polar `B` for `i<j` only), and the coefficientwise containment test are correct as written. Rank arithmetic `17+128=145`, `85+191=276`, `85+61=146`, `44+84=128`, `17+84=101`, `101+61=162` is tautological given those ranks.
2. **Two source-identical host replays.** Box02 and Box03 executed the same 61-path SOURCE_CLOSURE (SHA-256 `b0d8da1b2d313d0c1f9afe8372fbb0a09d5d96e92c64b0e1fc70e8df54d20425`, 42 unique hashes) and emitted byte-identical `result.json`, `compiler.stdout`, ANF, SMT, and parent replay. Distinct `/usr/bin/time -v` RSS `26872` / `27592` KiB and distinct `compiler.stderr` hashes show two processes. This is custody that the audited source ran, not a second mathematical solution.
3. **Empty residual formula.** After containment, the reduced ANF is empty and the SMT is seventeen `(_ BitVec 4)` variables with `bvule · #x2` and no equation asserts. That agrees with the finder, which tried the zero active vector first and stopped. It does not corroborate ranks `17`, `44`, `85`, nor the `276`-row integer identity. This package stores no Z3/Boolector logs.

No local compiler, Jacobian, or SAT replay was launched. Substantive compilation remains the frozen AWS jobs `as_b9_9_12_quadratic_3p11_20260825T1800Z_box02` and `…_box03`.

---

## Charge 1 — Transitive source hashes and the `3^10 → 3^11` divided equation

**CONFIRMED**

Independently recomputed SHA-256:

| Object | SHA-256 |
|---|---|
| `replay.py` (B9 mod-243, W5 **CONFIRMED**) | `f1b50bb2c3e21369da205ebcf1ba028eede20c89d5ad863253fdfec4d6d28c5d` |
| `solve_full_output_mod729.py` | `4deb7fe07acef4f37bb14735493b0d20b6c7ac66bb10633f81b7bc1a48264bd4` |
| `solve_9_12_mod729.py` (normalized restriction) | `d0c6fd4b62350b0d115aefd60846613ca7484dd3e5bdafdcd9339316b944a848` |
| `solve_linear_window_9_12.py` (quadratic `EXPECTED_PARENT`) | `fb4f16d808dfba754582fb1b5fe10dfa0e69bca0888b38f92586e1f5534724e2` |
| `compile_quadratic_9_12.py` | `7a51c772b0df8c900eddd84e4388fe5f3d47e2bb755ef837d17d7cc28debde58` |
| parent linear-window `result.json` (also this job’s `parent_linear_window_replay.json`) | `8c4060e8e48978492e115955af167e11149d6ba18be83ee3c82121834d617667` |
| quadratic `result.json` (both boxes) | `984dbcf57ce181c5f07308f80950b38a9c78174cd9c802c868b46ce337e90539` |
| ANF | `2a65d00367451476f31941426f086de0fef53bc0b73478e4eb9fa87fb2cf913e` |
| SMT | `4868d7e0b88855c6a9f751b3ad42a8a1c4a08694f5ffb76baad1784123ecf8bd` |
| producer report | `0b4d7a586e3d749d7716a3e56b3461357ee5a3522031d3ac5c39c575e257ca31` |
| this review’s prompt | `20f6118ee5744cb2368c34c00671fc35e17d404987abcbaf5e68766df47d9532` |
| `MANIFEST.sha256` | `6b0a0503d1ba2bc45aaf2f4496683eed5a4f3678d677c37da80dfd4688e3dc00` |
| `SOURCE_CLOSURE.sha256` (the 61-path list) | `b0d8da1b2d313d0c1f9afe8372fbb0a09d5d96e92c64b0e1fc70e8df54d20425` |

Every FREEZE line (6 paths) and every MANIFEST line (33 paths) recomputes. Every SOURCE_CLOSURE path (61) recomputes. The quadratic job re-execs the linear-window solver in-process and records the same parent result SHA as the frozen linear-window dual-AWS run; the replay JSON is byte-identical to that frozen `result.json`.

The Jacobian of a sum is bilinear. With `F = F5 + 243 T + 3^10 W`,

```text
det J(F) - 1
  = D5 + 243 B(F5, T) + 3^10 det J(T)
    + 3^10 B(F5, W) + 3^15 B(T, W) + 3^20 det J(W).
```

Modulo `3^11` the last two summands vanish, and `B(F5, W) ≡ A3 W (mod 3)` after division by `3^10`. The parent stores `base_integer = D5/243` and `matrix_integer` as the exact divided columns of `jac(F5+243 e_j)-d5`. Each standard basis vector `e_j` is pure-P or pure-Q, so `det J(e_j)=0` and those columns are exactly `B(F5, e_j)`. Therefore

```text
(D5 + 243 A T)/3^10 = (base_integer + matrix_integer T)/3^5
```

once `T` lies on the `3^10` family (so the numerator is divisible by `3^10`, hence the stored numerator by `3^5`). The stored divisor is `3^5=243` **because** the arrays have already been divided by the outer `243=3^5`; using `3^10` on those arrays would be an off-by-five error. The quadratic `243^2 det J(T)=3^10 det J(T)` is zero through modulus `3^10` and first appears, after division by `3^10`, in this gate. The compiler’s `power = 3**5` comment matches the algebra. No `3^10`/`3^5` interchange is being made.

The parent window’s last linear stage uses `power=3^4` on the same already-divided arrays and lands at modulus `3^10`. The next division of those arrays is `3^5`, which is exactly this gate. Pair controls `55×91=5005` check that mixed P/Q unit sums contribute a quadratic remainder of valuation at least `10`; they are a valuation/additivity check, not a coefficientwise match against an independently computed `243 det J(T)`.

This package consumes the pinned `145`-parameter family. A later reject of the five-stage rank table would punch through the cardinalities, not through the `(9,12)` inventory or the divided-equation typing. Rank-nullity of the stored table is checked in Charge 7.

## Charge 2 — Completeness of 145, 146, 276

**CONFIRMED**

Independently: monomials of total degree `≤ 9` in two variables number `10×11/2 = 55`. Monomials of total degree `≤ 12` number `13×14/2 = 91`. The normalized box is the `55` P-coefficients together with the `91` Q-coefficients, total `146`. The determinant of two degree-`12` maps has total degree at most `22`, and `23×24/2 = 276`. For maps actually in the `(9,12)` box the Jacobian has total degree at most `8+11=19`, so the `276`-row D12 ambient is a complete superset (the extra degree-`20,21,22` rows are identically zero). Nil ambient rows are preserved, as preregistered.

The mod-729 restriction writes

```text
allowed = ([index for index, xy in enumerate(support) if sum(xy) <= 9]
           + [91 + index for index, xy in enumerate(support)
              if sum(xy) <= 12])
assert len(allowed) == 55 + 91 == 146
```

and `support` / `slots` are the D12 enumerations of lengths `91` and `276`. The linear-window `correction` pads a `146`-vector into those `182` D12 slots and never writes a P-monomial of degree `>9` or a Q-monomial of degree `>12`. The quadratic compiler consumes `support`, `slots`, `A3`, `base_integer`, `matrix_integer`, `base_T`, and `directions` from that chain, asserts `len(T_base)==146` and `len(old_directions)==145`, and never drops a column or a slot.

The integer `145` is the parent’s stage-5 affine kernel. Parent dual-AWS stdout records

```text
stage 5 59049 129 145 84
```

and `final_solution_exponent=145`. Rank-nullity on combined columns `(pred_dim + 146)` holds at every stored stage: `146-85=61`, `207-115=92`, `238-127=111`, `257-129=128`, `274-129=145`. Orientation check: at every stage, `kernel_dimension - projection = 61 = 146-85`. This package uses **all** of those `145` directions. Completeness here is consumption of the pinned family, not a second derivation that the family is every mod-`3^10` solution in the box.

## Charge 3 — Invertibility of the active/spectator change and ranks 17, 44, 85

**CONFIRMED**

The compiler greedily extracts an `F_3`-basis of the images of the `145` directions modulo three (`17` pivots), then replaces every dependent direction `d` by `d - ∑ λ_j p_j` with `λ_j ∈ {0,1,2}`, asserting the remainder is `0 mod 3`. Ordering pivots first, the change-of-basis on the `145` direction module is a permutation times an integer matrix with inverse `c_k = a_{dep}`, `b_j = a_{pivot} + ∑ c_k λ_{kj}`, hence lies in `GL(145,Z)`. The `Z`-span of the family is preserved; every old digit tuple has a unique new `(active, spectator)` representative. Over `F_3` the `128` new spectators vanish, and the `17` active directions remain independent by the explicit rank assert on their reductions.

Numerical ranks are AWS Gaussian elimination of the audited `rref_solve`, not a second engine:

- **85.** Column rank of `A3` (`276×146`). Parent stage 1, on `A3` itself, already reported rank `85` and kernel `61` via a distinct `rref_with_left`. This compiler recomputes rank of `A3^T` and records `fresh_rank==85` and left-kernel length `191=276-85`. Row rank versus column rank of one matrix, plus the parent’s first-gate rank on the same `A3`, is a consistency check, not a second mathematical solution. Kernel `61=146-85` is then forced.
- **17.** Rank of the `145` directions modulo three. Reported as `active_quadratic_dimension`. Only this compiler computes it; both hosts print `active_inactive 17 128`.
- **44.** Rank of the `128` spectator columns acting on the `191`-dimensional cokernel. Kernel `84=128-44`. Both hosts print `spectator_rank_equations 44 0`. The same `44` appears as `combined_rank - 85` on the parent’s last two linear stages (`129-85=44`), which is the expected match: spectators are `0 mod 3`, so the next linear carry on spectators is this operator.

The values `17` and `44` are therefore certified as “what this source computed twice,” with the invertibility and the rank-arithmetic consequences audited independently. Dense matrices are not serialized; an independent re-RREF from payload is impossible by design.

## Charge 4 — Fresh left cokernel and coefficientwise containment

**CONFIRMED**

`fresh_left_kernel` is the RREF kernel of `A3^T`, dimension `191`. Projecting the divided carry plus `det J(T)` onto that kernel eliminates `W`. The remaining polynomial in the `17` active digits, with values in `F_3^191`, has monomials `{1} ∪ {a_i} ∪ {a_i^2} ∪ {a_i a_j : i<j}` — `1+17+17+136=171` coefficient vectors. The stored ANF has exactly those `136` pairs `[[0,1],…,[15,16]]`.

Polarization is correct in characteristic three. The compiler stores square coefficients as `det J(d_i)` and off-diagonal coefficients as the polar `B(d_i,d_j)` for `i<j` only. It does not use `B(d_i,d_i)/2`. Spectator–active and spectator–spectator quadratics vanish modulo three because spectator directions are `0 mod 3`. Linear spectator columns carry only the divided affine operator, not a vanished polar. Degree `≤ 2` polynomials inject into functions `F_3^{17} → F_3` (`a_i^3-a_i` starts at degree three), so coefficientwise containment is functional containment.

Reported: raw coefficient span rank `15`; adjoining those `171` vectors to the `44` spectator columns leaves rank `44`; `all_polynomial_coefficients_in_spectator_image=true` is written from `containment_augmented_rank == inactive_rank`. Equivalently, the further left kernel of the spectator map (`147=191-44` functionals) kills every reduced coefficient, `keep=[]`, `post_elimination_equation_count=0`. Two equivalent certificates of the same identity: the quadratic map `F_3^{17} → F_3^{191}/im(spectators)` is the zero polynomial. Both hosts print `coefficient_augmented_rank 15 44` and `spectator_rank_equations 44 0`. The emitted ANF is empty in every slot.

This is a full polynomial identity on the `17` active digits, not a sample of `3^17` points. The finder records a single SAT at trial `0` (the zero assignment) and does not enumerate.

Unlike the D12 sibling compiler, this source does **not** `assert containment_augmented_rank == inactive_rank`. The boolean is a recorded comparison; the load-bearing objects are the empty `keep` list, the printed ranks, and `rc=0`. Non-blocking (Charge 4 still holds).

## Charge 5 — Cardinalities `3^101` and `3^162`

**CONFIRMED** as finite-set `F_3`-digit counts of the displayed parameterization. **REFUSED** as a scheme, global, or geometric-point theorem.

Given zero reduced equations, every one of the `3^17` active assignments is admissible. For each, the spectator linear equation has rank `44` on `128` digits, so `3^{84}` spectator solutions. Predecessor projection `17+84=101`. Fresh kernel `61`. Total exponent `101+61=162`. The JSON field `full_lift_family_dimension_if_residual_zero` is computed from those ranks when `equation_count==0` and equals `162`; it is not a hardcoded cardinality string.

What is counted is the set of `F_3`-digit tuples `(active, spectator-kernel, fresh-kernel)` in the displayed coordinates. That is the cardinality of the compiler’s parameterization of the consumed `3^10` family. It is not Krull dimension, not a statement that the fibre scheme over `Z/3^{11}` is smooth of relative dimension `162`, not a count of distinct polynomial pairs up to a separately proved injection into maps modulo `177147`, and not coverage of the earlier mod-243 fibre. The producer body’s “displayed mod-`3^11` solution set” and the README’s “displayed mod-`3^11` family” are licensed at that finite-set strength; any global reading is refused.

## Charge 6 — Integer replay modulo `177147`, degree pairs `(9,12)`, boxes

**CONFIRMED** for the AWS integer replay of the audited `replay`, for the box inventory by construction, and for the residue degree pairs. The compiler’s own degree call is unreduced; the residue claim does not rest on that call.

`replay` reconstructs `T` from `(active, spectator)`, solves `A3 W ≡ -residual (mod 3)`, builds `P=p5+243 T_P+3^{10} W_P` and likewise `Q`, and asserts every `slots` coefficient of `det J(P,Q)-1` is divisible by `3^{11}`. It also asserts `tdeg(P)<=9`, `dydeg(P)<=9`, `tdeg(Q)<=12`, `dydeg(Q)<=12` on the **unreduced** integer polynomials (W5 `tdeg`/`dydeg`, which inspect `clean` support and do not reduce modulo `177147`). Both hosts record `literal_integer_replay_mod177147_passed` after those asserts, with determinant payload SHA-256 `3dc78ec4fa6f312837b8f6c512ce1625e7842929a37104763c62f905f746e16d` and recorded pairs `(9,12)` / `(9,12)`. This review did not recompute that Jacobian.

No coefficients outside the boxes are possible by construction: `correction` writes only the `55+91` allowed monomials, and `p5` itself lies in the box (`u-u^3` contributes `y^9`; `y+u^4` contributes `y^{12}`; the `18uy`, `81`, and `x y^{11}` digits do not leave it). The quadratic witness does not serialize `P_support`/`Q_support`, so an independent reduced-mod-`177147` degree reading from this payload is impossible. The parent linear-window particular, which is the `T_base` of this gate, **does** serialize supports; independently:

| | terms stored | alive integer | max total | max `y` | outside box |
|---|---:|---:|---:|---:|---|
| parent `P` | 31 | 31 | 9 | 9 | none |
| parent `Q` | 43 | 43 | 12 | 12 | none |

Face coefficients of that particular: `P_{(0,9)}=49085 ≡ 2 (mod 3)`, `Q_{(0,12)}=40825 ≡ 1 (mod 3)`. Stronger and independent of the particular: the W5 source has `p5_{(0,9)}=-1` from `-u^3` and `q5_{(0,12)}=1` from `u^4`. Any `(9,12)`-box correction contributes `243 T + 3^{10} W`, which is `0 mod 3`. Hence

```text
P_{(0,9)} ≡ -1  (mod 3),     Q_{(0,12)} ≡ 1  (mod 3)
```

at every point of this family, including every mod-`3^{11}` lift. Those residues are units, so both monomials survive modulo `177147`. Combined with the box cap, the honest pairs are `(9,12)` and `(9,12)` at the target. This is a normalized `(9,12)` object; it is not a D12 `(12,12)` lift.

Witness coordinates independently counted: active `17` zeros; inactive `128` with **10** nonzero digits; fresh `146` with **33** nonzero digits.

The emitted SMT is seventeen bounded variables and `check-sat`. With `equation_count=0` there are no equation asserts. No solver logs are deposited; none are required for this charge.

## Charge 7 — Parent linear-window replay, dual-host custody, one-parent refusal

**CONFIRMED**

- **Parent replay.** The quadratic compiler hash-pins `solve_linear_window_9_12.py` at `fb4f16d8…`, execs it in-process to `PARENT_REPLAY_JSON`, and records SHA-256 `8c4060e8…`. That file is byte-identical to both frozen linear-window AWS `result.json` copies. The linear-window job itself is dual-host: Box02/Box03 stdout identical, result SHA identical, RSS `22760` / `22956` KiB distinct, jobs `…T1740Z_box02` / `…_box03`, `rc=0`.
- **Parent typing consumed here.** Five consistent stages through modulus `3^{10}`; `pair_control_count=5005`; `quadratic_coefficient_valuation=10`; `quadratic_enters_divided_carry_for_transition=3^10_to_3^11`; refusal of that transition in the parent’s own `refusal_scope`. Rank-nullity and `kernel-projection=61` interlock as in Charge 2. `tdeg`/`dydeg` are re-exported by this parent (the D12 V2 failure mode does not apply).
- **Dual-host custody of this gate.** Box02 start `2026-08-25T17:00:23Z`, Box03 start `2026-08-25T17:00:22Z`, both end `2026-08-25T17:00:27Z`, elapsed `0:04.16` / `0:04.05`, `rc=0`. Load-bearing bytes (result, stdout, ANF, SMT, parent replay, SOURCE_CLOSURE, `compiler.rc`) are identical. `compiler.stderr` hashes differ. Launcher stdout/stderr are the empty-file digest `e3b0c442…`. Dual-host byte equality is deployment evidence, not an independent mathematical vote.
- **Refusal scope.** Preregistration, README, producer, and `result.json` agree: one displayed B9 mod-243 parent; the complete normalized `(9,12)` family at `3^{10}` (not the D12 box, not the complete earlier mod-243 fibre); `3^{10} → 3^{11}` only; not mod-`3^{12}` / all-depth / characteristic zero / common-cubic / maximum-twelve / counterexample / JC2.

There is no separate different-model review file for the `(9,12)` linear window. Charge 7 confirms the hash-pinned replay, the source typing needed by this gate, and the stored stage table’s rank-nullity. It does not replace a standalone promotion of that window’s five-stage claim beyond this consumption.

---

## Mathematical defects

None.

## Terminology, custody, or exposition defects (non-blocking)

1. The compiler measures degree with unreduced W5 `tdeg`/`dydeg`, not a `tdeg_mod(·, 177147)` helper. The producer sentence “Measured modulo the target” overstates that call. The residue pairs `(9,12)` are independently true by the unit face coefficients of `p5`/`q5` and the box cap.
2. Unlike `compile_quadratic_3p11.py`, this compiler does not `assert containment_augmented_rank == inactive_rank`. The boolean is a recorded equality; `keep=[]` and the printed ranks `15 44` / `44 0` are the operational certificates.
3. The quadratic witness does not serialize `P_support`/`Q_support`. Independent reduced-degree reading from this payload is impossible; Charge 6 uses construction plus the parent supports plus the `p5` face.
4. Boolean JSON flags (`all_polynomial_coefficients_in_spectator_image`, `literal_integer_replay_mod177147_passed`) are written `True` after comparison or assert. The load-bearing objects are the asserts, the empty ANF, the stored parent supports, and `rc=0`.
5. Job tag `T1800Z` versus recorded start/end `2026-08-25T17:00:22Z`–`17:00:27Z`. Empty `launcher.stdout`/`launcher.stderr`. Two-host identity is carried by result/stdout/ANF/SMT and by distinct `time -v` fields, not by the tag.
6. Dense Bockstein / cokernel matrices are not serialized. Independent re-RREF of ranks `17` and `44` from payload is impossible; those two numbers live in layer 2.
7. The empty SMT is not an independent vote on containment or on the `276`-row identity. This package correctly does not claim solver agreement.

None of these changes an identity or licenses a broader claim.

## Promotion

**Accept `OVER THE DISPLAYED B9 MOD-243 PARENT, THE COMPLETE NORMALIZED (9,12) 145-PARAMETER FAMILY AT MODULUS 3^10 HAS A COMPLETE QUADRATIC TRANSITION TO MODULUS 3^11. AFTER THE STORED OUTER 243 PREDIVISION THE REMAINING LINEAR DIVISOR IS 3^5, AND THE FIRST NONLINEAR TERM IS det J(T). THE FRESH 276×146 OPERATOR HAS RANK 85; THE 145 PREDECESSOR COORDINATES CHANGE INVERTIBLY INTO 17 ACTIVE DIRECTIONS AND 128 SPECTATORS OF RANK 44 IN THE 191-DIMENSIONAL LEFT COKERNEL; COEFFICIENTWISE CONTAINMENT OF THE RANK-15 QUADRATIC SPAN IN THAT IMAGE LEAVES ZERO REDUCED EQUATIONS. THE DISPLAYED F_3-DIGIT PARAMETERIZATION HAS CARDINALITY 3^101 ON THE PREDECESSOR PROJECTION AND 3^162 AFTER THE 61-DIMENSIONAL FRESH KERNEL. ONE ZERO-ACTIVE WITNESS REPLAYS ALL 276 INTEGER DETERMINANT COEFFICIENTS MODULO 177147 WITH HONEST DEGREE PAIRS (9,12).`**

**Refuse `COMPLETE EARLIER MOD-243 FIBRE`, `MODULUS 3^12`, `ALL-DEPTH / INVERSE LIMIT / Z_3`, `CHARACTERISTIC-ZERO POINT`, `COMMON-CUBIC LANDING`, `MAXIMUM-TWELVE THEOREM`, `SCHEME / GLOBAL FIBRE DIMENSION`, `COUNTEREXAMPLE`, and `JC2`. Refuse treating Box02/Box03 identity, or the empty SMT, as a second mathematical solution.**
