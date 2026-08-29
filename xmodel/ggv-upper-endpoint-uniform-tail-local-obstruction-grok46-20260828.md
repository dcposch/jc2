# Uniform A-adic square-defect obstruction on the fixed branch-P endpoint

Date: 2026-08-28  
Author: Grok 4.6, independent lane  
Status: `EXACT THEOREM` (necessary A-adic cascade through `D8` on the full fixture; not an emptiness certificate for cutoffs 4, 3, or 2)

## EXACT THEOREM

Work over a characteristic-zero field, on the frozen branch-P square baseline

```text
A = X^4-1,   H = A^2,   F0 = H^2,   G0 = H^3,   F1 = H,   c2 = 0,
```

with the reviewed field-valued cascade

```text
F2 = (1 + H Z)/4,     deg Z <= 6,
F3 = (Z + A T)/8,     deg T <= 9,
```

later raw `F` windows free, `G` the unique characteristic continuation of `F` in `K(X)[[t]]`, and charged rows `D0=...=D21=0`, `D22=1` (no `D23`, no `G22` slot).  The authoritative raw source is

```text
cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
SHA-256 ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
```

Write `S` for the oriented square root of `F` in `K(X)[[t]]` with `S_0 = H`, so `F = S^2` and the principal characteristic summand is `F^{3/2} = S^3`.  Let `V` be the unique polynomial of degree at most `5` with `T = A V` whenever `A` divides `T`.

**Theorem 1 (D7 forces `A|T` on the full fixture).**  
On any characteristic-zero field point of the complete 303-variable/513-generator fixture (cutoff 2), and therefore also on every square-tail specialization with `Z = 0` (cutoffs 3 and 4),

```text
A divides T.
```

Rows `D0` through `D6` do **not** force this: `T` remains free in the reviewed cascade through weight six.  The first forcing row is `D7`.

The forcing identity is scheme-theoretic on polar numerators and only field-radical on `T` itself.  Precisely, as an identity of 0-jets along `A = 0` (i.e. in `Q[X]/(A)`), independently of the 0-jets of `Z, F4, F5, F6, F7`,

```text
A^2 (F^{3/2})_7  ≡  - (3/1024) T^2     (mod A).            (1.1)
```

The same-weight operator at weight 7 has no rational kernel, and the polynomial modes `k4, k6` contribute only polynomials at weight 7, so a polynomial raw `G7` exists if and only if `(F^{3/2})_7` is polynomial.  Polynomial-ness forces the left side of (1.1) to vanish, hence `T^2 ≡ 0 (mod A)`.  Since `A` is squarefree this yields `A|T` on field points, but does **not** put `T` in the nonreduced coefficient ideal.

**Theorem 2 (uniform D8 square defect, including restored `Z`).**  
After the field-radical step `T = A V` of Theorem 1, as an identity of 0-jets along `A = 0`, independently of the 0-jets of `F5, F6, F7, F8`,

```text
A^2 (F^{3/2})_8  ≡  (3/8) (F4 - V/16 - Z^2/64)^2     (mod A).   (2.1)
```

The weight-8 polynomial modes cannot cancel this order-2 polar part: `k4 F4` and `k8 (F^{1/2})_0 = k8 A^2` are polynomial, while `k6 (F^{3/4})_2` has A-adic valuation at least `-1`.  Thus every characteristic-zero field point satisfies

```text
A  divides  (F4 - V/16 - Z^2/64).
```

Specializations:

| cutoff | frozen data | D7 | D8 defect |
|---:|---|---|---|
| 4 | `Z = 0`, `T = 0` | vacuous | `A \| F4` |
| 3 | `Z = 0`, `T` live | `A \| T`, write `T = A V` | `A \| (F4 - V/16)` (matches the frozen tail-3 radical step) |
| 2 | `Z`, `T` live | `A \| T`, write `T = A V` | `A \| (F4 - V/16 - Z^2/64)` |

The only cutoff-2 correction relative to the tail-3 packet is the square-root term `Z^2/64 = S_2^2`.  There is no counterexample to `A|T` on the full fixture: restoring `Z` does not change (1.1).

**Theorem 3 (endpoint polar target, and why a fully polynomial square root dies).**  
The same-weight operator at the slotless row is

```text
L_22(R) = 2H ((12-22) H' R - 4 H R') = -8 A^3 (5 A' R + A R').
```

For every polynomial `R`, `A^3` divides `L_22(R)`, so `L_22(R)` cannot be the nonzero constant `-1`.  The unique rational solutions of `L_22(R) = -1` are

```text
R = (X^5/5 - X + c) / (8 A^5),     c in K,                        (3.1)
```

which is the diagnostic of `CHARACTERISTIC_CROSSCHECK.md`.  Consequently `D_22 = 1` requires the characteristic `g_22` to have polar order exactly five along `A = 0`, with that principal part.  If the square-root cascade of Theorems 1--2 continues until `S` is polynomial through the weights that feed `g_22`, then `g_22` is polynomial (the forced pole-cancelling constants `k_14, k_16, k_18, k_20` all vanish on the pure square tail `F = (H + t/2)^2`), hence `D_22` vanishes at every root of `A`, contradicting `D_22 = 1`.

Theorems 1--2 are the first two rungs of the cascade that produces this tension.  They do **not** by themselves prove emptiness at cutoff 4, 3, or 2: later holomorphic core equations (the tail-6/5 scalar identities) remain, and the cutoff-5 two-branch unit is still pending different-model review.

No Keller pair, unrestricted branch-P family, other GGV branch, or JC2 statement is claimed.

## 1. Exact setting and what was rederived

The D5G recurrence is

```text
D_n = sum_{i+j=n} ((12-j) F_i' G_j + (i-8) F_i G_j').
```

Same-weight contribution of a new `G_n` is the operator `L_n` of the reviewed cascade; `ker L_n` in `K(X)` is spanned by `H^{(12-n)/4}` when that exponent makes sense.  At `n = 7` one has `(12-7)/4 = 5/4`, not an integer, so `ker L_7 ∩ K(X) = 0`.  Characteristic modes through weight 8 are

```text
m=4: k4 t^4 F,     m=6: k6 t^6 F^{3/4},     m=8: k8 t^8 F^{1/2}.
```

The oriented square root is the recurrence `2 H S_n = F_n - sum_{i=1}^{n-1} S_i S_{n-i}` with `S_0 = H`, equivalently

```text
S_0 = H,     S_1 = 1/2,     S_2 = Z/8,     S_3 = T/(16 A),
S_4 = (F4 - T/(16 A) - Z^2/64) / (2 H),    ...
```

so `S_3` is regular along `A = 0` if and only if `A|T`.  The reviewed cascade through `D6` already makes `G_n = (S^3)_n` polynomial for `n <= 6` with `T` arbitrary; this is the precise counterexample to the hope that some row before `D7` forces `A|T`.

Cutoff dictionary, matching `tail_deformation.py`:

- cutoff 4: `z_* = tt_* = 0`, all raw slots of weight `>= 4` live;
- cutoff 3: `z_* = 0`, the ten `tt_*` (coefficients of `T`) restored;
- cutoff 2: the seven `z_*` (coefficients of `Z`) restored; this is the full fixture.

Cutoff 5 is used only as a pattern source.  Its two-branch field exclusion is **not** consumed as a hypothesis.

## 2. Proof of Theorem 1

### 2.1 The polar identity (1.1)

Let `R = Q[X]/(A)`.  This is étale of rank 4 (CRT: values at the four simple roots `1, -1, i, -i`).  Both sides of (1.1) are elements of `R`.  It is therefore enough to compute with remainders of degree `< 4`.

Take generic 0-jets

```text
Z ≡ z0 + z1 X + z2 X^2 + z3 X^3,
T ≡ t0 + t1 X + t2 X^2 + t3 X^3,
F4, F5, F6, F7 likewise,
```

in the polynomial ring on those 28 coefficients, form `S` by the square-root recurrence as A-adic rationals (numerator a polynomial, denominator a power of `A`, `A` extracted from the numerator whenever it divides), and set `y_7 = (S^3)_7`.  The computation terminates with `y_7 = N / A^2` where `A` does not divide `N`, and

```text
N mod A  =  - (3/1024) T^2 mod A
```

as an identity of 4-coefficient polynomials.  Expanded,

```text
X^0:  -3/1024 (t0^2 + 2 t1 t3 + t2^2)
X^1:  -3/512  (t0 t1 + t2 t3)
X^2:  -3/1024 (2 t0 t2 + t1^2 + t3^2)
X^3:  -3/512  (t0 t3 + t1 t2)
```

which is exactly `-3/1024 T^2` reduced modulo `X^4-1`.  No monomial in any `z_i` or later `F`-jet appears.  Evaluating at `X=1` recovers `-3/1024 T(1)^2`, and likewise at the other three roots.

Because the identity lives in `R`, higher-degree parts of `Z, T, F_{>=4}` (i.e. multiples of `A`) cannot contribute.  This is the universal 0-jet identity (1.1).

Replay: the 0-jet ring and A-adic square-root/cube used here are specified in §6.  An independent checker that implements only those operations and compares `y_7.num mod A` with `-3/1024 T^2 mod A` must print identity.

### 2.2 Polynomial modes cannot cancel the pole

The weight-7 characteristic coefficient is

```text
g_7 = (F^{3/2})_7 + k4 F_3 + k6 (F^{3/4})_1.
```

`F_3` is polynomial by construction.  The binomial recurrence for `y = F^{3/4}` gives, independently of all positive-weight `F`,

```text
y_0 = A^3,     A^4 y_1 = (3/4) F_1 y_0 = (3/4) A^5,     y_1 = (3/4) A,
```

which is polynomial.  The next mode `k8` starts at weight 8.  An order-2 pole in `(F^{3/2})_7` therefore survives in `g_7`.

### 2.3 From polar part to `D7`, then to `A|T`

The same-weight operator at `n = 7` is

```text
L_7(R) = 2H (5 H' R - 4 H R') = 20 A^3 A' R - 8 A^4 R'.
```

Direct evaluation on the leading polar part produces the polynomial identity

```text
L_7(1/A^2) = 36 A A',
```

hence

```text
L_7((F^{3/2})_7) ≡ (27/256) A A' T^2     (modulo functions with A-valuation >= 2).   (1.2)
```

For `T = 1` this is the explicit polynomial `(27/64)(X^3 - X^7) = -(27/64) X^3 A`.  For `T = X` the two sides of (1.2) match as global polynomials, not merely modulo `A^2`.

Same-row unknowns do not affect `D_7` modulo `A^3`: `F_0 = A^4` and `F_0' = 4 A^3 A'` so the `G_7` block is divisible by `A^3`, while `G_0 = A^6` and `G_0' = 6 A^5 A'` so the `F_7` block is divisible by `A^5`.  Thus on polynomial raw points

```text
D_7 ≡ - L_7(g_7)  (mod A^3).
```

In particular the coefficient of `A^1` in `D_7` is a unit times `A' T^2`.  At each simple root `A'(ρ) = 4 ρ^3 ≠ 0`, so `D_7 = 0` forces `T(ρ)^2 = 0`.  Squarefreeness of `A` gives `T(ρ) = 0` on a field, i.e. `A|T`.

On the nonreduced scheme the same calculation only puts `T^2` in the ideal `(A)` of 0-jets, not `T` itself.

### 2.4 Counterexample to any earlier row

Take `Z = 0`, `T = 1`, and `F_n = 0` for `n >= 4`.  Then `S = H + t/2 + t^3/(16 A) + ...` and the computed A-adic valuations of `S^3` are

```text
n:     0  1  2  3  4  5  6  7
val_A: 6  4  2  0  1  ∞  0 -2
```

so `S^3` is polynomial through weight 6 and first acquires an order-2 pole at weight 7, with numerator `-3/1024`.  This is a concrete polynomial solution of `D_0 = ... = D_6 = 0` with `A` not dividing `T`, as already parametrized by the reviewed cascade.  The first forcing row is exactly `D7`.

## 3. Proof of Theorem 2

Impose the field-radical conclusion of Theorem 1: `T = A V`.  Then `S_3 = V/16` is polynomial, and the square-root identity

```text
F4 = 2 H S_4 + V/16 + Z^2/64
```

holds as rational functions.  Repeating the 0-jet A-adic cube, now with generic 0-jets of `V, Z, F4, ..., F8` and with `T = A V` substituted, yields `y_8 = N / A^2` and

```text
N mod A  =  (3/8) (F4 - V/16 - Z^2/64)^2 mod A
```

as an identity (399-term numerator, 4 reduced coefficients, exact termwise match against the expanded square).  No `F5, F6, F7, F8` monomial appears.

Modes at weight 8: `k4 F4` is polynomial; `k8 (F^{1/2})_0 = k8 A^2` is polynomial; `(F^{3/4})_2` has A-adic valuation `-1` as soon as `Z(ρ)` or the defect is nonzero (explicitly, on `Z = 1, T = 0` the numerator modulo `A` is `3/32`).  An order-1 correction cannot cancel an order-2 polar part.  Hence polynomial `G8` forces the right-hand side of (2.1) to vanish, and squarefreeness of `A` gives the stated divisibility.

On cutoff 3 one has `Z = 0`, so the defect is `F4 - V/16`, recovering the frozen tail-3 step `D8: A | (F4 - V/16)^2`.  On cutoff 4 one has `Z = T = 0`, hence `V = 0` and `A | F4`.  The `Z^2/64` term is the only new summand at cutoff 2; omitting it fails the identity as soon as `Z(ρ) ≠ 0` (mutation in §7).

## 4. Proof of Theorem 3, and the uniform mechanism

The formula `L_22(R) = -8 A^3 (5 A' R + A R')` is elementary.  For polynomial `R` the prefactor `A^3` is visible, so `L_22(Q[X])` cannot contain the constant `-1`.  For the rational family (3.1), the `5 A' R` and `A R'` polar terms cancel and one is left with `- (num)' / A`; here `num' = X^4 - 1 = A`, so `L_22 = -1`, independently of `c`.  The `c / A^5` summand is exactly `ker L_22 = < A^{-5} >`.  This confirms the characteristic diagnostic: the slotless affine target is equivalent to `g_22` having principal part (3.1).

On the pure square tail `Z = T = F_{n>=4} = 0` one has `F = (H + t/2)^2` exactly, `S = H + t/2`, and `F^{3/2}` supported only in weights `0,1,2,3`.  Negative-power modes begin

```text
(F^{-1/4})_0 = A^{-1},   (F^{-1/2})_0 = A^{-2},
(F^{-3/4})_0 = A^{-3},   (F^{-1})_0   = A^{-4},
```

and `(F^{3/2})_{14,16,18,20}` vanish, so polynomial windows at those weights force `k_14 = k_16 = k_18 = k_20 = 0`.  Then `g_22 = 0`, `L_22(g_22) = 0`, and `D_22 = 0`, contradicting the affine target.  This is the empty deepest square-tail point; it is **not** emptiness of cutoff 4, which restores `F_{>=4}`.

The common mechanism behind the observed radical ladders is now visible and does not depend on the cutoff:

1. `D_n` modulo `A^3` is independent of the same-row slots, so it is a finite CRT 2-jet condition at the four roots of `A`.
2. That condition, for the first weights at which `S^3` can polarize, is that a universal multiple of the square of the previous square-root defect vanish along `A`.
3. Because `A` is squarefree, field points make the defect itself vanish, which is exactly one more step of polynomiality of `S`.
4. The endpoint wants the opposite: `g_22` must retain a precise order-5 pole.  Each successful square-defect step makes that pole harder to produce.

The tail-6 identities `F6 = H V` with `V0 ∈ {0, 4 F7[0]}`, and the tail-5 identities `K_17 = V0 (b V0 + R0^2)` together with the quadratic `12 τ^2 + 6 τ + 1 = 0`, are **holomorphic-core** relations at `X = 0` after this A-adic cascade has already run.  They are not the A-adic squares themselves, and they are not used here.

## 5. What this does and does not finish

Handled uniformly, for cutoffs 4, 3, and 2 at once:

- `D7` forces `A|T` (vacuous at cutoff 4);
- `D8` forces `A | (F4 - V/16 - Z^2/64)`;
- gcd/squarefree stratification is recorded at each step;
- restoring `T mod A` is killed at `D7`; restoring `Z` only corrects the D8 defect by `S_2^2`.

Not proved:

- emptiness of cutoff 4, 3, or 2;
- any later defect identity (`D9` onward: `W^2 mod A`, then `F5 - R/2`, etc.);
- the tail-5 two-branch unit (provisional, pending Fable review);
- a scheme-theoretic unit in the raw ideal (all square steps are field-radical);
- any statement about `D23`, `q1`, other branches, or JC2.

The natural induction is: after each square-defect vanishing, rewrite the next square-root coefficient as a polynomial plus `A^{-2}` times a new defect, and repeat the 0-jet cube.  Theorems 1--2 are the base and first successor.

## 6. EXECUTABLE REDUCTION / minimal compiler specification

An independent reviewer should implement the following and nothing else.  No Groebner basis, no local CAS, no AWS.

**Ring.**  Sparse polynomials over `Q` in one distinguished variable `X`, plus a finite list of jet indeterminates.  A-adic rationals are pairs `(num, val)` meaning `num / A^{val}`, with `A = X^4-1` extracted from `num` whenever it divides.

**Square root.**  `S_0 = A^2`.  For `n >= 1`,

```text
S_n = ( F_n - sum_{i=1}^{n-1} S_i S_{n-i} ) / (2 A^2).
```

**Cube.**  `(S^3)_n = sum_{i+j+k=n} S_i S_j S_k`.

**Test A (identity 1.1).**  Take `Z, T, F4, F5, F6, F7` generic of degree `<= 3`.  Build `F0..F3` from the cascade, run `S` through weight 7, and assert

```text
(S^3)_7 has val = 2,   and   num((S^3)_7) ≡ -3/1024 T^2  (mod A).
```

**Test B (identity 2.1).**  Take generic 0-jets `V, Z, F4, ..., F8`, set `T = A V`, run `S` through weight 8, and assert

```text
(S^3)_7 is polynomial,   (S^3)_8 has val = 2,
num((S^3)_8) ≡ 3/8 (F4 - V/16 - Z^2/64)^2  (mod A).
```

**Test C (`L_22`).**  With `num = X^5/5 - X`, assert `L_22(num/(8 A^5)) = -1` and `L_22(1/A^5) = 0` as rational identities.

**Test D (no earlier forcing).**  `Z = 0`, `T = 1`, later `F` zero: `(S^3)_n` polynomial for `n <= 6`, first pole at `n = 7`.

**Optional raw-span check, not used in the proof.**  From `RAW_DIRECT_SYSTEM.json`, the cutoff-3 compiler of `cases/ggv_8_28_upper_endpoint_tail3_desk_20260828/analyze_tail3.py` already exhibits `T^2 mod A` as the D7 compatibility span at `Z = 0`.  A cutoff-2 analogue (keep `z_*` live) should reproduce the same four T-quadratics and no extra 0-jet condition; that is a raw-row cross-check of (1.1), not an independent source of (1.1).

Branch coverage of the compiler:

- generic 0-jets (the identities);
- `T = 0` (cutoff 4 D7 vacuous, D8 reduces to `F4 - Z^2/64`);
- `Z = 0` (tail-3 D8);
- `Z = T = 0` (pure square tail);
- `T = A V` with `V` generic (post-D7 stratum);
- later `F` jets switched on and off (independence).

## 7. Mutation tests

All of the following fail exactly as predicted.

| mutation | observed residual |
|---|---|
| replace `-3/1024` in (1.1) by `-3/512` | `num((S^3)_7) mod A` no longer equals the right-hand side (`T = 1` gives `-3/1024` vs `-3/512`) |
| drop `Z^2/64` from (2.1) | on `Z = 1, T = 0, F4 = 1`, left side is `11907/32768`, right side without `Z^2/64` is `3/8 = 12288/32768` |
| claim `D6` already forces `A\|T` | the specialization `T = 1, Z = 0, F_{>=4} = 0` has polynomial `S^3` through weight 6 |
| claim (1.1) depends on `Z` | generic 0-jets of `Z` are absent from the reduced numerator |
| claim `k6` cancels the D7 pole | `(F^{3/4})_1 = (3/4) A` is polynomial for every `F` |
| claim a polynomial `g_22` can produce `D_22 = 1` | `A^3` divides `L_22(Q[X])` |
| treat `T^2 ≡ 0 mod A` as a scheme unit `T ∈ (A)` | `A` squarefree is used; the nonreduced ideal need only contain `T^2` along `A = 0` |

A live coefficient mutation of a used D7 source row, once a cutoff-2 raw-span checker exists, must destroy membership of `T^2 mod A` in the compatibility span.

## 8. Scope firewall

- Fixed branch-P square baseline only.  Branch Q, other GGV faces, and the unrestricted family are untouched.
- Characteristic zero is used for squarefreeness of `A` and for the rational characteristic continuation (division by `n` and by `A^4`).
- Field points versus scheme: Theorems 1 and 2 give field-radical divisibilities.  Identities (1.1) and (2.1) of polar numerators are polynomial identities in the 0-jet ring.
- 0-jets at roots of `A` are local values of global polynomials, not a substitute for the global `H`-multiple in the Morse cokernel of `X^8-1`.  That seven-vector is a different operator on a different `H` and is not used.
- No endpoint carrier (`p32, p86, p91, F7[0]`, ...) is inverted or set to 1.
- Cutoff 5 is not an input.  Its scalar core and D18 unit, if promoted, sit *after* the present A-adic cascade.
- `D23` is not imposed and there is no `G22` slot.
- A timeout, modular point, proper ideal, or partial basis is not invoked and would not be evidence.

## 9. Ranked next action

1. **Continue the 0-jet defect recurrence one row at a time** with the same compiler (no cutoff specialization).  The predicted D9 step, after writing `F4 - V/16 - Z^2/64 = A W`, is that `(F^{3/2})_9` has polar numerator a universal multiple of `W^2`, forcing `A|W` on field points; then `F5 - R/2` with `W = A R`, and so on.  Freeze each identity as a 0-jet equality with the same mutation table.  This is the induction that actually consumes cutoffs 4, 3, and 2 simultaneously.
2. **Only after the A-adic defects are killed**, extract the remaining holomorphic core (constant-term / `X = 0` invariants generalizing `K_17` and the tail-6 `V0 ∈ {0, 4 F7[0]}`) and attempt a two-branch unit against `1 + a b - c d = 0`.  Do not import the cutoff-5 unit; rederive it with the extra defect polynomials set to their forced `A`-multiples.
3. **Raw-span cross-check of (1.1) at cutoff 2**, tracking every D7 compatibility to literal generators in `RAW_DIRECT_SYSTEM.json`, with `z_*` live.  This is corroboration, not a second proof.
4. Do not launch AWS on the full 303-variable ideal, and do not normalize carriers, until the defect recurrence has either produced a unit or isolated a genuine holomorphic leftover of small degree.

The cheapest exact object that can be compiled and reviewed immediately is Test A of §6: a 28-variable 0-jet identity whose output is four explicit quadratics in the `t_i`.
