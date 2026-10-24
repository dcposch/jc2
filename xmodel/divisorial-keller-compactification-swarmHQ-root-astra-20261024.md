# The compact boundary package attaches to the divisorial Keller branch

Producer: swarmHQ coordinator and Astra co-researcher (requested gpt-6-astra; hosted identity unmeasured).
Date: 2026-10-24 23:49:45 UTC
Basis: `6308026911a151c043d10ae6caf752588f08a7b0`.
Evidence tier: MANUAL, conditional on the stated dynamical inputs and named standard dependencies.
Lifecycle: PRODUCER-CHECKED / UNPROMOTED; exact public artifact review pending.

## Statement and scope

Let \(F:\mathbb A^2\to\mathbb A^2\) be a polynomial map with \(\det DF=1\) and generic degree \(N>1\).
Assume the adopted dynamical inputs: \(\lambda=\lambda_1(F)\ge N\) and an eigenvaluation
\(\nu_*\in V_1\), with \(F_*\nu_*=\lambda\nu_*\) and \(A(\nu_*)=0\).
Assume that this eigenvaluation is **divisorial**. These inputs are not re-proved here.
Then \(\alpha(\nu_*)>0\), \(\lambda=N\), and the three earlier compact boundary results
apply to the actual iterates \(F^j\), on one fixed target compactification, for every \(j\ge1\):

- There is a smooth projective rational compactification \(X\) of the given \(U=\mathbb A^2\)
  and a proper birational analytic contraction \(\rho:X\to Y\), with \(Y\) normal compact,
  \(Y\setminus B=U\), and genuine dualizing sheaf \(\omega_Y\simeq I_B\).
- The reduced irreducible boundary \(B\) is an intrinsically ordinary cuspidal rational curve.
  The surface \(Y\) has rational singularities and is singular exactly at that cusp.
- Resolving each actual iterate and taking the finite Stein factor gives
  \(Z_j\xrightarrow{r_j}W_j\xrightarrow{h_j}Y\), with \(\deg h_j=N^j\).
  The normal compact surface \(W_j\) has rational singularities. Its reduced inverse image
  \(C_j=(h_j^{-1}B)_{\mathrm{red}}\) maps isomorphically to \(B\), with boundary ramification \(N^j\).
- There is a proper birational source projection \(k_j:W_j\to Y\), identity on source \(U\).
  The standard meromorphic volume satisfies \(h_j^*\Omega=k_j^*\Omega\), with divisor
  \(R_j-C_j\), where \(R_j\ge0\) is supported on \(k_j\)-exceptional curves.

This is a divisorial-branch corollary. It neither proves that every relevant eigenvaluation
is divisorial nor makes \(F\) proper. In particular, \(W_j\setminus C_j=U\) is **not** assumed or concluded.

## Dependencies and prior work

The three MANUAL conditional inputs are the
[finite-factor theorem](finite-stein-factor-boundary-swarmHQ-root-20261024T202659Z.md),
[cusp and source-projection theorem](cuspidal-boundary-index-swarmHQ-root-astra-20261024T213422Z.md), and
[singular ambient cusp theorem](singular-ambient-cusp-local-index-swarmHQ-root-astra-20261024T223151Z.md).
Their review qualifications and local-versus-compact distinctions remain in force.
The present contribution checks their hypotheses for the actual divisorial branch;
it is not a re-audit of their proofs or a claim of historical novelty.

The adopted dynamical inputs are recorded in the
[dynamical-degree argument](keller-dynamical-degree-swarmHQ-root-20260914.md) and
[eigenvaluation reduction](keller-dynamical-minimization-swarmHQ-root-20260914.md),
with the [earlier source-scope review](dynamical-minimization-gate-fable51-20260914.md).
We use the stated scope of Favre--Jonsson, *Dynamical compactifications of C^2*,
[Annals of Mathematics 173 (2011)](https://annals.math.princeton.edu/wp-content/uploads/annals-v173-n1-p06-p.pdf):
valuation definitions, the divisorial-end alternatives after Proposition 2.6,
the non-end assertion in Section 4.1, and the dual-class identity in Appendix A.2.
These are named imports, not a certification of unread source proofs.
Other named dependencies are Hodge index, Grauert analytic contraction, normal/reflexive
surface duality, resolution, analytic Stein factorization, and the valuation degree inequality.

## Argument

**1. Positive skewness.** Since \(N>1\) and \(\lambda\ge N\), the small-topological-degree
regime \(N<\lambda^2\) holds. At the cited Favre--Jonsson scope, a divisorial eigenvaluation
which is not an end has \(\alpha>0>A\). The divisorial-end alternatives are
\(\alpha=0>A\) and \(\alpha>0=A\). Hence \(A=0\) forces \(\alpha>0\).
No separate zero-skewness divisorial case remains under these inputs.

**2. Contracting the complement.** Represent \(\nu_*=b_E^{-1}\operatorname{ord}_E\)
on a smooth surface \(X\) obtained by finitely many point blowups of \(\mathbb P^2\) at infinity.
Its boundary is an SNC tree of rational curves. Write \(X\setminus U=E\cup D\),
where \(D\) contains all other boundary primes and may be disconnected.
Boundary classes form a basis of \(\operatorname{NS}(X)_{\mathbb R}\): successive blowups
replace the line and exceptional basis by strict transforms through a triangular change of basis.
Let \(L_E\cdot E=1\) and \(L_E\cdot D_i=0\). Appendix A.2 gives
\(L_E=Z_{\operatorname{ord}_E}\) and \(L_E^2=b_E^2\alpha(\nu_*)>0\).
Hodge index makes \(L_E^\perp\) negative definite, so the entire intersection matrix of \(D\)
is negative definite. This uses neither a leaf model nor ampleness of \(L_E\).
Contract each connected component of \(D\) by Grauert's analytic theorem.
Each component meets \(E\) once because the boundary graph is a tree; therefore the contraction
identifies no two points of \(E\). With \(B=\rho(E)_{\mathrm{red}}\),
\(E\to B\) is its finite bijective normalization and a topological homeomorphism.
Moreover \(\rho^{-1}B=E\cup D\), so \(Y\setminus B\) is the whole given plane.
No algebraicity or projectivity of \(Y\) is required.

**3. The genuine canonical ideal.** The thinness identity
\(A(\nu_E)=(1+\operatorname{ord}_E(dx\wedge dy))/b_E\) gives order \(-1\) on \(E\).
The standard volume descends meromorphically through \(\rho\). Its sole codimension-one
boundary divisor on \(Y\) is \(-B\), and it is nowhere vanishing on \(U\).
Normal analytic surfaces are Cohen--Macaulay and their dualizing sheaves are reflexive.
Codimension-one identification and reflexive extension give
\(\omega_Y\simeq\mathcal O_Y(-B)=I_B\). We do not substitute \(\rho_*\omega_X\)
for \(\omega_Y\), or assume that \(B\) is Cartier or \(Y\) Gorenstein.
The projective rational source supplies \(H^1(X,\mathcal O_X)=0\).

**4. Unique boundary extension.** The eigenrelation says
\(\operatorname{ord}_E(a\circ F)=\lambda\operatorname{ord}_E(a)\) for target rational functions.
Thus the source valuation extends the target valuation with ramification \(e=\lambda\).
The DVR fundamental inequality gives \(ef\le N\), with the sum over all extensions at most \(N\).
Together with \(\lambda\ge N\), this forces \(e=\lambda=N\), residue degree \(f=1\),
and uniqueness of that extension, including extensions represented on higher resolutions.
For \(F^j\) the same argument gives \(e=N^j\), on the same \(X,E,Y\).
It says nothing about source boundary divisors whose images lie in the affine target.

**5. Actual finite factors.** Resolve \(F^j:X\dashrightarrow X\) by
\(\pi_j:Z_j\to X\) and \(G_j:Z_j\to X\). Since \(F^j\) is regular on all source \(U\),
the resolution centers may all lie outside \(U\); \(Z_j\) is smooth projective rational.
Take the analytic Stein factorization of \(H_j=\rho G_j\).
These are exactly the hypotheses of the three cited conditional results, which give the conclusions above.
Their source projection descends \(\rho\pi_j\), not \(\rho G_j\): the source divisor \(E\)
is not \(r_j\)-exceptional, while all other boundary curves are contracted by \(\rho\pi_j\).
Thus \(\rho\pi_j\) is constant on connected \(r_j\)-fibres and descends to \(k_j\).
The restriction \(r_j|_U\) is an open immersion; this does not identify its entire target complement with \(U\).

## Replay, limitations and next test

Desk-only. No computation, new source fetch, classification, or local family is used.
The actual \(k_j\) is proper birational; properness of the original polynomial \(F\) remains unproved.
No \(R_j=0\), \(k_j\) isomorphism, target-map descent, or finite self-germ follows.
Omitted boundary over affine target points and the infinitely singular eigenvaluation branch remain open.
The earlier inequality \(e\le5m\) requires a target smooth at its cusp, which this compact setting excludes.
Exceptional images lie at one boundary point each; a cusp location is not asserted for every image.
An earlier hostile-review objection imposed the absent full-preimage premise and was retracted
following an exact-hypothesis correction. The corrected mathematical review is not blind;
its correction and display/custody qualifications are retained in the final review and audit.
The next useful mathematical input must constrain the actual global map at the remaining gaps;
publication of this corollary alone authorizes no new local-model or classification claim.

## OPENS RAISED

None. The existing descent, omitted-boundary, and infinitely singular gaps are retained.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `6308026911a151c043d10ae6caf752588f08a7b0` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9000`.
- Body SHA-256:
  `f7e9a0cd5b84a4d1bb5b6cf8d6aa076d4a720f35488128494b8c4cb75e2bd8a4`.
- Frozen basis: `6308026911a151c043d10ae6caf752588f08a7b0`.
