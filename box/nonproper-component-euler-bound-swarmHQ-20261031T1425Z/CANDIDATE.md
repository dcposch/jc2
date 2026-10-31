# Localizing the sheet deficit to connected nonproper components

Status: INTERNAL / MANUAL / UNREVIEWED candidate. Not a proof of JC2; novelty unassessed.
Producer: swarmHQ ROOT. Date: 2026-10-31 UTC. Frozen HQ basis: 5250fb5723df15d713966db90ac5e86ec26087b6.
Public input basis: 38e3067ed1ad71c748e0bdca305e3ad2e4fe7ee6.

## Proposed conclusion and scope
Let F:U=A2_C -> Y=A2_C be a noninvertible polynomial Keller map of geometric degree N>1, with nonempty reduced nonproper-value curve D. Under the retained actual-normalization package and named foundations below, no CONNECTED COMPONENT of D is contractible. Consequently every connected component has first Betti number at least one, b1(D)>=b0(D), and chi(D)<=0.
A connected component here is a whole disjoint connected union of irreducible curves. This does not exclude a contractible individual irreducible curve lying inside a connected cyclic union. Noncontractible configurations and JC2 remain open.

## Inputs actually used
Use the reviewed all-Keller sheet budget and contractible WHOLE nonproper-curve exclusion at the public basis above:
- ../jc2/xmodel/all-keller-sheet-budget-swarmHQ-root-astra-sol56-20261026T005000Z.md (whole SHA256 5c4baaef7e6d5d1ab6edc68a1eb249b02732f001f5846e294557ee701eee5907).
- ../jc2/xmodel/contractible-nonproper-curve-swarmHQ-root-sol56-20261031T1245Z.md (whole SHA256 8147ff9b62fe2c8b71b0e74c0c39737ead5930977831c028b93839043767b70a).
Their classical foundations remain conditional/inherited: affine-curve normalization and Euler integration; Lin-Zaidenberg for a contractible singular irreducible plane curve; Abhyankar-Moh for an embedded smooth A1; and the Keller injective-on-line theorem. No new source proof is audited here. The connected WHOLE-D case uses the already reviewed theorem, including its zero-slack input.
Write h:X->Y for the finite flat normalization, with WHOLE U open in X. Its omitted E_i are disjoint, have Euler characteristic one, and have A1 normalizations; each image D_j has A1 normalization. Write r_i for transverse degree, delta_i for the polynomial normalization-map degree, t_x for local tangential degree, m_x for local finite-fibre length, and s_x=m_x-r_i*t_x>=0. The retained identities are sum_x(t_x-1)=delta_i-1 and N-1=sum_i r_i*delta_i+sum_x s_x, with finite excess support.

## 1. The localized identity
Let D_alpha run through the disjoint connected components of D, put Z_alpha=F^{-1}(D_alpha), reduced, and let I_alpha consist of omitted curves whose images lie in D_alpha. Define
    W_alpha = sum_{i in I_alpha} r_i*delta_i + sum_{i in I_alpha} sum_{x in E_i} s_x.
Then W_alpha is a positive integer and sum_alpha W_alpha=N-1. Positivity uses that each nonempty nonproper component is the image of at least one omitted E_i. We do NOT assert a separate N-1 budget for each component.
For every y in D_alpha, finite flatness and etaleness at all retained source points give
    #F^{-1}(y) = N - sum_{x in (X\U) over y} m_x.
Integrate this constructible function with compactly supported Euler characteristic over D_alpha. Because the entire E_i lies above exactly one D_alpha and chi(E_i)=1,
    integral_{E_i} m_x dchi = r_i + sum_x(m_x-r_i)
                            = r_i*delta_i + sum_x s_x.
Thus the genuinely localized identity is
    chi(Z_alpha) = N*chi(D_alpha) - W_alpha.                         (L)
This is restriction of the single finite-fibre identity followed by Euler integration, not multiplication of a nonproper covering degree and not addition of independent per-image sheet budgets.

## 2. A contractible component in a disconnected D is impossible
Assume D_alpha is contractible and D has at least one other connected component. Every other W_beta>=1, so W_alpha<=N-2. Formula (L) gives chi(Z_alpha)>=2.
For every irreducible affine curve H, chi(H)=2-2g-p-b<=1, with p>=1 punctures in its smooth projective normalization and b>=0 finite branch-identification deficit. Euler characteristic of a reduced union is the sum over its irreducible components minus nonnegative gluing deficits. Hence some irreducible component Gamma of Z_alpha has positive Euler characteristic; it has normalization A1, is unibranch everywhere, and is topologically contractible.
Contractibility of D_alpha implies every irreducible component D_j within it is unibranch: its A1 normalizations have a finite gluing graph, and a self-identification creates a cycle that subsequent gluing cannot erase.
If Gamma is smooth, rectify it to a line by a source polynomial automorphism. Its map to the normalization A1 of its image D_j is a nonconstant polynomial a(t), since F is quasi-finite. If a'(t)=0, the derivative of F along that source line vanishes; this contradicts etaleness. Thus a has degree one. Since A1->D_j is bijective by unibranchness, F is injective on the actual source line. The inherited injective-on-line theorem makes F invertible, a contradiction.
If Gamma is singular, the inherited Lin-Zaidenberg theorem rectifies it to x^p-y^q=0 with p,q>1 coprime. Section 3 of the reviewed whole-D proof shows that every irreducible closed affine curve H disjoint from Gamma has negative Euler characteristic of its smooth affine normalization, hence chi(H)<0.
Let Z_0 be the connected component of Z_alpha containing Gamma. Every connected reduced affine curve has Euler characteristic at most one. Every other connected component W of Z_alpha is a union of irreducible closed curves disjoint from Gamma, so chi(W)<0; finite gluing only decreases Euler characteristic. Therefore chi(Z_alpha)<=1, contradicting chi(Z_alpha)>=2.
Both smooth and singular Gamma are impossible. No contractible connected component can coexist with another connected component of D.

## 3. The connected case and the sign conclusion
If D itself is connected and contractible, the retained reviewed whole-D theorem already excludes it. Together with Section 2 this excludes every contractible connected component of a nonempty D.
Since all irreducible D_j have A1 normalizations, each connected D_alpha is homotopy equivalent to a finite connected gluing graph. Hence chi(D_alpha)=1-b1(D_alpha), and b1=0 is equivalent to contractibility. The exclusion implies b1(D_alpha)>=1 for every alpha. Summing gives b1(D)>=b0(D) and chi(D)<=0.

## Review targets and limitations
The independent reviewer should attack (L), positivity of the OTHER component weights, use of compactly supported Euler characteristic for the nonproper restriction, and the preservation of target unibranchness in the smooth-Gamma step. The singular-Gamma step invokes exactly the already reviewed cusp-disjointness lemma, with no extension to a nonclosed residual curve.
Selected historical routing recovered a rank-four disconnected-acyclic obstruction (old Opus review lines322-361), not an all-degree novelty certificate. That old report was read only for this scope; its proof is not imported. This candidate depends on the explicit new localization, and does not retroactively strengthen sealed older claims.
No CAS, source query, new paid/native lane, or public promotion is part of this ROOT candidate. It remains unreviewed until a separately admitted hostile review completes.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7205`.
- Body SHA-256:
  `815c4afd130169796792440bd94221770ced405c9a74a3e16b45b2368b60895a`.
- Frozen basis: `5250fb5723df15d713966db90ac5e86ec26087b6`.
