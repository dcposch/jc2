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
