
## 7. Task (4): the uniform problem (I) — is Γ_t ∩ {b4 ≠ 0} one orbit over A_t for ALL t?  Typed OPEN, with the structure

**What is proved.**  `k_t = 1` for t = 3, 4, 5, 6 with `Gal(f_t/A_t) = S_{n_t}` (t ≤ 5; t = 6: `⊇ A_1548`, and
`S_1548` since odd cycle types occur).  The boundary orbits are `b_3 = 1`, `b_4 = 0`, `b_5 = 2`, `b_6 = 0`.

**What the determinantal structure gives, and what it does not.**  `Γ_t` is the rank-≤1 locus of a `(t−1)×2`
matrix of weighted forms, cut out by the `C(t−1,2)` minors; the EN complex makes `P_t/I_2(N)` CM of dimension 1 with
Hilbert series determined by the weights alone, hence `d_Γ(t)` and `n_t = d_Γ(t) − (boundary)` are uniform.
Irreducibility, however, is NOT a consequence of the resolution: `I_2(N)` is generically reduced with `d_Γ(t)`
distinct points, and which field of definition those points have is a property of the specific entries `B_r,
C_r`, not of the format.  Three uniform routes were examined:

1. *Bertini/monodromy in a family.*  If `(B_r, C_r)` were a general member of the linear system of pairs of forms
   of weights `(t+1+r, 2t+2+r)`, the monodromy of the `d_Γ` points would be the full symmetric group (uniform-position
   for a general 0-dimensional determinantal scheme: the incidence variety over the parameter space is irreducible
   and the discriminant has codimension one), which is exactly what §4.3 measures.  But K16 is ONE point of that
   parameter space for each t, and Bertini says nothing about a specific member.  The measured `S_n` shows that
   K16's forms are "generic enough" at t ≤ 6; there is no theorem that they stay off the (codimension-one)
   locus of imprimitive/reducible monodromy for all t.  This is the same discriminant-avoidance typing as
   (V0)-tail itself (my card §1.2): (I) RELOCATES the genericity, it does not remove it.
2. *A resultant/elimination argument in t.*  At t = 3, `f_3` is the weight-14 part of the single minor
   `B_1 C_2 − B_2 C_1`, a binary form; irreducibility over `Q(√3)` was decided by factoring.  For t ≥ 4 the point
   polynomial is an eliminant of `C(t−1,2)` minors whose coefficients are the spine scalars (no closed form in t,
   17(rrrrr) §7, brcr CORRECTION), so no uniform Eisenstein/Newton-polygon criterion can even be written down;
   the natural candidate prime `p = 4t+1` (K16 p-adic regularity, banked) is only prime for some t.
3. *Chebotarev.*  The cycle-type statistics at t = 3..6 are those of `S_n` and determine the group — one t at a time;
   there is no t-uniform Frobenius.

**What a proof of (I) for all t would need**: a uniform *transitivity witness*, e.g. a t-indexed prime `𝔭_t` at
which `m̄` is a full `n_t`-cycle (at t = 4: 32323, 32443, 32579, 32749; at t = 3: nine of 49); one such prime is a
complete proof by 3.6, but full cycles have frequency `1/n` in `S_n` and nothing suggests a structural prime.
Typed `OPEN[K16-GAMMA-IRREDUCIBLE]` for t ≥ 7 with this quantity.

**Is (I) even necessary?**  No — and this is the useful observation.  Corollary 3.2 needs only `k_t + b_t`
evaluations, one per orbit; the instrument does not need to KNOW the orbits: it needs, for each orbit, one simple
point mod some prime.  Equivalently, the fixed-t certificate of clause (ii) is: a set of simple `F_p`-points of
`Γ_t` (over one or several primes) whose Hensel lifts meet every Galois orbit — which is exactly what
`vdim(J_1 + (W)) = 0` mod p certifies in one shot when combined with flatness (every geometric point of the
mod-p chart has `W ≠ 0`; every K̄-point specialises to one of them; by 3.7 applied in reverse — a K̄-point of the
flat proper model specialises to a k̄-point of the special fibre, and `W(P) = 0` would force `W(P̄) = 0`).  So

> **Proposition 7.1 (modular clause (ii) without irreducibility).**  If `CONE dim = 1` mod 𝔭 (flat model) and
> `V(I_2 + (W_1..W_{t−1})) = {0}` in `P_k` (a positive-weight cone statement, promotable by the banked properness
> lemma), then clause (ii)_t holds over `A_t`.  *Proof.*  By 3.3 the model `A` is flat; `Proj A → Spec R` is proper,
> so every `K̄`-point `P` of `Γ_t` extends to an `R̄`-point and specialises to a `k̄`-point `P̄` of `Γ_t ⊗ k`;
> `W_r(P̄) = W_r(P) mod 𝔭̄`; if all `W_r(P) = 0` then all `W_r(P̄) = 0`, contradicting the hypothesis.  ∎

This is the charged/banked promotion route (rank lane §8) re-derived; it needs no orbit count.  What the Galois
mechanism adds is not logical strength but COST and STRUCTURE: it turns `d_Γ(t)` non-vanishings into `k_t + b_t`
non-vanishings and tells one that the `d_Γ(t)` points are a single algebraic object (an `S_n`-extension of `A_t`).
The honest all-t statement is therefore: `(V0)-tail_t ⟸ (i)_t ∧ [one simple point per orbit with W ≠ 0]`, and
uniformity fails at the same place it always did — there is no t-indexed point of `Γ_t` with a closed-form
`T_top(P_t, β_t)`.  Problem (II) is thus the binding one, and it is unchanged by this lane.
