# Trace-zero kernel: exact obstruction, no closing implication

Owner /root/contact_collision_geometry. MANUAL / UNREVIEWED. First action 2026-09-11 20:35:37 UTC; original reserve 20:52 UTC / HARD 20:55 UTC. Basis 0d39df3c9fd69c939a8420c54d03228b9077777d.

Exactly TASK and its pinned ROOT report were read FRESH WHOLE after current hashes. The accepted input is theorem (T), with TASK's direct Theorem 7.1 residue-proof repair, not the frozen report's historical review status or section 8. No linked source or live report was used. External comparison/direct-image facts below are explicitly stipulated, not freshly literature-verified.

## 1. Exact kernel calculation

For the actual Keller map (P,Q), put A=C[P,Q], R=C[x,y], K=Frac(A), L=Frac(R), W=D_A and M=Tr_(L/K)(R), as in accepted (T). Set E=ker(Tr:R->M). Let c be the number of irreducible components of the ACTUAL nonproperness curve D. De Rham degrees are unshifted 0,1,2. The source identities H0(R)=C and H1(R)=H2(R)=0 are as stipulated in TASK.

Name the only further comparison input used for the dimension calculation: an IC module L_i supported on a curve with normalization A1 has

    H^j_DR(L_i)=H^(j-1)_DR(A1).

This is the standard normalization/IC direct-image comparison, including its codimension-one shift; it is STIPULATED here, not freshly source-verified. Thus H0(L_D)=H2(L_D)=0 and H1(L_D)=C^c. The exact sequence 0->A->M->L_D->0, with polynomial Poincare exactness for A, gives

    H0(M)=C,  H1(M)=C^c,  H2(M)=0.

In the long exact sequence of 0->E->R->M->0, the map H0(R)->H0(M) is multiplication by N=[L:K], hence an isomorphism. The remaining source cohomology vanishes. Therefore

    H0(E)=H1(E)=0,  H2(E) is canonically H1(M)=C^c.       (1)

This is compatible with every stated hypothesis; it is not a contradiction. Proving H2(E)=0 would indeed force c=0, but (1) alone only reformulates that properness goal.

The primitive obstruction is literal. For h in E choose a polynomial one-form alpha in the lifted frame with d alpha=h dp wedge dq. Its coefficientwise trace beta is closed in the M-valued de Rham complex. Changing alpha changes beta by an exact M-valued form because H1(R)=0. The class [beta] vanishes exactly when a trace-zero primitive exists: if beta=d m, lift m to b in R using trace surjectivity and replace alpha by alpha-d b. Conversely a trace-zero primitive makes that class zero. This is precisely the isomorphism (1), with the inverse of the connecting map.

There are explicit cohomological representatives, without computing source polynomials. By (T), each beta_i=dd_i/d_i has coefficients in M. Their classes are independent: at the generic smooth point of component i, beta_i has residue one, the others zero, and the differential of a rational function has zero residue. Since dim H1(M)=c, they form a basis. Choose polynomial lifts a_i,b_i of their two coefficients. Then

    e_i=delta_p b_i-delta_q a_i lies in E

and its class in H2(E) is nonzero, corresponding to [beta_i]. These are existential polynomial representatives, not emitted cofactors. Ordinary polynomial integration does not make their trace-zero primitive obstruction disappear.

## 2. Splitting and duality audit

The field trace has the horizontal K-linear section m->m/N and the rational projector r->r-Tr(r)/N. These rational maps need not preserve R. The polynomial source supplies a useful exact check:

    R intersect K = A.                                    (2)

To prove it, take a/b in K in reduced form. If an irreducible ell divides b, then ell(P,Q) is nonconstant by algebraic independence, hence has an irreducible divisor in C[x,y]. That source curve cannot map to a point because the Keller map is etale and quasi-finite. It consequently dominates ell=0; a(P,Q) does not vanish generically on it, while b(P,Q) does. Thus a/b has a pole there and is not in R. No nonconstant denominator is possible.

If D is nonempty, accepted height-one fullness M_eta=K implies M is not contained in A. Choose m in M\A. By (2), m/N is not in R. Thus the obvious rational section genuinely fails, and subtracting its trace from a polynomial lift can leave the polynomial ring. This is an obstruction to that correction method, not a proof that every conceivable section fails for elementary reasons.

A sharper elementary statement is available when D is nonempty:

    Hom_A(M,R)=0.                                         (3)

Any such map extends generically from M tensor_A K=K to R tensor_A K=L, hence is multiplication by a fixed r in L. Fix a boundary component ell=0 and a retained source divisor above it, whose existence was proved in (2). Its valuation is nonnegative on R_eta and strictly positive on ell. But M_eta=K contains ell^{-n} for every n. If r were nonzero, r ell^{-n} would eventually have negative valuation, contradicting that the localized map lands in R_eta. Thus r=0. This excludes EVERY A-linear section of the trace, not only m/N; flatness of the source supplies no such section.

A W-linear section would also split the de Rham complexes and force H1(M) to be a summand of H1(R)=0. Conversely if D is empty, M=A and m/N is a W-linear section. Thus splitting is equivalent to the missing properness conclusion, not an independently supplied premise. An arbitrary C-linear vector-space section exists but need not commute with derivatives.

The trace pairing Tr(ab) is nondegenerate on the finite separable FIELD extension L/K and horizontal under the lifted derivations. Its trace-zero generic summand is orthogonal to K and nondegenerate, since Tr(1)=N is nonzero. This rational statement controls no boundary extension. On R the pairing takes values in M, not necessarily A, and R need not be finite locally free over A. It therefore does not supply the asserted integral perfect pairing or identify the global holonomic D-dual of R with R.

The relevant standard duality statement, if invoked, is conditional here: holonomic duality interchanges ordinary direct image f_+ with compact-supported direct image f_!. Their equality needs a properness/cleanness argument. Assuming it for this nonproper etale map would insert precisely an unproved boundary assertion. Regular holonomicity alone supplies finite length and exact duality, not semisimplicity; a proper direct-image decomposition theorem cannot simply be applied to f.

## 3. Controls and surviving scope

The genuine etale open immersion j:Gm x A1 -> A2 has ordinary direct-image module B0=A[1/p]. Its field extension has degree one and its generic trace pairing is the identity. Nevertheless

    0 -> A -> B0 -> H_p=A[1/p]/A -> 0                   (4)

does not split as W-modules. Every element of H_p is killed by some power of p, whereas B0 has no p-torsion. Consequently every W-linear map H_p->B0 is zero, ruling out a section. Under the standard regular-holonomic localization fact, this is a concrete NONSEMISIMPLE regular-holonomic nonproper etale direct image, not just a formal warning about decomposition theorems.

It also tests self-duality. With the usual exact holonomic duality and the standard self-duality of A and of the smooth-divisor IC module H_p stipulated, dualizing (4) gives

    0 -> H_p -> D(B0) -> A -> 0.

The dual has nonzero p-torsion and B0 does not, so they are not isomorphic. A perfect rational trace pairing, even of degree one, cannot select the same extension across the missing divisor. This is exactly the ordinary-versus-compact-supported direct-image distinction; no primary duality reference was read in this task.

The control does NOT refute any Keller properness assertion: its source is Gm x A1, not A2. It has H1_DR(B0)=C, represented by dp/p, and H2_DR(B0)=0. Its trace kernel is zero. The nonzero source H1 is precisely why it does not satisfy the actual-source long-exact-sequence specialization (1). It defeats the proposed general semisimplicity/self-duality inference, not every possible use of the polynomial source.

VERDICT: NO_CLOSING_IMPLICATION. The additional polynomial implications (2)--(3) rule out rational correction and A-linear splitting on a hypothetical nonproper source; (1) identifies the exact remaining obstruction. They do not show H2(E) must vanish. Neither source polynomial primitives nor generic trace self-duality supplies that missing step. No impossibility of all future kernel arguments is asserted.

QUANTITY / CHEAPEST TEST: exact H1/H2 kernel calculation, residue representatives, rational-section failure, and the genuine etale nonsplitting control. A new proof would have to kill the classes [beta_i] by an additional polynomial-source argument or justify a W-splitting without presuming properness. Restating that goal is not a discriminator or a launched follow-on. Scientific runtime is UNMEASURED; zero scientific execution was authorized or performed.

OWN CHECKS: only the two pinned inputs and exact owned documentary targets were used. No clipping, reuse, new OPEN identifier, live source, web/AWS/SSH, shared/protected/Git access, code, CAS/import/AST/syntax/test/dummy or other agent occurred. Initial targets were absent; ROOT TASK was preserved. Own WHOLE readback, current input postpins and own-only collision/scope checks precede the unique final body marker; expected transaction verification and sealed WHOLE readback precede custody. All writers are idle before handoff. This is an unreviewed manual report, not a new properness theorem or JC2 claim.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9463`.
- Body SHA-256:
  `973263de59ebf194c460aa8ebb8c5d7d34681a3e7d3f11f54ea42a405649fa1d`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
