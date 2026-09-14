
## 3. The all-or-nothing lemma, its étale lift, and the auxiliary lemmas the instrument stands on

Throughout, `K = A_t`, `R = O_{K,𝔭}` for a prime 𝔭 of `O_K`, `k = O_K/𝔭` (= `F_p`: only split primes are used),
`K̂, R̂` the completions.  `A := R[b4,q]/I_2(N)` is the R-model of the cone (the exact minors are 𝔭-integral),
`M := A/(b4−1)A` the R-model of the chart, `M_K = O(Y_t)`, `M_k = O(Y_t ⊗ k)` (the mod-p chart scheme: the mod-p
generators are the reductions of the exact ones, §1).

**Lemma 3.1 (all-or-nothing).**  Let `f ∈ P_t[b3]` have coefficients in K and let `Z ⊂ Γ_t(K̄)` be one
`Gal(K̄/K)`-orbit.  Then `f(P, β(P)) = 0` for every `P ∈ Z` or for none, where `β(P) = −C_r(P)/B_r(P)` for any r
with `B_r(P) ≠ 0` (Gal-equivariant: `B_r, C_r` are K-rational and `−C_r/B_r` is r-independent on a rank-1 point).
*Proof.*  `σ(f(P, β(P))) = f(σP, β(σP))` and Gal is transitive on Z.  ∎  For `f = T_{t,2t−1}` (equivalently the
K-rational vector `(W_1..W_{t−1})`, which vanishes at P iff `T_{t,2t−1}(P, β(P)) = 0` when some `B_r(P) ≠ 0`, while
`W_r(P) = a_0 C_r(P)² ≠ 0` if all `B_r(P) = 0` — FITT):

> **Corollary 3.2.**  Clause (ii)_t holds on an orbit iff it holds at one of its points.  With `k_t` affine and
> `b_t` boundary orbits, clause (ii)_t is `k_t + b_t` non-vanishings, one point each.  For `k_t = 1` (proved here,
> t = 3..6) and the boundary done exactly (§5.3), clause (ii)_t is ONE non-vanishing at ONE affine point.

**Lemma 3.3 (flat model from the Hilbert function).**  If `dim P_k/I_2(N)_k = 1` (printed `CONE dim = 1`), then
(a) `dim P_K/I_2(N) = 1`; (b) A is R-torsion-free; (c) M is R-torsion-free.  *Proof.*  (a) `Proj A → Spec R` is
proper, so the special-fibre dimension is ≥ the generic one (EGA IV 13.1.5); the generic fibre is nonempty
since `ht I_2 ≤ t−2 < t−1`.  (b) In the CM rings `P_K, P_k` the height of `I_2(N)` is then the generic t−2, so
the Eagon–Northcott complex resolves over both fields (EN-CURVE, 17(rrrrr)) and `HF_K = HF_k` in every weight.
Each `A_d` is a f.g. R-module, `A_d ≅ R^{r_d} ⊕ T_d`, `r_d = HF_K(d)`, `HF_k(d) = r_d + dim T_d/𝔭T_d`, so `T_d = 0`.
(c) `b4` has weight 1, so `A/(b4−1) ≅ (A_{b4})_0`, torsion-free as a piece of a localisation of A.  ∎

**Lemma 3.4 (freeness).**  Let M be torsion-free over the DVR R with `n' = dim_K M_K < ∞`, `n = dim_k M/𝔭M`.
Then `n' ≥ n`, and `n' = n` ⇒ M is free of rank n.  *Proof.*  Lifts `m_i` of a k-basis of `M/𝔭M` are
K-independent (scale a relation to integral coefficients not all in 𝔭 and reduce), so `n' ≥ n`.  If `n' = n`,
write `m = Σ c_i m_i`, `c_i ∈ K`; if `v = min val(c_i) < 0` then `π^{−v}m ∈ 𝔭M` maps to 0 in `M/𝔭M` while its
coefficients are integral with a unit among them — contradiction with the independence of the `m̄_i`.  ∎
(Torsion-freeness is essential: `K ⊕ k` has `n' = n = 1`.)

**Lemma 3.5 (good reduction of the point polynomial).**  Assume `CONE dim = 1`, `n' = n`, and let `m̄ ∈ k[x]` be the
minimal polynomial of `q̄_2` on `M_k` with `deg m̄ = n`.  Then the exact point polynomial `f_t` (minimal polynomial
of `q_2` on `M_K`) is in `R[x]`, has degree n, and `f_t mod 𝔭 = m̄`.  *Proof.*  M is R-free of rank n (3.3, 3.4)
and `q_2`-stable; the minimal polynomial of an integral endomorphism over the integrally closed R lies in `R[x]`.
Reducing `f_t(q_2) = 0` gives `m̄ | f̄_t`, and `deg f̄_t ≤ n = deg m̄` forces equality.  ∎

**Corollary 3.6 (degree-pattern criterion).**  Under 3.5, if `m̄` is squarefree with irreducible factors of
degrees `d_1..d_s`, the Frobenius at 𝔭 acts on the n points with cycle type `(d_1..d_s)` (Dedekind), and every
monic factor of `f_t` over K is 𝔭-integral (Gauss) with degree a subset sum of `{d_j}`.  If the intersection over
several good primes of the proper subset sums is empty — e.g. if `m̄` is irreducible at ONE prime — `f_t` is
irreducible over `A_t`: the affine points of `Γ_t` are one Galois orbit.  ∎

**Lemma 3.7 (étale lift — the FALLACY-v2 statement).**  Assume `CONE dim = 1` (M flat, 3.3c) and let
`P̄ ∈ Y_t(k)` be a simple point (`vdim` of the fibre `J_1 + (q − P̄)` equal to 1; Jacobian rank t−2 printed).
Then `Spec M → Spec R` is étale at `P̄`, so `P̄` lifts uniquely to `P ∈ Y_t(R̂) ⊂ Γ_t(K̂)` (EGA IV 18.5.17), and
`g(P, β(P)) ≡ g(P̄, β̄) (mod 𝔭̂)` for every `g ∈ R[q, b3]`.  Hence `W_r(P̄) ≠ 0 ⇒ W_r(P) ≠ 0`: the non-vanishing is
at a genuine characteristic-0 point of `Γ_t`, the Hensel lift of `P̄`.  The lift needs flatness and simplicity;
it does NOT need `n' = n`.  ∎

**Lemma 3.8 (boundary bookkeeping).**  `d_Γ(t) = n' + Σ_{L ⊂ {b4=0}} e_L/g_L` (`e_L` multiplicity of the boundary
line L, `g_L` the gcd of the weights of its nonzero coordinates).  For the stratum chart `Y_{t,j} = Spec P/(I_2 +
(b4, q_{<j}, q_j − 1))`, `vdim Y_{t,j} = Σ_{L ⊂ stratum} (j/g_L) ℓ_L` with `ℓ_L = length(A_L/b4A_L) ≤ e_L` (the cone
`V(I_2, b4)` has no embedded component off the origin, by G_m-equivariance).  Hence the stratum contributes
`≥ vdim(Y_{t,j})/j` to `d_Γ − n'`.  ∎  (With 3.4's `n' ≥ n` this gives `n' = n` from the boundary alone, §5.3.)
