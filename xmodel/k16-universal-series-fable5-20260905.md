# UNIFORM lane: (UF) as ONE universal termination problem — the recursion is quadratic with unit pivots on both sides, the connection/residue route yields exactly (UT), the L-side is algebraic (a quartic with a tacnode) with its own resonance-free recursion; no uniform theorem, the obstruction restated, the instrument unchanged

Lane: `k16-universal-series-fable5-20260905`. Fable 5.1. 2026-09-05. Basis `e00b2002`.

**VERDICT: NO uniform-in-t theorem is obtained; (R) is not proved; theorem (T) is not promoted for any new index.**
The universal recursion is written out and its structure proved (quadratic; the L-jets enter each row two orders
late, linearly, with a k-independent pivot); the 0–∞ connection problem is Theorem H's system and its only residue
identity is (UT); eliminating P is algebraic — L is a root of a quartic attached to P with a tacnode at (0, −b) whose
degeneracy is the new pivot — and the t = 2 family is exactly P = −L²/4. All verified against the frozen t = 3, 4, 5
certificates.

```text
REQUESTED  (1) Φ_k explicitly; linear? denominators? the k = 3 resonance vs R_boundary = y·eta/3;  (2) P as the ODE solution
           through the marked jets, 0 vs ∞, a residue/monodromy obstruction?;  (3) eliminate P: the resultant on L, its
           structure;  (4) exact verification at t = 3, 4, 5;  (5) verdict.
ANSWER     (1) Φ_k = [ (k−3) Σ_{i=1}^{k−1} P_i P_{k−i} + Σ_{i=1}^{k} G_i P_{k−i} − R_k ]·2/((k−3)b²): QUADRATIC in the P-coefficients,
               denominators 4b², 4b⁴, 12b⁶, 16b⁸, 120b¹⁰, 1440b¹² (k = 4..9). NEW: l_k, l_{k−1} cancel in row k and row k is LINEAR
               in l_{k−2} with the k-INDEPENDENT pivot −(b/4)(4 eta + 3 b l_2) (Prop. 2.2). The k = 3 compatibility is an identity
               (B·eta enters twice and cancels); it is NOT R_boundary = y·eta/3, which is the SOURCE of the jet linkage P_2 = eta.
           (2) Briot–Bouquet exponents 3 at x = 0 and 4N + 6d at x = ∞ (irrational off the split indices: the ∞-germ is unique and
               convergent); polynomial solution ⟺ that germ is entire ⟺ Theorem H's E_k. The residue theorem for P'/P gives
               2N = 3/2 − 3/(4p) + 3/(32p²) — EXACTLY (UT) — and nothing else (Prop. 3.1).
           (3) L is never differentiated: the eliminant is algebraic (Theorem H's E_k; quasi-homogeneous; no Hankel/Wronskian form).
               Dually (UF) ⟺ Q_P(x, L(x)) ≡ 0 for the quartic Q_P = R − GP − (theta−3)P²: Q_P(0, L) = (3/16)(L+b)²(L²+b²), the
               tacnode is non-degenerate iff 4 eta + 3 b l_2 ≠ 0, a second branch L̃ is a formal solution with the SAME P
               (involution), and the dual recursion L-from-P has a k-independent pivot. P = −L²/4 forces N = 3 (the t = 2 family).
           (4) frozen rows/B/eta/target reproduced (t = 3, 4, 5 exact); bottom-up numerators in J with b-power 0 (only k = 4 is
               non-vacuous: socle degrees 14, 21, 30); dual chart UNIT at t = 3 (mod p; exact in §9) with non-unit negative control.
           (5) No uniform theorem; obstruction restated in three charts (§6); fixed-t instrument unchanged; one new uniform
               handle, OPEN[K16-UF-DEGENERATE-TACNODE].
CUSTODY    4/4 input hashes OK (awk manifest, sha256sum -c); frozen controls_t{3,4,5}_raw.sing reproduced by imap under the identity
           map; every structural claim machine-checked with generic jets to k = 12 (universal_recursion.json: ALL_PASS).
NOTIFY     not warranted (no new index, no exit claim; charge_basis inapplicable).
```
## 1. Custody

The receipt `xmodel/k16-universal-series-fable5-20260905.run.v2` was parsed with `awk -F=`, pairing each
`charged_input_<i>_sha256=` with its `_basename=` into `box/k16-universal-20260905/manifest.sha256`; `sha256sum -c`
returned **4/4 OK** before any input was opened (re-run at sealing: `input-verification-final.log`). No digest was
retyped. Basis `e00b2002`. All four charged inputs were read from `/tmp/jc2-lane.S7hyqB/inputs`; (UF), (UJ), (UL) and
the identities (I1)–(I4), Theorem H and the x = 0 pivot law are consumed from the charged abel-polysol report; the
boundary identity `R_boundary = y·eta/3` from the charged Astra §8. The frozen certificates replayed are
`box/k16xempty-20260905/controls_t{3,4,5}_raw.sing` (byte-unchanged, identifiers renamed on import), compared under
the identity map on `(c_i, b)` by `imap`, exactly as in the charged `uf_emit.py`. No ledger, `jc2-lean` or
`ideation-*` file was read or written. All drivers and transcripts are in `box/k16-universal-20260905/`.

Notation (charged §7.1): `N = t+1`, `q = 2N−1`, `theta = x d/dx`, `G = (3/2)L(L+b) − Bx`,
`R = Rfree = (3/16)L²(L(L+2b) − 4Bx) − eta·x²(bL/2 + Bx)`, so (UF) reads `(theta−3)(P²) + G·P = R`.
Write `L = −b + Σ_{j≥2} l_j x^j` (`l_1 = 0` is `L'(0) = 0`; on the ray `l_j = c_{N−j}/y` for `2 ≤ j ≤ N−1`,
`l_N = 1/y`, `l_j = 0` for `j > N`) and `P = Σ_k P_k x^k` with the jets `P_0 = −b²/4`, `P_1 = −B`, `P_2 = eta`,
`P_3 = w_2` (`= [x²]W`). `G_i`, `R_k` are x-coefficients; the tilde in `L̃` below is a label, not a derivative.
## 2. Task (1): the universal recursion, written out

Row `x^k` of `(theta−3)(P²) + GP − R` is

```text
row_k = (k−3) Σ_{i+j=k} P_i P_j + Σ_{i=0}^{k} G_i P_{k−i} − R_k
      = −((k−3) b²/2) · P_k + bracket_k,        bracket_k = (k−3) Σ_{i=1}^{k−1} P_i P_{k−i} + Σ_{i=1}^{k} G_i P_{k−i} − R_k,
```

because `G_0 = (3/2)L(0)(L(0)+b) = 0` and `2P_0 = −b²/2`. Everything below is proved for all k and machine-checked for k ≤ 12 with GENERIC jets (`universal_recursion.py`,
`.json`: `ALL_PASS`).

**Proposition 2.1 (shape of the recursion).**
(a) The pivot of `P_k` in `row_k` is `−(k−3)b²/2`: t-independent, zero only at k = 3 (checked k = 1..12).
(b) `row_0 = (3/16)(b² − 4P_0)(b² + 4P_0)` fixes `P_0 = ±b²/4`; on the marked sign the pivots of rows 1, 2 are `b²`,
`b²/2` and force `P_1 = −B`, `P_2 = eta`; row 3 has pivot 0 and, with the jets, vanishes identically: it is the
Briot–Bouquet compatibility at the resonance, `P_3 = w_2` is free.
(c) The recursion is **not linear** in the P-coefficients: `bracket_k` contains the convolution
`(k−3) Σ P_i P_{k−i}` and has total degree exactly 2 in `(P_1, …, P_{k−1})` for every k ≥ 4 (checked). The `P_k` are
not rational-linear functionals of a forcing term; they are the rational functions
`Φ_k(b, B, eta, w_2, l_2, …)` with denominators `4b², 4b⁴, 12b⁶, 16b⁸, 120b¹⁰, 1440b¹²` at k = 4, …, 9: the b-power is exactly
`2(k−3)` (no cancellation), the numeric part is not `∏_{j≤k}(j−3)`. Weighted-homogeneous: `wt Φ_k = 2N − k`.

```text
Φ_4 = (2/b²) ( eta² − 3 B w_2 − b eta l_2 − (3/8) b² l_2² )
Φ_5 = 30B²w_2/b⁴ − 10B eta²/b⁴ + 10 B eta l_2/b³ + 3 B l_2²/b² + 4 eta w_2/b² − eta l_3/b − (3/2) l_2 w_2/b − (3/4) l_2 l_3
```

**Proposition 2.2 (the L-side of a row).** For k ≥ 4 the coefficients `l_k` and `l_{k−1}` cancel in `row_k`; for
k ≥ 5, `row_k` is LINEAR in `l_{k−2}` with the k-independent coefficient `−(b/4)(4 eta + 3 b l_2)`. Hence
`Φ_k` depends on `l_2, …, l_{k−2}` only and `∂Φ_k/∂l_{k−2} = −(4 eta + 3 b l_2)/(2b(k−3))` (checked k = 5..12).

*Proof.* Only `G_k P_0`, `G_{k−1} P_1`, `G_{k−2} P_2` and `R_k` can carry `l_k, l_{k−1}, l_{k−2}` (by induction `P_i`
depends on `l_{≤ i−2}`). `l_k`: `G_k P_0 ∋ (3/2)(−b l_k)(−b²/4) = (3/8)b³ l_k`; in `R_k`, `(3/16)[(L²)_k (L(L+2b))_0 +
(L²)_0 (L(L+2b))_k]` with `(L²)_k ∋ −2b l_k`, `(L(L+2b))_0 = −b²`, `(L(L+2b))_k ∋ l_0 l_k + l_k(l_0 + 2b) = 0` gives
`(3/8)b³ l_k`; difference 0. `l_{k−1}`: `G_{k−1} P_1 ∋ (3/2)(−b l_{k−1})(−B)` against `(3/16)(L²)_{k−1}(−4B) =
(3/2) b B l_{k−1}` in `R_k` (`l_1 = 0` and `(L(L+2b))_1 = 0` kill every other route); difference 0. `l_{k−2}`:
`G_k P_0 ∋ (3/2)(2 l_2 l_{k−2})(−b²/4) = −(3/4) b² l_2 l_{k−2}`, `G_{k−2} P_2 ∋ −(3/2) b eta l_{k−2}`; in `R_k` the
`L²·L(L+2b)` part contributes `(3/16)[2 l_2 l_{k−2}(−b²) + b²·2 l_2 l_{k−2}] = 0` (and `(L(L+2b))_2 = 0`), while
`−eta x²·bL/2` contributes `−(b eta/2) l_{k−2}`; total `−b eta l_{k−2} − (3/4) b² l_2 l_{k−2}`. ∎

Two readings of the pivot: `4 eta + 3 b l_2 = 8 R_2/b²` (the first coefficient of `Rfree` not fixed by the jets), and
`Hdiff = (3/4)b² + (eta − (3/2) b l_2) x² + O(x³)`.

**The k = 3 resonance versus the boundary identity.** With the jets, `row_3 ≡ 0` is an identity in which the
product `B·eta` enters exactly twice and cancels: `G_1 P_2 = −B eta` against `+B eta` from `−R_3` (the term
`−eta x²·Bx`); the `l_2` and `l_3` terms cancel likewise (`(3/2) b B l_2`, `(3/8) b³ l_3`). It is therefore a
0 = 0 and carries no condition. It is NOT the charged boundary identity `R_boundary = U_h'(b4) + b3·C_h(b4) = y·eta/3`:
that identity lives in the residual chart (the `T_(t,k)` rows) and identifies the image of the jet `eta` with a chart
quantity up to the unit `y/3`; it is the SOURCE of the jet linkage `P_2 = eta`, and the linkage is what makes row 3
vacuous. Relation: linkage ⇒ compatibility; the compatibility itself has no content.
## 3. Task (2): the generating function as an ODE solution — connection problem, residues, monodromy

**The two fixed singular points.** At x = 0, (UF) is a Briot–Bouquet point of exponent `λ_0 = 3` (rows 0–3);
the compatibility holds identically (Prop. 2.1(b)), so by the Briot–Bouquet theorem (integer case with
compatibility) the marked solutions form a one-parameter HOLOMORPHIC family `P(x; w_2)`, analytic in `w_2`. At
x = ∞ put `u = 1/x`, `P = u^{−2N} Q(u)`: `(4N−3) Q² − 2u Q Q' + Ĝ Q = R̂` with `Ĝ = u^{2N} G(1/u)`, `R̂ = u^{4N} R(1/u)`;
`Q(0) = omega` is (UT), and the Briot–Bouquet exponent is

```text
λ_∞ = (4N−3) + Ĝ(0)/(2 omega) = 4N − 3 + 3(2d+1) = 4N + 6d,        pivot of Q_m:  2 omega (λ_∞ − m)  (= Theorem H's λ(2N−m); checked)
```

For non-split t, `λ_∞ ∉ Q`: no resonance, the formal solution at ∞ is unique for each root `omega` and CONVERGES
(Briot–Bouquet, non-integer case). So `P_∞` is an honest analytic function on `|x| > R_0` with a pole of order 2N,
determined by `(L, B, eta, omega)`. At split t, `λ_∞ = 4N ± 6m_0 ∈ Z` and the resonance sits at Laurent index `−2N − 6m_0` (d > 0, below the
truncation zone) or `−6m_0(m_0 − 1)` (d < 0): the charged resonance table.

**Movable singularities and the global reformulation.** From `2xPP' = 3P² − GP + R`, a solution vanishing at
`x_0 ≠ 0` with `R(x_0) ≠ 0` has `P² ≈ (R(x_0)/x_0)(x − x_0)`: a square-root branch point. So a solution is entire iff
every zero of P is a zero of `Rfree` (for a polynomial: `Rfree = P·Hdiff`), and *a polynomial solution at index t
exists iff the unique analytic germ `P_∞` at ∞ continues to an entire function*, i.e. iff its Laurent tail
`P_{−1..−2N}` vanishes (lower coefficients then vanish automatically). Rows `x^{2N+2}, x^{2N+1}` eliminate `eta, B`,
row `x^{2N}` is `E_{2t}`, rows `x^{2N−1}..x^4` are `E_{2t−1}..E_2`, rows `x^3..x^0` vanish by the jets: the connection
problem is Theorem H's system and the analytic picture adds no condition.

**Proposition 3.1 (the residue calculus yields exactly (UT)).** Let P be a polynomial solution of degree 2N, b ≠ 0.
Then `P'/P = 3/(2x) − G/(2xP) + R/(2xP²)`. Residues: at a zero `x_0` of P both sides have residue the multiplicity
(automatic, since `P | R`); at x = 0 the right side has residue `3/2 − G(0)/(2P(0)) + R(0)/(2P(0)²) = 3/2 − 0 − 3/2
= 0`, consistent with `P(0) = −b²/4 ≠ 0`; at ∞, `P'/P` has residue `−2N` while the right side has `1/x`-coefficient
`3/2 − 3/(4p) + 3/(32p²)`, `p = omega y²` (`lc G = 3/(2y²)`, `lc R = 3/(16y⁴)`). The residue theorem gives

```text
2N = 3/2 − 3/(4p) + 3/(32 p²)   ⟺   (4N−3) p² + (3/2) p − 3/16 = 0,     i.e. exactly (UT)
```

(machine-checked: the two sides differ by the constant factor −1/2). No other integer-valued residue exists, and
(UT) is consistent at every N (discriminant 3N; the field `Q(√(3N))`). ∎ Monodromy: coefficients rational in x, the marked germs at 0 and ∞ single-valued, a polynomial with trivial
monodromy — nothing to compare; the Liouville–Appell invariants of the first-kind form in `z = 1/P` are rational
functions carrying the unknown L and classify ONE equation. **Conclusion of task (2):** the residue/monodromy route
produces (UT) and stops; the "integer residue growing with N" is `−2N` against `3/2 − 3/(4p) + 3/(32p²)`, and their
equality is not an obstruction but the definition of the field.
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
## 5. Task (4): exact verification at t = 3, 4, 5 against the frozen certificates

Drivers `custody_bu.py` (full numerators) and `custody_bu_red.py` (every numerator reduced modulo `std(J)` as it is
built — legitimate because J is an ideal and the recursion uses only ring operations and scalar divisions), exact
over `Q(d)` with `minpoly 3d² − N`; modular controls at `p = 31991` with the declared root of `3d² − N`.

```text
t  frozen rows/B/eta/target reproduced from (UF)   std(J): dim, vdim   T∈J  T²∈J   socle degree of J   non-vacuous membership   L-pivot: in J / power in J   B, eta, b powers in J
3  yes (5 rows)  exact                              0, 66   (0 s)       no   yes    14                  k = 4 only (wt 12)        no / 3                       3, 3, 4
4  yes (7 rows)  exact                              0, 338  (10 s)      no   yes    21                  k = 4 only (wt 16)        no / 3                       3, 3, 5
5  yes (9 rows)  exact                              0, 1709 mod p       no   yes    30 (mod p)          k = 4 only (wt 20)        no / 4  (mod p, k ≤ 24)      3, 4, 6  (mod p)
```

**What was checked.** (i) Custody: the (UF)-emitter's `E_2..E_{2t}`, `B`, `eta`, `B·eta` equal the frozen objects under
`imap` (identity on `(c_i, b)`) at t = 3, 4, 5 exactly. (ii) Consistency of the two recursions: with the top-down data
`(b, B^TD, eta^TD, w_2^TD)`, `b^{2(k−3)} P^TD_k − N_k ∈ J` (4 ≤ k ≤ 2N) and `N_k ∈ J` (2N < k ≤ 4N), b-power 0 throughout
(t = 3, 4 exact; t = 4, 5 modular). **Vacuity caveat (FALLACY-v2, floor/attainment):** J is `m`-primary with socle degrees
14, 21, 30, while `wt N_k = (2N−1)k − 4N` is 12, 16, 20 at k = 4 and 19, 25, 31 at k = 5: every membership with k ≥ 5 is
forced by weight and is NO evidence; only the k = 4 identity (row 4, `E_2 ∈ J`) is non-vacuous. The truncation conditions
are consistent with the frozen ideal, but their membership is not an independent certificate here — the dual chart is.
(iii) The L-pivot `4 eta + 3 b c_{t−1}/y` (weight 2t) is NOT in J at t = 3, 4 (non-vacuous); `B², eta² ∉ J`,
`B³, eta³ ∈ J` as charged; `b⁴ ∈ J` (t = 3), `b⁵ ∈ J` (t = 4).

**The dual chart as an instrument (Prop. 4.2), `dual_chart.py`.** Unknowns `B, eta, l_2, P_3, P_5..P_{N+2}, u`
with `u·(4 eta + 3 l_2) = 1`, `b = 1`, `l_N = 1/y`; rows 5..N+1 solved for `l_3..l_{N−1}` through `u`; conditions
row N+2 and rows 2N+1..4N.

```text
t  field           full chart (u present)   pivot locus not excluded (no u)   negative control (first t+1 conditions)   time
3  GF(31991)       UNIT  (14 s)             UNIT  (176 s)                     dim 6, NONUNIT (61 s)                    ≤ 1 s for the charged bottom_up.py
3  Q(d), 3d²=4     not finished (29 min, §9) —                                —                                        —
4  GF(31991)       TIMEOUT 2400 s (§9)      —                                 —                                        27 s for the charged bottom_up.py
```

At t = 3 the dual chart is empty even on the pivot locus (consistent with `V(J) = {0}`) and the negative control is
non-unit: the L-recursion is a correct instrument, but slower than the Theorem H rows and the P-recursion, and it
grows faster with t (the `u`-substitutions carry the pivot denominators into every row). The t = 2 controls are in §4.
## 6. Task (5): verdict, the exact obstruction, the best next instrument

**No uniform theorem is obtained; (R) is not proved; theorem (T) is not promoted for any new index.** The
propositions of §2–§4 are PROVED-HERE as STRUCTURE (identities and finite algebraic statements, each with a written
proof and a machine check); none is the uniform statement.

**The exact obstruction, restated in the three equivalent charts.** For every N ≥ 9 (t ≥ 8) one must show:
(i) the 2N truncation conditions `Φ_{2N+1} = … = Φ_{4N} = 0` of the universal recursion (2N quasi-homogeneous rational
functions in N+3 unknowns) have no common zero off `B eta = 0`; equivalently (ii) Theorem H's `E_2..E_{2t}` have
`B eta ∈ rad J`; equivalently (iii) for no polynomial P of degree 2N with the marked jets does the Hensel factor
`F_0` of the quartic `Q_P` have a polynomial root of degree N with `lc = 1/y`. What this lane adds is a set of
constraints on the SHAPE of any uniform proof: it cannot come from a residue or monodromy integrality (Prop. 3.1:
the only integer residue is −2N and it IS (UT)); not from a linear or determinantal eliminant (§4.1: quadratic in P,
quartic in L; the L-pivot is k-independent so the L-side has no resonance to exploit); not from per-equation
counting (charged); not from the special strata (monomial stratum, charged §5; `P = −L²/4`, Prop. 4.3: both are the
t = 2 family alone). The one genuinely new uniform handle is the tacnode dichotomy: a polynomial solution has
either a degenerate tacnode (`4 eta + 3 b l_2 = 0`, as every known solution does) or a second convergent branch `L̃`
of `F_0` through `(0, −b)` that is a formal solution with the same P; no argument excluding the latter is known
(`OPEN[K16-UF-DEGENERATE-TACNODE]`, §8).

**Best next instrument.** For fixed t: unchanged — Theorem H's rows plus the weight-graded Macaulay certificate for
`(B eta)^n`; the dual chart of Prop. 4.2 is a valid second instrument but not a cheaper one (§5). For the uniform problem: the sharpest object is the Hensel factor `F_0(x, L)` of
`Q_P` — its coefficients `s(x), p(x)` are power series determined by P alone, and (R) is the statement that
`L² + s L + p` has no polynomial root with the prescribed degree and leading coefficient for any admissible P.
This is a statement about ONE quadratic over `k[[x]]` per P rather than about a t-indexed family of ideals; the
needed theorem — "such a quadratic has no polynomial root of degree `deg(P)/2`" — is not known.
## 7. FALLACY-v2 check

- **Prime label/derivative.** `P', L', W'` are x-derivatives (charged §7.1); `theta = x d/dx` is declared; `L̃, l̃_2`
  are labels (the second branch), not derivatives; Astra's `H` of (RC1) is `Hdiff`, distinct from the slice
  determinant `H`.
- **Variable/ring map.** Every Singular ring is declared with generator order, weights and coefficient field
  (`(0,d)` with `minpoly 3d²−N`, or `GF(p)` at a declared root); the ray specialisation is `l_j ↦ c_{N−j}/y`,
  `l_N ↦ 1/y`; frozen rows are compared by `imap` under the identity map on `(c_i, b)`, never by name.
- **Floor/attainment.** `deg P = 2N` is charged (exact); `deg D = 3N` is exact by its leading coefficient; the
  minimal b-powers of §5 are minima found by search, reported as such.
- **Raw remainder / `sat()`.** No `sat`; memberships are `reduce` against a reduced `std`, with the multiplier
  power reported; radicals via `primdec.lib` only at t = 2 (dimension ≤ 1).
- **Modular → char 0.** The t = 5 membership and the dual-chart units are modular controls, labelled so; the t = 3
  and t = 4 memberships are exact over `Q(d)`; no modular statement is promoted.
- **Number vs degree; generic-coefficient theorems.** No counting theorem is applied. Briot–Bouquet is applied to
  ONE equation at a time with its exponent computed (`3` at 0, `4N + 6d` at ∞) and its case named; nothing is
  inferred across t from it.
- **Flag/place/series, exit sets, pole identities, 8.5, arrival index:** not touched. No exit-price assertion is
  made; the `charge_basis` line is inapplicable.
## 8. OPENs

OPENS RAISED

- `OPEN[K16-UF-DEGENERATE-TACNODE]` — does every polynomial solution `(P, L)` of (UF) with the marked jets have a
  degenerate tacnode, i.e. is `4 eta + 3 b l_2 ∈ rad J_t` for every t (equivalently: can the second Hensel branch
  `L̃` of `F_0` be a formal solution distinct from a polynomial L)? QUANTITY: number of indices at which the
  statement is verified independently of (V0) = 1 (t = 2, both roots); first index at which it is not implied by
  the banked (V0) = 8. A proof would reduce (R) to the degenerate stratum `eta = −(3/4) b l_2`, where the second
  pivot `2 B l_2 + b² l_3 + 2 b w_2` governs.

OPENS RETAINED

- `OPEN[K16-UF-SECOND-KIND-FAMILY]` (charged): unchanged; sharpened to the Hensel-factor form of §6. QUANTITY:
  number of known theorems bounding polynomial roots of a power-series quadratic of the shape Prop. 4.1(c) = 0.
- `OPEN[K16-INTRINSIC-SLICE-UNIT]` (charged): unchanged. QUANTITY: first index without an exact certificate = 8.
- `OPEN[K16-UNIFORM-POINT]` (charged Galois lane): untouched. QUANTITY: #{t : a closed-form point of Γ_t is known} = 0.
## 9. Computation record (`box/k16-universal-20260905/`), collision scan, completion

```text
manifest.sha256, input-verification-final.log   custody (awk manifest; sha256sum -c 4/4 OK at start and at sealing)
universal_recursion.py/.json/_K12.log           Props 2.1, 2.2, 3.1, 4.1(a,b), 4.2 with generic jets, K = 9, 12: ALL_PASS
tacnode_checks.py/.json, degenerate_pivot.py/.json   tangent cone + discriminant; P = −L²/4 reduction; second L-pivot (k = 5..10)
custody_bu.py → custody_bu_t3.*                 exact t = 3 (full numerators); custody_bu_t4.* exact TIMEOUT 1500 s at k = 16 (superseded)
custody_bu_red.py → custody_bu_red_t4.*, _t5.*  exact, numerators reduced mod std(J): t = 4 complete (std 10 s); t = 5 rows equal, std: see below
custody_bu_t4_p31991_d4933.out, custody_bu_t5_p31991_d6434{,_long}.out   modular controls (short t = 5 run: k ≤ 20 then TIMEOUT)
socle.py → socle_t{3,4}.sing, socle_t5_p31991.sing   socle degrees 14, 21, 30 (kbase max weight)
dual_chart.py → dual_chart_t3_p31991_d14162.*, dual_chart_t3.*, dual_chart_t4_p31991_d4933.*   dual charts (§5, below)
t2_controls.sing/.out                            t = 2 both roots: V(J), rad J, L-pivot ∈ rad J, P + L²/4 on c_1 = 0
prelim_report.md, collision_scan{,.filtered}.txt, artifacts.sha256, hash_artifacts.sh, finalize.sh, sections/
```

All CAS work local, `--cpus=1`, ≤ 4 Singular processes at once. One shell was lost to a self-matching `pkill -f`
(no artefact affected; three misplaced driver copies were moved from the repository root into the box).

Collision scan (`ops/open_collision.py --root .`, filtered of this lane's files): `OPEN[K16-UF-DEGENERATE-TACNODE]`:
**NONE**. Retained OPENs: 17(ccccccc), 17(jjjjjjj) (the charged sources), 17(yyyyyy)/(zzzzzz)/(hhhhhhh)/(eeeeeee) (Moh/census
deltas: lexical noise), the K16 deltas 17(xx)–(vvvvvv) for `OPEN[K16-UNIFORM-POINT]` (KNOWN), and two lines of the
same-round `ideation-20260905T1200Z-astra.md` (uncharged, not read). Nothing closes any OPEN.

Status of the long runs at sealing:
- `custody_bu_t5_p31991_d6434_long.out` (modular t = 5): COMPLETE — vdim 1709, memberships k = 4..24 all b-power 0,
  L-pivot ∉ J, its 4th power ∈ J, B³, eta⁴, b⁶ ∈ J (weight-forced above k = 4 / socle degree 30, §5).
- `custody_bu_red_t5.out` (exact t = 5): rows/B/eta/T equal (exact); the exact `std(J)` over Q(d) had not finished after
  32 min and was stopped at seal — no exact t = 5 membership is claimed (modular control only).
- `dual_chart_t3.out` (exact dual chart, t = 3): substitutions done, `std` not finished after 29 min, stopped at seal — no claim.
- `dual_chart_t4_p31991_d4933.out` (modular dual chart, t = 4): TIMEOUT at 2400 s inside `std` (the charged P-recursion
  chart is unit in 27 s): the dual chart is the more expensive instrument, as stated in §5–§6.

<!-- BODY-END -->
