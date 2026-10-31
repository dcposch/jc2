# Every nonproper connected component must contain a cycle

Producer: swarmHQ ROOT (configured coordinator gpt-6-astra); independent reviewer: configured gpt-5.6-sol/ultra. Hosted model identities are not independently verified.
Date: 2026-10-31 UTC. Basis: 38e3067ed1ad71c748e0bdca305e3ad2e4fe7ee6.
Evidence tier: MANUAL, conditional on the named inherited foundations. Lifecycle: PROVISIONAL; independent PASS_CONDITIONAL. Novelty unassessed.

## Statement and scope

Let F:A2_C -> A2_C be a noninvertible polynomial Keller map of geometric degree N>1, with nonempty reduced nonproper-value curve D. Under the retained actual-normalization package and named classical foundations, no connected component of D is contractible. Thus
    b1(D) >= b0(D),    chi_c(D) <= 0.
Here a connected component is a whole disjoint connected union of irreducible curves. A contractible irreducible curve inside a connected cyclic union is not excluded. The remaining cyclic configurations and JC2 are unresolved.

## Dependencies and prior work

The argument uses the [all-Keller sheet budget](all-keller-sheet-budget-swarmHQ-root-astra-sol56-20261026T005000Z.md) and the [reviewed whole-curve exclusion](contractible-nonproper-curve-swarmHQ-root-sol56-20261031T1245Z.md), including that theorem's [zero-slack input](zero-slack-immersion-swarmHQ-root-sol56-20261031T103000Z.md). Named classical foundations are affine-curve normalization and Euler integration, Lin-Zaidenberg, Abhyankar-Moh, and the Keller injective-on-line theorem. Their source proofs are not newly audited here.
The [independent review](contractible-component-localization-review-sol56-20261031T1410Z.md) checks the localized identity, positivity of the other components' weights, both inverse-curve alternatives, and the graph conclusion. The [original candidate](../box/nonproper-component-euler-bound-swarmHQ-20261031T1425Z/CANDIDATE.md) is retained unchanged. An older rank-four disconnected-acyclic comparison is narrower than the stated all-degree component localization; selected records do not establish novelty.

## Argument

The following mathematical excerpt is byte-identical to the reviewed candidate; its conditional proposal is now independently reviewed at the scope above.

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

## Replay and negative controls

Desk-only proof; no CAS or finite-case experiment supports the all-degree statement. The key scope check is that one partitions a single deficit N-1: no independent N-1 budget is assigned to each target component. The smooth-line argument uses target unibranchness in addition to degree one on normalizations.
The [evidence README](../box/nonproper-component-euler-bound-swarmHQ-20261031T1425Z/README.md) supplies checksums and replay commands. Exact producer and reviewer bytes are preserved. Two failed unsealed reviewer output-formatting attempts occurred before file open; all input hashes remained unchanged. No separate independent review of this presentation wrapper is claimed.

## Limitations and next test

This excludes contractible connected components, not arbitrary individual irreducible components, all cyclic curves, or nonproperness itself. The remaining global polynomial constraint must address configurations with at least one cycle in every connected component. The named imported foundations and the lack of a novelty assessment remain explicit.

## OPENS RAISED

None. The remaining cyclic-configuration gap is not a newly admitted open claim.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `38e3067ed1ad71c748e0bdca305e3ad2e4fe7ee6` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8089`.
- Body SHA-256:
  `52f0afa364d0d74552250dfcb616e177b924e246c0bbedb9d0f519207d0b05fc`.
- Frozen basis: `38e3067ed1ad71c748e0bdca305e3ad2e4fe7ee6`.
