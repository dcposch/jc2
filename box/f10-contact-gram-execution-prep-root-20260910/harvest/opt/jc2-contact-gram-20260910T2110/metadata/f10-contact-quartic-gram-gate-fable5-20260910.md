# FIRST gate: exact contact quartic and real Gram discriminator (producer f10-contact-real-window-astra-20260910)

2026-09-10. Gate lane fable5. First action 19:33:49 UTC; hard stop the earlier of ROOT unit launch+18 min and 19:56:00 UTC; final 3 minutes are publication reserve. Charged inputs: exactly three frozen reports in /tmp/jc2-lane.5Td6uj/inputs, current SHA-256 verified before any body read (f87a2189 producer 158 lines 12368 B; 96deb541 accepted symmetric remainder 243 lines 10488 B; f4f51690 accepted same-model gate 70 lines 11573 B). All three read WHOLE by one bounded unclipped read each. The two accepted reports supply only the literal four remainders F_a1,F_a0,F_b1,F_b0, the entire guard G and the ordered/symmetric correspondence; their finiteness GAP is not a premise. My earlier same-model gate is a scoped import, not fresh review. ZERO mathematical subprocesses; every identity below is manual. No Seal, no charge_basis, no promotion authority.

## 0. Verdict table

| Item | Verdict | Smallest actual defect |
|---|---|---|
| A W elimination (1), N, d=210(s-3), both ideal directions, monic quartic Phi, no lost divisor | CONFIRMED | none |
| B R0,R1 polynomial, V-degrees <=6,<=5, all four rows preserved, free rank-4 A, coker M = A/(R0,R1) | CONFIRMED | none |
| C real M at real window (s,p); det(MM^T)>0 <=> rank 4 <=> full complex guarded fiber empty | CONFIRMED | none |
| D all guard factors nonzero on window incl. Gamma, Omega; W=0 impossible via c6,c7 recurrence | CONFIRMED | none |
| E weight envelope 3,4,6,5; columns 6..9 and 5..8; minor <=26; D <=52; prescribed triangle | CONFIRMED (envelope only) | none |
| F controls, scope, section 5 reality lemma, next exact question | CONFIRMED as scoped; section 5 EXCLUDED from acceptance | D1 documentary |

Nothing is computed: no determinant, matrix entry, minor, positivity certificate, unit ideal or point. The bridge is an exact reformulation whose positivity test remains untested.

## A. Exact W elimination and the monic quartic

Premises are the literal rows of the accepted report: F_a1=s^3-2sp+a3(s^2-p)+a2 s+a1 and F_b1 with b3,b2,b1, where a3=30V-14, a2=71-270V+180V^2+120W, a1=-154+780V-900V^2+120V^3-600W+720VW, b3=42V-18, b2=119-504V+420V^2+210W, b1=-342+1974V-2940V^2+840V^3-1470W+2520VW.

Hand collection of F_b1-(7/2)F_a1. Cubic block: (1-7/2)(s^3-2sp)=-(5/2)s^3+5sp. (s^2-p) block: b3-(7/2)a3=42V-18-105V+49=31-63V. s block: b2-(7/2)a2=119-504V+420V^2+210W-(497/2)+945V-630V^2-420W=-(259/2)+441V-210V^2-210W. Constant block: b1-(7/2)a1=-342+1974V-2940V^2+840V^3-1470W+2520VW+539-2730V+3150V^2-420V^3+2100W-2520VW=197-756V+210V^2+420V^3+630W. The VW terms cancel exactly (2520-2520). Collecting by monomials in V,W:

- W: -210s+630=-210(s-3)=-d. CONFIRMED.
- V^3: 420. V^2: -210s+210=-210(s-1). CONFIRMED.
- V: -63(s^2-p)+441s-756=-63[s^2-7s+12-p]=63[p-(s-3)(s-4)]=63K. CONFIRMED.
- V^0W^0: -(5/2)s^3+5sp+31s^2-31p-(259/2)s+197=[-5s^3+62s^2-259s+394+(10s-62)p]/2=D0. CONFIRMED.

So F_b1-(7/2)F_a1=N(V)-dW with N=420V^3-210(s-1)V^2+63KV+D0, identity (1) exact in Q[s,p,V,W].

Ideal directions. Over any Q-algebra B in which s-3 (hence d) is a unit, (F_a1,F_b1)=(F_a1,F_b1-(7/2)F_a1)=(F_a1,N-dW)=(F_a1,W-N/d), an equality of ideals in B[V,W] by unimodular row operations and the unit d. Hence B[V,W]/(F_a1,F_b1)=B[V]/(F_a1(V,N/d)), with W=N/d as an ideal consequence in both directions; nilpotent B and repeated roots are covered because nothing but the ideal identity is used. No V-dependent element (in particular not 3V-1) and no leading coefficient is inverted; the only unit is the existing guard factor s-3.

Monic quartic. F_a1 at W=0 is A(V): V^3 coefficient 120; V^2: 180s-900=180(s-5); V: 30(s^2-p)-270s+780=30(s^2-p-9s+26); constant s^3-2sp-14(s^2-p)+71s-154; and the W coefficient of F_a1 is 120s-600+720V=120(s-5+6V). All match the producer. Then d*F_a1(V,N/d)=d*A(V)+120(s-5+6V)N(V). The only V^4 term is 120*6V*420V^3=302400V^4, a fixed rational constant, while d*A has V-degree 3. So Phi=[dA+120(s-5+6V)N]/302400 is monic in Q[s,p][V]. Equivalently (s-3)F_a1(V,N/d)=[dF_a1(V,N/d)]/210 has leading coefficient 302400/210=1440, so Phi=(s-3)F_a1(V,N/d)/1440 with leading coefficient exactly 1; 210*1440=302400. The fixed denominators 302400, 1440 are legitimate rational scalars. In B[V] the ideal (F_a1(V,N/d)) equals (Phi) since 1440/(s-3) is a unit. A CONFIRMED.

## B. The two constant rows, polynomiality and the free rank-4 cokernel

F_a0=p^2-s^2p-a3sp-a2p+a0 has W-degree two (a0 carries 360W^2; a2,a0 carry 120W, 720W-1440VW). Substituting W=N/d puts denominators d^2 at most, so R0=d^2F_a0(V,N/d) lies in Q[s,p][V]. V-degree: 360N^2 contributes 6; (720-1440V)N*d contributes 4; the remaining terms at most 3. So deg_V R0<=6. CONFIRMED.

I=F_b0-7F_a0. W^2: 2520-7*360=0, so I is W-linear. W coefficient: from F_b0, -210p+2520-7560V+2520V^2; from 7F_a0, -840p+5040-10080V; difference 630p-2520+2520V+2520V^2=630[p-4+4V+4V^2], with VW and V^2W coefficients both 2520. W-free part: p^2: 1-7=-6; s^2p: -1+7=6; sp: -(42V-18)+(210V-98)=168V-80; p: -(119-504V+420V^2)+(497-1890V+1260V^2)=378-1386V+840V^2; constants 360-840=-480, 2520V, -2520V^2, -840V^3. Regrouped: -840V^3+840(p-3)V^2+42[(4s-33)p+60]V+D1, D1=-6p^2+(6s^2-80s+378)p-480 (42*33=1386, 42*60=2520, 168=42*4). Identity (3) CONFIRMED. R1=d*I(V,N/d) is polynomial; its V-degree is at most 2+3=5 from the W term and at most 3 elsewhere. CONFIRMED.

All four rows. Over B with d a unit, (F_a1,F_a0,F_b1,F_b0)=(F_a1,F_b1-(7/2)F_a1,F_a0,F_b0-7F_a0)=(F_a1,W-N/d,F_a0,I). Killing W-N/d gives B[V]/(F_a1(V,N/d),F_a0(V,N/d),I(V,N/d))=B[V]/(Phi,R0,R1), because d^2,d and 1440/(s-3) are units. Neither constant row is dropped and none is weakened; no common-root claim crosses any further divisor. Since Phi is monic of degree 4, A_B=B[V]/(Phi) is free with basis 1,V,V^2,V^3 whether or not Phi is squarefree; the reductions q_i=rem(R_i,Phi) give the same ideal (Phi,q0,q1)=(Phi,R0,R1).

Matrices. M_i is the matrix of multiplication by q_i on A_B in that basis; its j-th column is the coefficient vector of rem(V^jq_i,Phi)=rem(V^jR_i,Phi), j=0..3, and division by a monic polynomial introduces no parameter denominators, so the entries lie in Q[s,p]. The image of M=[M_0 M_1]:B^8->B^4 is q0A_B+q1A_B=(q0,q1)A_B; hence coker M=A_B/(q0,q1)=A_B/(R0,R1)=B[V,W]/(all four rows) exactly, with no generic finite-basis assumption and no determinant inverted. B CONFIRMED.

## C. Real Gram rank at a real window point

Fix real 5/3<x<y<2 and s=x+y, p=xy. Then s is in (10/3,4), so s-3>0 and B=R qualifies in A-B. Every entry of M is a rational-coefficient polynomial in s,p, so M is a real 4x8 matrix regardless of where the sought V,W lie. Monic division commutes with specialization Q[s,p]->R, so M(s,p) is the matrix of multiplication by the specialized q_i on E_sp=R[V]/(Phi_sp), a four-dimensional real algebra retaining repeated roots and nilpotents.

Rank. rank_R M=4 iff the image (q0,q1)E_sp is all of E_sp=R^4 iff E_sp/(q0,q1)=0. If this quotient is nonzero it is a nonzero finite-dimensional R-algebra, so it has a maximal ideal with residue field a finite extension of R, i.e. R or C; the composite R-algebra map E_sp/(q0,q1)->C sends V to a complex number V0 with Phi(V0)=q0(V0)=q1(V0)=0, hence R0(V0)=R1(V0)=0, and W0=N(V0)/d is a complex solution of all four rows by B. Conversely a complex common solution (V0,W0) of the four rows gives, by A-B over B=C, a C-point of E_sp/(q0,q1) tensor C, so the quotient is nonzero. (Equivalently: R->C is faithfully flat, and C[V]/(Phi,q0,q1) is zero iff the univariate gcd is 1 iff there is no common complex root.) Thus rank_R M=4 iff the four rows have NO complex solution (V,W) at these exponents. Repeated roots of Phi, nilpotents and conjugate pairs of complex points play no role: only zero-ness of the algebra is used, never a count of reduced or real points. Real-root emptiness is not substituted anywhere.

Gram. For real M, MM^T is symmetric positive semidefinite; Cauchy-Binet gives det(MM^T)=sum over the 70 four-column subsets of the squared 4x4 minors, so det(MM^T)>=0 with equality iff every 4x4 minor vanishes iff rank M<4. Hence det(MM^T)>0 iff rank_R M=4. Nonnegativity alone says nothing; the discriminator is strict positivity.

Guarded fiber. At a real window point the ordered rows A_x,B_x,A_y,B_y and the symmetric rows are equivalent over any coefficient ring because x-y is a unit (accepted gate, section B), so the complex (V,W)-fiber of the ordered contact system at (x,y) is the fiber of the four rows at (s,p). By D every factor of G except W is a nonzero real number at such (s,p), and W=0 is impossible on that fiber. Therefore the FULL guarded complex contact fiber is empty iff det(MM^T)(s,p)>0. The unguarded and guarded claims coincide here; no guard proof is missing. C CONFIRMED.

## D. Guard factors on the window and W=0

Geometric factors: p=xy>0; p-s+1=(x-1)(y-1)>0; 9p-15s+25=(3x-5)(3y-5)>0; p-2s+4=(2-x)(2-y)>0; Delta=(y-x)^2>0 as x<y; s-3>1/3>0; 4-s>0. With alpha=x-5/3, beta=y-5/3, T=alpha+beta (both positive, s=10/3+T, p=25/9+(5/3)T+alpha*beta): 36p=100+60T+36alpha*beta, 9s^2=100+60T+9T^2, -114s=-380-114T; so Gamma=(100+100-380+181)+(60+60-114)T+9T^2+36alpha*beta=1+6T+9T^2+36alpha*beta>0. 15s^2=500/3+100T+15T^2, -36p=-100-60T-36alpha*beta, -30s=-100-30T; so Omega=5/3+10T+15T^2-36alpha*beta=5/3+10T+15alpha^2+15beta^2-6alpha*beta=5/3+10T+12(alpha^2+beta^2)+3(alpha-beta)^2>0. Both producer displays CONFIRMED.

c6,c7 formulas. For f=(1+z+Vz^2+Wz^3)^X as a formal binomial series, [z^6] collects binom(X,k)*multinomial(k;i,j,l)V^jW^l over i+2j+3l=6, k=i+j+l: binom(X,6)+5Vbinom(X,5)+6V^2binom(X,4)+V^3binom(X,3)+4Wbinom(X,4)+6VWbinom(X,3)+W^2binom(X,2). Multiplying by 720/(X(X-1)) gives (X-2)(X-3)(X-4)(X-5)+30V(X-2)(X-3)(X-4)+180V^2(X-2)(X-3)+120V^3(X-2)+120W(X-2)(X-3)+720VW(X-2)+360W^2, exactly the accepted scalar-factor form of a(X). So c6=X(X-1)a(X)/720. For [z^7]: binom(X,7)+6Vbinom(X,6)+10V^2binom(X,5)+4V^3binom(X,4)+5Wbinom(X,5)+12VWbinom(X,4)+3V^2Wbinom(X,3)+3W^2binom(X,3); times 5040/(X(X-1)(X-2)) gives (X-3)(X-4)(X-5)(X-6)+42V(X-3)(X-4)(X-5)+420V^2(X-3)(X-4)+840V^3(X-3)+210W(X-3)(X-4)+2520VW(X-3)+2520V^2W+2520W^2, exactly b(X). So c7=X(X-1)(X-2)b(X)/5040. Both CONFIRMED; on the window X(X-1)(X-2)!=0, so a(X)=0 iff c6=0 and b(X)=0 iff c7=0.

Recurrence. Formally (1+z+Vz^2+Wz^3)f'=X(1+2Vz+3Wz^2)f. The z^k coefficient gives (k+1)c_(k+1)=(X-k)c_k+(2X-k+1)Vc_(k-1)+(3X-k+2)Wc_(k-2); at W=0 this is the producer's recurrence, valid for complex V. If W=V=0, c6=binom(X,6)!=0 since X is not an integer. If W=0, V!=0 and c6=c7=0 at one X in (5/3,2): k=6 gives (2X-5)Vc5=0, k=5 gives (2X-4)Vc4=0, then k=4,3,2,1 give c3=c2=c1=c0=0 in turn, each pivot 2X-k+1 (k=6..1) being nonzero because 2X lies in (10/3,4) and is not in {0,...,5}; the (X-k)c_k terms vanish by the previous step. But c0=1. So W!=0 on the whole complex fiber at any window exponent, using only x. Reality of V or W is never inferred; a window point is a real-exponent point only, not a prescribed rational, source or Keller point. D CONFIRMED.

## E. Weight envelope and the prescribed triangle

wt(s)=wt(V)=1, wt(p)=2, and formally wt(W)=2 for bookkeeping. N: 420V^3, 210(s-1)V^2, 63KV with K=p-(s-3)(s-4), D0: all <=3. A(V)<=3; d<=1; so dA and 120(s-5+6V)N are <=4 and Phi<=4, with the V^i coefficient of weight <=4-i (the V^4 coefficient 1 has weight 0). F_a0<=4 with each W^m term of (s,p,V)-weight <=4-2m, so d^2F_a0(V,N/d) has terms d^(2-m)N^m of weight <=(2-m)+3m+4-2m=6: R0<=6. I<=4 likewise, and R1=dI(V,N/d) has the W term 630[p-4+4V+4V^2]N of weight <=5 and the rest <=4+1=5: R1<=5. Reducing modulo the monic Phi replaces V^4 by terms of weight <=4, so weighted bounds are preserved. Columns rem(V^jR_0,Phi) have weight <=6+j (6,7,8,9) and rem(V^jR_1,Phi) <=5+j (5,6,7,8); the row-i entry (coefficient of V^i) has weight <=column-i. A 4x4 minor is a sum of products of four entries in distinct rows and columns: weight <=(sum of its four column weights)-(0+1+2+3)<=9+8+8+7-6=26. Cauchy-Binet: D<=52. With s=4-a-b (degree 1) and p=4-2(a+b)+ab (degree 2), total degree in a,b is <=52. All CONFIRMED as bounds only; no actual degree, term count, sparsity or runtime is asserted or known.

Prescribed family: with m=3r+1, a=2-x=(6r+2-5r-2)/m=r/m, b=2-y=(r-j)/m. a=r/(3r+1) increases with r, equals 2/7 at r=2 and tends to 1/3: 2/7<=a<1/3. 1-3a=1/m<=b=(r-j)/m<=(r-1)/m=4a-1 for 1<=j<=r-1. The lines b=1-3a, b=4a-1 meet at (2/7,1/7); at a=1/3 they give (1/3,0) and (1/3,1/3). CONFIRMED. The closed triangle's a=1/3 edge lies outside the open window (x=5/3, and Delta=0 at its top vertex), so strict positivity there is stronger than needed and a boundary zero would not yield a permitted contact; the two other edges and the interior lie in the window. E CONFIRMED.

## F. Controls, scope, excluded appendix, next exact question

Changed-object controls (producer section 6) support only what they test. R[V]/(V^4) with multiplication by V shows that a single column block of nonzero rank does not give emptiness: full row rank 4 is the criterion. The same algebra, with one reduced point but dimension four, shows that the fixed 4x8 size depends on keeping the free basis of the unreduced quotient; the emptiness verdict itself uses only zero-ness of the algebra (C). Replacing MM^T by a Hermitian form would be a different object; M is real because s,p are real, not because V,W are. Without s-3 a unit, (1) does not solve for W and clearing d could add false solutions; on the window s-3>1/3. None of these controls is a rank, squarefreeness, reality or positivity result.

Section 5 of the producer (for a window solution, V real iff W real). Forward direction is immediate from A: W=N(V)/d with real s,p,V and d!=0. The converse rests on imaginary-part reductions of F_a0+2F_a1, F_b1-7F_a1 and F_b0+3F_b1 that I did not replay within this bound. It is EXCLUDED from acceptance here. It is not load-bearing: C covers the branch where V and W are both nonreal without any reality descent, so the Gram bridge does not depend on it.

Scope. The producer asserts, and this gate confirms only, an exact equivalence: for real 5/3<x<y<2, the full guarded complex contact fiber at (x,y) is empty iff D(4-a-b,4-2(a+b)+ab)>0 at (a,b)=(2-x,2-y), with D=det(MM^T) an explicit but UNEVALUATED polynomial. No determinant, entry, minor, positivity certificate, unit ideal or interval point exists. Hence no full contact exclusion, no late-column or source unitness, no r>=3 source zero, no global coverage and no JC2 conclusion follows from this gate. A zero of D on the open triangle would give a guarded real-exponent contact with complex V,W, not a prescribed rational, source or Keller point. This is a changed fixed-size discriminator; the earlier multivariate eliminant attempt and the whole-locus finiteness question are neither premises nor retried. This gate authorizes no first computation and no next review.

D1 (documentary). The producer states the W elimination and the four-row equivalence pointwise ("at every point", "loses no point on the window"), while its rank argument needs the ideal-level, nilpotent-retaining equivalence over R; the ideal identities in A-B above supply it, so content is unaffected. No mathematical defect was found in A-E.

## OPENS RAISED

- NONE new. The assigned GAP stays as the producer recorded it, no new canonical ID: QUANTITY whether D(4-a-b,4-2(a+b)+ab)>0 for every 0<b<a<1/3 (equivalently on the closed prescribed triangle with vertices (2/7,1/7),(1/3,0),(1/3,1/3) for the discrete family), or one exact zero exists; presently undetermined. Cheapest test unknown and not authorized here.

## COLLISIONS

status: EMPTY

- NONE — own-only check: this report and its box were absent at first action; no corpus, ledger, live-body or provenance scan was performed.

Own WHOLE reread (87 lines, 15859 bytes, marker count 0) and own-only raised-OPEN/collision extraction done at 19:40:22 UTC, with all three input hashes re-verified unchanged at that time, before this completion edit and before the publication reserve. Written: this report and box/f10-contact-quartic-gram-gate-fable5-20260910/READ-SCOPE.md, both via apply_patch only. No mathematical subprocess of any size, code, coefficient or matrix artifact, determinant, network, AWS, SSH, process inspection, agent, Git, shared/protected write, other-lane read or provenance traversal occurred. No Seal and no charge_basis are authored. ROOT retains custody, terminal intake and any further review; this FIRST gate gives no promotion, computation or follow-on authority.

<!-- BODY-END -->
