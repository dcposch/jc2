# FIRST gate: r=3 mod 7 mixed-scalar valuation v7(B)=2l-15/7 (input1)

Owner Fable 5.1 (claude-fable-5-1). Independent different-model mathematical
FIRST. First action 2026-09-13 03:19:26 UTC; own target ABSENT at first
action. Original reserve 03:34 / HARD 03:37 UTC, never reset. MANUAL MATH
ONLY: read/hash/text-edit commands; no code, CAS, interpreter, network,
process control, protected tree, shared edit or delegation.

Charged inputs, all six SHA-256 pins matched in charged order BEFORE the
WHOLE reads (5e04..fea8a, c3f8..96d40, 4601..e97d, 7b85..75f8, aa8b..230f,
33cf..7597). Scope: input1 only (every r=3 mod 7, every source root,
v7(B)=2*v7(2r+1)-15/7). Input2's r=1,2 mod 7 families are accepted and not
re-reviewed. Accepted imports at recorded scope: the whole-leading septic
map S_r=Q[X]/(P), Y=V/U (input4 under 17zzd), and v(X)=-2/7 at every root
for r=3 mod 7 (input3). No source-array comparison, REG, source zero,
all-r/F10 closure, cutoff or JC2 claim; no new exit price; no charge_basis.

## 1. Initial data and residue relations: CONFIRMED

r=3 mod 7 gives 3r+1=3 mod 7 (unit) and 2r+1=0 mod 7, so t-1=(2r+1)/(3r+1)
has v=l=v7(2r+1)>=1 and t=1 mod 7. I re-derived input4's U,V from
(d7-(t-2)d6)/c3 term by term (Y^2 cancels; XY gives -3(t-1); Y gives
-(t-3)(3t-4)/4; X^2 gives -(t-3)(t-1); X gives -(t-3)(t-4)(4t-5)/20;
constant (t-3)(t-4)(t-5)[(t-6)/840-(t-2)/120]=-(t-3)(t-4)(t-5)(3t-4)/420):
CONFIRMED. Valuations at t=1 mod 7 with v(X)=-2/7: U terms -4/7, >=5/7, 0
(constant 1/2), so v(U)=-4/7. V terms -6/7, >=3/7, -2/7 (coefficient -3/10,
unit), constant 24/420=2/35 at v=-1; unique minimum, v(V)=-1, v(Y)=-3/7.
Leading level of UY=V: 3X^2Y=2/35+O(higher); times pi^7=7: 3x^2y=2/5,
x^2y=2/15=2 in F_7. CONFIRMED. d6/c3 re-derived from multinomials
(Y^2: 3/(t-2); LXY: 6; L^3Y: t-3; L^2X^2: 3(t-3)/2; L^4X: (t-3)(t-4)/4;
L^6: (t-3)(t-4)(t-5)/120): CONFIRMED. Lowest terms X^3 and 3Y^2/(t-2) at
-6/7 (6XY is -5/7); with t-2=-1 mod 7 this is x^3=3y^2. CONFIRMED.
Derived: y^3/x=x^2y/3=2*5=3, and x,y nonzero since x^2y=2.

## 2. Exact deflation: CONFIRMED

beta(1,t)=0: T_1=phi, (phi'/phi)phi=phi' has degree 2, T_(t+2) degree<=7,
product degree<=9<14. Q=beta/(s-1) and C=(Q(s,t)-Q(t,t))/(s-t) are exact
monic divisions in s. (4): [u^8]phi^3=3XY^2, [u^9]phi^3=Y^3, so
T_3=phi^3-u^8(3XY^2+Y^3u). First part [u^14](phi^3)'T_t/3 uses pairs
(8,6),(7,7): (9Y^3d6+24XY^2d7)/3=3Y^3d6+8XY^2d7. Tail: (phi'/phi)T_t
agrees with (phi^t)'/t through u^7, so [u^6]=7d7/t, [u^5]=6d6/t, giving
-(21XY^2d7+6Y^3d6)/t. Sum =3(t-2)Y^3d6/t+(8t-21)XY^2d7/t. CONFIRMED (d_j/t
polynomial since d_j(0)=0). On the source d6=d7=0, so beta(t,t)=0 and
Q(t,t)=0 (t-1 a nonzero rational). Then C(2t-1,t)=Q(2t-1,t)/(t-1)
=beta(2t-1,t)/(2(t-1)^2), and beta(2t-1,t)=[u^14](phi'/phi)T_(2t-1)T_(4-t)
=B. Identity (5) B=2(t-1)^2 C(2t-1,t) CONFIRMED on the whole algebra.

## 3. Denominator/weight bound through both divisions: CONFIRMED

With L restored, wt(L,X,Y,u)=(1,2,3,-1): phi has weight 0, phi'/phi weight
1, so [u^14] has weight 15 and the L-exponent of a monomial L^aX^iY^j is
a=15-w, w=2i+3j. Truncated-power coefficients are h(h-1)..(h-m+1)/
(e0!e1!e2!) with e0<=7, e1<=3, e2<=2; the only 7 in a denominator is e0=7
(pure L^7, k=7). Log-derivative coefficients are -Tr(z^(k+1)), integer
polynomials. Hence each Cauchy term with d pure-L^7 factors has a>=7d, so
w<=15-7d, and its coefficient lies in 7^(-d)Z_(7)[s,t] (falling factorials
in s and t+3-s are integer polynomials). Per monomial X^iY^j the combined
coefficient of beta lies in R_w[s], R_w=7^(-floor((15-w)/7))Z_(7)[t]. This
is the load-bearing point: division by the monic s-1 (beta(1,t)=0 holds
per monomial, universally in L,X,Y) and division of Q(s,t)-Q(t,t) by the
monic s-t are long divisions over R_w and stay in R_w[s]; specialization
at s=1+2eps, t=1+eps stays in 7^(-d)Z_(7)[eps] with constant term
C_ij(1,1). So v(C_ij(2t-1,t)X^iY^j)>=-d-w/7>=-15/7 and the difference from
C_ij(1,1) has valuation >=l-d-w/7+15/7>=l>0. (7) CONFIRMED for every l>=1.
No integrality of the old K_r quotient and no rational prefactor was used;
the residue is carried by the exact pairs (d,w)=(0,15),(1,8),(2,1) only.

## 4. Trace computation: CONFIRMED, including the three factorial carries

Identity: det(I-uM_z)=u^3q(1/u)=phi(u), phi'/phi=-sum Tr(z^(k+1))u^k, and
[u^14] of the triple product matches -Tr(z A_s A_b) term by term (exponent
1+7-k1+7-k2=k0+1). CONFIRMED without separability. A_1=z^4q. Since
beta(s,1)=(s-1)Q(s,1), C(1,1)=Q_s(1,1)=(1/2)beta_ss(1,1); expanding
-Tr(zA_sA_(4-s)) twice gives -Tr(zA''_1A_3)+2Tr(zA'_1A'_3)-Tr(zA_1A''_3)
with the last zero mod q. (8) CONFIRMED with signs.

Formula (9): I reduced z^4..z^7 in z^3=-Xz-Y (z^7=2XYz^2+(Y^2-X^3)z-X^2Y)
and recombined the seven listed terms: z^2 gives (h-1)(h-2)XY, z gives
(h-1)(h-2)Y^2/2+(h-1)(h-2)(h-3)X^3/6, constant (h-1)^2(h-2)X^2Y/2.
CONFIRMED. Scaling: pi^k X^iY^j z^(7-k)=x^iy^jZ^(7-k) exactly when e0=0;
1<=e0<=6 leaves pi^e0 with unit denominators; e0=7 gives 7*binom(h,7).
The Z^2 term of the scaled cubic is pi Z^2, so the residue cubic is
Z^3+xZ+y and the O-algebra O[Z] reduces with its trace. CONFIRMED.

Factorial constants: binom'(1,7)=1*(-1)(-2)(-3)(-4)(-5)/5040=-120/5040
=-1/42; binom'(3,7)=3*2*1*(-1)(-2)(-3)/5040=-36/5040=-1/140;
binom''(1,7)=2g'(1) with g(1)=-1/42 and the harmonic sum
1-1-1/2-1/3-1/4-1/5=-77/60, so 2*(77/2520)=11/180. Times 7: -1/6, -1/20,
77/180 with residues 1, 1, 0 (6^-1=6, 20=6). CONFIRMED.

After x^3=3y^2, x^2y=2, (9) becomes (h-1)(h-2)aZ^2+(h-1)(h-2)^2(b/2)Z
+(h-1)^2(h-2), a=xy, b=y^2. Derivatives: f'(1)=-1=6, g'(1)=1 (b/2=4b),
k'(1)=0, plus carry 1: R1=6aZ^2+4bZ+1. f'(3)=3, g'(3)=5 (5*4b=6b),
k'(3)=8=1, plus carry 1: R3=3aZ^2+6bZ+2. f''=2, g''(1)=-4=3 (3*4b=5b),
k''(1)=-2=5, carry 0: R11=2aZ^2+5bZ+5. R0=P_3=2aZ^2+bZ+4. All four
quadratics CONFIRMED. Products in F_7: R1R3=4a^2Z^4+6abZ^3+(a+3b^2)Z^2+2;
R11R0=4a^2Z^4+5abZ^3+(4a+5b^2)Z^2+4bZ+6, halved (4x) to
2a^2Z^4+6abZ^3+(2a+6b^2)Z^2+2bZ+3. Difference 2a^2Z^4+0Z^3+(6a+4b^2)Z^2
+5bZ+6. (11) CONFIRMED, Z^3 coefficient zero. Newton sums of Z^3+xZ+y:
p1=0,p2=-2x,p3=-3y,p4=2x^2,p5=5xy. Tr(Z*(11))=10x^3y^3-18xy^2-12y^5-10xy^2
=3x^3y^3+2y^5 (the xy^2 terms sum to 7); x^3y^3=(x^2y)(xy^2)=2xy^2 gives
6xy^2, and y^5=y^2*y^3=3xy^2 gives 6xy^2; total 12xy^2=5xy^2, nonzero.
(12) CONFIRMED: residue(pi^15 C(2t-1,t))=5xy^2, v(C)=-15/7,
v(B)=0+2l-15/7. Control: dropping both first-derivative carries replaces
R1R3 by (R1-1)(R3-1), a change of Tr(Z(R1+R3-1))=Tr(Z(2aZ^2+3bZ+3))
=8xy^2+15xy^2=2xy^2, so the wrong answer is 3xy^2. CONFIRMED (old-pass
by nonzeroness, wrong coefficient). No mod-7 shortcut erased a carry.

## 5. Scope, all roots, whole algebra, posterior check: CONFIRMED

All l>=1: the discarded difference in section 3 has valuation >=l, with no
l-dependence elsewhere. All seven roots: v(X)=-2/7 is imported for every
root (input3, tau=1 mod 7), and sections 1-4 use only that valuation and
the two residue relations, which hold at every root with x,y nonzero.
Whole algebra: B has finite valuation at every root of P, U(X_i)!=0, so
F=U^7B(t,X,V/U) shares no root with P, gcd(P,F)=1 in Q[X], and the Bezout
identity aP+bF=1 gives B^-1=bU^7 in S_r and in every base change. This is
an inverse-existence proof, correctly labelled; no coefficient certificate
is computed or claimed. Posterior consistency: input5's factorisation
B=-(7!)^-2(s-1)(s-2)(s-3)(s-t)(s-t-1)(s-t-2)K_r(s) at s=2t-1 has factor
valuations l,0,0,l,0,0 (2t-3=-1, 2t-4=-2, t-2=-1, t-3=-2 mod 7) and
v((7!)^-2)=-2, so v(B)=2l-2+v(K_r(2t-1)) forces v(K_r(2t-1))=-1/7: exact
prefactors were available and the arithmetic is CONFIRMED; it shows the
old quotient is NOT 7-integral at these roots, as input1 says.

Verdict on input1's theorem: CONFIRMED for every r=3 mod 7, every source
root, v7(B)=2v7(2r+1)-15/7, hence B a unit of S_r. No GAP found in
sections 1-5; no step was accepted on prose. Remaining 0,4,5,6 mod 7 are
untouched. This gate supplies no source-array comparison, REG, source
zero, all-r/F10 closure, cutoff or JC2 conclusion.

## Reads, readback, postpins and collisions

All six inputs were read WHOLE after their pins matched; the 806-line
COORDINATION snapshot was read in three ranges (1-400, 400-806 with the
truncated 482-700 range re-read in full). No other file, live ledger, peer
report, ROOT parallel file, linked text or code was read. Own WHOLE
readback of this report was completed at 03:27:53 UTC, before this section.
Input postpins at 03:27:53 UTC, all identical to the charged pins:
5e044b639572c125aefa612e2f4fc257b456dcf477d3766242ff1f08d34fea8a,
c3f87e0fb4982f3bd0bad4b8a355041cc58cb9623fb5240d5c343b26f7b96d40,
460129a51fce4ee17d5d71815be014cbb4075dee71a39bb269721761ba29e97d,
7b8545a623a771ebd423b441c4c1567389d0ca837d4e5b80c8990bc52b1075f8,
aa8b0148f8bfb63ef072b23106f92bafa703a6b83033984e17a62f49eb70230f,
33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597.
Collisions: own target absent at first action; at the final check xmodel
holds this report plus this lane's harness .log/.run.v2 names only. No
OPEN raised, no charge_basis, no exit price. External ops/lane.sh owns
custody; no local finalizer. Under 1,300 words; finished before reserve.

<!-- BODY-END -->
