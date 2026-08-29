# Hostile review: V22R1 first weighted K00 stratum

| Field | Value |
|---|---|
| Charged case | `cases/max12_812_order2_u2_62_k00_weighted_first_stratum_v22_20260827/` |
| Charged claim | On the valuation-one, `k10(0)!=0` prefix, the first honest weighted contracted K10 equation is `kappa*F10(x)=0` at grade six; `D(F10)` is excluded and the closed homogeneous stratum `V(Q1,...,Q6,F10)` remains, with affine dimension three |
| Overall verdict | **PASS** |
| Scope of PASS | first honest weighted prefix at grade six only |
| Smallest failing identity | none |
| Repairs required of the algebra | none |
| Additive custody notes | (1) V22's own 12-line R1 freeze does not contain `TARGET_K6` / `TARGET_K2` / `CONTRACTED_TARGET`; the K6 exclusion at grade six was typed from the cited V18/V20 frozen polynomials, not from V22 harvest alone. (2) Producer `RESULT.json` still labels V20R2/V21R1 provisional; this review does not inherit those PASS markers. |
| Reviewer / model | Grok 4.6 (xAI) |
| Tools | Python 3.14.6 (Clang 16.0.0 / clang-1600.0.26.6); independent recursive-descent parser (no `ast`, no producer modules); Singular 4.4.1 (44105, 64-bit, 2025-11-11) with GMP 6.3.0, NTL 11.6.0, FLINT 3.6.0, monomial orders `lp` and `dp`; Homebrew `sha256sum` |
| Method | Independent SHA-256 of every freeze and all 14 evidence entries; complete R0/R1 compiler diff; independent parse of the six unloaded rows; independent reconstruction of the 66-generator K10 image and target from charged V21/V18 bytes; independent replay of every D3-lift entry and every D4 dual pairing, including annihilation of all 603 truncated generators; independent Gröbner bases of `T` and `L` over `Q` in `lp` (this host) and `dp` (this host vs AWS x86); independent min-degree census of the V20 contracted target and V18 `TARGET_K6`/`TARGET_K2`/`IMAGE_K*` |
| Temporary replay | `/tmp/jc2-v22r1-hostile/` (outside the producer tree; no producer file, ledger, or `jc2-lean` path was written) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` (producer directory is untracked) |
| Date | 2026-08-27 |

No producer `PASS` marker, `RESULT.json` integer, serialized Gröbner basis, or prose sentence is evidence. Every identity below was re-derived from frozen bytes on this host. Canonical ledgers, `jc2-lean`, and every file other than this review were left untouched.

---

## Line-item verdicts

| # | Required attack | Verdict |
|---|---|---|
| 0 | Rehash freeze and all 14 evidence entries; manifest excludes itself; complete R0/R1 diff | **PASS** |
| 1 | Parse unloaded rows; `Q1..Q5` nonzero, `Q6=0`; fire both mutations | **PASS** |
| 2 | Reconstruct 66-generator K10 image/target; replay complete D3 lift; residual vanishes through degree 3; re-emit `F10` | **PASS** (byte-identical) |
| 3 | Replay D4 dual coefficientwise; annihilate every truncated generator; pair as `25/45056`; sign and coefficient mutations | **PASS** |
| 4 | Independent `T=(Q1,...,Q6)` and `L=(Q1,...,Q6,F10)` over `Q`; `F10` nonzero mod `T`; `L` proper; affine dim 3; projective nonemptiness | **PASS** (`lp` and `dp`, arm64 ≠ AWS x86) |
| 5 | Type-check honest weighting; first contracted K10 equation is `kappa*F10(x)=0` at grade six; rule out K6/K2/mu2/mu4/mu6/Jdet and syzygy-representative cancellation | **PASS** (K6 exclusion uses cited V18/V20 frozen polynomials; see §5) |
| 6 | Reject inflations; smallest exact theorem and both-outcome scope | **PASS** (scope held) |

**Overall: PASS.**

---

## Smallest proved statement

Let `R=Q[d0,...,d5]` and let `r1,...,r6` be the six unloaded rows of the frozen V21 prelude

```text
5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a.
```

Write a valuation-one coefficient prefix and a unit `k10` prefix

```text
d_i = Lambda * x_i + O(Lambda^2),    k10 = kappa + O(Lambda),    kappa != 0
```

in the normalized unloaded K00 chart `C6=1`. Let `Q_i` be the homogeneous degree-two part of `r_i`. Independently, `Q1,...,Q5` are nonzero and `Q6` is the zero polynomial (`r6` has order three). Let `T=(Q1,...,Q6)` in `Q[x0,...,x5]`.

Let `E_K10` be the frozen 66-generator K10 filtered image and `D_K10` the frozen K10 target (V21 `image_K10.txt` / `target_K10.txt`, byte-identical to the V18 artifacts of the same names). The complete V18 D3 lift (10 rational entries on the frozen 101-column D3 map) subtracts from `D_K10` to a residual of order exactly four. Its homogeneous degree-four part `F10` is the 30-term quartic independently re-emitted with SHA-256

```text
c8e214ae21b058dddb063dcd7a9075a34b02a14f01f54386822cf85f0dc2c8e8,
```

byte-identical to the charged serialization. The frozen D4 dual annihilates all 603 truncated generators of `(r1,...,r6)+E_K10` through degree four and pairs with `F10` as exactly `25/45056`. Hence `F10` is a well-defined nonzero class in the D4 filtered cokernel, and in particular `F10 ∉ T`.

Under the honest weights of the V20 contracted design,

```text
p = (Lambda^2 k10, Lambda^6 k6, Lambda^10 k2,
     Lambda^14 mu2, Lambda^16 mu4, Lambda^18 mu6, Lambda^19 Jdet),
```

the scalar contracted target is `D_p = p10 D_K10 + p6 D_K6 + p2 D_K2 + ...`. Independently, every `p2`, `mu2`, `mu4`, `mu6`, and `Jdet` summand has weighted grade at least 12 on this prefix. The `p6` summand has `d`-order two, hence weighted grade at least 8. The `p10` summand has `d`-order three; the complete D3 lift cancels that polynomial identity through degree three, leaving

```text
p10 * residual(d) = kappa * F10(x) * Lambda^6 + O(Lambda^7).
```

A change of the complete six-row syzygy representative subtracts a `Gamma_p(s)`. The K10 component of `Gamma` has `d`-order at least 3, so it contributes at grades ≥5 and is already accounted for by the D3 lift; its degree-four remainder is annihilated by the D4 dual. The K6/K2/mu/Jdet components of `Gamma` have weighted grades ≥8. Therefore the first canonical contracted K10 equation on this prefix is

```text
kappa * F10(x) = 0     at weighted grade 6.
```

Because `kappa` is a unit, the open set `D(F10)` is excluded. Exact Gröbner bases of `L=(Q1,...,Q6,F10)` over `Q`, computed on this host in both `lp` and `dp`, give that `L` is proper and `dim Q[x0,...,x5]/L = 3`. The generators of `L` are homogeneous, so `V(L)` is a cone. A proper homogeneous ideal of affine Krull dimension at least one has nonempty projectivization over an algebraic closure (the affine cone is not `{0}`). Affine dimension three therefore yields a nonempty projective closed prefix stratum of projective dimension two.

This is only the grade-six equation on the valuation-one, `k10(0)!=0` prefix. It does not decide the closed `F10=0` branch beyond grade six, grades 7–19, another coefficient valuation, a finite full jet, an arc, K00 closure incidence, order two, maximum twelve, or JC2.

---

## 0. Freeze, evidence, chronology, R0/R1 delta

### 0.1 Charged hashes

All nine charged hashes reproduce exactly from disk bytes:

```text
1b4ae1199e7e2e88fa56c9a8c4d5a48e853af5fa67b75766b0a30c1aa0353180  PREREGISTRATION.md
1bbabb2aeb9385756e2ac1edf0ec075a613920fb939122826307e9bd3f7caf78  PREREGISTRATION_R1.md
677f6451fc126ef1b44998619436d11e9a2ca1c567ba3fd4dba0be2c01d4d0ad  FAILURE_R0.md
19c5a44190f685438240fc418fe0a99e419abf71c8d055133e3f14fb05a7751b  SOURCE_FREEZE_R1.sha256
23ad457b06c42073ddf64b2162b8458d412315d104fb61995d1eacf6b1855a81  compile_weighted_first_stratum_v22.py
494075c5675a2571808aec8606ed5744c2362bf3abc470304226b6fee699e293  RESULT_V22R1.md
920c31841cd96ea4cbac0172f14923b209c3e2a3d00ad8a264299ff592bdd9c4  aws_r6b_r1_pass/output/RESULT.json
99d6b1e6274a30cbffdae87a72e8a42011fe2059a499684c6ac1f28774512ad9  aws_r6b_r1_pass/EVIDENCE.sha256
c8e214ae21b058dddb063dcd7a9075a34b02a14f01f54386822cf85f0dc2c8e8  aws_r6b_r1_pass/output/F10_QUARTIC.txt
```

R1 source-freeze contents: **12/12 OK** against live bytes, including the seven V21/V18 K10 pins.

R0 source-freeze contents: **10/10 OK**, with the R0 compiler pinned at `aws_r6b_r0_failed/source/compile_weighted_first_stratum_v22.py` SHA-256 `9515d3a95eec7fe28d00149d3567a6029725256674a8df050b1b9ddbbdc61cf4`. The live R1 compiler is different, as required.

### 0.2 Evidence manifest

`aws_r6b_r1_pass/EVIDENCE.sha256` has **exactly 14 entries**. Remapping the AWS prefix

```text
/home/ubuntu/jobs/max12_812_order2_u2_62_k00_weighted_first_stratum_v22r1_20260827T130220Z_r6b/
```

onto `aws_r6b_r1_pass/` yields **14/14 OK**. The harvested tree's fifteenth file is `EVIDENCE.sha256` itself; it is not listed. The empty `singular.stderr` hashes to the SHA-256 of empty bytes `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

### 0.3 Chronology

```text
R0  ...v22_20260827T125930Z_r6b     PID 59589   start 12:59:43Z  rc=1  wall 1.49 s   RSS 41,728 KiB   swap 0
R1  ...v22r1_20260827T130220Z_r6b   PID 60717   start 13:02:40Z  rc=0  wall 1.47 s   RSS 35,512 KiB   swap 0
```

R1 follows R0 by lane timestamp and PID. R0 created no `output/` directory, wrote empty `compiler.stdout`, and died in Python before Singular. Its `compiler.stderr` hashes to `4e96a9f0919b0fd9b92c54305a6983f9e8ef9ce5659118ea92b887dde026343f`, matching `FAILURE_R0.md`. The failure string is `RuntimeError: missing unloaded quadratic initial`. R0 is a pre-algebra source-profile failure, permanently nonpromotable.

### 0.4 Complete R0/R1 compiler diff

The unified diff of the frozen R0 compiler against the live R1 compiler contains exactly four hunks, and nothing else:

1. **Preregistration gate.** `PREREG_R1` is added to `EXPECTED` with hash `1bbabb2a…`.
2. **Predicate.** `any(not quad for quad in quadrics)` / `"missing unloaded quadratic initial"` is replaced by `valid_quadratic_profile`, which is `len==6` and `Q1..Q5` nonempty and `Q6` empty.
3. **Two mutations.** A nonzero quadratic is written onto `Q6` and must fail the predicate; `Q1` is zeroed and must fail the predicate.
4. **Audit flags.** `Q6_nonzero_profile_mutation_detected` and `Q1_zero_profile_mutation_detected` are added to `EXTRACTION_AUDIT.json`.

The wrapper `run_weighted_first_stratum_v22_aws.sh` is byte-identical in the R0 and R1 freezes (`b9fea33e…`). Extraction, D3-lift replay, D4-dual pairing, Singular question, branch criterion, resource caps, firewall, and allowed outcomes are unchanged. This is exactly the charged R1 repair, not a silent widening.

---

## 1. Attack 1 — unloaded quadratic profile

The six rows were parsed from `prelude_Q.sing` by a recursive-descent grammar written for this review (integer and rational atoms, `+ - * / ^`, parentheses; `/` only by a nonzero constant). Producer `ast.parse` was not used.

| row | terms | order | max deg | constant | quadratic terms |
|---|---|---|---|---|---|
| `r1` | 16 | 2 | 4 | 0 | 8 |
| `r2` | 23 | 2 | 4 | 0 | 11 |
| `r3` | 27 | 2 | 5 | 0 | 9 |
| `r4` | 36 | 2 | 5 | 0 | 12 |
| `r5` | 40 | 2 | 5 | 0 | 8 |
| `r6` | 42 | 3 | 6 | 0 | 0 |

`Q_i` is the homogeneous degree-two part of `r_i`. Independently, `Q1,...,Q5` are nonzero and `Q6` is the empty polynomial — not a cancellation of quadratic terms, but an order-three row. The independent `Q_i` are coefficientwise equal to the charged `UNLOADED_QUADRATIC_INITIALS.txt`.

Mutations, all detected:

- `Q6 := x0^2` makes `valid_quadratic_profile` false.
- Zeroing each of `Q1,...,Q5` in turn makes `valid_quadratic_profile` false (five independent checks; the producer only zeros `Q1`).

The R0 predicate `all six quadrics nonzero` is false on this source, which is why R0 died before algebra. R1's predicate matches the frozen profile.

---

## 2. Attack 2 — K10 image, D3 lift, independent `F10`

V21 `image_K10.txt` (SHA-256 `9f37ef3f…`) splits into **exactly 66** polynomials. Independently: 65 have order 3, one has order 4, none is zero. The file is **byte-identical** to V18 `run/artifacts/IMAGE_K10.txt`. V21 `target_K10.txt` is **byte-identical** to V18 `run/artifacts/TARGET_K10.txt`: 79 terms, order 3, max degree 7, with degree census `(3:27, 4:30, 5:17, 6:4, 7:1)`.

Generators are the six rows plus the 66 image polynomials (72 total). The frozen D3 column map has 101 columns; independently regenerating columns by the filtered rule

```text
for each generator g of order m <= 3:
    all monomial multipliers of degree 0, ..., 3-m
```

in total-degree-then-recursive-lex order is not required at D3 for the lift replay (the frozen 101-column map is used), and is confirmed at D4 (see §3).

The D3 certificate has **10** nonzero `x`-entries. Each contribution `c_j * g_{i_j} * monomial_j` was formed over `Q` and subtracted from `D_K10`:

```text
residual = D_K10 - combination,     order(residual) = 4,     52 terms.
```

No term of total degree ≤ 3 remains. The homogeneous degree-four part has 30 terms. Independently serialized with the same monomial sort and coefficient grammar as the producer, it is **byte-identical** to `F10_QUARTIC.txt` and hashes to `c8e214ae…`. Coefficientwise equality was also checked by dictionary identity over `Q`, so the byte match is not an artifact of serialization.

The 22 residual terms of degree ≥ 5 are the polynomial tail; after `d = Lambda x + O(Lambda^2)` they contribute only at grade ≥ 7.

Sign mutation: `D_K10 + combination` has order 3. Lift-coefficient mutation: incrementing the first lift entry by `1` produces a residual of order 3. Both mutations fail closed, as required.

---

## 3. Attack 3 — D4 dual

The frozen D4 row map is the 210 monomials of total degree ≤ 4 in six variables, in the independent total-degree-then-recursive-lex order constructed for this review. It matches `rows_K10_D4.json` entrywise.

The dual has 37 rational `y`-entries. Independently:

```text
<y, F10> = 25/45056
<y, (D_K10 truncated to degree 4)> = 25/45056
```

The two pairings agree because the D3-lift combination is in the dual's annihilator. This is the same rational as V18's `certificate_dot` / `target_pairing`.

Independent D4 columns, reconstructed from generator orders by the filtered rule through cutoff 4, number **603** and are **entrywise equal** to frozen `columns_K10_D4.json`. For every one of those 603 columns the truncated generator (product of generator by multiplier, degree ≤ 4) pairs with `y` as `0`. Annihilation is therefore a coefficientwise identity on the complete truncated module, not a pairing against `F10` alone.

Mutations:

- Dual sign: `<-y, F10> = -25/45056`, detected.
- Dual coefficient: the first dual entry that actually meets `F10` is row 85, monomial `x4 x5^3`, dual value `8`, `F10` coefficient `90165/65536`. Incrementing that entry by `1` yields pairing `992215/720896 ≠ 25/45056`, detected.
- D3 lift coefficient, already in §2, also breaks the residual and therefore the pairing.

The first dual dictionary key (row 11) does not meet `F10`; mutating it would leave the `F10` pairing unchanged. That is why the mutation was taken on a supporting degree-four row, not on `next(iter(dual))`.

---

## 4. Attack 4 — independent `T` and `L` over `Q`

On this arm64-Darwin host, Singular 4.4.1 was run off-tree on independently emitted polynomials, in two orders.

| order | `T` proper | `F10` nonzero mod `T` | `L` proper | `dim T` | `dim L` |
|---|---|---|---|---|---|
| `lp` (lex) | yes | yes | yes | 4 | 3 |
| `dp` (grevlex) | yes | yes | yes | 4 | 3 |

The `dp` standard bases of `T` and `L` and the `dp` remainder of `F10` modulo `T` are **byte-identical** to the charged AWS x86 artifacts `TANGENT_STANDARD_BASIS.txt`, `LEADING_STRATUM_STANDARD_BASIS.txt`, and `F10_TANGENT_REMAINDER.txt`. The `lp` bases are different polynomials (47 generators for `L` versus 9) with the same Krull dimensions, which is the independent-order check.

`F10 ∉ T` is therefore not a Singular-`dp` accident. Affine dimension three of `L` is not a leading-term tie-break accident.

`Q_i` and `F10` are homogeneous (degrees 2 and 4). `L` is a homogeneous ideal, so `V(L) ⊂ A^6` is a cone. Singular's `dim` over `Q` is the Krull dimension of `Q[x]/L`, equal to that of `Qbar[x]/L` because the leading-term combinatorics are characteristic-zero. A proper homogeneous ideal with affine dimension 0 has affine cone `{0}` and empty projectivization. Affine dimension 3 ≥ 1 therefore implies that the cone contains a line through the origin, so `Proj Q[x]/L` is nonempty of dimension 2 over an algebraic closure. This is an exact homogeneous-dimension certificate; no finite-field sample point was used.

The producer branch test is `proper && dim >= 1`, which is the correct nonemptiness test. The charged integer is the actual dimension 3, independently reproduced.

---

## 5. Attack 5 — honest weighting, grade six, no cancellation

### 5.1 What V22's own freeze contains

The R1 source freeze pins the six rows, the K10 image/target, and the K10 D3/D4 certificates. It does **not** pin `TARGET_K6`, `TARGET_K2`, `IMAGE_K6`, `IMAGE_K2`, or V20 `CONTRACTED_TARGET.txt`. The weights themselves are in `PREREGISTRATION.md`, which cites the V20 contracted design. The K6 exclusion therefore cannot be typed from the V22 harvest alone. It **can** be typed from the frozen V18/V20 polynomials that the preregistration names as design dependencies. Those files were parsed independently for this section; producer prose was not used.

### 5.2 Contracted target, coefficientwise

V20 `CONTRACTED_TARGET.txt` is a 151-term polynomial, linear in the seven load coordinates. Independently splitting by those coordinates recovers

| component | terms | `d`-order | weight | lowest weighted grade on `d=O(Lambda)` |
|---|---|---|---|---|
| `p10` | 79 | 3 | 2 | 5 |
| `p6` | 41 | 2 | 6 | 8 |
| `p2` | 16 | 2 | 10 | 12 |
| `pmu2` | 7 | 1 | 14 | 15 |
| `pmu4` | 4 | 1 | 16 | 17 |
| `pmu6` | 2 | 1 | 18 | 19 |
| `pJ` | 2 | 0 | 19 | 19 |

The `p10`, `p6`, and `p2` components are coefficientwise equal to V18 `TARGET_K10`, `TARGET_K6`, and `TARGET_K2`. The `pJ` component is `-5 - (63/4) d4`, the constant `-5 = -h(0)/4` of the V20 design. There are no bilinear `p`-terms.

On `d = Lambda x + O(Lambda^2)`:

- `p2`, `mu2`, `mu4`, `mu6`, `Jdet` cannot meet grade 6 even if their `d`-parts were constants. This follows from the weights alone.
- `p6 * TARGET_K6` has `d`-order 2, hence grade ≥ 8. A unit `k6(0)` would not cancel `F10` at grade 6. (V20 additionally restricts `k6[0]=0`, which is not needed here.)
- `p10 * TARGET_K10` has `d`-order 3, hence a raw grade-5 term. That term is a polynomial identity of degree 3. The complete D3 lift cancels it through degree 3 as a polynomial, not merely on the leading ray `d=Lambda x`. After that cancellation the residual has order 4, so

```text
p10 * residual(Lambda x + O(Lambda^2))
  = (Lambda^2 (kappa + O(Lambda))) * (Lambda^4 F10(x) + O(Lambda^5))
  = kappa F10(x) Lambda^6 + O(Lambda^7).
```

The degree-3 pieces of `TARGET_K10` cannot re-enter grade 6 through the `O(Lambda^2)` tails of `d`, because those pieces have already been subtracted as polynomials.

### 5.3 Syzygy-representative change

`Gamma_p(s) = p10 IMAGE_K10(s) + p6 IMAGE_K6(s) + p2 IMAGE_K2(s) + (mu/Jdet components)`. Independently:

- `IMAGE_K10`: 66 generators, min order 3. Times `p10` this is grade ≥ 5, which is the D3-lift range. Degree-four remainders of such a change are truncated D4 generators, annihilated by the dual of §3. The class of `F10` is therefore invariant.
- `IMAGE_K6`: 66 generators, min order 2, none zero. Times `p6` this is grade ≥ 8.
- `IMAGE_K2`: 66 generators, min order 2. Times `p2` this is grade ≥ 12.
- `Gamma`'s mu/Jdet coordinates are `-s2,-s4,-s6,0` with weights 14, 16, 18, 19. Even a degree-zero `s_i` cannot meet grade 6.

No change of the complete six-row representative cancels `kappa F10(x)` at grade 6.

### 5.4 Hardcoded producer grade

`RESULT.json` writes `"weighted_grade": 6` as a Python literal, not as a computed valuation of `D_p`. The grade-six identity above is the independent replacement for that literal.

---

## 6. Attack 6 — rejected inflations, both-outcome scope

Two inflations are false and were not charged.

**`F10` nonzero modulo `T` does not exclude all valuation-one prefixes.** It excludes the open set `D(F10)` on this prefix at grade six. Prefixes with `F10(x)=0` remain live. That is the closed stratum `V(L)`, which is nonempty.

**`dim L = 3` does not produce a `Lambda <= 19` jet or an arc.** It is a statement about the homogeneous leading ideal in six coefficient variables. Grades 7–19 of the contracted source, the cubic-and-higher unloaded row conditions, other load axes, Fitting/constructible decomposition of `V(L)`, jet existence, arc existence, and closure incidence are all uncomputed.

Allowed producer outcomes were `M1_STRATUM_EMPTY_FORCES_HIGHER_VALUATION` and `M1_STRATUM_NONEMPTY_REMAINS` (plus resource/source failures). The algebra returns the second. The first would have been the correct recording if `L` had been the unit ideal or of affine dimension 0.

`RESULT_V22R1.md` and `RESULT.json` firewall strings match this scope. The producer dependency line still says V20R2/V21R1 are provisional pending hostile review. That is a custody label, not an algebraic widening. This review does not promote V20 or V21 and does not read their PASS markers as inputs.

---

## Scope firewall (binding)

The only conclusion authorized by this PASS is:

> At grade six on the valuation-one, `k10(0)!=0` prefix, the open set `D(F10)` is excluded and the closed homogeneous stratum `V(Q1,...,Q6,F10)` remains, with affine dimension three.

Not authorized: grades 7–19, a full finite jet, an arc, K00 closure incidence, order two, maximum twelve, JC2, emptiness of `V(L)` in any finer constructible piece, or any statement about other coefficient valuations.

---

## Reviewer controls

- Parser: recursive descent over `Q`, independent of `ast` and of `compile_weighted_first_stratum_v22.py`.
- Arithmetic: Python `fractions.Fraction`.
- Gröbner: Singular 4.4.1, orders `lp` and `dp`, arm64-Darwin; producer ran Singular `dp` on AWS x86-64. The `dp` bases and remainder are byte-identical across that architecture change.
- Mutations fired: nonzero `Q6`; zero `Q1` through `Q5`; D3 lift sign; D3 lift coefficient; D4 dual sign; D4 dual coefficient on an `F10`-supported row.
- Replay staging: `/tmp/jc2-v22r1-hostile/`. Producer tree, canonical ledgers, and `jc2-lean` were not written.
