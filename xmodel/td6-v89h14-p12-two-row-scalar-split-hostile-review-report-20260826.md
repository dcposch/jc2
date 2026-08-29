# Hostile review — TD6 V89H14 P12 two-row/six-scalar split

| Field | Value |
|---|---|
| Target | Frozen producer package `cases/td6_c1_c2_c3_allq_mod_f_unitriangular_functional_v89h10_aws_20260826/`; controlling pins `P12_TWO_ROW_SCALAR_RESULT.md`, `P12_TWO_ROW_SCALAR_EVIDENCE.sha256`, `P12_TWO_ROW_SCALAR_FREEZE.sha256`, `PREREGISTRATION_P12_TWO_ROW_SCALAR_SPLIT.md`, `SOURCE_P12_TWO_ROW_SCALAR_SPLIT.sha256`, `source_p12_two_row_scalar_split.tar.gz`, client `replay_v89h14_p12_two_row_scalar_split.py`, V89H12 normal form TSV |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest bad coefficient / denominator / omission | none |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile algebra review. Producer `PASS` banners, dual-host byte identity, and RSS/elapsed lines are custody only |
| Method | SHA-256 of every charged pin and every consumed freeze/source/evidence row; independent flint parse of all 166 V89H12 records as polynomials in `Q[U,V]` (exact vanishing, not string `"0"` and not finite-field sampling); independent rebuild of the 6-by-12 scalar matrix, 6-by-6 minor, and q2 block over `Q`; explicit mixed-low-q rational point at `(U,V)=(1,3)` that kills all 18 E3 coordinates; local replay of the H14 client into `/tmp/td6_v89h14_review/replay_out` (exit 0) producing byte-identical artifacts and stdout. No Singular, Sage, Lean, or `jc2-lean`. The AWS wrapper was not re-run (EC2/Linux gated); the Python client was |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Prompt SHA-256 `09cac7b60155160a67b7ddb0fde5c3c493aa1a0c27da2e448ebaa2afd0b6e68f` matched. Independently recomputed SHA-256 of every required primary pin matches. Every path named in `P12_TWO_ROW_SCALAR_FREEZE.sha256` (10/10), `P12_TWO_ROW_SCALAR_EVIDENCE.sha256` (14/14), and `SOURCE_P12_TWO_ROW_SCALAR_SPLIT.sha256` (6/6) rehashes to the printed digest. Every `SOURCE_P12_TWO_ROW_SCALAR_SPLIT.sha256` row exists at the case root and as a same-named member of `source_p12_two_row_scalar_split.tar.gz`, and both copies match. Producer `TD6-V89H14-P12-TWO-ROW-SCALAR-SPLIT PASS` was not used as algebra. No file other than this review was written. The frozen producer package, campaign ledgers, and `jc2-lean` were not edited.

---

## Verdict

**CONFIRMED.**

On the frozen V89H12 all-q, `F=0`, `D(U*H*B3)` P12/FIRST normal form (166 records, SHA `c8a738b6…`), the exact split is

```text
R(q,y) = c(q) + A(q) y
```

in the 18 E3 coordinates, with `y` the 16 surviving original-FIRST nonpivot labels

```text
6,8,9,11,12,13,15,16,17,18,20,21,22,24,25,27
```

all of which lie in the frozen 94-element nonpivot list. Flint polynomial vanishing on every numerator shows:

- every nonempty-parameter coefficient is supported exactly in coordinates `{0,1}`, and both occur;
- the empty-parameter coefficient is supported exactly in coordinates `{0,1,2,3,4,5,6,7}`, and all eight occur;
- coordinates 8 through 17 are the zero polynomial in every record;
- the six equations in coordinates 2 through 7 are independent of every quotient variable;
- q-support of those six equations is exactly `q3,...,q14`; q2 is absent from the entire empty-parameter class (no `((), (2,))` record among the 166), and `q16,...,q24` are absent from the entire TSV.

The q2 block in rows `(0,1)`, columns `(y24,y27)` is the constant integer matrix `[[6,8],[0,4]]`. Because the normal form is separately of parameter degree one and q degree one, with no mixed-q monomial, the q2-squared coefficient of that 2-by-2 determinant is exactly `6*4-8*0=24` as an element of `Q`, and cannot be cancelled by higher or mixed q terms. Combined with `A(q)` having only two nonzero rows, this is rank exactly two of `A(q)` over the rational function field `Q(U,V,q2,...,q14)`. It is not a global rank statement on `D(U*H*B3)` and not a unit-minor claim.

The 6-by-12 coefficient matrix of the scalar equations in `q3,...,q14`, evaluated at the denominator-safe point `(U,V)=(1,3)` (where `U=1`, `U*H=V^2-4U^3=5`, `B3=V^4=81`), has rank 6 with pivot columns `q3,q4,q5,q6,q7,q9` and exact 6-by-6 determinant

```text
-1656161280873829337287680.
```

That single nonzero evaluation proves the symbolic determinant is a nonzero element of `Q(U,V)`, hence generic rank six over `Q(U,V)`. It supplies no right to invert the minor throughout `D(U*H*B3)`.

Over `Q(U,V)` those six independent equations therefore determine `q3,q4,q5,q6,q7,q9` uniquely in terms of the remaining q variables. q2 does not appear and may remain transcendental. After that substitution the `(y24,y27)` minor remains a degree-2 polynomial in q2 with leading coefficient 24. Localizing at it solves rows 0 and 1 for `y24,y27`; rows 2 through 7 are already zero by the scalar solve; rows 8 through 17 are identically zero. An explicit mixed-low-q point over `Q` at `(U,V)=(1,3)` (q2=1, nonzero `q3,q4,q5,q6`, other listed q zero, `y24,y27` as below, remaining surviving y zero) evaluates the frozen normal form to the 18-zero vector. The pure q2-axis at the same base point does not: coordinates 2 and 3 evaluate to `-72/25` and `18/25`. Mixed low q is essential, so there is no conflict with V89H7.

That section is a P12/FIRST/`F=0` point on the registered open with `q2≠0`. A global certificate `q_ideal ⊂ √(P12,FIRST,F)` after localizing only at `U*H*B3` therefore cannot exist. It is not a literal total-source point, later-CURRENT solution, total-Rees chart, or JC2 counterexample. Later CURRENT grades and source-map conditions remain open.

No Singular qring is used. Arithmetic is Python/`fractions` plus reviewer flint `Q[U,V]`.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 1. Frozen pins | controlling hashes | all eight required pins match |
| 1. Manifests | every named file | freeze 10/10, evidence 14/14, source 6/6; tarball payload copies match |
| 1. Dual AWS | rc, stdout, exact artifacts | both `rc=0`; stdout and all three mathematical outputs byte-identical; stderr differs only in `/usr/bin/time` counters |
| 1. Independent replay | local client | exit 0; three outputs and stdout byte-identical to AWS |
| 1. V89H12 TSV | 166 records | reparsed independently; box02 and r6d copies identical, SHA `c8a738b6…` |
| 2. Support of `A(q)` and `c(q)` | flint exact zero | nonempty-parameter support exactly `{0,1}`; empty-parameter support exactly `{0..7}`; coords 8–17 vanish in every record; string `"0"` is the unique zero-numerator spelling |
| 3. Six scalar equations | y-independent, q3–q14, no q2/high q | holds on the TSV keys themselves; not a client-side drop of a present monomial |
| 4. q2 block and rank of `A` | `[[6,8],[0,4]]`, det leading 24, generic rank 2 | constant integer block; no mixed/higher q; rank exactly two over the function field only |
| 5. 6-by-12 at `(1,3)` | pivots `q3..q7,q9`, det `-1656161280873829337287680` | exact match; nonzero evaluation ⇒ generic rank 6 over `Q(U,V)`, not a unit on `D(U*H*B3)` |
| 6. Rational-section corollary | solve over `Q(U,V)`, q2 transcendental, 24 q2² leading | unique pivot solution over `Q(U,V)`; explicit `Q`-point kills all 18 coordinates; no FIRST-label mismatch |
| 7. Global radical routing | `q_ideal ⊂ √(P12,FIRST,F)` on `D(U*H*B3)` | ruled out by the mixed-low-q point with `q2=1`; not a source/CURRENT/Rees/JC2 object; no conflict with V89H7 |
| 8. qring and scope | no Singular qring; P12/FIRST structure and negative routing only | holds |

---

## 1. Charge 1 — frozen manifests, dual AWS, independent TSV parse

Recomputed SHA-256 of the required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `P12_TWO_ROW_SCALAR_RESULT.md` | `88f4354b7b639d098e91b96e07ffbed1793d5c73aed8cc8014ba2b5996adf2e3` | producer result |
| `P12_TWO_ROW_SCALAR_EVIDENCE.sha256` | `4b19cfa4d518ffbcbccf4fde2dfc21bae435a50a61817e1f7fcb804365a45dec` | evidence manifest |
| `P12_TWO_ROW_SCALAR_FREEZE.sha256` | `0e2aa4a0cb1c0e01b025f2de061cf0d70f093a68654fcc40eccc1929a0d811e7` | freeze |
| `PREREGISTRATION_P12_TWO_ROW_SCALAR_SPLIT.md` | `34338772b99db1616e1f6bf6d860655e58ec67d89136f844cd7eebc7aa4dcdbf` | preregistration |
| `SOURCE_P12_TWO_ROW_SCALAR_SPLIT.sha256` | `1103a905a378d885f607253ae8888d26fcb961d19a08d72b94ab87a4194f0100` | source manifest |
| `source_p12_two_row_scalar_split.tar.gz` | `0a4c6eed75888e72fad759709b608f10de6f859d3dca6e6cdd515ede6076d381` | source archive |
| client `replay_v89h14_p12_two_row_scalar_split.py` | `3c842d74ee9aa4da01e6474970e342d2f15cb1df8db68a1046cbb900234615c7` | controlling replay |
| V89H12 `ALLQ_P12_FULL_NORMAL_FORM.tsv` | `c8a738b6024ac02e56455674efa8c89c37684a87e0312141a5ca4259ca02e4c4` | consumed normal form |

Nested freeze rows, independently rehashed:

| Pin | SHA-256 |
|---|---|
| wrapper `run_v89h14_p12_two_row_scalar_split.sh` | `094f8a12955f1ac45b359939b05bbe5d552fbb380d171f279cbf2c23ee38ed49` |
| parent `P12_FULL_NORMAL_FORM_RESULT.md` | `7004c6359eba808c6f5f66ddd0b72c917fc734c1c3a6eea67878d19859ba23ef` |
| parent `P12_FULL_NORMAL_FORM_FREEZE.sha256` | `c7a146ee89ced521cb23544be6a977413c003b17d0a256a26eda6dae9d435a11` |
| parent `P12_MAXIMAL_MINOR_PILOT_RESULT.md` | `87c3756a947264b0b95ae664ba8eac0c15703a1fe99f2ed4025aaa8d461f8643` |

`source_p12_two_row_scalar_split.tar.gz` contains the six charged source paths plus `SOURCE_P12_TWO_ROW_SCALAR_SPLIT.sha256` itself, together with AppleDouble `._*` sidecar files of common SHA `7b7e703638a2c8654bbaeecc7148e1717958bb825d0f1b13593ac3c3cb748c6c`. Every charged source path is present in the tarball and hash-correct against disk. The AppleDouble members are not mathematical evidence; the same packaging residue was already recorded for V89H12 R3.

Box02 and r6d both have `rc` equal to the two-byte string `0\n` (SHA `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`). Mathematical stdout SHA `166406ccf6140ae4617cd96d9aa8ef3702f19632ae3bef57fe77f919a41d1891` is byte-identical. All three exact output files are byte-identical:

| Output | SHA-256 |
|---|---|
| `P12_SIX_SCALAR_COMPATIBILITY_EQUATIONS.tsv` | `2f888859f6a4f2e383cd43812b3f48e28aa6c1885ff66374f5e458aa138a2e51` |
| `P12_TWO_ROW_SCALAR_SPLIT_RESULT.txt` | `48a3f53722df716affbb36445468293cd7e0a7be5198699f61df13d547088cea` |
| `P12_TWO_ROW_SCALAR_SUPPORT.tsv` | `35eb7b24f9362a3f3be7bf85072edf7dc7606c8f1e305bbd864e2aa6ac56d029` |

`source_check.stdout` is byte-identical (SHA `4e56eff57a6750b8230d12b053a87b9c7731082ac2cad615239127517c997e4c`) and reports OK on all six source-manifest paths. Host stderr differs only in `/usr/bin/time` counters (RSS 17580 vs 17320 KiB; involuntary context switches 2 vs 1; CPU 100% vs 98%; both elapsed 0:00.06, both swaps 0, both exit status 0). Dual-host equality is custody, not the identity.

Independent local replay of the client with `AWS_RUN_TAG=td6_v89h14_p12_two_row_review_local` wrote the same three files with byte-identical contents and the same stdout, including `result_sha256=48a3f537…` and the `PASS` banner. That replay is algebraic verification; AWS dual-host identity is not.

The frozen V89H12 TSV at `evidence/p12-full-r3/box02/output/ALLQ_P12_FULL_NORMAL_FORM.tsv` has header plus 166 records (167 newline-terminated lines, 69466 bytes). The r6d copy is byte-identical. Independent `ast.literal_eval` parse yields 166 unique `(parameter_monomial, q_monomial)` keys, each an 18-tuple of `(numerator, denominator)` strings. Flint `fmpq_mpoly` in `Q[U,V]` parsed every numerator and every denominator with zero failures (371 distinct numerators, 31 distinct denominators).

---

## 2. Charge 2 — exact coefficient support in E3 coordinates

Zero is decided by flint polynomial vanishing of the numerator in `Q[U,V]`, not by finite-field sampling and not by trusting a noncanonical string. Census of the frozen TSV:

- the only numerator string whose polynomial is zero is exactly `"0"`;
- every such zero has denominator string `"1"`;
- conversely, every numerator string other than `"0"` parses to a nonzero polynomial.

On this frozen file the client's test `numerator != "0"` (`replay_v89h14_p12_two_row_scalar_split.py` lines 88–89, 166–169) is therefore equivalent to exact vanishing. It is not the reviewer's test; the reviewer used flint.

Let `A(q)` collect nonempty-parameter records (153 of 166) and `c(q)` the empty-parameter records (13 of 166). Flint support:

| Class | Nonzero E3 coordinates | Claim |
|---|---|---|
| nonempty-parameter (`A(q)`) | exactly `{0,1}` | both occur; coords 2–17 are the zero polynomial |
| empty-parameter (`c(q)`) | exactly `{0,1,2,3,4,5,6,7}` | all eight occur |
| every record | coords 8–17 identically `"0"/"1"` | 10 zero coordinates in all 166 records |

No nonempty-parameter coefficient has a flint-nonzero entry in coordinates 2 through 17. Coordinates 0 and 1 both occur among nonempty-parameter records (already visible in the two q2 records cited in charge 4, and in many others). No empty-parameter coefficient has a flint-nonzero entry outside 0 through 7, and each of 0 through 7 occurs.

Nonconstant denominator factors of every flint-nonzero entry, after `fmpq_mpoly.factor`, lie in `{U, V, 4U^3-V^2}` up to units. The last factor is `-(V^2-4U^3)`, i.e. `-(U*H)` on `F=0`. This matches the V89H12 denominator firewall `U^5 V^4 (V^2-4U^3)^2` and introduces no new inverted factor.

---

## 3. Charge 3 — six y-independent affine-linear equations, q-support q3 through q14

The 166 keys have parameter-monomial length in `{0,1}` and q-monomial length in `{0,1}`. There is no mixed-q monomial and no q-power. Parameter support is exactly

```text
(), (6,), (8,), (9,), (11,), (12,), (13,), (15,), (16,),
(17,), (18,), (20,), (21,), (22,), (24,), (25,), (27,).
```

Q-exponents present in the entire TSV are exactly `2,3,...,14`. In particular `q15` is absent (target shear) and `q16,...,q24` are absent after the complete V89H12 reduction: they are not keys of this TSV, so they are not omitted by the H14 client.

Empty-parameter keys, with TSV line numbers, are exactly

```text
L2  ()
L3  (3,)
L4  (4,)
L5  (5,)
L6  (6,)
L7  (7,)
L8  (8,)
L9  (9,)
L10 (10,)
L11 (11,)
L12 (12,)
L13 (13,)
L14 (14,)
```

There is no `((), (2,))` record. Because the TSV stores only nonzero 18-vectors, the entire empty-parameter q2 coefficient is the zero 18-vector, including coordinates 2 through 7.

Coordinates 2 through 7 of every nonempty-parameter record vanish (charge 2), so those six coordinates are independent of all 16 surviving quotient variables, and of the 78 cancelled nonpivots as well. Their q-support, read from the empty-parameter class, is:

| Coordinate | Empty-parameter q monomials with flint-nonzero entry |
|---|---|
| 2 | `(), q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14` |
| 3 | `(), q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14` |
| 4 | `q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14` |
| 5 | `q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14` |
| 6 | `q7, q8, q9, q10, q11, q12, q13, q14` |
| 7 | `q9, q10, q11, q12, q13, q14` |

Union of exponents is exactly `{3,...,14}`. q2 is absent; `q16,...,q24` are absent. The frozen scalar TSV (63 data rows plus header, SHA `2f888859…`) is byte-identical to an independent rebuild that emits every flint-nonzero empty-parameter entry in coordinates 2 through 7 among `{(), q3, ..., q14}`.

The H14 client iterates `SCALAR_Q = range(3,15)` when emitting those equations (`replay_v89h14_p12_two_row_scalar_split.py` lines 26, 185–190, 199–202) and never uses the unused tuple `Q_EXPONENTS = range(2,15)` at line 25. That unused tuple is not a drop of a present monomial: the frozen 166 keys contain no empty-parameter q2 and no q16–q24. Absence is a property of the complete literal V89H12 TSV, independently reparsed, not an H14 omission.

---

## 4. Charge 4 — q2 block `[[6,8],[0,4]]`, leading coefficient 24, generic rank exactly two

The only nonempty-parameter q2 records in the 166 are TSV lines 137 and 158:

```text
L137 (24,) (2,)  (('6','1'), ('0','1'), ('0','1'), ..., ('0','1'))
L158 (27,) (2,)  (('8','1'), ('4','1'), ('0','1'), ..., ('0','1'))
```

In rows `(0,1)` and columns `(y24,y27)` this is the constant integer matrix

```text
[[6, 8],
 [0, 4]].
```

Both q2 coefficients are flint constants with denominator 1; they do not depend on `U` or `V`. All other 14 surviving parameters have no q2 record (the corresponding 18-vector is zero). Coordinates 2 through 17 of both displayed records are zero. The empty-parameter q2 record is absent (charge 3), so q2 does not enter `c(q)` at all.

The 2-by-2 determinant of those two columns, as a polynomial in q, has q2-squared coefficient

```text
det([[6,8],[0,4]]) = 6*4 - 8*0 = 24.
```

This is the only contribution to the monomial `q2^2`. Every matrix entry of `A(q)` is affine-linear in q: the TSV has q-degree one and no mixed-q monomial, so no entry contains `q2^2` or `q2 q_j`. Cross terms in the determinant expansion therefore produce `q2 q_j` or q-independent summands, never a correction to the coefficient of `q2^2`. The coefficient 24 is an element of `Q`, not a polynomial in `(U,V)` that could vanish identically on `D(U*H*B3)`.

`A(q)` has only two nonzero rows, so its rank is at most two. The displayed minor is a nonzero element of `Q(U,V)[q2,...,q14]` (it has a degree-2 term `24 q2^2`), so those two rows are linearly independent over the rational function field. Rank of `A(q)` is therefore exactly two over `Q(U,V,q2,...,q14)`.

That is the generic / function-field statement. It is not a claim that the rank is two at every point of `D(U*H*B3)`, and not a claim that the minor is a unit there. When the minor vanishes, rank may drop; V89H13 already saw modular rank 1 on the pure q13 and q14 axes. `P12_TWO_ROW_SCALAR_RESULT.md` lines 33–36 correctly locates the rank statement over the rational function field, and the result artifact records `global_minor_unit_claim=false`.

---

## 5. Charge 5 — 6-by-12 scalar matrix at `(U,V)=(1,3)`

The point `(U,V)=(1,3)` lies on the registered open: `U=1≠0`, `V=3≠0`, `U*H=V^2-4U^3=5≠0`, `B3=V^4=81≠0`. On `F=0` one has `C=(V^2-U^3)/U=8` and `F=CU-V^2+U^3=0`. No scalar-equation denominator vanishes there (independent evaluation of every flint denominator).

Independent Gaussian elimination over `Q` on the 6-by-12 matrix in columns `q3,...,q14` yields rank 6, pivot columns `(0,1,2,3,4,6)`, hence pivot q-variables

```text
q3, q4, q5, q6, q7, q9
```

and 6-by-6 minor determinant

```text
-1656161280873829337287680
```

exactly as frozen in `P12_TWO_ROW_SCALAR_SPLIT_RESULT.txt` lines 11–12 and `P12_TWO_ROW_SCALAR_RESULT.md` lines 42–52. The constant vector at this point is

```text
(-72/25, 18/25, 0, 0, 0, 0).
```

A nonzero value of one 6-by-6 minor at one denominator-safe point of `D(U*H*B3)` proves that minor is not the zero element of `Q(U,V)`, hence the 6-by-12 matrix has rank 6 over `Q(U,V)`. It does not prove that the minor is a unit in the coordinate ring localized only at `U*H*B3`: the evaluation may land off the zero-divisor of that minor. The producer states this limitation explicitly (`P12_TWO_ROW_SCALAR_RESULT.md` lines 54–56; result artifact `global_minor_unit_claim=false`; preregistration lines 20–23). No repair.

A supplementary evaluation at `(U,V)=(2,3)` (where `U*H=-23≠0`, `B3=81`) again has rank 6 with the same pivot columns. That is corroboration only; the charged witness is `(1,3)`.

---

## 6. Charge 6 — fraction-field rational-section corollary

Because the 6-by-12 coefficient matrix has rank 6 over `Q(U,V)`, the six affine-linear equations determine `q3,q4,q5,q6,q7,q9` uniquely as elements of `Q(U,V)` in the remaining q-variables `{q8,q10,q11,q12,q13,q14}` (and the constant term). q2 does not appear in those equations (charge 3) and remains an independent transcendental.

The substitution does not touch the q2 block of `A(q)`. The `(y24,y27)` minor therefore remains of the form

```text
24 q2^2 + (affine in the remaining q's, with coefficients in Q(U,V)) · q2
        + (quadratic in the remaining q's).
```

The leading coefficient in q2 is still 24, which is nonzero in characteristic zero. Localizing at that nonvanishing polynomial makes the 2-by-2 invertible, so rows 0 and 1 solve uniquely for `y24,y27` in terms of the other surviving y-variables. Rows 2 through 7 are zero by the scalar solve. Rows 8 through 17 are identically zero.

The sixteen y-labels are original FIRST nonpivot coordinates, not a q-dependent rename: they are exactly the 16 of 94 that survive in the frozen V89H12 normal form (`P12_FULL_NORMAL_FORM_RESULT.md` lines 47–55). The normal form is already the substitution of the affine pivot map into literal P12, so vanishing of all 18 E3 coordinates is vanishing of P12 on a FIRST solution. The 78 cancelled nonpivots may be set to zero; the 38 FIRST pivots are then determined by the V89H12 affine pivot map, whose denominators `U^7 V^4 (V^2-4U^3)^2` are nonzero at `(1,3)`.

An explicit specialization confirms there is no hidden inconsistency or denominator zero at a point of the registered open. At `(U,V)=(1,3)`, with free q-variables `{q8,q10,q11,q12,q13,q14}` set to 0, the unique pivot solution is

```text
q3 = -182201660 / 54543223433
q4 = -38795608 / 2127185713887
q5 = -316649156 / 17726547615725
q6 = 983831413 / 574340142749490
q7 = 0
q9 = 0
```

Coordinates 2 through 17 of the normal form then vanish for every q2, as required by q2-independence of those rows. The `(y24,y27)` minor at this mixed-q point interpolates to

```text
24 q2^2
  - (14104207136768 / 31907785708305) q2
  - 6018994203517390864384 / 37707658844707881872073075
```

with leading coefficient exactly 24. At `q2=1` the minor is the nonzero rational

```text
2664929599957963678740172888 / 113122976534123645616219225.
```

Solving rows 0 and 1 for `(y24,y27)` with the other surviving y set to 0 gives

```text
y24 = 1961846330681274722079575679 / 333116199994745459842521611
y27 = -6171720362773799734102048989 / 1332464799978981839370086444.
```

The frozen 166-term normal form then evaluates to the 18-zero vector over `Q`. No extra denominator vanished. No coordinate of the original FIRST normal form is missing from this vanishing: the object being set to zero is exactly the frozen V89H12 TSV.

The preregistration (lines 25–27) correctly declined to have the *client* solve the six equations. `P12_TWO_ROW_SCALAR_RESULT.md` lines 58–75 draws the fraction-field corollary from the structure theorem. That corollary is an inference, not an H14 output artifact. Independently solving it does not change the frozen package and does not require a repair.

---

## 7. Charge 7 — the section kills global radical membership and does not fight V89H7

The Q-point of charge 6 has

```text
(U,V)=(1,3) ∈ D(U*H*B3),   F=0,   q2=1 ≠ 0,
```

together with nonzero mixed `q3,q4,q5,q6` and a FIRST-lift of `(y24,y27)` as above. It is a common zero of P12, FIRST, and F on the registered open. Therefore `q2` is not nilpotent modulo `(P12,FIRST,F)` after localizing only at `U*H*B3`, and a global certificate

```text
q_ideal ⊂ √(P12, FIRST, F)
```

on that open cannot exist. This is a negative routing result for P12-only exclusion, as claimed in `P12_TWO_ROW_SCALAR_RESULT.md` lines 67–75.

The same point is not:

- a literal total-source point (no source-map or total-Faber condition is imposed);
- a later-CURRENT solution (grades after FIRST are open);
- a total-Rees chart;
- a JC2 counterexample.

The result artifact records `source_point_claim=false`, `whole_TD6_killed=false`, `JC2_resolved=false`. `P12_TWO_ROW_SCALAR_RESULT.md` lines 86–88 repeats the firewall. No promotion is present in the frozen text.

The section does not contradict pure-axis exclusions such as V89H7. V89H7 works on `q2=⋯=q13=0` with only q14 (and high q) active, and produces a nonzero one-coordinate functional of the pure-q14 P12 class. The present section cannot live on that axis: at `(U,V)=(1,3)`, setting every q except q2 to zero leaves scalar coordinates 2 and 3 equal to `-72/25` and `18/25`, which are not zero. The six scalar equations force mixed low q. The nonzero q-variables of the explicit point are `q2,q3,q4,q5,q6`. That is the mixed-low-q locus the producer names, and it is essential.

---

## 8. Charge 8 — no Singular qring; scope is P12/FIRST structure and negative routing

The H14 client and wrapper import only `ast`, `fractions.Fraction`, `hashlib.sha256`, `os`, and `pathlib`. There is no Singular, no `qring`, no Groebner basis, and no modular reduction in the producer path. The reviewer used python-flint solely to parse and factor polynomials in `Q[U,V]` and did not call Singular.

The theorem established by the frozen package is:

1. the exact two-row / six-scalar decomposition of the V89H12 P12/FIRST normal form;
2. generic rank two of `A(q)` over the function field, witnessed by the constant q2 minor coefficient 24;
3. generic rank six of the scalar coefficient matrix over `Q(U,V)`, witnessed at `(1,3)`;
4. the fraction-field mixed-low-q section, and the consequent impossibility of a global `q_ideal ⊂ √(P12,FIRST,F)` certificate on `D(U*H*B3)`.

Later CURRENT grades, literal total-source / source-map conditions, a total-Rees chart, whole-TD6 closure, and JC2 remain open, exactly as preregistered (`PREREGISTRATION_P12_TWO_ROW_SCALAR_SPLIT.md` lines 25–29) and as repeated in the result (lines 73–75, 86–88).

---

## Non-blocking observations

These do not change the theorem and do not trigger `CORRECTED`.

- `Q_EXPONENTS = tuple(range(2, 15))` at client line 25 is unused. Scalar emission iterates `SCALAR_Q = range(3,15)`. Absence of q2 and of `q16..q24` was verified from the 166 TSV keys, not from that unused tuple.
- The source tarball contains AppleDouble `._*` sidecars. They are not hashed in the source manifest. This matches the V89H12 R3 packaging residue.
- H14 evidence directories have no `launch.meta`. Distinct AWS runs are still witnessed by distinct `/usr/bin/time` stderr and by the `box02` / `r6d` tree. Mathematical artifacts are byte-identical.

---

## Scope firewall

This review confirms an exact P12/FIRST structure theorem and a negative routing corollary on the registered open `D(U*H*B3)` in the frozen `F=0`, all-22-q scope. It does not produce a source point, a later-CURRENT solution, a total-Rees map, a whole-TD6 closure, or a JC2 result. No file other than this review was written.

**CONFIRMED**
