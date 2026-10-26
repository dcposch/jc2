# NORMALIZEDV0535 — a finite-boundary bound for normalized cusp volume
Producer: freshglobal1740_astra, configured gpt-6-astra; primary co-research, not independent review.
Date: 2026-10-26 UTC. Launch/report basis: 1c797fcffb79faf49ac37849de4e47aff3d13b48.
Lifecycle: PRODUCER-CHECKED / INTERNAL / UNPROMOTED. Verdict: NEF_COMPLETION_BOUND; NO_NEW_CLOSING_BOUND.

## Statement and exact scope
For the reviewed numerical-resolution invariant V, set I(T,D)=D^2 V(T,cusp;D). On the adopted actual simultaneous model, write c=C^2=1/(ne), and let P be the exceptional maximal nef part defining V_W(p)=-P^2 at the cusp p of C. This report constructs a finite-boundary quantity M_C with
  I(W,C)<=M_C^2.
The actual finite-map comparison already gives I(W,C)>=I(Y,B)>0. A strict M_C<sqrt(I(Y,B)) would therefore close this test. No such strict estimate is proved. The derived bound is not a rescaling of the preceding E_mat majorant.
Keep every adopted hypothesis: Y is normal projective rational, Y\B is the WHOLE A2, B is an ordinary rational cuspidal boundary, q is the ONLY singular point of Y, and K_Y+B=0. The actual maps h:W->Y and k:W->Y are finite and proper birational respectively; W has rational singularities, C is Q-Cartier ample, and each of h_C,k_C is an isomorphism C->B. They need not be the same isomorphism.
We use h^*B=eC, k^*B=C+Z with Z>=0, K_W+C=R=sum_i(r_i-1)E_i>=0, common volume, B^2=1/n, C^2=1/(ne), and neC Cartier. The cusp p maps to q under both curve isomorphisms. The marked source U=A2 is not asserted to equal W\C. The infinitely singular valuation branch remains separate.
The source cusp is ONE exceptional block. Other ambient singularities of W along intrinsically smooth C are not excluded by the q-only hypothesis on Y; none are silently discarded below.

## Evidence and changed test
The five mathematical artifacts were canonically verified after the fixed32 input gate. The independent VOLUMEREVIEW0520 report148LF was personally read whole, including its precise numerical-invariant, finite-scaling, model-independence and positivity conclusions. The mandatory VOLUMESHEET terminal clarification96-103 was also personally read.
Own exact-hash whole readings of VOLUMESHEET0500, LOGVOLUME1202, the public integrations and LOGBRIDGE2148 erratum are retained. The previous work did not test I=D^2V via global nef completion. Multiplying its E_mat inequality by C^2 alone would be unchanged work and is not the present calculation.
The old k-only control1/6->49/60 has preserved cusp but lacks ample C and simultaneous finite h. It does not answer this normalized actual-global question. No new graph, control family, source theorem or history query is used.

## Full compact resolution and the finite formula
Choose a smooth projective resolution rho:X->W resolving C and all needed source singularities. Extend the cusp nef divisor P by zero on every other exceptional block. By the reviewed definition, P is rho-exceptional, relatively nef, nonpositive coefficientwise, and nonzero. Write
  rho^*C=C'+sum_j z_j A_j,    P=sum_(j over p) p_j A_j,
where C' is the strict transform. Since C is effective Q-Cartier, every z_j>=0; over p every z_j>0. Indeed a local equation of neC vanishes at p, so its order along each divisorial valuation centred at p is a positive integer. The other blocks may have zero z_j and have p_j=0.
Put a=-P.C'. It is positive: projection gives rho^*C.P=0, so a=sum_(j over p) z_j(P.A_j)>0. All summands are nonnegative, and some P.A_j is positive because the exceptional matrix is invertible and P is nonzero. In an SNC resolution the unibranch strict cusp meets a single exceptional component A_b over p transversely, so a=-p_b. Its intrinsic cusp type does not fix that coefficient numerically.
Define
  q_C=min_(p_j<0) z_j/(-p_j)>0,
  t_0=min{c/a,q_C}>0,
  M_C=c/t_0=max{a, max_(p_j<0) c(-p_j)/z_j}.              (1)
All minima range over finitely many cusp-exceptional components, not over arbitrary global curves.

## Global nef completion: proof and all other blocks
For t>=0 put H(t)=rho^*C+tP. Its strict-C coefficient is1, its exceptional coefficients are z_j+t p_j over p, and its coefficients on the other source blocks remain z_j>=0. Consequently H(t) is effective exactly when t<=q_C.
For any rho-exceptional A_j, H(t).A_j=t(P.A_j)>=0; outside the cusp block this intersection is zero. For C' itself,
  H(t).C'=c-ta.
For every other irreducible curve Gamma on the smooth X, effectivity of H(t) and the fact that Gamma is not a component of its support give H(t).Gamma>=0. This includes strict omitted E_i, retained affine curves, and curves passing through other singular blocks; it does not require a separate bound for each of them.
It follows that H(t) is BOTH effective and globally nef if and only if 0<=t<=t_0. For t>q_C effectivity fails; for t>c/a its intersection with C' is negative. This is an exact statement for simultaneous effectivity and nefness. It is not a claim that H(t) cannot remain nef after losing effectivity.
The finite reduction is what ampleness alone had not supplied: the positivity of C.Gamma for each curve is insufficient by itself to bound -P.Gamma, but the effective-boundary representation controls all other strict curves at once.
Projection gives (rho^*C).P=0 and therefore
  H(t_0)^2=c-t_0^2 V_W(p)>=0,
because H(t_0) is nef on the smooth projective surface. Multiplying the resulting V_W(p)<=c/t_0^2 by c proves
  I(W,C)=cV_W(p)<=c^2/t_0^2=M_C^2.                       (2)
No volume identification or curvature theorem is used; only the reviewed numerical invariant and surface intersection theory enter this bound.
The quantities in (1) are stable under further resolution. P pulls back by the reviewed invariance, rho^*C pulls back, and H_new(t)=sigma^*H(t). Effectivity of a divisor is equivalent to effectivity of its birational pullback, so q_C is unchanged. Projection preserves a=-P.C', and c is intrinsic. Common refinements therefore leave t_0 and M_C unchanged. This does not identify them with any external invariant.

## The normalized closing consumer and exact remaining condition
From finite h and C^2=B^2/e, the reviewed inequality V_W(p)>=eV_Y(q)>0 gives I(W,C)>=I(Y,B)>0. Thus (2) forces the necessary condition
  M_C>=sqrt(I(Y,B)).                                    (3)
A sufficient strict reverse would follow from BOTH finite conditions
  a<sqrt(I(Y,B)),
  c(-p_j)/z_j<sqrt(I(Y,B)) for every p_j<0.               (4)
Equivalently t_0/c>1/sqrt(I(Y,B)). Since the set of coefficients is finite, these strict inequalities give a genuine margin. Neither inequality in (4) has been established from the supplied actual k data.
These are sufficient conditions for this effective-nef completion, not necessary conditions for every possible strict normalized-volume comparison. Failure to prove (4) is not a no-go theorem for the original normalized question, a different nef completion, or a weaker sufficient closing estimate.
The actual Cartier information makes the remaining coefficients especially concrete. With m=ne and c=1/m, each m z_j over p is a positive integer, and
  c(-p_j)/z_j=(-p_j)/(m z_j).
This controls the denominator, not the numerator -p_j. Likewise mC.Gamma is a positive integer for an irreducible curve on W, but that alone does not bound its cusp-weighted contact. No unproved relation between the Cartier index and individual r_i is used.

## What k and adjunction currently control
The actual compact identities remain valid:
  C.Z=-Z^2=(e-1)/(ne),
  C.E_i=delta_i d_i/(ne),    sum_i z_i^k delta_i d_i=e-1,
where Z=sum_i z_i^k E_i and the closure of h(E_i) has class d_i B. The coefficients z_i^k of the k-exceptional divisor Z are NOT the resolution coefficients z_j of rho^*C in (1). Identifying them would erase precisely the source-resolution information under test.
Those identities constrain Z and global intersections, but no comparison of -p_b or (-p_j)/(m z_j) with sqrt(I(Y,B)) has been deduced. Whole-source geometry and ample C have been used in the global nef argument; they have not bounded the remaining cusp-discrepancy coefficients at the needed strength.
For completeness, use a FULL compact SNC resolution and let s=E_red.C' count all exceptional contacts with C', including blocks away from p. Let L_full be its full numerical log-discrepancy divisor. Since C' is P1 and numerical pullback projects to R.C, adjunction gives
  L_full.C'=s-2-R.C.
If L_full=P_full+N_full is decomposed block by block, then
  sum_(all C-contacting blocks) (-P_block.C')=2-s+R.C+N_full.C'.
Here N_full.C'>=0, but the left side is NOT automatically the cusp quantity a alone. Only if s=1 and the cusp block is the sole contacting block does this specialize to a=1+R.C+N_full.C'>=1. That additional source hypothesis is not supplied and is not adopted.
On the target, the q-only singularity hypothesis does give a_Y=-P_Y.B'=1+N_Y.B'>=1. This does not prove I(Y,B)<=1, nor compare a with a_Y. Also R.C=sum_i(r_i-1)delta_i d_i/(ne); its known sign is not the required upper bound on the cusp term in (4).

## Result, limits and custody
The new result is the actual finite-boundary completion formula (1)-(2), with all source blocks respected. The normalized strict reverse remains unproved. The first missing implication is an actual k-based estimate on the finitely many ratios in (4), or another sufficient strict bound. No arbitrary replacement surface was tested and no E_mat rescaling is promoted as new input.
All fixed32 inputs passed physical/no-symlink/hash/mode/bytes/LF gates in batches<=8, five canonical verifiers, and whole STATE357-to-launch equality. STATE was personally read whole before mathematics; review148 and result96-103 are new personal readings. Own prior readings were reused only with exact fresh hashes. Eleven immutable archive pins and launch blobs passed; no history body/query was used.
Measured ACK05:36:55.543748Z; whole STATE05:38:25Z; initial DRAFT receipt05:40:24.790474Z; checked partial05:46:53.189378Z. Canonical capability0600 with file+directory fsync preceded allocated-partial body writing. Whole own body read, close/finalize/verify, original collision custody, postpins, errors and exact hashes are recorded separately. Original05:50/06:05/06:15/06:25 clocks and06:00 intake/workflow clocks remain unchanged.

## OPENS RAISED
None. The normalized comparison remains the existing assigned gap; no new open identifier or successor.

## COLLISIONS
Original frozen-public terminal scan and raw stdout/stderr are retained separately after canonical verification. Empty is not novelty evidence; sealed bytes are not edited to append a receipt.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10660`.
- Body SHA-256:
  `60d864336056dee2f5c5c01f3c905bb5f04c5bebe13412b6370c9ff9af9e8058`.
- Frozen basis: `1c797fcffb79faf49ac37849de4e47aff3d13b48`.
