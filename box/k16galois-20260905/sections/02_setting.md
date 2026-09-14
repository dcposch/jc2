
## 2. Setting (charged conventions) and the objects of this lane

```text
A_t = Q[y]/(H_t),  H_t = 12q²y² − 12q(t+1)y + (t+1)(3t+2),  q = 2t+1;   A_t ≅ Q(√(3(t+1)))
P_t = A_t[b4, q_2, .., q_{t−1}]  (weights 1, 2, .., t−1),   S_t = P_t[b3]  (weight t+1)
T_{t,2t−1−r} = a_r b3² + b_r b3 + c_r   (r = 0..t−1),   a_0 = −α_t a unit for t ≥ 3
G_r = a_0 T_{t,2t−1−r} − a_r T_{t,2t−1} = B_r b3 + C_r,   N = ((C_r, B_r))_{r=1..t−1},   Γ_t = V(I_2(N)) ⊂ Spec P_t
W_r = a_0 C_r² − b_0 B_r C_r + c_0 B_r²;   at a rank-1 point p with kernel (1:β):  W_r(p) = B_r(p)² T_{t,2t−1}(p, β)
clause (i):  V(B, C) = {0};   clause (ii):  T_{t,2t−1}(p, β(p)) ≠ 0 at every point p ≠ 0 of Γ_t   (FITT, 17(rrrrr))
(V0)-tail_t  ⟺  (i) ∧ (ii)   ⟹  (V0)_t  ⟹  (8.1)_t  ⟹  (T)_t
```

`Γ_t` is a cone over a zero-dimensional weighted-projective scheme; its affine chart `{b4 = 1}` is the
zero-dimensional scheme `Y_t := Spec P_t/(I_2(N) + (b4 − 1))` in the coordinates `q_2, .., q_{t−1}`, and its
boundary `{b4 = 0}` is stratified by the first nonzero coordinate.  The **point polynomial** `f_t ∈ A_t[x]` is
the minimal polynomial of the coordinate `q_2` on `Y_t ⊗ Ā_t`; when `q_2` separates the geometric points and
`Y_t` is reduced, `deg f_t = #Y_t(Ā_t)` and `A_t[x]/(f_t) ≅ O(Y_t)`, so the `Gal(Ā_t/A_t)`-orbits of the affine
points of `Γ_t` are exactly the irreducible factors of `f_t` over `A_t`.

**Charged as measured (17(tttttt))**: `Y_t` reduced with 7, 46, 265 points at t = 3, 4, 5 (mod p), `f_3`
irreducible over `A_3` (exact), Frobenius (2,5) at p = 32003.

### 2.1 Summary table (all entries measured in this lane unless marked charged)

```text
 t  A_t          n_t = #Y_t  boundary of Γ_t (b4=0)                   f_t irreducible over A_t?      Gal(f_t/A_t)      one-point test (ii)   colon (G):T_top = (G)
 3  Q(√3)        7           q_2-axis point (rational)               YES exact + 49 primes          S_7  (proved)      YES (28 primes; bdry exact)   YES exact, YES mod p
 4  Q(√15)       46          none (exact: slice b4=0 has dim 0)      YES (48 primes; 46-cycle)      S_46 (proved)      YES (28 primes)               YES mod 32029; exact: see §6
 5  Q(√2)        265         6 pts (b4=0,q2=1,q3=0) + q_3-axis pt    YES (24 primes)                S_265 (proved)     YES (17 primes; bdry exact)   YES mod 32009
 6  Q(√21)       1548        none (mod p ⇒ none over A_6)              YES (8 primes; 3.6)            S_1548 (proved)    YES (5 primes)                not run
 8  Q(√3)        (52140)     6 pts in stratum q_3 = 1 (mod 32003)     not attempted                  —                  §5.3 (msolve at seal)         not run
```
