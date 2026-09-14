## 2. The four objects and the exact identities behind the dichotomy (PROVED-HERE; generic jets, K = 10)

Everything here is an identity in the free jets `(b, B, eta, w_2, l_2, l_3, ...)` with `P_k = Φ_k`, proved below and
machine-checked to order K = 10 (`tacnode_involution.py`, `_K10.json`: ALL_PASS, 70 s). Correction to the charged Prop. 4.1: the
Y¹-coefficient of `Q_P` is `-((eta b/2)x² + (3/2)bP)`, of x-degree **2N**, not 3N; so the Newton polygon at x = ∞ is one edge of
slope N with edge polynomial `(3/16)λ⁴ - (3/2)omega λ² - (4N-3)omega² = -λ⁴*(UT)(omega/λ²)` (checked): four distinct unramified
branches of order `x^N`, `λ ∈ {±1/y, ±sqrt(omega/p̃)}` (`p̃` the other root of (UT)). Nothing below depends on the mis-stated degree.

**Proposition 2.1 (the difference equation is algebraic).** Let `Y_1, Y_2` be any two roots of `Q_P(x, *)` in `k[[x]]`
(or in any extension), `sigma = Y_1 + Y_2`, `pi = Y_1Y_2`, `tau = sigma + b`, and

```text
q(x)   := b² + 4Bx - (8 eta/3) x²,
Psi    := Y_1² + Y_2² + b(Y_1 + Y_2) - 8P - b² - 4Bx.
Then  (E-):     tau * Psi  =  -b * q(x).
```

*Proof.* `Q_P(Y_1) - Q_P(Y_2) = [R(Y_1) - R(Y_2)] - P[G(Y_1) - G(Y_2)]` with `G(Y_1) - G(Y_2) = (3/2)(Y_1 - Y_2)(sigma + b)`,
`R(Y_1) - R(Y_2) = (Y_1 - Y_2)[(3/16)sigma(sigma² - 2pi) + (3/8)b(sigma² - pi) - (3/4)Bx sigma - (eta b/2)x²]`; divide by
`Y_1 - Y_2`, multiply by 16/3, and write `sigma = tau - b` on the right. (The other remainder coefficient of
`Q_P mod (Y² - sigma Y + pi)` involves `P'` and is (UF) itself once (E-) holds.) ∎

**Proposition 2.2 (the residual cubic, in the variable tau).** With `L` the polynomial root and `Y = tau - L - b`,

```text
C_tau(tau) = tau³ - (2L + b) tau² + (2L² + 2bL - b² - 8P - 4Bx) tau + b*q(x)   ( = (16/3)*Q_P/(Y - L) ),
C_tau|_{x=0} = (tau + b)(tau² + b²):   the branch L̃ has tau(0) = -b, the branches through ±ib have tau(0) = ±ib.
```

The product of the three roots is `-b*q(x)`, a polynomial of degree <= 2. With `delta = L̃ - L = tau - A`, `A := 2L + b`:

```text
delta³ + 2A delta² + D_1 delta + D_0 = 0,    D_1 = (3/2)(A² - b²) - 8P - 4Bx,   D_1(0) = 2b²,
D_0 = A[(A² - 3b²)/2 - 8P - 4Bx] + b q  =  (16/3) D,      D := d_Y Q_P(x, L(x)) = R_Y(x, L) - (3/2)(2L + b) P.
```

**Proposition 2.3 (the pivot chain is the polynomial D).** (a) `[x⁰]D = [x¹]D = 0` are the jets `P(0) = -b²/4`, `P'(0) = -B`
(the graph of L is tangent to C at (0, -b)); `[x²]D = (b/4)Lpivot`;
`[x³]D = (3/4)(2 B l_2 + b² l_3 + 2 b w_2)` IDENTICALLY - the charged "second pivot" is unconditional and eta-free;
for every j >= 2, `[x^j]D = (3/4) b² l_j + f_j(b, B, eta, w_2, l_2, ..., l_{j-1})`. (b) With P fixed, `d row_k/dl_m = -[x^{k-m}]D` (k >= 4, 2 <= m <= k; 42 pairs checked): the k-independent pivots of the charged
Props. 2.2/4.2 and of `degenerate_pivot.json` are the coefficients of the one polynomial D. (c) `deg_x D = 3N` with `lc D = (3/(4y³))(1 - 4p) != 0` (`p != 1/4` since `d != 0`); hence

```text
j0 := ord_0 D = ord_0 (L̃ - L) ∈ [2, 3N],   delta = -(D_0/D_1)(1 + ...),   delta_2 = -(2/(3b))*Lpivot,   Lpivot² = (9b²/4)*[x⁴]Disc(F_0).
```

j0 is the intersection multiplicity at (0, -b) of the graph of L with the residual cubic C; the tacnode is non-degenerate iff
j0 = 2. Since `D ≢ 0`, `F_0 = (Y - L)(Y - L̃)` is never a square: **L̃ != L for every polynomial solution with b != 0**.

**Proposition 2.4 (the Hensel factor, P-only through order 3).** `F_0 = Y² + sY + p` with

```text
s = 2b + (8eta/(3b)) x² + (4w_2/b - 16B eta/(3b³)) x³ + s_4 x⁴ + ...,     p = b² + (8eta/3) x² + (4w_2 - 16B eta/(3b²)) x³ + p_4 x⁴ + ...,
s_4, p_4 affine in P_4 (closed forms in disc4_check.json),
Disc(F_0) = s² - 4p = 0*x⁰ + 0*x¹ + 0*x² + 0*x³ - (16/(9b²))*T_2 * x⁴ + ...,      T_2 := 3b² P_4 + 18 B w_2 - 10 eta².
```

(`disc4_check.json`; `s_1 = p_1 = 0`.) `F_0` is a function of P alone; the first discriminant coefficient not forced to vanish by the jets is `T_2`.
