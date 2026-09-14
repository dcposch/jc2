
## 5. Tasks (2)–(3): the one-evaluation instrument, run at t = 3, 4, 5, 6 (and t = 8, §5.3), and the boundary

### 5.1 The instrument (what one modular evaluation proves, by 3.1 + 3.7)

At a split prime 𝔭 with `CONE dim = 1` (flatness, 3.3) take a root `v` of a linear factor of `m̄(q_2)`; the
fibre `J_1 + (q_2 − v)` has `vdim = 1` (printed), so it is one simple `F_p`-point `P̄ = (1, v, q̄_3, ..)` (the
Jacobian of the minors in the chart variables has rank t−2 at `P̄`, printed as `JACRANK_FREE`); all minors
vanish at `P̄` (`MINORS_ZERO=1`); `β̄ = −C_r(P̄)/B_r(P̄)` is computed from the first r with `B_r(P̄) ≠ 0` and
checked against every other r (`KERNEL_CONSISTENT=1`); `T_{t,2t−1}(P̄, β̄) = a_0 β̄² + b_0(P̄) β̄ + c_0(P̄)` and
all `W_r(P̄)` are printed, together with the FITT identity `W_r(P̄) = B_r(P̄)² T_{t,2t−1}(P̄, β̄)` (`FITTcheck=1`).
By 3.7, `P̄` lifts to `P ∈ Γ_t(K̂)` with `W_r(P) ≡ W_r(P̄) (mod 𝔭̂)`; by 3.1, `W(P) ≠ 0` propagates to the whole
`Gal(K̄/K)`-orbit of `P`; by §4 that orbit is all of `Γ_t ∩ {b4 ≠ 0}` for t ≤ 6.  **The lift is stated, not
assumed (FALLACY-v2): the char-0 point is the Hensel lift of a simple point on the flat model; no modular
non-vanishing is promoted without it.**

### 5.2 Results

```text
 t  #𝔭 with a rational point / #𝔭 tried   W ≠ 0 at the lift (all of them?)   example (p, b): P̄ = (b4, q_2, ..), β̄, T_top(P̄,β̄)
 3  28 / 49                                 28 / 28  YES                        (32183, 0): (1, 12012), β̄ = ·, T_top = −642 ≠ 0
 4  28 / 48                                 28 / 28  YES                        (32749, 0): (1, −5944, −5832), T_top = −11 ≠ 0;  (32203,0): T_top = 86
 5  17 / 24                                 17 / 17  YES                        (32479, 0): (1, 13130, −6481, 8290), T_top = 6541 ≠ 0
 6   5 / 8                                   5 / 5   YES                        (32003, 0): (1, 4339, 9016, −15982, −6895), β̄ = 12955, T_top = 13229 ≠ 0
```

(The fraction of primes with a rational point, 0.57–0.71, is the fixed-point probability in `S_n`, consistent with
4.3.)  Every rational simple point at every prime gave `W ≠ 0`; one per t suffices.  Combined with §4:

> **Clause (ii)_t on Γ_t ∩ {b4 ≠ 0} holds for t = 3, 4, 5, 6**, each by ONE modular evaluation + the étale lift +
> one Galois orbit.  For t = 3, 4, 5 this re-proves the charged exact/promoted clause (ii) by a different route
> (no number-field `std`, no `radical`); at t = 6 it replaces the promoted `dim(F_6) = 0` by an argument that
> needs only a 3 s modular `std`, a 150 s `finduni`, and one evaluation.

### 5.3 Boundary orbits (b4 = 0), exact

The boundary of `Γ_t` is the cone `V(I_2, b4)`, stratified by the first nonzero coordinate `q_j` (chart `q_j = 1`).
Exact over `A_t` (`boundary_t{3,5}_exact.out`) and mod p (t = 4, 6, 8):

```text
 t  stratum j=2 (b4=0,q2=1)                         stratum j=3 (b4=q2=0,q3=1)    higher strata   (stratum + (W_1..W_{t−1})) vdim
 3  1 point, the q_2-axis (rational)                —                             —               0  ⇒ W ≠ 0 there (exact)
 4  ∅ (slice dim 0, mod 32029)                       ∅                             ∅               —
 5  6 points with q_3 = 0; q_4-minpoly of degree 6   1 point, the q_3-axis (q_4=0)  ∅               0 and 0  ⇒ W ≠ 0 at all 7 points (exact)
    IRREDUCIBLE over Q(√2) ⇒ ONE orbit                (rational)
 6  ∅ (slice dim 0, mod 32003 and 32713/17/19)       ∅                             ∅               —
 8  ∅ (mod 32003)                                    6 points (mod 32003)          ∅               0 (mod p) ⇒ W ≠ 0 at all 6 (modular; lift as in 3.7 needs flatness, see 5.4)
```

At t = 5 the six stratum-2 points have `q_3 = 0` (the μ_2 acting on the chart fixes them, so each is a
weighted point with `g_L = 2`), the `q_4`-minimal polynomial is irreducible of degree 6 over `A_5` (printed in
`boundary_t5_exact.out`), i.e. they are ONE Galois orbit; with the rational axis point, `b_5 = 2`.  The
bookkeeping of Lemma 3.8 then reads `265 + 6/2 + 1/3 = 805/3 = d_Γ(5)` exactly over `A_5`, a second proof of
`n' = 265` independent of the exact chart `std`.  At t = 3: `7 + 1/2 = 15/2`.  W-nonvanishing on the boundary
was tested as `vdim(stratum ideal + (W)) = 0`, i.e. at EVERY geometric boundary point at once (Nullstellensatz),
exactly over `A_t` at t = 3, 5 — so clause (ii) on the boundary needs no orbit argument at all at these t.

### 5.4 Consequence for (V0) at fixed t

For t = 3, 4, 5, 6: clause (i) is charged (exact t ≤ 5, promoted t = 6..8, B-hsop), clause (ii) on the affine
orbit is §5.2, on the boundary §5.3 (t = 6: empty).  Hence `(V0)-tail_t` holds for t = 3..6 by the new route.
No new index is added to the banked `(V0)` list (t ≤ 7 was banked); what is new is the COST: at t = 6 the
whole certificate is three modular jobs of ≤ 3 min and no number-field or radical computation.
