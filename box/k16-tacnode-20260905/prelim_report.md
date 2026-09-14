# UNIFORM lane: the tacnode dichotomy on (UF) - the second Hensel branch L̃ is NEVER a polynomial (the residual cubic is irreducible), so the involution yields no second solution and no contradiction; the dichotomy iterates as the contact order j0 = ord_0 d_Y Q_P(x, L) ∈ [2, 3N]; the OPEN is one quadratic relation on the 4-jet of P; no uniform theorem, (R) not proved

Lane: `k16-tacnode-fable5-20260905`. Fable 5.1. 2026-09-05. Basis `57ba54fa`.

**VERDICT: NO uniform theorem is obtained; the tacnode statement (`4eta + 3bl_2 ∈ rad J_t` for every t) is NOT proved; (R) is not proved; theorem (T) is not promoted for any new index.** PROVED-HERE as structure: the non-degenerate alternative cannot be excluded by the involution, because `L̃` is never a polynomial and never equals L (Theorem 3.1); the dichotomy iterates as the coefficient chain of the single polynomial `D = d_Y Q_P(x, L(x))` of degree 3N, and its termination forces nothing about `B*eta` (§4); the OPEN is equivalent to the vanishing on `V(J_t)` of the P-only quadratic `T_2 = 3b²w_3 + 18Bw_2 - 10eta²`, i.e. `6P_0P_4 + 9P_1P_3 + 5P_2² = 0`, i.e. `ord_0 Disc_Y(Q_P) >= 6` (§5). All identities verified exactly on the frozen t = 3, 4 certificates and modularly at t = 5.

```text
REQUESTED  (1) non-degenerate case: L̃ polynomial (then s, p polynomial: derive, compatibility with deg P = 2N and (UT))
           or transcendental with an incompatible growth type; involution / ∞-expansions;  (2) degenerate case: reduced
           recursion, iteration, descent, termination, does it force B*eta = 0;  (3) exact checks at t = 3, 4, 5;  (4) verdict.
ANSWER     (1) Neither. THEOREM 3.1: for b != 0 the quartic Q_P has exactly ONE polynomial root (L), the residual cubic is
               irreducible over k(x), F_0 is never a square. Key: for any two roots the difference of the equations is the
               ALGEBRAIC identity (E-) tau*Psi = -b*q, tau = L + L̃ + b, q = b² + 4Bx - (8eta/3)x²; a polynomial second root
               forces tau | b*q (deg <= 2) against deg tau = N >= 3, or tau -> 0 at ∞ on the lc = -1/y branch, hence b = 0.
               Polynomial s alone forces s ≡ 2b and P = (L² + 2bL)/4 - Bx + (eta/3)x², i.e. p = 1/4, d = 0: incompatible
               with (UT) at every N. L̃ is algebraic of degree 3, convergent, continues to ∞ onto one of three branches
               (lc ∈ {-1/y, ±sqrt(omega/p̃)}), all consistent for every N: the involution gives NO contradiction.
           (2) The dichotomy iterates exactly: d row_k/dl_m = -[x^{k-m}]D with D = d_Y Q_P(x, L), deg D = 3N; the j-th pivot
               is [x^j]D = (3/4)b² l_j + f_j; [x²]D = (b/4)Lpivot; [x³]D = (3/4)(2Bl_2 + b²l_3 + 2bw_2) identically.
               j0 = ord_0 D = ord_0(L̃ - L) ∈ [2, 3N] terminates for every solution and forces nothing (t = 2 family:
               j0 = 3 = N, second pivot (15/2)b² != 0, B = eta = 0 for the independent reason c = 0); it descends in j, not in N.
           (3) On the frozen data: D = x²D̂, [x²]D = (b/4)Lpivot, [x³]D = (3/4)piv_2 (cofactor 0), Lpivot² = -4T_2 - 24E_2
               EXACTLY (t = 3, 4 over Q(d); t = 5 mod p), [x⁴]Disc(F_0) = -16T_2/(9b²); all pivots and T_2 ∉ J (non-vacuous);
               NEW: B*eta ∈ J + (Lpivot) at t = 3 (weight 13 < socle 14) but not at t = 4, 5 (non-vacuous).
           (4) No uniform theorem; the tacnode statement is not proved; the residual is the jet-quadratic
               T_2 = 3b²w_3 + 18Bw_2 - 10w_1² ∈ rad J_t  <=>  6P_0P_4 + 9P_1P_3 + 5P_2² = 0 on every solution  <=>  ord_0 Disc_Y(Q_P) >= 6.
CUSTODY    4/4 input hashes OK (awk manifest, sha256sum -c); frozen controls_t{3,4}_raw.sing reproduced by imap (identity map);
           frozen universal_recursion/tacnode_checks/degenerate_pivot JSONs re-derived; generic jets to K = 10: ALL_PASS.
NOTIFY     not warranted (no new index, no exit claim; charge_basis inapplicable).
```
## 1. Custody

The receipt `xmodel/k16-tacnode-fable5-20260905.run.v2` was parsed with `awk -F=`, pairing each `charged_input_<i>_sha256=`
with its `_basename=` into `box/k16-tacnode-20260905/manifest.sha256`; `sha256sum -c` returned **4/4 OK** before any input
was opened (re-run at sealing: `input-verification-final.log`). No digest was retyped. Basis `57ba54fa`. The four charged
inputs were read from `/tmp/jc2-lane.WnfxfS/inputs`. Consumed: from the charged universal-series report (UF) in Euler form, `Φ_k`, Props. 2.2, 4.1, 4.2, 4.3 and the frozen
`universal_recursion / tacnode_checks / degenerate_pivot` drivers and JSONs in `box/k16-universal-20260905/`; from the charged
abel-polysol report (I1)–(I4), Theorem H and the pivot laws; from the charged Astra report (UF), (UJ), (UL), (UT), the t = 2
family and the `b = 0` chart (§7.3). The frozen certificates replayed are
`box/k16xempty-20260905/controls_t{3,4,5}_raw.sing` (byte-unchanged, identifiers renamed on import), compared under the
identity map on `(c_i, b)` by `imap`, exactly as in the charged `custody_bu.py`. No ledger, `jc2-lean` or `ideation-*` file
was read or written. All drivers and transcripts are in `box/k16-tacnode-20260905/`.

Notation (charged §7.1): `N = t+1`, `q_deg = 2N-1`, `theta = x d/dx`, `G = (3/2)L(L+b) - Bx`,
`R = (3/16)L²(L(L+2b) - 4Bx) - eta*x²(bL/2 + Bx)`; (UF) is `(theta-3)(P²) + G*P = R`. `L = -b + Σ_{j>=2} l_j x^j`
(on the ray `l_j = c_{N-j}/y`, `l_N = 1/y`, `l_j = 0` for `j > N`), `P = Σ P_k x^k` with `P_0 = -b²/4`, `P_1 = -B`,
`P_2 = eta = w_1`, `P_3 = w_2`, `P_4 = w_3` (`w_i` = Astra's coefficients of W). `p = omega*y²`, `3d² = N`, `p = 1/(4(2d+1))`.
`Q_P(x, Y) = R(x,Y) - G(x,Y)P - (theta-3)(P²)` (quartic in Y, leading coefficient 3/16). The tilde in `L̃` is a label, never
a derivative; `Lpivot := 4eta + 3bl_2`; `piv_2 := 2Bl_2 + b²l_3 + 2bw_2`. Throughout `b != 0` (§5 end for b = 0).
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
(the graph of L is tangent to C at (0, -b)); `[x²]D = (b/4)(4 eta + 3 b l_2)` (the charged L-pivot);
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
s_4 = 8(12B² eta + 6 b⁴ P_4 + b² eta²)/(9b⁵),   p_4 = 4(24B² eta + 18B b² w_2 + 15 b⁴ P_4 - 4 b² eta²)/(9b⁴)   (affine in P_4),
Disc(F_0) = s² - 4p = 0*x⁰ + 0*x¹ + 0*x² + 0*x³ - (16/(9b²))*T_2 * x⁴ + ...,      T_2 := 3b² P_4 + 18 B w_2 - 10 eta².
```

(`disc4_check.py/.json`; `s_1 = p_1 = 0`; `s_{>=4}` depend on `l_2, l_3, ...` only through `P_{>=4}`.) The Hensel factor is a
function of P alone, and the first coefficient of its discriminant not forced to vanish by the jets is the quadratic `T_2`.
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
(b) `L̃` is never transcendental: algebraic of degree 3, of polynomial growth `|x|^N` on every continuation; no Gevrey or
growth obstruction exists. (c) `L̃` continues along any path avoiding the <= 6N zeros of `Disc_Y(C)` onto one of the three
branches of C at ∞:

```text
λ̃ = -1/y:            L̃_∞ = -L - b + tau_∞,   tau_∞ = -b q/Psi_∞ = O(x^{2-2N})  (eta != 0),  O(x^{1-2N}) (eta = 0 != B),  O(x^{-2N}) (B = eta = 0);
λ̃ = ±sqrt(omega/p̃):  L + L̃ ~ (1/y + λ̃) x^N,   and the leading term of (E-) holds identically because 1/y² + λ̃² - 8 omega =
                      omega[(p + p̃)/(p p̃) - 8] = 0  by Vieta on (UT)   (checked).
```

All three are consistent for every N; the divisor of `tau` on the normalisation of C is
`Z_1 + Z_2 + (2N-2)∞_1 - N∞_2 - N∞_3` (eta != 0), of degree 0 for every N: the ∞-side pins nothing. (d) Exactly one branch
has `lc = 1/y` at ∞ (namely L); the question of a second polynomial solution with the same normalisation never arises, since
`L̃` is not a polynomial with ANY leading coefficient. (e) So the involution `ι: (P, L) ↦ (P, L̃)` maps every polynomial
solution to a convergent, algebraic, non-polynomial one, whether `j0 = 2` or `j0 >= 3`. **No contradiction follows from the
non-degenerate alternative.** (FALLACY-v2: the second branch is convergent and still proves nothing, because the polynomial
solutions are not closed under ι; "pinned at ∞" is a consistency, not a constraint.) What remains is §5.

Witness (t = 2, d = -1, `L = 5x³ - b`, `P = -L²/4`, `t2_family.out`): `factorize` gives C irreducible over Q(b)[x, Y];
`L̃ = -b - 15x³ + (100/b)x⁶ - (20000/b³)x¹² + ...` (Newton to order 40, residual 0; not a polynomial); `D = (15/2)L²x³`, `j0 = 3`;
the ∞-branch with lc -1/y is `-L - b - b³/(100x⁶) - ...` (residual 0 mod u³¹), `O(x^{-2N})` as predicted for `B = eta = 0`.
## 4. Task (2): the degenerate case - the dichotomy iterates as the chain [x^j]D, terminates, and forces nothing

**The reduced recursion.** On `Lpivot = 0`, by Prop. 2.3(b), row k (k >= 6) is linear in `l_{k-3}` with the k-independent
coefficient `-[x³]D = -(3/4)piv_2`; row 5 is quadratic in `l_2` and row 6 in `l_3`. On `piv_2 != 0` the charged dual recursion
becomes `l_{k-3} = [rest'_k - (k-3)b²P_k/2]/((3/4)piv_2)` (k >= 7), `l_3` fixed by row 6: the cascade of
`degenerate_pivot.json`, now identified as the coefficients of D.

**Iteration.** The tangent cone of `Q_P` at (0, -b) in weight (1, 2) is `(3/8)b²(ℓ - l_2x²)(ℓ - l̃_2x²)`; on the degenerate
locus it is a square and the two branches are separated at the first order j with `[x^j]D != 0`, because
`delta = L̃ - L = -(D_0/D_1)(1 + ...)` with `D_1(0) = 2b²` a unit. So the dichotomy iterates as the chain

```text
level j (j = 2, 3, 4, ...):   [x^j]D = (3/4) b² l_j + f_j(b, B, eta, w_2, l_2, ..., l_{j-1})   is either != 0 (j0 = j)  or  = 0 (go to j+1),
```

a k-independent pivot at every level, linear in the new L-jet `l_j` with the unit coefficient `(3/4)b²`. On the fully
degenerate chain (`[x^2]D = ... = [x^{m}]D = 0`) the L-jets are determined by `(b, B, l_2, w_2)` (eta = -(3/4)bl_2):

```text
l_3 = -2(Bl_2 + bw_2)/b²,   l_4 = (16B²l_2 + 64Bbw_2 - 21b³l_2²)/(4b⁴),   l_5 = (-32B³l_2 - 368B²bw_2 + 123Bb³l_2² + 52b⁴l_2w_2)/(4b⁶), ...
```

(closed forms to `l_9` in `tacnode_involution_K10.json`, key `l_j_on_full_degenerate_chain`; each is weighted-homogeneous of
weight N - j). The infinite chain is the locus `D ≡ 0`, i.e. `F_0 = (Y - L)²`, a 4-parameter formal family (3 after G_m) which
contains NO polynomial L (Theorem 3.1(iv)). Hence:

**Proposition 4.1 (termination).** For every polynomial solution with b != 0 the chain terminates at a finite level
`j0 = ord_0 D <= 3N`, and `j0 >= 3` is exactly the tacnode statement. Termination by itself forces nothing about `B*eta`:
the exceptional t = 2 family terminates at `j0 = 3 = N` with `[x³]D = (15/2)b² != 0` (`piv_2 = 10b²`), and its `B = eta = 0`
is the weight-forced vanishing on the axis `c = 0` (charged abel-polysol §5), not a consequence of the termination. The
chain moves in the x-order j, never in N or t: it is a descent on the jet data of ONE solution, not a descent on the index,
and it produces no induction. What it does produce is the reformulation of §5 (the first level in P-only terms).

**Does j0 >= 3 with the truncation force B*eta = 0?** Level j ties `P_j` to `l_2..l_j` (`[x^j]D_0 ∋ 8bP_j + 4b²l_j`), one
P-jet per level; for `j0 - 1 >= N` the chain would fix `l_N = 1/y`, `l_{N+1} = 0` as weight-2N, 2N+1 relations among
`(b, B, l_2, w_2)`; no bound on j0 in terms of N is known (`OPEN[K16-UF-CONTACT-ORDER-BOUND]`; `j0 = N` in the only known
nontrivial solution). At t = 3, 4, 5 the chain is invisible: every `[x^j]D` is nilpotent mod J but not in J (§6): the scheme
`V(J)` has `j0 = 2` to first order and only its reduction has `j0 >= 3`.
## 5. The OPEN as one quadratic relation on the 4-jet of P (PROVED-HERE equivalences)

**Theorem 5.1.** On every polynomial solution (b != 0), with `T_2 := 3b² P_4 + 18 B w_2 - 10 eta² = 3b² w_3 + 18 B w_2 - 10 w_1²`,

```text
(i)   Lpivot² = (4eta + 3bl_2)² = -4*T_2 - 24*E_2            EXACTLY (E_2 = row 4 of (UF); so Lpivot² ≡ -4T_2 mod J),
(ii)  [x⁴] Disc(F_0) = -(16/(9b²))*T_2 = (4/(9b²))*Lpivot²  (mod E_2),   [x^j] Disc(F_0) = 0 for j <= 3 automatically,
(iii) ord_0 Disc_Y(Q_P) = 2 j0 = 4 + 2*ord_0 D̂  (Disc_Y(Q_P) = D²*Disc_Y(C), Disc_Y(C)(0) != 0),
(iv)  T_2 = -2(6 P_0 P_4 + 9 P_1 P_3 + 5 P_2²).
```

Hence the following are equivalent for a polynomial solution with b != 0: the tacnode is degenerate; `Lpivot = 0`;
`T_2 = 0`; `6P_0P_4 + 9P_1P_3 + 5P_2² = 0`; `ord_0 Disc_Y(Q_P) >= 6`; `j0 >= 3`. And
**`OPEN[K16-UF-DEGENERATE-TACNODE]` <=> `T_2 ∈ rad J_t` for every t**, a statement about the 4-jet of P alone (weight 4t,
one less than `B*eta`), equivalently about the order of the discriminant of the quartic at the marked point.

*Proof.* (i): row 4 is `E_2 = -(b²/2)(P_4 - Φ_4)` with `Φ_4 = (2/b²)(eta² - 3Bw_2 - b eta l_2 - (3/8)b² l_2²)`; then
`T_2 = 3b²(P_4 - Φ_4) + 3b²Φ_4 + 18Bw_2 - 10eta² = -6E_2 - (1/4)(4eta + 3bl_2)²`. (ii): Prop. 2.4 and (i). (iii): the
factorisation of the discriminant and `Disc(F_1)(0) = -4b²`, `Res(F_0, F_1)(0) = 4b⁴`. (iv): `b² = -4P_0`, `B = -P_1`,
`w_2 = P_3`, `eta = P_2`. All four verified exactly on the frozen data (§6) and generically (`disc4_check.json`,
`tacnode_involution_K10.json`). ∎

Remarks. `T_2` is not the classical invariant `12P_0P_4 - 3P_1P_3 + P_2²` of the binary quartic. On `b = 0` (where
`Q_P(0, Y) = (3/16)Y⁴` and the tacnode picture does not apply) the OPEN reads `eta ∈ rad(J + (b))` and (i) gives
`18Bw_2 - 6eta² ∈ J + (b)`, so there it is equivalent to `B*w_2 ∈ rad(J + (b))`; no claim is made on b = 0 (Astra's chart, charged §7.3).
## 6. Task (3): exact verification at t = 3, 4, 5 against the frozen certificates

Driver `custody_tacnode.py` (`custody_tacnode_t{3,4}.sing` exact over `Q(d)`, `minpoly 3d² - N`; `_t{3,4,5}_p31991_d{14162,4933,6434}.sing`
modular controls, `--hensel` adds the b = 1 Hensel replay) replays the frozen top-down data as the charged `custody_bu.py` does,
builds `Q_P(x, Y)` with a ring variable Y, `D = d_Y Q_P(x, L)`, `Lpivot`, `piv_2`, `T_2`, and tests in `S = k[c, b]` (weights `wt c_j = j`, `wt b = N`).

```text
t  frozen rows/B/eta/T   [x⁰]D=[x¹]D=0  [x²]D=(b/4)Lpivot  deg D, lc   [x³]D-(3/4)piv_2  Lpivot²+4T_2+24E_2  Q_P(x,L)+UF  std(J) dim,vdim  socle
3  equal (exact)         yes            yes                12, yes     0 (cofactor 0)    0 (exact)            0 (exact)    0, 66            14
4  equal (exact)         yes            yes                15, yes     0 (cofactor 0)    0 (exact)            0 (exact)    0, 338 (10 s)    21
5  (mod p control)       yes            yes                18, yes     0 (cofactor 0)    0 (mod p)            0 (mod p)    0, 1709          30
```

Every entry in the first eight columns is a polynomial identity in `k[c, b]` (not a membership) and is non-vacuous; the
weights are `wt [x^j]D = 3N - j`, `wt Lpivot = 2t`, `wt piv_2 = 3t`, `wt T_2 = 4t`, `wt B*eta = 4t + 1`. (`homog` and the
weight of every `[x^j]D` were checked: `D_WEIGHTS_CHECKED`.)

**Memberships in J (socle-degree caveat as in the charged §5: a membership whose weight exceeds the socle degree is
weight-forced and is no evidence; a NON-membership at weight <= socle is non-vacuous).**

```text
t  Lpivot ∈ J / min power   piv_2 ∈ J / min power   T_2 ∈ J / min power   [x^j]D ∈ J (j = 2..3N-1)   Lpivot² ∈ J   Lpivot*B, Lpivot*eta ∈ J
3  no / 3 (wt 18: vacuous)   no / 2 (vacuous)         no / 2 (vacuous)       none; min powers 2,2,2,3,3,3,4,5,8,9   no (wt 12)   no, no (wt 13, 12)
4  no / 3 (vacuous)          no / 2 (vacuous)         no / 2 (vacuous)       none (j = 2..14)                       no (wt 16)   no, no
5  no / 4 (Lpivot³ ∉ J: wt 30, non-vacuous)  no / 3 (piv_2² ∉ J: wt 30, non-vacuous)  no / 2 (vacuous)  none (j = 2..17)  no (wt 20)   no, no
```

So at every verified index the scheme `V(J)` does NOT satisfy the tacnode relation (`Lpivot`, `T_2`, every `[x^j]D` ∉ J);
only its reduction does (`rad J = m`): at t <= 5 the statement carries no content independent of the banked `V(J) = {0}`.

**The degenerate stratum `J_deg = J + (Lpivot)` and the target (new, exact).**

```text
t  vdim J_deg   (B*eta)^n ∈ J_deg: min n   non-vacuous?          B, eta, piv_2 ∈ J_deg   vdim J+(B*eta)   Lpivot^m ∈ J+(B*eta)   Lpivot^m ∈ J+(eta)   Lpivot^m ∈ J+(B)
3  41           n = 1                      YES (wt 13 <= 14)      no, no, no              64               m = 3                  m = 2 (wt 12: non-vacuous)   m = 3
4  215          n = 2                      B*eta ∉ J_deg is non-vacuous (wt 17 <= 21); n = 2 vacuous   no, no, no   327   m = 3 (Lpivot² ∉: non-vac.)  m = 3   m = 3
5  1099 (mod p) n = 2                      B*eta ∉ J_deg non-vacuous (wt 21 <= 30); n = 2 vacuous      no, no, no   1651  m = 3 (Lpivot² ∉: non-vac.)  m = 3   m = 3
```

Reading: "degenerate tacnode ⇒ (R)" holds at the IDEAL level at t = 3 (n = 1, weight 13 in a ring of socle degree 14) and only
at the radical level at t = 4, 5; the converse needs m = 3 everywhere with `Lpivot² ∉ J + (B*eta)` non-vacuous. Neither
direction is uniform at the ideal level.

**Hensel replay (modular controls, b = 1, order M = 2N+2).** t = 3 (`p = 31991`, `d ↦ 14162`): factorisation
`Q_P = (3/16)F_0F_1` mod `x^{M+1}` OK; `F_0(L)F_1(L) + (16/3)*UF ≡ 0` (so L is a root of `F_0` modulo J); `s_1 = p_1 = 0`,
`s_2 = 8eta/3`, `p_2 = 8eta/3`, `s_3 = 4w_2 - 16B eta/3`, `p_3 = (4/3)(3w_2 - 4B eta)`, `s_4, p_4` as in Prop. 2.4;
`Disc(F_0)` vanishes to order 4; `[x⁴]Disc(F_0) + (16/9)T_2 = 0` and `[x⁴]Disc(F_0) - (4/9)Lpivot² ∈ (E_2)`; the direct
`resultant(Q_P, d_Y Q_P, Y)` confirms `[x⁴]Disc_Y(Q_P) = (3/16)(-64)(3/16)⁶(-16/9)T_2` (`hensel_debug2`). t = 4 (`d ↦ 4933`):
all the same lines pass (157 s). t = 5: §10. (A first draft used Singular's `jet(f, M)`, which truncates by TOTAL degree and
dropped the high c-degree part of `[x⁴]Disc(F_0)`; the accepted version truncates by x-weight; the draft's failure was
diagnosed by the resultant before anything was consumed.)

The generic-jet checks (K = 10, 20 named checks, ALL_PASS) and the reproduction of the frozen `universal_recursion.json`
values (pivot laws, `Φ_4`, `Φ_5`, `Q_P(0, L) = (3/16)(L+b)²(L²+b²)`, `d_L Q_P = (b/4)Lpivot*x² + ...`) are in `tacnode_involution_K10.json`.
## 7. Task (4): verdict, the exact obstruction, what any proof must look like

**No uniform theorem is obtained. The tacnode statement is not proved; (R) is not proved; theorem (T) is not promoted for
any new index.** The propositions of §2–§5 are PROVED-HERE as structure (identities and finite algebraic statements, each with a
written proof and a machine check with generic jets); Theorem 3.1 and Theorem 5.1 are new and t-independent, but neither is
the uniform statement.

**The residual, stated precisely (type OPEN).** For every t >= 8 (t >= 6 without the frozen t = 6, 7 results) and every field
factor k of `Q[d]/(3d² - t - 1)`: with `B, w_1 = eta, w_2, w_3` the Theorem H reconstructions in `k[c_1..c_{t-1}, b]`,

```text
T_2 := 3 b² w_3 + 18 B w_2 - 10 w_1²   ∈  rad (E_2, ..., E_{2t})          [equivalently  4 w_1 + 3 b c_{t-1}/y ∈ rad J_t;
                                                                          equivalently j0 >= 3 on every polynomial solution with b != 0].
```

A proof would reduce (R) to the degenerate stratum `J + (Lpivot)`, on which the L-side recursion has the k-independent
second pivot `piv_2` (§4); it would not by itself give (R): at t = 4, 5 `B*eta ∉ J + (Lpivot)` non-vacuously (§6), so the
remaining step on the stratum is again a radical statement.

**Shape constraints on any proof, established here.** (i) Not from the involution: `L̃` is never a polynomial and never
equals L (Theorem 3.1), whether `j0 = 2` or `j0 >= 3`. (ii) Not from the ∞-branches: all four are unramified, distinct, and satisfy
the leading (E-) identically by Vieta on (UT); the `lc = -1/y` branch is `-L - b + O(x^{2-2N})` for every P. (iii) Not from
the termination of the pivot chain: it terminates at `j0 <= 3N` for every solution, and the only known nontrivial solution has
`j0 = 3` with no relation to `B*eta`. (iv) Not at the scheme level: `T_2`, `Lpivot`, every `[x^j]D` ∉ J non-vacuously at
t = 3, 4, 5; like (R) itself the statement lives in the radical, so a uniform proof must see the reduced structure (the
polynomiality of L through the truncation conditions), not the local geometry at (0, -b) alone. (v) Positively: the statement
is one quadratic relation on the 4-jet of P, `ord_0 Disc_Y(Q_P) >= 6`, where `Disc_Y(Q_P)` has degree 12N and order `2j0` at 0;
a uniform bound on `j0` through the global structure of D (degree 3N, `D | Disc_Y(Q_P)`, the 3N intersections of the graph of L
with the residual cubic) is the direction opened here and not closed.

**Best next instrument.** Fixed t: unchanged (Theorem H rows + weight-graded Macaulay certificate for `(B*eta)^n`); for the
tacnode sub-target the certificate `T_2^n ∈ J` lives in weight `4tn` against `(4t+1)n`, a smaller block, and the t = 3 identity
`B*eta ∈ J + (Lpivot)` suggests testing it and `T_2^n ∈ J` at t = 6, 7 as cheap controls before any t = 8 attempt. Uniform
problem: the Hensel factor `F_0` (charged §6) with its exact first obstruction `[x⁴]Disc(F_0) = -16T_2/(9b²)`, equivalently
the contact order `j0 = ord_0 d_Y Q_P(x, L)`.
## 8. FALLACY-v2 check

- **Formal vs convergent branch; involution.** `L̃` is shown convergent AND algebraic of degree 3; the involution is used only
  to derive identities ((E-), the cubics), never to transport polynomiality; the ∞-description of both branches is stated as a
  consistency. No contradiction is claimed from the involution.
- **Prime label/derivative.** `L̃`, `p̃`, `λ̃` are labels; `P'`, `R_Y`, `d_Y`, `theta = x d/dx` are declared derivatives.
- **Variable/ring map.** Every Singular ring is declared with generator order, weights and field (`(0,d)`, `minpoly 3d² - N`, or
  `GF(31991)` at the declared root); Y is a ring variable; frozen rows are compared by `imap` (identity on `(c_i, b)`); the b = 1
  replay uses an explicit `map` whose image list is printed in the script.
- **Raw remainder / `sat()`.** No `sat`; memberships are `reduce` against reduced standard bases with the power reported;
  "cofactor 0" means the polynomial is identically zero.
- **Floor/attainment.** `deg D = 3N`, `lc D` exact; `j0 <= 3N` is a bound, `j0 = 3` at t = 2 a witness; min powers are search
  minima; every membership is labelled vacuous or non-vacuous against the socle degree.
- **Modular -> char 0.** Nothing modular is promoted; t = 3, 4 identities are exact over `Q(d)`, generic identities exact over
  `Q(b, B, eta, w_2, l_j)`.
- **Number vs degree; generic-coefficient theorems.** Theorem 3.1 uses one explicit Newton polygon and a divisibility in `k[x]`.
- **Rejected draft.** The total-degree `jet` truncation was caught by an independent resultant and replaced (§6).
- **Flag/place/series, exit sets, pole identities, 8.5, arrival index:** not touched. No exit-price assertion; `charge_basis` inapplicable.
## 9. OPENs

OPENS RAISED

- `OPEN[K16-UF-CONTACT-ORDER-BOUND]` - for a polynomial solution `(P, L)` of (UF) with the marked jets and `b != 0`, the contact
  order `j0 = ord_0 d_Y Q_P(x, L(x))` of the graph of L with the residual cubic at `(0, -b)` satisfies `2 <= j0 <= 3N`; is
  `j0 <= N` (or any bound `< 3N`) forced, and is `j0 >= 3` (the degenerate-tacnode statement) provable from a bound? QUANTITY:
  number of solutions with known `j0` = 1 (t = 2, d = -1: `j0 = 3 = N`); proved upper bound = 3N; proved lower bound = 2.

OPENS RETAINED

- `OPEN[K16-UF-DEGENERATE-TACNODE]` (charged): retained and SHARPENED - equivalent to `T_2 = 3b²w_3 + 18Bw_2 - 10w_1² ∈ rad J_t`
  for every t, i.e. `6P_0P_4 + 9P_1P_3 + 5P_2² = 0` on every solution, i.e. `ord_0 Disc_Y(Q_P) >= 6`; the non-degenerate
  alternative is NOT excluded by the involution (Theorem 3.1). QUANTITY: number of indices at which the statement is verified
  independently of (V0) = 1 (t = 2); first index at which it is not implied by the banked (V0) = 8; number of indices at which
  `B*eta ∈ J + (Lpivot)` holds at the ideal level = 1 (t = 3; fails non-vacuously at t = 4, 5).
- `OPEN[K16-UF-SECOND-KIND-FAMILY]` (charged): unchanged. QUANTITY: number of known theorems bounding polynomial roots of a
  power-series quadratic of the shape `F_0` = 0.
- `OPEN[K16-INTRINSIC-SLICE-UNIT]` (charged): unchanged. QUANTITY: first index without an exact certificate = 8.
- `OPEN[K16-UNIFORM-POINT]` (charged Galois lane): untouched. QUANTITY: #{t : a closed-form point of Γ_t is known} = 0.
## 10. Computation record (`box/k16-tacnode-20260905/`), collision scan, completion

```text
manifest.sha256, input-verification-final.log     custody (awk manifest; sha256sum -c 4/4 OK at start and at sealing)
tacnode_involution.py -> _K6.json/.log, _K10.json/.log   Props. 2.1–2.4, Theorem 5.1 pieces, pivot chain, closed forms (generic jets; ALL_PASS)
disc4_check.py/.json                              [x⁴]Disc(F_0) with generic P_4: = -16T_2/(9b²); on solutions (4/(9b²))Lpivot²
t2_family.sing/.out                               t = 2, d = -1 family: C irreducible, L̃ series, D = (15/2)L²x³, ∞-branch with lc -1/y
custody_tacnode.py -> custody_tacnode_t3.*, _t4.*  exact over Q(d): D identities, T_2 identity, second pivot, memberships, degenerate stratum
custody_tacnode_t{3,4,5}_p31991_d*.{sing,out}     modular controls incl. the b = 1 Hensel replay (t = 3: instant; t = 4: 157 s; t = 5: STATUS_T5)
hensel_debug{,2,3}_t3_p31991.sing                 diagnosis of the rejected jet-truncation draft (resultant cross-check)
sections/, finalize.sh, hash_artifacts.sh, artifacts.sha256, collision_scan{,.filtered}.txt
```

All CAS work local, `--cpus=1`, at most five Singular processes at once. One shell was lost to a self-matching `pkill -f`
(no artefact affected; processes were then killed by exact name). The exact t = 5 standard basis over Q(d) was not attempted
(the charged lanes report it unfinished after 32 min); t = 5 is a modular control only.

Collision scan (`ops/open_collision.py --root .`, filtered of this lane's files): COLLISION_SUMMARY

<!-- BODY-END -->
