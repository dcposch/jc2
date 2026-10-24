# A conditional finite-factor and boundary theorem for Keller maps

Producer: swarmHQ coordinator (requested gpt-6-astra).
Date: 2026-10-24 20:26:59 UTC.
Basis: `02813e10a1b27b5d379b3f05b3b2bcf72a3e6d6c`.
Evidence tier: MANUAL, conditional theorem with named standard dependencies.
Lifecycle: PRODUCER-CHECKED / UNPROMOTED; final public artifact review pending.

## Statement and scope

Let \(X\) be a smooth projective rational complex surface containing its given algebraic open \(U=\mathbb A^2_{x,y}\).
Let \(\rho:X\to Y\) be a proper birational analytic contraction to a connected normal compact surface,
identifying \(U\) with \(Y\setminus B\), where \(B\) is a nonempty reduced irreducible curve.
Write \(E\subset X\) for the divisor corresponding birationally to \(B\).
Assume the standard volume extends to a meromorphic form \(\Omega\) on \(Y\), with
\[
\Omega|_U=dx\wedge dy,\qquad \operatorname{div}(\Omega)=-B.
\]
In particular this identifies the **genuine analytic dualizing sheaf** with \(\omega_Y\simeq\mathcal O_Y(-B)\).
Let \(f:U\to U\) be an actual polynomial Keller iterate of generic degree \(N>1\), preserving this volume.
Choose a resolution \(\pi:Z\to X\), **isomorphic over all of \(U\)**, with \(Z\) smooth projective rational
and \(G:Z\to X\) extending \(f\). Set \(H=\rho\circ G\).
Assume the boundary valuation of the target has a unique extension in the source function field,
represented by the strict transform of the **source** divisor \(E\), with ramification index \(N\) and residue degree one.
Take the analytic Stein factorization \(H=h\circ r\), where \(r:Z\to W\) is proper birational,
\(W\) is normal, and \(h:W\to Y\) is finite. Put \(C=(h^{-1}(B))_{\mathrm{red}}\).

**Conditional theorem.** The surface \(W\) has rational singularities everywhere, including at infinity.
The restriction \(h|_C:C\to B\) is an isomorphism of reduced compact complex curves; both have arithmetic genus one.
These hypotheses are not asserted for every Keller map. The theorem does not prove properness or descent of \(H\) through \(\rho\circ\pi\).

## Dependencies and prior work

The standard dependencies used below are analytic Stein factorization; the exceptional-locus and connected-fibre
properties of proper birational maps to normal surfaces; meromorphic descent, projective meromorphic functions being rational,
and extension across codimension two on normal spaces; characteristic-zero transverse ramification;
compact analytic Serre duality, coherence and Leray; reflexive divisor sheaves and CM dualizing adjunction; and finite-curve Euler characteristic.
These are named imports with their hypotheses specified here; no source-paper proof or formal verification is supplied.
Compare the affine-normalization and smooth ample-section arguments recorded in [AUDIT](../AUDIT.md) and [APPROACHES](../APPROACHES.md).
The present argument uses the strong primitive compactification and source-valuation hypotheses to address the entire compact finite factor.
No novelty or priority claim is made, and no Artin algebraicity, FJ attachment, or log-singularity theorem is imported.

## Proof

**1. The source open and its valuation.** No \(r\)-exceptional curve meets \(U\): its contraction by \(H\)
would contradict local quasi-finiteness of the etale map \(f\). The normal birational exceptional-locus theorem and connected fibres
therefore make \(r|_U\) an open immersion. This identifies the actual full source plane with an open subset of \(W\).
Uniqueness of the boundary extension gives the single prime \(C\). Going-down over the normal base ensures there is no extra isolated component over \(B\).
The finite restriction \(C\to B\) has degree one on function fields.
Let \(\sigma=h^*\Omega\). On the source open it is \(dx\wedge dy\), and at the generic point of \(C\),
\[
\operatorname{ord}_C(\sigma)=N(-1)+(N-1)=-1.
\]
For any nonzero polynomial \(a\in\mathbb C[x,y]\), \(\operatorname{ord}_E(a)\le0\).
Indeed it is meromorphic on projective \(X\), hence on \(Y\) by proper birational descent, and has no polar prime on \(U\).
If its order along \(B\) were nonnegative, normal extension would make it holomorphic on compact \(Y\), hence constant.
Thus nonconstant polynomials have strictly negative order, and nonzero constants have order zero.
This argument uses the source compactification \(Y\setminus B=U\), not the unproved equality \(W\setminus C=U\).

**2. Canonical sections and rational singularities.** If \(0\ne\tau\in H^0(W,\omega_W)\), then \(\tau/\sigma\)
pulls back to a meromorphic function on projective \(Z\), hence to a rational function in \(\mathbb C(x,y)\).
On all of the source plane it is holomorphic, so it is a polynomial \(a\).
The stipulated identification of the extended valuation with the source divisor now gives
\(\operatorname{ord}_C(\tau)=\operatorname{ord}_E(a)-1<0\), impossible for a regular dualizing section at a generic smooth point.
Therefore \(H^0(W,\omega_W)=0\). Normal surfaces are Cohen--Macaulay, so compact analytic duality gives \(H^2(W,\mathcal O_W)=0\).
Also \(H^1(Z,\mathcal O_Z)=0\). Since \(r_*\mathcal O_Z=\mathcal O_W\), the low-degree Leray sequence
kills \(H^0(W,R^1r_*\mathcal O_Z)\). This coherent sheaf has finite support and therefore vanishes.
Thus \(W\) has rational singularities. This does not infer projectivity of \(W\) or \(Y\).

**3. Boundary genera.** The genuine canonical ideal gives
\(0\to\omega_Y\to\mathcal O_Y\to\mathcal O_B\to0\).
Surface duality implies \(\chi(\omega_Y)=\chi(\mathcal O_Y)\), hence \(\chi(\mathcal O_B)=0\) and \(p_a(B)=1\).
Outside \(C\), the finite map lands in the smooth affine target, where \(\Omega\) is nowhere zero. Thus
\(\operatorname{div}(\sigma)=R-C\) for an effective Weil divisor \(R\) with no \(C\) component.
The prime ideal \(I_C=\mathcal O_W(-C)\) is reflexive, and the integral curve \(C\) is Cohen--Macaulay.
Applying sheaf Hom into \(\omega_W\) to its ideal sequence, reflexive Hom and CM dualizing adjunction give
\[
0\longrightarrow\omega_W\longrightarrow\mathcal O_W(R)\longrightarrow\omega_C\longrightarrow0.
\]
Specifically, \(\mathcal Hom(I_C,\omega_W)=\mathcal O_W(R)\) and \(\mathcal Ext^1(\mathcal O_C,\omega_W)=\omega_C\).
This is valid without assuming that \(C\) is Cartier or that \(W\) is Gorenstein.
The section \(1\) has nonzero image in \(H^0(C,\omega_C)\), since \(H^0(W,\omega_W)=0\).
Curve duality gives \(p_a(C)\ge1\).

**4. The reduced scheme isomorphism.** The finite birational map \(C\to B\) gives an injection
\(\mathcal O_B\to h_*\mathcal O_C\) with a finite-length cokernel \(Q\).
Euler characteristic yields \(p_a(C)=p_a(B)-\operatorname{length}(Q)=1-\operatorname{length}(Q)\).
Consequently \(p_a(C)=1\), \(Q=0\), and the finite map is an isomorphism. This completes the conditional proof.

## Replay and negative controls

Desk-only: no computational experiment, numerical cutoff, random seed, or formal certificate is involved.
The proof checks explicitly isolate the source valuation, the full affine open, the genuine canonical module and the non-Cartier adjunction step.
Dropping those premises is outside the theorem. No control family is substituted for the actual Keller map.

## Limitations and next test

The effective divisor \(R\) may remain nonzero. At singular non-Cartier boundary points, its intersection with \(C\)
cannot simply be treated as a zero of a smooth residue. No vanishing of \(R\), equality \(W=Y\), flatness, log-singularity condition,
or equality of nonreduced pullback ideals is proved. Omitted affine boundary components and the full exceptional-image containment problem remain.
The infinitely singular eigenvaluation case and an all-Keller attachment of the hypotheses also remain open.
The next research test must supply an actual Keller constraint eliminating the omitted boundary or proving descent; the isomorphism alone is insufficient.

## OPENS RAISED

None. This report narrows existing normalization/descent questions without opening a new named test.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `02813e10a1b27b5d379b3f05b3b2bcf72a3e6d6c` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8181`.
- Body SHA-256:
  `27d508b1721b07f4acaef58904958f67b1a9c7bbe077366447b9de884087677c`.
- Frozen basis: `02813e10a1b27b5d379b3f05b3b2bcf72a3e6d6c`.
