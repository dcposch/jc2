# CUSPLOG0635 — actual cusp contact and infeasibility of the strict completion test
Producer: freshglobal1740_astra, configured gpt-6-astra; primary co-research, not independent review.
Date: 2026-10-26 UTC. Launch/report basis: ce05682d614f94a682c422b0cb1090114e294608.
Lifecycle: PRODUCER-CHECKED / INTERNAL / UNPROMOTED. Verdict: CUSP_IDENTITY / SPECIFIC_COMPLETION_INFEASIBLE.

## Outcome and scope
At the adopted actual divisorial finite-h/proper-k scope, the cusp-only coefficient satisfies
  a_W=-P_p.C'=1+R_q.C
      =1+sum_(k(E_i)=q)(r_i-1)delta_i d_i/(ne)>=1.          (1)
Here R_q is the part of R centred at q under k. Other ambient source singularities along C are allowed; their blocks are not included in P_p or silently discarded from global adjunction.
The same rationality argument on the target gives a_Y=1, and a canonical-form extension gives
  0<I_Y=B^2 V_Y(q)<=1.                                   (2)
Consequently the published completion quantity satisfies M_C>=a_W>=1>=sqrt(I_Y). Thus its proposed strict separation M_C<sqrt(I_Y) is impossible at these hypotheses. This is a feasibility decision about THIS sufficient completion test. It is not a JC2 proof or counterexample and does not exclude other normalized-volume comparisons, use of the larger unrestricted nef interval, or other actual-global arguments.
Retain precisely the published package: Y is normal projective rational, Y\B is the whole marked A2, B is ordinary rational cuspidal, q is the only singular point of Y, and K_Y+B=0. W has rational singularities; h:W->Y is finite of degree e, k:W->Y proper birational; C is Q-Cartier ample and h_C,k_C are isomorphisms onto B, not necessarily the same map.
We use h^*B=eC, k^*B=C+Z, Z>=0, common volume, K_W+C=R=sum_i(r_i-1)E_i>=0, B^2=1/n, C^2=1/(ne), and nB,neC Cartier. The cusp p of C maps to q under both curve isomorphisms. The marked source A2 is not asserted to be W\C. No infinitely singular transfer occurs.
The numerical invariant, its model independence, finite lower bound, and definition of M_C are dependencies from the newly read public synthesis. They are not re-audited here. New claims below remain co-research until any independent review.

## Actual coordinates at the resolved cusp contact
Choose compatible smooth SNC resolutions rho:Z->W and pi:X->Y with g:Z->X, pi g=h rho. Such a common resolution induces an isomorphism C'->B' between normalizations. Because the intrinsic cusps are unibranch, C' meets the reduced rho-exceptional fibre over p at one point x, and B' meets the pi-exceptional fibre over q at one point y=g(x), each transversely after SNC resolution.
At y choose regular parameters u,v with B'=(u=0) and the sole exceptional component through y equal to (v=0). At x choose s,t with C'=(s=0) and the sole source exceptional component through x equal to (t=0). All other source blocks are away from this germ.
The source exceptional component through x maps into pi^(-1)(q). Locally the latter has support v=0; hence t divides g^*v. There are no other local divisor components in its zero set: h^(-1)(q)={p}, and the source exceptional boundary is SNC with a single component at x. Restriction to C' is a uniformizer because g_C is an isomorphism. Therefore its t-order is1 and
  g^*v=t V,     V a unit.
Likewise the zero support of g^*u lies in C' plus source exceptionals, since h^(-1)(B)=C set-theoretically. At x these are just s=0 and t=0. The generic C'-order is e from h^*B=eC, unchanged by resolutions away from the generic boundary point. Thus
  g^*u=s^e t^b U,     U a unit, b>=0.
These factorizations are deduced from the actual map and support, not assumed toroidality or a replacement family. In logarithmic bases ds/s,dt/t and du/u,dv/v the differential matrix reduces modulo(s,t) to [[e,b],[0,1]]. Its determinant is the nonzero constant e in characteristic zero. The logarithmic Jacobian is therefore a unit at x.
In the previously reviewed discrepancy identity write
  L_p=g^*L_Y+T_p-E_(R,p),                                (3)
localized to the rho-exceptional block over p. Here E_(R,p) is the p-supported exceptional part of rho_num^*R; it excludes R_strict. The full logarithmic Jacobian divisor is R_strict plus a g-exceptional divisor T. Strict R components are not g-exceptional because h is finite and maps each of them to a curve. The unit calculation shows that neither strict R nor T meets x. In particular T_p.C'=0.
On the target, L_Y.B'=-1 at the exact q-only-singularity scope. Projection along the isomorphism C'->B' gives (g^*L_Y).C'=-1. Only x meets the source p-block, so (3) yields
  L_p.C'=-1-E_(R,p).C',
  a_W=1+N_p.C'+E_(R,p).C',                              (4)
where L_p=P_p+N_p is the local relative nef decomposition. This is a cusp-only identity; it does not replace the full source formula by a one-contact global assumption.

## Identifying the numerical ramification contribution
Every E_i with k(E_i)=q can meet C only at p, since k_C is an isomorphism; every other k-centred exceptional component misses p. Put R_q=sum_(k(E_i)=q)(r_i-1)E_i. Its intersection with C is therefore entirely at p, and near p it agrees with R.
The strict transform of R_q misses C': all its possible intersections would lie over p at x, excluded by the logarithmic Jacobian calculation. Numerical pullback has zero intersection with rho-exceptional curves. Since C is Q-Cartier, projection consequently gives
  E_(R,p).C'=(rho_num^*R_q).C'=R_q.C.
Other exceptional parts of rho_num^*R_q have no intersection with C'; no Cartierness of R or R_q has been presumed. The numerical pullback's exceptional part is effective by the negative-definite matrix sign, as in the reviewed finite comparison.
Let the closure of h(E_i) have class d_i B in Cl(Y)=Z[B]. Projection through h gives C.E_i=delta_i d_i/(ne). This proves the weighted expression for R_q.C in (1), once N_p.C'=0 is established next.

## Rationality lemma: the negative part misses the strict boundary contact
The following argument applies separately to the target cusp block and to the source cusp block, and does not require contracting or classifying a subconfiguration. Work on a resolution over an affine neighbourhood of a rational surface singularity. For every effective exceptional cycle Z_0, one has H^1(O_(Z_0))=0: rationality gives H^1(O_X)=0, and H^2(O_X(-Z_0))=0 because the proper morphism to the affine base has fibres of dimension at most one. The exact sequence for Z_0 then proves the assertion. Thus p_a(Z_0)=1-h^0(O_(Z_0))<=0.
For a connected exceptional subconfiguration S, construct a positive anti-nef cycle Z_S on S by starting with one reduced component and adding E_i whenever the current cycle has positive intersection with E_i in S. The negative-definite matrix provides a fixed positive integral anti-nef cycle bounding this process. If the current coefficient already equals that bound at i, its intersection at i cannot be positive, because all off-diagonal intersections are nonnegative. Hence additions stay bounded and terminate; connectedness makes the final support all of S.
Every exceptional component is a smooth rational curve. The arithmetic-genus identity for an addition is p_a(Z+E_i)=p_a(Z)+Z.E_i-1. Starting with genus0, positive intersection makes this nondecreasing; the preceding p_a<=0 forces every addition to have intersection1 and keeps p_a=0. Thus the resulting positive anti-nef cycle satisfies p_a(Z_S)=0. No unread fundamental-cycle classification is being imported.
Now let L=P+N be the local decomposition, with P nonzero. Its intersections with exceptional curves equal those of K_X+C'+E_red, since the numerically pulled-back K_T+D has zero exceptional intersections. Suppose a connected component S of the positive support of N meets C'. On S, nefness and P.N=0 give P.E_i=0 and hence N.E_i=L.E_i.
S cannot be the whole connected exceptional block: that would give P.E_i=0 for every component, forcing P=0 by invertibility. Thus S has an external exceptional contact as well as its contact with C'. Write D_ext for C' plus exceptional components outside S. The SNC condition and positivity of all coefficients of Z_S give D_ext.Z_S>=2.
Adjunction for p_a(Z_S)=0 gives (K_X+Z_S).Z_S=-2. Therefore
  N.Z_S=(K_X+E_S+D_ext).Z_S
       =-2+(E_S-Z_S).Z_S+D_ext.Z_S >=0.
Indeed E_S-Z_S has nonpositive coefficients and Z_S is anti-nef on S. But N has strictly positive coefficients on S, Z_S.E_i<=0 there, and at least one intersection is strictly negative by negative definiteness. Hence N.Z_S<0, a contradiction.
It follows that N.C'=0 at the cusp contact whenever its local P is nonzero. Both cusp parts here are nonzero by the reviewed positive target volume and finite lower bound. Thus N_p.C'=0 on W, while N_Y.B'=0 on Y. Equations (4) and target L_Y.B'=-1 now give
  a_W=1+R_q.C>=1,     a_Y=1.                            (5)
This uses the actual rationality of each whole ambient singularity to control cycles on S; it does not assume S itself has already been contracted to a rational singularity.

## A target upper bound from canonical extension
Write pi^*B=B'+Z_B, Z_B=sum z_j A_j on the target resolution. Since nB is Cartier, a local defining equation f of nB near q belongs to I_B. The adopted genuine canonical sheaf is omega_Y=I_B Omega, so fOmega is a regular canonical section on Y.
Rationality makes this section regular on X: explicitly, Rpi_*O_X=O_Y, and proper duality on the Cohen–Macaulay surfaces gives Rpi_*omega_X=omega_Y. This is the canonical-extension consequence of rationality, not an identification of arbitrary reflexive forms with logarithmic pushforwards or a new specialized volume theorem.
With compatible canonical divisors, L_Y=K_X+B'+E_red=sum l_j A_j. The coefficient of div(pi^*(fOmega)) on A_j is n z_j+l_j-1. Regularity gives
  n z_j+l_j-1>=0,     -nZ_B<=L_Y.
The divisor -nZ_B is exceptional and relatively nef: pi^*B.A_j=0 implies (-nZ_B).A_j=n(B'.A_j)>=0. By maximality P_Y>=-nZ_B.
Consequently H_Y=pi^*B+P_Y/n is effective. Its exceptional intersections are nonnegative; its intersection with B' is B^2-a_Y/n=0 by a_Y=1 and B^2=1/n. Every other irreducible curve intersects this effective boundary divisor nonnegatively. Thus H_Y is globally nef.
Its square is H_Y^2=1/n-V_Y/n^2>=0, so V_Y<=n and I_Y=V_Y/n<=1, proving (2). No flatness of h at q, exact canonical-index claim, or external local-volume theorem enters this target argument.

## Feasibility decision for the assigned consumer
The published finite-boundary formula always has M_C>=a_W. Equations (2) and (5) imply
  M_C >= 1+R_q.C >= 1 >= sqrt(I_Y).
Hence this completion's sufficient condition M_C<sqrt(I_Y) cannot hold for an actual attached source. The test is closed at this precise scope; no further denominator estimate can repair that strict condition. This does not assert I_W<I_Y or prove that the hypothetical source exists, and it does not rule out a different volume comparison or use of the unrestricted nef interval after effectivity is lost.
The general full-resolution identity L_full.C'=s-2-R.C remains valid. The new cusp-only identity was obtained from finite-h contact plus the local rationality lemma, not by assuming s=1 or deleting other source singularities.

## Optional fixed-target consistency check
The one previously accepted static target S=Proj C[X,Y,W,T]/(X^2-Y^5-WT^7), weights(5,2,3,1), has n=3 and local cover V:(a^2-b^5-c^7=0) modulo mu3 weights(2,2,1). This input has NO actual h/k pair and is not a replacement family. The following check is subordinate and unnecessary for the general feasibility decision.
Blow up V with weights(35,14,10), weighted degree70. The exceptional weighted curve has H^0(O_E(70m)) of dimension m+1: after reducing a-exponents to0 or1, parity forces a-exponent0, and the monomials are b^(5j)c^(7(m-j)),0<=j<=m. Thus deg O_E(70)=1. The exceptional normal Q-line bundle is O_E(-1), so E_V^2=-1/70.
On the c-chart a=r^35 A,b=r^14 B,c=r^10, the residue db wedge dc/(2a) has radial order -12. The boundary c=0 has order10, giving log coefficient -12+1-10=-21. The mu3 action is radial r->zeta r, since the weights reduce to(2,2,1); generic exceptional ramification is3 and the induced map on E is degree1. Therefore E_S^2=3E_V^2=-3/70 and the downstairs log coefficient is -7.
The three weighted-chart covers have equations 1-B^5-C^7=0, A^2-1-C^7=0 and A^2-B^5-1=0, times the radial coordinate. They are smooth. The reduced exceptional boundary, and strict c=0 where present, are transverse coordinate axes. Remaining finite stabilizers are cyclic and act diagonally in local boundary coordinates; finite averaging supplies such coordinates. Unimodular subdivisions of the corresponding two-dimensional quotient cones give nonnegative log discrepancies for one or two reduced boundary axes. Thus no negative correction is hidden in the quotient charts.
On a smooth refinement, P_Y=-7 numerical pullback(E_S): it is relatively nef, while the remaining log discrepancies are effective and orthogonal to that numerical pullback. Hence V_Y=49(3/70)=21/10 and I_Y=7/10. Also E_V.C'_V=10/70=1/7 and projection gives E_S.B'=1/7, so a_Y=1. This confirms the general bound on ONE static target; it is not a universal formula for I_Y or a JC2 counterexample.

## Reading, custody and limits
Fixed41 inputs were physically/hash/mode/bytes/LF gated in batches<=8; eight mathematical artifacts canonically verified; whole frozen STATE195 equals launch STATE and was personally read before mathematics. New public synthesis115 was personally read whole. Own unchanged complete body baselines were reused only after exact hashes; new seal and reviewer-window qualifications are recorded in coverage. The added static report was read only1-72, not whole138, after its own metadata/canonical gate; it is a selected accepted dependency, not a new global-geometry audit.
All12 archive pins and launch blobs passed. A disclosed ordering deviation occurred: the archive receipt used relative paths and an extra git_blob_equal field, causing an initial comparison assertion; a subsequent call displayed static report1-24 before the corrected archive gate passed. No input mismatch occurred, and all later old-body windows followed the successful gate. No new history query, web/source lookup, CAS/farm, paid lane, child, protected-tree or shared/Git/public mutation occurred.
Measured ACK06:39:26.930887Z; whole STATE06:41:03Z; DRAFT06:44:47.135788Z; first checked partial06:54:24.756580Z; strengthened partial07:01:34.905379Z. Private capability0600 with file+directory fsync preceded allocated body writing. Whole own-body read, close/finalize/verify, original raw collision, postpins, hashes and deviations are retained separately. Original07:15/07:25/07:30 author/ROOT/bank and08:00 intake clocks remain unchanged.

## OPENS RAISED
None. The specific completion consumer is closed as infeasible under its adopted hypotheses; no successor is initiated.

## COLLISIONS
Original frozen-public terminal scan and exact raw stdout/stderr are retained separately after canonical verification. Empty is not novelty evidence; sealed bytes are not edited to append a receipt.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15160`.
- Body SHA-256:
  `1ff66eee8afd5d1c3fb9e0388bdc4cb1e1a45dd0b067431be469cc742fa9d962`.
- Frozen basis: `ce05682d614f94a682c422b0cb1090114e294608`.
