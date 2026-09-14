# FIRST mixed-scalar gate and unit test: bounded manual review

Owner Fable 5.1 (claude-fable-5-1). First action 2026-09-11 14:14:44 UTC; both own targets ABSENT at first action. Publication reserve 14:27:00 UTC / HARD 14:30:00 UTC, never reset. MANUAL MATH / FIRST REVIEW / UNREVIEWED.

Sole scientific input: /tmp/jc2-lane.8kHBa2/inputs/f10-mixed-kernel-scalar-astra-20260911.md, SHA256 f6fe0986808f697e5e437af7f40ae5064cb609c92887a42a10963e91d09191c8, matched the charged pin BEFORE a FRESH WHOLE read; one display clip (section 3 through the start of section 4) was recovered by line range and read in full. No TASK, prior report, corpus, peer report or code was read.

## Stipulated premises

Accepted as hypotheses only: the leading identity mCD'-nC'D=-theta^7, units a,b,H, the degrees deg C=3, deg D=5, monicity of C and D, and the two normalized inverse pairs with mCQ-nDP=T_alpha. The producer's reduction, its degree bookkeeping and its unit implications are gated below, not assumed.

## 1. Parameter bookkeeping: CONFIRMED

The four displayed relations alpha=2nu-1, beta=4-nu, 5m-3n=-1 and 3nu-5=1/m are mutually consistent and force (n,m)=(5r+2,3r+1): alpha+beta gives n+3m=14r+5, the difference gives 3n-5m=1, whence m=3r+1, n=5r+2. Then nu-5/3=1/(3m)>0 and nu(2)=12/7, decreasing in r, so 5/3<nu<=12/7<2 for every r>=2. Also alpha+beta=nu+3, the symmetry used in section 6.

## 2. Entire-forcing cancellation (producer section 2)

- Identity (3) and the L-values: GAP BY ABSENCE. W, L_k, the four inverse polynomials and the "given modified formulas" are not displayed in the input, so (3), the insertion R*L_r(P,Q)+P*L_(r+1)(R,S)=-2e*theta^6*P and the passage to (4) cannot be verified here. Internal consistency does hold: with R=R_0+(2e/7)C', S=S_0+(2e/7)D' one gets mCS_0-nDR_0=T_beta exactly (the CDT_beta' terms cancel, the leading identity supplies T_beta), hence mCS-nDR=T_beta-(2e/7)theta^7; differentiating the leading identity gives (m-n)C'D'+mCD''-nC''D=-7theta^6, which is the producer's L_h(C',D') value only if L_h is that bilinear form, not displayed.
- [theta^7](DPC'/C)=P(0)/(na): CONFIRMED from nDC'/C=mD'+theta^7/C and [theta^7](PD')=0, which needs deg P<=2 (deg D'=4). deg P<=2 is not stated in the input; it matches the displayed deg R_0<=2 and is recorded as an assumption.
- Cancellation of -6eP(0)/H: CONFIRMED given (4): (21an/H)(2e/7)P(0)/(na)=6eP(0)/H; no division by e or P(0).
- n[theta^7](DPR_0/C)=-[theta^7](T_alpha R_0/C): CONFIRMED from mCQ-nDP=T_alpha, needing deg(QR_0)<=6, i.e. deg Q<=4 (not displayed; assumption).
- -[theta^7](T_alpha R_0/C)=[theta^14](C'/C)T_alpha T_beta: CONFIRMED; the dropped T_alpha T_beta'/beta has degree <=13.
- Scale exponent: CONFIRMED. With u=lambda theta, C'/C=lambda phi'/phi and [theta^14]G(lambda theta)=lambda^14[u^14]G, so [theta^14](C'/C)T_alpha T_beta=lambda^15 B_r and Gamma=(21a/H)lambda^15 B_r=21 lambda^14 B_r because a/H=1/lambda. Truncation through degree 7 commutes with the scaling.

Net: the chain from (4) to (1) is CONFIRMED under the undisplayed degree bounds deg P<=2, deg Q<=4; the step from the stipulated forcing W to (4) is a GAP for this review because its inputs are not in the charged file.

## 3. Presentation and guards (producer section 3): CONFIRMED

Monicity: aY lambda^3=1 and b lambda^5 d_5=1, so lambda,Y,d_5 are units; lambda=H/a, X=aF/H^2, Y=a^2/H^3 follow from C=a+H theta+F theta^2+theta^3. Identity (5): C=a phi(u), D=b d(u) give m phi d'-n phi' d=-u^7/(ab lambda^8)=-Y d_5 u^7 since ab lambda^8=1/(Y d_5). Forward: (d/phi^nu)'=phi^(-nu-1)(m phi d'-n phi' d)/m vanishes mod u^7, so d=phi^nu mod u^8 and d_6=d_7=0. Converse: with d=trunc_(<=5)phi^nu the left side of (5) has degree <=7 and u^7 coefficient 5mYd_5-3nYd_5=(5m-3n)Yd_5=-Yd_5. Reconstruction maps agree. The three literal cubics d_5,d_6,d_7 were re-derived term by term from the multinomial formula (5, 7 and 8 terms; e.g. (nu)_4/6=4c_4, (nu)_5/12=10c_5, (nu)_3/2=3c_3). All CONFIRMED.

## 4. Finite formula and envelope (producer section 4): CONFIRMED

b_k(s)=[u^k]phi^s and ell_k=[u^(k-1)]phi'/phi follow from phi=1+v, v=u+Xu^2+Yu^3, with p=k-i-2j, l=k-2i-3j; sign and factorial in ell_k come from log(1+v)=sum(-1)^(p-1)v^p/p, the factor k from differentiation. (6) is the Cauchy product, indices 15-i-j in [1,15]. Weights (L,X,Y,u)=(1,2,3,-1) make phi weight 0 and phi'/phi weight 1, so [u^14] has weight 15 and 2i+3j<=15 gives ordinary degree <=7. Factors (7): T_1=phi, T_2=phi^2 (degree 6, exact), integrand degrees 9 and 12 below 14; factor theorem in Q[nu,X,Y] with four distinct rational roots. nu-degree <=14 since b_i(alpha) has degree i. All CONFIRMED.

## 5. Changed-parameter control (producer section 5): CONFIRMED

phi=(1+u/3)^3 gives X=1/3, Y=1/27, phi^(5/3)=(1+u/3)^5, d_5=3^-5, d_6=d_7=0, alpha=beta=7/3, T_alpha=T_beta=(1+u/3)^7 exactly, phi'/phi=(1+u/3)^-1, product (1+u/3)^13, u^14 coefficient zero. Not an actual r (3nu-5=0).

## 6. Unit question on the whole algebra: GAP, with an exact reduction

Criterion. S_r is a finitely generated Q-algebra, hence Jacobson, so an element is a unit iff it lies in no maximal ideal iff it vanishes at no Qbar-point of V(d_6,d_7) outside V(Y d_5). Nilpotents and embedded components therefore never change unitness, and an "exact actual-r zero component" means exactly a Galois orbit of such points on which B_r vanishes. The whole-algebra verdict is a closed-point statement, still exact, never a generic one.

ROOT's six roots: CONFIRMED, and they reduce but do not decide. B_s=[u^14](phi'/phi)T_s T_(nu+3-s) is symmetric under s<->nu+3-s. B_1=B_2=0 for every phi (degrees 9 and 12), hence B_(nu+2)=B_(nu+1)=0 for every phi by the symmetry; these are the producer's four factors in the s-variable. Extra pair on d_6=d_7=0: T_nu=d, T_3=phi^3-u^8(3XY^2+Y^3 u) ([u^8]phi^3=3XY^2, [u^9]=Y^3), and (5) rewritten is nu*d*phi'/phi=d'+Y d_5 u^7/(m phi), which is ROOT's displayed relation since 3nu-5=1/m. Then B_3=[u^14](phi' phi^2 d)-[u^6]((3XY^2+Y^3 u)(phi'/phi)d); the first term has degree 13, and the second equals (1/nu)(3XY^2[u^6]d'+Y^3[u^5]d') plus a u^7-supported term out of range, all zero because deg d'=4. So B_3=B_nu=0 on S_r. Leading coefficient: ell_1=1 and b_7(s) leads with s^7/7!, so B_s leads with -(7!)^-2 s^14. The six roots 1,2,3,nu,nu+1,nu+2 differ pairwise by nonzero rationals (nu in (5/3,12/7]), so the factor theorem over S_r[s] applies repeatedly and

    B_s = -(7!)^-2 (s-1)(s-2)(s-3)(s-nu)(s-nu-1)(s-nu-2) K_r(s),

with K_r of s-degree 8 and coefficients in S_r. At the actual s=2nu-1 the six linear factors are the nonzero rationals 2(nu-1), 2nu-3, 2(nu-2), nu-1, nu-2, nu-3, so B_r is a unit in S_r iff K_r(2nu-1) is. This corrects the producer's removable count from four to six factors on the reduced algebra, but K_r(2nu-1) is a specific polynomial of ordinary degree <=7 in X,Y whose vanishing at the closed points of V(d_6,d_7) I could not settle by hand in the window.

What a decisive test is. V(d_6,d_7) is the intersection of two plane cubics; if they share no component it has at most 9 Qbar-points, and the exact test is the resultant of d_6,d_7 in one variable followed by evaluation of K_r(2nu-1) (or of B_r via (6)) at those roots away from Y d_5=0. Whether the two cubics are coprime for actual nu is itself undecided here; a common component would be a positive-dimensional exact component, on which the same closed-point criterion applies. The only point on V(d_6,d_7) I can name for any nu is the perfect-cube point X=1/3,Y=1/27 at nu=5/3, where phi^nu is a polynomial; for actual r, 3nu=5+1/m is never an integer, so that mechanism produces no actual point, but that excludes nothing else.

VERDICT: unit status of B_r on S_r for r>=2 is a GAP. Neither a unit nor an exact zero component is proved. No generic-nonzero, one-factor or sample claim is substituted.

## Consumer and read scope

For the proposed comparison of the actual highest block with a regular rational-power model, this review passes only the presentation and the (4)-to-(1) chain under the two recorded degree assumptions; the scalar unit needed by that comparison is not supplied, so the comparison is not licensed on any component by this review. Nothing here bears on a potential, REG, source zero, all-F10 or JC2 result. No computational task, OPEN ID or descendant is created.

Read scope: the charged file was pinned, then read WHOLE (159 lines, 11457 bytes; the clipped range was recovered and read); nothing else was read. Manual math, static text and hashes only; no subprocess, CAS, code, network or peer access; input unmodified, post-pin hash identical. COLLISIONS: own targets absent at first action; at the final check xmodel holds only this report plus the harness .log and .run.v2 files of this lane (created 14:14 UTC, not authored here), and the box directory is still absent. Own final WHOLE re-read done; the six-root factorisation and the section 2 coefficient identities were re-derived a second time as the cheapest quantity tests.

<!-- BODY-END -->
