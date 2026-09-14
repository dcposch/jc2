# FIRST gate: entire paired-contact finiteness via an integral family (producer f10-contact-generic-subresultant-astra-20260910)

2026-09-10. Gate lane fable5. Launch 01:47:06 UTC; fixed stop 02:00:00 UTC (earlier than launch+15 min, 02:02:06); publication reserve from 01:58:00 UTC. Charged inputs: the four ordered SHA256 pins of the lane brief, verified byte-identical in /tmp/jc2-lane.SwsoIb/inputs before any body read (521ec17b producer 11813 B; e79deea0 ROOT-CARD 2863 B; 96deb541 accepted17zi producer 10488 B; f4f51690 accepted17zi gate 11573 B). All four read WHOLE; no clipping. Premises: accepted17zi only for its exact quartics/remainders, whole guarded ring R, ordered cover C and the closed V=1/3 slice (three symmetric, six ordered points; x,y live in the cover). No unreviewed dimension<=1 argument is a premise. ZERO mathematical subprocesses; every check below is manual recomputation. No Seal, no charge_basis.

## 0. Verdict table

| Item | Verdict | Smallest actual defect |
|---|---|---|
| A literal a,b = accepted17zi; identity (2); W-degree<=8; L=90^4*1944^2; L mod 7=4; degree exactly 8; L unit in Z_(7) | CONFIRMED | F1: (2) is asserted, not derived (documentary; derivation supplied below) |
| B free rank-2 E, injectivity without Delta; P=0 in D; W,s,p integral; D finite over Z_(7)[V] | CONFIRMED | none |
| C b=(X-3)(X-4)(X-5)(X-6) mod 7 at V=1; f3..f6; six pair checks; exhaustion over the closure; zero ring | CONFIRMED | none (finiteness is not even needed for the zero-ring step; see C) |
| D Nakayama over Z_(7) then over Q[V]_(V-1); nonzero f(V), f(1)!=0; dim_Q M finite; both countercontrols | CONFIRMED | none |
| E R=M[G^-1], C, V!=1/3 chart finite-dimensional with nilpotents and all coefficient-loss loci; scope statements | CONFIRMED as scoped | none |
| F cubic reduction: f(s), U,T,Z, both remainder rows, modular reduction | CONFIRMED (separate claim, not load-bearing) | none |

Overall: the finiteness proof stands on independent manual recomputation. It is a NEW result reviewed once by this gate; no promotion, execution or follow-on authority is granted here.

## A. Literal family, scaling identity, leading coefficient L

Literal comparison: all eight nonleading coefficients a3..a0, b3..b0 in the producer's section 2 are byte-for-byte the accepted17zi section 2 coefficients (a3=30V-14, a2=71-270V+180V^2+120W, a1=-154+780V-900V^2+120V^3-600W+720VW, a0=120-720V+1080V^2-240V^3+720W-1440VW+360W^2; b3=42V-18, b2=119-504V+420V^2+210W, b1=-342+1974V-2940V^2+840V^3-1470W+2520VW, b0=360-2520V+5040V^2-2520V^3+2520W-7560VW+2520V^2W+2520W^2). CONFIRMED.

Identity (2), derived (the producer only states it): for monic quartics a=prod(X-alpha_i), b=prod(X-beta_j) over a splitting extension of Z[V,W,t,t^-1], t^-4 a(tZeta)=prod(Zeta-alpha_i/t) is monic in Zeta, likewise b; so Res_Zeta of the two normalized quartics is prod(alpha_i-beta_j)/t^16 = t^-16 Res_X(a,b). Equivalently, the Sylvester determinant is homogeneous of degree 16 under X->tX after the t^-4 normalization. Substituting W=t^2 gives P(V,t^2)=t^16 Res_Zeta(...). CONFIRMED.

Coefficients of the normalized quartics, by hand: a3 t^-1 in Z[V]t^-1; a2 t^-2=(71-270V+180V^2)t^-2+120; a1 t^-3=(-154+780V-900V^2+120V^3)t^-3+(-600+720V)t^-1; a0 t^-4=(120-720V+1080V^2-240V^3)t^-4+(720-1440V)t^-2+360. So all coefficients lie in Z[V,t^-1] and setting t^-1=0 leaves A0=Zeta^4+120Zeta^2+360. For b: b2 t^-2 -> 210; b1 t^-3 has only t^-3,t^-1 terms; b0 t^-4=(...)t^-4+(2520-7560V+2520V^2)t^-2+2520, so B0=Zeta^4+210Zeta^2+2520. CONFIRMED. Hence Res_Zeta of the normalized pair is Q(V,u) in Z[V,u], u=t^-1, with Q(V,0)=Res(A0,B0)=L, and P(V,t^2)=t^16 Q(V,1/t) has t-degree at most 16 with t^16 coefficient L; comparing with P(V,t^2)=sum c_k(V)t^(2k) gives c_k=0 for k>8 and c_8=L, a constant. W-degree at most 8 with W^8 coefficient L. CONFIRMED.

L: with Y=Zeta^2, B0-A0=90Y+2160=90(Y+24). Res_Y(A0,B0)=prod over roots y_i of A0 of 90(y_i+24)=90^2 A0(-24); A0(-24)=576-2880+360=-1944. Res_Zeta(A0(Zeta^2),B0(Zeta^2))=prod over the four roots +-sqrt(y_i) of B0(y_i), each y_i twice, =[Res_Y]^2=(90^2*1944)^2=90^4*1944^2, nonzero. L mod 7: 90=-1, 90^4=1; 1944=7*277+5, 5^2=25=4; L=4. Direct check: 210,2520 vanish mod 7 so B0=Zeta^4; A0=Zeta^4+Zeta^2+3 (120=1, 360=3); Res(A0,Zeta^4)=A0(0)^4=81=4. Consistent. 7 does not divide L, so L is a unit in Z_(7); with L!=0 the W-degree is exactly 8. CONFIRMED. The producer makes no assertion about the other seven coefficients c_k(V); none is needed.

## B. P=0 in D and finiteness of D over Z_(7)[V]

D=k[s,p,V,W]/F with k=Z_(7) and F the four accepted17zi remainder coefficients (integer polynomials; monic division by q, no inversion). E=D[x]/(x^2-sx+p) is free over D with basis 1,x, so D->E is injective for any D, including the zero ring and rings with nilpotents; no Delta inversion is used or available. In D[X], a=q*h_a+F_a1 X+F_a0 with F_a1=F_a0=0, so q|a; likewise q|b. Hence a(x)=b(x)=0 in E. Also q(s-x)=x^2-sx+p=0, so y=s-x is a second root: a(y)=b(y)=0. CONFIRMED.

Sylvester adjugate: there are U_a,U_b in Z[V,W][X] with U_a a+U_b b=Res_X(a,b)=P. Evaluating at x in E gives P=0 in E; P is the image of an element of k[V,W] in D, and D->E is injective, so P=0 in D. Since P=L W^8+lower and L is a unit, W satisfies a monic degree-8 polynomial over k[V] in D. CONFIRMED.

x and y are roots of the monic quartic a with coefficients in k[V,W], hence integral over the image of k[V,W] in E; so are s=x+y and p=xy. Each integrality identity for s (or p) is an equation among elements of D that holds in E, hence in D by injectivity. W integral over k[V] and s,p integral over k[V][W] give, by transitivity, that D=k[V][W,s,p] is generated by three integral elements, so D is a finite k[V]-module (4). All steps are ring identities valid for every scalar ring map; no reducedness, no field points, no quasi-finiteness or genericity substitute. Finiteness (4) is established in the producer's section 3 before the fibre argument of section 4. CONFIRMED.

## C. The whole V=1 fibre modulo 7

b at V=1 mod 7: b3=24=3; b2=35+210W=0; b1=-468+1050W, -468=-469+1=1, 1050=7*150, so b1=1; b0=360-2520W+2520W^2=3. So b=X^4+3X^3+X+3. And (X-3)(X-4)(X-5)(X-6)=X^4-18X^3+119X^2-342X+360 reduces to X^4+3X^3+0X^2+X+3 (-18=3, 119=0, -342=-6=1, 360=3). Equal, W-free, four distinct roots 3,4,5,6. CONFIRMED.

a at V=1 mod 7: a3=16=2; a2=-19+120W=2+W; a1=-154+120W=W; a0=240-720W+360W^2=2+W+3W^2 (240=2, -720=-6=1, 360=3). So a=X^4+2X^3+(2+W)X^2+WX+2+W+3W^2 as printed. Evaluations (powers mod 7: 3^2=2,3^3=6,3^4=4; 4^2=2,4^3=1,4^4=4; 5^2=4,5^3=6,5^4=2; 6=-1): f3=4+5+(4+2W)+3W+(2+W+3W^2)=3W^2+6W+1; f4=4+2+(4+2W)+4W+(2+W+3W^2)=3W^2+5; f5=2+5+(1+4W)+5W+(2+W+3W^2)=3W^2+3W+3; f6=1+5+(2+W)-W+(2+W+3W^2)=3W^2+W+3. All four as printed. CONFIRMED.

Six pairs: f3-f4=6W+3, root W=3, f4(3)=32=4. f3-f5=3W-2, W=2*5=3, f5(3)=39=4. f3-f6=5W-2, W=2*3=6, f6(6)=117=5. f4-f5=4W+2, W=5*2=3, f4(3)=4. f4-f6=-W+2, W=2, f4(2)=17=3. f5-f6=2W, W=0, f5(0)=3. All six table rows CONFIRMED.

Exhaustion: any monic quadratic q dividing b over any field K of characteristic 7 has both roots in {3,4,5,6} and distinct (b is squarefree, so (X-alpha)^2 does not divide b; repeated q refused). q|a iff f_alpha(W)=f_beta(W)=0 in K. Each pairwise difference is linear in W with nonzero coefficient (6,3,5,4,-1,2), so it has exactly one root, which lies in F7, and at that root the remaining value is a nonzero constant. This holds for every W in K, including W=0 (only the pair 5,6 forces W=0 and f5(0)=3) and W outside F7. Zero ring: D/(V-1,7) is a finitely generated F7-algebra (and finite-dimensional by (4)); if nonzero it has a maximal ideal whose residue field K has characteristic 7 and carries a point (s,p,W) with q|a and q|b over K, contradicting the table. So D/(V-1,7)=0 as a ring, not merely pointless over F7 or reduced. CONFIRMED. Note the table excludes points over every characteristic-7 field, so finite-dimensionality is not even needed for this step; it is needed in D.

## D. Two Nakayama steps and total finite dimension

N=D/(V-1) is finite over k[V]/(V-1)=k=Z_(7), a local ring with maximal ideal (7), by (4). N/7N=D/(V-1,7)=0 by C. Nakayama: N=0. CONFIRMED. M=D tensor_k Q=Q[s,p,V,W]/F is finite over Q[V] (base change of (4)) and M/(V-1)M=N tensor Q=0. Nakayama over the local ring Q[V]_(V-1): M_(V-1)=0. For finitely many generators m_i there are g_i with g_i(1)!=0 and g_i m_i=0; f=prod g_i kills M and f(1)!=0, so f!=0 and f(V) lies in F itself. M is a finite module over Q[V]/(f), finite-dimensional over Q, so dim_Q M is finite (7). CONFIRMED.

Countercontrols with finite generation removed, both recomputed: Q=k[1/7] as a k-module has Q/7Q=0 and Q!=0 (not finitely generated over k), so the first Nakayama needs (4). Q[V,W]/(V) as a Q[V]-module: V acts as 0, V-1 acts invertibly, so the V=1 fibre is empty, yet the module is nonzero of dimension one (not finitely generated over Q[V]), so the second Nakayama needs finiteness over Q[V]. Both CONFIRMED. The conclusion (7) is total finite dimension of the unlocalized algebra M, established because M is finite over the one-dimensional ring Q[V] before its empty fibre is used; a generically empty fibre or a resultant nonzero at one parameter would give neither.

## E. Transport to R, C, the V!=1/3 chart; scope

M=Q[s,p,V,W]/F is exactly the unguarded accepted17zi algebra, and R=M[G^-1] with the exact whole G=W*p*(p-s+1)*(9p-15s+25)*(p-2s+4)*(s^2-4p)*(s-3)*(4-s)*Gamma*Omega, identical to accepted17zi section 2. A localization of a finite-dimensional Q-algebra is a direct factor of it (Artinian: the factors where G is a unit), hence finite-dimensional, with nilpotents retained. Every coefficient-loss locus (c=4-12V=0, 3V-1=0, U=T=Z=0, W=0, any Euclidean leading coefficient) is inside M, since (7) was proved before any inversion. C=R[x]/(x^2-sx+p) is free of rank two over R (accepted17zi, G=(y-x)H, unit discriminant), so dim_Q C=2 dim_Q R is finite; R[(3V-1)^-1] and C[(3V-1)^-1] are further localizations, finite-dimensional. Accepted17zi's predicate (7) therefore HOLDS: f(V) in F and a Cayley-Hamilton annihilator g(W) of W on M lie in F, hence in the saturation I. CONFIRMED.

Scope, as the producer states and this gate confirms: the ENTIRE complex guarded contact locus (R, C and both charts) is a finite set of closed points, already known nonempty from the accepted17zi V=1/3 slice (three symmetric, six ordered points, none in 5/3<x<y<2). NOT established: generic-chart emptiness, any point count or enumeration, any explicit eliminant or degree bound, exclusion of prescribed rational/integer specializations, late affine forcing, companion or source closure, any counterexample or JC2 conclusion. What a future elimination may consume, once Root accepts this gate: (i) dim_Q M finite with M unlocalized; (ii) existence of nonzero f(V), g(W) in F (hence in I), with no explicit form or degree; (iii) the eight-degree monic-after-L resultant P/L in W over Z_(7)[V] as an exact ideal member; (iv) the six mod-7 point checks as a fibre certificate at (V,7)=(1,7). No execution or promotion authority is granted by this gate.

## F. Optional cubic simplification (separate claim)

a-b has cubic coefficient a3-b3=(30V-14)-(42V-18)=4-12V=c, as stated. With h=X^3+uX^2+vX+w=q(X-r): expanding (X^2-sX+p)(X-r)=X^3-(r+s)X^2+(sr+p)X-pr gives r=-u-s, p=v-sr=s^2+us+v, and w=-pr=(s^2+us+v)(s+u)=s^3+2us^2+(u^2+v)s+uv, i.e. f(s)=s^3+2us^2+(u^2+v)s+uv-w=0. CONFIRMED. Also rem_q(h)=[s^2-p+us+v]X+[w-p(s+u)], so on the chart the ideal F equals (p-(s^2+us+v), f(s), rem_q(a)_X, rem_q(a)_0), consistent with the card.

First row: substituting p=s^2+us+v into rem_q(a)_X=s^3-2sp+a3(s^2-p)+a2 s+a1 gives -s^3-2us^2+(a2-2v-a3 u)s+(a1-a3 v). And -f(s)+Us+T with U=a2-v-a3 u+u^2, T=a1-w-a3 v+uv equals -s^3-2us^2+[-(u^2+v)+a2-v-a3 u+u^2]s+[-uv+w+a1-w-a3 v+uv], the same. CONFIRMED. Second row: rem_q(a)_0=p^2-s^2p-a3 sp-a2 p+a0=p[(u-a3)s+(v-a2)]+a0. And (u-a3)f(s)+Z-U p with Z=a0+(u-a3)w: the w terms cancel, f(s)+w=(s^2+us+v)(s+u)=p(s+u), so the expression is p[(u-a3)(s+u)-U]+a0=p[(u-a3)s+u^2-a3 u-a2+v+a3 u-u^2]+a0=p[(u-a3)s+(v-a2)]+a0. CONFIRMED. Modulo f(s) and Us+T: Z-U(s^2+us+v) with Us=-T gives Z+Ts+uT-Uv=Ts+uT+Z-Uv. CONFIRMED. No denominator beyond c is inverted, and nothing in A-E depends on this section.

## G. Smallest actual defects

F1 (documentary, A). The scaling identity (2) is asserted ("The exact scaling identity is") without derivation and without naming the ring Z[V,t,t^-1] in which it holds; the root-product/Sylvester-homogeneity argument in A closes it. Content unaffected.
F2 (documentary, C). The zero-ring step invokes finite-dimensionality to obtain a point over the algebraic closure; the table already excludes points over every characteristic-7 field, so the appeal is redundant, not wrong.
No mathematical defect was found in A-F. The least actual defect is F1.

## OPENS RAISED

- NONE new. QUANTITY dim_Q M < infinity for M=Q[s,p,V,W]/F, hence nonzero f(V), g(W) in I=F:[G(3V-1)]^infinity: the accepted17zi predicate (7), previously undetermined, is now established existentially by this producer subject to Root acceptance; enumeration, explicit eliminants, prescribed-specialization exclusion and source/JC2 closure remain outside scope, and no follow-on task is authorized here.

## COLLISIONS

status: EMPTY

- NONE — own-only check: xmodel/f10-contact-global-finiteness-gate-fable5-20260910.md and box/f10-contact-global-finiteness-gate-fable5-20260910/ were ABSENT at 01:47:22 UTC before the skeleton; no corpus, ledger, provenance, Git, live-file or other-lane scan performed.

Own WHOLE reread (78 lines, 13528 bytes before this completion edit, marker count 0) and own-only raised-OPEN/collision extraction done at 01:52:54 UTC, before the 01:58:00 publication reserve; this completion edit adds relation tokens to the QUANTITY line and this paragraph only. Written: this report and box/f10-contact-global-finiteness-gate-fable5-20260910/READ-SCOPE.md, both via apply_patch only. Uncompleted checks: none of A-F; no GAP verdicts. No mathematical subprocess of any size, code, coefficient artifact, network, AWS, SSH, process inspection, agent, Git/shared/protected work or other-lane read occurred. Root retains custody and any further review; this gate gives no promotion, execution or follow-on authority.

<!-- BODY-END -->
