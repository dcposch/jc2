# VOLUMESHEET0500 — numerical cusp volume and the actual exceptional-matrix residual
Producer: freshglobal1740_astra, configured gpt-6-astra; primary co-research, not independent review.
Date: 2026-10-26 UTC. Launch/report basis: 8735c22cafc4f40464453fdc9f4bd92c775a7bd3.
Lifecycle: PRODUCER-CHECKED / INTERNAL / UNPROMOTED. Verdict: EXPLICIT_RESIDUAL; NO_NEW_CLOSING_BOUND.

## Scope and outcome
For a precisely defined numerical-resolution quantity, the adopted actual finite h gives V_W(p)>=e V_Y(q)>0. The proof below uses exceptional intersection matrices, not an imported local-volume theorem or identification with an external invariant.
The main upper-bound test yields an explicit actual-matrix charge E_mat with V_W(p)<=V_Y(q)+E_mat. Neither the new sheet budget nor the tested ample-C identities bound E_mat by (sum_i(r_i-1)delta_i)V_Y(q). This is the remaining implication; no JC2 proof, counterexample or all-volume-method no-go theorem follows.
Keep the adopted DIVISORIAL package: Y is normal projective rational, Y\B is the WHOLE A2, B is an ordinary rational cuspidal curve, and q is the ONLY singular point of Y. Both Y and W have rational singularities. There are actual h:W->Y finite of degree e and k:W->Y proper birational, the marked source U=A2, and C isomorphic to B under each restricted map. These two isomorphisms need not coincide.
We use h^*B=eC, k^*B=C+Z with Z>=0, common volume h^*Omega=k^*Omega, K_Y+B=0, and K_W+C=R=sum_i R_i E_i, where R_i=r_i-1>=0. C is Q-Cartier ample, B^2=1/n and C^2=1/(ne). The curves E_i are omitted affine boundary components. The accepted all-Keller sheet budget is sum_i r_i delta_i<=e-1.
The unique cusp p of C maps to q under BOTH restricted isomorphisms. Also h^(-1)(q)={p}, since h^(-1)(B)=C as sets and h_C is an isomorphism. No flatness of h at q is asserted. The separate infinitely singular valuation branch is untouched.

## Fixed evidence and earlier failure
Whole LOGVOLUME1202, its terminal receipt and ROOT scope review were personally read after fresh gates and canonical verification. Its explicit resolution quantity increases from 1/6 to 49/60 under its proper k. The control lacks simultaneous actual finite h and ample C; even its projective globalization has a curve disjoint from C. It refutes only the k-only upper comparison. We do not rerun or replace that control.
The pinned public all-Keller and logarithmic integrations retain their exact hypotheses and own unchanged whole-read baselines. The linked LOGBRIDGE2148 erratum was freshly read whole: canonical pullback must include differential ramification; strict-C cancellation is e-1 minus e, not minus e alone.
All scientific conclusions here remain internal co-research until any separate review. No named volume theorem, external source identification, new history query or new family is used.

## Definition using numerical pullback
For a normal surface germ (T,o) with reduced boundary D, choose an SNC resolution rho:X->T. For a Weil divisor A, define rho_num^*A as its strict transform plus the unique exceptional rational divisor making its intersection with every rho-exceptional curve zero. This definition uses the invertible negative-definite exceptional intersection matrix; it does not assume A is Q-Cartier.
Let D' be the strict boundary and E_rho the reduced exceptional divisor. Define the exceptional log-discrepancy vector L_T=K_X+D'+E_rho-rho_num^*(K_T+D), using compatible canonical divisors. Write L_T=P_T+N_T, where P_T is exceptional and relatively nef, N_T>=0, and P_T.N_T=0. Set V(T,o;D)=-P_T^2.
Here is the finite-dimensional construction, to specify exactly what is used. For the exceptional matrix M, off-diagonal entries are nonnegative and M^(-1) is entrywise nonpositive. A sufficiently large negative multiple of -M^(-1)1 is nef and lies below any given L. Nef vectors below L are closed under componentwise maximum and bounded above by zero. Their componentwise supremum is therefore a nef vector P<=L. If (L-P)_j>0 and (MP)_j>0, slightly increasing P_j preserves both conditions, a contradiction. Thus P.(L-P)=0. This gives the maximal nef part and uniqueness.
For two exceptional nef vectors Q<=P, P^2-Q^2=(P+Q).(P-Q)>=0. Consequently -P^2<=-Q^2. These elementary order and energy properties will be used below.
This quantity is unchanged by further point blowups of an SNC resolution above o. If a branches of D'+E_rho pass through the centre, L_new=sigma^*L+(2-a)F, with a<=2. The decomposition pulls back as P_new=sigma^*P and N_new=sigma^*N+(2-a)F; it has the stated nefness, effectivity and orthogonality. Common refinements give independence of the chosen SNC model. This is the same resolution convention as LOGVOLUME1202, now with numerical pullbacks explicitly specified.
For Y, K_Y+B=0, so L_Y=K_X+B'+E_pi on a resolution pi:X->Y isomorphic off q. For W at p, L_W=K_Z+C'+E_rho-rho_num^*R. No Cartierness of R is silently inserted.
Under the EXACT q-only singularity hypothesis, B' is P1 on the smooth projective X and meets E_pi transversely once after an embedded resolution of the unibranch cusp. Adjunction gives L_Y.B'=-2+1=-1. As L_Y is exceptional, it has a negative coefficient; hence its maximal nef part P_Y is nonzero and V_Y=-P_Y^2>0 by negative definiteness. This argument is not asserted for a weakened package allowing another ambient singularity on B.

## Actual finite-h lower comparison, localized at the cusp
Take a small target neighbourhood of q and its full finite inverse image, whose only point above q is p. Choose compatible resolutions rho:Z->W and pi:X->Y with a proper generically finite morphism g:Z->X of degree e and pi g=h rho. Resolve until the strict boundaries plus exceptional divisors are SNC. Intersections below involve the compact exceptional fibres; resolving elsewhere has no role in this local comparison.
Write rho_num^*R=R_strict+E_R. Here E_R is EFFECTIVE: its coefficient vector is -M_rho^(-1) times the nonnegative intersection vector of R_strict with exceptional curves. In particular the correction is E_R, not the entire divisor R or its strict transform.
For a divisor of Z dominating a divisor of X, the log differential calculation is explicit. Over an exceptional component of pi, ramification r-1 plus the reduced source exceptional coefficient 1 cancels the pullback boundary coefficient r. At strict C the same cancellation uses e-1+1-e=0. Over affine branch divisors the residual coefficient is exactly that of R_strict. Thus
  K_Z+C'+E_rho = g^*(K_X+B'+E_pi)+R_strict+T,
where T is g-exceptional. Its sign is not needed. Subtracting rho_num^*R gives L_W=g^*L_Y+T-E_R, and hence
  g_*L_W=e L_Y-g_*E_R <= e L_Y.
This cancellation is why subtracting g_*rho_num^*R without restoring g_*R_strict would be wrong. All divisors in the surviving correction lie over the cusp.
Let P_W be the maximal source nef part and Q=g_*P_W/e. Pullback of each target exceptional curve is effective and rho-exceptional, because h^(-1)(q)={p}; projection therefore shows Q is relatively nef. Also Q<=g_*L_W/e<=L_Y, so Q<=P_Y by maximality.
Write P_W=g^*Q+K, with g_*K=0. Both terms are supported in the rho-exceptional fibre; its lattice is negative definite. Projection gives K.g^*Q=0 and (g^*Q)^2=e Q^2. Therefore
  V_W(p)=-P_W^2=e(-Q^2)-K^2 >= e(-Q^2) >= e V_Y(q)>0.
This proves only the lower comparison for the DEFINED numerical-resolution quantity. It does not supply the weighted upper estimate and does not assert an external invariant identification.

## Main test: exact proper-k block matrix
Now choose a common SNC resolution Xtilde->W->Y for k over q, also dominating the target resolution. Let the full k-exceptional lattice split into A, the rho-exceptional curves, and T, the strict transforms of k-exceptional curves E_i with centre q. Include ALL rho-exceptional blocks over k^(-1)(q), not merely the block above the cusp p. Curves centred at p0 are outside this local matrix.
Write the negative-definite matrix in blocks M_AA,M_AT,M_TA,M_TT and put G=-M_AA^(-1)M_AT>=0. Empty blocks have their evident zero interpretation. Let L=P+N be the target discrepancy decomposition on this common model. By invariance, -P^2=V_Y(q).
The target log discrepancy coefficient on a strict omitted E_i in T is l_i=R_i+1=r_i>0. Since P<=0, N_i=r_i-P_i>0. Orthogonality P.N=0 and nefness force P.E_i=0 for every i in T.
The numerical pullback of R_T=sum_(i in T)R_i E_i has A-coefficient vector G R_T. Removing the strict T-curves from the reduced exceptional boundary then gives the EXACT source vector, on all A-blocks,
  L_source,A = L_A-G R_T.
This is not a reduced-support approximation: it is the full numerical discrepancy on the source resolution. No relation between global Cartier index and an individual r_i is assumed.
Set eta=P_A-G P_T, considered as a divisor supported on A, and J=(G P_T,P_T), the numerical pullback of the divisor P_T on W. Then P=eta+J, eta.J=0, and M_AA eta equals the A-intersection vector of P, which is nonnegative. Thus eta is source-nef. Also J^2<=0, so -eta^2=V_Y(q)+J^2<=V_Y(q).
The exact remaining discrepancy is
  L_source,A-eta = N_A-G(R_T-P_T).                         (1)
Nothing established so far forces the right side to be nonnegative. If it were, eta would be an admissible source nef minorant and the upper comparison would be stronger than needed; LOGVOLUME1202 already warns against silently assigning such a sign from proper k alone.

## A weaker upper bound with an explicit actual-matrix charge
The following constructs a feasible minorant and makes the missing term quantitative. All positive parts are coefficientwise. Put
  d=[G(R_T-P_T)-N_A]_+,   v=[-M_AA d]_+,   u=-M_AA^(-1)v.
Then u>=0, M_AA u=-v<=0, and M_AA(u-d)=-v-M_AA d<=0; entrywise nonpositivity of M_AA^(-1) gives u>=d. Hence Q_A=eta-u is source-nef and, by (1), Q_A<=L_source,A.
Let V_source,total be the SUM of numerical local volumes over all points of W in k^(-1)(q), computed by the A-blocks. Maximality and energy monotonicity give
  V_W(p) <= V_source,total <= -(eta-u)^2
         = V_Y(q)+J^2+2 eta.u-u^2.                       (2)
The first inequality is merely nonnegativity of each other local volume; it must not be replaced by equality without excluding those other blocks. Define E_mat=J^2+2 eta.u-u^2. This term has no asserted sign by itself, although 2 eta.u-u^2>=0 and J^2<=0. Formula (2) is a derived upper bound on the actual simultaneous model, not a model-family experiment.
Together with the finite comparison, actual existence requires E_mat>=(e-1)V_Y(q). The proposed weighted route would close only if one could additionally prove
  E_mat <= (sum_all_i (r_i-1)delta_i) V_Y(q).              (3)
No proof of (3) is obtained. The obstruction has been localized to the Green matrix G, the target negative part N_A, the coefficients P_T and the source exceptional quadratic form. Generic sheet counts alone do not evaluate these data.

## What actual ampleness and class-group data do give
Let the closure of h(E_i) have class d_i B in Cl(Y)=Z[B], with positive integer d_i. Projection through h and h^*B=eC gives C.E_i=delta_i d_i/(ne)>0. Write Z=sum_all_i z_i E_i in k^*B=C+Z. Since k^*B.Z=0,
  C.Z=-Z^2=B^2-C^2=(e-1)/(ne),
and therefore sum_all_i z_i delta_i d_i=e-1. These equalities use the WHOLE actual compact model and ample C, not a k-only replacement.
On the q-block, ampleness also says the Schur-complement intersection matrix S=M_TT-M_TA M_AA^(-1)M_AT satisfies the corresponding positive C-intersection constraints; equivalently (with the actual Z-coefficients) S z_T=- (C.E_i)_(i in T)<0. These are genuine restrictions on the actual matrix.
They do not yet estimate the defect in (1) or the quadratic charge in (2). The sheet bound controls sum r_i delta_i; the displayed ample identities involve z_i and d_i, whereas E_mat involves G,P_T,N_A and their energies. No inequality eliminating these extra quantities has been proved. This is a precise missing comparison, not a claim that the full actual hypotheses can never imply one.
If (3) held, the accepted sheet bound would give E_mat/V_Y <= sum(r_i-1)delta_i <= e-1-sum delta_i<e-1 when omitted curves exist, contradicting the necessary lower bound. This arithmetic is only the closing consumer, not evidence for (3).

## Limits, coverage and custody
The finite lower bound and explicit matrix upper bound are source-free internal deductions for the specified numerical quantity and adopted divisorial package. They are not independently promoted. The weighted estimate remains unproved; no actual Keller counterexample, infinitely-singular conclusion, source-theorem import or automatic successor follows.
All26 fixed inputs were physically/hash/mode/bytes/LF gated in batches<=8. Three mathematical artifacts were canonically verified; frozen STATE351 equals launch STATE and was personally read whole before mathematics in <=24LF windows. Own unchanged governance/helper and public report baselines were reused only after exact fresh matches. LOGVOLUME1202, its scope receipts and the linked erratum were read whole. All11 immutable archive pins and launch blobs were checked; no history bodies or new history query were used.
Measured ACK04:58:52.936575Z; whole STATE05:00:17Z; secure capability0600 with file+directory fsync and empty-partial inspection preceded DRAFT05:03:43.195403Z; useful checked partial05:08:12.692544Z. Original05:20/05:35/05:45/05:50 clocks and06:00 intake remain unchanged. Exact coverage, deviations, lifecycle timestamps, postpins and hashes are retained separately.

## OPENS RAISED
None. The existing weighted comparison gap is retained without a new open identifier.

## COLLISIONS
Original terminal frozen-public scan and exact raw stdout/stderr are retained separately after canonical verification. An empty scan is not novelty evidence; sealed bytes are not changed to append a receipt.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13883`.
- Body SHA-256:
  `7f8f2b77b9353b8a7dee61d784afba5ec087f9ab0f656fc4f6313cd8b47920e6`.
- Frozen basis: `8735c22cafc4f40464453fdc9f4bd92c775a7bd3`.
