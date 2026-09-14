# Different-model FIRST: mixed-scalar seven-adic theorem, r=1,2 mod 7

Owner Fable 5.1 (claude-fable-5-1). First action 2026-09-13 02:48:07 UTC;
own target ABSENT at first action. Reserve 03:00 / HARD 03:03 UTC, never
extended. MANUAL MATH, different-model review; no code, CAS, interpreter,
network, process or protected-tree action. Read/hash/heredoc only.

## 0. Custody and read scope

All six charged pins reproduced by sha256sum BEFORE any read, in charged
order: c3f87e0f (discriminator, input1), 460129a5 (septic irreducibility),
7b8545a6 (univariate reduction), aa8b0148 (mixed-scalar FIRST), ae4eda25
(cube INTAKE), 33cfa610 (COORDINATION snapshot). All six read WHOLE. No
live ROOT/Sol/Astra report or mutable canonical file was read. Imports at
recorded scope only: all-root valuations from the septic report, the
whole-leading map S_r=Q[X]/(P), Y=V/U from the reduction note (already
PROVED via 17zzd per the cube INTAKE), and the scalar/weight facts of the
September 11 FIRST. The old middle scalar Z is not this B and is not used.

## 1. r=1 mod 7: CONFIRMED (input1 sections 1-2, all recomputed)

Parameters. r=1+7j: 5r+2=7(1+5j), 3r+1=4+21j, so t=0 mod 7 and
tau=2-t=1/4=2 mod 7; s=2t-1=6, b=4-t=4 mod 7. Import: v(X)=-2/7 at every
root (septic report, r=1,3 class; old V is X by the reduction note).

Source data. I re-derived d6/c3 from the multinomial formula: Y^2 has
c2/c3=3/(t-2), Y has 4c4/c3=t-3, X^2 has 6c4/c3=3(t-3)/2, X has
5c5/c3=(t-3)(t-4)/4, constant c6/c3=(t-3)(t-4)(t-5)/120; all match K and
the displayed equation. U's X^2, X, constant coefficients (3, -3(t-1),
-(t-3)(3t-4)/4) and V's constant -(t-3)(t-4)(t-5)(3t-4)/420 were also
re-derived from d7-(t-2)d6. Import confirmed at recorded scope.

Valuations. U: 3X^2 at -4/7, -3(t-1)X at -2/7, constant unit: v(U)=-4/7,
uniquely least, so U!=0. V: X^3 at -6/7, X^2 at -4/7, X at -2/7
((-3)(-4)(-5)/20=-3, unit), constant (4)(3)(2)(3)/420 at -1: v(V)=-1,
v(Y)=-3/7. Nonzero residues xbar,ybar follow from exactness. In the d6
equation only X^3 and 3Y^2/(t-2) sit at -6/7 (6XY at -5/7, (t-3)Y at
-3/7, X^2 at -4/7, X at -2/7, constant with 120=1 mod 7 at 0). With
t-2=5 and 3/5=3*3=2 mod 7: xbar^3=-2ybar^2=5ybar^2. Equation (1) CONFIRMED.

Integrality and weight. [u^n]phi^s=sum binom(s,M)*M!/(e1!e2!e3!) L^e1X^e2Y^e3
with M<=n<=7; binom(s,M) in Z_7 for s in Z_7 (M<=6: unit factorial; M=7:
seven consecutive factors supply the single 7 of 7!). phi'/phi=phi'*(1/phi)
with 1/(1+v) integral. Weights (L,X,Y,u)=(1,2,3,-1) make B homogeneous of
weight 15, so the X,Y-weight-15 part at L=1 is exactly B|_{L=0}, and
pi^15 B_w has valuation >=(15-w)/7>0 for w<15. CONFIRMED.

Formula (2). Reducing z^3=-Xz-Y: z^5=-Yz^2+X^2z+XY, z^7=2XYz^2+(Y^2-X^3)z
-X^2Y. Collecting A_h: z^2 coefficient XY(2-2h+h(h-1))=(h-1)(h-2)XY; z
coefficient Y^2(1-h+C(h,2))=(h-1)(h-2)Y^2/2 and X^3(-1+h-C(h,2)+C(h,3))
=(h-1)(h-2)(h-3)/6; constant X^2Y(-1+h-C(h,2)+3C(h,3))=(h^3-4h^2+5h-2)/2
=(h-1)^2(h-2)/2. All four match (2). Only binom(h,<=3) occur since L=0
kills u^7 except 3C(h,3)X^2Y. CONFIRMED.

Trace identity. phi=prod(1-z_i u) gives [u^a](phi'/phi)=-p_{a+1}; with
A_h=sum_n [u^n]T_h z^{7-n}, Tr(zA_sA_b)=sum p_{15-n-n'}[u^n]T_s[u^n']T_b
=-B (n+n'<=14 always, so p_0 never enters). Polynomial identity via Newton
sums, no separability. CONFIRMED.

Residue (4). A_6=20[..]: 20=6, 1/2=4, 3/6=1/2: 6xyz^2+3(y^2+x^3)z+x^2y,
and y^2+x^3=6y^2 gives 4y^2 z. A_4=6[..]: 1/6=6: 6xyz^2+(3y^2+x^3)z+2x^2y
with 3y^2+5y^2=y^2. Both match (3). Newton: p1=0,p2=-2x,p3=-3y,p4=2x^2,
p5=5xy (checked by recursion). Product A_6A_4: z^4 x^2y^2, z^3 2xy^3,
z^2 4x^3y^2+4y^4, z 2x^2y^3, const 2x^4y^2. Tr(z*...)=5x^3y^3+4x^3y^3
-12x^3y^3-12y^5-4x^3y^3; with x^3y^3=5y^5: 25,20,-72,-20 -> 4,6,5,1 times
y^5, sum 16=2. B=-2y^5=5ybar^5!=0. So v(B)=-15/7 at every root. CONFIRMED.

## 2. r=2 mod 7, all k>=1: CONFIRMED (input1 section 3)

v(t)=-k (5r+2=5 unit, 3r+1=0), v(X)=-k-2/7 imported from the rescaled
Sbar argument (valid for every v_7(3r+1)). U: 3X^2 at -2k-4/7, X term at
-2k-2/7, constant -2k: v(U)=-2k-4/7. V: X^3 -3k-6/7, X^2 -4k-4/7, X
-4k-2/7, constant -4k-1 (least since k>=1). v(Y)=-2k-3/7. x=X/t, y=Y/t^2
have valuations -2/7,-3/7. Leading UY=V: 3x^2y=1/140, 7x^2y=1/60=1/4=2:
xbar^2 ybar=2. (5) CONFIRMED. d6 equation: X^3 and 3Y^2/(t-2) at -3k-6/7,
6XY at -3k-5/7, (t-3)Y -3k-3/7, X^2 -3k-4/7, X -3k-2/7, constant -3k;
t/(t-2)->1 gives xbar^3=-3ybar^2=4ybar^2. (6) CONFIRMED. Consistency:
these force xbar^7=2, solvable, and ybar^3=4xbar.

t-degree. A T-term with counts (e1,e2,e3), M=e1+e2+e3, n=e1+2e2+3e3 has
t-degree M+e2+2e3=n; a log-derivative monomial at u^{n-1} has >=1 factor,
degree <=n-1; (n1-1)+n2+n3=14. Degree <=14 CONFIRMED. Coefficientwise
bound: denominators of the t-expansion are unit except binom(s,7) (only
the L^7u^7 term, since M=7 forces e2=e3=0), valuation >=-1. With d such
factors, x,y-weight w<=15-7d and v>=-d-w/7>=-15/7 for EVERY t-coefficient
c_d(x,y). Hence v(c_d t^d)>=-dk-15/7>-14k-15/7 for d<=13. Strict exclusion
CONFIRMED for all k>=1 (uses k>=1 exactly once).

Degree-14 coefficient. Leading t-coefficient of binom(2t-1,M)M!/(e!) is
2^M/(e!) and of binom(4-t,M) is (-1)^M/(e!), i.e. H_n(c) with c=2,-1;
single-factor log-derivative terms are L,2X,3Y (the -L^2 in [u^1] has two
factors). Truncation n<=7 leaves exactly the pairs in (7). CONFIRMED.
Residues: pi^jH_j keeps e1=0 monomials plus, at j=7, c^7/7! times pi^7=7,
giving c^7/720 (720=6!=-1 mod 7 by Wilson). j5: c^2xy; j6:
c^3x^3/6+c^2y^2/2; j7: c^7/720+c^3x^2y/2. c=2: 4xy; 8*4y^2/6+2y^2=
32/6=16/3=2*5=3 so 3y^2+2y^2=5y^2; 128/720+8=
2/6+1=5+1=6. c=-1: xy; -4y^2/6+y^2/2=-3y^2+4y^2=y^2; -1/720-1=1-1=0.
(8) CONFIRMED including the essential factorial cancellation.
(9): H7(2)H7(-1) has v>=-2>-15/7. 2xbar[6ybar^2+5ybar^2*0]=12=5 xbar ybar^2;
3ybar[6xbar ybar+5ybar^4+0]=18xbar ybar^2+15ybar^5=4xbar ybar^2+ybar^5.
Sum 9xbar ybar^2+ybar^5=2xbar ybar^2+4xbar ybar^2=6xbar ybar^2!=0 using
ybar^3=4xbar (from xbar=2ybar^3). v(t^-14 B)=-15/7, v(B)=-14k-15/7. CONFIRMED.

## 3. Descent, controls, r=3: CONFIRMED with one structural remark

Descent. For actual r in either family, B!=0 at every Q_7bar-root of P,
hence (fixed embedding, nonvanishing is embedding-independent) at every
Qbar-root. U!=0 at each root by the uniquely-least term, so F=U^7B(t,X,V/U)
in Q[X] has no common root with P, gcd(P,F)=1, and the rational Bezout
cofactor times U^7 inverts B in Q[X]/(P)=S_r. Nilpotents, repeated roots and
arbitrary base change do not affect a Bezout identity. CONFIRMED. Ordinary
degree <=7 of B (2i+3j<=15 gives i+j<=7) makes F a polynomial. CONFIRMED.

r=3 control. 3r+1=3 unit, t=1, s=1, b=3 mod 7; v(X)=-2/7 (septic report,
class 3), U constant (-2)(-1)/4 unit, V constant 24/420 at -1, so
v(Y)=-3/7; 3/(t-2)=3/6=4 gives xbar^3=-4ybar^2=3ybar^2. (2) carries the
factor (h-1), so A_s=0 mod pi and residue(pi^15 B)=0: the first test fails,
nothing about B=0 follows. CONFIRMED as stated. Structural remark from the
pinned September 11 FIRST: on S_r, B=-(7!)^-2 (s-1)(s-2)(s-3)(s-t)(s-t-1)
(s-t-2) K_r(s) at s=2t-1, i.e. rational prefactor 4(t-1)^2(2t-3)(t-2)^2(t-3).
For r=3 mod 7, t-1=(2r+1)/(3r+1) has v>=1, so the weight-15 residue of B
MUST vanish for a rational reason; the honest continuation object is
K_r(2t-1), not a next term of B. For r=1 mod 7 the prefactor is a unit and
for r=2 mod 7 it has valuation -6k, consistent with both results above.
Also consistent: at r=1 mod 7 the promoted cube leading term
-2delta^2/279006525 (279006525=3^13*5^2*7) has v_7=-1, not -15/7; the
archimedean O(delta^(15/7)) tail is not 7-adically small, so there is no
contradiction and no falsifier there. r=0 mod 7 has t=2 mod 7 (denominator
t-2 and the (t-2)^2 prefactor lose unitness), correctly left unsettled.

## 4. Falsifier search: none found

Attacks tried, each closed by explicit arithmetic above: (a) sign or index
error in the reciprocal trace identity (p_0 never enters); (b) a hidden
factorial-7 denominator in the weight-15 part (none: L=0 uses binom(h,<=3));
(c) the constant term of (2) (recomputed as (h-1)^2(h-2)/2); (d) the r=2
lower-degree bound at large k (bound is per coefficient, k enters only as
the strict gap k>=1); (e) H7(-1) wrongly dropped or kept (it is exactly 0
by Wilson plus xbar^2 ybar=2, and is retained in (7)); (f) the final
identity ybar^3/xbar=4 (from xbar=2ybar^3). The source-coefficient import
was re-derived from the multinomial formula rather than trusted.

## 5. Verdicts

- r=1 mod 7, v_7(B)=-15/7 at every leading point: CONFIRMED.
- r=2 mod 7, v_7(B)=-14k-15/7 for every k=v_7(3r+1)>=1: CONFIRMED.
- Unit of the WHOLE S_r, all embeddings/base changes, both families: CONFIRMED.
- r=3 mod 7 first-term vanishing is only a failed test: CONFIRMED, and it is
  forced by the rational factor (t-1)^2, so no next-term B test should be run.
- r=0,3,4,5,6 mod 7: UNSETTLED, no zero supplied, none claimed; correct scope.
- No all-r claim, effective cutoff, REG, source exclusion or JC2: correctly
  absent. Finite-but-unidentified exception set follows from the promoted
  cube theorem plus these two families. No GAP, no REFUTED item.

Imports used at recorded scope only; no runtime or publication authority is
supplied by this review; no charge_basis line (no new exit price).

## 6. Readback and postpins

Own WHOLE readback completed 02:58 UTC; one stray phrase in section 2 was
tidied by a single in-place text edit, no content change. Postpins taken
after all reads: c3f87e0f, 460129a5, 7b8545a6, aa8b0148, ae4eda25, 33cfa610,
all identical to the charged pins (inputs unchanged). No OPEN raised, no
collision target; only this file was written. Word count about 1,300,
under the 2,000-word cap. Finished early because the result is decisive;
clocks not extended. External ops/lane.sh owns custody.

<!-- BODY-END -->
