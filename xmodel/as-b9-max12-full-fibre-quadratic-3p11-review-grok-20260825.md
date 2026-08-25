# Hostile different-model review — B9 first quadratic full-family gate at `3^11`

| Field | Value |
|---|---|
| Producer | `xmodel/as-b9-max12-full-fibre-quadratic-3p11-producer-20260825.md` (SHA-256 `2992772c950199f3282e1a18abfcf147c168444614091cfd3cfab47ea71038d7`) |
| Frozen case | `cases/as_b9_max12_full_fibre_quadratic_3p11_20260825/` |
| Parent solver | `cases/as_b9_max12_full_fibre_linear_window_20260825/solve_linear_window.py` (SHA-256 `0bf4766d8e4840fb89661eaba6b8cb4661b554c7f8944f5eb55bac37298f2ac7`) |
| Overall verdict | **CONFIRMED** |
| Mathematics | **CONFIRMED** |
| Source typing | **CONFIRMED** |
| Software | **CONFIRMED** (non-blocking notes below) |
| Custody | **CONFIRMED** of the frozen dual-AWS V4 run. Box02 and Box03 are two executions of one implementation, not two implementations |
| Wording / scope | **CONFIRMED** of the licensed finite-set claim. Solver and “183-file closure” sentences are non-blocking colour |
| Mathematical defects | none |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Evidence | source audit of the quadratic compiler and of the hash-pinned parent chain; independent SHA-256 of freeze/manifest/result/ANF/SMT; independent combinatorial counts `91+91=182` and `276`; independent degree reading of the stored supports modulo `177147`; no local compiler, CAS, or Jacobian replay |
| Git HEAD | `d0f6edfbfcd8fbe4c77ffadcd336df349c11eb7e` (producer, this case, the linear-window case, and the mod-729 case uncommitted) |
| Review window | 2026-08-25 |

## Verdict

**CONFIRMED**

Over one fixed B9 mod-243 parent, the complete fixed-D12 affine family of `3^165` predecessor digit-tuples at modulus `3^10` has a complete quadratic transition to modulus `3^11=177147`. After the outer `243` predivision already stored in `base_integer` and `matrix_integer`, the remaining exact divisor of the linear carry is `3^5`, and the first nonlinear term is `det J(T)`. The fresh operator is `276\times 182` of rank `108`; an invertible change of the `165` predecessor coordinates splits them into `18` directions visible modulo three and `147` spectators of rank `56` in the `168`-dimensional left cokernel. Coefficientwise containment of the full constant/linear/quadratic span (raw rank `16`) in that spectator image leaves **zero** reduced equations. The displayed parameterization therefore has exactly `3^109` liftable predecessors and `3^74` fresh lifts each, cardinality `3^183` as an `F_3`-digit count. One zero-active witness replays all `276` integer determinant coefficients modulo `177147` on AWS, with honest degree pairs `(12,12)`. This is not a scheme theorem, not a mod-`3^12` result, and not a `(9,12)` lift.

## Strongest exact claim

Fix the displayed B9 point `(p5,q5)` of source SHA-256 `f1b50bb2c3e21369da205ebcf1ba028eede20c89d5ad863253fdfec4d6d28c5d`, determinant one modulo `243`. Let `T` run through the complete `165`-parameter fixed-D12 family produced by the linear-window solver at modulus `3^10`, and write

```text
F = F5 + 243 T + 3^10 W,
```

with `W` an unrestricted `182`-digit D12 correction. The integer identity

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

On this congruence, after eliminating `W` by the rank-`108` left cokernel and eliminating the `147` spectators of rank `56`, every active assignment in `F_3^18` lifts. The displayed `F_3`-digit parameterization of solutions has cardinality `3^109` on the predecessor projection and `3^183` after adjoining the `74`-dimensional fresh kernel. One explicit point, the zero active assignment with a `16`-nonzero spectator particular and a `46`-nonzero fresh particular, has `det J(P,Q)-1` vanishing on all `276` slots modulo `177147`, with actual partial-`y` and total-degree pairs both `(12,12)` at that modulus.

## Sharpest non-claim

A finite-depth parameterized count over **one** B9 mod-243 parent and **one** consumed `3^10` D12 family. Not the complete earlier mod-243 fibre, not a mod-`3^12` or inverse-limit/`Z_3` point, not a characteristic-zero map, not a maximum-twelve theorem, not a `(9,12)` normalized lift, not a scheme-theoretic fibre dimension, not a counterexample, and not JC2. Z3 and Boolector do not re-prove the elimination. Box02 and Box03 do not supply a second implementation.

---

## Evidence layers (do not collapse)

1. **Source/compiler correctness.** The quadratic compiler, the linear-window parent, the mod-729 parent, and the W5 B9 replay were read. The divided equation, the `/243` then `/3^5` arithmetic, the `GL(165,Z)` coordinate change, the left-cokernel construction, the char-3 polarization (squares stored as `det J(d_i)`, crosses as the polar `B` for `i<j` only), and the coefficientwise containment test are correct as written. Rank arithmetic `18+147=165`, `108+168=276`, `108+74=182`, `56+91=147`, `18+91=109`, `109+74=183` is tautological given those ranks.
2. **Two source-identical host replays.** Box02 V4 and Box03 V4 executed the same 85-path SOURCE_CLOSURE (SHA-256 `caba10f799ccd0f82d31b5d085d4b82818ce613af643ee18aa560ee508b92e51`) and emitted byte-identical `result.json`, `compiler.stdout`, ANF, SMT, and parent replay. Distinct `/usr/bin/time -v` RSS `26880` / `28032` KiB and distinct `compiler.stderr` hashes show two processes. This is custody that the audited source ran, not a second mathematical solution.
3. **Solver agreement on the already eliminated formula.** After containment, the reduced ANF is empty and the SMT is eighteen `(_ BitVec 4)` variables with `bvule · #x2` and no equation asserts. Z3 4.16 and Boolector both return the all-zero model of that bound-only problem. That agrees with the finder, which tried the zero active vector first and stopped. It does not corroborate ranks `18`, `56`, `108`, nor the `276`-row integer identity.

No local compiler, Jacobian, or SAT replay was launched. Substantive compilation remains the frozen AWS V4 jobs `as_b9_d12_quadratic_3p11_20260825T1720Z_v4_box02` and `…_box03`.

---

## Charge 1 — Transitive source hashes and the `3^10 → 3^11` divided equation

**CONFIRMED**

Independently recomputed SHA-256:

| Object | SHA-256 |
|---|---|
| `replay.py` (B9 mod-243, W5 **CONFIRMED**) | `f1b50bb2c3e21369da205ebcf1ba028eede20c89d5ad863253fdfec4d6d28c5d` |
| `solve_full_output_mod729.py` | `4deb7fe07acef4f37bb14735493b0d20b6c7ac66bb10633f81b7bc1a48264bd4` |
| `solve_linear_window.py` (quadratic `EXPECTED_PARENT`) | `0bf4766d8e4840fb89661eaba6b8cb4661b554c7f8944f5eb55bac37298f2ac7` |
| `compile_quadratic_3p11.py` | `2a55f0d25328f4f443916c24764f1c7cd7436772353aece84c6284d8fa711c1e` |
| parent linear-window `result.json` (also this job’s `parent_linear_window_replay.json`) | `6a2145187e5697890e9838bfb6370505329c01e905abd060310f8b73cd606168` |
| quadratic `result.json` (both boxes) | `7a1b5da26974ee5e5f4fb42ade1575abc0b18d9de54349c8fdcc08ab4a267379` |
| ANF | `60f645cf7d03100eed6d56c7269a2138a628a498d105bae492acd6ab8b64575f` |
| canonical SMT | `616f406a35ef99e3d6540d4321787be1dc8153af4c6810a64c4ccf59aaf4ecfc` |
| Boolector v3 SMT (canonical minus `set-option` and `get-model`) | `98bf803a3e6eed52229d5f231ac43e2c1e1c0e40c29c9457b50f658c87ad2d88` |
| producer report | `2992772c950199f3282e1a18abfcf147c168444614091cfd3cfab47ea71038d7` |
| this review’s prompt | `7bb055a49f68cb9b4b3229e069b8fdd7a95e84289a05eaa8e1cb386e1583fd21` |
| `MANIFEST.sha256` | `63dd90dad1fca9e39e301605c2a41bdbea83196126643a70a9a8eff3e703e660` |

Every FREEZE and MANIFEST line recomputes. The quadratic job re-execs the linear-window solver in-process and records the same parent result SHA as the frozen linear-window dual-AWS run.

The Jacobian of a sum is bilinear. With `F = F5 + 243 T + 3^10 W`,

```text
det J(F) - 1
  = D5 + 243 B(F5, T) + 3^10 det J(T)
    + 3^10 B(F5, W) + 3^15 B(T, W) + 3^20 det J(W).
```

Modulo `3^11` the last two summands vanish, and `B(F5, W) ≡ A3 W (mod 3)` after division by `3^10`. The parent stores `base_integer = D5/243` and `matrix_integer` as the exact divided columns of `jac(F5+243 e_j)-d5`. Each standard basis vector `e_j` is pure-P or pure-Q, so `det J(e_j)=0` and those columns are exactly `B(F5, e_j)` plus a `243`-multiple that is invisible modulo three. Therefore

```text
(D5 + 243 A T)/3^10 = (base_integer + matrix_integer T)/3^5
```

once `T` lies on the `3^10` family (so the numerator is divisible by `3^10`, hence the stored numerator by `3^5`). The stored divisor is `3^5=243` **because** the arrays have already been divided by the outer `243=3^5`; using `3^10` on those arrays would be an off-by-five error. The quadratic `243^2 det J(T)=3^10 det J(T)` is zero through modulus `3^10` and first appears, after division by `3^10`, in this gate. The compiler’s `power = 3**5` comment matches the algebra. No `3^10`/`3^5` interchange is being made.

The linear-window hostile review is still pending. Charge 1 confirms the hashes and the divided-equation typing of this gate; it does not replace a different-model review of the five-stage rank table that produced the `165` directions.

## Charge 2 — Completeness of 165, 182, 276

**CONFIRMED**

Independently: monomials of total degree `≤ 12` in two variables number `1+2+…+13 = 91`. Two coordinates give `182` fresh digits. The determinant of two degree-`12` maps has total degree at most `22`, and `1+2+…+23 = 276`. The mod-729 parent writes exactly

```text
support = [(i, d-i) for d in range(13) for i in range(d+1)]   # 91
slots   = [(i, d-i) for d in range(23) for i in range(d+1)]   # 276
```

and `correction` splits an `182`-vector into those two copies. The quadratic compiler consumes `support`, `slots`, `A3`, `base_integer`, `matrix_integer`, `base_T`, and `directions` from that chain, asserts `len(old_directions)==165`, and never drops a column or a slot. Nil ambient rows are preserved, as preregistered.

The integer `165` is the parent’s stage-5 affine kernel (`147` prior directions plus `182` fresh, combined rank `164`, kernel `329-164=165`). Parent dual-AWS stdout records

```text
stage 5 59049 164 165 91
```

and `final_solution_exponent=165`. This package uses **all** of those `165` directions. Completeness here is consumption of the pinned family, not a second derivation that the family is every mod-`3^10` solution. A later reject of the linear-window table would punch through the cardinalities, not through the D12 inventory.

## Charge 3 — Invertibility of the active/spectator change and ranks 18, 56, 108

**CONFIRMED**

The compiler greedily extracts an `F_3`-basis of the images of the `165` directions modulo three (`18` pivots), then replaces every dependent direction `d` by `d - ∑ λ_j p_j` with `λ_j ∈ {0,1,2}`, asserting the remainder is `0 mod 3`. Ordering pivots first, the change-of-basis matrix on the `165` direction module is a permutation times a unipotent integer matrix, hence lies in `GL(165,Z)`. The `Z`-span of the family is preserved; every old digit tuple has a unique new `(active, spectator)` representative. Over `F_3` the `147` new spectators vanish, and the `18` active directions remain independent by the explicit rank assert on their reductions.

Numerical ranks are AWS Gaussian elimination of the audited `rref_solve`, not a second engine:

- **108.** Column rank of `A3` (`276×182`). Parent stage 1, on `A3` itself, already reported rank `108` and kernel `74`. This compiler recomputes rank of `A3^T` and asserts `fresh_rank==108` and left-kernel length `168=276-108`. Row rank versus column rank of one matrix in one RREF is a consistency check, not a second implementation. Kernel `74=182-108` is then forced.
- **18.** Rank of the `165` directions modulo three. Reported as `active_quadratic_dimension`. Only this compiler computes it; both hosts print `active_inactive 18 147`.
- **56.** Rank of the `147` spectator columns acting on the `168`-dimensional cokernel. Kernel `91=147-56`. Both hosts print `spectator_rank_reduced_equations 56 0`.

The values `18` and `56` are therefore certified as “what this source computed twice,” with the invertibility and the rank-arithmetic consequences audited independently. Dense matrices are not serialized; an independent re-RREF from payload is impossible by design.

## Charge 4 — Fresh left cokernel and coefficientwise containment

**CONFIRMED**

`fresh_left_kernel` is the RREF kernel of `A3^T`, dimension `168`. Projecting the divided carry plus `det J(T)` onto that kernel eliminates `W`. The remaining polynomial in the `18` active digits, with values in `F_3^168`, has monomials `{1} ∪ {a_i} ∪ {a_i^2} ∪ {a_i a_j : i<j}` — `1+18+18+153=190` coefficient vectors, matching the BV design size.

Polarization is correct in characteristic three. The compiler stores square coefficients as `det J(d_i)` and off-diagonal coefficients as the polar `B(d_i,d_j)` for `i<j` only. It does not use `B(d_i,d_i)/2`. Spectator–active and spectator–spectator quadratics vanish modulo three because spectator directions are `0 mod 3`. Degree `≤ 2` polynomials inject into functions `F_3^{18} → F_3` (`a_i^3-a_i` starts at degree three), so coefficientwise containment is functional containment.

Reported: raw coefficient span rank `16`; adjoining those `190` vectors to the `56` spectator columns leaves rank `56`; `all_polynomial_coefficients_in_spectator_image=true` is written only after `assert containment_augmented_rank == inactive_rank`. Equivalently, the further left kernel of the spectator map (`112=168-56` functionals) kills every reduced coefficient, `keep=[]`, `post_elimination_equation_count=0`, `quadratic_cross_support_count=0`. Two equivalent certificates of the same identity: the quadratic map `F_3^{18} → F_3^{168}/im(spectators)` is the zero polynomial.

This is a full polynomial identity on the `18` active digits, not a sample of `3^18` points. The finder records a single SAT at trial `0` (the zero assignment) and does not enumerate.

## Charge 5 — Cardinalities `3^109` and `3^183`

**CONFIRMED** as finite-set `F_3`-digit counts of the displayed parameterization. **REFUSED** as a scheme, global, or geometric-point theorem.

Given zero reduced equations, every one of the `3^18` active assignments is admissible. For each, the spectator linear equation has rank `56` on `147` digits, so `3^{91}` spectator solutions. Predecessor projection `18+91=109`. Fresh kernel `74`. Total exponent `109+74=183`. The JSON field `full_lift_family_dimension` is computed from those ranks and equals `183`; the string `full_lift_family_cardinality: "3^183"` is a literal, not an f-string, but it matches the computed exponent in this run.

What is counted is the set of `F_3`-digit tuples `(active, spectator-kernel, fresh-kernel)` in the displayed coordinates. That is the cardinality of the compiler’s parameterization of the consumed `3^10` family. It is not Krull dimension, not a statement that the fibre scheme over `Z/3^{11}` is smooth of relative dimension `183`, not a count of distinct polynomial pairs up to a separately proved injection into maps modulo `177147`, and not coverage of the earlier mod-243 fibre. The producer body’s “displayed mod-`3^11` solution set” and the README’s “complete displayed lift family” are licensed at that finite-set strength; any global reading is refused.

## Charge 6 — Integer replay modulo `177147`, degree pairs `(12,12)`, solvers

**CONFIRMED** for the AWS integer replay of the audited `full_replay`, and for the independently reread degree pairs. Solvers **CONFIRMED** only as agreement on the already empty formula.

`full_replay` reconstructs `T` from `(active, spectator)`, solves `A3 W ≡ -residual (mod 3)`, builds `P=p5+243 T_P+3^{10} W_P` and likewise `Q`, and asserts every `slots` coefficient of `det J(P,Q)-1` is divisible by `3^{11}`. Both hosts record `literal_integer_replay_mod177147_passed` after that assert, with determinant payload SHA-256 `6c0156ef3a1305bc3532d3cc9506f28e710f6d69150453ce51ab341595953324`. This review did not recompute that Jacobian.

Independently, from the stored supports, reducing coefficients modulo `177147`:

| | terms stored | alive mod `177147` | partial `y` | total degree | `(0,12)` residue |
|---|---:|---:|---:|---:|---:|
| `P` | 48 | 47 | 12 | 12 | `27702` |
| `Q` | 60 | 60 | 12 | 12 | `156736` |

No alive term has `y`-degree or total degree `> 12`. The one dropped `P` term is `(5,3)` with coefficient `-885735 = -5·3^{11}`, valuation exactly `11`, so it is correctly invisible at the target and would appear only at `3^{12}`. `P_{(0,12)}` and `Q_{(0,12)}` are nonzero modulo `177147`, as is `P_{(1,11)}=3^{10}`. Honest pairs are `(12,12)` and `(12,12)`. This is a D12 object; it is not a `(9,12)` lift. The W5 parent is `(9,12)` at modulus `243`; the extra face is the gate.

Witness coordinates independently counted: active `18` zeros; inactive `147` with **16** nonzero digits; fresh `182` with **46** nonzero digits. Matches the producer.

The emitted SMT is eighteen bounded variables and `check-sat`. The `190`-point BV-versus-ANF design is `1+36+C(18,2)=190` as claimed, but with `equation_count=0` both evaluators return the empty list, so the assert is vacuous. It does not test overflow wrapping. Z3 4.16 (`z3_4_16/bin/z3`, rc `0`, `sat`, all `a_i=#x0`) and Boolector (`boolector -m` on the custody transform, rc `10` which is Boolector SAT, all `a_i=0000`) agree on that tautology. `model_crosscheck.stdout` records `PASS-MODELS-ACTIVE-ZERO-MATCH-LITERAL-WITNESS` for `18` variables each. Parser failures (`set-option` on Box02 `solver_model`, `get-model` on Boolector v2, Box03 `solver_model` rc `127`) are correctly filed as environment controls, not mathematics.

## Charge 7 — V2/V3 negative controls and one-parent/full-D12 refusal

**CONFIRMED**

- **V2** (`NEGATIVE_V2_BOX02/`, SOURCE_CLOSURE `a8311c2a…`, rc `1`): `KeyError: 'dydeg'`. The V2 compiler asked the linear-window namespace for `dydeg`/`tdeg`; those helpers live on the W5 replay and are not re-exported. V4 defines `dydeg_mod`/`tdeg_mod` locally. Deployment/source-scope failure, not a mathematical counterexample.
- **V3** (`NEGATIVE_V3_BOX02/`, SOURCE_CLOSURE `0a11021a…`, rc `1`): `assert partial_y_degree_pair == (9, 12)` raises `AssertionError` inside `full_replay`. The stored traceback is the partial-`y` assertion only. The producer’s extra “(11,12)” is prose for the earlier linear-window degree pair, not a second line in the V3 log. The control still does what is needed: it refuses to freeze a false `(9,12)` lift and forced the honest `(12,12)` measurement.
- V1 is correctly not the producer (missing degree and containment fields).
- Refusal lists in preregistration, README, producer, and `result.json` agree: one displayed B9 mod-243 parent; full D12 (not the `(9,12)` box); `3^10 → 3^11` only; not the complete earlier mod-243 fibre; not mod-`3^{12}` / all-depth / characteristic zero / maximum-twelve / counterexample / JC2.

---

## Mathematical defects

None.

## Terminology, custody, or exposition defects (non-blocking)

1. Producer sentence “pinned 183-file source closure” is false as a file count. The stored `SOURCE_CLOSURE.sha256` hashes **85** paths (53 unique hashes) along the W5 → mod-729 → linear-window → quadratic chain. `183` is the family exponent. Dual-host identity of that 85-path list still holds.
2. The `190`-point BV encoding check is vacuously `[]==[]` at zero equations. The producer’s overflow-reduction language does not apply to an empty gate list.
3. “Z3 4.16 and Boolector both returned the all-zero active model” is true and easy. It is agreement on the already eliminated formula, not independent evidence of containment or of the `276`-row identity.
4. `full_lift_family_cardinality` is a hardcoded `"3^183"` rather than a format of `full_lift_family_dimension`. They match in this run; they could desync.
5. Boolean JSON flags (`all_polynomial_coefficients_in_spectator_image`, `literal_integer_replay_mod177147_passed`, `bv_encoding_crosscheck_passed`) are written `True` after asserts. The load-bearing objects are the asserts, the empty ANF, the stored supports, and rc `0`.
6. Job tag `T1720Z` versus recorded start/end `2026-08-25T16:44:43Z`–`16:44:59Z` on both boxes. Empty `launcher.stdout`/`launcher.stderr`. Two-host identity is carried by result/stdout/ANF/SMT and by distinct `time -v` fields, not by the tag.
7. Dense Bockstein / cokernel matrices are not serialized. Independent re-RREF of ranks `18` and `56` from payload is impossible; those two numbers live in layer 2.

None of these changes an identity or licenses a broader claim.

## Promotion

**Accept `OVER THE DISPLAYED B9 MOD-243 PARENT, THE COMPLETE FIXED-D12 165-PARAMETER FAMILY AT MODULUS 3^10 HAS A COMPLETE QUADRATIC TRANSITION TO MODULUS 3^11. AFTER THE STORED OUTER 243 PREDIVISION THE REMAINING LINEAR DIVISOR IS 3^5, AND THE FIRST NONLINEAR TERM IS det J(T). THE FRESH 276×182 OPERATOR HAS RANK 108; THE 165 PREDECESSOR COORDINATES CHANGE INVERTIBLY INTO 18 ACTIVE DIRECTIONS AND 147 SPECTATORS OF RANK 56 IN THE 168-DIMENSIONAL LEFT COKERNEL; COEFFICIENTWISE CONTAINMENT OF THE RANK-16 QUADRATIC SPAN IN THAT IMAGE LEAVES ZERO REDUCED EQUATIONS. THE DISPLAYED F_3-DIGIT PARAMETERIZATION HAS CARDINALITY 3^109 ON THE PREDECESSOR PROJECTION AND 3^183 AFTER THE 74-DIMENSIONAL FRESH KERNEL. ONE ZERO-ACTIVE WITNESS REPLAYS ALL 276 INTEGER DETERMINANT COEFFICIENTS MODULO 177147 WITH HONEST DEGREE PAIRS (12,12).`**

**Refuse `COMPLETE EARLIER MOD-243 FIBRE`, `MODULUS 3^12`, `ALL-DEPTH / INVERSE LIMIT / Z_3`, `CHARACTERISTIC-ZERO POINT`, `MAXIMUM-TWELVE THEOREM`, `NORMALIZED (9,12) LIFT`, `SCHEME / GLOBAL FIBRE DIMENSION`, `COUNTEREXAMPLE`, and `JC2`. Refuse treating Box02/Box03 identity, or Z3/Boolector SAT on the empty SMT, as a second mathematical solution.**
