# Fable5.1 independent hostile gate: F10 coalesced reduction and standalone ODE

Fable5.1, September9,2026, invitation 09:26:50Z. Independent gate over fields of
characteristic zero. Both charged proofs were read WHOLE from the lane inputs and
every arrow below was rederived by hand; ZERO mathematical subprocesses of any size.
No F10 source theorem, source review, D28, peer body, log, receipt or AWS was used.

Inputs (full-file SHA-256, matching the artifact JSON full_sha256 fields):
- f10-coalesced-resonance-reduction-coordinator-20260909.md d225258c605617037d4d74b2cdce9430ce1fc8ac49e81d01dc1b125d76ad0ee1 (body 70f894ac..., 14218 B)
- f10-cubic-resonance-ode-discriminator-astra-20260909.md 38cf3fb95cdc7a0298fa5b35f56ab08dec5b64a40f4d2fc8d7976d189b23538c (body 5e113c2e..., 12649 B)
- the two .artifact.json files 9889e44d... and 75791586...

## Summary verdicts

| Item | Verdict | First precise failure |
|---|---|---|
| A finite reference, budget, simple minimizer | CONFIRMED | none |
| B cubic right coordinate | CONFIRMED | none |
| C coalesced whole B, r=(7m-1)/(3m) | CONFIRMED | none |
| D resonance supports and ODE | CONFIRMED | none |
| E first-contact narrowing d=2m, j=7q+9, F_j | CONFIRMED | none (quantifier note below) |
| F standalone equivalence and uniform existence | CONFIRMED | none |
| G normalized recipe | CONFIRMED | none; one non-load-bearing wording note |
| H composition | CONFIRMED compatible; no exclusion follows | source data listed below |

No verdict below depends on a producer statement; where I reproduce their numbers it
is because my own derivation lands on the same value.

## A. Finite canonical A-reference, F nonzero, budget (C), simple minimizer

Reference. R=K+sum s^i R_(7-i), f_s(T)=T^m+sum_(i<=m-2) alpha_i s^(7(m-i))T^i,
A_s=f_s(R)+F. At s-order i<=7 the coefficient of A_s is homogeneous of degree
7m-i, and mK^(m-1)R_(7-i) has exactly that degree, so a component in the image of
multiplication by mK^(m-1) is removable, uniquely because multiplication by a nonzero
polynomial is injective. At i=7 the image of the scalars is the line spanned by
K^(m-1), which is why T^(m-1) is absent from f_s. At order i>7 the coefficient has
degree 7m-i<7(m-1), so a nonzero one is never divisible by K^(m-1). The alpha_i
steps sit at orders 7(m-i)>=14 in increasing order and do not touch orders <=7 or any
earlier alpha order; a scalar K^i component at order 7(m-i) is removed against a fixed
complement of the line spanned by K^i. Everything is a finite sequence of finite
linear-algebra choices: CONFIRMED.

F nonzero. If F=0 then A=f_1(R_1) at s=1 and [A,B]=f_1'(R_1)[R_1,B]. f_1'(T) has
leading term mT^(m-1) and R_1 has degree 7 with top K, so f_1'(R_1) has degree
exactly 7(m-1)>=21>3 and cannot divide the nonzero cubic 2c a^3. CONFIRMED. Hence
j=ord_s F>=1 (A_s and f_s(R) agree at s=0), F_j lies in a complement of the
K^(m-1)-image for j<=7 (a complement meets the image only in 0), has degree
<7(m-1) for j>7, and is never a scalar K^i (i=m-i' would put it at order 7(m-i),
where the complement of the K^i line was imposed). CONFIRMED.

Budget (C). delta=min ord_L(F_j)/e_L over b, b-a, b+a with e=1,3,3. delta>=m-1
would give K^(m-1)|F_j, so delta<m-1 and L=m-delta>1. Integral delta=t: K^t|F_j,
F_j=K^t G, deg G=7L-j>=0, and 7L-j=0 makes F_j a scalar K-power; so j<=7L-1,
Delta=1. delta=t+1/3: the minimum is at a triple line (a simple line gives an
integer), so ord_b>=t+1 by integrality and ord_(b+-a)>=3t+1; total >=7t+3, so I
get 7m-j>=7t+3, i.e. j<=7m-7t-3=7L-2/3 with 7L=7m-7t-7/3. delta=t+2/3: ord_b>=t+1,
ord_(b+-a)>=3t+2, total 7t+5, j<=7m-7t-5=7L-1/3. All three lines of (C) CONFIRMED,
with Delta=1,2/3,1/3 and no G>=2j premise anywhere.

Simple minimizer. Then delta=d=ord_b F_j<=m-2 is an integer. z=R inverts to
b in kbar[a^(+-1)][[s,z]] because d_b K at b=0 is -a^6, a unit; weights s,a:1, z:7,
b:1 are preserved. F=sum c_l z^l with ord c_d=j, ord c_l>=j+d-l for l<d, ord
c_l>=j for l>d. eta=min ord c_l/(m-l) over l<=d satisfies eta<=j/(m-d)=j/L<7 by
(C); for l>d the ratio exceeds j/(m-d). So the initial at m*eta is P=Y^m+U with U!=0
of degree <=d<=m-2; alpha_i terms are later by (m-i)(7-eta)>0. W=B_s-R^n is
divisible by s, so every z-coefficient has s-order >=1; an earlier B initial Q at
nu<n*eta has top Y-degree v with v*eta<=nu-1<nu and a-weight of q_v equal to
7n-nu-v(7-eta)>7n-7nu/eta>0. Target in (a,z) coordinates is 2c s^N a^3 b_z with
b_z(0,0,a)=-a^(-6), so order N, and N+eta after z=s^eta Y. Bracket of initials sits
at m*eta+nu<(m+n)eta, and (m+n-1)eta<=(m+n-1)j/L<=7(m+n-1)-(m+n-1)Delta/L, so
N-(m+n-1)eta>=2+(m+n-1)Delta/L>0: the initials commute. The Y^(m+v-1)
coefficient of [P,Q] is m*(q_v)_a (P_a has degree <=m-2), so q_v is a-constant,
contradicting positive weight. At nu=n*eta Q is monic of degree n and commutes;
n Q P_Y=m P Q_Y from the two Euler identities, so Q^m/P^n is Y-free and equals 1,
Q^m=P^n, coprimality gives P=(Y+t)^m, the absent Y^(m-1) term gives mt=0, U=0.
CONFIRMED. The triple minimizer has d=3delta<3(m-1), i.e. d<=3m-4: CONFIRMED.
The nonvanishing of the target on b=0 is not even needed for the commuting step
(a target vanishing there would be later still); the report's caution is harmless.

## B. Cubic right coordinate

zeta0=X^(1/3)(X^2-a^2) gives zeta0^3=X(X^2-a^2)^3=K exactly. a^2=X^2-X^(-1/3)zeta0
is exactly linear in zeta0, so a=eps X(1-X^(-7/3)zeta0)^(1/2) is a formal series in
zeta0 over kbar[X^(+-1/3)] with a_zeta0=-1/(2aX^(1/3)), equal to -eps X^(-4/3)/2 at
zeta0=0, nonzero: invertible. Weights s,X:1, zeta0:7/3, a:1 are consistent.
Elimination: at order s^l write f_l=zeta^2 h_l+a_l zeta+b_l; zeta->zeta-s^l h_l/3
changes zeta^3 by -s^l zeta^2 h_l+O(s^(2l)) and changes alpha*zeta, beta only at
order >=l+1 since alpha,beta lie in sE[[s]]. Each map is zeta+s^l(series in zeta),
composable s-adically in E[[s,zeta]]; for a fixed monomial s^a zeta^b only finitely
many (l,k) pairs contribute, so no negative exponent and no convergence issue. h_l
has weight 7/3-l, alpha weight 14/3, beta weight 7. Both deformations are carried
into Section 4/5 and only removed there by integrality. All F and W coefficients
keep integral s-orders (>=j, >=1) and the zeta-multiplicity d of F_j is preserved
because zeta0 vanishes simply on the chosen line and zeta=zeta0+O(s). Bracket:
with b=X the Jacobian factor is a_zeta, so [A,B]_(zeta,X)=2c s^N a^3 a_zeta; at s=0
a^3 a_zeta0=-a^2/(2X^(1/3))=-X^(5/3)/2+X^(-2/3)zeta0/2 exactly, giving (E) and the
transverse term +cX^(-2/3)zeta0, both independent of eps. CONFIRMED.

## C. Coalesced whole B

Bound (F): r<=ord c_d/(3m-d)=j/(3L)<=7/3-Delta/(3L)<7/3. Initial of A at 3mr is
V^m+U, U!=0, deg U<=d<=3m-4; l>d terms are later by at least r, scalar terms by
(m-i)(7-3r)>0; the R^n part contributes nothing before 3nr under lambda_split>=r.
Earlier B initial at nu<3nr: v r<=nu-1, first bracket order theta=(3m-1)r+nu
(one Y-derivative, order -r). theta>N: bracket has no s^N term, target does,
contradiction. theta<N: [P,Q]=0. theta=N: [P,Q]=-cX^(5/3), Y-free. In the last two
cases the Y^(3m+v-1) coefficient vanishes; P_X has degree <=3m-2 (V_X is linear),
so that coefficient is 3m q_v' and q_v is X-constant, against weight
7n-nu-vh>7n-7nu/(3r)>0 (v<nu/r, h=7/3-r). The v=0 case is included (weight
7n-nu>0). At 3nr, Q is monic of degree 3n, first bracket order (3(m+n)-1)r; if >N
the target is missed, if <N the Euler identities give nQP_Y=mPQ_Y, Q^m=P^n,
P=W0^m, and W0!=V forces deg U>=3(m-1) (the cofactor sum is monic of degree
3(m-1) in characteristic zero) while W0=V forces U=0. Hence
(3(m+n)-1)r=N: 3(m+n)-1=24q+32=8m, N=56q+72=8(7q+9), r=(7q+9)/m=(7m-1)/(3m)<7/3.
The coefficient is 3(m+n)-1 because exactly one transverse derivative lowers the
order. CONFIRMED.

## D. Resonance supports and the bracket ODE

gcd(7q+9,3q+4)=1 from 3(7q+9)-7(3q+4)=-1. 3r=7-1/m is not integral; 2r integral
would need 3m|14m-2, hence 3m|m+2, impossible for m>=4. Integral ord alpha,ord beta
with >=2r,>=3r are therefore >2r,>3r: V=Y^3. An initial F index l has
(3m-l)(7q+9)/m integral, so m|l, l in {0,m,2m}; a B correction index l has
(3n-l)r a positive integer, so l=1 mod m, l<5m+1. h=1/(3m); weights of P and Q are
1 and n/m; the Y^l coefficient of P has weight 1-l/(3m), so p_(2m)=lambda X^(1/3),
p_m=vX^(2/3), p_0=wX, i.e. P=XC(T), T=Y^m/X^(1/3); the Y^(im+1) coefficient of Q has
weight (5-i)/3, so Q=X^(5/3)YD(T), D monic quintic. Scalars because homogeneous
elements of kbar[X^(+-1/3)] are monomials. With T_Y=mT/Y, T_X=-T/(3X):
P_Y Q_X-P_X Q_Y=X^(5/3)[(5m/3+1/3)TC'D-mTCD'-CD]; the T^2C'D' terms cancel; times 3
this is (5m+1)TC'D-3mTCD'-3CD=-3c. Same sign at eps=+1,-1 since a^2=X^2 at both.
The later term cX^(-2/3)zeta=c s^r X^(-2/3)Y is a separate condition at order N+r
on the next initials; (B) is the leading equation only, as the report states.
CONFIRMED.

## E. First-contact narrowing

Reciprocal step. With T=1/x, C=x^(-3)c0, D=x^(-5)d0, C'(T)=3x^(-2)c0-x^(-1)c0',
D'(T)=5x^(-4)d0-x^(-3)d0', so TC'D=3x^(-8)c0d0-x^(-7)c0'd0,
TCD'=5x^(-8)c0d0-x^(-7)c0d0', CD=x^(-8)c0d0. The x^(-8) scalar is
3(5m+1)-15m-3=0 and (B) becomes 3m c0 d0'-(5m+1)c0'd0=K0 x^7 exactly, K0=-3c.
(d0 c0^(-a0))'=c0^(-a0-1)K0x^7/(3m), so d0=c0^(a0)+O(x^8) and the x^6,x^7
coefficients of c0^(a0) vanish. With c0=1+vx^2+wx^3 those are
binom(a0,3)v^3+binom(a0,2)w^2 and 3binom(a0,3)v^2w=a0(a0-1)(a0-2)v^2w/2; a0=n/m is
in (5/3,7/4], never 0,1,2, so v=0 or w=0, then both vanish, C=T^3, C(0)D(0)=c=0.
Contradiction: lambda!=0 and the initial contains Y^(2m), so 2m<=deg U<=d.
Budget. r<=j/(3m-d) and j<=7(m-d/3)-Delta give, with r=7/3-1/(3m),
7m-7d/3-1+d/(3m)<=7m-7d/3-Delta, i.e. Delta<=1-d/(3m). d=0 mod 3: 1<=1-d/(3m)
forces d=0<2m. d=1 mod 3: d<=m<2m. d=2 mod 3: d<=2m, and 2m=6q+8=2 mod 3 is
consistent. So d=2m and j=m r=7q+9 with equality throughout; the equal budget forces
ord_b F_j=2q+3, ord_(b+-a)F_j=6q+8, total 14q+19=7m-j=deg F_j, so
F_j=lambda b^(2q+3)(b^2-a^2)^(6q+8) with no room for another factor. In the
chart: b^(2q+3)(b^2-a^2)^(2m)=X^(1/3)zeta0^(2m) since 2q+3-2m/3=1/3, and
zeta=zeta0+O(s), so c_(2m)=s^j lambda X^(1/3)+..., which is exactly the T^2
coefficient of C. The consistency j=ord c_(2m)=mr with ord c_l>=j for all l is
closed, not circular. Both triple lines carry the same zeta0, the same F_j and the
same target, so no second-chart sign contrast exists. CONFIRMED.
Quantifiers: the theorem is about the minimising factor and the FIRST nonzero
s-order j of F only; it is a necessary condition (coalesced triple minimiser implies
(A) and (B)) and asserts no converse, no realisation and nothing about
lambda_split<r. The report says exactly this. Ties are covered: a simple line tied
for the minimum still has integral delta and dies under A.

## F. Standalone equivalence and existence

Equivalence. The reciprocal identity above is the same computation, so
(1) with scalar k is exactly W:=3mcd'-(5m+1)c'd=kx^7 for c=x^3C(1/x), d=x^5D(1/x),
monic in T if and only if c(0)=d(0)=1, with no degree condition needed. f_N is the
finite partition sum: (1+y)^a=sum binom(a,r)y^r, y=ux+vx^2+wx^3, and
binom(a,r)r!/(i!j!l!)=(a)_(i+j+l)/(i!j!l!): CONFIRMED. If f6=f7=0 and d=[c^a]_(<=5)
then d-c^a=O(x^8), W=3mc^(a+1)(dc^(-a))'=O(x^7), and deg W<=7 gives W=kx^7.
Conversely W=kx^7 gives (log d-a log c)'=O(x^7), formal integration in
characteristic zero gives d=c^a+O(x^8), so the coefficients of d are f0..f5 and
f6=f7=0. CONFIRMED, no omitted middle coefficient.
k=0 exclusion. W=0 is (d^m/c^h)'=0 with 3h=5m+1, so d^m=c^h; for an irreducible
factor of multiplicity e in c, m|e by gcd(h,m)=1, and e<=3<m forces c=1, then d=1.
So every nonzero point of (3) has k!=0; deg W=7<=deg c+deg d-1 forces deg c=3,
deg d=5, w!=0, f5!=0, and [x^7]W=15m w f5-3(5m+1)w f5=-3w f5. CONFIRMED.
Existence for every m. a=5/3+1/(3m) lies in (5/3,7/4], so binom(a,6),binom(a,7) are
nonzero for all m in the family; F=f6(X,Y^2,Z^3), G=f7(X,Y^2,Z^3) are honest forms of
degrees 6,7 with constant nonzero X-leading coefficients. Because the leading
coefficients never vanish, the Sylvester determinant commutes with every
specialisation of (Y,Z) and vanishes exactly at common X-roots; it is homogeneous
of degree 42. R=0 identically: any (Y,Z)!=0 gives a common finite X. R!=0: a nonzero
binary form of degree 42 over an algebraically closed field has a projective zero
(a root of R(Y,1), or the point (1:0) when R=const*Z^42). Either way a nonzero
(X,Y,Z) with F=G=0, hence (u,v,w)=(X,Y^2,Z^3)!=0 solving (3). Coefficients are
rational, so the point exists in Qbar and in every algebraically closed field of
characteristic zero. CONFIRMED; no resultant value is needed or claimed.

## G. Normalised recipe

u=0: f6(0,v,w)=(a)_3v^3/6+(a)_2w^2/2, f7(0,v,w)=(a)_3v^2w/2 (only (j,l)=(3,0),(0,2)
and (2,1) partition 6 and 7 with i=0), (a)_2,(a)_3!=0, so v=w=0: CONFIRMED. Scaling:
C_t'=t^(-2)C'(tT), D_t'=t^(-4)D'(tT), every term of (1) is t^(-8)(value at tT), so
k_t=t^(-8)k and reciprocal coefficients (u/t,v/t^2,w/t^3): CONFIRMED. The two
displayed equations: I enumerated all (i,j,l) with i+2j+3l=6 and 7 and recover
exactly the seven and eight displayed terms with the stated factorials. CONFIRMED.
Prescribed k_star is reached by t^8=k/k_star and the report correctly refuses to
assume u=1 at the same time. Finiteness: a common factor of F,G would have a zero on
X=0 (F(0,Y,Z) is not identically zero), contradicting the u=0 computation, so R!=0
and the projective intersection is finite; the normalised (v,w) set is its image
under (1:Y:Z)->(Y^2,Z^3). CONFIRMED. Non-load-bearing note: "up to scaling" is a
K^*-family times a finite set; for a PRESCRIBED k the solution set is finite, since
t is then determined up to eighth roots of unity. This sharpens, not contradicts,
the report.

## H. Composition and what is still missing

Compatible. The reduction produces a solution of (B) with T^2 coefficient
lambda!=0, simple disjoint nonzero roots and right side -3c; the standalone theorem
says such solutions exist for every m and any nonzero right side and that every
solution has a nonzero T^2 coefficient. The two reciprocal computations coincide.
Hence NO contradiction can come from (B) alone, exactly as both reports say; a
claimed ODE-only exclusion of the coalesced triple regime would be false.
Composing them yields one new necessary relation, not a kill: with the finite
normalised set {(v_i,w_i)} and k_i=-3w_i f5(1,v_i,w_i), the source datum must
satisfy (lambda,v,w)=(1/t,v_i/t^2,w_i/t^3) with t^(-8)k_i=-3c, i.e.
lambda^8 k_i=-3c for some i. Whether F_j's scalar and the bracket scalar obey this
is source information not present in either proof.
Still missing after ODE existence: the values v,w (from F at s-orders 2j,3j) and
the five D coefficients (from W at orders k0..5k0); the order N+r transverse
equation with target cX^(-2/3)Y and every later order; the separated regimes
lambda_split<r; the simple line b=0 with ord_b F_j=2q+3 as a second local chart;
global polynomiality and the finite degrees 7m,7n of A,B; the inverse or
reverse-source lift and the F10 orientation/sign convention. None of: a source
realisation, an ordinary receiver, an inverse lift, a JC2 result, a no-case claim
or a computational certificate follows from A-G. This is a local necessary
reduction; a realised formal or full source would need all of the above.

## Perimeter and own checks

Read: the four charged inputs only, whole. No historical or provenance paths were
followed, no source, peer, D28, F2 or F10 body, no protected jc2-lean tree, no
fetch, no AWS/SSH, no agent, no Python/CAS/script of any size. Written: this file
and box/f10-coalesced-resonance-gate-fable5-20260909/ (README and input hashes)
only. No OPEN token is raised here and no existing one is consumed or closed; no
seal or charge_basis line is authored. Own whole-body read and the own-only
raised-OPEN/collision check were done before the marker was appended.

<!-- BODY-END -->
