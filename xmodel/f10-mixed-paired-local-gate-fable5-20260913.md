# Paired local mixed-scalar claims (r=12 mod 49 and r=6 mod 7): different-model FIRST

Owner Fable 5.1 (claude-fable-5-1). First action 2026-09-13 04:38:30 UTC;
own target ABSENT at first action. Original reserve 04:55 / HARD 04:58 UTC,
never reset. MANUAL MATH / FIRST REVIEW / UNREVIEWED. ROOT collector;
external ops/lane.sh owns custody, no local finalizer. Review only: no new
finite-family research, no new cases, no higher carries, no stronger theorem.

## Inputs and read scope

Six frozen files in /tmp/jc2-lane.O995fN/inputs, SHA-256 matched to the six
charged pins in charged order BEFORE any whole read, then each read WHOLE
(the coordination snapshot by targeted allocation grep plus its whole
byte hash; no allocation line in it names this lane):

1. f10-mixed-twelve49-root-20260913.md (Claim A)
   31c0f3cd433e1066a8a190cdd52c2710150ecd5f27c86645d1cf0a2748ec52d5
2. f10-mixed-four-six-astra-20260913.md (Claim B)
   73d6f4b980eb83986978b4fda7ab059b3d7569903053bd2cb4542ef72d55f22d
3. f10-mixed-five49-gate-fable5-20260913.md (accepted source map, carries)
   8c9e1035093cb5b2619f7370320b3063b7ab5269d75dbdd74292c6d2281d7225
4. f10-mixed-univariate-reduction-root-20260912.md (accepted U,V,K,P)
   7b8545a623a771ebd423b441c4c1567389d0ca837d4e5b80c8990bc52b1075f8
5. f10-middle-final-residues-astra-20260910.md (coordinate integrality)
   ab2fcd97d3662d04a49ab0e9d169e1a18ca6f5df30e273041673d2f578beb24b
6. box/f10-mixed-paired-local-gate-fable5-20260913/COORDINATION.snapshot.md
   517fca6f67f3d705f9b4045e10f9039aaf11bf3280dfd27bb90bf003ee4a3ead

Common source: phi=1+u+Xu^2+Yu^3, T_h=trunc_7(phi^h), t=(5r+2)/(3r+1),
B=[u^14](phi'/phi)T_(2t-1)T_(4-t), accepted WHOLE S_r=Q[X]/P with Y=V/U.
Input 4's old UNPROMOTED heading is superseded by the accepted actual-source
FIRST. Inputs 3, 4, 5 are consumed only for the accepted source map, the
factorial carries and coordinate integrality; the old middle Z/H7 scalar is
not B and is not used.

Typo notice (input 3, section 3): the display "e(-36)/720=e/20" has a sign
error. The correct value is (-36)e/720=-e/20, and since 20=-1 mod 7 this is
e mod 7, which is what input 3 states and uses. The residue e and every
following source equation are correct; only the intermediate display is
wrong. With the typo taken literally one would get 6e, so it is not
repeated here.

## Verdict summary

| Claim | Verdict |
|---|---|
| A main: r=12 mod 49, n=v_7(e)>=1, B valuations n (1 root), 7n/4 (4), 2n (2); B a unit of S_r | CONFIRMED (inverse existence, no DATA certificate) |
| A auxiliary: exact G in Z_(7)[e,X,Y], B=-eG, both carries, support bound, P0 divisibilities, polygon, Y valuations, three initial forms | CONFIRMED |
| B main: r=6,13,20,27,34,41 mod 49, v_7(B)=0 at every root over every residue extension; B a unit of S_r | CONFIRMED (inverse existence, no DATA certificate) |
| B auxiliary: R_s division, B=(2t-3)J, second digits, carry, F/C/b5, residue(7J)=3(X-2)^4, exact r-to-e map | CONFIRMED |
| B auxiliary: r=48 mod 49 six-root residual cluster, t0=3/2 specialisation, one nonzero root | CONFIRMED as a residual obstruction only, with one labelling note (section 5) |

No decisive gap was found in either claim, so both reviews ran to the end.
Nothing below yields a cutoff, a largest-r statement, REG, a full source
comparison, a source zero, an all-F10 or a JC2 conclusion.

## 1. Claim A: exact integrality, B=-eG and the two carries: CONFIRMED

For r=12+49k: 4r+1=49(1+4k) and 3r+1=37 mod 49, so e=-(4r+1)/(7(3r+1))
has n=v_7(4r+1)-1>=1, every n>=1 occurring; e is never 0. With t=3+7e,
s=5+14e, b=1-7e: T_1=phi (degree 3<=7), so R_b=(T_b-phi)/(b-1) is a
polynomial and B=[u^14]phi'T_s+(b-1)J with deg(phi'T_s)<=9<14. Hence
B=-7eJ=-eG exactly, before any reduction. For j<=7 only p<=7 multinomial
lengths occur; p!=7!*only for the pure u^7 term m_(7,7)=1. So
7*binom(b,7)/(b-1)=b(b-2)...(b-6)/720 lies in Z_(7)[e] and 7R_b is in
Z_(7)[e,X,Y,u]; at b=1 it is -120/720=-1/6=1 mod 7, so 7R_b=u^7 mod 7.
binom(s,7) carries the single 7 from s-5=14e: 2e*(5*4*3*2*1*(-1))/720
=2e mod 7, so T_s is 7-integral and T_s=T_5+2e u^7 mod 7. Therefore
G=7J is in Z_(7)[e,X,Y] and, using (phi'/phi)phi^5=(phi^5)'/5 and
8/5=3 mod 7, G mod 7=3c8(5)+2e coefficientwise. My re-expansion of
c8(5) (p=5: 10X^3+20XY; p=4: 5(X^4+12X^2Y+6Y^2); p=3: 30XY^2) gives
3X^3+5X^4+6XY+4X^2Y+2Y^2+2XY^2 mod 7, as displayed. The exact d6, d7:
binom(t,p) for p=4,5,6 carries 7e; binom(t,7)=e*t(t-1)(t-2)(t-4)(t-5)(t-6)/720
is e times a 7-integral unit congruent to -36/720=-1/20=1 mod 7. So
d6=X^3+6XY+3Y^2 mod 7, d7=3X^2Y+3Y^2+e mod 7 (multinomials re-derived:
[u^6]v^3=X^3+6XY, [u^6]v^2=Y^2, [u^7]v^3=3X^2Y+3Y^2). CONFIRMED.

Support bound at e=0. A monomial of weight w (wt X=1, wt Y=2) in phi^4 has
u-degree <=4+w (each X spends one extra u, each Y two) and in phi' exactly
w; R_1=d/db T_b at b=1 has u-degree <=7 and nonnegative weights. In
[u^14]phi'phi^4R_1 the first factor must reach u^7, forcing w>=3. In the
tail part, a phi^5 monomial of u-degree >=8 has 5+w>=8, so w>=3, and the
remaining factors only add weight. This is an exact support statement over
Q for G(0,X,Y), so a coefficient divisible by 7 cannot hide a lower-weight
term at any n. Weight >=3 implies ordinary degree >=2, so X^2 is absent as
well as X, Y and 1. G-G(0,X,Y) is divisible by e in Z_(7)[e,X,Y] trivially.
CONFIRMED.

## 2. Claim A: septic coefficients, polygon, Y valuations: CONFIRMED

I re-expanded P0=(t-2)P at e=0: 3X^6+18X^6-36X^5+X^3(9X^4-36X^3+36X^2)
=9X^7-15X^6=3X^6(3X-5). Mod 7 with U=3X^2+X, V=X^3-e, K=X^3, t-2=1:
3(X^3-e)^2+6X(X^3-e)(3X^2+X)+X^3(3X^2+X)^2=2X^7+6X^6+4eX^3+eX^2+3e^2
(the X^5 coefficient 6+1 vanishes). V's constant is
7e(t-4)(t-5)(3t-4)/420=(e/6)*((-1)(-2)(5)/10 mod 7)=(e/6)*unit, unit=1,
and 1/6=-1 mod 7, matching V=X^3-e; its X coefficient carries 49e, its X^2
coefficient 7e. Since P0(e=0) has a_i=0 for i<=5, each a_i (i<=5) is
divisible by e as a polynomial; a2=e(1+7h) so v(a2)=n exactly;
a0=3V(0)^2+(t-2)(t-3)V(0)U(0)+(t-2)K(0)U(0)^2 with V(0)~e, U(0)~7e,
K(0)~7e is e^2*(3+7h') exactly, v(a0)=2n; differentiating each product,
a1 collects 6V(0)V'(0) (e*49e), 6V(0)U(0), (t-3)V(0)U'(0), 2K(0)U(0)U'(0)
(all e^2*7) and two e^3 terms, so a1 is divisible by e^2 with v(a1)>=2n+1;
a6=6, a7=2 units. Lower hull: (2,n) lies below the chord (0,2n)-(6,0)
(value 4n/3), (1,>=2n+1) above the chord (0,2n)-(2,n) (value 3n/2), and
(3..5,>=n) above (2,n)-(6,0) (value <=3n/4). Vertices (0,2n),(2,n),(6,0),
(7,0): two roots of X-valuation n/2, four of n/4, one unit root, 7=deg,
leading coefficient a unit so no root is lost. CONFIRMED.

Y=V/U. At v(X)=n/4: U=-6X leading (n/4), V=X^3 leading (3n/4<n), v(Y)=n/2.
At v(X)=n/2: U=-6X leading (n/2), V=e/6 leading (n<3n/2), v(Y)=n/2. Unit
root: X=5/3=4, U=3*16+4=3, V=64=1, Y=1/3=5 mod 7. Cross-checks: the
V/U leading terms give y=-x^2/6=x^2 (four-root) and E=-xy (two-root),
consistent with the d6, d7 initial forms below. CONFIRMED.

## 3. Claim A: three initial forms and the unit conclusion: CONFIRMED

Unit root: d6(4,5)=259=7*37 and d7(4,5)=315=7*45 vanish mod 7, and
directly 3c8(5)(4,5)=3*(3+1+6+5+1+4)=3*20=4 mod 7, agreeing with
Y((3Y-1)X+Y)=5*5=4 from input 3's accepted reduction. v(G)=0, v(B)=n.

Four-root cluster (pi^4=7, X=pi^n x, Y=pi^(2n) y, e=7^n E): d6's least
terms X^3, 6XY sit at 3n/4, Y^2 and every 7e term higher, so
x^3+6xy=0, y=x^2 (x,y nonzero because the valuations are exact); d7 gives
6x^4+E=0, E=x^4 nonzero. In G, weight-w monomials of G(0) have valuation
wn/4>=3n/4, e-multiples have valuation >=n>3n/4, and 7-divisible
weight-3 coefficients are strictly higher. Weight-3 part of 3c8(5):
9X^3+18XY=2X^3+4XY, giving 2x^3+4x^3=6x^3=6xy nonzero. v(G)=3n/4,
v(B)=7n/4.

Two-root cluster (rho^2=7, X=rho^n x, Y=rho^n y, e=7^n E): d6 at
valuation n: 6xy+3y^2=0 (X^3 at 3n/2, 7e-constant at n+1), y nonzero so
x=-y/2=3y; d7 at n: 3y^2+E=0 (the e*unit term is exactly at n, the others
higher). In G the degree-2 monomials XY, Y^2 (weights 3,4; X^2 is excluded
by the support bound) and the e*constant term are the only valuation-n
terms; e*X, e*Y and e^2 are higher. So residue(G/7^n)=4xy+6y^2+2E
=(-2+6-6)y^2=-2y^2=5y^2 nonzero. The divided carry 2e is retained at exact
order; dropping it would change the coefficient (to 4y^2), so the
retention is correct rather than merely harmless. v(G)=n, v(B)=2n.

Valuation multiset n (1), 7n/4 (4), 2n (2), all seven roots with
multiplicity, each argument per root so residue extensions and Galois
orbits are irrelevant. B nonvanishing at every closed point of the
Artinian algebra S_r=Q[X]/P (F=U^7B(X,V/U) coprime to P, U a unit by
input 4's accepted Bezout identity) is unitness, nilpotents included,
stable under base change. This is inverse EXISTENCE; no Bezout DATA
certificate exists or is claimed. Attacks tried and failed: a 7-divisible
weight-2 or degree-1 term in G(0) surviving at large n (excluded exactly,
not mod 7); a1 of valuation exactly 2n breaking the vertex (2,n) (it is
>=2n+1 and irrelevant to the hull anyway); an e^1 term of G at weight <3
entering the four-root form (valuation >=n); a missing seventh root
(degree and unit leading coefficient); the n=0 boundary (correctly
excluded by input 1). The residual point (0,0,0) is the reduction of the
six cluster roots and is handled by the initial forms, not discarded.
Main theorem A CONFIRMED.

## 4. Claim B: deflation, carries, residue(7J)=3(X-2)^4, six classes: CONFIRMED

r=6 mod 7 gives t=4/5=5 mod 7 (3r+1=5, 5r+2=4), so t=5+7e with
e=(t-5)/7=-(10r+3)/(7(3r+1)); for r=6+7n this is -(9+10n)/(19+21n),
7-integral, and mod 7 equals -(2+3n)/5=-3(2+3n)=1-2n. So e=3 iff n=6,
i.e. r=48 mod 49; the six classes are n=0..5. Also 2t-3=(r+1)/(3r+1)
=7(1+2e), so v_7(2t-3)=1 exactly iff e!=3 mod 7, consistent. s=2t-1
=2+7(1+2e), b=4-t=6-7(1+e). CONFIRMED.

deg phi^2=6<=7 gives T_2=phi^2, so R_s=(T_s-phi^2)/(s-2) is a polynomial;
B=[u^14](phi'/phi)phi^2T_b+(s-2)J and deg(phi'phi T_b)<=12<14, hence
B=(2t-3)J exactly. 7R_s: only the pure u^7 term has a 7! denominator;
7*binom(s,7)/(s-2)=s(s-1)(s-3)(s-4)(s-5)(s-6)/720, at s=2 equal to
48/720=1/15=1 mod 7. So 7R_s=u^7 mod 7 and residue(7J)=[u^7](phi'/phi)
residue(T_b). For h=h0+7h1 the p<=6 binomials depend only on h0, and
binom(h,7): exactly one of h,...,h-6 is 7h1, the other six multiply to
6!=-1 (Wilson), so binom(h,7)=7h1*720/5040=h1 mod 7. Hence
residue(T_h)=trunc_7(phi^h0)+h1 u^7 and residue(T_b) has second digit
-(1+e). Both carries CONFIRMED.

Assembly: residue(7J)=[u^7](phi'phi^5)-(1+e)=(8/6)[u^8]phi^6-(1+e)
=6[u^8]phi^6-(1+e). Frobenius phi^7=1+u^7+X^7u^14+Y^7u^21 gives
[u^8]phi^6=a8+a1=a8-1, [u^6]phi^5=b6, [u^7]phi^5=b7+1, so d6=b6=0,
d7=b7+1+e=0 and residue(7J)=6a8-7-e=-a8-e. From (phi^-1)'=-phi'phi^-2 at
u^7: a8=-(b7+2Xb6+3Yb5)=1+e-3Yb5, so residue(7J)=-1-2e+3Yb5 (3).
CONFIRMED.

Finite coefficients, all re-expanded by multinomials: [u^6]phi^5
=5X+30X^2+20Y+10X^3+60XY+10Y^2, divided by 3 (times 5) mod 7 gives
F=Y^2+(2-X)Y+X^3+3X^2+4X; C=[u^7]phi^5=10X^2+5Y+20X^3+60XY+30X^2Y+30Y^2
=3X^2+6X^3+5Y+4XY+2X^2Y+2Y^2 mod 7; b5=[u^5]phi^-2 with binom(-2,p)
=(-1)^p(p+1): -6+20X-12X^2-12Y+6XY=1+6X+2X^2+2Y+6XY. All three match.
Reduction by Y^2=(X-2)Y-X^3-3X^2-4X: C=4X^3+4X^2+6X+(1+6X+2X^2)Y and
Yb5=X^4+X^3+5X^2+6X+(4+3X+X^2)Y (re-derived termwise). In 1-2C-3Yb5 the
Y coefficient is -2(1+6X+2X^2)-3(4+3X+X^2)=-14-21X-7X^2=0, and the rest is
1-3X^4-11X^3-23X^2-30X=1+4X^4+3X^3+5X^2+5X, while 4(X-2)^4=4X^4-32X^3
+96X^2-128X+64 reduces to the same. So residue(7J)=-(1-2C-3Yb5)
=-4(X-2)^4=3(X-2)^4 (4). CONFIRMED; no residue-field division occurred.

Exclusion: in ANY extension of F_7, (4)=0 forces X=2; then F=Y^2+28=Y^2
forces Y=0, C(2,0)=48+12=4, e=-C=3. Conversely (2,0,3) satisfies F, d7 and
kills (4). For the six classes e!=3, so (4)!=0 at every root reduction
(7-integrality of X,Y for r=6 mod 7 imported from input 5, whose V,W are
the current X,Y by identity), v(J)=-1, v(2t-3)=1, v(B)=0 at every root
with multiplicity. Nonvanishing at every closed point of S_r is unitness
(F=U^7B coprime to P, U a unit), nilpotents included, base-change stable.
Inverse EXISTENCE only; no DATA certificate is produced or claimed. Main
theorem B CONFIRMED.

## 5. Claim B: r=48 mod 49 residual six-root cluster: CONFIRMED as stated

At r=48 mod 49, v_7(2t-3)=v_7(r+1)>=2, finite, unbounded. With t0=3/2
(2t0-3=0) and a=X-1/4: U=3X^2-(3/2)X+3/16=3a^2; V=X^3-(3/4)X^2+(3/16)X
-1/64=a^3 (constant (-3/2)(-5/2)(-7/2)(1/2)/420=-1/64, the 7 of t-5
cancelling 420's); K=X^3-(9/4)X^2+(15/16)X-7/64=a^2(a-3/2). Then
P=3V^2/(t-2)+(6X+t-3)VU+KU^2=-6a^6+18a^6+9a^7-(27/2)a^6=9a^7-(3/2)a^6.
Labelling note: input 2 calls this P0, but it is input 1/input 4's P;
input 1's P0=(t-2)P equals -(1/2) of it at t0. Since t-2 is a unit this
changes nothing below. Coefficients of U,K are polynomials in t with
7-free denominators, V has the single 7 in 420 and v(t-t0)>=2, so all
differ from their t0 values by multiples of 7. With 1/4=2 and 3/2=5 mod 7:
residue(P)=5a^6(6a-1)=5*6(X-2)^6(X-1)=2(X-2)^6(X-1). Hensel separation of
the coprime factors gives six roots (with multiplicity) reducing to X=2
and one to X=1. At X=2, F forces Y=0 and (4)=0: the first deflated test is
exhausted there, and the rational guard cannot remove it (unit in the
rational algebra does not mean unit residue). At X=1, F=Y^2+Y+1 gives
Y in {2,4}; e=3 means C=4, i.e. 2Y^2+4Y+2=4, i.e. Y^2+2Y+6=0, satisfied by
Y=2 only; (4)=3 nonzero there, so v(7J)=0 and v(B)=v(2t-3)-1>=1: nonzero
but of positive valuation, exactly as input 2 states. No B-zero, no lift
of a B-zero, no all-r statement and no r=4 statement follows; r=4 mod 7 is
uncalculated and stays so. CONFIRMED as a residual obstruction.

## Boundary

Not in scope and not promoted: r=5 mod 49, r=4 mod 7, r=0,3 mod 7, any
second-order term of 7J on the r=48 cluster, any cutoff or largest-r bound,
REG, source comparison, full-source zero, all-F10, JC2. No new exit-price
assertion is made, so no exit-price declaration line. Attacks that failed on B:
the sign of the p=3 term of [u^7]phi^5 (3Y^2, not 3XY^2), the Wilson sign
in the second-digit carry, the 8/6 versus 8/5 factor (this claim uses
phi^6, so 4/3=6 mod 7), the Y-coefficient cancellation, the second root
Y=4 at X=1, and the unit prefactor t-2 in the P/P0 labelling.

## Own readback, postpins and custody

Own WHOLE readback of this report (every section above, in order) done
04:45:31-04:45:50 UTC before the marker; the verdict table, every displayed
congruence, the polygon vertices, the three initial forms, the
(X-2)^4 identity and the t0=3/2 specialisation were re-read against the
derivations. Postpins at 04:45:22 UTC and again at 04:45:50 UTC: all six
input SHA-256 values are byte-identical to the six charged pins listed
under Inputs (unchanged after readback). Collision check: xmodel holds
only this report plus this lane's harness .log and .run.v2; no other
paired-local file. Tools used: date, ls, test, wc, sha256sum, grep, cat,
sed, awk, tr and heredoc appends only, on this file alone. No code, CAS,
interpreter, import, AST, syntax, test, fixture, network, AWS, SSH,
process or service control, protected tree or mirror, peer or live or
shared file, new agent or extra/linked source. Custody, manifest,
expected-finalizer verification and terminal author/idle collection
belong to ROOT via external ops/lane.sh; no local finalizer was run.
Old COORD pins in historical producers do not override the supplied
current allocation-only amendment. The standalone marker below is the
last content.

<!-- BODY-END -->
