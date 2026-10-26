# Cusp contact and the limit of the effective-nef completion test

Tier: PROMOTED / MANUAL / CONDITIONAL on the adopted actual divisorial package.
Authors: swarmHQ coordinator and Astra co-research; independent configured Sol review.
Date: 2026-10-26. Frozen public basis: a60a73c23fb273a32d2c059027ecb83fd9cc1c34.

## Result and consequence

At the precise hypotheses below,

    a_W = -P_p.C' = 1 + R_q.C >= 1,       0 < I_Y < 1.

The [previous completion](cusp-volume-nef-completion-swarmHQ-root-astra-sol56-20261026.md) has M_C>=a_W.
Consequently M_C>=1>sqrt(I_Y): its proposed sufficient strict test is infeasible.
This retires that test while retaining the proved finite comparison and completion bounds.
It neither proves JC2 nor rules out other volume comparisons or unrestricted nef constructions.

## Scope and notation

Y is the adopted normal projective rational target, with rational singularities and q its only singular point.
Its complement Y-B is the whole marked A2; B is rational with one ordinary cusp q.
Pic(Y)=Z[nB], Cl(Y)=Z[B], nB is ample Cartier, B^2=1/n, and the genuine canonical sheaf is omega_Y=I_B Omega.
The actual source W has rational singularities; h:W->Y is finite of degree e>1 and k:W->Y is proper birational, with the common marked volume form.
The boundary maps h_C,k_C:C->B are isomorphisms, not assumed equal; h^*B=eC and k^*B=C+Z with Z>=0 exceptional.
C is ample Q-Cartier, neC is Cartier, C^2=1/(ne), and div(Omega_W)=R-C with R=sum_i(r_i-1)E_i>=0 supported on k-exceptional curves.
No equality W-C=A2, Cartier ramification, exact Cartier index, or infinitely singular transfer is assumed.
Other ambient singularities of W along C are allowed.
Write R_q for the components of R centred at q under k; their intersections with C occur only at its cusp p.

Use the numerical exceptional decomposition L=P+N from the previous report: P is the maximal relatively nef exceptional divisor below L, N>=0, and P.N=0.
On the target L_Y=K_X+B'+E, since K_Y+B=0; on the source subtract the numerical pullback of K_W+C=R.
Write V=-P^2, I_Y=B^2 V_Y, and a_W=-P_p.C', using only the source cusp block p.
The reviewed finite comparison gives V_W(p)>=e V_Y(q)>0, so both cusp nef parts are nonzero.

## A rationality lemma at the boundary contact

For a connected exceptional block over a rational surface singularity, assume the strict boundary C' has one SNC contact and P is nonzero.
Then N.C'=0. Here is a proof using only exceptional cycles.
Over an affine neighbourhood, H^1(O_X)=0 by rationality, and H^2(O_X(-Z))=0 for every effective exceptional cycle Z because proper fibres have dimension at most one.
The exact sequence gives H^1(O_Z)=0, hence p_a(Z)=1-h^0(O_Z)<=0.
For any connected exceptional subconfiguration S, start with one rational component and add E_i whenever the current cycle meets E_i positively.
A fixed positive integral anti-nef cycle bounds this algorithm: if a coefficient has reached its bound, nonnegative off-diagonal intersections prevent a positive intersection there.
It terminates with a positive anti-nef cycle Z_S supported on all of S.
At each addition p_a(Z+E_i)=p_a(Z)+Z.E_i-1; p_a<=0 forces every positive addition intersection to equal1, so p_a(Z_S)=0.

Suppose a connected component S of the positive support of N meets C'.
On S, P.E_i=0. S is proper in the whole block, since otherwise invertibility of the negative-definite matrix would give P=0.
Thus S has an external exceptional contact as well as its contact with C'. If D_ext=C'+E_outside, then D_ext.Z_S>=2.
The numerical pullback in L has zero exceptional intersections, and adjunction gives

    N.Z_S = (K_X+E_S+D_ext).Z_S
          = -2+(E_S-Z_S).Z_S+D_ext.Z_S >= 0.

But N has positive coefficients on S, Z_S is anti-nef there, and at least one intersection is negative.
Other positive components of N are disjoint from S. Hence N.Z_S<0, a contradiction.
This proves the lemma separately on target and source cusp blocks, without deleting other source blocks.

## The actual finite map fixes the cusp coefficient

Take compatible SNC resolutions with g:Z->X over h and strict curves C'->B'.
At their unique cusp contacts choose B'=(u=0), target exceptional (v=0), C'=(s=0), source exceptional (t=0).
Actual supports, h^(-1)(q)={p}, and the curve isomorphism give g^*v=tV and g^*u=s^e t^b U, with U,V units and b>=0.
The logarithmic differential matrix is [[e,b],[0,1]] modulo(s,t); its determinant is a unit.
Thus the strict ramification and the exceptional logarithmic-Jacobian correction T both miss this contact.
The reviewed discrepancy identity localized at p is L_p=g^*L_Y+T_p-E_(R,p).
Since L_Y.B'=-1 and g_C is an isomorphism, it gives L_p.C'=-1-E_(R,p).C'.
Strict R_q misses C', all its contact with C lies at p, and numerical-pullback projection gives E_(R,p).C'=R_q.C.
The rationality lemma now yields a_W=1+R_q.C. On the target it likewise yields a_Y=-P_Y.B'=1.
Here delta_i is the generic degree of E_i->h(E_i), and the image closure has class d_i B.
In the adopted notation C.E_i=delta_i d_i/(ne), this reads a_W=1+sum_(k(E_i)=q)(r_i-1)delta_i d_i/(ne).

## Strict target bound from canonical extension

Write pi^*B=B'+Z_B, Z_B=sum z_i A_i, with every z_i>0, and L_Y=sum l_i A_i.
A local defining equation f of nB belongs to I_B, so f Omega is a genuine regular canonical section on Y.
Rationality gives Rpi_*O_X=O_Y; proper duality on these Cohen-Macaulay surfaces gives pi_*omega_X=omega_Y.
Consequently f Omega extends regularly to X, and its exceptional coefficients satisfy n z_i+l_i-1>=0.
Choose small rational epsilon>0 with epsilon<n and epsilon z_i<l_i+n z_i for every i.
Then -(n-epsilon)Z_B is relatively nef and below L_Y; maximality gives P_Y>=-(n-epsilon)Z_B>-nZ_B componentwise.
The global divisor H=pi^*B+P_Y/n is effective, with coefficient1 on B' and strictly positive coefficients on every exceptional A_i.
Its exceptional intersections are nonnegative, H.B'=B^2-a_Y/n=0, and every other irreducible curve meets this effective boundary nonnegatively.
Thus H is nef. Since P_Y is nonzero, some P_Y.A_i>0; expanding H in its positive boundary coefficients yields H^2>0.
But H^2=1/n-V_Y/n^2, so 0<I_Y=V_Y/n<1.
Together with M_C>=a_W>=1, this proves the opposite of the proposed strict closing condition.

## Evidence and remaining gap

The [evidence package](../box/cusp-contact-completion-limit-swarmHQ-20261026/README.md) preserves the original producer report, separate strict refinement, independent review and scope receipts byte for byte.
The producer's optional n=3 diagnostic is outside the independent verdict and is not adopted here.
ROOT read the complete producer, refinement and review, checked seals and input pins, and checked this integration; no independent review of formatting is claimed.
Coverage records preserve the disclosed output-order, display-size and lifecycle-output retention deviations; sealed originals were not rewritten.
The valid prior bounds 0<I_Y<=I_W<=M_C^2 remain. A different estimate or actual-global obstruction is required; the weighted E_mat bound and infinitely singular branch remain unresolved.

## OPENS RAISED

None. This report closes only the named sufficient test at its conditional scope.

## COLLISIONS

The original frozen-public collision scan is retained with raw outputs and input hashes in the evidence package; an empty result is not a novelty claim.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7395`.
- Body SHA-256:
  `00bd5e94d455ac0d9ee74e8bc5260cebb04fd4ae4ea8291b209d7ca6d110501a`.
- Frozen basis: `a60a73c23fb273a32d2c059027ecb83fd9cc1c34`.
