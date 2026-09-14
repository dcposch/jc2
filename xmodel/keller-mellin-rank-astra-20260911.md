# Keller Mellin rank versus first-delta selection

Owner: /root/contact_collision_geometry (Astra). Basis: 0d39df3c9fd69c939a8420c54d03228b9077777d.
First action: 2026-09-11 22:01:47 UTC. Original publication reserve 22:20 UTC; HARD 22:23 UTC, unchanged.

Verdict: the stated Mellin-rank formula holds, using the named standard external theorems below. Finite rank does not supply a first-order delta relation: the explicit rank-two control has no invariant rational line. This is an interface result, not a Keller-map exclusion.

## 1. Rank attachment

Write F=(p,q):X=A²_C→Y=A²_C, with nonzero constant Jacobian, A=C[p,q], R=C[x,y], N=R/A, B=C[e_p,e_q], E=Frac(B). All modules are left modules. The inverse Jacobian defines commuting polynomial derivations ∂p,∂q on R; thus R, A and N are Weyl modules. F is affine, étale, dominant and quasi-finite, but is NOT assumed finite or proper.

External inputs, distinguished from the deductions: (i) algebraic D-module direct image preserves holonomicity; (ii) the corrected Loeser–Sabbah Mellin-rank theorem for holonomic torus modules, restated as BBKP Theorem 35 for affine Weyl modules; (iii) algebraic de Rham comparison for smooth complex varieties, and additivity of their Euler characteristic. Bass's B-torsion-freeness of N is stipulated by TASK, not reproved. The corrected primary theorem is [Loeser–Sabbah (1992), Theorem 2(1)](https://webusers.imj-prg.fr/~francois.loeser/loeser-sabbah_cras1991-92.pdf), printed pp.1263–1264. [BBKP, Theorem 35 and (3.5)–(3.6)](https://arxiv.org/pdf/1712.09215v2) fixes the shift convention. No hypergeometric rank-one classification is imported.

The direct-image identification needs no properness: for an étale map the transfer tensor with O_X is O_X with its lifted target connection, without a relative shift; affineness kills higher quasi-coherent pushforwards. Hence F_+O_X is R in degree zero. It is a finitely generated holonomic D_Y-module by (i), not necessarily a finite A-module. This discharges the precise holonomicity hypothesis of (ii).

Let T={pq≠0}⊂Y and X_T=F⁻¹(T). Torus restriction is R[1/(pq)]. Because dp,dq form a basis of Ω¹_X, its target de Rham complex identifies with the ordinary algebraic de Rham complex of X_T, shifted by [2]. In particular its Euler characteristic is (+1)χ(X_T), not its negative. The theorem gives

    dim_E(E⊗_B R)=χ(X_T)<∞.

Each polynomial in A is B-torsion: if its p-exponents lie in a finite set S, ∏_(i∈S)(e_p−i) annihilates it. Thus E⊗_B A=0. Flat localization of 0→A→R→N→0 yields E⊗_B N≅E⊗_B R. Inclusion-exclusion on the SOURCE now proves exactly

    rank_B N = 1−χ_X(p=0)−χ_X(q=0)+#F⁻¹(0,0).

The final intersection is finite and reduced by étaleness. Ordinary and compact-support Euler characteristics agree here for complex algebraic varieties, so the additive formula applies even for noncompact curves. If one translates the target origin into an open set where F is finite étale of geometric degree d=[C(x,y):C(p,q)], the count becomes d. The curves and Euler operators must then also be translated: this is not invariance of rank under arbitrary target changes. For the identity map the complement is (C*)², of Euler characteristic zero, and N=0. Using χ(X)=1 instead would already fail that control.

The formula is nonnegative by its rank interpretation; no numerical value or vanishing is asserted for a hypothetical noninvertible Keller map. If rank were zero, stipulated B-torsion-freeness would give N=0, hence R=A. Establishing that vanishing is a further source problem, not a consequence of the formula.

## 2. Exact difference-module control

The actual commutators give δb=σ(b)δ, where δ=p∂q, σ(e_p)=e_p−1 and σ(e_q)=e_q+1. Put z=e_p and t=e_p+e_q, so B=C[t,z], E=C(t,z), σ(t)=t, σ(z)=z−1. Define M=Bv₁⊕Bv₂ and extend semilinearly from

    δv₁=v₂,       δv₂=zv₁,       δ(bv)=σ(b)δv.

This is an exact module over U=B[δ;σ]. It is B-free, hence B-torsion-free, and E⊗_B M has dimension two. Every m is U-torsion: three vectors m,δm,δ²m are E-linearly dependent; clearing the left coefficients' common denominator gives a nonzero Ore polynomial annihilating m. Injection M→E⊗M makes that relation valid in M itself. For example (δ²−z)v₁=0. Localized δ is invertible since its semilinear matrix has determinant −z≠0.

Nevertheless there is NO δ-stable E-line. The lines Ev₁ and Ev₂ are not stable. Any other line has a generator av₁+v₂ with a∈E*. Stability would require

    z v₁+σ(a)v₂=λ(av₁+v₂),  hence  aσ(a)=z.

For rational functions in z over C(t), define deg_z a=deg(numerator)−deg(denominator). Translation z↦z−1 preserves this integer degree. The left side has even degree 2deg_z a, whereas z has degree one. Contradiction, including all possible finite poles and zeros of a.

Consequently NO nonzero m∈M has a nonzero annihilator b₁δ+b₀ with b₀,b₁∈B: if b₁≠0 it produces the forbidden line after localization; if b₁=0, B-torsion-freeness contradicts b₀m=0. This tests existence, not merely the degree of a chosen vector's annihilator. Changing the same definition to δv₂=v₁ gives stable lines E(v₁±v₂), so the odd-degree multiplier is genuinely load-bearing.

M is an abstract difference module, NOT claimed to extend to a full Weyl module, arise from a commutative algebra, or equal an actual Keller quotient. It refutes precisely an inference from B-torsion-freeness, U-torsion and finite Mellin rank alone. Extra source structure might still force a line.

## 3. Interface, limits, and completion checks

For the actual module V=E⊗_B N, the smallest missing first-order-selection fact is the existence of a δ-stable E-line whenever N≠0. Such a line intersects N nontrivially after clearing denominators, so it is equivalent to existence of a nonzero source class with some first-order U-relation. A finite rank r only supplies vectorwise relations of degree at most r. Rank one would supply a line; rank two or more does not. No rank-one source theorem has been obtained here.

There is a SECOND, narrower interface requirement for the family

    e_p−r+δ G(e_p,e_q),     r∈Z_≥0, G∈B.

A general first-order relation aδ+b does not automatically have that form: in left Ore normal form the displayed family has coefficients σ(G)δ+(e_p−r). A rational change of generator changes the coefficient ratio by a σ-coboundary; rank gives neither the integral resonance r nor polynomial G. In addition, a relation in N says only that its value on a representative f∈R lies in A, not that it is zero in R. Applying a homogeneous algebraic-germ theorem requires a separately justified correction by an element of A (or an inhomogeneous theorem). No such correction, normalization, or first-order-selection premise is supplied by the rank formula.

Thus a theorem excluding nonpolynomial algebraic germs for the displayed operator family cannot yet be composed with this result to exclude an arbitrary Keller source. The next useful source-specific target remains this selection/lifting bridge, rather than another formal family or a numerical rank guess. No assertion that arbitrary annihilators have first delta order, no actual source vanishing, and no JC2 or novelty claim follows.

Source audit limit: corrected LS Theorem 2(1), not the uncorrected 1991 higher-dimensional proof, is used. BBKP Appendix B was read, but its optional final ∂-locally-nilpotent-subspace argument is not used: C[x,x⁻¹] already has 1 locally ∂-nilpotent and x⁻¹ not locally ∂-nilpotent. The subspace need not be a torus D-submodule. The standard Koszul spectral-sequence Euler identity and the independently stated corrected theorem avoid that step. This is not a refutation of the rank theorem.

OPEN quantity: existence of a δ-stable E-line in an ACTUAL nonzero Keller N, then a lift satisfying the specified homogeneous relation. Cheapest discriminator: a manual source-specific line/lift argument or faithful source countercontrol; planning wall 900 seconds, UNMEASURED, not execution authority. No generic extension theorem is proposed as a substitute. Collision check is own-output/allowed-input only: no corpus novelty audit; no current peer or ROOT report read. Documentary source rendering/hashing only, no scientific subprocess, payload, worker, protected access, or descendant. Source versions, exact read scopes, clipping recovery, and limits are in the owned SOURCE-INDEX and READ-SCOPE; terminal current pins and transaction verification are recorded separately.

Preseal completion: own substantive partial read WHOLE at 22:11 UTC; all four owned documentation objects read WHOLE; local input and owned pins rechecked 22:12:17 UTC. Final/manifest destinations still absent; no collision, no placeholder, and only the explicitly scoped OPEN above remains. Remote source postpins matched at 22:09 UTC. Scientific work ends here; final transaction/readback/custody only. Original deadlines unchanged.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9103`.
- Body SHA-256:
  `d28b7505d4a289211fe05f549f8d899339402c40d98121777d544abf171c64a0`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
