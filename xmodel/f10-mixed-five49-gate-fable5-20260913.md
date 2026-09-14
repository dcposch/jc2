# Five-mod-49 mixed-scalar unit claim: independent FIRST on sections 1-2

Owner Fable 5.1 (claude-fable-5-1). First action 2026-09-13 03:55:54 UTC;
own target ABSENT at first action. Reserve 04:12 / HARD 04:15 UTC, never
reset. MANUAL MATH / FIRST REVIEW / UNREVIEWED. ROOT collector; external
ops/lane.sh owns custody, no local finalizer.

## Inputs and read scope

Five frozen files in /tmp/jc2-lane.pUx2G7/inputs, SHA-256 matched to the
charged pins in charged order BEFORE any read, then each read WHOLE:

1. f10-mixed-remaining-local-astra-20260913.md
   cec05bddcbed1a0a9fc9e4ef9922f4b6eed3ca08684b52cec69bf1a9406bfd42
   (claim under review; ONLY sections 1-2 are in scope).
2. f10-middle-final-residues-astra-20260910.md
   ab2fcd97d3662d04a49ab0e9d169e1a18ca6f5df30e273041673d2f578beb24b
   (coordinate integrality for r=4,5,6 mod 7 in its own V,W).
3. f10-mixed-univariate-reduction-root-20260912.md
   7b8545a623a771ebd423b441c4c1567389d0ca837d4e5b80c8990bc52b1075f8
   (exact U,V,K,P and the V,W=X,Y map; its UNPROMOTED heading is
   superseded by 17zzd and the accepted September 12 actual-map FIRST).
4. f10-mixed-scalar-unit-gate-fable5-20260911.md
   aa8b0148f8bfb63ef072b23106f92bafa703a6b83033984e17a62f49eb70230f
   (B definition, six-root factorisation, closed-point unit criterion).
5. box/ideation-20260912T2150Z-prep/COORDINATION.snapshot.md
   33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597.

No r3, rzero, resonance, peer, live or linked file, no code and no
coefficient artifact was read. Manual mathematics only.

## Verdict summary

| Item | Verdict |
|---|---|
| 1 Universal deflation, R_b denominator bound | CONFIRMED |
| 2 Both factorial carries, no higher e digit | CONFIRMED |
| 3 Residual equations, c8(5), reduction to (4) | CONFIRMED |
| 4 All-root elimination over arbitrary residue fields | CONFIRMED |
| 5 Every r in the five classes, valuation, inverse, base change | CONFIRMED as EXISTENCE; no DATA certificate exists or is claimed |

Net: the sections 1-2 theorem (v_7(B)=0 at every root and B a unit of the
whole accepted leading algebra S_r for every actual r=19,26,33,40,47 mod 49)
is CONFIRMED under the two imported premises named in item 5. No decisive
gap was found, so the review ran to the end.

## 1. Universal deflation and the R_b denominator bound: CONFIRMED

Write phi=1+v, v=u+Xu^2+Yu^3, c_j(h)=[u^j]phi^h=sum_p binom(h,p)m_(j,p),
where m_(j,p)=[u^j]v^p is an INTEGER polynomial in X,Y (multinomial
coefficients). T_h=sum_(j<=7)c_j(h)u^j. Since deg phi=3<=7, T_1=phi, so
T_b-phi vanishes at b=1 and R_b=(T_b-phi)/(b-1) is a polynomial in b,X,Y.
Then T_b=phi+(b-1)R_b and

    B=[u^14](phi'/phi)T_s T_b=[u^14]phi'T_s+(b-1)J,

and phi'T_s has degree<=2+7=9<14, so the first term is zero for every phi.
With b-1=3-t=-delta this is B=-delta J exactly, before any source or
residue reduction. CONFIRMED.

Denominator bound. For j<=7 only p<=7 occurs, and p! is prime to 7 except
p=7, whose only contribution is m_(7,7)=1 (pure u^7). Hence every
c_j(b), j<=6, lies in Z_(7)[b][X,Y], and c_7(b)=binom(b,7)+g(b) with
g in Z_(7)[b][X,Y]. Division by the monic b-1 keeps Z_(7)[b][X,Y]
(each of c_j(b)-[u^j]phi, g(b) vanishes at b=1 because binom(1,7)=0).
The remaining term is binom(b,7)/(b-1)=b(b-2)(b-3)(b-4)(b-5)(b-6)/5040,
denominator exactly one 7. At b=1 it is 1(-1)(-2)(-3)(-4)(-5)/5040
=-120/5040=-1/42, the producer's value. So at most one factor 7, and
only in the pure u^7 coefficient. CONFIRMED.

## 2. Both divided factorial carries: CONFIRMED

t=3+7e, s=2t-1=5+14e, b=4-t=1-7e, e in Z_7 (checked in item 4). Take
X,Y 7-integral (item 5 premise). Then 7R_b=[b(b-2)...(b-6)/720]u^7 + 7G
with G in Z_7[u]; at b=1-7e the bracket is congruent to -120/720=-1/6=1
mod 7 (6=-1). So 7R_b=u^7 mod 7, every other coefficient zero. First
carry CONFIRMED; it needs only b=1 mod 7.

T_s: c_j(s) for j<=6 lies in Z_(7)[s] so depends mod 7 only on s=5 mod 7.
c_7(s)=binom(s,7)+g(s), g(s)=g(5) mod 7, and binom(5,7)=0. The numerator
of binom(s,7) has exactly one factor 7, from s-5=14e=7*2e; the other six
factors are 5,4,3,2,1,-1 mod 7 with product -120. So binom(s,7)
=2e*(-120)/720=2e mod 7 (again -1/6=1). Hence T_s is 7-INTEGRAL and
T_s=T_5+2e*u^7 mod 7. Second carry CONFIRMED. Only e mod 7 enters either
carry, so no higher e digit survives: it multiplies 7.

Assembly. phi'/phi in Z[X,Y][[u]]. 7J=[u^14](phi'/phi)T_s(7R_b) is
7-integral (only R_b carried a 7-denominator). Mod 7 it equals
[u^7](phi'/phi)(T_5+2e*u^7)=[u^7](phi'/phi)T_5+2e. Since T_5 agrees with
phi^5 through u^7 and (phi'/phi)phi^5=(phi^5)'/5, the first term is
(8/5)c8(5), and 8/5=1/5=3 mod 7. residue(7J)=3c8(5)+2ebar CONFIRMED.

## 3. Residual equations, c8(5) and the reduction: CONFIRMED

Multinomials re-derived: [u^6]v^p for p=2..6 are Y^2; X^3+6XY; 6X^2+4Y;
5X; 1. [u^7]v^p for p=3..7 are 3X^2Y+3Y^2; 4X^3+12XY; 10X^2+5Y; 6X; 1.
At t=3+7e, binom(t,p)=0 mod 7 for p=4,5,6 (factor t-3), binom(t,3)=1,
binom(t,2)=3, and binom(t,7)=7e*(3*2*1*(-1)(-2)(-3))/5040=e(-36)/720
=e/20=e mod 7 (20=-1). So d6=X^3+6XY+3Y^2 and d7=ebar+3X^2Y+3Y^2 mod 7:
both lines of (3) CONFIRMED, including the producer's 7binom'(3,7)=-1/20=1.

c8(5)=sum binom(5,p)[u^8]v^p: p=5 gives 10X^3+20XY; p=4 gives
5(X^4+12X^2Y+6Y^2); p=3 gives 10*3XY^2. Mod 7:
3X^3+5X^4+6XY+4X^2Y+2Y^2+2XY^2, the producer's polynomial. With
X^3=XY+4Y^2 (from d6): 3X^3=3XY+5Y^2, 5X^4=5X^2Y+6XY^2, total
2XY+2X^2Y+XY^2 (Y^2 coefficient 5+2=0). Then 3c8(5)+2ebar with
ebar=-3Y^2-3X^2Y gives 6XY+3XY^2+Y^2=Y((3Y-1)X+Y). Equation (4)
CONFIRMED; both source relations were retained, ebar only substituted.

## 4. All-root elimination over arbitrary residue fields: CONFIRMED

Let k be ANY extension of F_7 and (X,Y,ebar) in k^2 x F_7 satisfy (3)
and (4)=0. Branch Y=0: d6 gives X^3=0, X=0, and d7 gives ebar=0. Branch
Y!=0: with d=3Y-1, d=0 would leave the second factor equal to Y!=0, so
d!=0, X=-Y/d, Y=(d+1)/3. Clearing d^3 and Y^2 in d6 and multiplying by 3:
9d^3-18d^2-d-1=2d^3+3d^2+6d+6 mod 7, and (d-3)(2d^2+2d+5) expands to
the same. (5) CONFIRMED. d=3 gives Y=4/3=6, X=-2=5, ebar=-108-450=2 mod 7
and X^3+6XY+3Y^2=413=7*59: control (5,6,2) CONFIRMED. On 2d^2+2d+5, i.e.
d^2+d-1=0 (discriminant 5, nonsquare mod 7, so d not in F_7): using
d^2=1-d, Y^2=(d+1)^2/9=4(d+2)=4d+1, d^2+Y=4d+6, and
ebar=-3Y^2(d^2+Y)/d^2=-3(4d+1)(4d+6)/(1-d)=(6d-3)/(1-d)=-(3+d)/(1-d).
Numerical witness in F_49=F_7(w), w^2=5: d=3+4w, X=3+w, Y=6+6w satisfy
d6=0 and (4)=0, and ebar=2+5w=-(3+d)/(1-d) is not in F_7. If ebar in F_7
then d(1-ebar)=-(3+ebar): ebar=1 gives 0=-4, otherwise d rational.
Contradiction. So (4)!=0 at every residual point unless ebar in {0,2}.
Also (0,0,0) satisfies everything with (4)=0. CONFIRMED.

r-to-e: r=5+7n gives t-3=-(4r+1)/(3r+1)=-7(3+4n)/(16+21n), so e is
7-integral with ebar=-(3+4n)/2=2-2n mod 7. ebar=0 iff n=1 (r=12 mod 49),
ebar=2 iff n=0 (r=5 mod 49); n=2..6 give ebar=5,3,1,6,4, the five
classes. CONFIRMED. Note ebar!=0 also forces v_7(delta)=1 exactly.

## 5. Every actual r, valuation, inverse, base change: CONFIRMED (existence)

Premises used, both charged: (P1) S_r=Q[X,Y,(Yd5)^-1]/(d6,d7)=Q[X]/(P) via
Y=V/U (input 3, accepted by 17zzd); (P2) 7-integrality of X,Y at every
root for r=5 mod 7 (input 2). Map check, beyond labels: I re-expanded
d6/c3=3Y^2/(t-2)+(6X+t-3)Y+K and (d7-(t-2)d6)/c3=UY-V from the
multinomials above, term by term, reproducing input 3's U,V,K exactly
(the constant of V is (t-3)(t-4)(t-5)(3t-4)/420). Its Bezout identity
AU0=(A+Mq/3)U-MV was verified from U=U0+M(X-x0), V=qU/3+A(X-x0)
(the X-coefficient identity checked at t=0,1,2,3, four points of a cubic).
Against input 2: tau=r/(3r+1)=2-t exactly; old K=-840V has constant
-2(t-3)(t-4)(t-5)(3t-4)=2(2-3tau)(1+tau)(2+tau)(3+tau)=k0 exactly; the
leading coefficient of S/49=470400(t-2)P/49 is 86400(t-2)=-5*120*144*tau
exactly; and old W=-K/(210D)=840V/(840U)=V/U=Y. So input 2's V,W are the
current X,Y by identity, not by name. Independently, in the X,Y
coordinates: 9600(t-2)P has 7-integral coefficients when t-3=7e (every
t-3 factor kills the 7 in 420 and 196), leading coefficient a unit, so
a root with v(X)<0 has a uniquely least-valued X^7 term; then d6=0 with
360Y^2 leading, beta,gamma integral, forces v(Y)>=0. (P2) is thus
re-derived here for r=5 mod 7. At every closed point of S_r (every
root of P, with or without multiplicity, hence for every 7-adic place
of its residue number field), items 2-4 give residue(7J)!=0 for the five
classes, so v(J)=-1, v(delta)=1, v(B)=0. Nonvanishing at every closed
point of the Artinian Q-algebra S_r is unitness, nilpotents included; a
unit stays a unit after every base change. CONFIRMED.

Distinction: this is EXISTENCE of an inverse (gcd(P,F)=1 in Q[X]), not a
computed Bezout DATA certificate A1P+A2F=N; none is produced or claimed
by input 1, and input 3's selected certificate experiment is untouched.
No residual-point lift is assumed anywhere: the argument only needs the
reduction of an actual root, whatever it is.

## Boundary

Out of scope and not promoted: input 1 section 3 (rzero cancellation),
r3, r=4,6 mod 7, r=5,12 mod 49, any cutoff, REG, source comparison,
full-source zero, all-F10, JC2. No new exit-price assertion; no
exit-price declaration line. Attacks that failed: sign of the p=3 term in d7
(3Y^2, not 3XY^2); the F_49 branch; the r-to-e sign; the c8(5) Y^2
cancellation. No decisive gap, so no early stop.

## Own readback, postpins and custody

Own WHOLE readback of this report done 04:03:47 UTC before sealing; the
verdict table, every displayed congruence and the five map identities
were re-read against the derivations above. Postpins at 04:03:47 UTC:
all five input SHA-256 values are byte-identical to the charged pins
listed under Inputs (unchanged after readback). Collision check: xmodel
holds only this report plus the harness .log and .run.v2 of this lane;
no other five49 file. Tools used: date, ls, wc, sha256sum, grep, cat,
sed and heredoc appends only. No code, CAS, interpreter, import, AST,
syntax, test, fixture, network, AWS, SSH, process, service, protected
jc2-lean or mirror, peer or live file, shared edit or new agent. Custody,
manifest, expected-finalizer verification and terminal author/idle
collection belong to ROOT via external ops/lane.sh; no local finalizer
was run. The standalone marker below is the last content.

<!-- BODY-END -->
