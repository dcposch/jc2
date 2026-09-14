# F10 all-r late contact: exact column ideal, uniqueness still unresolved

2026-09-09. MANUAL PRODUCER RESULT, pending independent review. No source point, leading nonemptiness, ideal decision or runtime authority. First action20:09:57 UTC; controlling cap20:24:57 UTC. Basis0d39df3c9fd69c939a8420c54d03228b9077777d. Exactly four accepted reports were current-pinned and read WHOLE/reused as documented in the matching input-pins and READ-SCOPE. No middle-band premise is used.

## 1. Outcome and coefficient-ring scope

Fix integers r>=2 and1<=j<=r-1. Put m=3r+1,n=5r+2,kappa=n+j,nu=n/m,alpha=kappa/m. Then5/3<nu<alpha<2 and3alpha-5=(1+3j)/m. Let B be ANY commutative Q-algebra with

    C=theta^3+Ftheta^2+Htheta+a,
    D monic of degree5, D(0)=b,
    a,b units, mCD'-nC'D=-theta^7.                 (1)

Define H_i(alpha)=[theta^i](C/a)^alpha by the finite binomial recipe; no analytic branch is involved. Let (g1,g0) be the literal homogeneous late-column residual for the variation k_j=1, after the three admissible upper equations have reconstructed V of degree<=2. The proved reduction is

    (g1,g0)=(H6(alpha),H7(alpha)) in B.             (2)

It is an equality of ideals, not just equality of geometric zero sets; nilpotents and arbitrary scalar extension are included. Also

    (H5(alpha),H6(alpha),H7(alpha))=B.              (3)

Consequently H5 is a unit on the entire contact quotient. There is no lost H5=0 chart or selected field factor. A normalized nonzero homogeneous kernel exists over a field exactly when both contacts vanish.

NOT PROVED: that the ideal in(2) is B for the actual integers(r,j). No counterexample to that assertion was found. Equation(3) does not imply it. The useful result is the exact full-base column/contact identification and a proved safe normalization on the still-possibly-nonempty contact quotient, not a uniform late-band exclusion.

## 2. Actual homogeneous source variation and corrected operator

From accepted16r use weights wt(S)=1,wt(t)=r and theta=t/S^r. Freeze every other source coefficient, including all earlier bands and their complete mixed forcing, and vary only k_j. The corresponding gap is h=m-j. Since j<r, the weight-j A band has no t-dependent monomial: its homogeneous variation is S^j*k with scalar k. The B band has weight n-h=2r+1+j. Thus its varying part is S^(n-h)V(theta) with deg V<=2. At j=r-1 the nominal t^3 slot has S exponent0, but16r gives B3(0)=u^2, independent of k_j, so its variation is still zero. Higher t slots have negative S exponents or are fixed. No beta/gamma kernel is introduced; their existing gauges remain fixed.

The homogeneous chain rule (accepted17q, independently checked) gives

    L(k,V)=mCV'-(n-m+j)C'V+j*k*D'.                (4)

This confirms root's immediate correction: the originally suggested coefficient -j on C'V was wrong. Since k varies only A's constant-in-t polynomial k(S), the full target Delta has zero variation. All earlier mixed forcing stays in the affine part and is NOT set to zero. In particular at j=r-1 the direct -u^2*t^5 target lies at the band weight5r, but is fixed in this variation. The gate's separate printed weight for -ell*S*t^4 is corrected to4r+1; it does not affect(4).

The three theta4,theta3,theta2 pivots for V2,V1,V0 are

    delta_l=m*l-3(n-m+j), l=2,1,0.

Here delta2=-(3j+1), and the others subtract positive multiples of m. All are fixed nonzero rationals. Thus for every k there is a unique V_lin(k) killing those upper coefficients. It is k*V_lin(1), and L(k,V_lin(k))=k*(g1*theta+g0). The two actual residual positions are [S^(3r+1+j)]E1 and[S^(4r+1+j)]E0. This establishes the literal column under consideration without importing any intervening-band elimination theorem.

## 3. Correct T identity and highest coefficient

Put T=mCV-nDk, of degree<=5. Direct differentiation gives

    T'=kappa*(C'V-D'k)+L,
    CT'-alpha*C'T=C*L+alpha*k*theta^7.             (5)

The second equality uses precisely nC'D-mCD'=theta^7. Thus a homogeneous kernel satisfies

    CT'-alpha*C'T=alpha*k*theta^7.                 (6)

The theta4 coefficient of L=0 is

    -(3j+1)V2+5j*k=0.

Therefore

    V2=5j*k/(3j+1), T5=-kappa*k/(3j+1).           (7)

The coefficient of theta7 in(6) is independently (5-3alpha)T5=alpha*k, agreeing with(7). If k=0, upper uniqueness forces V=0; a nonzero kernel over a field necessarily has k!=0 and can be normalized to k=1. No arbitrary parameter is divided in constructing the column.

Because a is a unit, the coefficient equations of(6) through theta6 recursively imply

    T_i=T0*H_i(alpha), i=0,...,7,                  (8)

where T6=T7=0 by degree. Over a field with k!=0, (7) makes T5 nonzero, hence T0 and H5 nonzero. Equation(8) then yields both H6=H7=0. A single contact does not suffice for this derivation.

## 4. Safe contact-quotient normalization and converse

Let I=(H6,H7). In B/I define P=sum_(i=0)^5 H_i theta^i. Since the two omitted coefficients vanish, the exact formal power identity implies

    CP'-alpha*C'P=K*theta^7,
    K=(5-3alpha)H5.                               (9)

Indeed the left side has degree<=7 and order>=7. This is an entire polynomial identity, not a necessary finite jet being promoted to an arc.

We prove H5 a unit in B/I. If a maximal residue field also killed H5, then deg P<=4, and (9) would become CP'-alpha*C'P=0 with P(0)=1. Extend that field algebraically. Every root zeta of C is nonzero, since a is a unit; it is simple because a repeated root contradicts(1) at zeta. If P has multiplicity e>=0 at zeta, the leading local coefficient in CP'-alpha*C'P is proportional to e-alpha. Thus the identity forces e=alpha, impossible for the noninteger alpha in(5/3,2). This excludes every maximal ideal containing I and H5, proving(3) and the asserted unit. The zero-ring case is harmless. No reducedness, reality, positivity, generic rank or assumed leading point was used. This argument proves existence of a unit inverse, not an explicitly computed Bezout coefficient list.

Now in B/I choose

    T=alpha*P/((5-3alpha)H5), k=1.                 (10)

Only a proved unit is inverted. To reconstruct polynomial V, work modulo monic C. The constant a makes theta invertible in B[theta]/(C), explicitly by theta*(-a^-1*(theta^2+Ftheta+H))=1. Equation(1) then makes C' and D units modulo C, because nC'D=theta^7 there. Combining(6) for(10) with that same identity gives C'*(T+nD)=0 modulo C. Hence

    V=(T+nD)/(mC)                                 (11)

is a polynomial over B/I of degree<=2. Substituting into(5) yields C*L=0; monic C is a nonzerodivisor in every polynomial ring, so L=0. This proves the converse over the whole contact quotient, including nonreduced algebras, without rootwise interpolation or arbitrary field inversion.

## 5. Ideal equality, not merely a residue-field equivalence

Let J=(g1,g0). Over B/J take k=1 and its unique V_lin(1). Then L=0. By(7)-(8), T0*H5=-kappa/(3j+1), a rational unit. Both T0 and H5 are therefore units in B/J. The identities T0*H6=T0*H7=0 force H6=H7=0. Thus I is contained in J.

Conversely (10)-(11) give a kernel with k=1 over B/I. The fixed upper pivots identify its V with V_lin(1), hence g1=g0=0 in B/I and J is contained in I. This proves(2) literally. In particular the sought unimodular column exists exactly if the two-contact ideal is the unit ideal. The proof removes any missing normalization or nilpotent loophole, but does not settle that remaining unit-ideal assertion.

## 6. The suggested quadratic comparison is equivalent, not a new uniqueness proof

Suppose a field-point solution T obeys CT'-alpha C'T=K theta7 while D obeys CD'-nu C'D=-theta7/m. At a simple C-root,

    T/D=lambda=-m*nu*K/alpha.

Consequently T-lambda D=C E, deg E<=2. Substitution gives exactly

    C E'+(1-alpha)C'E+lambda*(nu-alpha)*D'/nu=0.    (12)

For the actual kernel K=alpha*k, one has lambda=-n*k and E=mV. Equation(12) is then precisely(4), multiplied by a fixed scalar. It does not supply an additional independent equation or rule out contact. Treating it as a new constraint would double-count the same homogeneous kernel. This identifies the first unearned arrow in the proposed uniqueness route: no argument here prevents the same cubic from having both the nu and alpha contact pairs.

## 7. Manual changed-hypothesis controls

j=0 gauge control: if j=0, alpha=nu, k is the A-constant gauge, V=0 and T=-n*k*D solve(4)-(6). Since D/b=(C/a)^nu+O(theta8), both contacts vanish at every allowed leading point. Formula(7) still agrees. Thus no claimed exponent uniqueness may include j=0.

Dropping one contact, at the formal-contact tier ONLY: take c=1+theta^2+w theta^3 with w^2=-(alpha-2)/3 and a=1/w so C=a*c is monic. Then H6=(alpha)_2*w^2/2+(alpha)_3/6=0, but H7=(alpha)_3*w/2!=0. The truncated fifth-degree power has a nonzero theta6 differential error. This is a changed cubic, NOT a point of the leading nu algebra: its linear coefficient is zero, and the accepted standalone contact calculation shows it cannot support the required nu pair. We do not claim it establishes independence of the two contacts after imposing(1); that sharper question is unresolved.

Repeated-root/leading-ODE control: C=(theta+1)^3 cannot occur in(1), since at theta=-1 the left side is0 and the right side is1. If both the leading ODE and actual exponent interval are dropped, that cubic admits contact powers alpha=4/3 and5/3, giving polynomials of degrees4 and5. Thus repeated-root toy contacts do not refute the genuine guarded question, and multiplicity hypotheses cannot be silently omitted.

Generic-only nonvanishing control: over Q[t], the column(t,t^2) is nonzero over Q(t) but its ideal(t) is proper and vanishes at t=0. This abstract algebra control is not an F10 point; it shows why a generic column computation cannot prove the required global unimodularity. Our equality(2) avoids that inference, while leaving its actual unitness undecided.

## 8. Stop, precise remaining quantity and custody

The new exact conclusion is(2)-(3), the source-typed operator with all fixed earlier forcing retained in the affine part, and the two-way reconstruction. No all-r late-column nonvanishing, counterexample, complete row elimination, source point or F10/JC2 conclusion is claimed. The parent early tower is not extrapolated to later source supports. No leading nonemptiness attribution is needed or adopted.

Remaining quantity: for each actual r>=2,1<=j<=r-1, whether B/(H6(alpha),H7(alpha)) is the zero ring. Cheapest next mathematical test is a genuine uniform uniqueness or an exact exceptional relation for this simultaneous-contact locus, not merely the already-equivalent quadratic E equation or an unproved resultant assertion. No calculation or follow-on is authorized. This is one scoped unresolved source-algebra assertion, not an added canonical OPEN ID.

Exactly four allowed reports were current-pinned before reads; aggregate truncation was repaired by separate WHOLE reads. All derivations are manual. ZERO mathematical subprocess, CAS, arithmetic script, coefficient computation by code, import/compile/test, AWS/SSH/process/network/web, agent or shared/frozen edit occurred. Own input/postpins, read scope and terminal transaction accompany this report. Own WHOLE/raised-OPEN/collision checks precede the marker; all writers IDLE at publication within the original cap.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11383`.
- Body SHA-256:
  `70b5d34f77c66969dfdb162d47d9920350f8e38e13c43f680c2193c158d5c15d`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
