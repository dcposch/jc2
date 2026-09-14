## 3. Task (1): the non-degenerate case - the involution never produces a second polynomial solution

**Theorem 3.1 (exactly one polynomial root; the residual cubic is irreducible).** Let `(P, L)` be a polynomial solution of
(UF) with the marked jets, `b != 0`, `N = deg L >= 3`, on either root d. Then (i) L is the only polynomial root of
`Q_P(x, Y)` in Y; (ii) the cubic `C = Q_P/((3/16)(Y - L))` is irreducible over k(x); (iii) the second Hensel branch `L̃` is an
algebraic function of degree exactly 3 over k(x), convergent, and NOT a polynomial; (iv) `L̃ != L` (Prop. 2.3(c)).

*Proof.* Let M != L be a polynomial root. By §2 (edge polynomial), `deg M = N` and `lc(M) ∈ {-1/y, ±sqrt(omega/p̃)}` (not 1/y,
that branch is L: the ∞-branches are distinct). Apply (E-) to the pair (L, M): `tau'*Psi' = -b*q` with `tau' = L + M + b`,
polynomials. So `tau' | b*q` in k[x], and `b*q != 0` (`q(0) = b²`), hence `deg tau' <= deg q <= 2`. If `lc(M) != -1/y`, then
`deg tau' = N >= 3`: contradiction. If `lc(M) = -1/y`, then `deg tau' < N`, and writing `M = tau' - L - b`,
`Psi' = 2L² + 2bL - 8P - 4Bx + tau'² - tau'(2L + b)` has degree exactly 2N with leading coefficient `2/y² - 8 omega =
(2/y²)(1 - 4p) != 0`; then `deg(tau' Psi') = deg tau' + 2N > 2 >= deg(bq)` unless `tau' = 0`, and `tau' = 0` gives `0 = -bq`,
i.e. `b = 0`. Contradiction in every case: (i). A root of C in k(x) is integral over k[x] (C has constant leading coefficient),
hence a polynomial, hence (by (i)) equal to L; but `C(x, L) = (16/3)D ≢ 0`. So C has no root in k(x) and, being a cubic, is
irreducible: (ii). `L̃` is a root of C (it is a root of `Q_P` distinct from L, Prop. 2.3(c)), so (iii); convergence is Hensel's
lemma for the analytic quartic. ∎

**What this settles in Task (1).** (a) `L̃` is never a polynomial, for any b != 0, any t >= 2, either root d: the branch
"then `s = -(L + L̃)` and `p = L L̃` are polynomials" is EMPTY. Explicitly, polynomiality of s alone is already impossible:
`tau = L + L̃ + b = b - s` polynomial forces (as in the proof) `tau ≡ -b`, i.e. `s ≡ 2b`, `L̃ = -2b - L`,
and then (E-) reads `P = (L² + 2bL)/4 - Bx + (eta/3)x²`, whose leading coefficient gives `p = omega y² = 1/4`, i.e. `d = 0`:
incompatible with (UT)/(UL) at every N (it also forces `eta = 0`, since `tau_2 = l_2 + l̃_2 = -8eta/(3b)` must vanish).
(b) `L̃` is never transcendental (algebraic of degree 3, growth `|x|^N` on every continuation): no Gevrey obstruction exists.
(c) `L̃` continues along any path avoiding the <= 6N zeros of `Disc_Y(C)` onto one of the three branches of C at ∞:

```text
λ̃ = -1/y:            L̃_∞ = -L - b - b q/Psi_∞ = -L - b + O(x^{2-2N})  (eta != 0; O(x^{1-2N}) if eta = 0 != B; O(x^{-2N}) if B = eta = 0);
λ̃ = ±sqrt(omega/p̃):  L + L̃ ~ (1/y + λ̃) x^N;  the leading (E-) holds identically: 1/y² + λ̃² - 8omega = omega[(p+p̃)/(pp̃) - 8] = 0 (Vieta on (UT)).
```

All three are consistent for every N; the divisor of `tau` on the normalisation of C is
`Z_1 + Z_2 + (2N-2)∞_1 - N∞_2 - N∞_3` (eta != 0), of degree 0 for every N: the ∞-side pins nothing. (d) So the involution `ι: (P, L) ↦ (P, L̃)` maps every polynomial
solution to a convergent, algebraic, non-polynomial one, whether `j0 = 2` or `j0 >= 3`. **No contradiction follows from the
non-degenerate alternative.** (FALLACY-v2: the second branch is convergent and still proves nothing, because the polynomial
solutions are not closed under ι; "pinned at ∞" is a consistency, not a constraint.) What remains is §5.

Witness (t = 2, d = -1, `L = 5x³ - b`, `P = -L²/4`, `t2_family.out`): C irreducible over Q(b)[x, Y] (`factorize`);
`L̃ = -b - 15x³ + (100/b)x⁶ - (20000/b³)x¹² + ...` (Newton to order 40, residual 0; not a polynomial); `D = (15/2)L²x³`, `j0 = 3`;
the ∞-branch with lc -1/y is `-L - b - b³/(100x⁶) - ...` (residual 0 mod u³¹), `O(x^{-2N})` as predicted for `B = eta = 0`.
