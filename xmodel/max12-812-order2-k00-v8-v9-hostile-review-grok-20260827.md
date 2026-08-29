# Hostile review — K00 unloaded V8 global nonmembership versus V9 filtered D7 compatibility

| Field | Value |
|---|---|
| Target | V8 unloaded global nonmembership and V9 filtered Macaulay compatibility through transverse degree 7, at the generic K00 coefficient germ |
| Charged tails SHA-256 | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` |
| One-parameter theorem SHA-256 | `5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b` |
| Overall verdict | **PASS** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks either charged claim; mixed `Lambda^19` reachability and filtered cutoffs `D>=8` remain uncharged |
| Reviewer / model | Grok 4.6 (xAI). Independent reconstruction from frozen tail bytes, independent exact row expansion, independent Macaulay emission, independent lift replay, independent exact ranks D2--D4, independent modular ranks D2--D7 at two primes, and independent Singular 4.4.1 standard bases at `C6=1` and on `D(C6)`. Producer `PASS`/`ENDPOINT`/`validator` strings were not used as characteristic-zero evidence |
| Method | SHA-256 of every charged pin; history/type-check of all 569 tail monomials; affine-linearity audit in `k10,k6,k2`; full (untruncated) substitution of the K00 transverse chart; weighted-homogeneity check; Rabinowitsch localization `1-t*C6`; fresh `dp` Gröbner bases; coefficientwise replay of the saved D7 multiplier jet against freshly emitted matrices; two-prime modular rank |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-27 |

Independently recomputed SHA-256 of the frozen tails, the one-parameter theorem, both preregistrations, V6 `RESULT.md`, and the V7 source map match the producer pins. No producer status line, no charged `PASS`/`ENDPOINT`/`UNIT` token, and no validator string is evidence. The one-parameter reduction was consumed only for the displayed row identity `(0.1)` and the identification of the unloaded coefficient polynomials `r_ell(C,0,0,0)`; it was not used as a fibre-equality or saturation license. The design note was consumed only for the K00 octic `(2.2)`, the `Jdet`/`J1`/`J2` distinction, and the transverse chart; V8/V9 make no Jacobian elimination. No file other than this review was written. Charged artifacts, shared ledgers, and `jc2-lean` were not entered, inspected as a build, or edited.

The two charged statements are compatible. Global polynomial nonmembership on `D(C6)` does not identify the first filtered/local obstruction. A global `dp` remainder's lowest displayed degree is not a filtration invariant.

---

## Line-item verdicts

| # | Task | Verdict |
|---|---|---|
| 1 | Frozen tail schema, affine linearity in `k10,k6,k2`, `Jdet` kept distinct from `J1,J2` | **PASS** |
| 2 | Reconstruct all seven unloaded rows after the K00 chart; constants and linear normals vanish | **PASS** |
| 3 | Direct `D(C6)` membership, Rabinowitsch localizer, proper standard basis, Kummer `C6=1` | **PASS** |
| 4 | V8 has no diagnostic; V7 `exit(0)` correctly rejected; V8 uses `quit;` plus external failure markers; residual and basis hashes | **PASS** |
| 5 | Reject both raw remainder degrees as canonical obstruction degrees; recheck `Q7=-(1/512)Q1-(1/128)Q3`; explain the displayed degree-2 remainder | **PASS** |
| 6 | Independent cumulative filtered Macaulay maps through `D7`, including all constant and later syzygies and every multiplier monomial of degree `<= D-2` | **PASS** |
| 7 | Coefficientwise D7 lift replay; matrix SHA `1a094f16...3473`; lift SHA `2fe2b6bc...d71db`; representation independence of the full cumulative map | **PASS** |
| 8 | Load-normal stencil minimal degrees are correct, and are input to (not a substitute for) the pending `Lambda^19` mixed test | **PASS** |
| 9 | Defect search: denominator loss, bad Kummer descent, row/column order, truncation, characteristic leakage, false rank replay, unjustified formal/local membership | **PASS** (no such defect in the charged claims) |

**Overall: PASS.**

---

## Hashes and charged artifacts

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| frozen `tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` | charged source bytes (matches pin) |
| canonical all-tail digest | `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8` | 569-term serialization (matches pin) |
| one-parameter Rees reduction | `5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b` | charged `(0.1)`; not a saturation license |
| V6 quadratic `RESULT.md` | `9b95409aafdd10346ca1095047bd1ea5ebbdd6ca23e2b5a7e29323e01e8e5909` | charged quadratic identities, independently re-expanded |
| V8 preregistration | `fe085951e6a5a9e23f33a6af37d0ab1861221831a4c22a026f06428d55d54ea0` | repair/measurement design; no V8 result at registration |
| V9 preregistration | `dce7ac60e820f0a11eb2cc531b6d2def85e5f86c7d6209cd63a4efb979afca30` | degree-7 compatibility design; prefix ranks D2--D6 |
| V7 source map `compile_unloaded_membership.py` | `a7f335cdbc3e5525ce641ff10d8370a52d4cbb9c84e2417b17eea64a38154f70` | frozen coefficient images used by V8 |
| K00 design note | `9c5bf1229cf45dd7ea4d5d3907fd6033c88c0d9768934d01ea79e658f3d65a17` | `(2.2)`, `Jdet` vs `J1,J2`; not a V8/V9 algebra source |

Independently hashed V8 evidence, matching the V8 `RESULT.json` fields:

| Evidence | SHA-256 |
|---|---|
| direct residual | `ebc1c27dffa45ebd94caf472059e0ac55cd39f706567e5b0b785bb9a0da693a5` |
| direct leading transverse class | `5cd154a9937db66be5bef66afeaccd7013c1c30b11986c24de3633cbb584d9b6` |
| direct standard basis | `0d05c38026506c20bcee035f2c585588e2d50edc13748123776dd2bbff307b56` |
| normalized residual | `e5b08388cb0acb1340c2000cee6bafc0a39c48c9bc6f5995d72785f8c5bf8347` |
| normalized leading class | `1bbf72de6cf5aec888fdccf0de6ceb7a084e303ae6716c837409e1f8d8770c8f` |
| normalized standard basis | `1288296b116352595b855e4a54a77c6b9965cd02620c21c84524c7ef446f8397` |

Independently hashed V9 D7 artifacts, matching the V9 `RESULT.json` fields:

| Evidence | SHA-256 |
|---|---|
| D7 matrix | `1a094f16bb3ba2a44571a26684bcc592d1895cd65f60a8b4722bb43397cf3473` |
| D7 exact lift | `2fe2b6bc81c79a345e3773e1f92982002d953aa9e4aef955e6023a15fb9d71db` |
| load-normal stencil | `c59bdf58d2a2f62c2cb5831c82b5e609a014ccb3fcf17b1802b736174f3eb7dd` |

The exact-Q and `p=65521` D7 matrix files are byte-identical. The quarantined r6d V9 attempt failed before matrix algebra (`g++: command not found`) and was not used.

---

## Strongest exact theorem that survives

Work over `Q`. Let `r1,...,r7` be the unloaded (`k10=k6=k2=0`) ordinary tails obtained from the frozen 569-term source by the K00 transverse chart

```text
C5=d5,           C4=(3*C6^2+d4)/8,
C3=d3,           C2=(C6^3+d2)/16,
C1=d1,           C0=(C6^4+d0)/256.
```

These seven polynomials are weighted-homogeneous of weight `12+ell` if `wt(C6)=2` and `wt(d0,...,d5)=(8,7,6,5,4,3)`. Every constant term and every linear term in `(d0,...,d5)` vanishes. The quadratic-normal pieces satisfy

```text
Q6 = 0,
Q5 = -(3*C6^2/128)*Q1 - (C6/8)*Q3,
Q7 = -(C6^3/512)*Q1 - (C6^2/128)*Q3,
```

and therefore at the Kummer slice `C6=1`

```text
Q7 = -(1/512)Q1 - (1/128)Q3.
```

1. **Global unloaded nonmembership.** In `Q[t,C6,d0,...,d5]`, the ideal `(r1,...,r6,1-t*C6)` is proper, and `r7` is not in it. Equivalently,

   ```text
   r7 not in (r1,...,r6)  over  Q[C6,C6^{-1},d0,...,d5].
   ```

   The same nonmembership holds after the weighted Kummer slice `C6=1` in `Q[d0,...,d5]`. Both conclusions were obtained from independently expanded generators by a fresh `dp` standard basis (direct: 337 generators, residual 53 terms; normalized: 117 generators, residual 32 terms), not from producer status strings.

2. **Filtered compatibility through degree 7.** At `C6=1`, write `ri = sum_{m>=2} Ri,m` with `Ri,m` homogeneous of degree `m` in `(d0,...,d5)`. For each cutoff `D=2,...,7`, the cumulative Macaulay map

   ```text
   (h1,...,h6) |-> sum_{i=1}^6 hi * ri  mod (d)^{D+1},
   deg(hi) <= D-2,
   ```

   acting on all equations in degrees `2` through `D`, has rank equal to augmented rank:

   ```text
   D2 21 x 6,   rank = augmented rank = 4
   D3 77 x 42,  rank = augmented rank = 28
   D4 203 x 168, rank = augmented rank = 106
   D5 455 x 504, rank = augmented rank = 294
   D6 917 x 1260, rank = augmented rank = 676
   D7 1709 x 2772, rank = augmented rank = 1372.
   ```

   Thus `r7` lies in `(r1,...,r6)+(d0,...,d5)^8` at the normalized germ. A saved exact rational multiplier jet with 273 nonzero entries (through multiplier degree 5) replays all 1,709 rational coefficient equations. This is representation-independent: it is a property of the full cumulative map, not of one chosen quadratic correction.

The two statements are not in conflict. Statement 1 is polynomial ideal nonmembership on the generic coefficient chart `D(C6)`. Statement 2 is finite-order filtered compatibility at the closed point `d=0` of that chart. Neither is membership in the local ring, mixed `Lambda`/load/`Jdet` reachability, Taylor realization, order-two closure, `(8,12)` closure, maximum twelve, or JC2.

---

## Attack 1 — frozen tail schema, affine load linearity, `Jdet` vs `J1,J2`

**PASS.**

The frozen file `cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json` hashes to the charged pin. Its canonical `sort_keys` digest is `6eed03d486…387e8`. Keys are exactly `"1"` through `"7"`. Term counts are

```text
36, 54, 58, 81, 89, 120, 131
```

summing to 569, matching `result.json` `tail_supports`. Every monomial has length 10, nonnegative exponents, and weighted degree `12+ell` against

```text
wt(a0,...,a6,k10,k6,k2) = (8,7,6,5,4,3,2, 2,6,10).
```

Load exponents occupy the last three slots. For every one of the 569 terms, those three exponents lie in `{0,1}` and sum to at most 1. There is no bilinear or higher load monomial. Unloaded / `k10` / `k6` / `k2` counts:

```text
row   unloaded  k10  k6  k2
  1        19    12   4   1
  2        27    18   7   2
  3        30    19   7   2
  4        40    27  10   4
  5        44    30  11   4
  6        57    40  16   7
  7        63    44  17   7.
```

This is the affine-linear expansion `g=F12+k10 F10+k6 F6+k2 F2` of `compile_rees.py` `build_faber_and_tails`, serialized by V2. Coefficients are exact rationals.

The tails contain no `J`, `j`, `Jdet`, `J1`, or `J2` variable. The design note `xmodel/max12-812-order2-p0-k00-honest-source-discriminator-design-sol-20260827.md` (0.1) and (3.3) keeps the terminal Jacobian `Jdet` distinct from the collision ideals `J1=(rs,cs,c0,c1)` and `J2=(a0,a1)`. V8 and V9 specialize loads to zero and never eliminate a Jacobian. The one-parameter identity (0.1) with `delta_7=J/4` is not an input to either computation.

---

## Attack 2 — K00 chart and vanishing of constants and linear normals

**PASS.**

The design octic (2.2) is `(z^2+C6/4)^4`. Expanding gives the K00 even coefficients

```text
C4 = (3/8) C6^2,    C2 = (1/16) C6^3,    C0 = (1/256) C6^4,
C5 = C3 = C1 = 0.
```

The charged transverse chart is exactly that expansion plus the six normal coordinates `d0,...,d5`. At the K00 point every `d_i` vanishes.

Independent (untruncated) substitution of the chart into every unloaded tail monomial produces seven polynomials in `(C6,d0,...,d5)`. After the Kummer slice `C6=1` the term counts are 16, 23, 27, 36, 40, 42, 57. For each row, the degree-0 piece and the degree-1 piece in `(d0,...,d5)` are empty, both at `C6=1` and with symbolic `C6`. Weighted homogeneity of every surviving term holds with weight `12+ell`; there are zero failures.

Quadratic-normal term counts are `8,11,9,12,8,0,6`, matching V6. The three identities of Attack 5 hold on these independently expanded quadratics, so V6's multiply-time truncation at normal degree `>2` did not drop a quadratic term.

---

## Attack 3 — direct `D(C6)` membership, localization, and `C6=1`

**PASS.**

Adjoining `1-t*C6` is the Rabinowitsch localizer: `r7` lies in the extension of `(r1,...,r6)` to `Q[C6,C6^{-1},d0,...,d5]` if and only if `r7` lies in `(r1,...,r6,1-t*C6)` in `Q[t,C6,d0,...,d5]`. V8 writes this generator into the source ideal (`compile_unloaded_membership_v8.py` `localizer_generator = ",1-t*C6"`; compiled `k00_unloaded_v8_direct_q.sing` line 13). The saved direct standard basis begins with `t*C6-1`, so the localizer is in the basis.

A fresh local Singular 4.4.1 `dp` standard basis of the independently expanded generators in `Q[t,C6,d0,...,d5]` returned

```text
G_SIZE=337,   reduce(1,G) != 0,   reduce(r7,G) != 0,   residual size 53.
```

The same engine, reducing the independently expanded `r7` against the saved V8 basis, matched the saved 53-term residual coefficientwise, reduced `1-t*C6` and `r1,...,r6` to zero, and left `1` unreduced. The source ideal is proper. This is exact global nonmembership on `D(C6)`.

Weighted homogeneity supplies the Kummer descent. After inverting `C6`, the `G_m`-action `lambda * C6 = lambda^2 C6`, `lambda * d_i = lambda^{wt(d_i)} d_i` has slice `C6=1`. Because every `r_ell` is weighted-homogeneous, membership over `Q[C6,C6^{-1},d0,...,d5]` is equivalent to membership of the specialized generators over `Q[d0,...,d5]`. A fresh `dp` standard basis at `C6=1` returned

```text
G_SIZE=117,   reduce(1,G) != 0,   reduce(r7,G) != 0,   residual size 32,
```

and the residual polynomial is byte-identical to the saved V8 normalized residual

```text
e5b08388cb0acb1340c2000cee6bafc0a39c48c9bc6f5995d72785f8c5bf8347.
```

The extra inert `h` in the V8 rings is bookkeeping for post-reduction transverse telemetry. It does not appear in the generators, in either residual, or in either saved basis. V7 (no `h`) and V8 (with `h`) standard-basis and residual files are byte-identical; V8 dimensions are one higher because `h` is free. The membership decision is unaffected.

---

## Attack 4 — V7 `exit(0)` rejection and V8 endpoint hygiene

**PASS.**

V7 `compile_unloaded_membership.py` line 157 emits `exit(0);`. Both raw V7 lanes computed a nonzero residual and then printed Singular diagnostics

```text
? `exit(0)` is undefined
```

The V7 validator (`validate_unloaded_membership.py` line 27) rejects any `?` in engine output. Both V7 `*.validation` files record `engine_rc=0` without a validator pass. `FAILURE.md` correctly quarantines those runs. Under the registered fail-closed policy there is no V7 verdict.

V8 replaces every `exit(N)` by `quit;` and prints an explicit `K00_UNLOADED_V8_FAIL=...` marker on failure paths, which the external validator rejects (`validate_unloaded_membership_v8.py` lines 33--34). Compiled `k00_unloaded_v8_direct_q.sing` and `k00_unloaded_v8_normalized_q.sing` end with `quit;`. Neither accepted V8 stdout contains `?` or a `FAIL=` marker. Both carry `K00_UNLOADED_V8_NEGATIVE_CONTROL_PROPER=1` and `K00_UNLOADED_V8_MEMBER=0`. The saved residual and basis hashes in Attack 3 match the V8 `RESULT.json` fields independently recomputed from the artifact bytes.

V8 does not change the frozen tails, the K00 chart, the source ideal, the characteristic, the localization, or the monomial order. The only mathematical addition is the post-reduction `di |-> h*di` telemetry, which is not used as an obstruction degree (Attack 5).

---

## Attack 5 — raw remainder degrees are not obstruction degrees; `Q7` identity

**PASS.**  Both displayed remainder degrees are rejected as canonical filtered obstruction degrees.

Independent full expansion gives, identically as quadratic polynomials in `(C6,d0,...,d5)`,

```text
Q7 + (C6^3/512) Q1 + (C6^2/128) Q3 = 0,
```

and at `C6=1`

```text
Q7 + (1/512) Q1 + (1/128) Q3 = 0.
```

Sample coefficient, monomial `d4 d5` at `C6=1`:

```text
Q7 = 3/1048576,   Q1 = -3/512,   Q3 = 9/8192,
3/1048576 + (1/512)(-3/512) + (1/128)(9/8192)
  = 3/1048576 - 12/1048576 + 9/1048576
  = 0.
```

`Q6=0` and `Q5+(3/128)Q1+(1/8)Q3=0` likewise. The D2 Macaulay particular solution is exactly the multipliers `h1=-1/512`, `h3=-1/128`, with all other constant multipliers zero. The associated-graded quadratic class of `r7` is therefore zero.

The normalized global `dp` remainder nevertheless begins with the seven-term quadratic

```text
-3/311296 d0 d1 + 3/311296 d2 d3 + 3/155648 d1 d4
-3/311296 d3 d4 + 3/4980736 d0 d5 - 3/622592 d2 d5
+ 9/2490368 d4 d5.
```

This is not `Q7`. The quadratic `Q7` is supported on `{d4 d5, d3 d4, d2 d5, d1 d2, d0 d3, d0 d1}`; the remainder piece is supported on `{d0 d1, d2 d3, d1 d4, d3 d4, d0 d5, d2 d5, d4 d5}`; coefficients disagree on the overlapping monomials. The direct remainder's lowest `d`-degree is 3, not 2.

Cause: `dp` selects highest total degree. After the affine (not linear) even-coefficient substitutions, each `r_i` is inhomogeneous in the `d`'s. The Gröbner leading terms are therefore not the lowest-degree homogeneous pieces. Reducing high-degree terms of `r7` against those leading terms can reintroduce quadratic combinations that vanish in the ideal but are not reduced with respect to the quadratic initials. The lowest displayed `dp` degree is a property of this frozen global normal form, not an invariant of the transverse filtration. V8 `RESULT.md` already refuses to promote it. The refusal is mandatory and is here independently justified.

---

## Attack 6 — cumulative filtered Macaulay maps D2--D7

**PASS.**

The construction in `emit_filtered_macaulay.py` `write_matrix` is the complete cumulative map of V9 preregistration: columns are indexed by multiplier degree `0,...,D-2`, then row `1..6`, then colex monomials in `(d0,...,d5)` (producer label `lex_normal_monomial`; last index varies fastest); rows are normal degrees `2` through `D` in the same monomial order. Constant syzygies, later syzygies, and every multiplier monomial through degree `D-2` are included. Degree-0 and degree-1 row pieces are absent because they vanish (Attack 2); they are not silently dropped from a nonzero expansion.

Predicted shapes from `sum_{d=2}^{D} binom(d+5,5)` rows and `6 * sum_{k=0}^{D-2} binom(k+5,5)` columns match the producer headers exactly:

```text
D2  21 x 6      nnz 54
D3  77 x 42     nnz 449
D4  203 x 168   nnz 2022
D5  455 x 504   nnz 6743
D6  917 x 1260  nnz 18433
D7  1709 x 2772 nnz 43660.
```

Independently emitted TSV files hash to the producer matrices at every cutoff, including D7

```text
1a094f16bb3ba2a44571a26684bcc592d1895cd65f60a8b4722bb43397cf3473.
```

Independent exact `Q` RREF on D2, D3, and D4 reproduces rank = augmented rank = `4, 28, 106`. Independent dense Gaussian elimination over `F_65521` and over `F_10007` reproduces

```text
D2 4, D3 28, D4 106, D5 294, D6 676, D7 1372
```

with equal augmented ranks, and every matrix denominator is invertible at both primes. All observed denominators divide `2^21=2097152`. There is no odd-prime denominator and no characteristic leakage at these two primes. The V9 prefix sentinels D2--D6 are confirmed; the D7 rank, which the validator does not pre-register, is confirmed independently.

This is not a degreewise test of isolated homogeneous pieces without lifts. Compatibility at cutoff `D` uses all lower-degree multipliers simultaneously.

---

## Attack 7 — D7 multiplier replay and representation independence

**PASS.**

The saved exact D7 solution hashes to `2fe2b6bc81c79a345e3773e1f92982002d953aa9e4aef955e6023a15fb9d71db`, has 273 nonzero entries, and, applied to the independently emitted D7 matrix, leaves a zero residual on all 1,709 rows over `Q`. The same coefficientwise replay succeeds at D2 through D6 against the independently emitted matrices. That is an exact membership certificate for `r7` in `(r1,...,r6)+(d)^8`, independent of the producer RREF binary.

The D2 particular solution is the V6 identity `(h1,h3)=(-1/512,-1/128)`. The D7 particular solution has constant multipliers

```text
h1=-5/1024,  h3=-3/128,  h5=-1/8.
```

These differ from the D2 solution by the constant syzygy of `Q5`:

```text
(-1/512, -1/128, 0) + (-1/8) * (3/128, 1/8, 1)
  = (-5/1024, -3/128, -1/8).
```

RREF is entitled to add kernel vectors. The D7 jet also carries higher-degree multipliers that the quadratic identity does not see. Compatibility is a property of the existence of some lift for the full cumulative map, not of a preferred quadratic correction. The two particular solutions are different points of the same affine space of D2 solutions, extended by higher jets. No unique-correction claim is required, and none is used.

The separately serialized `p=65521` lane is software/navigation only. It reproduces rank 1372 and replays its own modular lift; it does not replace the rational endpoint. The r6d V9 attempt that lacked `g++` is quarantined.

---

## Attack 8 — load-normal stencil

**PASS** as a valuation stencil. It is not a mixed-reachability theorem.

Independent expansion of each affine load sector at `C6=1` reproduces the producer `load_normal_stencil.json` coefficientwise (zero diffs). Minimum normal degrees:

```text
k10:  2,2,2,2,2,2,2     in rows 1..7
k6:   1,1,1,2,1,2,1
k2:   1,1,1,1,1,1,1
```

Spot check against frozen bytes: row 1, term `[[0,0,0,0,0,1,0,0,0,1],"1/4"]` is `(1/4) C5 k2 = (1/4) d5`, so the `k2` derivative of row 1 starts in degree 1. Constants in every load sector vanish.

These numbers are lower bounds on the first transverse degree at which each load derivative can appear in the K00 jet. They are the correct input to a later mixed compiler that retains

```text
Lambda^2 k10,  Lambda^6 k6,  Lambda^10 k2
```

and the targets of one-parameter (0.1), with terminal scale `Lambda^19`. They are not a substitute for that test: load scalings, target scalings, and coefficient normals can cancel, and the stencil does not impose divisibility. V9 `RESULT.md` and the V9 preregistration state this limitation. The present review does not promote the stencil to a `Lambda^19` verdict.

---

## Attack 9 — defect search

**PASS.** No charged claim is supported by a defect of the listed kinds.

- **Denominator loss.** Chart denominators are `8,16,256`. Matrix denominators divide `2^21`. The characteristic-zero expansions and both modular ranks invert them. No coefficient was dropped.
- **Bad Kummer descent.** Direct localization and the `C6=1` slice agree on nonmembership. Weighted homogeneity of the independently expanded rows is exact. The slice is a section of the standard weight-2 Kummer cover, not a random specialization.
- **Row/column ordering.** Independent emission in the producer monomial order matches every matrix SHA. Rank is independent of that order; the SHA match additionally pins the serialization.
- **Truncated terms.** V9 multiplies without a degree cap, then cuts the cumulative map at `D`. V6's quadratic-only truncation is independently validated by the untruncated expansion. No D7 matrix entry is missing relative to that expansion.
- **Characteristic leakage.** Exact D2--D4 ranks agree with two distinct odd primes. D5--D7 modular ranks agree at `65521` and `10007`. All denominators are powers of two.
- **False rank replay.** Rank was recomputed from independently emitted matrices. The D7 lift was applied to those matrices over `Q`, not to a producer-reduced copy.
- **Unjustified finite-to-formal passage.** Compatibility through degree 7 is `r7 in (r1,...,r6)+(d)^8`. It is not membership in the `d`-adic completion, not local-ring membership, and not a Krull-intersection argument. V8 and V9 firewalls state this. This review does not reverse those firewalls.

V8's unused `LIB "elim.lib"` and the extra inert `h` are endpoint-hygiene nits, not algebraic defects. Singular's `G is no standard basis` warning on a `write()` dump loaded without an `isSB` attribute is an artifact of remainder replay; the fresh `std` calls are the membership proofs.

---

## Firewall

The surviving theorem is exactly the pair (1)+(2) in the strongest-theorem section: global unloaded nonmembership on `D(C6)`, and filtered compatibility of the complete cumulative Macaulay map through transverse degree 7 at the normalized generic K00 germ. It is a statement about the six-dimensional transverse coefficient chart with loads set to zero.

It does not decide membership in the local ring of that germ, mixed `Lambda`/load/`mu`/`Jdet` reachability, the closure-first incidence `H_K00`, Taylor realization of either finite family, order-two closure, `(8,12)` closure, maximum twelve, or JC2. The one-parameter reduction's boundary-scheme equality is not invoked.

---

## Next unresolved obligation

The first unresolved filtered coefficient question is compatibility at cutoff 8, or the first cutoff at which adjoining row 7 increases rank. Independently, the load-normal stencil is ready as input to the pending mixed `Lambda^19` reachability test that retains `k10,k6,k2` and the targets of (0.1). Neither of those tests is charged here, and neither is a JC2 statement.

**PASS**
