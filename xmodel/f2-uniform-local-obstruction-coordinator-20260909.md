# Degree-five receiver obstructions uniformly in the output exponents

Coordinator /root, 2026-09-09. NEW / UNREVIEWED. Manual factored proof;
zero mathematical subprocess, CAS, source expansion, checker or AWS.
This is a local polynomial theorem, not a source-family or JC2 exclusion.

## 1. Statement, motivation and exact boundary

Let k have characteristic zero, c!=0, and 2<=m<n be coprime integers.
Consider polynomials A,B in k[g,p] whose ordinary leading forms are H^m,H^n
and whose Jacobian in the declared order (g,p) is c*g².

(S) If H=p²(g³+p³), no such pair exists for ANY coprime2<=m<n.

(G) If H=p²(p+g)(p+t*g)², t=1-rho, rho²-3rho+1=0, no such pair exists
provided n>=2m-1. Both embeddings of rho and finite extensions are allowed.

In particular both top patterns are excluded for every m>=2,n=2m-1,
the exponent family proposed for ordinary F2 sources. Independent nonzero
leading scalars may be removed by dividing outputs, preserving c!=0.
No weighted polygon, parity, lower face, inverse lift, B-reference or
ordG>=2ordF premise occurs in this theorem. The independent all-parameter
F2 source-interface task is NOT a premise; no same-degree-to-F2 selection,
existence of a source, or all-counterexample coverage is claimed.

The accepted degree-seven whole-B proof suggested the redesign. The older
degree-five3/5 proof supplied the two actual golden double-line coefficient
data. This proof rederives the local estimates and the NEW all-m resonance;
it does not assume that either earlier theorem generalizes automatically.
Read motivation: xmodel/f9-all-exponents-local-exclusion-coordinator-20260909.md
SHA2dba41ed5e07d62b2e96221e67fc2c3ba16325d1a99f0015f09194d285c3d192;
xmodel/d125-weightfree-local-consumer-coordinator-20260909.md
SHAd4fd2a0e6549edbf9e65f8aa59e2fc2a1d6bbbc0299188fdd6adf96f340c8f51.
Neither proof's computational controls are consumed. No current cross or
pending F2 source report is an input. We may extend k algebraically and
prove the stronger nonexistence there, so assume k algebraically closed.

## 2. Finite A-only normalization and the global multiplicity budget

Put D=5, A_s=s^(Dm)A(g/s,p/s), B_s=s^(Dn)B(g/s,p/s). All s,g,p have degree1,
and

    [A_s,B_s]_(g,p)=c*s^N*g²,  N=D(m+n)-4.              (1)

Construct the finite degree-D reference

    R_s=H+sum_(i=1)^D s^i R_(D-i),
    f_s(T)=T^m+sum_(i=0)^(m-2)alpha_i*s^[D(m-i)]*T^i,
    A_s=f_s(R_s)+F.                                     (2)

At orders1..D, choose a linear complement to multiplication by mH^(m-1)
in the appropriate homogeneous polynomial space. Remove that image
component by choosing R_(D-i); subsequent choices change only later
orders. At orderD the image is the scalar multiples of H^(m-1), accounting
for the absent T^(m-1) term. At later orders every nonzero residual has
degree<D(m-1) and cannot be divisible by H^(m-1). At each orderD(m-i),
i=m-2,...,0, remove the scalar H^i component by alpha_i*s^[D(m-i)]R_s^i.
These orders are>=2D; process them in increasing order, so earlier terms
stay fixed. No other homogeneous degree can carry a nonzero scalar H-power.

Thus if j is the first surviving order, its nonzero homogeneous F_j obeys

    H^(m-1) does not divide F_j,
    F_j is not a scalar multiple of any H^i.             (3)

F cannot be identically zero: at s=1, A=f_1(R_1) would make f_1'(R_1), of
degreeD(m-1)>2, divide the nonzero degree-two Jacobian in the polynomial
domain. All reference objects remain finite polynomials.

Let L_i be the distinct linear factors of H, with multiplicities e_i=1 or2,
and S their number of SIMPLE factors. Here S=3 for(S), S=1 for(G).
Choose a line minimizing

    delta=min_i ord_(L_i)(F_j)/e_i < m-1,  L=m-delta.

The multiplicities make delta integral or half-integral. Homogeneity and
(3) give the STRICT degree budget

    j<=D*L-Delta,
    Delta=1 for integer delta, Delta=S/2 otherwise.       (4)

Indeed for integer delta, H^delta divides F_j; equality of degrees would
make it a removed scalar power. For delta=a+1/2, each simple line occurs
at least a+1 times, each double line at least2a+1 times, a total degree
D*delta+S/2. No preliminary H|F_j or order2j assertion is used.
For a minimizing simple line d=delta<=m-2. For a minimizing double line
d=2delta<=2m-3. All these quantities, including j, are actual integer
orders before any Puiseux extension.

## 3. Formal local and Euler tools

At a simple factor use coordinates (y,X) with X generic and nonzero along
the line, and invert z=R_s(y,X). The inverse has nonnegative s,z orders.
At a double factor the formal implicit function theorem gives its unique
moving critical point y_c; Taylor factorization and a square root of its
unit coefficient give the EXACT Morse form

    R_s=xi(s,X)+zeta²,  kappa=ord_s xi>=1 or infinity.

Here y_zeta is a unit, zeta has degreeD/2 and coefficients lie in
E=k(X^(1/2)). Every inverse coefficient has nonnegative s,zeta orders.
For each displayed H the transverse quadratic coefficient is a nonzero
constant times X³, so this field suffices. Formal homogeneity follows by
uniqueness of the implicit inverse and square root. A finite Puiseux
extension of s allows rational scalings; it does not specialize X.

Elementary Euler lemma: if P is monic of degree M>0 in Z and Q!=0 has
degree v, then [P,Q]_(Z,X)=0 implies the derivative of its leading
coefficient q_v is zero: the coefficient of Z^(M+v-1) is M*q_v'.
If Q has Euler degree Lambda for X*d_X+h*Z*d_Z, then

    (Lambda-v*h)*q_v=0.                                 (5)

A positive Lambda-v*h is impossible in this field. This includes v=0.

If instead P,Q are both monic, degrees em,en, Euler degrees emh,enh,
h!=0 and they commute, then

    X[P,Q]=e*h*(n*P_Z*Q-m*P*Q_Z)=0.

Consequently Q^m/P^n is Z-constant and monicity makes it1. Coprimality
and unique factorization give P=W^m,Q=W^n with W monic degree e.
For e=1, P=Z^m+U, degU<=m-2, forces W=Z and U=0.
For e=2, P=(Y²+b0)^m+U, degU<=2m-3, the degree2m-1 and2m-2
coefficients force W=Y²+b0, again U=0. These are field arguments.

## 4. Simple lines and the entire B polynomial

In the simple inverse write F=sum f_l z^l. All ord f_l>=j and ord f_d=j,
by the exact transverse multiplicity of F_j and the unit linear inverse.
Put eta=min_(0<=l<=d)ord f_l/(m-l). Then eta is finite positive,
eta<=j/L<D. After z=s^eta Z the A initial is

    P=Z^m+U, 0!=U, degU<=d<=m-2,  at orderm*eta.

Terms l>d are later because j+l*eta>m*eta. Every lower scalar term in
(2) is later by (m-i)(D-eta)>0.

Use W_s=B_s-R_s^n, whose EVERY original local coefficient has s-order>=1.
An earlier B initial at nu<n*eta is a polynomial Q of degree v with
v*eta<=nu-1. Its Euler degree is Dn-nu and h=D-eta, giving

    Dn-nu-v*h >= Dn-D*nu/eta+(D/eta-1)>0.               (6)

The actual bracket target in (Z,X) has orderN+eta: the inverse derivative
is a unit and g at the selected line is a nonzero multiple of X. By(4),

    N-(m+n-1)*j/L >= D-4+(m+n-1)*Delta/L>0.             (7)

Hence the earlier Q commutes with P, contradicting(5)-(6). At n*eta,
W contributes only degree<n, so B has a monic degree-n initial Q;
(7) gives commutation, and the common-linear lemma contradicts U!=0.
This excludes every minimizing simple line for both patterns.

## 5. Coalesced doubles and the one possible equality

Write full F=sum c_l zeta^l. All ord c_l>=j and ord c_d=j. Set
r=min_(0<=l<=d)ord c_l/(2m-l), so0<r<=j/(2L)<D/2. If kappa>=2r,
including equality/infinity, the A initial at2m*r is

    P=(Y²+b0)^m+U, 0!=U, degU<=d<=2m-3,

with zeta=s^rY; b0=0 for kappa>2r. Higher F terms and scalar terms are
later, exactly by j+l*r>2m*r and (m-i)(D-2r)>0.
For full W_s=B_s-R_s^n, every zeta coefficient has order>=1. A B initial
Q at nu<2n*r has degree v with v*r<=nu-1 and Euler factor, h=D/2-r,

    Dn-nu-v*h >= Dn-D*nu/(2r)+(D/(2r)-1)>0.            (8)

The bracket target in (Y,X) is orderN+r. Therefore an earlier Q commutes
with P if (2m+2n-1)r<=N; its strictly earlier order makes this implication
strict even when that displayed bound is equality. At2n*r, B is monic2n.
If (2m+2n-1)r<N, its initial commutes with P and the common-quadratic
lemma contradicts U!=0.

Here is the global budget determining the possible equality:

    E0=N-(m+n-1/2)*j/L
      >= -3/2+(m+n-1/2)*Delta/L.                       (9)

For integer delta, Delta=1 and (m+n-1/2)/L>2, so E0>1/2.
For(S), half-integer delta has Delta=3/2, so E0>3/2 as well.
Thus(S) has no coalesced exception for ANY coprime m<n.
For(G), half-integer delta has Delta=1/2, L<=m-1/2, and n>=2m-1 gives
(m+n-1/2)/L>=3. Consequently E0>=0, with equality possible ONLY when

    n=2m-1, delta=1/2, j=5m-3, r=j/(2m-1).            (10)

The first three equalities are necessary to attain(9); the last is necessary
to attain (2m+2n-1)r<= (m+n-1/2)j/L<=N. In this unique case F_j has
degree3 and is divisible by ALL three distinct lines, so

    F_j=lambda*p*(p+g)*(p+t*g), lambda!=0.              (11)

It has multiplicity1 at BOTH actual double lines p=0 and p+t*g=0.
The equality case is not called commuting; its nonzero target is retained
and treated in section7 below.

## 6. Separated doubles: no equality survives

Suppose kappa<2r. Set rho_s=sqrt(-xi), of orderkappa/2, and regroup BEFORE
selecting an initial:

    U(z)=sum c_(2i)(z-xi)^i,
    V(z)=sum c_(2i+1)(z-xi)^i,
    F_+/-=U(z)+/-rho_s*sqrt(1-z/xi)*V(z).              (12)

Every coefficient U_l,V_l has order>=j; the sums converge since their
i-th summands have order>=j+(i-l)kappa. If d=2k, U_k has orderj; if
d=2k+1, V_k has orderj. Terms after its anchor are strictly later.
For EVERY l, ord c_l+l*kappa/2>m*kappa: use the definition of r for
l<=d, and j>=(2m-d)r with l>d otherwise. Hence

    q_l=min(ord U_l,kappa/2+ord V_l)>(m-l)kappa.

Put eta=min_(0<=l<=m-2)q_l/(m-l). The anchor makes this finite and
eta>kappa. For even d, eta<=j/L; for odd d,
eta<=(j+kappa/2)/(L+1/2)<j/L because kappa<2r<=j/L.
In both cases eta<D and eta<j (L>=2 for even d, L>=3/2 for odd d).
At z=s^eta Z, all EVEN/ODD BASES have order>=m*eta, at least one attains
it with degree<=m-2, and higher indices are later since j>eta. Every
positive binomial shift is later than its OWN base by t0*(eta-kappa)>0.
The global earliest tuple is(u+v,u-v); it cannot vanish on both sheets.
Thus both A initials are monic degree m and at least one has nonzero
correction of degree<=m-2. Scalar reference terms are later since eta<D.

Apply the SAME regrouping to ENTIRE W_s=B_s-R_s^n. Its original zeta
coefficients have order>=1, as do its regrouped even/odd coefficients.
Its bases have order>=1+l*eta, and finitely many lie below any bound.
If a base lies below n*eta, take the GLOBAL minimum nu. No later shift
returns to nu from an earlier base; the tuple cannot cancel on both
sheets, giving an actual earlier B initial Q on some sheet of degree v
with v*eta<=nu-1. The Euler factor(6) is strictly positive.

The X-dependent chain rule cancels the y_X cross terms. Its exact inverse
factor is y_z=y_zeta/(2zeta), of order-kappa/2. The bracket target in
(Z,X) is thus orderN-kappa/2+eta, retaining its nonzero generic coefficient.
Even when E0=0, the strict bound kappa<j/L gives

    (m+n-1)*eta+kappa/2
       <(m+n-1/2)*j/L<=N.                            (13)

The earlier Q must therefore commute with its A initial, impossible by(5).
No whole-B base occurs below n*eta on either sheet. At n*eta positive
shifts cannot return from any earlier base; bases present there have
degree<n. Both B initials are monic degree n and commute with their
respective A initials by(13). Common-linear powers force both corrections
to vanish, contradicting the nonzero tuple. This excludes ALL separated
cases, including the putative equality data(10).

## 7. Golden equality: all-m resonance and two incompatible scalar values

Assume(G) has survived. Sections4–6 and(10) force n=2m-1, j=5m-3 and
(11). At BOTH double lines the same argument applies, since both minimize
delta=1/2. Each must be coalesced at r=j/n. Since 2j=5n-1,

    gcd(j,n)=1, n>=3 odd,
    2r=5-1/n<5, r nonintegral,
    kappa>=ceil(2r)=5>2r.                            (14)

The original s-orders in the Morse coefficients are integers. Since d=1,
r=min(ord c0/(2m),j/(2m-1)); survival at r=j/n forces ord c0>=2m*r=j+r.
The right side is nonintegral, so ord c0>j+r. Higher c_l terms are later
as before. xi and scalar A terms are later by(14). Therefore the COMPLETE
A initial is

    P=Y^(n+1)+uY, u=k0*X^(1/2), k0!=0,
    at order2m*r.                                    (15)

Earlier whole-B initials were already excluded using the non-strict
bound in section5. At its expected order2n*r=2j, every contribution
from W_s has index l<2n and integer s-order2j-l*j/n. Since gcd(j,n)=1,
only l=0 or n can occur. R_s^n supplies exactly Y^(2n), because xi is
strictly later than zeta². Euler homogeneity gives h=D/2-r=1/(2n), so
B's complete monic initial has the form

    Q=Y^(2n)+beta*Y^n+gamma,
    beta=b0*X^(1/2), gamma=d0*X.                      (16)

No old G or qF estimate was used to determine this complete support.
Here the initial bracket is NONZERO at equality: (2m+2n-1)r=3nr=3j=N.
In coordinates(Y,X), both sides have orderN+r. Its leading target is a
nonzero constant times X^(1/2), independent of Y. Their Euler identity is

    X[P,Q]=h*(2n*P_Y*Q-(n+1)*P*Q_Y).                 (17)

Direct factored multiplication in(17) cancels Y^(3n). The remaining
coefficients BEFORE multiplication by h are

    Y^(2n): n(n+1)*beta-2n²*u,
    Y^n:    2n(n+1)*gamma-n(n-1)*u*beta,
    Y^0:    2n*u*gamma.                              (18)

There are no other powers. Since the target is independent of Y, the
first two coefficients vanish. Therefore

    beta=2n*u/(n+1),
    gamma=C_n*u², C_n=n(n-1)/(n+1)²!=0,
    [P,Q]=C_n*k0³*X^(1/2).                           (19)

The last equality uses h=1/(2n). These are scalar factored identities
valid for every integer n=2m-1, not numerical checks or expanded sources.

Now compare the TWO ACTUAL double charts of(11). Put L0=p+g,M0=p+t*g.
Let a0 denote a chosen constant square root of the quadratic Morse
coefficient after factoring out X³. The exact data are:

| chart(y,X) | root | a0² | (F_j)_y at root | original target |
|---|---|---|---|---|
| (p,g) | y=0 | t² | lambda*t*X² | -c*X² |
| (g,p) | y=-X/t | t(t-1) | lambda*(t-1)*X² | c*X²/t² |

All denominators are nonzero: rho and t are nonzero and t!=1 by the
quadratic relation. These data follow directly by factoring H at each
line and differentiating lambda*p*L0*M0. In either chart
y_zeta(0,0,X)=1/(a0*X^(3/2)). Consequently k0=lambda*t/a0 in the first
chart and k0=lambda*(t-1)/a0 in the second. The exact leading target
after the chain rule is respectively -c*X^(1/2)/a0 and
c*X^(1/2)/(t²*a0). Equation(19) therefore forces

    p-chart: c=-C_n*lambda³*t,
    M-chart: c= C_n*lambda³*t*(t-1)².                 (20)

Only the ORIGINAL c and lambda are shared; the local a0,k0,b0,d0 need
not agree. Equality in(20) would give(t-1)²+1=0. But t=1-rho and
rho²-3rho+1=0 give(t-1)²+1=rho²+1=3rho!=0. This is impossible.
Changing a0 to-a0 changes k0 to-k0 and leaves a0*k0³ unchanged, so
neither Morse sign nor either conjugate supplies an exception.
This eliminates the unique coalesced equality and proves(G).

## 8. Exhaustion, negative controls and remaining global boundary

The finite canonical A supplies a minimizing simple or double line.
Sections4–6 cover all simple, coalesced and separated regimes whenever
the strict budget applies. For(S) it always applies. For(G), n>=2m-1
makes it nonnegative and isolates exactly(10); section7 eliminates that
case using both actual double lines. This proves the two local statements
IF independently reviewed; it does not assume or produce an F2 source.

Controls, all manual and not executed:

- c=0 allows A=H^m,B=H^n and invalidates the proof of F!=0.
- Removing scalar-power normality loses the strict Delta in(4).
- Noncoprime m,n allow nontrivial common powers; the Euler/UFD conclusion
  need not have root degree1 or2. Coprimality is essential.
- Degree2m-2 corrections may be absorbed by a different common quadratic;
  the bound2m-3 from minimizing multiplicity is used literally.
- A separated correction can cancel on one sheet but not both; all tuples
  and first-base exclusions retain both sheets and their X derivatives.
- At the golden equality, the target must NOT be set to zero. One chart
  alone admits the scalar relation(19). Its impossibility uses the two
  different actual lines and the specified golden ratio, not a generic
  one-double-line argument.
- For m=2,n=3 the same symbolic formulas have n>=3, gcd(j,n)=1 and
  C_n!=0; no exceptional smallest exponent is omitted. At m=3,n=5,
  (19) specializes formally to C_n=5/9, the old3/5 scalar coefficient.
- For(G) with n<2m-1, inequality(9) can be negative. That is a scope
  limitation of THIS proof, not a counterexample or proof of impossibility
  for every other uniform method. No such exponents are claimed here.

No nilpotent coefficient rings, positive characteristic, general H,
higher-degree targets, arbitrary same numerical degrees, complete source
ideal, polynomial inverse or JC2 resolution is established. The next
different-model gate must reconstruct(4),(9), both entire-B arguments,
the integer-order support restriction(14)–(16), the factored coefficients
(18) and both signed scalar comparisons(20). Source attachment remains
an independent obligation; no expensive computation is authorized.

## Own publication check

Root read the complete own body in ranges1–210 and211–end before sealing,
and rederived the three scalar coefficients in(18). The owned raised-OPEN
check below is administrative only; there are no raised campaign OPENs.
This remains a new UNREVIEWED proof after transactional publication.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17854`.
- Body SHA-256:
  `4a4c8b57e346f38381d026ab2c9f976b17e858730761f6a7400fc2020df1a1c4`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
