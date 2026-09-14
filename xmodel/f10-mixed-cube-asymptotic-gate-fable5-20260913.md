# FIRST gate (Fable 5.1): all-seven-branch asymptotic mixed-scalar nonvanishing

Fable 5.1, September 13, 2026, independent different-model FIRST on
xmodel/f10-mixed-cube-asymptotic-root-20260913.md. Mathematical gate only:
no source/runtime review, no CAS, no interpreter, hand arithmetic only.
Not an all-r unit conclusion, effective cutoff, source exclusion, REG,
comparison or JC2 conclusion; none is requested and none is asserted.

## Custody

Charged pins, all matched by sha256sum before whole reads, in charged order:

- input1 xmodel/f10-mixed-cube-asymptotic-root-20260913.md
  1c33e474a4378c88603a5591f1b227e08b17ab5ab25c1c9841d93b3f5397ec6b
- input2 xmodel/f10-mixed-univariate-reduction-root-20260912.md
  7b8545a623a771ebd423b441c4c1567389d0ca837d4e5b80c8990bc52b1075f8
- input3 box/ideation-20260912T2150Z-prep/COORDINATION.snapshot.md
  33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597

The rank-seven/septic whole-leading map of input2 is imported at its
recorded tier (AUDIT 17zzd, DOCUMENTARY/MANUAL, UNPROMOTED), not re-reviewed.
Provenance: input1's statement that both initial whole reads followed fresh
pins is too strong for the reduction note's first read; ROOT completed a fresh
whole read after matching pins before this invitation. No formula depends
on this. The concurrent Astra lane was not read.

## 1. Hand recomputation of every NEW item in input1

Coordinates. With s=1-v/3, u=v/s: s^3 phi = s^3+v s^2+X v^2 s+Y v^3
= 1+(X-1/3)v^2+(Y-X/3+2/27)v^3, and c=Y-1/27-a/3=Y-X/3+2/27. CONFIRMED.
du=(s+v/3)/s^2 dv=dv/s^2, u^-(k+1)=s^(k+1)v^-(k+1), phi^t=s^(-3t)C^t, so
d_k=[v^k]s^(k-1-3t)C^t. Formal substitution v=u+O(u^2) is a k[[u]]
automorphism; residue invariance needs no root choice. CONFIRMED (2).

Boundary. At t=5/3 the d6 exponent is 0, the d7 exponent is 1.
binom(5/3,2)=5/9, binom(5/3,3)=-5/81. [v^6]C^(5/3)=(5/9)c^2-(5/81)a^3;
d7=[v^7]C^(5/3)-d6/3, so G=[v^7]C^(5/3)=binom(5/3,3)*3a^2c=-(5/27)a^2c.
CONFIRMED (3). Lex c>a: S(c^2-a^3/9, a^2c)=-a^5/9; the pairs with a^5
reduce to 0; standard monomials 1,a,a^2,a^3,a^4,c,ac, length 7. CONFIRMED.

Septic at the boundary (independent check, requested). At t=5/3 from
input2: U=3X^2-2X+1/3=3a^2; V=X^3-(8/9)X^2+(7/27)X-2/81=a^2(a+1/9);
K=a^3-a^2-2a/9-1/81; P=9a^4[(a+1/9)^2+a^3-a^2-2a/9-1/81]=9a^7. Bezout
constant A=(3t-5)(3t-4)(2t-3)/15 vanishes at delta=0, so U is NOT a unit
on the boundary algebra; indeed UY=V there forces c=0 for a!=0, and the
two-equation quotient then forces a=0: the whole boundary support sits on
U=0. Input1 correctly refuses Q[a]/(a^7) and derives the branches from
(d6,G). For delta!=0 small, A has a simple zero, so A*U0!=0, U is
invertible mod P, and P (leading coefficient 9 for every t) has exactly
seven complex roots. CONFIRMED, including the "count only" use of P.

Delta-linear constants. d6 exponent is -3delta: [v^6](-3delta log(1-v/3))
= -3delta*(-1/4374)=delta/1458. d7 exponent 1-3delta:
delta/5103-delta/4374=(6-7)delta/30618=-delta/30618. G constant:
-1/30618+7/30618=1/5103 (also directly [v^7](1-v/3)^(-3delta)).
CONFIRMED both constants and (4). A delta-linear term with a or c has
weight >=9; delta^2 terms >=14. CONFIRMED.

Scaled system. A^2C0=27/(5*5103)=1/945; (A^2C0)^2=A^7/9 gives
A^7=9/893025=1/99225. Seven distinct nonzero A, each with unique
C0=1/(945A^2), consistent with A^3=9C0^2. Jacobian:
(5/27)^2A^4+(10/9)(10/27)AC0^2=(75+100)A^4/2187=175A^4/2187!=0.
Polynomial equations in (h,A,C0), simple zeros at h=0: analytic IFT gives
seven convergent branches, a_j=h^2A_j(h) pairwise distinct for small
h!=0. CONFIRMED (5) and the branch count.

Exhaustion. On each branch d6=G=0, U=3h^4A_j(0)^2+O(h^5)!=0, so Y=V/U and
U^2*d6/c3=P(X_j)=0 with c3,t-2 units near 5/3: seven distinct roots of a
degree-7 P exhaust it and prove it squarefree there. No solution with U=0
exists since A*U0!=0. Y d5 -> (1/27)(1/243)!=0. CONFIRMED: the seven
branch points are the full complex spectrum of S_r for small delta!=0.

Trace identity. det(I-uM)=u^3 q0(1/u)=phi(u); phi'/phi=-sum Tr(M^(k+1))u^k.
With T_1T_2=sum e_m u^m, [u^14](phi'/phi T_1T_2)=-sum e_m Tr(M^(15-m)),
and wA_1A_2=sum e_m w^(15-m). CONFIRMED B=-Tr(wA_1A_2), polynomial in
X,Y,t. Shift: (z-1/3)^3+(z-1/3)^2+X(z-1/3)+Y=z^3+az+c. CONFIRMED. The
same map v=u/(1+u/3) sends 1/z to 1/w, w^7=z^7(1-v/3)^7, and
u^k(1-v/3)^7 is a degree-7 polynomial, so Q_s is degree<=7 and equals
trunc_7[(1-v/3)^(7-3s)C^s] by agreement through v^7. CONFIRMED (6).

Weights. Exponents 7-3(2t-1)=-6delta, 7-3(4-t)=3delta. A term
delta^n a^i c^j v^k of Q_s has weight 7n+2i+3j+7-k>=7 in A_s, with
equality only at n=0,k=2i+3j (the weight-7 A) or n=1,i=j=0,k=7. The
latter are -6delta*(-1/15309)=2delta/5103 and 3delta*(-1/15309)
=-delta/5103. CONFIRMED (7). q is weight-3 monic, so reduction and trace
preserve weight; -z A_1A_2 has weight>=15; the weight-14 part is
(1/3)Tr of the product of (7). CONFIRMED.

Finite trace. binom(7/3,2)=14/9, binom(7/3,3)=14/81.
A=z^7+(7/3)az^5+(7/3)cz^4+(14/9)a^2z^3+(28/9)acz^2
 +[(14/9)c^2+(14/81)a^3]z+(14/27)a^2c. Mod q: z^4=-az^2-cz,
z^5=-cz^2+a^2z+ac, z^7=2acz^2+(c^2-a^3)z-a^2c. Collecting:
alpha=(2-14/3+28/9)ac=(4/9)ac; beta=(1-7/3+14/9)c^2+(-1+7/3-14/9+14/81)a^3
=(2/9)c^2-(4/81)a^3; gamma=(-27+63-42+14)/27 a^2c=(8/27)a^2c. Newton with
e1=0,e2=a,e3=-c: p2=-2a,p3=-3c,p4=2a^2. TrA=-(8/9)a^2c+(8/9)a^2c=0.
On a^3=9c^2, beta=-(2/81)a^3 and, in units a^7/6561: 2a^2alpha^2=288,
-6c alpha beta=+48, -2a beta^2=-8, -4a alpha gamma=-384, 3gamma^2=192;
sum 136. CONFIRMED. Cross terms vanish by TrA=0; the constant product
gives (1/3)*3*(2/5103)(-1/5103)delta^2=-2delta^2/5103^2. Since
99225/5103^2=(3^4 5^2 7^2)/(7^2 3^12)=25/6561, that is -150a^7/19683;
136-150=-14; -14/(19683*99225)=-14/1953045675=-2/279006525. CONFIRMED
(8) and (1); the coefficient depends only on A_j(0)^7=1/99225, hence is
identical on all seven branches.

Consistency control: at delta=0 all of B has weight>=14>8, the top
standard-monomial weight, so B=0 in the boundary algebra. CONFIRMED the
cube control is reproduced.

## 2. Analytic and generic-norm items

Uniform neighborhood. Each branch gives B_j(h)=sum_(n>=14) b_n h^n,
convergent, with b_14=-2/279006525!=0, so B_j!=0 on 0<|h|<eps_j; take
eps=min over the seven. For 0<|delta|<eps^7 pick any h with h^7=delta;
the seven branch points at that h are all seven roots of P_t, so B is a
unit of C[X]/(P_t), hence of Q[X]/(P_t)=S_r whenever delta=1/(3(3r+1)) is
below eps^7. CONFIRMED for all sufficiently large r; eps is not effective
and no R0 follows. No real-root or positivity input anywhere.

Generic norm. N:=prod_j B(X_j) is a rational function of t, single-valued
in delta, and equals (-2/279006525)^7 delta^14 (1+O(h)), so the correction
is O(delta) and the order is exactly 14. CONFIRMED. Since roots of P are
simple and U!=0 at them for small delta!=0, F(X_j)=U^7B(X_j)!=0, so
gcd(P,F)=1 over Q(t). CONFIRMED. Label note only: this N is not input2's
Bezout constant N(t) nor Res_X(P,F); those differ by U and 9 powers.

Finite exceptions. The numerator of N is a nonzero polynomial in t; B
fails to be a unit in S_r only at its rational zeros t=(5r+2)/(3r+1),
finitely many r. Nothing identifies or excludes any r>=2. CONFIRMED as
stated, with the whole-ring map at actual r imported from input2.

## 3. Verdict table on input1's literal claims

- (2) coordinate identity and residue form: CONFIRMED.
- (3) exact d6, G at t=5/3; length-7 quotient; Groebner list: CONFIRMED.
- U=3a^2 not invertible on the boundary; refusal of Q[a]/(a^7); septic
  used only to count for delta!=0: CONFIRMED (P->9a^7 recomputed).
- (4) weights and both delta-linear constants 1/1458, -1/30618, 1/5103:
  CONFIRMED.
- (5) seven simple solutions, A^7=1/99225, Jacobian 175A^4/2187: CONFIRMED.
- Seven convergent branches, distinct a_j, exhaustion of every component
  of S_r near delta=0, guard nonzero: CONFIRMED.
- Trace identity B=-Tr(wA_1A_2) and its shifted form (6): CONFIRMED.
- (7) weight-7 truncation with constants 2delta/5103 and -delta/5103,
  all other terms weight>=8: CONFIRMED.
- alpha,beta,gamma, moments, TrA=0, TrA^2=136a^7/6561: CONFIRMED.
- (8) and (1): B=-2delta^2/279006525+O(delta^(15/7)), same coefficient on
  all seven branches: CONFIRMED.
- Unit for all sufficiently small complex delta!=0 and all sufficiently
  large r: CONFIRMED, non-effective.
- Norm order 14, leading (-2/279006525)^7, generic gcd(P,F)=1: CONFIRMED.
- Finite but unidentified exceptional r: CONFIRMED as a finiteness
  statement only.
- Cube control B=0 at delta=0 reproduced: CONFIRMED.
- Provenance sentence on both initial whole reads: over-stated for the
  reduction note's first read (see Custody); affects no formula.

No REFUTED item. No mathematical GAP found in the charged scope. Not
established here and not claimed: any integer cutoff R0, any all-r unit
statement, exclusion of specific r, source arrays, REG/comparison, all-F10
or JC2 consequences. No exit-price assertion is made.

<!-- BODY-END -->
