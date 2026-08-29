# Hostile review — sharpened square third-tail source theorem V2

| Field | Value |
|---|---|
| Targets | `cases/max12_812_order2_square_third_tail_sharp_v2_20260826/RESULT.md`; `FREEZE.sha256`; `RESULTS.sha256`; `compile_square_third_tail_sharp_v2.py` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. Charged reviews and producer status lines are not evidence |
| Method | source reading, SHA-256 of every named pin and evidence file, and hand identities only; no Singular, Sage, msolve, Lean, package compiler, CAS, AWS job, or substantive exact Python |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the four required primary pins match. Every path named in `FREEZE.sha256` (7 rows) and `RESULTS.sha256` (63 rows) rehashes to the printed digest. V1 is preserved as a four-lane deployment negative and is not an accepted mathematical endpoint. Producer verdict language, both V2 status lines, and both `F_65521` lanes were not used as characteristic-zero algebra. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

In the matched square chart

```text
K = L^2 + Lambda R,
N = L M + Lambda S,
k10 = Lambda kappa,
T = 2 L R + M,
B = R^2 + S,
```

with `L = z^2 + p/2` at fixed `p`, or with the displayed integral tangent `p = Lambda p1` and boundary `L = z^2`, the seven complete frozen one-parameter ordinary rows are identically divisible by `Lambda^3`. Their divided boundary values are the lower-unitriangular Faber image of the first seven strictly negative Laurent coefficients of

```text
[ P / (16 L^3) ]_-,     P = T (12 B L^2 - T^2).
```

The factor `16` is a unit in characteristic zero. The proper denominator has degree six, so vanishing of those seven (in fact already the first six) negative coefficients is equivalent to `L^3 | P`. Reducing modulo `L` gives the polynomial identity `P ≡ -M^3 (mod L)`. On fixed `p ≠ 0`, `L` is squarefree of degree two and `deg M ≤ 1`, so `M = 0`. At the quadruple-root boundary `L = z^2`, the same seven vanished rows give `z^6 | P`, not merely `z^2 | P`; then `[z^0]P = -β^3` forces `β = 0` and `[z^3](P|β=0) = -α^3` forces `α = 0`, for arbitrary linear `R, S`. Thus the complete third-tail necessary condition forces `M = 0` at both generic square `p` and at `p = 0` along the displayed integral tangent, with integral load `k10 = Lambda kappa` retained.

This sharpens the predecessor divisibility note, whose rank-drop conclusion was only `β = 0`. It is a necessary third-tail gate for this charged source, not a square-component, Newton-fan, order-two, `(8,12)`, maximum-twelve, or JC2 theorem.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 1. Four primary pins | SHA-256 | `RESULT.md`, `FREEZE.sha256`, `RESULTS.sha256`, and the V2 compiler match the required pins |
| 1. Both manifests | every named file | all 7 `FREEZE` rows and all 63 `RESULTS` rows rehash to the printed digest |
| 1. V1 isolation | deployment negative | V1 directory has no `RESULT.md`, no `RESULTS.sha256`, and no run artifacts; generated Singular uses unavailable `coeff(poly,var,n)`; V2 repair replaces only those four extraction sites plus a sparse self-control |
| 1. Four frozen endpoints | two Q + two `F_65521` | four distinct compiled scripts, tags, hosts, `result.json` payloads, and engine stderr hashes; only the two exact-Q lanes carry the characteristic-zero statement |
| 1. `F_65521` | software control | `65521` divides none of `2,3,5,7,16,12` or `n!` for `n≤10`; not a characteristic-zero proof |
| 2. Source substitutions | charged rows | `K,N,k10` and the linear chart `R,S,M` match the predecessor and the load-ladder coefficient list, with `M` restored |
| 2. `Lambda^3` divisibility | exact quotient | both `reduce(Phi, Lambda^3)==0` and `Lambda^3 Q3 = Phi` are in the generated script; frozen exact-Q stdout records both sentinels equal to 1 |
| 2. Laurent orientation | reversal and `Inv3` | `Prev = t^9 P(1/t)`, `H = Prev Inv3 / 16`, `h_ell = [t^{ell+3}] H = [z^{-ell}] P/(16 L^3)`; no off-by-one |
| 2. Faber transform | lower unitriangular | diagonal 1; odd differences vanish; printed `RowCheck` coefficients match the binomial expansion of `z^{-j}` in `w^{-1}` for `w^2 = z^2 + pbase/2` |
| 2. Seven row identities | inspect both sides | sides mean the ordinary divided source versus Faber of `[P/(16 L^3)]_-`; equality is a frozen exact-Q polynomial certificate, not a slogan |
| 2. Lower-grade mixing | `Lambda^1, Lambda^2` of `f^{3/2}` | both grades are polynomial in `z` on this chart; unitriangular change therefore has no inhomogeneous lower-grade source into the `Lambda^3` ordinary rows |
| 3. Completeness at this grade | charged source, not a weight slogan | integral `k10 = Lambda kappa` contributes `kappa L^5` at `Lambda^3`, which is polynomial; `k6`, `k2`, and the displayed targets begin at `Lambda^6`, `Lambda^{10}`, and `Lambda^{12+ell}`; `p = Lambda p1` is absent from the divided negative grade |
| 3. Seven rows suffice | degree, not slogan | after deleting the polynomial part, the remainder has denominator degree six, so six negative Laurent coefficients already imply `L^3 | P` |
| 3. Arbitrary linear `R,S` | retained | `R = cs z + rs/4` and `S = (v1 z + v0)/2` remain free in `P` and in the row identities |
| 4. Generic square | `P ≡ -M^3 (mod L)` | polynomial identity; on `p≠0`, `L` is squarefree of degree two in characteristic zero, `deg M ≤ 1`, hence `M = 0` |
| 4. Moving-`p` denominator | not replaced in the source | `p0moving` builds `Phi` from `pp = Lambda pt`; the analytic comparison is of the extracted `Lambda^3` boundary, whose denominator is the boundary `L = z^2` |
| 5. Quadruple-root sharpening | `[z^0]P`, `[z^3]P` | hand identities `[z^0]P = -β^3` and `[z^3](P\|β=0) = -α^3` for arbitrary linear `R,S`; seven vanished rows give `z^6 | P`, hence `α = β = 0` |
| 6. Exact scope | necessary gate only | `M = 0` for fixed `p` or the displayed integral `Lambda` tangent, with `k10` of integral `Lambda`-order at least one; named nonzero zero-load first directions and their `p=0` limit fail this gate |
| 6. Sharpest nonclaim | excluded | fractional or ramified slopes of `p` or `k10`; post-`M=0` cusp/odd faces; Newton-fan exhaustiveness; terminal or Taylor conditions; existence or exclusion of a strict arc; the whole square component; order two; `(8,12)`; maximum twelve; JC2 |

---

## 1. Custody and execution

Recomputed SHA-256 of the four required primaries:

| Artifact | SHA-256 | Role |
|---|---|---|
| `RESULT.md` | `5a966b1d4dfde21e51bbaa6120a7cf118b05e68cfc0878aa2d1c345c6a0f47a0` | producer endpoint (matches required pin) |
| `FREEZE.sha256` | `96cb2824fb5c901e7485ba725f5d92e8f116b32a8a9dde7fd6c59cb901be013e` | source freeze (matches required pin) |
| `RESULTS.sha256` | `6ae5fe22481ac4ec085006d91919b35b9ff5b85abd05517b502850fdc07bb26b` | evidence freeze (matches required pin) |
| `compile_square_third_tail_sharp_v2.py` | `b93d402434f3e76fa277567ca87af881da685826c58b2ffa75e06a4e975e09eb` | V2 compiler (matches required pin) |

V1 pins named by the V2 freeze, independently rehashed:

| Artifact | SHA-256 |
|---|---|
| V1 compiler | `9a39ba22d85bbc0336f11269701acb312f6cd2629ac157c54c2d76836d07e124` |
| V1 `FREEZE.sha256` | `f6999a1f9ef2a07bcb921fbf8482b5b00d8daeceb7a41c6a9fca2030203cabe4` |
| predecessor theorem | `045b1bdc6c1429451afa34dd2d7d12da4c72d9af716e52228a869f61d0f4a4bb` |
| `tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` |

Every V1 freeze row also rehashes. The successor design is frozen in V1 and is not a mathematical premise of this review.

### Four frozen runs

The two exact-Q configurations and two `F_65521` controls are four frozen endpoints in the custody sense. Only exact Q carries the characteristic-zero statement.

| Charge | generic `Q` | `p=Lambda p1` `Q` | generic `F_65521` | `p=Lambda p1` `F_65521` |
|---|---|---|---|---|
| Host | `ip-172-30-0-249` (Box03) | same | `ip-172-30-0-45` (r6d) | same |
| Tag | `...generic_q_20260826T090820Z_box03` | `...p0moving_q_...box03` | `...generic_p65521_...r6d` | `...p0moving_p65521_...r6d` |
| Ring | `R=0` | `R=0` | `R=65521` | `R=65521` |
| Compiled script | `c77fa2dc…b6ed61` | `8ea26976…a80252` | `9f30ebac…9f09e9` | `b4f93bcc…7a4c9c` |
| `result.json` | `087220e7…00ab021` | `1824ad6d…18a99f` | `4daf9b12…381a87c` | `ed90fda5…8f43ebb` |
| Engine `rc` | `0` | `0` | `0` | `0` |
| Validator | `PASS_SQUARE_THIRD_SHARP_V2` | same token | same token | same token |
| Stdout SHA | `cf0e22ab…b0c90d` | `df80ce50…085b7ff` | `cf0e22ab…b0c90d` | `df80ce50…085b7ff` |
| Stderr SHA | `6e8fbfb5…cbe18e` | `09e18e49…c05ad29` | `edc0dec9…a60c995` | `83f80af4…a99f2a2` |
| Peak RSS / swap | 11,956 KiB / 0 | 11,196 KiB / 0 | 11,304 KiB / 0 | 10,780 KiB / 0 |
| Extractor control | `=1` | `=1` | `=1` | `=1` |
| `V2_PATCH` | `DERIVATIVE_FACTORIAL` | same | same | same |

Same-config exact-Q and `F_65521` stdout hashes coincide because stdout is only sentinels, not polynomials. The compiled scripts differ by the ring-characteristic token (and therefore by hash), the engine stderr hashes differ, and the hosts, tags, and `result.json` characteristics differ. Shared validation-file hashes are the same two-line payload `engine_rc=0` plus the V2 validator line, not evidence that the runs were copied. All four compiler stderr files are the empty digest `e3b0c442…`. All four freeze checks report every V2 and V1 freeze row OK. Each `result.json` records `v1_compiler_sha256` and `v1_freeze_sha256` matching the V2 freeze, and `scope` equal to `V2_COEFFICIENT_API_REPAIR_ONLY_NO_SQUARE_OR_ORDER2_VERDICT`.

A passing manifest is not a mathematical verdict. The algebra below is independent of those sentinels.

### V1 is not an endpoint; V2 changes only extraction

The V1 package contains the compiler, registration, launch scripts, metadata, and freeze, and no run tree, no `RESULT.md`, and no `RESULTS.sha256`. V1 `emit` writes four `coeff(poly,var,degree)` calls. That is not a Singular builtin. V2 `repair` does exactly the following, and then refuses any remaining `coeff(`:

- replace each `coeff(PP,z,k)` by the iterated derivative/factorial coefficient `PZC k`, `k = 0..9`;
- replace each `coeff(H,t,ell+3)` by `HTC{ell+3}`, `ell = 1..7`;
- on `p0moving`, replace `coeff(PP,z,0)` and `coeff(PPbeta0,z,3)` by `PZC0` and `PBC3`;
- insert the known sparse control `3+5z+7z^3` with expected coefficients `(3,5,0,7)` before any row identity is accepted;
- print `SQUARE_THIRD_SHARP_V2_PATCH=DERIVATIVE_FACTORIAL`.

Source substitutions, frozen tail polynomials, Faber matrix, configurations, fields, divisibility sentinels, and the analytic polynomials `L,M,R,S,T,B,P` are those of V1. Factorials in the generated scripts are the correct values `1,1,2,6,24,120,720,5040,40320,362880,3628800`. The self-control is a correct Taylor extraction of a polynomial with a missing quadratic term. There is no hidden source-formula change.

The four V1 AWS tags were preregistered at `09:04:01Z`. Their validator records are not in the charged V1 directory. A V1 mathematical endpoint is already impossible: the generated engine input is not a Singular program.

---

## 2. Complete-source bridge

Start from the charged substitutions and the load-ladder coefficient list of `f = K^2 + Lambda N`, with `M` restored:

```text
L = z^2 + p/2,
R = cs z + rs/4,
M = m1 z + m0,
S = (v1 z + v0)/2,
K = L^2 + Lambda R,
N = L M + Lambda S.
```

Then `K = z^4 + p z^2 + Lambda cs z + (p^2 + Lambda rs)/4` on the generic chart, and

```text
N = m1 z^3 + m0 z^2 + ((p m1 + Lambda v1)/2) z + ((p m0 + Lambda v0)/2),
```

which is exactly the V1/V2 `n3,n2,n1,n0` block. Direct expansion, with `T` and `B` as above, gives

```text
f = L^4 + Lambda L T + Lambda^2 B
```

when `L` is independent of `Lambda`. Write `X = Lambda T/L^3 + Lambda^2 B/L^4`. Then

```text
f^{3/2} = L^6 (1+X)^{3/2},
(1+X)^{3/2} = 1 + (3/2) X + (3/8) X^2 - (1/16) X^3 + O(X^4).
```

The `Lambda^1` piece is `(3/2) T L^3`, polynomial in `z`. The `Lambda^2` pieces are `(3/2) B L^2` and `(3/8) T^2`, both polynomial. The `O(X^4)` remainder starts at `Lambda^4`. The first `Lambda^3` contribution to `f^{3/2}` is therefore exactly the negative-tail candidate

```text
(3/4) T B / L - T^3 / (16 L^3) = T (12 B L^2 - T^2) / (16 L^3) = P / (16 L^3).
```

There is no lower-grade inhomogeneous source to mix through a unitriangular change of ordinary coordinates.

### Laurent extraction, inspected

`P` has degree at most nine (`T` degree 3, `12 B L^2 - T^2` degree 6). The generated reversal is

```text
Prev = sum_{k=0}^{9} [z^k] P · t^{9-k} = t^9 P(1/t).
```

With `s = pbase/2` and `L = z^2 + s`,

```text
L^3 = z^6 (1 + s t^2)^3,     P / L^3 = t^6 P(1/t) / (1 + s t^2)^3 = (Prev / t^3) (1 + s t^2)^{-3}.
```

The truncated binomial

```text
Inv3 = 1 - 3 s t^2 + 6 s^2 t^4 - 10 s^3 t^6 + 15 s^4 t^8 - 21 s^5 t^{10} + 28 s^6 t^{12}
```

is the expansion of `(1+X)^{-3}` through `X^6`, and the coefficients are `binom(n+2,2)`. Terms of `Inv3` beyond `t^{10}` cannot affect `[t^{10}](Prev Inv3)`, which is the highest coefficient extracted. Then `H = Prev Inv3 / 16` satisfies

```text
H / t^3 = P / (16 L^3)
```

as series in `t = z^{-1}` through the charged order, and

```text
h_ell = [t^{ell+3}] H = [z^{-ell}] P/(16 L^3),    ell = 1..7.
```

This is `z^{-1}` through `z^{-7}`, the first seven strictly negative coefficients. It is not `z^0` through `z^{-6}`, and it is not reversed.

### Faber transform, inspected

The printed transform is the expansion of `z^{-j}` in descending powers of `w`, for `w^2 = z^2 + pbase/2`. With `X = s/w^2` and `s = pbase/2`,

```text
z^{-j} = w^{-j} (1 - s/w^2)^{-j/2},
```

and the coefficient of `w^{-(j+2n)}` is

```text
( product_{k=0}^{n-1} (j/2 + k) ) / ( n!  2^n ) · pbase^n.
```

Odd `ell-j` vanish. The case `n=0` is `1`. The seven printed `RowCheck` formulae reproduce this matrix exactly, including

```text
g1 = h1,
g2 = h2,
g3 = (pbase/4) h1 + h3,
g4 = (pbase/2) h2 + h4,
g5 = (3/32) pbase^2 h1 + (3/4) pbase h3 + h5,
g6 = (1/4) pbase^2 h2 + pbase h4 + h6,
g7 = (5/128) pbase^3 h1 + (15/32) pbase^2 h3 + (5/4) pbase h5 + h7.
```

The matrix is lower unitriangular, hence invertible over every characteristic-zero field. Vanishing of `g_1..g_7` is equivalent to vanishing of `h_1..h_7`. At `pbase = 0` it is the identity.

The large equalities `RowCheck_ell = 0` are frozen exact-Q polynomial certificates that the divided source rows equal this Faber image. Both sides were inspected as displayed; the equality of the two large polynomials is the charged Q run, not a hand expansion of `tails.json`.

---

## 3. Completeness at this grade

The frozen tails are homogeneous of weight `12+ell` in `(a0..a6, k10, k6, k2)` with load weights `(2,6,10)`. After the chart substitution, `k10` is replaced by `Lambda kappa` and then multiplied by the load weight `Lambda^2`, so every `k10` monomial in `Phi_ell` is `O(Lambda^3)`. Analytically, the charged summand is `Lambda^2 k10 f^{5/4}`. With `k10 = Lambda kappa`,

```text
f^{5/4} = L^5 ( 1 + (5/4) X + O(X^2) ),
```

the `Lambda^3` term is `kappa L^5`, a polynomial of degree ten. It contributes no negative Laurent coefficient, hence no ordinary coordinate at this grade. The forbidden-variable check `diff(g, kappa)==0` is the corresponding source-side statement.

`k6` and `k2` are multiplied by `Lambda^6` and `Lambda^{10}`. After division by `Lambda^3` and setting `Lambda = 0` they vanish. Targets enter as `Lambda^{12+ell} mu`, which is `Lambda^{13}` through `Lambda^{19}`. The same vanishing holds.

On `p0moving`, every ordinary coefficient uses `pp = Lambda pt`, so the source is the complete family along the integral tangent. The generated script additionally requires `diff(g_ell, pt)==0`. The analytic comparison then uses `pbase = 0`, i.e. the boundary denominator `L = z^2`, as a model of that extracted grade. This does not replace the Lambda-dependent source denominator by its boundary before extraction: `Phi` is built from `pp = Lambda pt`, is certified `Lambda^3`-divisible as a polynomial, and its divided boundary is independent of `pt`.

Linear `R` and `S` are present in `P`, in `T` and `B`, and in the row identities. They are not set to zero.

### Seven rows suffice by degree

`deg P ≤ 9` and `deg L^3 = 6`, so

```text
P / L^3 = Q + R / L^3,    deg Q ≤ 3,    deg R < 6.
```

The negative part is `[R/L^3]_-`. Writing `R = r_5 z^5 + ⋯ + r_0`,

```text
R / L^3 = ( r_5 t + r_4 t^2 + ⋯ + r_0 t^6 ) (1 + s t^2)^{-3}.
```

The map `(r_5,…,r_0) ↦ ([z^{-1}],…,[z^{-6}])` is lower triangular with unit diagonal. Vanishing of the first six negative coefficients forces `R = 0`, i.e. `L^3 | P`. The seventh coefficient is redundant. Polynomial parts of `P/L^3` are discarded by the extraction of `t^{≥1}` and do not mix into `h_ell`.

At `p = 0`, `L^3 = z^6` and

```text
P / z^6 = (cubic polynomial) + [z^5]P · z^{-1} + ⋯ + [z^0]P · z^{-6},
```

with `[z^{-7}] = 0` automatically. Vanishing of `h_1..h_6` is exactly `[z^0]P = ⋯ = [z^5]P = 0`, i.e. `z^6 | P`.

---

## 4. Generic square consequence

Modulo `L`,

```text
T = 2 L R + M ≡ M,     12 B L^2 ≡ 0,
P = T (12 B L^2 - T^2) ≡ M ( - M^2 ) = -M^3.
```

This is a polynomial identity and does not use an engine. Thus `L^3 | P` implies `L | M^3`.

On fixed `p ≠ 0`, in characteristic zero: `L' = 2z`, and `gcd(z^2 + p/2, 2z) = 1` because a common root would force `p = 0`. So `L` is squarefree of degree two. If `M ≠ 0` then `deg M ≤ 1`. An irreducible quadratic cannot divide a power of a degree-`≤1` polynomial. A split squarefree quadratic has two distinct linear factors, both of which would have to divide `M`, forcing `deg M ≥ 2`. Hence `M = 0`.

The same conclusion holds along `p = Lambda p1` after extraction: the divided rows equal the `p = 0` Laurent transform, so the necessary condition is the quadruple-root condition of the next section, not a reduction of the moving denominator before taking `Lambda^3`.

---

## 5. Quadruple-root sharpening

Put `L = z^2` and `M = α z + β`, with `R = a z + b` and `S = u z + v` arbitrary linear. Then

```text
T = 2 z^2 (a z + b) + α z + β = 2 a z^3 + 2 b z^2 + α z + β,
P = 12 T B z^4 - T^3.
```

The summand `12 T B z^4` has valuation at least 4. The constant term of `T^3` is `β^3`. Therefore

```text
[z^0] P = - β^3.
```

This is independent of `a,b,u,v`. After `β = 0`,

```text
T = z (2 a z^2 + 2 b z + α),     T^3 = z^3 (2 a z^2 + 2 b z + α)^3,
```

so `[z^3] T^3 = α^3`. The product `T · 12 B z^4` now has valuation at least 5, hence does not contribute to degree 3. Therefore

```text
[z^3] (P | β=0) = - α^3,
```

again independent of linear `R,S`.

The seven vanished source rows, through the identity Faber matrix at `pbase = 0`, force `z^6 | P`. In particular `[z^0]P = 0` and `[z^3]P = 0`. In characteristic zero, `β^3 = 0` forces `β = 0` and then `α^3 = 0` forces `α = 0`. This is `M = 0` at the necessary third-tail gate, including the predecessor's leftover direction `M = α z`.

The predecessor obtained only `β = 0` at `s = 0`, because it reduced `L^3 | P` modulo the non-squarefree `L = z^2` and used `L | M^3`. The seven source rows give the full `L^3 | P`, which is `z^6 | P` rather than `z^2 | P`. That is the sharpening.

As a parenthetical converse, not required for necessity: if `M = 0` then `T = 2 L R` and

```text
P = 2 L R (12 B L^2 - 4 L^2 R^2) = 2 L^3 R (12 B - 4 R^2),
```

so `L^3 | P` automatically, at both generic `p` and `p = 0`. The third-tail gate is equivalent to `M = 0` on this charged source.

---

## 6. Strongest surviving theorem, exact scope, sharpest nonclaim

**Strongest surviving theorem.** Over every characteristic-zero field, in the matched square chart `K = L^2 + Lambda R`, `N = L M + Lambda S`, with integral load `k10 = Lambda kappa` of `Lambda`-order at least one, and with arbitrary linear `R,S` retained: if the seven complete frozen ordinary third-tail rows vanish, then `M = 0`. This holds for each fixed `p`, and it holds for the displayed integral tangent `p = Lambda p1`. In particular every named nonzero zero-load square or discriminant first direction, and the quadruple-root limit of those directions, fails this necessary gate.

**Exact scope.** The statement is a necessary condition at this grade for this charged source. It uses the frozen one-parameter rows, the displayed substitutions, and the Faber/Laurent identification of those rows with `[P/(16 L^3)]_-`.

**Sharpest nonclaim.** The theorem does not cover fractional or ramified positive-order slopes of `p` or `k10` relative to `Lambda`. It does not analyse any post-`M=0` cusp or odd face. It does not establish Newton-fan exhaustiveness. It does not impose the terminal `[6,2]` row or either Taylor family. It does not construct or exclude a strict arc. It does not close the square component, order two, or `(8,12)`. It does not prove maximum twelve. It does not prove JC2. The successor design is outside the review. `F_65521` is a software control and is not a characteristic-zero proof.

---

## Independent identities (hand)

```text
P ≡ -M^3 (mod L).                                         (generic reduction)

At L = z^2, M = α z + β, R,S arbitrary linear:
  [z^0] P = -β^3,
  [z^3] (P | β=0) = -α^3.                                  (quadruple-root)

f^{3/2} at Lambda^1, Lambda^2 is polynomial in z;
the Lambda^3 negative part is P/(16 L^3).                  (grade completeness)

deg L^3 = 6, deg P ≤ 9 ⇒ six negative Laurent
coefficients already force L^3 | P.                        (degree count)

Faber matrix is lower unitriangular with diagonal 1.       (ordinary ↔ Laurent)
```

ORDER2_SQUARE_THIRD_TAIL_SHARP_V2_CONFIRMED
