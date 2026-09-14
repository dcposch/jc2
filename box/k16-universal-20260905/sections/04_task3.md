## 4. Task (3): eliminating P — the eliminant is algebraic, and the L-side has its own recursion

**4.1 No differential resultant is needed.** L enters (UF) with no derivative. Eliminating P is an ordinary
algebraic elimination, already done twice: at ∞ (Theorem H: `E_2..E_{2t} ∈ k[c, b]`, weights `4t+2−k`, 2t−1 equations
in t unknowns) and at 0 (`Φ_{2N+1..4N}`, 2N equations in N+2 unknowns, `Φ_{4N}` containing (UT)). Both are
quasi-homogeneous for the one `G_m`. Neither has a Wronskian or Hankel form: the identity is quadratic in P and
quartic in L, so no elimination step is linear; the scalar pivots (`λ(m)`, `−(k−3)b²/2`) sit inside a quadratic
recursion. The only determinantal objects are (UT) and the discriminant factorisation (e), a consequence, not a
criterion. Dually, (UF) says that a quartic plane curve in `(x, L)` attached to P has a polynomial branch:

**Proposition 4.1 (the quartic and its tacnode).** Fix P (polynomial, marked jets) and `b, B, eta`, and set

```text
Q_P(x, L) := R(x,L) − G(x,L)·P − (theta−3)(P²)
           = (3/16) L⁴ + (3/8) b L³ − ((3/4)Bx + (3/2)P) L² − ((eta b/2) x² + (3/2) b P) L + (BxP − eta B x³ − (theta−3)(P²)).
```

(UF) ⟺ `Q_P(x, L(x)) ≡ 0`: given P, L is an algebraic function of x (a root of a quartic with polynomial
coefficients of x-degrees 0, 0, 2N, 3N, 4N), and the problem is whether one of its four branches is a POLYNOMIAL of
degree N with `lc = 1/y`. Verified (`universal_recursion.json`, `tacnode_checks.json`):
(a) `Q_P(0, L) = (3/16)(L + b)²(L² + b²)`: `L = −b` is a double root, `±ib` simple.
(b) With `L = −b + ℓ`, `wt x = 1`, `wt ℓ = 2`, the weight-4 tangent cone of `Q_P` at `(0, −b)` is
`(3/8) b² ℓ² + b eta x² ℓ + κ x⁴`, `κ = (b²/2) P_4 + 3 B w_2 − eta²`, with no terms of weight < 4; on a solution
`κ = −b eta l_2 − (3/8) b² l_2²` (this is row 4), the two branches are `ℓ = l_2 x² + …` and `ℓ = l̃_2 x² + …` with
`l_2 + l̃_2 = −8 eta/(3b)`, and the cone's ℓ-discriminant is `b² x⁴ (4 eta + 3 b l_2)²/16`. So `(0, −b)` is a
non-degenerate tacnode (two smooth branches, contact order 2) iff the L-pivot `4 eta + 3 b l_2 ≠ 0`, and
`∂_L Q_P(x, L(x)) = (b/4)(4 eta + 3 b l_2) x² + O(x³)`: Prop. 2.2's pivot is the tangent-cone discriminant.
(c) Hensel: `(L+b)²` and `L² + b²` are coprime, so `Q_P = (3/16) F_0 F_1` uniquely in `k[[x]][L]` with
`F_0 ≡ (L+b)²`, `F_1 ≡ L² + b²` mod x. A polynomial solution L is a root of `F_0 = L² + s(x)L + p(x)`, and
`L̃ := −s − L` is a second FORMAL solution `(P, L̃)` of (UF) with the same `P, b, B, eta, w_2` and `l̃_2` as in (b):
the involution `ι` of the formal solution space. So formal solutions with P a polynomial of degree 2N exist in abundance (any P with the jets, any `l_2` off the
pivot locus, then Prop. 4.2); the polynomiality of L is the entire content of the problem.
(d) Divisibility duals. Given L: `P | Rfree(L)`. Given P: `(L(x) − L_0) | Q_P(x, L_0)` for every constant `L_0`; in
particular `L | BxP − eta B x³ − (theta−3)(P²)` and `x²C = L + b | Q_P(x, −b)`.
(e) `Disc_L(Q_P) = D(x)² · Disc_L(Q_P/(L − L(x)))`, `D = ∂_L Q_P(x, L(x))` of degree exactly 3N with
`D = x² D̂`, `D̂(0) = (b/4)(4 eta + 3 b l_2)`: necessary, not sufficient.

**Proposition 4.2 (dual universal recursion — L from P).** On `{4 eta + 3 b l_2 ≠ 0}`, for k ≥ 5,

```text
l_{k−2} = 4 [ rest_k − (k−3) b² P_k / 2 ] / ( b (4 eta + 3 b l_2) ),      rest_k = bracket_k |_{l_{k−2} = l_{k−1} = l_k = 0},
```

a recursion with a k-INDEPENDENT pivot (no resonance index at all); it recovers `l_3, …, l_{10}` from the output of
the P-recursion (checked, K = 12). At index t: rows 4, N+3..2N define `P_4, P_{N+3}..P_{2N}`, rows 5..N+1 define
`l_3..l_{N−1}` from P, conditions are row N+2 (`l_N = 1/y`) and rows 2N+1..4N — 2N+1 equations in the N+2 unknowns
`(B, eta, l_2, P_3, P_5..P_{N+2})` at `b = 1`, excess t as for Theorem H. On `4 eta + 3 b l_2 = 0` the leading unknown of
`row_k` drops to `l_{k−3}` with the k-independent coefficient `−(3/4)(2 B l_2 + b² l_3 + 2 b w_2)` (k ≥ 7, checked to
10, `degenerate_pivot.json`); the cascade continues one order per vanished pivot.

**Proposition 4.3 (the exceptional family in this language; P = −L²/4 forces t = 2).** If `P = −L²/4` then the jets
force `B = 0`, `eta = b l_2/2`, and (UF) reduces exactly to `L²(xL' − 3(L+b)) = −2 eta b x²` (checked with `eta` free).
The left side has top coefficient `(N−3) l_N³ x^{3N}`, so N = 3; then the residual coefficients are
`−l_2 l_N², −2 l_2² l_N, −l_2³, 2 b l_2 l_N, 2 b l_2²`, forcing `l_2 = 0`, `eta = 0`: `L = −b + l_3 x³`, `P = −L²/4` —
exactly the charged t = 2, d = −1 family, and nothing else at any t. On it the L-pivot vanishes (degenerate tacnode: the two
branches through `(0, −b)` agree to order ≥ 3; `L` is still a simple root of `Q_P` for x ≠ 0) and the second pivot is
`−(15/2) b² ≠ 0`. Exact t = 2 controls at both roots
(`t2_controls.out`): d = +1: `V(J) = {0}`; d = −1: `rad J = (c_1)`, `P + L²/4 ≡ 0` on `c_1 = 0`, and the L-pivot
`(6/5) c_1⁴ + 33 c_1 b ∈ rad J`. **Observation, not a theorem:** at every index with data (t = 2 both roots
non-trivially; t = 3, 4, 5 where `V(J) = {0}`, §5) every solution has `4 eta + 3 b l_2 ∈ rad J`, i.e. a degenerate
tacnode. "Every polynomial solution of (UF) has a degenerate tacnode" is strictly weaker than (V0) and is the
natural intermediate uniform target; below t = 8 it cannot be tested independently of the banked (V0).
