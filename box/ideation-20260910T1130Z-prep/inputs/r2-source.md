# Complete normalized F10 r2: a faithful 19-row source presentation

2026-09-10. NEW MANUAL CONSUMER, UNREVIEWED. First action 08:19:27.999558493 UTC; controlling stop 08:39:27.999558493 UTC, reserve from 08:36:27.999558493 UTC. Exactly the assigned card and its 20 accepted reports are charged. Zero scientific execution, coefficient arrays, executable source, or source outcome.

## 1. Result and exact perimeter

For r=2, m=7, n=12, the COMPLETE normalized, gauge-fixed 16r coefficient ring is isomorphic to the following finite presentation:

    B[s,s^-1][X1,X2,X3] / I19,                    (1)

where B is the WHOLE accepted degree-seven leading algebra, defined literally in section 2. The ideal I19 has exactly 19 specified scalar slots, including possible zero or dependent slots. Sections 3–8 give both maps and the finite reconstruction prescriptions; section 9 gives a polynomial envelope for every reconstructed coefficient and retained row. No s=1 specialization, selected embedding, generic coefficient inversion, or additional guard is used.

The accepted early, modified, middle and critical maps first give a 20-slot presentation with ell retained. The accepted late contact obstruction supplies a whole-base unimodular column, not an individually chosen unit entry. A NEW elementary r2 ell-column proof below then removes ell, retaining its companion compatibility. This last proof is independently derived from the charged 16r and leading-algebra formulas; root supplied a contemporaneous exploratory suggestion, not an accepted extra premise. The only endpoint claimed here is the complete normalized r2 system. No original physical degree, global source coverage, Keller map, source point, unit ideal, properness, dimension or runtime conclusion is made.

B is finite-etale of rank seven; at r2 the charged irreducibility theorem also makes it a field over Q. Its scalar extension can split. Neither fact implies that (1) is finite, reduced, nonzero or proper. All maps below remain exact after arbitrary commutative base change, including nonreduced algebras.

## 2. The full leading ring, with scale retained

To distinguish the original source variable S from its septic, use Z for the degree-seven coefficient coordinate. Put tau=2/7, nu=12/7 and define, by literal factored formulas,

    dL(Z)=12Z^2-12(1-tau)Z+(1+tau)(2-3tau),
    KL(Z)=-840Z^3+840(1-tau^2)Z^2
          +42(1+tau)(2+tau)(4tau-3)Z
          +2(2-3tau)(1+tau)(2+tau)(3+tau),
    gammaL(Z)=tau*((1+tau)(2+tau)(3+tau)
              -30(1+tau)(2+tau)Z+180(1+tau)Z^2-120Z^3),
    Sept(Z)=2KL^2-140tau(1+tau-6Z)KL*dL+245gammaL*dL^2.

Let P7 be Sept divided by its nonzero rational leading coefficient -245*120*144*tau. Then

    B=Q[Z]/(P7),   W=-KL/(210dL) in B,
    c(z)=1+z+Zz^2+Wz^3,
    t_i=[z^i]c(z)^nu,  dnu(z)=sum_(i=0)^5 t_i z^i.

These are finite prescriptions, not emitted or computed polynomials. The accepted septic reports prove dL, W and t5 units in the WHOLE B, and identify it with the guarded two-contact leading algebra. No new inverse guard is adjoined. Every B element or inverse has a unique representative of Z-degree at most six. None of their inverse representatives is calculated here.

The charged exact normalization gives the WHOLE leading ring

    L=B[s,s^-1],
    a=1/(W s^3), H=1/(W s^2), F=Z/(W s),
    b=1/(t5 s^5),
    C(theta)=a*c(s theta), D(theta)=b*dnu(s theta).

Thus C and D are monic of degrees 3 and 5 and

    7CD'-12C'D=-theta^7.                           (2)

The maps back are s=H/a, Z=Fa/H^2, W=a^2/H^3. All target factors match exactly, since ab*W*t5*s^8=1. The original guard is reconstructed as omega=1/(ab)=W*t5*s^8.

Why this applies to the actual 16r ring: its two top residual rows are [S^14]E1 and [S^16]E0. Its five upper leading equations already uniquely express D4,...,D0 from F,H,a, with fixed pivots 7j-36 for j=4,...,0. Quotienting by those two residuals and localizing ab therefore gives exactly the universal L of (2), not an extra assumption on a free coefficient ring. The normalization is an isomorphism of this leading ring. It does not set the scale in any full source to one.

## 3. The literal complete source and the reconstruction used throughout

Write hA for the coefficient polynomial, reserving h for a gap. The actual source data are

    d=d0+d1 S+F S^2,
    v=v0+v1 S+v2 S^2+v3 S^3+H S^4,
    k=k1 S+k2 S^2+k3 S^3+k4 S^4+k5 S^5+k6 S^6+a S^7,
    f=S d-u, hA=1-u d+S v,
    A=S t^3+f t^2+hA t+k,
    Pi=t-u t^2+S t^3,
    Delta=1+u t-ell*t*Pi-t*Pi^2.

The existing gauges remain k(0)=0, [S]B3=0, B0(0)=0. Set B5=S^2, B_j=0 for j>5, and reconstruct in order j=4,3,2,1,0:

    (j-3S*d/dS)B_j=Q_j,
    Q_j=delta_(j+2)-(j+1)f'B_(j+1)+2f B'_(j+1)
         -(j+2)hA'B_(j+2)+hA B'_(j+2)
         -(j+3)k'B_(j+3),                         (3)

where delta0,...,delta7 are respectively

    1, u, -ell, ell*u-1, 2u-ell*S,
    -u^2-2S, 2uS, -S^2.

Every nonresonant S^i coefficient is divided by the fixed rational j-3i. The two resonant coefficients vanish identically by accepted 16r; set their gauge coefficients to zero. This is the unchanged WHOLE mate, not a new collection of free B variables. It satisfies every upper Jacobian and complete inverse-polynomiality condition at all u and S, including zero, before the following two residual polynomials are imposed:

    E1=2k'B2+hA'B1-hA B1'-2f B0'-u,
    E0=k'B1-hA B0'-1.                             (4)

Their full S envelopes are 14 and 16. No coefficient of either polynomial is discarded except by one of the proved row replacements below.

For band bookkeeping only, theta=t/S^2. Let U_i,V_i be the ACTUAL gap-i polynomials in A and in (3), so A_(7-i)=S^(7-i)U_i and B_(12-i)=S^(12-i)V_i. For each gap h, define all mixed forcing by

    W_h=sum_(i+j=h; i,j>=1)
            ((7-i)U_i V_j'-(12-j)U_i' V_j).       (5)

Only earlier gaps enter. In particular V_j includes every earlier particular solution and every earlier literal target. Theta is homogeneous notation, not source localization or a permission to keep negative S exponents.

## 4. Early, modified and middle substitutions: no artificial Y4

For h=1,2 the actual triples are (d1,v3,k6) and (d0,v2,k5). Define

    L_h(U,V)=7CV'-(12-h)C'V+(7-h)UD'-12U'D.

The accepted prescribed-residual inverse Phi_h is the finite map: with kappa=19-h, alpha=kappa/7, R=R1 theta+R0 and rho,

    T=trunc_7[(C/a)^alpha*(rho+integral_0^theta R/(C/a)^alpha)],
    U=((7/kappa)C(T'-R)-C'T)/theta^7,
    V=((12/kappa)D(T'-R)-D'T)/theta^7.             (6)

The numerators are polynomial-divisible; only a and fixed rational units are inverted. Solve the five upper rows for V_part at U=0 and forcing W_h; set c_h=L_h(0,V_part)+W_h=c_h1 theta+c_h0. Use

    U_h=Phi_h(-c_h1,-c_h0,Y_h), h=1,2,
    V_h=V_lin(U_h)+V_part.

For h=3 use the separately accepted MODIFIED inverse, not (6) unchanged. Its source triple is q=-u, l=v1-uF, k4; kappa=16. Form Tbase by (6)'s truncation, q=7[Tbase]_7/16, T=Tbase-(2q/7)theta^7; replace T'-R by T'+2q theta^6-R in both numerators. This gives U=q theta^2+l theta+k4, u=-q, v1=l-Fq. Its actual target is -2q theta^6; include it in the homogeneous operator before constructing the particular residual. The free homogeneous read-back coordinate is Y3.

For every one of these steps the coordinate is rho=7a V_lin(0)-12b U0. The WHOLE constant from V_actual differs by 7a V_part(0). This difference is subtracted in the inverse map; no claim of vanishing is made.

The sole r2 middle gap is h=4. Its actual U is

    U=(v0-u*d1)theta+k3,

and its actual V has degree at most three. Use the auxiliary inverse (6) at kappa=15 with the complete W4. Write T7=H7 Y4+J4 with H7=[theta^7](C/a)^(15/7). The accepted irreducibility consequence makes H7 a unit of the whole L. Hence use Y4=-J4/H7, not an additional variable. Then U2=V4=0 exactly; recover v0=U1+u*d1 and k3=U0. This kills both middle rows. Its inverse recovers the uniquely forced Y4, using V_actual-V_part.

Uncomputed inverse qualification: H7=s^7*t7(15/7); the inverse of the second factor is an element of B whose existence is proved. It is not an exported coefficient list or a computed Bezout certificate. A future implementation must represent and verify that inverse over the complete basis of B before use.

## 5. Critical k2: corrected forcing and determinant-one replacement

At h=5 the actual A band is y theta+k2, y=1-u*d0; the B band has degree at most two, by B4 support and the unchanged [S]B3 gauge. Ell has not entered. Set

    N=-2theta^5-W5-y*(2theta D'-12D),
    N_i=-(W5)_i+(12-2i)y D_i, 0<=i<=4.           (7)

The theta^5 row is the accepted automatic identity. The y term uses D_i, NOT D_(i+1); only the separate k2 D' term shifts that index. With q2,q1,q0 the three V coefficients, solve

    q2=(10k2-N4)/7,
    q1=(8D4 k2-N3)/14,
    q0=(7H q2-7F q1+6D3 k2-N2)/21,
    r1=14a q2-14F q0+4D2 k2-N1,
    r0=7a q1-7H q0+2D1 k2-N0.

These are exactly E1[S^9],E0[S^11]. Write r=chi*k2+b5. The accepted finite functional

    Lambda(R)=F*[theta^6](C^2 integral R/C^2)
                  -(1/2)*[theta^5](C^2 integral R/C^2)
              =lambda1 R1+lambda0 R0

satisfies lambda1 chi1+lambda0 chi0=1 in L. Therefore replace

    k2=-lambda1 b5_1-lambda0 b5_0,
    Psi5=chi1 b5_0-chi0 b5_1=0.                  (8)

After substitution, the former pair equals (-lambda0,lambda1)Psi5. This determinant-one replacement is valid over arbitrary earlier-parameter quotients and retains every lower row.

## 6. Late k1: a full-base completion, not a chosen entry

At h=6 the varying A band is the constant k1. The varying B band has degree at most two; the ACTUAL fixed theta^3 coefficient is u^2 and belongs in the particular forcing. The target -u^2 theta^5 and the entire W6 are retained. For the homogeneous variation the operator is

    Llate(k,V)=7CV'-18C'V+kD',

with the three upper pivots -4,-11,-18. Let Vlin(1) be its unique upper solution and g=(g1,g0) the residual column. The two actual rows are E1[S^8],E0[S^10], of the form g*k1+b6. One safe definition of b6 is to set k1=0, apply the original full recurrence (3), and extract these two rows, after all preceding substitutions. Thus the fixed u^2 and every mixed term are included without an invented homogeneous-only recurrence.

Accepted 17v gives the equality of ideals

    (g1,g0)=(H6(13/7),H7(13/7)) in L.

At r2, the distinct exponents 12/7 and 13/7 lie in the exact 17w range. Accepted 17y excludes the guarded simultaneous contact algebra, including nilpotents. Under the exact leading normalization, this says the displayed ideal is L itself. Hence there exist lambda1,lambda0 in L with lambda1 g1+lambda0 g0=1. No particular g_i is asserted a unit.

A finite, whole-B specification of the witnesses is available without evaluating them. The homogeneity of the three upper rows gives g1=s^-3*gbar1, g0=s^-4*gbar0 with gbar_i in B. Reduce gbar_i to Z-degree at most six. Choose Bezout cofactors sigma1,sigma0, each reduced to degree at most six, satisfying sigma1*gbar1+sigma0*gbar0=1 modulo P7; fix them, for example, by ordered monic extended Euclid on (P7,gbar1,gbar0). Then lambda1=s^3*sigma1, lambda0=s^4*sigma0. Their existence is proved; their values are NOT computed here. The polynomial read-back must include the P7 cofactor, rather than a field-sample check. This is a prescription for proved unit-ideal completion, not division by an unknown generic entry.

For a fixed literal witness convention in this report, first perform formal monic extended Euclid on (P7,gbar1), then on (that monic gcd,gbar0), compose its cofactors and reduce sigma1,sigma0 modulo P7. A zero second input is skipped with the identity cofactor for the first; both barred columns cannot be zero. This specifies a deterministic finite rational prescription, not an executed calculation. Use the same ordered convention for the ell column below.

Replace k1=-lambda1 b6_1-lambda0 b6_0 and retain

    Psi6=g1 b6_0-g0 b6_1=0.                       (9)

The pair again becomes (-lambda0,lambda1)Psi6. This is a two-sided quotient map with determinant one. The remaining E1[0..7],E0[0..9],Psi5,Psi6 give the intermediate 20-slot ideal over L[Y1,Y2,Y3,ell]. Nothing about a full source solution has been decided.

## 7. NEW r2 ell-column elimination from the accepted leading D-unit

All preceding substitutions are independent of ell: its highest target term is -ell*S*t^4, at weight nine and gap seven, below gaps 1 through 6. A has no ell dependence and (3) is linear in the target, so the ENTIRE mate is affine in ell. At gap seven, A's new constant band is k(0)=0 by its original gauge. The ell-varying B band is S^5*Q(theta), deg Q<=2. Its upper equation is

    7C Q'-5C'Q=-theta^4+L1 theta+L0,
    Q=theta^2+(F/2)theta+gE,
    gE=(6H-F^2)/10,
    L1=14a+FH-10FgE,
    L0=(7/2)aF-5HgE.                              (10)

Direct coefficient comparison proves these formulas: the theta^4 pivot is -1; the next is -8 and gives Q1=F/2; the theta^2 row is 9H-(3/2)F^2-15gE=0. The theta^1 and theta^0 coefficients are exactly the displayed L1,L0. The source row positions are E1[S^7],E0[S^9]. No higher B coefficient varies with ell; the three relevant pivots are nonresonant. The actual affine constants b7 are defined by setting ell=0 in the WHOLE recurrence after the previous substitutions and extracting those rows. All forcing is thereby retained.

Claim: (L1,L0)=L. Work in its quotient and compute the polynomial identity

    7a L1-2H L0=98a^2+(10H^2-70aF)gE.            (11)

The right side shows that gE is a unit in the quotient, since a is. Put beta=5/7. Equation (10) there is 7C Q'-5C'Q=-theta^4. Formal integration at theta=0 gives

    Q/gE=(C/a)^beta+O(theta^5).

Since deg Q=2, both [theta^3](C/a)^beta and [theta^4](C/a)^beta vanish. Under C/a=c(s theta), the unit s cancels, giving t3(beta)=t4(beta)=0. The finite hand identities are

    t3(beta)/beta=W+(beta-1)Z+(beta-1)(beta-2)/6,
    t4(beta)/(beta*(beta-1))
       =W+Z^2/2+(beta-2)Z/2+(beta-2)(beta-3)/24,
    24*(t4/(beta*(beta-1))-t3/beta)
       =12Z^2-12beta Z+(beta-2)(1-3beta)=dL(Z),   (12)

because beta=1-tau. All scalar denominators are nonzero rationals. But dL is already a unit of B and of every L-algebra. Thus this quotient is zero, proving the claim with no field, reducedness, positivity or chosen-embedding assumption. This NEW r2 proof uses only accepted leading identities; it does not import another live theorem or extrapolate its conclusion to every r.

As in section 6, L1=s^-3*Lbar1, L0=s^-4*Lbar0. Choose whole-B Bezout witnesses for the barred column, giving a left inverse lambda of the unbarred column. Existence is now proved, but no cofactor array is exported. For r=(L1,L0)*ell+b7, replace

    ell=-lambda1 b7_1-lambda0 b7_0,
    Psi7=L1 b7_0-L0 b7_1=0.                       (13)

Both directions follow from the SAME determinant-one matrix identity. Every lower residual receives this substitution. This is not a fixed-A failure or an exclusion: the column is everywhere solvable for one linear combination, and a real compatibility remains.

## 8. Exact retained indices, variables and two-sided maps

Here is the entire scalar-row accounting, before the harmless row-unit rescalings in section 9. Each entry names BOTH original residual slots, not a band representative alone.

| gap | coefficients replaced | E1 index | E0 index | output |
|---|---|---:|---:|---|
| leading | F,H,a and original guard in L | 14 | 16 | B[s,s^-1] |
| 1 | d1,v3,k6 | 13 | 15 | Y1 |
| 2 | d0,v2,k5 | 12 | 14 | Y2 |
| 3, modified | u,v1,k4 | 11 | 13 | Y3 |
| 4, middle | v0,k3 | 10 | 12 | no variable, no row: H7 unit |
| 5, critical | k2 | 9 | 11 | Psi5 |
| 6, late | k1 | 8 | 10 | Psi6 |
| 7, ell | ell | 7 | 9 | Psi7 |

Thus the first complete final form is

    L[Y1,Y2,Y3] /
       ( E1[S^0],...,E1[S^6],
         E0[S^0],...,E0[S^8], Psi5,Psi6,Psi7 ),     (14)

where EVERY entry is evaluated after all ordered back-substitutions above. There are 7+9+3=19 slots. Zero or dependent entries remain explicitly named slots; no independence assertion is made. Original 32 residual slots lose the two leading slots, six early/modified slots and two middle slots; each of the remaining three two-row replacements loses exactly one slot: 32-2-6-2-3=19. The original guard is represented by omega=W*t5*s^8, not dropped. Ell is not silently gauge-fixed; (13) is its proved elimination with an additional retained equation.

Forward reconstruction from (14): form C,D from Z,s; apply gaps 1,2,3 in order with the complete actual W; eliminate gap 4 using its proved unit; compute (8), then (9), then (13), carrying every particular term. Reconstruct all d,v,k,u,ell and the complete B through (3). All discarded original rows read back either to zero identically or to the displayed determinant-one multiple of Psi5, Psi6 or Psi7. The other 16 original residual slots are literally retained. The full inverse-polynomiality conditions and fixed gauges follow from the SAME unchanged 16r formulas, not from an ordinary receiver-only point.

Conversely, a point of the complete normalized 16r ring determines its unique leading Z,s and omega. Read U1,U2,U3 successively and take their HOMOGENEOUS rho, subtracting 7a V_part(0) if using the actual band constant. The accepted two-sided inverses recover precisely Y1,Y2,Y3. The middle unit forces its unique Y4, and the determinant-one identities force precisely k2, k1 and ell as reconstructed. The retained compatibilities and lower coefficients vanish. Every original generator is recovered, and conversely every generator of (14) is recovered. These are quotient-ring identities over Q with the stated units, not only bijections on reduced points or a finite cover.

No arbitrary ideal row combination has been substituted for a missing source equation. The actual forcing, rather than an invented homogeneous forcing, enters each b-vector. Source support ensures the ell-band forcing has no theta^5 term: at weight nine any ordinary theta^5 contribution would require a negative S exponent. Its three remaining upper rows and two low rows therefore exhaust that band. At gap six, in contrast, the fixed u^2 theta^3 term genuinely occurs and cannot be discarded.

## 9. A smaller finite polynomial envelope, without s=1

The following invertible coefficient change supplies a useful exact artifact envelope for (14). It is NEW bookkeeping derived here; no uncharged r1 scale theorem is used. Set

    vartheta=s*t,  z=s^2,
    U=s*u, Dpar=s*d, Vpar=s^2*v, Kpar=s^3*k,
    E=s^3*ell,
    Ahat(S,vartheta)=s^3*A(S,vartheta/s),
    Bhat(S,vartheta)=s^5*B(S,vartheta/s),
    X_i=s^8*Y_i, i=1,2,3.                         (15)

The symbol z in this section is a coefficient parameter used to describe a finite polynomial envelope; it is NOT the physical inverse-chart coordinate and is ultimately s^2. No free specialization of z or s is a source operation. Explicitly,

    Ahat=S*vartheta^3+(S*Dpar-U)*vartheta^2
              +(z-U*Dpar+S*Vpar)*vartheta+Kpar,
    Pihat=z*vartheta-U*vartheta^2+S*vartheta^3,
    [Ahat,Bhat]=s^7+U*s^5*vartheta
                    -E*vartheta*Pihat-vartheta*Pihat^2. (16)

The bracket scales by s^7: the t derivative contributes s^-1, while the two outputs contribute s^3 and s^5. In particular the two low targets are s^7 and U*s^5, not constants silently normalized to one.

The leading polynomials now have coefficients in B alone:

    Cbar=c(theta)/W, Dbar=dnu(theta)/t5,
    abar=Hbar=1/W, Fbar=Z/W, bbar=1/t5.

Here theta=vartheta/S^2 for band extraction. Normalized U-band coefficients are s^(3-i) times the old theta^i coefficients; normalized V-band coefficients are s^(5-i) times the old ones. Therefore each homogeneous rho is multiplied by s^8, proving the X_i formula in (15), INCLUDING the particular-constant subtraction. Normalized residual coefficient pairs are (s^6*r1,s^7*r0). Each normalized column is (s^3*column1,s^4*column0), so its determinant compatibility is exactly

    Psihat_h=s^10*Psi_h, h=5,6,7.                 (17)

The column witnesses can consequently be chosen in B for the normalized problem. The critical functional has that property directly; for late and ell use the full-B Bezout prescriptions above. They are constants with respect to every earlier parameter. They need not be single unit entries.

Assign positive weights

    wt(X1)=1, wt(X2)=2, wt(X3)=3, wt(z)=5,
    wt(S)=1, wt(vartheta)=2.                       (18)

Before eliminating E assign wt(E)=7. The normalized source coefficient weights are

    wt([S^i]Dpar)=2-i,
    wt([S^i]Vpar)=4-i,
    wt([S^i]Kpar)=7-i,
    wt(U)=3.

These are homogeneous weights, not generic exact nonzero degrees. A zero coefficient satisfies every stated envelope. To prove the assignments after reconstruction: the leading coefficients are in B; at gap h, the full mixed W is homogeneous of weight h because it is a sum of earlier gap-i and gap-j terms with i+j=h. The finite inverse maps have coefficients in B and are linear in their residuals/rho. Thus gaps 1,2,3 produce weight-1,2,3 coefficients. At gap 4 the shift U*[S]Dpar has weight 3+1=4 and H7bar is a B-unit; its solution has weight four. At gap 5 the coefficient y is z-U*[S^0]Dpar of weight five, the target is -2z*theta^5, and the determinant-one reconstruction gives [S^2]Kpar and Psihat5 of weight five. At gap 6 the fixed Bhat3(0)=U^2 and target -U^2 theta^5 have weight six; the whole affine solution and Psihat6 have weight six. At gap 7 the ell target and all mixed forcing have weight seven, so E and Psihat7 have weight seven. No earlier-variable division is used at any step.

Consequently, AFTER E is eliminated, every reconstructed coefficient lies in B[X1,X2,X3,z], not an unbounded rational function ring in these variables. The only inverses used are constants of B. Both Ahat and Bhat are weighted homogeneous of weights 7 and 12. One way to check Bhat is to grade the original Euler recursion: the upper target -E*vartheta*Pihat-vartheta*Pihat^2 has weight 16 since Pihat has weight seven. The inhomogeneous targets s^7 and U*s^5*vartheta occupy only t^0,t^1 and never enter the five upper inversions. The fixed zero gauges preserve homogeneity.

This proves the following COMPLETE finite envelopes. For j=0,1,2,3,

    deg_S Ahat_j <= 7-2j;
    [S^i]Ahat_j is homogeneous of coefficient weight 7-i-2j.

For j=0,1,2,3,4,5,

    deg_S Bhat_j <= 12-2j;
    [S^i]Bhat_j is homogeneous of coefficient weight 12-i-2j. (19)

Thus the S-degree lists are (7,5,3,1) and (12,10,8,6,4,2). They include the forced Bhat5=S^2 and Ahat3=S. The complete Jacobian has coefficient bound deg_S[t^j]<=16-2j for j=0,...,7: 80 potential scalar slots, not an asserted nonzero count. The original A,B are recovered by multiplying their jth t coefficients by s^(j-3), s^(j-5) respectively.

Define polynomial K0_i,K1_i in B[X1,X2,X3,z] by extracting [S^i*vartheta^0] and [S^i*vartheta^1] of

    [Ahat,Bhat]+E*vartheta*Pihat+vartheta*Pihat^2.

Their weights are 16-i and 14-i. The FINAL literal version of I19 in (1) is, with z=s^2 in every entry,

    Psihat5, Psihat6, Psihat7;
    K1_1,...,K1_6;  K0_1,...,K0_8;
    K1_0-U*s^5;  K0_0-s^7.                       (20)

The count is 3+6+8+2=19. Equation (20) is precisely (14) multiplied by units, by (16)-(17), not a different lower-target system. Its two-sided map to (14) is X_i=s^8 Y_i and Y_i=s^-8 X_i. S and the Laurent scale s are distinct throughout.

For an explicit finite coefficient inventory, every homogeneous polynomial of weight w in (18) is supported on

    X1^a1 X2^a2 X3^a3 z^d,
    a1+2a2+3a3+5d=w, all exponents nonnegative,    (21)

with each coefficient uniquely in the seven-dimensional basis 1,Z,...,Z^6 of B. This inventory bounds every reconstructed coefficient via (19), the three compatibilities via w=5,6,7, and every K row via w=14-i or 16-i. It allows zero polynomials and all coefficient cancellations. In particular all these objects have ordinary polynomial degree at most their stated weight, at most 16 for the retained K rows; no coefficient-height or timing bound is asserted. Substituting z=s^2 changes (21) to the exact finite exponent envelope a1+2a2+3a3+5d=w with s-exponent 2d. The separate low target monomials s^7 and U*s^5 must also be present; the latter uses U of weight three and is NOT merged with K1_0's homogeneous envelope.

If a purely polynomial Q-presentation is desired, use variables Z,s,sminus,X1,X2,X3 with the two additional rows P7(Z),s*sminus-1, and the 19 rows (20), reducing all B constants to degree at most six. No extra omega or inverse-variable proliferation is necessary. This is 21 named relation slots in six variables, not a finite-dimensionality assertion. The Laurent presentation (1) is the smaller natural interface.

## 10. Honest implementation boundary and changed-object checks

No generator or checker is written or run. The smallest faithful next implementation is only the finite recurrences and coefficient inventories above: the degree-seven leading algebra, its verified inverse constants, seven ordered band substitutions, the unchanged full Euler mate, and all 19 rows. It must not be replaced by a same-degree receiver, a leading-contact test, or a source with s=1. No new solver, registration, budget or run is authorized here.

Before any actual use, an independent identity checker must verify, in the COMPLETE B basis: P7 and normalization read-back; every inverse used (dL,W,t5,H7bar and the late/ell column completions); each two-sided band map with the actual particular forcing; all original 32 residual coefficients and omega*ab-1 after reconstruction modulo the 19 rows; and the unchanged full inverse-polynomiality/gauge conditions. The full Jacobian envelope has the 80 slots just listed. Neither quotient dimension nor degree of B substitutes for those identities. All inverse coefficients and emitted rows remain uncomputed. Their existence has been proved where used; no fresh certificate or verification PASS is minted here.

Manual changed-object controls:

1. Set a prescribed particular forcing to the constant 1 in an early operator. Its homogeneous kernel alone leaves residual 1; the affine inverse with prescribed constant -1 is necessary. This is a changed forcing, not a source point, and tests retaining every V_part in (5).
2. Replacing v0-u*d1 by v0 changes the actual S*t coefficient by u*d1. Taking those two earlier coefficients formally as 1 makes the change nonzero; it is not a licensed relation on the full source.
3. The critical y term at i=0 is 12*y*b. Replacing D_i with D_(i+1) changes this to 12*y*D1 while leaving the homogeneous k-column test blind to the error. The indexed forcing must be checked separately.
4. The late j=0 extension is false: it is the original A-constant gauge, with a zero column and coincident contact exponents. Here only j=1, nu=12/7, alpha=13/7 is used. At j=1 the fixed theta^3 coefficient u^2 still belongs to the ACTUAL affine term, not to its degree-two variation.
5. For any of the three column completions, deleting its compatibility while imposing only the scalar-variable back-map leaves the residual vector (-lambda0,lambda1)*Psi. Its column is unimodular because the determinant is one; it is not the zero vector. A changed prescribed affine vector equal to this column times 1 passes the chosen scalar coordinate but fails the full pair. This is an operator control, not an exhibited complete source point.
6. In the ell proof, the upper target coefficient is -1 at theta^4, giving Q2=1. Deleting that target makes the homogeneous fixed-A ell variation zero and removes (10)-(12); the D-unit contradiction is not a statement about zero forcing. The two distinct indices t3,t4 are essential to (12), not an unproved extra t6/t7 contact.
7. Source-scale control: the full transformed low equations are K0_0=s^7 and K1_0=U*s^5. Replacing them by 1 and U with arbitrary s discards their exact factors. Likewise Psihat=s^10*Psi, not Psi without its row-unit accounting. The proof keeps these equalities before using the fact that s is a unit.
8. A finite coefficient field and unit column do not imply a finite/proper source quotient. Abstractly B[X] is not finite over B, and a single affine equation with unit coefficient solves for its variable without excluding a point. This prevents interpreting any eliminated contact exception or ell column as a full-source obstruction.

## 11. Scope, documentary completeness and stop

Verdict: a NEW complete r2 transfer with 19 retained slots, three free band coordinates and the unremoved Laurent scale is proved manually from the assigned accepted inputs, with the independently proved r2 ell-column lemma. It remains UNREVIEWED. No useful full-source residual has been set to zero by convention; no original physical-map or global-coverage inference is charged. A full-source decision and the concrete cofactor/row identities remain uncomputed.

First card and all 20 named reports matched their current SHA256 before bodies. The 20 accepted bodies were read whole through bounded reads and continuation reads; early aggregate output truncation was repaired or covered by explicit same-byte prior WHOLE reuse (the accepted early-tower gate). The corresponding read-scope and exact current pins are owned documentary artifacts. No provenance path, uncharged report, ledger, code, data, network, other lane, current review, process or protected project was accessed. Only manual mathematics, documentary metadata, apply_patch and the existing publication transaction were used.

## OPEN(S) RAISED

None new. The exact remaining quantity is whether the full quotient (1), with ALL 19 rows (20), is zero. The cheapest prerequisite to an honest decision is independently checked finite reconstruction and inverse read-back over the full B basis, not a new contact test or a computed sample. Cost, coefficient heights and outcome are unknown; this is not an execution registration or a follow-on invitation.

## COLLISIONS

status: EMPTY

- NONE — owned targets absent at first action; own-only check, no corpus scan. The original accepted files and all shared/canonical state remain unchanged.

Own WHOLE derivation/read-scope/input-list review is complete; the final witness-convention addition was reread before the completion marker. No mathematical action, implementation, or open writer remains after transactional publication.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `30451`.
- Body SHA-256:
  `f1f50b286aa90ec67929d84a7dce23328b410369d176adf4bbfdc3537a96e1c8`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
