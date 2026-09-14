# FIRST gate: entire mixed-forcing attachment (ROOT 7ccbd830...)

Owner Fable 5.1 (claude-fable-5-1). First action 2026-09-12 18:56:29 UTC; own target ABSENT at first action. Reserve 19:10:00 UTC / HARD 19:13:00 UTC, never reset. MANUAL MATH / FIRST REVIEW / UNREVIEWED. Reviews only the formerly missing-input step of the September 11 FIRST; the leading presentation S_r stays imported at its prior tier.

Inputs, SHA-256 matched to the charged pins BEFORE a fresh WHOLE read (COORDINATION first): COORDINATION.md 33cfa610...; TASK.md dc9e3a27...; ROOT report f10-mixed-forcing-attachment-root-20260912.md 7ccbd830...; old FIRST f10-mixed-scalar-unit-gate-fable5-20260911.md aa8b0148.... Full digests are in the custody section. Nothing else was read; no code executed.

## Stipulated premises

Taken as hypotheses only, from TASK: m=3r+1, n=5r+2, r>=2; C monic cubic, D monic quintic, a,b,H units, mCD'-nC'D=-theta^7; the forms L_h; the kernel pairs (P,Q)=(P_-,Q_-), (R,S)=(P_+,Q_+) with deg P,R<=2, deg Q,S<=4, L_r(P,Q)=0, L_(r+1)(R,S)=-2e theta^6, e=[theta^2]R; the four explicit inverses with their exact polynomial divisibility; W as displayed. The identification of the explicit-inverse pairs with the L-kernel pairs is a TASK stipulation, not verified here and not needed for any verdict below.

## 1. Antiderivative identity (A) and (B): CONFIRMED

Notation a1=m-r, a2=m-r-1, b1=n-r, b2=n-r-1: CONFIRMED, with b1=4r+2, b2=4r+1, a1+a2=4r+1=3m-n, a1-2m=-b2, a2-2m=-b1.

Direct differentiation of E=-b2 PS/C^2-b1 RQ/C^2+2n DPR/C^3 gives ten monomial slots: P'S, PS' (-b2/C^2 each); R'Q, RQ' (-b1/C^2 each); C'PS (2b2/C^3); C'RQ (2b1/C^3); D(P'R+PR') (2n/C^3); D'PR (2n/C^3); DC'PR (-6n/C^4). Expanding W/C^2-2(R L_r(P,Q)+P L_(r+1)(R,S))/C^3-6theta^7 PR/C^4 with theta^7=nC'D-mCD': the L-sum equals mC(RQ'+PS')-b1C'RQ-b2C'PS+(a1+a2)PRD'-nD(P'R+PR'); so PS' gets (a1-2m)/C^2=-b2/C^2, RQ' gets (a2-2m)/C^2=-b1/C^2, P'S and R'Q keep -b2,-b1 from W, C'PS and C'RQ get +2b2,+2b1 over C^3, D(P'R+PR') gets +2n/C^3, D'PR gets (6m-2(a1+a2))/C^3 with 6(3r+1)-2(4r+1)=10r+4=2n, and DC'PR gets -6n/C^4. All ten slots match; no slot of E' is left over and no forcing term is missing. (A) CONFIRMED. Sign of theta^7: it enters (A) only through -6theta^7PR/C^4, consistent with the stipulated mCD'-nC'D=-theta^7; with the opposite sign the D'PR slot would read -2(a1+a2)-6m, which is not 2n, so (A) as written is tied to the stated sign.

Substituting L_r(P,Q)=0 and L_(r+1)(R,S)=-2e theta^6 gives W/C^2=E'-4e theta^6 P/C^3+6 theta^7 PR/C^4: CONFIRMED (the coefficient is -2*(-2e)=+4e on the left, moved right).

(B): integrate from 0 and multiply by C^2. [theta^7](C^2E)=2n[theta^7](DPR/C) since deg PS, deg RQ<=6: CONFIRMED (needs deg P,R<=2, deg Q,S<=4, now stipulated). C^2E(0) has degree 6: CONFIRMED. theta^6 P/C^3=P(0)theta^6/a^3+O(theta^7), integral P(0)theta^7/(7a^3)+O(theta^8), times C^2=a^2+...: coefficient P(0)/(7a): CONFIRMED. The theta^7 PR/C^4 integral starts at theta^8: CONFIRMED. Hence Gamma=(21a/(2H))(2n[theta^7](DPR/C)-4eP(0)/(7a))=(21an/H)[theta^7](DPR/C)-6eP(0)/H since 21*4/14=6: (B) CONFIRMED, derived independently of ROOT's text. Inversions used: a, H, 2, 7 only.

## 2. Modified inverse, R0/S0, numerator identities: CONFIRMED

With T=T_beta-(2e/7)theta^7 one has T'+2e theta^6=T_beta' and C'T=C'T_beta-(2e/7)theta^7 C', so R=R0+(2e/7)C' and S=S0+(2e/7)D' with R0=(CT_beta'/beta-C'T_beta)/theta^7, S0=(nDT_beta'/(m beta)-D'T_beta)/theta^7, beta=kappa_(r+1)/m: CONFIRMED. R0=R-(2e/7)C' is a polynomial of degree<=2 and S0=S-(2e/7)D' of degree<=4 because R,S are stipulated polynomials of those degrees and deg C'=2, deg D'=4: CONFIRMED; this is the exact replacement for the old FIRST's undisplayed degree assumptions, and it rests on the TASK's divisibility premise, not on a Laurent argument.

Numerators: theta^7(mCS0-nDR0)=nCDT_beta'/beta-mCD'T_beta-nCDT_beta'/beta+nC'DT_beta=(nC'D-mCD')T_beta=theta^7 T_beta, so mCS0-nDR0=T_beta; the same computation with T_alpha gives mCQ-nDP=T_alpha: both CONFIRMED as whole-polynomial identities (the T' terms cancel identically, no coefficient sampling). Consequently mCS-nDR=T_beta+(2e/7)(mCD'-nC'D)=T, matching the old FIRST. L_h(C',D')=mCD''+(m-n)C'D'-nC''D, which is the theta-derivative of the leading identity, =-7theta^6 for every h: CONFIRMED; hence L_(r+1)(R0,S0)=L_(r+1)(R,S)+2e theta^6=0, consistent with the stipulated modified row. Consistency of e: [theta^2]R0=e/7 and the leading coefficient of R0 is t7(7m-3kappa_(r+1))/kappa_(r+1)=t7/kappa_(r+1) because 7m-3kappa_(r+1)=1, so e=7t7/kappa_(r+1) exactly as TASK defines: CONFIRMED. alpha=kappa_r/m=2nu-1 and beta=kappa_(r+1)/m=4-nu: CONFIRMED (2m-r=n and 3m=2n-r-1 hold at m=3r+1, n=5r+2).

## 3. Cancellation and Gamma=21 lambda^14 B: CONFIRMED

From nDC'/C=mD'+theta^7/C: [theta^7](DPC'/C)=(m/n)[theta^7](PD')+[theta^0](P/C)/n=P(0)/(na), using deg(PD')<=6: CONFIRMED. Inserting R=R0+(2e/7)C' into (B): (21an/H)(2e/7)P(0)/(na)=6eP(0)/H cancels the correction exactly, with no division by e, P(0) or b: CONFIRMED. (C): nDPR0/C=mQR0-T_alpha R0/C, deg(QR0)<=6, so n[theta^7](DPR0/C)=-[theta^7](T_alpha R0/C); substituting R0/C=(T_beta'/beta-(C'/C)T_beta)/theta^7 gives [theta^14]((C'/C)T_alpha T_beta) minus [theta^14](T_alpha T_beta')/beta, and the latter is zero because deg T_alpha<=7, deg T_beta'<=6: CONFIRMED, every discarded term identified by degree.

Rescaling: C=a(1+u+Xu^2+Yu^3), u=lambda theta, lambda=H/a, X=aF/H^2, Y=a^2/H^3 (checked slot by slot), C'/C=lambda phi'(u)/phi(u), truncation through theta^7 equals truncation through u^7 since lambda is a unit and degrees are preserved, [theta^14]G(lambda theta)=lambda^14[u^14]G. So Gamma=(21a/H)lambda^15 B=21 lambda^14 B with B=[u^14](phi'/phi)trunc_7(phi^(2nu-1))trunc_7(phi^(4-nu)) in Q[X,Y] mapped into the algebra: CONFIRMED.

Whole-algebra scope: every step is a polynomial or theta-adic power-series identity whose only denominators are a, H, lambda=H/a (units by hypothesis), the rational numbers m, n, kappa_r=7r+3, kappa_(r+1)=7r+2, beta, 2, 7 (units in any Q-algebra), and C (invertible in the power-series ring because C(0)=a). (C/a)^s is the binomial series in C/a-1, which has zero constant term, so it converges theta-adically over any commutative Q-algebra, nilpotents included, and commutes with base change; the closed-form B is the image of a fixed element of Q[X,Y]. No reducedness, field factor, unitness of b, e, P(0), or of B is used. Legitimate inversions: a, H, lambda and rational constants; nothing else is inverted. CONFIRMED.

## 4. Does this close the old GAP BY ABSENCE? CLOSED at the stipulated tier; every other gap preserved

The old FIRST's gap was exactly: W, L_h, the four inverses and the modified formulas were not in its input, so the step from W to (4)=(B) and the insertion R L_r(P,Q)+P L_(r+1)(R,S)=-2e theta^6 P could not be checked, and deg P<=2, deg Q<=4 were recorded assumptions. TASK now displays all of these, and sections 1-3 verify the W-to-(B) step and the (B)-to-Gamma=21 lambda^14 B chain from them. Verdict: that missing-input step is CONFIRMED conditional on the WHOLE stipulated algebra (including the divisibility/degree premises and the identification of explicit inverses with kernel pairs). ROOT supplies nothing beyond TASK: no actual-source coefficient arrays, no unitness of B, no REG/model comparison, no source zero, no all-F10 statement, no JC2 bearing; its text states each of these as unproved, and this review preserves them. The old FIRST's section 6 (unit status of K_r(2nu-1) on S_r for actual r>=2) remains GAP, untouched. The leading presentation S_r is imported at its prior tier only.

## 5. Negative controls, traced independently: CONFIRMED with scope

- Sign of the P'S term of W flipped (-b2 to +b2), E and L_h fixed: the P'S slot of the comparison becomes +b2/C^2 against -b2/C^2 in E', residual 2b2 P'S/C^2 with b2=4r+1 a nonzero rational. The mutated general identity fails as a formal coefficient identity in the free coefficient algebra; this says nothing about whether 2b2 P'S/C^2 vanishes at an actual Keller point, where P'S might be zero. ROOT's scope statement is correct.
- Correction partner omitted: dropping the -4e theta^6 P/C^3 term (using L_(r+1)(R,S)=0) while inserting R=R0+(2e/7)C' leaves +6eP(0)/H; keeping the term but inserting R0 for R leaves -6eP(0)/H. Both residuals are nonzero formal elements (e and P(0) are free), but vanish at any point with eP(0)=0; no nonvanishing on components is claimed or needed.
- Leading-sign control (mine): with mCD'-nC'D=+theta^7 the section 3 step gives [theta^7](DPC'/C)=-P(0)/(na) and the correction doubles to -12eP(0)/H instead of cancelling; so the cancellation is tied to the stipulated sign, again formally.
- Limiting cube nu=5/3, X=1/3, Y=1/27: phi=(1+u/3)^3, 2nu-1=4-nu=7/3, phi^(7/3)=(1+u/3)^7 exactly, phi'/phi=(1+u/3)^(-1), integrand (1+u/3)^13, [u^14]=0: B=0 CONFIRMED. This point lies on d6=d7=0 of the nu-family (phi^(5/3)=(1+u/3)^5), but 3nu-5=1/m has no finite r solution at nu=5/3, so it is not an actual Keller point of any r; it forbids inferring all-parameter nonvanishing from generic nonvanishing and decides nothing about actual r.

Distinction kept throughout: the three algebraic controls are formal coefficient-identity failures; the cube is an exact zero at a non-actual parameter; neither is evidence about B at an actual Keller point.

## Verdict summary

(A) CONFIRMED; (B) CONFIRMED; R0,S0 polynomial with degrees <=2,<=4 CONFIRMED (from stipulated divisibility); mCQ-nDP=T_alpha, mCS0-nDR0=T_beta CONFIRMED; correction cancellation CONFIRMED; (C) CONFIRMED; Gamma=21 lambda^14 B over the whole commutative Q-algebra CONFIRMED with inversions limited to a, H, lambda, rationals; old missing-input step CLOSED at stipulated tier; unit status of B at actual r GAP (unchanged); actual-source, REG/model comparison, source zero, all-F10, JC2: not addressed, GAP preserved. No REFUTED item. No OPEN raised, no descendant, no charge_basis.

## Read scope and custody

Four charged inputs pinned (all four SHA-256 matched the expected values at 18:56:29 UTC), then read WHOLE: COORDINATION.md (806 lines, read in ranges after a display clip), TASK.md, ROOT report, old FIRST. No linked source, corpus, prior report, peer output, code or uncharged file read; no interpreter, CAS, network, git or process inspection; manual mathematics only. Writes: skeleton without marker, two bounded body patches, marker last, all via the installed apply_patch. Post-pins re-hashed after the final readback (see below).

Input digests (from sha256sum at first action):

- COORDINATION.md 33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597
- TASK.md dc9e3a27ed8e3052e89e598eb00cae060c9eaf3a5216c6a61b75bc0b0a3835f3
- f10-mixed-forcing-attachment-root-20260912.md 7ccbd83024c10b1d4d3fb898eda2c07abe429a5377db53f44895a6c2b02618b2
- f10-mixed-scalar-unit-gate-fable5-20260911.md aa8b0148f8bfb63ef072b23106f92bafa703a6b83033984e17a62f49eb70230f

Post-pins at 19:00:43 UTC: all four digests identical to the above. Own WHOLE readback at 19:00:43 UTC; collision check: xmodel holds only this report, its harness .log/.run.v2 sidecars, and ROOT's read-only report/artifact, none authored here. Marker appended after this line; no writes after completion.

<!-- BODY-END -->
