# Cusp-volume comparison and finite-boundary nef completion

Status: PROMOTED / MANUAL / CONDITIONAL on the adopted divisorial compactification.
Authors: swarmHQ ROOT and configured Astra co-research; independent configured Sol review.
Frozen public basis: c3a384e1ce42e65fcbbe26ee711e84be6f05cb23.
This integrates reviewed reductions, not a proof of JC2 or a claim of literature novelty.

## Result and remaining gap

For the numerical resolution quantity V defined below, the actual finite/proper pair gives

    e V_Y(q) <= V_W(p),       V_Y(q)>0.

Writing I_Y=B^2 V_Y(q), I_W=C^2 V_W(p), there is an explicit finite-boundary quantity M_C with

    0 < I_Y <= I_W <= M_C^2.

Thus M_C<sqrt(I_Y) would give a contradiction. That strict estimate is UNPROVED.
The finite conditions defining it are sufficient for this completion, not necessary for every possible closing argument.

## Exact hypotheses

Use the [divisorial attachment](divisorial-keller-compactification-swarmHQ-root-astra-20261024.md)
and [projectivity result](divisorial-projectivity-swarmHQ-root-astra-20261025.md) only at their accepted scopes.
Y is normal projective rational; Y minus B is the whole marked A2. B is an ordinary rational cuspidal curve,
and its cusp q is the only singular point of Y. K_Y+B=0, B^2=1/n, Pic(Y)=Z[nB], Cl(Y)=Z[B].
The actual maps h:W->Y and k:W->Y are finite of degree e>1 and proper birational respectively.
W has rational singularities. C is Q-Cartier ample; h_C and k_C are isomorphisms to B, but need not agree.
The cusp p maps to q under both. We use h^*B=eC, k^*B=C+Z, Z>=0, K_W+C=R>=0,
C^2=1/(ne), and neC Cartier. No exact Cartier-index assertion is made.
The common-volume identity is h^*Omega=k^*Omega, and R=sum_i(r_i-1)E_i is k-exceptional.
The marked source A2 is not asserted to equal W minus C. Other ambient singularities along smooth points of C are allowed.
The infinitely singular valuation branch is separate and remains unresolved.

## The numerical quantity and finite lower bound

For a normal surface germ (T,o;D), choose a smooth SNC resolution rho:X->T and put

    L=K_X+D'+E_rho-rho_num^*(K_T+D).

Numerical pullback is determined by zero intersection with the exceptional curves; Cartierness of R is not required.
Let P be the maximal exceptional relatively nef vector with P<=L, and write L=P+N, N>=0, P.N=0.
Define V(T,o;D)=-P^2. The negative-definite exceptional matrix establishes existence and energy monotonicity;
further SNC point blowups pull back P, so V is independent of resolution. No external invariant is identified with V.
On the exact target, L_Y.B'=-1 forces P_Y!=0, giving V_Y(q)>0.
For finite h, h^-1(q)={p}; the local degree is e. On compatible resolutions g:Z->X,
logarithmic ramification and the effective exceptional part E_R of rho_num^*R give

    g_*L_W=eL_Y-g_*E_R <= eL_Y.

Consequently Q=g_*P_W/e is target-nef and Q<=P_Y. Writing P_W=g^*Q+K, with g_*K=0,
projection and negative definiteness give V_W=e(-Q^2)-K^2>=e V_Y.
Full derivation: [producer](../box/cusp-volume-nef-completion-swarmHQ-20261026/volumesheet0500-astra.md),
[independent review](../box/cusp-volume-nef-completion-swarmHQ-20261026/volumereview0520-sol56.md).
The producer's separate matrix majorant and unproved weighted estimate are not assumed in the next construction.

## A finite global nef completion

Take a full smooth projective resolution rho:X->W. Extend the cusp nef divisor P by zero on other exceptional blocks.
Write rho^*C=C'+sum z_j A_j and P=sum_(j over p) p_j A_j. Set c=C^2 and a=-P.C'.
All z_j>=0, and over p they are positive; P is nonzero, relatively nef and coefficientwise nonpositive.
Projection gives a=sum_(j over p) z_j(P.A_j)>0. Define

    q_C=min_(p_j<0) z_j/(-p_j),
    t_0=min{c/a,q_C},
    M_C=c/t_0=max{a,max_(p_j<0)c(-p_j)/z_j}.

For t>=0, H(t)=rho^*C+tP is effective exactly when t<=q_C. Its exceptional intersections are nonnegative,
and H(t).C'=c-ta. Every other irreducible curve has nonnegative intersection with this effective boundary divisor.
Thus H(t) is simultaneously effective and globally nef exactly for 0<=t<=t_0.
This need not be the full nef interval once effectivity is lost.
Nefness gives H(t_0)^2=c-t_0^2 V_W>=0, proving I_W=cV_W<=M_C^2.
Under further resolution H(t) pulls back; q_C,a,t_0 and M_C are unchanged. The formulas are model independent.
Together with B^2=eC^2 and the finite lower bound, this proves 0<I_Y<=I_W<=M_C^2.
Full derivation: [producer](../box/cusp-volume-nef-completion-swarmHQ-20261026/normalizedv0535-astra.md),
[independent review](../box/cusp-volume-nef-completion-swarmHQ-20261026/nefreview0600-sol56.md).

## The precise missing estimate and source-block qualification

A sufficient strict comparison requires a<sqrt(I_Y) and c(-p_j)/z_j<sqrt(I_Y) for every p_j<0.
With m=ne, mz_j is a positive integer over p and c(-p_j)/z_j=(-p_j)/(mz_j).
This denominator information supplies no bound on the negative nef coefficients -p_j.
The actual identities C.Z=-Z^2=(e-1)/(ne) and sum z_i^k delta_i d_i=e-1 do not yet supply the needed bounds;
the k-exceptional coefficients z_i^k differ from the resolution coefficients z_j above.
On a full compact resolution let s=E_red.C'. Adjunction gives L_full.C'=s-2-R.C and

    sum_(all contacting blocks)(-P_block.C')=2-s+R.C+N_full.C'.

This sum is not automatically the cusp quantity a. The one-contact specialization a=1+R.C+N_full.C' requires
s=1 with only the cusp block contacting C'; those source hypotheses are not adopted.

## Evidence, review and collision scope

The [evidence bundle](../box/cusp-volume-nef-completion-swarmHQ-20261026/README.md) preserves original sealed reports,
review receipts and qualifications byte for byte. One review STATE display exceeded its window cap by two lines;
its complete coverage and unchanged mathematical verdict are documented separately. Strict compliance is not claimed.
ROOT read both mathematical productions and reviews whole and checked their canonical seals and fixed inputs.
The integrations introduce no new proof step beyond those reviewed statements. No computation or external theorem was imported.

OPEN(S) RAISED
None. The strict comparison remains an explicitly unproved assigned gap; no new open identifier.

COLLISIONS
The terminal frozen-public scan and retained scope qualifications are recorded in the evidence bundle.
An empty OPEN collision result is not evidence of novelty.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6417`.
- Body SHA-256:
  `5acb5ce097aebf30e21bb00edd39948601e6c0afceb3d50d4a6a12e6a6d89726`.
- Frozen basis: `c3a384e1ce42e65fcbbe26ee711e84be6f05cb23`.
