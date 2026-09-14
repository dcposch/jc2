# F10 double-h discriminator

Manual bounded investigation from four initially assigned accepted frozen inputs, plus the two explicitly authorized accepted17zzh imports added at19:08 UTC. First action 2026-09-10T18:59:22.490887620Z; fixed stop 19:18 UTC and publication reserve 19:15 UTC. No scientific execution or coefficient-body access.

## Scope

The question concerns the whole leading algebra and the actual Euler-reconstructed mate, not a leading-only mate, a selected number-field component, or a source point inferred from a relaxation point. Conclusions and exact controls are recorded below before sealing.

## 1. Outcome: a lossless global ell elimination, not an exclusion

The double-h relaxation admits an explicit elimination of ell over the WHOLE guarded leading algebra, including every nonreduced base change. It reduces its literal presentation from 6r+2 lower variables and at most 8r+4 remainder slots to 6r+1 lower variables and at most 8r+3 slots. The eliminated two selected slots are replaced by ONE compatibility, and every other remainder slot is retained after the exact substitution. No generic coefficient is divided and no h-root or component is selected.

This is outcome (iii), a small faithful structural reduction with a constructive refinement of KNOWN ell unitness. The accepted17zzh theorem already supplies global ell-column unitness and full-row elimination; those are NOT new findings. New here are preservation of that whole column under double-h division, the exact changed forcing, and a finite formula for a left inverse whose coefficients the accepted producer did not specify. Neither emptiness nor a point of the relaxation is proved. Verdict on the proposed uniform shortcut: NO_CLOSING_DISCRIMINATOR. Whether the reduced remainder ideal is the unit ideal remains unresolved; no runtime improvement is claimed.

The first four inputs are accepted16r Euler producer a5ab487c... and FIRST gate77d59f7b..., and accepted all-r scale producer b6c5e894... and FIRST gate c9fcecfc.... All four current full hashes matched before their fresh WHOLE reads. At19:08:52 the authorized accepted17zzh producer55f37038... and FIRST gate dfc13df4... were also pinned before WHOLE reads. Their global unitness theorem is imported, not re-reviewed. The constructive formula below was derived before that comparison and is retained only as a finite refinement. Historical provisional headers are governed by the assigned accepted scope. The scale gate's wording qualification is retained: a retained low row need not be independent. The ell gate's changed-control series is valid only modulo z^5, not exactly; ROOT's stated z^5 coefficient1/1715 qualification is retained, and that control is not used in this proof. No linked provenance, actual coefficient packet, degree-selection result, or live lane was read.

## 2. Literal ring and whole-mate equations

Fix r>=3, m=3r+1, n=5r+2, q=2r+1, so n=m+q. The accepted leading ring is L=B_nu[s,s^-1], nu=n/m, with its whole B_nu, not a selected field factor. Its leading coefficients satisfy

    C(theta)=theta^3+F theta^2+H theta+a,
    D(theta) monic of degree5, D(0)=b,
    m C D'-n C' D=-theta^7,
    a=1/(W s^3), H=1/(W s^2),
    F=V/(W s), b=1/(t5 s^5).

In particular a,H,b are units. The proof below uses these units and this polynomial identity, not reducedness, positivity, or an assumed field. Let R0=L[u,d_0,...,d_(r-1),v_0,...,v_(2r-1),k_1,...,k_(m-1)] and R=R0[ell]. Restore d_r=F, v_(2r)=H, k_m=a, k_0=0. There are 6r+1 variables in R0 and 6r+2 in R. Define

    f=S d-u, h=1-u d+S v, k=sum k_i S^i.

Since deg_S h=q and its leading coefficient is the unit H, hbar=H^-1 h is monic. Its square has degree 2q=4r+2 and generates the same polynomial ideal as h^2. Division by hbar^2 is defined over EVERY R0-algebra without dividing any further coefficient.

Reconstruct the ACTUAL whole B by accepted16r.5, B5=S^2, [S]B3=B0(0)=0. Its two unsolved residuals, with derivatives taken in S before any division, are

    E0=k' B1-h B0'-1,
    E1=2k' B2+h' B1-h B1'-2f B0'-u.

The target constants and every upper forcing, including all u and ell terms, are retained. The relaxation T_r means R modulo ALL coefficients of rem(E0,hbar^2) and rem(E1,hbar^2). Any full source gives this quotient a point, but the converse is neither asserted nor used.

## 3. The entire ell column survives double-h division

Write a dot for the coefficientwise derivative with respect to ell. The Euler recurrence is affine in ell: B4,B3 are independent of ell; B2,B1,B0 are affine because their coefficient operators and f,h,k are independent of ell. Differentiating the actual recurrence gives exactly

    dot B4=dot B3=0, dot B2=S,
    J=dot B1=-u+sum_(i=1)^r (2i/(3i+2))*d_i*S^(i+1),
    -3S K'= -1-f'J+2f J'-2S h'+h,
    K=dot B0, K(0)=0.

The last constant compatibility is the derivative of the accepted automatic second resonance, so K is the uniquely gauged polynomial. Its degree is at most q. Thus the WHOLE residual columns are

    J0=dot E0=k'J-h K',              deg J0<=4r+1,
    J1=dot E1=2S k'+h'J-h J'-2f K', deg J1<=3r+1.

Both degrees are strictly below deg(hbar^2). Hence their remainders are THEMSELVES; none of their coefficients is folded into another slot. Put P_i=rem(E_i at ell=0,hbar^2). Then the exact remainder pair is P_i+ell*J_i. This uses the full Euler mate, not its leading part. The leading part will be used only to construct a left inverse for two entries of this actual column.

For precision, dot B2=S follows from (2-3S d/dS)dot B2=-S. The next forcing is u-2Sf'+2f=-u-2S^2 d', giving the displayed J. Differentiating the j=0 equation gives the displayed K with its minus-one target. Thus neither target differentiation nor the u=0 boundary has been discarded.

## 4. Known column unitness; a finite constructive left inverse

Let j=2r/(3r+2) and

    g=((4r+1)H-(r+1)j F^2)/(3q),
    Q(theta)=theta^2+jF theta+g.

The weight-q part of dot B is S^q Q(t/S^r): dot B2=S, the top of J is jF*S^(r+1), and the top of K is g*S^q. Equivalently the three upper coefficients of m C Q'-q C'Q fix these quantities. Direct factored multiplication gives

    m C Q'-q C'Q=-theta^4+L1 theta+L0,
    L0=m a jF-q H g,
    L1=2m a+r jFH-2q Fg.                       (A)

Indeed the theta4 coefficient is 2m-3q=-1; theta3 is 2rF-(3r+2)jF=0; theta2 is (4r+1)H-(r+1)jF^2-3qg=0. The remaining two coefficients are as displayed. On the actual column,

    [S^(4r+1)]J0=L0, [S^(3r+1)]J1=L1.         (B)

Define a finite L-linear functional on polynomials R(theta)=R0+R1 theta. Put c=C/a, nu=n/m. Formal powers of c, which has constant1, have their usual rational binomial definition over any Q-algebra. Integration below has zero constant and divides only positive integers. Define

    N_R=-(1/m)*trunc_(degree<=4)
          (c^nu * integral R*c^(-nu) dtheta),
    Z_R=m C N_R'-n C' N_R+C R,
    lambda(R)= (5m/(nH))*[theta5]Z_R
               +((n-5m)/(na))*[theta4]Z_R.    (C)

Accepted17zzh already proves that (L0,L1) is the unit ideal and permits a choice of Bezout multipliers. It does not specify their coefficients. Formula(C) is a literal finite coefficient prescription, using degrees at most4 of N_R and at most6 of Z_R; it is not an infinite computation. It uses only the already-required a and H units and rational scalars. In particular it does not divide g,F, h, h', or a parameter-dependent minor. Write alpha=lambda(1), beta=lambda(theta). The following verifies this PARTICULAR choice, not a re-review of the accepted theorem:

    alpha L0+beta L1=1.                        (D)

Here is an all-algebra proof with all constants and signs. Take R=L0+L1 theta, and form M=a*g*D-b*C*Q. Then deg M<=5 and M(0)=0, even if g=0. Using n=m+q, the two accepted/displayed ODEs give

    m C M'-n C'M = -a*g*theta7
                    +b*C*theta4-b*C*R.       (E)

Before truncation, the expression defining N_R solves m C N'-n C'N=-C R with N(0)=0. Its truncation therefore has Z_R divisible by theta4, and deg Z_R<=6. Equation (E) implies M and b*N_R have identical coefficients through degree4: the remaining forcing starts at theta4 and affects only degree5 and above in the solution. This coefficient recursion has pivots m*a*i for i=1,...,4, all units. Consequently

    M=b*N_R+t*theta5                           (F)

for a uniquely determined t in L, without any g inversion. Substitute (F) into (E), cancel the polynomial monomial theta4, and write z_i=[theta^i]Z_R. Constant and theta coefficients give, respectively,

    a(5m*t-b)=-b*z4,
    H(5m*t-b)-n*t*H=-b*z5.

Thus n*t*H=b*(z5-H*z4/a). Substitution into the first equation and cancellation of the existing unit b yield

    1=(5m/(nH))*z5+((n-5m)/(na))*z4.

This is precisely lambda(R)=1. All cancellations are by polynomial monomials or the stipulated units a,H,b and nonzero rationals; the proof works unchanged with nilpotents. In particular it establishes a specific global left inverse, not merely rank at residue fields or a claim that one entry L0 or L1 is a unit.

## 5. Exact quotient maps and the remaining test

In the remainders P0,P1 defined in section3 set

    A0=[S^(4r+1)]P0, A1=[S^(3r+1)]P1,
    Kstar=alpha*A0+beta*A1,
    Phi=L0*A1-L1*A0.                           (G)

Here alpha,beta are the functional coefficients (C), not the already-fixed mate shear gauge. The two selected remainder equations are A0+ell*L0 and A1+ell*L1. Apply the matrix

    [ alpha   beta ]
    [ -L1     L0   ],

whose determinant is1 by (D) and whose inverse is [L0,-beta;L1,alpha]. The selected pair becomes ell+Kstar and Phi. This is an invertible row operation over L, not generic Gaussian elimination.

Define J_reduced in R0 by Phi and EVERY coefficient of P_i-Kstar*J_i except the two selected slots (i=0,S^(4r+1)) and (i=1,S^(3r+1)). Then there is an exact algebra isomorphism

    T_r = R0[ell]/(all coefficients P_i+ell J_i)
          ≅ R0/J_reduced,                     (H)

with forward ell -> -Kstar and all other variables fixed. The reverse map fixes R0; its well-definedness follows by the same invertible two-row operation, and ell=-Kstar holds in T_r. The inverse matrix reconstructs BOTH removed selected rows from ell+Kstar and Phi. Every other remainder equation is literally substituted, not dropped. All existing leading/scale guards are in L and preserved unchanged. If additional full-source equations are retained alongside the relaxation, the same substitution must also be applied to every one of them.

There are two remainders each with 2q=4r+2 slots. Removing the two selected slots and adding Phi leaves at most 8r+3 slots in 6r+1 lower variables over L. Counts are envelopes; no independence, actual nonzero row count, height, dimension or computational speed is asserted. The original full residual equations E_i=0 remain stronger than their double-h remainders. In particular (H) is a ring isomorphism for the stated relaxation, NOT an equivalence of relaxation points with Keller or compact source points.

There is a genuine forcing distinction from the already accepted full-row ell elimination. Divide the actual ell=0 residuals as

    E_i^0=hbar^2*Q_i+P_i.

Let c0=[S^(4r+1)]E0^0, c1=[S^(3r+1)]E1^0 and delta_i the respective coefficient of hbar^2*Q_i. Then A_i=c_i-delta_i and the double-h value is

    ell_star=-(alpha*c0+beta*c1)
                  +alpha*delta0+beta*delta1.          (I)

Thus the old full-row ell value cannot simply be transplanted: the quotient contributions can change the selected forcing. No independence or vanishing of these actual quotient contributions has been proved. Since the ENTIRE ell columns have degree below2q, both Euclidean quotients Q_i are ell-independent.

On L the two top residual slots have already vanished, so deg E0^0<=7r+1 and deg E1^0<=6r+1. Hence deg Q0<=3r-1 and deg Q1<=2r-1. These at most5r quotient slots are exactly the remaining difference between full source and double-h relaxation: because hbar^2 is monic, E_i=0 is equivalent to P_i+ell J_i=0 AND Q_i=0. They must all be added, unchanged by ell substitution, to recover the full-source ideal. The count is consistent: (8r+3)+5r=13r+3 slots after ell elimination. This is an exact decomposition, not an assertion of row independence or emptiness.

The remaining question is whether J_reduced is the unit ideal over WHOLE L with every remainder slot retained. No unit or guarded relaxation point was obtained, and the leading-column argument above does not decide this ideal. In particular there is no proved new nonlinear forcing contradiction beyond the displayed correction(I).

There is also a necessary local forcing identity, checked directly from the actual E0 rather than any leading approximation. Over T_r[S]/(hbar),

    k'*B1=1,
    k''*B1+k'*B1'-h'*B0'=0.                  (J)

The first follows by reducing E0 modulo h. The second follows by differentiating the full divisibility E0=hbar^2*Q0 BEFORE reducing modulo hbar; the omitted term -h*B0'' vanishes only at that final reduction. Thus k' is a unit in the entire finite free rank-q T_r-algebra T_r[S]/(hbar), with inverse B1. Multiplication by k' consequently has a unit determinant; defining the monic resultant by this determinant gives Res(hbar,k') a unit in T_r. These statements survive nonreduced base change. This is an automatic consequence in the relaxation quotient, not a claimed unit of the freely generated leading/lower base before its equations are imposed. No h' inverse or squarefreeness follows. Conditions(J) do not supply a contradiction: the other actual remainder forcing remains unconsumed. They are recorded as a precise additional necessary test, not as a source point or new localization to be imposed without its equations.

## 6. Manual controls and failed stronger readings

1. Integral sign control. For R=1, (C) gives [theta]N_R=-1/m, so Z_R(0)=m*a*(-1/m)+a=0. Reversing the sign in N_R instead gives Z_R(0)=2a, nonzero in any nonzero allowed algebra. It invalidates theta4 divisibility and the displayed left inverse. No numeric sample or coefficient program was used.
2. Retained-row control. Under the determinant-one transformation, the selected residual pair is exactly (ell+Kstar,Phi). Solving only ell=-Kstar leaves the second transformed residual Phi, whose vanishing has not been proved automatic. Thus the compatibility cannot be deleted on the strength of the pivot. This is an exact row identity, not an assertion that a point with Phi nonzero exists in the source.
3. Derivative-order control. In the changed polynomial-division object hbar=S^q and P=hbar^2, rem(P,hbar^2)=0 but rem(P',hbar^2)=2q*S^(2q-1) is nonzero in characteristic zero. Differentiating a remainder instead of the original polynomial loses information. All derivatives in this proof precede division; this control is not a source point.
4. Divisor-size control. The selected J0 coefficient has index4r+1, just below deg(hbar^2). Division only by hbar would not preserve that slot; this proof does NOT establish the same left inverse for a single-h remainder. Nor does it justify replacing hbar by its radical, assuming h squarefree, or discarding h-root collisions.
5. Changed-forcing control. Take the changed polynomial-division object hbar=S^q+t*S^(q-1), E0^0=S^(2q), with t an independent scalar. The original S^(2q-1) coefficient is zero, but rem(E0^0,hbar^2)=-2t*S^(2q-1)-t^2*S^(2q-2). The selected forcing becomes -2t. Thus preservation of a low-degree ell column does NOT mean preservation of its original full-row constant forcing. This is not a guarded relaxation or source point.
6. Guard/scope control. (D) uses the accepted unit a,H,b relations and the ENTIRE leading ODE, while section3 uses the ENTIRE reconstructed mate. Arbitrary leading cubics, leading-only B, or H=0 are different hypotheses. No g or u inversion appears, so their zero strata have not been suppressed. A failed attempt to prove emptiness is not evidence of nonemptiness, even after this exact reduction.

## 7. Verdict, read scope and stop

MANUAL CONSTRUCTIVE REFINEMENT AND DOUBLE-H TRANSFER, UNREVIEWED pending any separate FIRST review. Global ell unitness/elimination is KNOWN17zzh, not a new mechanism. The new limited content is the explicit formula(C), its actual remainder application, and the full quotient-forcing correction(I). There is NO_CLOSING_DISCRIMINATOR and no relaxation/source point in this report. No degree196/336 selection, actual r2 certificate, source closure, all-r nonexistence or JC2 consequence is supplied.

All six input reports were freshly read WHOLE after current pins matched, with no clipped reads. Only their assigned accepted propositions were imported, without following links or re-reviewing foundations. All new algebra is manual. No scientific subprocess/import/AST/syntax/compile/test/CAS, actual coefficient-body access, network/worker/process/Git/corpus/protected/shared/live-lane access occurred. Only documentary reads, hashing, owned apply_patch writes and the established artifact transaction were used.

## OPEN(S) RAISED

None new. The surviving quantity is the same double-h remainder unit problem, now expressed as J_reduced with all8r+3 possible slots and whole-leading guards. Its cheapest new prerequisite is independent hand verification of (C)-(H); evaluating or deciding the remaining ideal is unperformed, has unknown cost, and is not authorized here.

## COLLISIONS

status: EMPTY. Own targets were absent before begin; no old scientific or shared file was changed. Own whole/report/raised-OPEN review precedes the completion marker. No descendant, code instrument or execution is authorized. All writers will be IDLE after custody sealing.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17709`.
- Body SHA-256:
  `018c38810d654e4c59b392beacdd3c724d246986a1d1511739eb6027f5489010`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
