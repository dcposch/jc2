# Gate: c-unit, faithful univariate base and exact cubic cover (hostile manual gate)

lane=f10-r1-univariate-cover-gate-fable5-20260909
gate_of=xmodel/f10-r1-slice-low-weight-discriminator-astra-20260909.md
launch_utc=2026-09-09T18:44Z stop_utc=EARLIER(2026-09-09T19:05:00Z, launch+20min)
status=COMPLETE; verdict A,B,C,D CONFIRMED (conditional on the parent composition); no GAP; no new OPEN

## 0. Custody

All sixteen charged inputs were hashed in the charged order at 18:45:03 UTC and every digest matched before any read. Producer artifact.json (transaction 0eb23510) records body_bytes 18355, body SHA 326372711573d0e0..., closed_utc 2026-09-09T18:40:27Z, frozen_basis 0d39df3c. The producer was read WHOLE (269 lines, 18688 bytes). Parent interfaces read: composition d91b3e38 by keyword grep only, i.e. the matched lines cited below (within 19-64, 71-72, 83-97, 110-132, 134-237), NOT contiguous ranges and NOT WHOLE; the other thirteen charged inputs were hashed but not read here; no other corpus, ledger, code, data or peer. The charged statements that all producer writers were IDLE at 18:41:05 before 18:41:54, and that the parent was promoted 17j after its terminal gate dc4f601e without the producer reading that gate, are taken as charged and not verified here. Parent acceptance is lifecycle promotion of the same scope; it is NOT evidence for the new c-unit/univariate theorem, which receives its first independent gate below. All parent lemmas and the corrected third band are accepted premises. ZERO mathematical subprocesses, CAS, scripts, coefficient or matrix evaluation; every calculation below is manual algebra.

Verdict summary: A CONFIRMED, B CONFIRMED, C CONFIRMED, D CONFIRMED, each conditional on the parent composition exactly as the producer states. No GAP. Doubts and smallest documentary repairs are listed in E; none changes a verdict.

## A. Weight-3/4 lists, F3/F4, forcing, evaluation formulas

Monomial lists. i+2j+3k=3 has exactly (3,0,0),(1,1,0),(0,0,1): x^3, xy, z. i+2j+3k=4 has exactly (4,0,0),(2,1,0),(0,2,0),(1,0,1): x^4, x^2y, y^2, xz. Lists (2) are exhaustive. CONFIRMED.

Evaluation formulas (6), with F3=Phi3 and F4=Phi4 as polynomial functionals: F3(1,0,0)=a; F3(1,1,0)-F3(1,0,0)=(a+b)-a=b; F3(0,0,1)=c; F4(1,0,0)=d; F4(0,1,0)=f; F4(1,1,0)-F4(1,0,0)-F4(0,1,0)=(d+e+f)-d-f=e; F4(1,0,1)-F4(1,0,0)=(d+g)-d=g. All seven CONFIRMED. The Z=0 evaluations are coefficient prescriptions of a polynomial in free X,Y,Z; they assert nothing about z=0 being admissible, and the producer says so (line 74).

Normalization signs against the parent: composition line 39-42 gives q=-u, l=v0-uF, hence u=-q and v0=l-Fq; the producer U=-q, Vcal0=l-Fq is the normalized transport of exactly this. Composition line 121 gives the linear-tau coefficient z-U*Dcal0 and the actual target -2z*S*tau^5; producer y0=Z-U*Dcal0 and target -2Z theta^5 agree. Composition lines 19-20 give the corrected rule N_i=-W_i+(7-i)y_old D_i. Independent check: theta*D^prime has theta^i coefficient i*D_i, so -y0(theta D^prime-7D) contributes -(i-7)y0 D_i=(7-i)y0 D_i. Rule (3) CONFIRMED.

Theta^5 cancellation at the specialization x=y=0 used in B: N_5=-2z-W3_5+(7-5)z D5=-2z-0+2z=0 with D5=1 and W3=0. CONFIRMED independently there; away from x=y=0 it is the parent premise.

k1=0 rows (4). With V=V2 theta^2+V1 theta+V0 and C=theta^3+F theta^2+H theta+a0, I expanded 4CV^prime=8V2 t^4+(4V1+8F V2)t^3+(4F V1+8H V2)t^2+(4H V1+8a0 V2)t+4a0 V1 and 4C^prime V=12V2 t^4+(12V1+8F V2)t^3+(12V0+8F V1+4H V2)t^2+(8F V0+4H V1)t+4H V0 (t=theta). Difference: -4V2 t^4-8V1 t^3+(-4F V1+4H V2-12V0)t^2+(8a0 V2-8F V0)t+(4a0 V1-4H V0). Matching to N at degrees 4,3,2 gives V2=-N4/4, V1=-N3/8, V0=(-4F V1+4H V2-N2)/12, and the residual r=(4CV^prime-4C^prime V)-N at degrees 1,0 gives r1=8a0 V2-8F V0-N1, r0=4a0 V1-4H V0-N0. All five rows of (4) CONFIRMED, with N2 the coefficient.

Column and left inverse. Putting Y=k alone (k*D^prime on the left, same residual convention) forces V2=5k/4, V1=D4 k/2, 12V0=k(-2F D4+5H+3D3), i.e. V0=k*zeta with the producer zeta; then r1^k=k(8a0*5/4-8F zeta+2D2)=k(10a0-8F zeta+2D2)=k*chi1 and r0^k=k(4a0 D4/2-4H zeta+D1)=k(2a0 D4-4H zeta+D1)=k*chi0. So (chi1,chi0) is the k-column h3 of composition line 46 with plus sign, lambda1 chi1+lambda0 chi0=1 is lambda3(h3)=1, and Kcal1=-lambda1 r1-lambda0 r0 is k1=-lambda3(c3) of composition line 48. Signs CONFIRMED. With F3=chi1 r0-chi0 r1, the post-back-map residual is r1-(lambda1 r1+lambda0 r0)chi1=lambda0(chi0 r1-chi1 r0)=-lambda0 F3 and r0-(lambda1 r1+lambda0 r0)chi0=lambda1(chi1 r0-chi0 r1)=lambda1 F3, i.e. (r1,r0)=(-lambda0,lambda1)Phi3 as used in B.

Literal formula (7). At x=y=0: W3=0, U=0, y0=z, so N_i=(7-i)z D_i: N4=3zD4, N3=4zD3, N2=5zD2, N1=6zD1, N0=7z b0. Then V2=-3zD4/4, V1=-zD3/2, V0=z(2F D3-3H D4-5D2)/12=zM/12, r1=z(-6a0 D4-(2F/3)M-6D1), r0=z(-2a0 D3-(H/3)M-7b0), and c=chi1 r0,z-chi0 r1,z. M, r1,z, r0,z and (7) CONFIRMED. No coefficient of B was evaluated.

## B. Global c-unit

Vanishing of the earlier bands at x=y=0: composition lines 119-120 make the first normalized band linear in x and the second the quadratic forcing in x plus beta^(2)y, so both, and the mate bands J,K built from them, vanish at x=y=0; hence W3=0, U=0 and the third A band is Y=z theta+k. Degree of V at most 2 uses the accepted V4=0 and the V3=0 gauge (composition line 22). deg(CV)<=5, deg(DY)=6 (D5=1), so deg T<=6 for T=4CV-7DY. CONFIRMED.

Identities (9), re-derived from (8) and (1). T^prime=4C^prime V+4CV^prime-7D^prime Y-7DY^prime. From (8), 4CV^prime-7Y^prime D=-2z theta^5+r+4C^prime V-YD^prime, so T^prime=8C^prime V-8D^prime Y-2z theta^5+r. Then CT^prime-2C^prime T=8CC^prime V-8CD^prime Y-2zC theta^5+Cr-8CC^prime V+14C^prime DY=-2(4CD^prime-7C^prime D)Y-2zC theta^5+Cr=2theta^7 Y-2zC theta^5+Cr by (1). Both lines of (9) CONFIRMED; no bracket or shift missing.

Division by the formal unit C^3 (a0 is a unit, so C^-1 is a formal series in theta over B): (T/C^2)^prime=T^prime/C^2-2C^prime T/C^3 equals the right side of (9) divided by C^3. Char 0 formal integration: T/C^2 = Int(2theta^7 Y/C^3)+Int(-2z theta^5/C^2)+Int(r/C^2)+K0. The first integrand is theta^7 times a series with constant term k/a0^3, so its integral starts at theta^8 and C^2 times it has no theta^7 term, also for k nonzero. K0*C^2 has degree 6. T has degree <=6. Extracting [theta^7] of C^2 times the series gives (10) exactly. CONFIRMED.

The load-bearing coefficient, from only the two lowest coefficients of C^-2: C^-2=a0^-2-2H a0^-3 theta+O(theta^2); Int(theta^5/C^2)=a0^-2 theta^6/6-2H a0^-3 theta^7/7+O(theta^8); C^2=a0^2+2a0 H theta+...; [theta^7]C^2 Int=a0^2(-2H a0^-3/7)+2a0 H(a0^-2/6)=(2H/a0)(1/6-1/7)=H/(21a0). (11) CONFIRMED, and (12) follows since H=a0=1/w is a unit of B and 2,21 are units.

Free-z legitimacy. The composite maps are polynomial in x,y,z over B (composition lines 119-124), V,k,r are defined from N by the rows above with divisions only by 4,8,12 and by lambda-coefficients in B, and (8) is the defining identity of r. So (8)-(12) are identities in B[z][theta] at x=y=0 with z a free indeterminate, BEFORE any source equation is imposed; no lower compatibility exists at weights 1,2 (the nine G weights are 7,6,5,8,7,6,5,3,4). Substituting r=c z(-lambda0 theta+lambda1) gives z=c*gamma*z in B[z], and the coefficient of z yields c*gamma=1 in the entire B. No chart, b-unit, reality, domain or residue-field assumption is used. (13) CONFIRMED; c is a unit of B. The producer correctly claims nothing about b.

Changed-object controls at exactly this identity. Target 0 instead of -2z theta^5: (10) loses the -2zH/(21a0) term and reads c*z*gamma=0, giving c*gamma=0, no unit conclusion; the producer states this correctly (line 236). Shifted rule D_(i+1): N_i at x=y=0 would become (7-i)z D_(i+1) and (7) would change, but more basically (8) would no longer be the actual third-band equation, so (12) is not available; the corrected rule is load-bearing exactly here. CONFIRMED.

## C. Faithful chart and univariate rows/guards

Parent guard. Composition (17), lines 162-163: the normalized eleven-slot system is nine G_i=0, z*H1-U*H0=0, H0^2=z^7 with z invertible and s=H0/z^3. So z is a unit of the parent ring by definition of the guard, and H0 is then a unit because H0^2=z^7. The producer line 145 "Its z is a unit" matches (documentary repair: cite (17)).

x-unit. Phi3=0 reads x*(a x^2+b y)=-c z. In any commutative B-algebra where c and z are units, x times an element equals a unit, so x is a unit (inverse (a x^2+b y)(-cz)^-1). Holds over products, nilpotent-containing rings and the zero ring alike. CONFIRMED; the x=0 locus is empty on the guarded system, not discarded.

Parameters. t=y/x^2 and r=z/x^3 are well defined once x is a unit; t is a parameter, distinct from the source t and from theta. Phi3/x^3=a+b t+c r, so r(t)=-(a+b t)/c, affine in t for every b including b=0; only c is inverted. Phi4/x^4=d+e t+f t^2+g r(t)=P4(t), degree <=2. CONFIRMED, no b-division, no factor selection.

Nine rows. The parent nine G_i have weights 7,6,5;8,7,6,5;3,4 (composition line 153); the weight-3 and weight-4 rows are Phi3 and Phi4, the other seven are the low rows, G_w(x,y,z)=x^w G_w(1,t,r(t)). The eleventh homogeneous relation z*H1-U*H0 with wt(H0)=9, wt(H1)=8, wt(U)=2 (line 145) becomes x^11(r h1-ubar h0)=x^11 P11. Rows: seven low, P4, P11 = nine slots, plus Phi3 consumed by r(t). CONFIRMED. Guard qguard=r*h0: r unit is z unit (x already a unit), h0 unit is H0 unit; both exclusions retained, neither factor cancelled. No claim that any row is nonzero is made or needed.

Bounds. For x^i y^j z^k with i+2j+3k=w, degree in t at (1,t,r(t)) is j+k (r affine). Maximising j+k under 2j+3k<=w gives floor(w/2) (k=0), and any k>=1 gives j+k<=(w-k)/2<(w/2). Weights 7,6,5,8,7,6,5 give 3,3,2,4,3,3,2; weight 4 gives P4<=2; wt 9 gives h0<=4, wt 8 gives h1<=4, wt 2 gives ubar<=1; qguard=r h0<=5; P11<=max(1+4,1+4)=5. CONFIRMED. Coefficient counts (degree+1): 4+4+3+5+4+4+3+3+6=36 for the nine rows, 6 for the guard; times the rank-7 rational basis: 252 and 42; xi*qguard-1 has the 42 slots plus the constant, 43; p(v) separate. CONFIRMED. z=1 comparison: weight-w slot count sum_(k=0)^floor(w/3)(floor((w-3k)/2)+1) gives 3,4,5,7,8,10 at w=3,4,5,6,7,8, so the nine G weights give 3+4+5+5+7+7+8+8+10=57, weight 11 gives 6+5+3+2=16, total 73, and h0 at weight 9 gives 5+4+2+1=12; distinct (i,j) for distinct k, so no collisions. Envelope only, not speed. CONFIRMED.

## D. Parameter-ring isomorphism and faithful flatness

Runi as (17): B[t,qguard^-1]/(seven low rows, P4, P11). Cover Rcov=Runi[x]/(x^3-h0^2/r^7); divisions are by the guard units. The claim is Rfull (parent (17)-form ring) is isomorphic to Rcov, NOT to Runi. CONFIRMED as stated by the producer (line 215).

Reverse map Rcov -> Rfull: x->x, t->y/x^2, r(t)->z/x^3 (valid since Phi3=0 and c unit give a+b t+c(z/x^3)=0). Seven low rows -> x^-w G_w=0; P4 -> Phi4/x^4=0; P11 -> (z H1-U H0)/x^11=0; qguard -> (z/x^3)(H0/x^9), a unit; cubic -> x^3-(H0^2/x^18)(x^21/z^7)=x^3(1-H0^2/z^7)=0. CONFIRMED. Forward map Rfull -> Rcov: y->x^2 t, z->x^3 r(t), s->h0/r^3. Seven low rows and Phi4 -> x^w times a Runi row = 0; Phi3 -> x^3(a+b t+c r(t))=0; z H1-U H0 -> x^11 P11=0; H0^2-z^7 -> x^18 h0^2-x^21 r^7=x^18 r^7(h0^2/r^7-x^3)=0; z -> x^3 r unit, H0 -> x^9 h0 unit; s=H0/z^3 -> x^9 h0/(x^9 r^3)=h0/r^3. Consistency: z=x^3 r=h0^2 r/r^7=h0^2/r^6=s^2, H0=x^9 h0=h0^7/r^21=s^7, and P11=0 with z a unit gives H1=U H0/z=U s^5 UNSQUARED, exactly composition (16). Compositions: t->y/x^2->x^2 t/x^2=t; y->x^2 t->x^2(y/x^2)=y; z->x^3 r(t)->x^3(z/x^3)=z. Inverse isomorphisms, all eleven slots, guard, s and hence the mate/source/poles/gauges/omega=w s^8 f5 read-backs preserved through the parent maps. CONFIRMED, conditional on the parent identification of its Lambda[Y1,Y2] ring with the (17)-form (accepted premise, not re-verified).

Ring theory of the cubic. x^3-u with u=h0^2/r^7 a unit of Runi: Rcov is free with basis 1,x,x^2 (monic), rank 3; free of positive rank implies faithfully flat (M tensor Runi^3=M^3 vanishes only if M=0). x is a unit with inverse x^2 u^-1. The derivative 3x^2 is a unit since 3 is invertible in a Q-algebra; finite free plus invertible derivative is finite etale, for arbitrary Runi including nilpotents and the zero ring, no domain or field assumption. CONFIRMED. Zero-ring equivalence: Runi=0 implies Rcov=0 trivially; if Rcov=0 then 1=0 in Rcov, and Runi injects into Rcov as the coefficient of the basis element 1, so 1=0 in Runi. Hence the nine-row-plus-guard ideal in B[t,xi] is proper iff Rcov is nonzero iff (by the isomorphism) the parent guarded ideal is proper. CONFIRMED; this is the ring-level statement, not a passage to closed points.

Field points. A Runi point over a char-0 field K gives u in K^x; a root of x^3=u lies in an extension of degree <=3 and yields a full point. A full point over K has x nonzero (unit), so t=y/x^2 lies in K itself: same field, no extension. Existence over algebraic closures is exactly equivalent. This is a parameter-space cover of degree 3, not a source-map degree; the producer says so (line 9). The full B is retained; all nine rows may be zero on a factor and degrees may drop, so no finite solution count, no nonzero or independent equation, no b-unit and no ideal decision follows. The 112/196 endpoint is conditional on every guarded equation and is neither a map nor a JC2 resolution. CONFIRMED as scoped.

## E. Verdict, raised OPENs, GAPs

Verdict. The producer theorem is CONFIRMED at its stated scope: c is a unit of the entire B by the explicit element gamma of (13); the x-unit chart is faithful over all commutative B-algebras; Runi with its nine rows and guard, covered by the monic cubic (19), is isomorphic to the parent (17)-form normalized ring; the cover is free of rank 3, faithfully flat and finite etale; properness of the univariate guarded ideal is equivalent to properness of the parent guarded ideal; forward field extension <=3, reverse same field. Everything remains CONDITIONAL on the frozen composition d91b3e38 at its complete-source scope; this gate is the first independent gate of the new theorem and is separate from the parent 17j lifecycle acceptance. No nonzero or independent equation, finite solution count, b-unit, ideal decision, point, runtime or execution claim is made or endorsed.

Concrete doubts and smallest repairs (documentary; none changes a verdict):
- Producer line 109 says the integration constant is chosen zero for the last two terms; the three integrals share one constant K0 whose C^2 multiple has degree 6. Rephrase; the argument is unchanged.
- Producer line 90 uses deg V<=2; this rests on the accepted V4=0 and the V3=0 mate gauge (composition line 22). Add the citation.
- Producer line 145 asserts z is a unit; cite composition (17) "z invertible", from which H0 unit follows via H0^2=z^7.
- Producer line 215 proves the isomorphism with the (17)-form normalized ring; its identification with the Lambda[Y1,Y2] eleven-slot presentation is the parent (8),(12) read-back and should be named as the consumed premise.
- Producer section 2 step 2 quotes N2^-1(-c2,1,-c2,0,Y); this gate did not re-derive the second-band completed matrix or its forcing, which are accepted premises.

GAPs: none.

## OPEN(S) RAISED

None. No bounded quantity remains inside the scope of this gate that is not already the explicitly deferred exact univariate decision (producer line 244), which is not authorized here and is not re-raised.

## COLLISIONS

status: EMPTY

- NONE — own-only check: this task wrote exactly xmodel/f10-r1-univariate-cover-gate-fable5-20260909.md and created box/f10-r1-univariate-cover-gate-fable5-20260909/ (empty). No corpus scan.

## Completion

Both targets were absent at 18:45 UTC; all sixteen ordered hashes matched before reading. Producer read WHOLE; parent composition read only at the grep-matched lines named in section 0. ZERO mathematical subprocesses of any size, no CAS, script, import, compile, test, coefficient or matrix evaluation; no web, network, AWS, SSH, proc, agent, ledger, code or peer access. Only date, ls, which, sha256sum, grep, cut, head, sed, cat, wc, tail, od, read-only git status on charged inputs or the own file, mkdir of the owned box and apply_patch ran. Skeleton without marker was written first; writes were bounded; own WHOLE, raised-OPEN and collision check precede the marker. No Seal and no charge_basis are authored. The theorem stays PROVISIONAL under its provisional parent; this gate does not accept the parent.

<!-- BODY-END -->
