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
