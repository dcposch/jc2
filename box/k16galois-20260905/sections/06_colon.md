
## 6. Task (5): the liaison cross-check — `(G_1..G_{t−1}) : T_{t,2t−1} = (G)`

`S_t/(G)` is the complete-intersection curve `V(G) = (b3-axis, multiplicity C(2t,t−1)) ∪ (lift of Γ_t)`
(17(rrrrr) §5.3); it is Cohen–Macaulay of dimension 1, so its associated primes are its minimal primes and
`T_{t,2t−1}` is a nonzerodivisor on it iff it vanishes identically on no component, i.e. iff clause (ii) holds
at every point of Γ_t (affine AND boundary) and `a_0 ≠ 0` on the axis.  So `(G) : T_top = (G)` is exactly
clause (ii) in its ideal-theoretic form, tested on the whole curve at once and independently of §4–5.

```text
 t  field               (G): dim, mult      (G):T_top  ==  (G)?    control (G):G_1 = (1)?   control (G):b4 == (G)?  (expected NO: the axis lies in b4=0)
 3  exact A_3           1, 45               YES (10 gens, all reduce to 0)   YES                      NO   ✓
 3  GF(32003)           1, 45               YES                    YES                      NO   ✓
 4  GF(32029)           1, 286              YES (53 gens)          YES                      NO   ✓
 4  exact A_4           1, 286 (std 55 s)   see §9 (quotient running at seal)
 5  GF(32009)           1, 1820             YES (262 gens, 4 s)    YES                      NO   ✓
```

`mult(G) = 45, 286, 1820 = C(3t+1,t−1)` is the CI degree (LENGTH-SPLIT), as it must be.  The colon equality at
t = 3 (exact), 4, 5 (mod p) is the arithmetically-CM cross-check the card asked for and agrees with §5 at every
index.  A modular colon equality is evidence only: a nonzero element of `((G):T_top)/(G)` over K has nonzero
reduction at all but finitely many 𝔭, which could include the one tested; the exact t = 3 run and §5 carry the
char-0 weight.
