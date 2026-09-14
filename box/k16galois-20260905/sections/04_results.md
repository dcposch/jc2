
## 4. Task (1): exact factorisation of the point polynomials — Γ_t ∩ {b4 ≠ 0} is ONE Galois orbit at t = 3, 4, 5, 6

### 4.1 What was computed, per t

Per prime ideal 𝔭 (`pattern_t{t}_mod_p{p}_b{b}.out`): mod-𝔭 rows, split and identities (§1); `CONE dim` of
`P_k/I_2(N)` (t ≤ 6); `SLICE dim` of `V(I_2, b4)`; the chart `J_1 = I_2 + (b4 − 1)`: `std`, `vdim`, `dim`; `finduni`,
the ordinary degree of every chart variable's minimal polynomial, squarefreeness of `m̄(q_2)`; `factorize(m̄)` and
its degree pattern (the Frobenius cycle type, 3.6); and, whenever `m̄` has a linear factor, the instrument of §5 at
the first rational point.  The exact chart `std` over `A_t` gave `vdim = 7, 46, 265` at t = 3, 4 (< 1 s) and 5
(426 s), equal to every modular count, so `n' = n` and 3.4–3.6 apply wherever the printed hypotheses hold.  Exact
`finduni` + `factorize` over `A_t` completed at t = 3 (`7^1`: irreducible over `Q(√3)`, reproducing my round's
`gammax_t3`); at t = 4, 5 the exact `finduni` did not finish inside the caps (§9) and irreducibility is proved by
3.6, which needs no exact point polynomial.

### 4.2 The verdict per t, with the hypotheses of 3.5 checked at every prime used

```text
 t  n_t   primes 𝔭 used (all split, both 𝔭|p)   hypotheses at every 𝔭            proper-subset-sum intersection   f_t over A_t
 3    7   49 (24 p × 2, + 32003)                cone dim 1, vdim 7, deg m̄ 7, sqf   ∅  (also: m̄ irreducible at 9 𝔭)   IRREDUCIBLE (exact + 3.6)
 4   46   48 (24 p × 2)                          cone dim 1, vdim 46, deg 46, sqf   ∅  (m̄ irreducible at 32323,32443,32579,32749)   IRREDUCIBLE (3.6)
 5  265   24 (12 p × 2)                          cone dim 1, vdim 265, deg 265, sqf ∅                                IRREDUCIBLE (3.6)
 6 1548    8 (8 p, branch 0)                     chart dim 0 + slice dim 0 (⇒ cone dim 1), vdim 1548, deg 1548, sqf   ∅ (was {292, 1256} after 4 𝔭)   IRREDUCIBLE (3.6)
```

At t = 6 the exact chart `vdim` was not computed; `n' = n = 1548` follows from Lemma 3.8 with an EMPTY boundary:
the slice `V(I_2, b4)` has dimension 0 mod p, hence (properness: a nonempty generic fibre would specialise to a
nonempty special fibre) the boundary of `Γ_6` over `A_6` is empty and `n' = d_Γ(6) = 1548`.  The same argument
gives `n' = 46 = d_Γ(4)` at t = 4 independently of the exact `std` (slice dim 0 at every prime).

So `k_3 = k_4 = k_5 = k_6 = 1`: **the affine points of Γ_t form a single Galois orbit over A_t for t = 3, 4, 5, 6**.
This closes `OPEN[K16-GAMMA-IRREDUCIBLE]` for t ≤ 6 and answers the charged "is it irreducible?" with YES.

### 4.3 Frobenius cycle types and the Galois groups (proved, not conjectured)

The cycle types are the printed degree patterns (full lists: `pattern_*.out`, tabulated in `frobenius_tables.txt`).
Excerpts:

```text
 t=3 (n=7):   7 (×9), 1+2+4 (×7), 2+2+3 (×7), 1+1+2+3 (×5), 1+1+5 (×4), 1+6 (×4), 2+5 (×3), 1+3+3 (×3), 3+4 (×2), ...
 t=4 (n=46):  46 (×4), 1+45 (×4), 1+1+3+10+31 (×2), 13+33, 18+28, 5+41, 15+31, 21+25, 22+24, 1+4+41, 1+1+44, ...
 t=5 (n=265): 1+3+261, 2+3+3+257, 1+2+2+12+248, 1+4+7+9+244, 4+14+42+205, 9+14+18+21+203, ...
 t=6 (n=1548): 1+2+4+7+108+180+308+336+602, 1+2+2+47+107+120+137+1132, 1+1+1+2+524+1019, 9+26+35+114+292+1072, ...
```

*Consequences (Jordan).*  `G_t := Gal(f_t/A_t)` is transitive (4.2).  A Frobenius power is a pure c-cycle whenever
c occurs once in a cycle type and divides no other part; a transitive group containing a prime cycle of length
c > n/2 is primitive, and a primitive group containing a prime cycle of length c ≤ n − 3 contains `A_n` (Jordan);
an odd cycle type then gives `S_n`.
- t = 3: degree 7 is prime, so `G_3` is primitive; `(2,5)^5` is a transposition ⇒ **`G_3 = S_7`**.
- t = 4: prime cycles 29, 31, 41 (23 < c ≤ 43) ⇒ `G_4 ⊇ A_46`; `46` is an odd cycle ⇒ **`G_4 = S_46`**.
- t = 5: prime cycles 137, 139, 149, 181, 257 (132 < c ≤ 262) ⇒ `G_5 ⊇ A_265`; the type `1+3+261` is odd ⇒ **`G_5 = S_265`**.
- t = 6: the prime cycle 1019 (774 < 1019 ≤ 1545, from the type `1+1+1+2+524+1019` at p = 32633) ⇒ `G_6 ⊇ A_1548`; odd types present ⇒ **`G_6 = S_1548`**.

The Galois groups are FULL SYMMETRIC: the points of `Γ_t` have no hidden symmetry over `A_t` — the generic
(uniform-position) behaviour of a 0-dimensional determinantal scheme, and the datum any uniform argument for (I)
would have to reproduce (§7).
