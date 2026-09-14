# f10 middle full-boundary gate (fable5, 2026-09-10): FIRST hostile review of the global denominator unit theorem

lane=f10-middle-full-boundary-gate-fable5-20260910
gate_model=claude-fable-5-1 (first different-model review of the NEW denominator theorem; NOT a re-review of accepted 17zz)
launch=2026-09-10 06:45:39 UTC (first own command); controlling_stop=min(07:00:00 UTC, first+14min=06:59:39)=06:59:39 UTC; reserve 06:57:39 UTC; never reset
owner_writes=xmodel/f10-middle-full-boundary-gate-fable5-20260910.md, box/f10-middle-full-boundary-gate-fable5-20260910/ (both absent at first action, checked by ls)
mode=pure manual algebra. Tools: date, ls, cat, sha256sum, apply_patch (skeleton without marker first, bounded sections, marker last). ZERO CAS, Python, subprocess, compile, test or scripted arithmetic of any size; every number below is hand arithmetic. No network, AWS, SSH, process, agent, Git, corpus, shared, protected, other-lane or live-file read; no uncharged link opened. Premises: the accepted 17zz interface exactly (E_X, Q_X display (5), Z/P/ell/P0 (6)-(10)) taken as scoped premises; the prior gate's excerpt-read qualification on the earlier 17o/17s attachments is preserved, not re-reviewed. No Seal, no charge_basis (no exit-price assertion is made).

## 0. Custody (five ordered immutable snapshots, hashed BEFORE any body read)

| # | file | sha256 | status |
|---|------|--------|--------|
| 1 | f10-middle-full-boundary-astra-20260910.md | 82f11ed717d1691bb37c36242fdd9eb1eea23ec5eb46b42db5590b1997db18e6 | MATCH |
| 2 | READ-SCOPE.md | 462b3dc5c018e1798e071be72c0414ff28eb26f311987c745385bcc7452d75ad | MATCH |
| 3 | ROOT-CARD.md | 5fe30ca2b2e311690bd1012f55df1c67c75c03ff2b3e3268aa3d7cf6266f5e31 | MATCH |
| 4 | f10-middle-resonance-unit-astra-20260910.md | 8cf54b2f78840ced62fd35722da6d0d969eedd3344aa07d4ab08ff62c50df012 | MATCH |
| 5 | f10-middle-resonance-unit-gate-fable5-20260910.md | dc43ef1cfba68da21d0e26f6422e6af626d15a75d551858e72e78c7236ac27ad | MATCH |

All five equal the charged list and were read WHOLE after the match. Producer timeline (first action 06:34:10, reserve 06:47:10, cap 06:49:10) agrees with READ-SCOPE and ROOT-CARD (first+15 min earlier than 06:50). The producer text carries its own Seal (body bytes 9143) outside the body; this gate did not recompute it (no dependence on it).

## A. Parameters (2), identity (3), D(v0)>0 (5)-(6), rational W forced in ANY Q-algebra: CONFIRMED

Parameters. m=3r+1, nu=(5r+2)/m, alpha=(m+n-h)/m=(8r+3-h)/m as in 17zz. d=h-r-1 runs over 1..r-1 (h=r+2..2r). tau=r/m; 2-nu=(6r+2-5r-2)/m=r/m=tau. delta=d/m>0 since d>=1. tau=r/(3r+1) increases in r (derivative 1/(3r+1)^2>0), equals 2/7 at r=2 and tends to 1/3: 2/7<=tau<1/3. 1-3tau=(m-3r)/m=1/m<=d/m=delta<=(r-1)/m=(4r-m)/m=4tau-1<4/3-1=1/3. alpha+nu=(8r+3-h+5r+2)/m=(13r+5-h)/m and 4-delta=(4m-h+r+1)/m=(13r+5-h)/m: equal. ell=12V+4-delta-7=12V-3-delta=12(V-(3+delta)/12): v0 correct. The delta-interval is nonempty exactly when 7tau>=2, i.e. r>=2, and is the single point 1/7 at r=2 (h=4 only). All of (2) CONFIRMED; all quantities are rational numbers, no coefficient ordering is assumed.

Identity (3), from the accepted display (5) of 17zz, Q_u-7E_u term by term. W^2: 2520-7*360=0. V^2W: 2520-0. VW: 2520(u-3)-5040(u-2)=-2520u+2520=2520(1-u). W: 210(u-3)(u-4)-840(u-2)(u-3)=210(u-3)[(u-4)-4(u-2)]=210(u-3)(4-3u). So the W-part is 210W[(u-3)(4-3u)+12(1-u)V+12V^2]=210 D_u W: D_u CONFIRMED. V^3: 840(u-3)-840(u-2)=-840. V^2: 420(u-3)(u-4)-1260(u-2)(u-3)=420(u-3)[(u-4)-3(u-2)]=420(u-3)(2-2u)=840(u-3)(1-u). V: 42(u-3)(u-4)(u-5)-210(u-2)(u-3)(u-4)=42(u-3)(u-4)[(u-5)-5(u-2)]=42(u-3)(u-4)(5-4u). Constant: (u-3)(u-4)(u-5)[(u-6)-7(u-2)]=(u-3)(u-4)(u-5)(8-6u)=-2(3u-4)(u-3)(u-4)(u-5). All four K_u terms CONFIRMED; nothing dropped.

(5). At u=2-tau: (u-3)(4-3u)=(-1-tau)(3tau-2)=(1+tau)(2-3tau)=2-tau-3tau^2; 12(1-u)V=(tau-1)(3+delta)=3tau+tau delta-3-delta; 12V^2=(9+6delta+delta^2)/12. Times 12: 24-12tau-36tau^2+36tau+12tau delta-36-12delta+9+6delta+delta^2=delta^2+(12tau-6)delta-3+24tau-36tau^2. CONFIRMED.

(6). d(12D)/d delta=2delta+12tau-6, increasing in delta, so on the interval it is <=2(4tau-1)+12tau-6=20tau-8<20/3-8=-4/3<0. Hence 12D is strictly decreasing on [1-3tau,4tau-1] and 12D>=12D(4tau-1)=(4tau-1)^2+(12tau-6)(4tau-1)-3+24tau-36tau^2=16tau^2-8tau+1+48tau^2-36tau+6-3+24tau-36tau^2=28tau^2-20tau+4=4(7tau^2-5tau+1). And 28(tau-5/14)^2+3/7=28tau^2-20tau+25/7+3/7=28tau^2-20tau+4, so 12D>=3/7>0 at every actual pair. Own endpoint check r=2 (tau=2/7, delta=1/7): 12D=(1-18+45)/49=4/7=4(28-70+49)/49, consistent. CONFIRMED, strict.

Forcing (7). In ANY commutative Q-algebra R with images V,W satisfying E_nu=Q_nu=ell=0: 12 is a unit so V=v0 exactly; then (3) gives K+210D W=0 with K,D in Q and 210D a nonzero rational, so W-w0=0 EXACTLY in R (not modulo nilpotents), w0=-K/(210D) in Q. No positivity of V,W and no reality of the base ring enters; positivity was used only to show the rational scalar D is nonzero. Complex or nilpotent W cannot escape. CONFIRMED.

## B. E_nu quadratic (8), beta/gamma, Delta=1440 tau J, Phi (9), completed square (10), Phi<5(delta-1)^3<0, e>0: CONFIRMED

(8). At X=nu=2-tau: X-2=-tau, X-3=-(1+tau), X-4=-(2+tau), X-5=-(3+tau). The four W-free terms of E_X become tau(1+tau)(2+tau)(3+tau), -30tau(1+tau)(2+tau)V, +180tau(1+tau)V^2, -120tau V^3: gamma CONFIRMED. W-terms 120(-tau)(-(1+tau))W+720(-tau)VW=120tau(1+tau-6V)W: beta CONFIRMED. 360W^2 unchanged.

Discriminant. Delta=beta^2-4*360*gamma=beta^2-1440gamma. beta^2=14400tau^2(1+tau-6V)^2, so Delta=1440tau[10tau(1+tau-6V)^2-(1+tau)(2+tau)(3+tau)+30(1+tau)(2+tau)V-180(1+tau)V^2+120V^3]. Expanding 10tau(1+tau-6V)^2=10tau(1+tau)^2-120tau(1+tau)V+360tau V^2: V^3 120; V^2 360tau-180(1+tau)=-180(1-tau); V 30(1+tau)[(2+tau)-4tau]=30(1+tau)(2-3tau); constant (1+tau)[10tau+10tau^2-(6+5tau+tau^2)]=(1+tau)(9tau^2+5tau-6). J CONFIRMED.

(9). V=(3+delta)/12: 72*120V^3=5(3+delta)^3=135+135delta+45delta^2+5delta^3; 72*(-180(1-tau))V^2=-90(1-tau)(9+6delta+delta^2); 72*30(1+tau)(2-3tau)V=180(2-tau-3tau^2)(3+delta); 72(1+tau)(9tau^2+5tau-6)=72(9tau^3+14tau^2-tau-6)=648tau^3+1008tau^2-72tau-432. delta^3: 5. delta^2: 45-90+90tau=90tau-45. delta: 135-540+540tau+360-180tau-540tau^2=-45+360tau-540tau^2. constant: 135-810+810tau+1080-540tau-1620tau^2+648tau^3+1008tau^2-72tau-432=-27+198tau-612tau^2+648tau^3. Every coefficient of (9) CONFIRMED by hand.

(10). Phi_tau=90delta^2+(360-1080tau)delta+198-1224tau+1944tau^2. 1944(tau-17/54)^2+16/3: 1944/54=36, 2*36*17=1224; 1944*289/2916=(2/3)*289=578/3, plus 16/3 gives 594/3=198. Exact. For delta>=0 and tau<=1/3 each of the four terms is >=0 and the last is 16/3>0: Phi_tau>0. CONFIRMED.

(11). Phi(1/3,delta)=5delta^3+(30-45)delta^2+(-45+120-60)delta+(-27+66-68+24)=5delta^3-15delta^2+15delta-5=5(delta-1)^3. Since tau<1/3 strictly and Phi_tau>0 on [tau,1/3] at fixed delta>=0, Phi(tau,delta)<5(delta-1)^3<0 because delta<1/3<1. Delta=1440tau J=20tau Phi<0 since tau>0. Own endpoint check r=2: Phi=(5-135+675-1809)/343=-1264/343<-1080/343=5(-6/7)^3, consistent. CONFIRMED.

(12). 360W^2+beta W+gamma=360(W+beta/720)^2-(beta^2-1440gamma)/1440: exact. With w0 the rational forced in A, the square term is >=0 and -Delta/1440>0, so e=E_nu(v0,w0) is a positive rational, hence a nonzero scalar, a unit of every Q-algebra. Logical order verified: rational w0 comes from Q-7E=0 in A FIRST; only then does reality of w0 make the square nonnegative. Without that step E_nu(v0,W)=0 has nonreal solutions (section D), so no complex or nilpotent escape exists once Q is imposed, and none is claimed without it. CONFIRMED.

## C. Polynomial inverse recipe (13)-(15), unit in unguarded Q[V,W]/(E,Q) and every base change: CONFIRMED

(13). At V=v0, (3) reads Q_nu(v0,W)-7E_nu(v0,W)=K+210D W=210D(W-w0) since K=-210D w0. Division of the quadratic E_nu(v0,W)=360W^2+beta W+gamma by the monic linear W-w0: (W-w0)(360W+c)+rem with c-360w0=beta, rem=gamma+c w0=gamma+beta w0+360w0^2=E_nu(v0,w0)=e. So E_nu(v0,W)=(W-w0)[360(W+w0)+beta]+e=A(W)*210D(W-w0)+e=A(W)[Q_nu-7E_nu](v0,W)+e with A(W)=[360(W+w0)+beta]/(210D). CONFIRMED; the only division is by the nonzero rational 210D.

(14). N(V,W)=E_nu-A(W)(Q_nu-7E_nu)-e is a polynomial in Q[V,W] vanishing identically at V=v0 by (13), hence divisible by the monic linear V-v0 in Q[W][V]: J0 is a genuine polynomial. Division is by a monic polynomial, never by an element of a coefficient algebra. CONFIRMED.

(15). N=(V-v0)J0=ell J0/12 gives e=E_nu-A(Q_nu-7E_nu)-ell J0/12, i.e. 1=E_nu/e-(A/e)(Q_nu-7E_nu)-ell J0/(12e): a polynomial identity in Q[V,W]. Modulo (E_nu,Q_nu) it becomes 1=ell*(-J0/(12e)); sign and factor 12 CONFIRMED. Divisions: 210D (A), e (12), and the integers 12,720: all nonzero rationals. Therefore ell is a unit of A_nu=Q[V,W]/(E_nu,Q_nu) with explicit inverse -J0/(12e), hence of every A_nu-algebra: any base change, rings with nilpotents, the zero ring, the localization B_nu=A_nu[(W t5)^-1] (t6(nu),t7(nu) equal E_nu,Q_nu up to the nonzero rationals (nu)_2/720,(nu)_3/5040 since nu is not 0,1,2), and the guarded resonance quotient B_nu/(Z). Equivalently A_nu/(ell)=0, which is the field-free form of A+B. No standalone P0 statement is needed or made: in B_nu/(Z), ell(J+210W)=-P0 holds whether P0 is zero or not. CONFIRMED.

Licence. In B_nu/(Z), Z=P+210 ell W=0 and ell a unit give W=-P(V)/(210 ell) exactly; the retained objects are E_nu(V,-P/(210ell))=Q_nu(V,-P/(210ell))=0 with ell, W and t5 invertible. The producer keeps both leading equations and the guard and asserts nothing about their compatibility. CONFIRMED as stated.

## D. Changed-equation guarded E-only control: CONFIRMED

Drop Q_nu, keep ell=0, E_nu=0 and the guard. E_nu(v0,W)=0 has roots W_+-=(-beta+-sqrt(Delta))/720 with Delta<0 by B: two nonreal complex numbers, hence nonzero (also gamma>0 from beta^2<1440gamma). t5(X) has partitions i+2j+3k=5 with k<=1, so it is affine in W; its W-terms are (2,0,1): (X)_3 W/2 and (0,1,1): (X)_2 VW, coefficient (nu)_3/2+(nu)_2 v0=(nu)_2(v0-tau/2) at nu, since (nu)_3=(nu)_2(nu-2)=-(nu)_2 tau. (nu)_2 is nonzero and v0-tau/2>1/4-1/6=1/12>0, so at fixed rational v0 the guard factor t5 is an affine polynomial in W with rational coefficients and nonzero slope; its only zero is rational, not W_+-. Hence W t5 is nonzero at (v0,W_+-), ell=E_nu=0 hold, and Q_nu(v0,W_+-)=7*0+210D(W_+- - w0) is nonzero because w0 is real and W_+- are not. So the changed objects fail exactly Q and are not allowed leading points; the control isolates Q as the equation that forces rational W. No real-coefficient assumption is used beyond the coefficients being rational numbers at fixed actual (r,h). Dropping ell instead removes V=v0, and the producer correctly claims no positivity or reality for arbitrary complex leading V,W and does not make Z a unit. CONFIRMED.

## Verdicts, smallest defect, what this closes

| item | verdict |
|---|---|
| A parameter inequalities (2) incl. r=2 single point, identity (3) all eight coefficients, (5), strict D>0 by (6), rational w0 forced in ANY Q-algebra | CONFIRMED |
| B (8) beta/gamma, Delta=1440tau J, all seven coefficients of (9), exact completed square (10), (11) strict, e>0 only after w0 rational | CONFIRMED |
| C (13)-(15) exact, monic divisions only, divisions by 210D and e only, unit in unguarded A_nu and every base change, W=-P/(210ell) licensed with leading rows and guard retained | CONFIRMED |
| D E-only guarded complex roots, affine t5 with nonzero rational slope, guard nonzero, Q fails, no reality assumption | CONFIRMED |

REFUTED: none. Independent attacks tried and failed: (i) D=0 somewhere in the strip (excluded by the strict minimum 3/7 at delta=4tau-1); (ii) e=0 (excluded by Delta<0 and w0 real); (iii) escape by complex or nilpotent W (excluded because W-w0=0 holds exactly in the ring, no positivity of unknowns used); (iv) a hidden division by a non-unit (only 12, 720, 210D, e occur); (v) misuse of the retained P0=0 branch (the identity (15) is independent of P0). Smallest defect: no mathematical error found. Precision items, none changing a verdict: (P1) section 2's phrase "cannot coexist with E=0, even for complex W" is justified only by sections 3-4 together, as the producer intends; (P2) section 6's "only possible zero is real" is in fact rational; (P3) the theorem is nonvacuous only insofar as B_nu is nonzero, which neither input asserts nor needs.

What this closes. JUST the boundary gap of 17zz section 4: the ell=0 branch is empty in every Q-algebra, uniformly in (r,h), and the W-elimination W=-P/(210ell) is licensed at every actual pair without any P0 integer theorem. NOT closed: the final unit gap, i.e. B_nu/(Z)=0 for every linked (r,h), equivalently global H7_h-unitness; the retained one-variable equations E_nu(V,-P/(210ell))=Q_nu(V,-P/(210ell))=0 with their guard are neither shown compatible nor incompatible. No resonance-empty, uniform-r cutoff, full-source, forcing, earlier-row or JC2 conclusion follows from A-D.

## OPEN(S) RAISED

None. No new canonical OPEN ID. The existing global H7-unit question (17s/17zz) remains the sole unresolved quantity, now sharpened to the guarded resonance quotient after the licensed W substitution. Its cheapest genuinely new test is compatibility of the two retained one-variable leading equations with the guard; not performed or authorized here.

## COLLISIONS

status: EMPTY

- NONE. Own-only check: this lane wrote exactly xmodel/f10-middle-full-boundary-gate-fable5-20260910.md and box/f10-middle-full-boundary-gate-fable5-20260910/input_custody.md, both absent at first action; no Seal, no charge_basis, no source modification, no coefficient artifact, no rerun of any accepted report.

## Completion

Own WHOLE read, raised-OPEN check (none) and collision check (EMPTY) done before the marker and before the 06:57:39 reserve; every 64-hex token in this file equals an input hash from live sha256sum output. The marker below is the only standalone marker in this file and nothing follows it. All writers idle at the marker.

<!-- BODY-END -->
