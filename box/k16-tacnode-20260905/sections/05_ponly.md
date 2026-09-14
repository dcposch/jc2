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

Remark. On `b = 0` (where
`Q_P(0, Y) = (3/16)Y⁴` and the tacnode picture does not apply) the OPEN reads `eta ∈ rad(J + (b))` and (i) gives
`18Bw_2 - 6eta² ∈ J + (b)`, so there it is equivalent to `B*w_2 ∈ rad(J + (b))`; no claim is made on b = 0 (Astra's chart, charged §7.3).
