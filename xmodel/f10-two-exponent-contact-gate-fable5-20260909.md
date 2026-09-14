# FIRST gate: two-exponent cubic exceptional-algebra reduction (producer f10-two-exponent-contact-discriminator-astra-20260909)

2026-09-09. Gate lane fable5. First action 21:01:17 UTC; controlling stop 21:18:00 UTC (earlier than launch+18 min). Charged inputs: exactly the five ordered SHA256 pins in the lane brief, all five verified byte-identical before any read. Sole scientific premise: the accepted 16l producer (12982 bytes, 38cf3fb9...); the producer under review is the 303-line WHOLE (18506 bytes, 4bbecd35...). ZERO mathematical subprocesses; every derivation below is manual. No Seal, no charge_basis.

## 0. Verdict table

| Item | Verdict | Smallest actual defect |
|---|---|---|
| A literal H6/H7, u-normalization, A_X,B_X,P_X,Q_X, 24(A-B)=P+QW | CONFIRMED | none mathematical; see F1 (label only) |
| B Bezout identity (12), Gamma>0 (13), ideal identity (16), deg W=3, [V^4]E=48d(s-3), monic quartic M | CONFIRMED | none |
| C F0,F1, formula (21), R1/R0, degree cancellations, isomorphism (23) | CONFIRMED | cross-reference "(20)" at line 195 points at an unnumbered display (line 180) |
| D (25),(26),(27), J3 monic cubic, Z0,Z1, isomorphism (29), dim 0..3, gcd|W^3, field degree<=3 | CONFIRMED | none |
| E six controls; uniform emptiness | controls CONFIRMED; uniform existence/nonexistence GAP (as the producer states) | none; the r=2,j=1 gcd test is unexecuted and unauthorized |

The new result is an EXACT reduction of the four-row two-exponent contact system to the guarded cubic algebra (29). It is not an emptiness proof and no source/Keller/JC2 conclusion or global rank change follows. READ-SCOPE's word "quartic" is superseded by section 6A's cubic; custody.json scope already says "final monic cubic", so the two owned metadata files disagree only in READ-SCOPE's older wording.

## A. Literal 16l H6/H7, normalization, A_X/B_X/P_X/Q_X recomputation

Source check. 16l lines 143-147 give f_6(1,v,w), f_7(1,v,w). I re-derived them from the partition formula f_N = sum_{i+2j+3l=N} (a)_{i+j+l} u^i v^j w^l/(i!j!l!) at u=1. N=6 partitions (6,0,0),(4,1,0),(2,2,0),(0,3,0),(3,0,1),(1,1,1),(0,0,2) give (a)_6/720, (a)_5 v/24, (a)_4 v^2/4, (a)_3 v^3/6, (a)_4 w/6, (a)_3 vw, (a)_2 w^2/2. N=7 partitions (7,0,0),(5,1,0),(3,2,0),(1,3,0),(4,0,1),(2,1,1),(0,2,1),(1,0,2) give (a)_7/5040, (a)_6 v/120, (a)_5 v^2/12, (a)_4 v^3/6, (a)_5 w/24, (a)_4 vw/2, (a)_3 v^2 w/2, (a)_3 w^2/2. Producer (4) matches term by term with (X)_k for a_k.

Parameter range. 3n-5m = 3(5r+2)-5(3r+1) = 1 and m = 3r+1 = 3(r-1)+4 with q=r-1>=1, so x = n/m is exactly the 16l exponent a=(5m+1)/(3m). x-5/3 = 1/(3m). n+j <= 6r+1 < 6r+2 = 2m gives y<2. Hence 5/3<x<y<2, d=j/m>0, s>10/3, s-3>1/3, and x(x-1), y(y-1), x-2, y-2 are nonzero rationals. Every division in the producer is by one of these or by Gamma, Omega (see B, D). y is NOT of 16l form (3(n+j)-5m = 1+3j), but u!=0 is derived from exponent x alone, which suffices since u is shared.

Normalization. At u=0 the surviving partitions are (0,3,0),(0,0,2) for N=6 and (0,2,1) for N=7, giving H6(x)=(x)_2 w^2/2+(x)_3 v^3/6 and H7(x)=(x)_3 v^2 w/2 as displayed. With x not in {0,1,2} and w!=0: v=0, then w=0, contradiction. c(t/u) has [t^i] scaled by u^{-i} for EVERY exponent, so both contact pairs are preserved at once. The producer (lines 39, 202) states this as a field-point assertion or explicit u-unit localization chart, not a scaling of a nonunit u in an arbitrary ring. Distinction correctly drawn.

A_X, B_X. Dividing (4) by X(X-1) resp. X(X-1)(X-2): (X)_k/(X)_2 = (X-2)...(X-k+1), (X)_k/(X)_3 = (X-3)...(X-k+1). Each of the seven A-terms and eight B-terms in (6),(7) checks. Subtraction times 24: W^2 cancels; W-coefficient 24(X-2)V+4(X-2)(X-3)-12V^2-12(X-3)V-(X-3)(X-4) = -12V^2+12(X-1)V+(X-3)(3X-4) = Q_X (V: 24X-48-12X+36 = 12(X-1); constant (X-3)(4X-8-X+4)). Non-W part: V^3: 24(1/6)=4; V^2: 24(X-3)[3(X-2)-(X-4)]/12 = 4(X-3)(X-1); V: 24(X-3)(X-4)[5(X-2)-(X-5)]/120 = (X-3)(X-4)(4X-5)/5; constant: 24(X-3)(X-4)(X-5)[7(X-2)-(X-6)]/5040 = (3X-4)(X-3)(X-4)(X-5)/105. All four P_X coefficients and the signs (negative V^2 W, unscaled V^3/6, unscaled constant /2520) confirmed. (10) is an ideal equivalence because 24, X(X-1), X(X-1)(X-2) are units. A CONFIRMED.

## B. Global Bezout identity, W elimination, ideal identity (16), monic quartic

Q_y-Q_x = 3(y^2-x^2)-13(y-x)+12dV = d(3s-13)+12dV = 12d(V-Vstar), Vstar=(13-3s)/12. Q_x(Vstar): 3x^2-13x+12+12xVstar-12Vstar-12Vstar^2 with 12xVstar = 13x-3x^2-3p gives 12-3p-12Vstar-12Vstar^2; then -12*that = 12+36p-36s+169-78s+9s^2 = 9s^2-114s+36p+181 = Gamma, so qstar=-Gamma/12. Q_x is quadratic with leading -12, so Q_x(V)-qstar = 12(V-Vstar)(x-1-V-Vstar). With L=(x-1-V-Vstar)/d: (1+L)Q_x-LQ_y = Q_x-L*12d(V-Vstar) = qstar. (11),(12) CONFIRMED.

Positivity (13). With x=xi+5/3, y=eta+5/3: 36p = 36 xi eta+60(xi+eta)+100; 9s^2 = 9(xi+eta)^2+60(xi+eta)+100; -114s = -114(xi+eta)-380; +181. Constants 1, linear 6(xi+eta), quadratic 9xi^2+54 xi eta+9eta^2. Gamma>=1 for positive rational xi,eta. Only the exponents enter; no reality of V,W is used. Hence Q_x,Q_y generate the unit ideal of Q[V] and of any Q-algebra; an individual Q may vanish and never is divided by.

Ideal identity (16). With g_X = P_X+Q_X W: (1+L)g_x-Lg_y = N+qstar W = qstar(W-W(V)) for W(V)=-N/qstar=12N/Gamma; Q_y g_x-Q_x g_y = E. Conversely at W=W(V) the residues e_x,e_y satisfy (1+L)e_x-Le_y=0, Q_y e_x-Q_x e_y=E, determinant -(1+L)Q_x+LQ_y = -qstar; Cramer gives e_x = 12LE/Gamma, e_y = -12(1+L)E/Gamma in Q[V], so g_x, g_y lie in (W-W(V),E). Ideal identity over Q[V,W], stable under any base change, nilpotents included. CONFIRMED.

Degrees. [V^3](P_x-P_y)=0; [V^2](P_x-P_y) = 4[(x^2-4x)-(y^2-4y)] = -4d(s-4); [V]L=-1/d; [V^3]N = 4+(-1/d)(-4d(s-4)) = 4(s-3); [V^3]W = 48(s-3)/Gamma != 0, degree exactly 3. [V^5]E = -48+48 = 0. [V^4]E = Q2 P2(x)+Q1(y)P3-Q2 P2(y)-Q1(x)P3 = -48[(x-3)(x-1)-(y-3)(y-1)]+48(y-x) = 48d(s-4)+48d = 48d(s-3), exactly the producer's line 162. M=E/(48d(s-3)) is uniformly monic quartic; divisions only by d, s-3, Gamma. B CONFIRMED.

## C. Remaining rows F0, F1, formula (21), R0/R1, isomorphism (23)

Divided difference (A_y-A_x)/d from (6): W^2 cancels; VW coefficient [(y-2)-(x-2)]/d = 1; W/6 coefficient (y-x)(s-5)/(6d) = (s-5)/6; V^3: 1/6; V^2: (s-5)/4; V: divided difference of X^3-9X^2+26X-24 is (s^2-p)-9s+26, over 24; constant: (X-2)(X-3)(X-4)(X-5) = X^4-14X^3+71X^2-154X+120 has divided difference s^3-2ps-14(s^2-p)+71s-154, over 720. Formula (21) CONFIRMED exactly.

Degrees. deg F0<=6 (W^2 term). deg F1<=4 with [V^4]F1 = [V^3]W = 48(s-3)/Gamma, and [V^4]E/(dGamma) = 48(s-3)/Gamma, so R1 = F1-E/(dGamma) has deg<=3: the cancellation is exact. R0 = rem_M F0 is a formal finite monic division (deg R0<=3); the producer correctly says its degree-6,5,4 coefficient cancellations were not executed, and no nonzero/independence claim on R0,R1 is made.

Isomorphism (23). (A_x,B_x,A_y,B_y) = (A_x,A_y,g_x,g_y) = (A_x,A_y,W-W(V),E) by (16). Modulo W-W(V): A_x -> F0, A_y -> F0+dF1, E -> 48d(s-3)M, so the ideal becomes (F0,F1,M) = (R0,R1,M) since F1 = R1+48(s-3)M/Gamma and F0 = R0+qM. Localization W^-1 -> W(V)^-1. Inverse read-back M=0 => E=0; R1=0 => F1=0; R0=0 => F0=0 => A_x=A_y=0; W=W(V), E=0 => g_x=g_y=0 => B_x=B_y=0. All four contacts and the guard restored. C CONFIRMED.

## D. Section 6A: [V^2]N, [V^3]E/d, [V^3]R1, Omega, cubic algebra (29)

[V^2]N. N = P_x+L(P_x-P_y), L = L0+L1V, L0=(x-1-Vstar)/d, L1=-1/d. [V^2]N = 4(x-3)(x-1)+L0(-4d(s-4))+(P1(x)-P1(y))/(-d). P1(X) = (4X^3-33X^2+83X-60)/5, divided difference (4(s^2-p)-33s+83)/5 (producer's displayed value). -4(s-4)(x-1-Vstar) = -4x(s-4)-(s-4)(3s-25)/3 using 12(x-1-Vstar)=12x+3s-25. Then 4x^2-16x+12-4x(s-4) = 12-4p (symmetric, as N must be). Over 15: (180-60p)+(-15s^2+185s-500)+(12s^2-12p-99s+249) = -3s^2+86s-71-72p. (25a) CONFIRMED.

[V^3]E/d. Three products: Q2(P1(x)-P1(y)) = 12d(4s^2-4p-33s+83)/5; Q1(y)P2(x)-Q1(x)P2(y) = 48(x-1)(y-1)(x-y) = -48d(p-s+1); P3(Q0(y)-Q0(x)) = 4*12d(-Vstar) = d(12s-52). Sum/d = (48s^2-48p-396s+996-240p+300s-500)/5 = (48s^2-288p-96s+496)/5. The Q0 P3 term is included. (25b) CONFIRMED.

[V^3]R1 = [V^2]W+((s-5)/6)[V^3]W+1/6-[V^3]E/(dGamma). [V^2]W = 12[V^2]N/Gamma = (-12s^2+344s-284-288p)/(5Gamma); 8(s-5)(s-3) = (40s^2-320s+600)/5; bracket sum (28s^2+24s+316-288p)/5; minus (48s^2-288p-96s+496)/5 gives (-20s^2+120s-180)/5 = -4(s-3)^2. So [V^3]R1 = 1/6-4(s-3)^2/Gamma = -Omega/(6Gamma), Omega = 24(s-3)^2-Gamma = 15s^2-36p-30s+35. (26) CONFIRMED.

(27). 15s^2 = 15(xi+eta)^2+100(xi+eta)+500/3; -36p = -36 xi eta-60(xi+eta)-100; -30s = -30(xi+eta)-100; +35. Constant 5/3, linear 10(xi+eta), quadratic 15xi^2+15eta^2-6 xi eta = 12(xi^2+eta^2)+3(xi-eta)^2. Omega>0 on the rational parameter range. CONFIRMED.

Cubic algebra. J3 = -(6Gamma/Omega)R1 is monic of degree 3. (M,R0,R1) = (M,F0,J3) = (Z1,Z0,J3) with Z1 = M-q1J3, Z0 = F0-q0J3 of degree<=2 (possibly zero). (29) follows from (23); every row and the W guard retained; the identity is over Q[V,W] with only rational-unit divisions, so any Q-algebra base extension after the normalized chart preserves it with no field-factor loss. dim_Q of Q[V,W(V)^-1]/(J3,Z0,Z1) is 0..3 including nilpotents. Over algebraically closed K nonexistence <=> every irreducible factor of G=gcd(J3,Z0,Z1) divides W <=> G | W^3 (deg G<=3). A field point has V a root of monic cubic J3 and W=W(V) in Q(V), field degree<=3; no point is assumed or constructed. D CONFIRMED.

## E. Six manual controls and limits

1. j=0: d=0, so L, F1, M, R1 are undefined; 16l (its sections 4-6) supplies a normalized single-contact cubic with w!=0 for every x=(5m+1)/(3m), m=3q+4, and the four rows collapse to two solvable rows. The elimination therefore cannot be an accidental single-contact impossibility proof. Survives. 2. X=3: A_3 = W^2/2+VW+V^3/6, B_3 = W^2/2+V^2W/2, 24(A_3-B_3) = 4V^3+(24V-12V^2)W = P_3+Q_3W with P_3=4V^3, Q_3=24V-12V^2. Sign of V^2W negative confirmed. 3. Individual Q zero: (12) never divides by Q_x or Q_y; only the simultaneous zero is refuted by (11)-(13). 4. Cross E: the 2x2 determinant argument needs E=0; dropping E, R0 or R1 is not licensed by monicity. 5. Guard/nilpotents: W^-1 kept explicitly; ideal identities, not reduced point counts. 6. Positivity perimeter: (13),(27) are statements about x,y only, give no sign of V,W,M,R0,R1 and no real-root argument. All six CONFIRMED as meaningful.

Limits. Uniform emptiness remains GAP. Gamma and Omega being units licenses only the two eliminations and does not make the contact ideal the unit ideal. The r=2,j=1 (x=12/7, y=13/7) gcd/read-back proposal is a prospective separate test of unknown cost, not executed here and not authorized by this gate; a verdict at one (r,j) proves nothing for all r,j. No source/Keller/JC2 conclusion, no global rank change.

## F. Smallest actual defects found

F1 (documentary, C). Line 195 cites "(18),(20)" for the cancelling leading coefficients; the [V^4]F1 value is the unnumbered display at line 180 following (20). Content unaffected.
F2 (documentary, metadata). READ-SCOPE (line 3) calls the criterion "quartic" while the report's final form and custody.json scope are the cubic; superseded wording, no mathematical data involved.
No mathematical defect was found in A-E. No coefficient expansion, gcd, sample or code exists anywhere in the five inputs, as stated by the producer.

## G. Read scope and custody

All five hashes matched before reading. Producer body (first 18173 bytes) hashes to e788274a... and the 16l body (first 12649 bytes) to 5e113c2e..., both equal to their Seal and artifact/custody records (documentary check). Producer terminal state, all-writers-idle 20:56:56 before the 20:59:51 controlling cap, is taken from custody.json and the brief; no ledger or provenance follower was read. Only the accepted 16l content is a scientific premise; its UNREVIEWED header does not change the accepted lifecycle. Written: this report and box/f10-two-exponent-contact-gate-fable5-20260909/READ-SCOPE.md only, via apply_patch. Own WHOLE read, raised-OPEN and own-only collision check precede the single marker below.

## OPENS RAISED

- NONE new. The assigned two-exponent question stays at the producer's own recorded gap, restated without a new canonical ID: QUANTITY 0 <= dim_Q Q[V,W(V)^-1]/(J3,Z0,Z1) <= 3 for each (r,j), r>=2, 1<=j<=r-1, presently undetermined; nonexistence <=> gcd(J3,Z0,Z1) | W^3. Cheapest test: exact r=2,j=1 cubic/two-quadratic gcd with W guard and read-back, cost unknown, not executed or authorized here.

## COLLISIONS

status: EMPTY

- NONE — own-only check: both owned targets were absent before the lane; no corpus, ledger or provenance scan performed.

<!-- BODY-END -->
