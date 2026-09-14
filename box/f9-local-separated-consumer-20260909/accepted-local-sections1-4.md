# Weight-free local consumers and the two-chart golden resonance

2026-09-09. Coordinator derivation. NEW / UNREVIEWED, conditional only on
the explicit reference hypotheses below. No receiver weights, polygons,
parity, finite g-degree normal blocks, or cubic-in-g reference is assumed.
This local proof is separate from the weight-free framework report. Its
composition with that framework and the conditional client map needs a
different-model hostile review before any weight-free source exclusion.

## 1. Exact reference hypotheses and conclusions

Work over a characteristic-zero field K, enlarged algebraically as needed.
Let H be either p²(g³+p³) or p²LM², where L=p+g, M=p+tg,
t=1-rho, rho²-3rho+1=0. Assume polynomial homogeneous dilations A_s,B_s
of combined degrees15,25 (s,g,p have degree1), with

    [A_s,B_s]_(g,p)=c*s^36*g², c in K nonzero,
    R_s=H+sum_(a=1)^5 s^a R_(5-a),
    A_s=R_s³+alpha*s^10*R_s+a0*s^15+F,
    B_s=R_s^5+sum_(i=0)^4 b_i*s^(25-5i)*R_s^i+q_s(R_s)*F+G,
    q_s(z)=(5/3)z²+(4/3)b4*s^5*z+(b3-5alpha/9)*s^10,
    j=ord_s F>=1, ord_s G>=2j.

All coefficients R_(5-a) are homogeneous polynomials of the indicated
ordinary degrees, and alpha,a0,b_i are field scalars. F,G have combined
degrees15,25. These are hypotheses, not consequences of a weighted theorem.
In particular B_s-R_s^5 belongs to sK[s,g,p] from the common top alone.

At a simple factor of H suppose F_j=H*C and C does not vanish there,
with j<=9. We prove this impossible. At a double factor T of H let
d=ord_T F_j. We prove impossibility for d=2,j<=9; d=3,j<=7; and
d=1,j<=11. For d=1,j=12 the only possible balance is the coalesced
resonance specified in section5. If F12=lambda*pLM, lambda nonzero,
the two actual double charts p and M force incompatible scalar equations.

The independently authored framework cbc0330b001faeb8692e45c3be3fdcd3c0727b5734e648143642234da5d63696
rederives the reference hypotheses and conditional factor cover; it is NOT
an accepted premise here. Root verified its terminal transaction and pins
before whole reading. The proof below uses only the stated hypotheses and
standard characteristic-zero formal inversion, Euler differentiation and
factorization in one-variable polynomial rings over fields. The weighted
source14c4cded and reviewed15n/p motivated parts of the calculation, but
their excluded sources and weight-dependent normality are not invoked.

Use X for a nonzero generic coordinate along the selected line and y for
the transverse affine coordinate. For p=0 take (y,X)=(p,g); for a V,L,M
root take (y,X)=(g,p). Thus [A,B]_(y,X) has sign minus at p=0, plus
otherwise. In every named chart g at the root is a nonzero multiple of X,
so the target has s-order36 and a nonzero generic coefficient.

## 2. Euler tools and the simple-root consumer

Use the coefficient field E=Kbar(X^(1/2)), with the usual X-derivation;
the simple chart already works over Kbar(X). Suppose P is monic of
positive degree m in Z, Q!=0 has degree n, [P,Q]_(Z,X)=0, and
(X*d_X+h*Z*d_Z)Q=Lambda*Q. The coefficient of Z^(m+n-1) in the bracket
is m*q_n': P_X has degree at most m-1. Hence q_n'=0 and
(Lambda-n*h)q_n=0, so Lambda=n*h. This includes n=0, but requires m>=1
and a field. It does NOT require Euler homogeneity of P. For example,
P=1,Q=X violates the conclusion if m=0 is allowed.

If P,Q are monic of degrees3e,5e, are Euler homogeneous of degrees3e*h,
5e*h with h!=0, and commute, then

    X[P,Q]=h*(5e*P_Z*Q-3e*P*Q_Z)=0.

Thus Q³/P^5 is Z-constant; monicity makes it1. Unique factorization in
E[Z] gives P=W³,Q=W^5 for a monic W of degree e. For e=1 a depressed
cubic forces W=Z. For e=2, if P=(Z²+b)³+U with deg U<=3, its Z5/Z4
coefficients force W=Z²+b, hence U=0. A common quadratic without that
degree restriction is not excluded by this argument.

At a simple factor H_y is a unit over Kbar(X). The formal inverse
R_s(y,X)=z exists with nonnegative s,z powers and combined degree1.
Write F after this inverse as sum f_n(s,X)z^n. Every ord f_n>=j;
ord f_1=j and q=ord f_0>j, with infinity permitted, because at s=0 the
coefficient F_j is z times a function with nonzero constant C-value.
Put eta=min(j/2,q/3). It is finite and 0<eta<=9/2. After z=s^eta Z,
terms n>=2 have order>=j+2eta>3eta. The linear and constant terms have
order>=3eta with at least one equality. Therefore the A initial is

    s^(3eta) P,  P=Z³+u*Z+v, (u,v)!=(0,0).

The reference scalars lie later since eta<5. All B kernels are later
than5eta by (5-i)(5-eta)>0. The two lower q_s terms are later by
5-eta and10-2eta. The remaining (5/3)z²F is at5eta.
Since the inverse has nonnegative s-orders, each G coefficient has
order>=2j. Below5eta its only possible initial has Z-degree0, as
2j+eta>=5eta. If such an initial occurs at nu<5eta, its bracket with
P vanishes: 2eta+nu<7eta<36. Its Euler degree25-nu is positive, so
the preceding top-coefficient lemma kills it. At5eta G can contribute
a linear term and a constant, both retained. Thus B has a monic
quintic initial Q, Euler degree5h, and P degree3h, h=5-eta>0.
Here [A,B]_(z,X) equals the original target times y_z, a unit, of
order36; passing to Z multiplies it by s^eta. Hence 7eta<36 gives
[P,Q]=0. The monic-linear conclusion forces u=v=0, a contradiction.

## 3. General double-root chart and the coalesced regime

There is a formal critical point y_c(s,X) with R_y=0. Set xi_s=R_s(y_c,X),
kappa=ord xi_s>=1, infinity if xi_s=0. Taylor factorization for the
GENERAL degree5 polynomial, not a cubic, gives

    R_s(y_c+w,X)=xi_s+w² U_s(w,X), U_0(0,X)!=0.

Taking the formal square root of this unit defines zeta=w*sqrt(U_s).
The inverse w(s,zeta,X) has nonnegative s,zeta powers over E and
R_s=xi_s+zeta² exactly. Its combined degree is1, zeta has degree5/2,
and its leading derivative is a nonzero constant times X^(-3/2).
No finite Taylor truncation is claimed. Write F=sum c_n(s,X)zeta^n.
Every ord c_n>=j, ord c_d=j, and ord c_n>j for n<d. The last claims
follow from the exact transverse multiplicity of F_j and the inverse's
nonzero linear coefficient.

For d in {1,2,3} put r=min_(0<=n<=d) ord(c_n)/(6-n). It is finite,
positive and <=j/(6-d). Suppose kappa>=2r. For n<=d all terms have
order>=6r at zeta=s^rY and at least one attains it. Terms n>d have
order>=j+(d+1)r>=7r>6r. Thus F has a NONZERO polynomial initial U(Y),
deg U<=d, and R_s has initial Y²+b at2r. Here b=0 unless kappa=2r.
For r<5/2 all A scalar references are later, and

    P=(Y²+b)³+U(Y)

is monic6 at6r. This proof covers all higher terms of a general Morse
inverse and xi=0. Each coefficient of B_s-R_s^5 has s-order>=1, so a
possible earlier B initial at nu<10r has degree n with nr<=nu-1.
At10r R_s^5 supplies the unique monic degree10 term. If 15r<=36,
the earlier initial commutes with P since5r+nu<36. Its Euler factor
obeys, for h=5/2-r>0,

    25-nu-n*h > 25-5nu/(2r) > 0.

The positive-degree top-coefficient lemma excludes it. Hence B starts
at10r, monic10 and Euler homogeneous, while P has Euler degree6h.
If15r<36 the common-quadratic conclusion forces U=0, contradiction.
The bounds are 15r<=3j<=33 for d1,j<=11; 15r<=15j/4<=135/4 for
d2,j<=9; and15r<=5j<=35 for d3,j<=7. All are strict below36 and
r<5/2. For d1,j12 the same proof excludes r<12/5 but NOT equality.
That equality, analyzed below, forces kappa>=5 since kappa is integral.

## 4. Separated regime: exact regrouping before selecting a balance

Now kappa<2r, so xi is nonzero. For every n,

    ord(c_n)+n*kappa/2>3kappa.                         (7)

For n<=d use ord(c_n)>=(6-n)r and r>kappa/2. For n>d use
ord(c_n)>=j>=(6-d)r and n>=d+1. These inequalities include infinite
orders and do not use a finite expansion of F. Set

    U(z)=sum_(m>=0) c_(2m)*(z-xi)^m,
    V(z)=sum_(m>=0) c_(2m+1)*(z-xi)^m.

Every coefficient U_l,V_l has order>=j: for instance its m-th summand
is binom(m,l)c_(2m)(-xi)^(m-l), tending to infinite order as m tends
to infinity. Thus the regrouping is coefficientwise s-adically convergent.
Equation(7) implies

    ord(U_l)+l*kappa>3kappa,
    ord(V_l)+kappa/2+l*kappa>3kappa.                  (8)

Discreteness gives a strict lower bound after summation as well; cancellation
can only raise it. Let b_s=sqrt(-xi), ord b_s=kappa/2. The two sheets are

    zeta_pm=+/- b_s*sqrt(1-z/xi),
    F_pm=U(z)+/- b_s*sqrt(1-z/xi)*V(z).              (9)

Before the rescaling below, (9) is a series in E((s^(1/N)))[[z]],
whose individual coefficients can have negative orders. It is NOT asserted
to be a nonnegative-order Taylor series in z. Taking square roots may
require a finite Puiseux extension; because each combined-homogeneous
coefficient is a scalar times a rational power of X, no new X-dependent
transcendental coefficients are introduced. Both signs are retained.

Define, without adding across signs,

    q0=min(ord U_0, kappa/2+ord V_0)>3kappa,
    q1=min(ord U_1, kappa/2+ord V_1)>2kappa,
    eta=min(q0/3,q1/2)>kappa.                        (10)

These orders may individually be infinite, but eta is finite:

- d1: ord V_0=j, since its c1 term has orderj and all later terms
  have order>=j+kappa. Thus eta<=(j+kappa/2)/3<2j/5.
- d2: ord U_1=j, with all terms after c2 later. Thus eta<=j/2.
- d3: ord V_1=j, with all terms after c3 later. Thus
  eta<=j/2+kappa/4<2j/3.

The strict inequalities use kappa<2r<=2j/(6-d). In all stated ranges
(including d1,j12), eta<j and eta<5. At z=s^eta Z every positive
binomial correction in (9) is later than its OWN base by a positive
integer multiple of eta-kappa. Bases with l>=2 have order>=j+2eta>3eta.
The l=0,1 bases have order>=3eta, and at least one attains it. An
attained coefficient has two-sheet tuple (a+b,a-b), which cannot vanish
on BOTH sheets unless a=b=0 in characteristic zero. Different l values
are different Z-degrees. Consequently the actual A initials on both sheets
are depressed monic cubics

    P_pm=Z³+u_pm*Z+v_pm,
    (u_+,v_+,u_-,v_-) != (0,0,0,0).                (11)

One entire sheet correction may vanish; it gives no contradiction alone.
The scalar references are later since eta<5. Each P_pm is Euler
homogeneous of degree3h for h=5-eta>0, with derivation X*d_X+h*Z*d_Z.

Apply the SAME regrouping to the ENTIRE G. Its even/odd coefficient
functions all have order>=2j. The earliest order across the pair of sheets
is the minimum of base orders ord(U_(G,l))+l*eta and
kappa/2+ord(V_(G,l))+l*eta. This follows because positive binomial
shifts are later, different l values have distinct degrees, and the
two-sheet tuple at an attained degree cannot vanish on both sheets.
This is a statement about all coefficients, not a bounded sampling of G.

For d1, 5eta<2j, so G lies strictly after5eta. For d2 an initial below
5eta must have degree0, since2j>=4eta. For d3 such an initial has degree
at most1, since2j>3eta. In either latter case suppose its earliest order
nu<5eta exists and choose a sheet where it is nonzero. Every B kernel
and the lower q terms are later than5eta, exactly as in section2; z^5
and (5/3)z²F start at5eta. Thus this G initial is B's actual initial Q.

The transformed bracket in (z,X) is the signed source target times
y_z=y_zeta/(2zeta_pm). Substituting z=s^eta Z into that coefficient
gives order36-kappa/2; expressing the bracket instead in (Z,X)
adds eta by the chain rule. The generic original g and y_zeta have
nonzero leading values. The relevant strict bounds are

    d1: 7eta+kappa/2 <= (7j+5kappa)/3 < 3j <=36;
    d2: 7eta+kappa/2 <= 7j/2+kappa/2 <15j/4<=135/4<36;
    d3: 7eta+kappa/2 <= 7j/2+9kappa/4 <5j<=35<36.

Thus 2eta+nu<7eta<36-kappa/2, so [P_pm,Q]=0. If deg Q=0, its
Euler factor25-nu is positive. If deg Q=1, it is
25-nu-h=20-nu+eta>20-4eta>0 because eta<5 (in d3 actually<14/3).
The top-coefficient lemma gives a contradiction in either case.
Therefore G has no earlier initial on either sheet. At5eta it can
contribute at most a linear term and a constant for d2/d3, and nothing
for d1. Positive binomial shifts of earlier bases cannot reappear here:
we just proved that there is no earlier base across the two sheets.

The complete B initial on each sheet is consequently

    Q_pm=Z^5+(5/3)Z²*(u_pm*Z+v_pm)+ell_pm*Z+e_pm,   (12)

with ell=e=0 in d1. It is monic5, Euler homogeneous of degree5h.
The same strict bounds give [P_pm,Q_pm]=0. The common-linear argument
forces u_pm=v_pm=0 on each sheet, contradicting(11). This excludes
ALL separated cases d1,j<=12; d2,j<=9; d3,j<=7. No missing balance
eta=kappa is licensed: separated means strict kappa<2r and implies
strict eta>kappa. At equality the binomial shift argument would fail.
