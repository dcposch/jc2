# UNIFORM lane: the tacnode dichotomy on (UF) - the second Hensel branch L̃ is NEVER a polynomial (the residual cubic is irreducible), so the involution yields no contradiction; the dichotomy iterates as the contact order j0 = ord_0 d_Y Q_P(x, L) ∈ [2, 3N]; the OPEN is one quadratic on the 4-jet of P; no uniform theorem, (R) not proved

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
           (2) It iterates exactly: d row_k/d l_m = -[x^{k-m}]D, D = d_Y Q_P(x, L), deg D = 3N; j-th pivot [x^j]D = (3/4)b²l_j + f_j;
               [x²]D = (b/4)Lpivot; [x³]D = (3/4)(2Bl_2 + b²l_3 + 2bw_2) identically; j0 = ord_0 D = ord_0(L̃ - L) ∈ [2, 3N]
               terminates for every solution and forces nothing (t = 2 family: j0 = 3 = N, second pivot != 0, B = eta = 0
               for the independent reason c = 0); the descent is in j, not in N.
           (3) Frozen data: D = x²D̂, [x²]D = (b/4)Lpivot, [x³]D = (3/4)piv_2 (cofactor 0), Lpivot² = -4T_2 - 24E_2 EXACTLY
               (t = 3, 4 over Q(d); t = 5 mod p), [x⁴]Disc(F_0) = -16T_2/(9b²); all pivots and T_2 ∉ J (non-vacuous);
               NEW: B*eta ∈ J + (Lpivot) at t = 3 (weight 13 < socle 14), not at t = 4, 5 (non-vacuous).
           (4) No uniform theorem; the tacnode statement is not proved; the residual is the jet-quadratic
               T_2 = 3b²w_3 + 18Bw_2 - 10w_1² ∈ rad J_t  <=>  6P_0P_4 + 9P_1P_3 + 5P_2² = 0 on every solution  <=>  ord_0 Disc_Y(Q_P) >= 6.
CUSTODY    4/4 input hashes OK (awk manifest, sha256sum -c); frozen controls_t{3,4}_raw.sing reproduced by imap (identity map);
           frozen universal_recursion/tacnode_checks/degenerate_pivot JSONs re-derived; generic jets to K = 10: ALL_PASS.
NOTIFY     not warranted (no new index, no exit claim; charge_basis inapplicable).
```
