# A degree-seven Jacobian obstruction for all coprime output exponents

Coordinator /root, 2026-09-09. NEW, PRODUCER-CHECKED CANDIDATE; independent
different-model review is required. Pure factored prose; no mathematical
subprocess of any size, coefficient expansion, CAS, source emission or AWS.
This is not a resolution of JC2 or an accepted all-family source exclusion.

## 1. Statement and precise source boundary

Let k be any characteristic-zero field and let

    K(a,b)=(b²-a²)² b(b²-3a²/2),    deg K=7.

For every coprime pair of integers 2<=m<n, there are NO A,B in k[a,b] with
ordinary degrees 7m,7n, highest homogeneous forms K^m,K^n, and

    [A,B]_(a,b)=2c*a³,    c in k nonzero.                  (1)

All lower homogeneous coefficients are unrestricted. In particular no
weighted support, parity, inverse lift, polynomial-centralizer assumption,
reference for B, or ordG>=2ordF hypothesis is present. Independent nonzero
leading scalars can be removed by scaling the outputs, changing c only.

It suffices to prove this over an algebraic closure of k. We henceforth
assume k algebraically closed. It follows that no weighted(2,1) polynomial
pair in k[g,p], with weighted leaders H^m,H^n for

    H=p(p²-g)²(p²-3g/2),

and Jacobian c*g exists: the injective polynomial substitution g=a²,p=b
gives ordinary leaders K^m,K^n and Jacobian 2c*a³. This is a necessary
polynomial receiver obstruction. An infinite family of actual Keller
sources is excluded ONLY if its source-to-receiver map is separately proved.
The all-parameter F9 source task is independent and not a premise here.

The accepted m=3,n=5 proof motivated this candidate. Its reference/G
theorem is not used; all exponents and bounds are derived below. The own
0730 blind proposed the redesign before peer invitations. No 0730 peer
blind or new source-interface output has been read or used in this proof.

## 2. A-only canonical reference and the minimizing factor

Homogenize by dilation: A_s=s^(7m)A(a/s,b/s), and similarly for B_s. The
variables s,a,b have degree1 and

    [A_s,B_s]_(a,b)=2c*s^N*a³,   N=7(m+n)-5.             (2)

We construct a polynomial R_s=K+sum_(i=1)^7 s^i R_(7-i), and constants
alpha_i in k, 0<=i<=m-2, with

    A_s=f_s(R_s)+F,
    f_s(T)=T^m+sum_(i=0)^(m-2) alpha_i s^[7(m-i)] T^i.  (3)

Every term has combined degree7m. The first nonzero coefficient F_j of F
satisfies BOTH

    K^(m-1) does not divide F_j,
    F_j is not a scalar power lambda*K^i.               (4)

Here is a finite construction, not an assumed polynomial mth root. At
s-orders 1 through7, addition of s^i R_(7-i) changes the coefficient of
R_s^m at that order by m*K^(m-1)*R_(7-i). In each homogeneous polynomial
space choose a k-linear complement to this image and remove its image
component. Subsequent choices cannot change a preceding coefficient.
At i=7 the image consists of scalar K^(m-1), so this removes the otherwise
possible T^(m-1) term as well. Fix all these seven coefficients of R_s.
For orders greater than7, any nonzero residual has degree less than
7(m-1), and hence cannot be divisible by K^(m-1).

Now at each order j=7(m-i), i=m-2,...,0, remove its scalar K^i component
by the corresponding term alpha_i s^j R_s^i, using a linear complement
to k*K^i. These orders are >=14, and their higher contributions affect
only later orders. No other order can contain a nonzero scalar K-power,
by homogeneity. This proves (4) for the first surviving residual. All
objects remain finite polynomials; no negative-degree correction to R_s
is made and no B-centralizer lemma has been invoked.

The residual is not identically zero. Otherwise at s=1, A=f_1(R_1), and
the nonzero polynomial f_1'(R_1), of degree7(m-1)>3, divides [A,B]. A
nonzero polynomial product cannot have degree3 in the domain k[a,b].
Thus j>=1 is finite, and F_j is homogeneous of degree7m-j.

Over k, K has three distinct simple lines and two distinct double lines.
Write these factors L_i with multiplicities e_i in {1,2}, and choose a
line attaining

    delta=min_i ord_(L_i)(F_j)/e_i,    0<=delta<m-1.

The strict upper bound is (4). Delta is an integer or a half-integer.
Put L=m-delta>0. There is the important STRICT degree budget

    j <= 7L-Delta, where Delta=1 if delta is integral,
                           Delta=3/2 otherwise.         (5)

Indeed if delta=t is integral, K^t divides F_j. Degree7t would force
F_j=lambda*K^t, removed by (4), so degF_j>=7t+1. If delta=t+1/2,
the three simple lines divide F_j to order at least t+1 and the two
double lines to order at least2t+1. Their total degree is7delta+3/2.
No equal-multiplicity assumption or assertion F_j=K*C is used.

The proof now uses ONE minimizing line. If it is simple, its transverse
multiplicity d=delta is an integer <=m-2. If it is double, d=2delta
is an integer <=2m-3. All scalar terms in (3) are retained below.

## 3. Formal charts, Euler lemmas and target margins

Use coordinates y=b,X=a, so the bracket target is -2c*s^N*X³. Work at
the generic point y=gamma*X of the selected line, with X transcendental
and nonzero. Coefficients lie in E=k(X^(1/2)), with its X-derivation;
its constants are k. Formal inverses below have nonnegative s and local
coordinate orders. Finite Puiseux extensions in s are allowed; they do
not specialize X or turn a field into a nonreduced coefficient ring.

At a simple line R_y is a unit, so z=R_s has a formal inverse y(s,z,X)
over k(X)[[s,z]]. At a double line solve R_y=0 for its unique moving
critical point y_c(s,X) by the formal implicit-function theorem. Taylor
expansion and a formal square root of the transverse unit give an EXACT
coordinate zeta, with invertible y_zeta, such that

    R_s=xi(s,X)+zeta²,   xi=R_s(y_c,X),
    kappa=ord_s xi>=1, or kappa=infinity if xi=0.         (6)

For the two double lines y=epsilon*X, epsilon=+/-1, the quadratic
coefficient of K is -2epsilon*X^5, a unit with a square root in E. Thus
the asserted coordinate exists. The implicit inverses and square root
preserve homogeneity: z has degree7, zeta has degree7/2, and s,X have
degree1. All their coefficients are homogeneous rational powers of X.
Initial polynomials after z=s^eta Z or zeta=s^r Y therefore satisfy the
induced Euler identities. Coefficient functions are never presumed
constant; their X-derivatives are essential.

Two elementary lemmas suffice. Let P be monic of degree M>0 in Z, Q!=0
have degree t, and [P,Q]_(Z,X)=0. If q_t is its leading coefficient,
the coefficient of Z^(M+t-1) is M*q_t', so q_t'=0. If in addition

    (X*d_X+h*Z*d_Z)Q=Lambda*Q,

then (Lambda-t*h)q_t=0. A strictly positive Lambda-t*h is impossible.
This includes t=0; monicity and M>0 are necessary.

Next let P,Q be monic of degrees em,en, with Euler degrees emh,enh and
h!=0. Their commutation yields

    X[P,Q]=e*h*(n*P_Z*Q-m*P*Q_Z)=0.

Consequently Q^m/P^n is Z-constant, and monicity makes it1. Unique
factorization and gcd(m,n)=1 give P=W^m,Q=W^n for a monic W of degree e.
For e=1, P=Z^m+U, degU<=m-2, forces W=Z and U=0. For e=2,

    P=(Y²+b0)^m+U, degU<=2m-3,

the coefficients of Y^(2m-1) and Y^(2m-2) force W=Y²+b0, hence U=0.

For later use, n>=m+1 and L<=m give

    (m+n-1/2)/L > 2,
    N-(m+n-1/2)*j/L
       >= -3/2+(m+n-1/2)*Delta/L > 1/2 > 0.            (7)

This is uniform in m,n and is exactly where the strict loss in (5)
matters. The simple-line version is

    N-(m+n-1)*j/L >= 2+(m+n-1)*Delta/L > 0.             (8)

## 4. Minimizing simple line

Write the complete transformed F=sum f_l(s,X) z^l. Every coefficient
has s-order>=j, while f_d has order exactly j, where d=delta<=m-2.
Define

    eta=min_(0<=l<=d) ord_s(f_l)/(m-l).

Zero coefficients have order infinity. The d-term makes this a finite
positive rational number and eta<=j/(m-d)=j/L<7. Terms with l<=d have
order at least m*eta after scaling z=s^eta Z. Terms with l>d are later:
j+l*eta >= (m-d+l)*eta >= (m+1)*eta. At least one low term attains
m*eta. The lower scalar terms of f_s(R_s) are later by
(m-i)(7-eta)>0. Thus the A initial is

    s^(m*eta) P,   P=Z^m+U, 0!=U, degU<=d<=m-2.        (9)

Now use ENTIRE W_s=B_s-R_s^n, not a divided remainder G. It has s-order
>=1 as a polynomial; the complete simple inverse preserves that bound
for every coefficient in z. If B had an initial of order nu<n*eta,
its nonzero coefficient polynomial Q has degree t with

    t*eta<=nu-1,
    Lambda-t*h=7n-nu-t*(7-eta)
       >=7n-7nu/eta+(7/eta-1)>0,   h=7-eta.            (10)

The initial is a polynomial because eta>0 and all coefficient orders
are >=1. The coordinate change makes the target have s-order N+eta;
its chain-rule factor y_z is a unit. By (8), (m+n-1)*eta<N, so this
earlier Q must commute with P. The first Euler lemma contradicts (10).

At order n*eta, contributions of W_s have degree<n by the same positive
coefficient bound. Hence B has a MONIC degree-n initial Q; it cannot
cancel the degree-n term of R_s^n=z^n. Equation(8) again forces [P,Q]=0.
Their Euler degrees are m(7-eta),n(7-eta). The e=1 lemma forces U=0,
contradicting (9). A minimizing simple line is impossible.

## 5. Minimizing double line: coalesced roots

Use (6) and write the ENTIRE transformed F=sum c_l(s,X) zeta^l. Every
coefficient has order>=j and c_d has order exactly j, with d=2delta<=2m-3.
Set

    r=min_(0<=l<=d) ord_s(c_l)/(2m-l).

It is positive and finite; r<=j/(2m-d)=j/(2L)<7/2. All higher l>d terms
are later than2m*r, since j+l*r>2m*r. First suppose kappa>=2r, including
equality and xi=0. Under zeta=s^r Y, the initial of R_s is Y²+b0 at
order2r, where b0=0 when kappa>2r. The lower scalar terms of (3) are
later by (m-i)(7-2r)>0. Therefore the A initial is

    s^(2m*r) P,  P=(Y²+b0)^m+U, 0!=U, degU<=d<=2m-3.  (11)

Again W_s=B_s-R_s^n has each zeta coefficient of order>=1. A hypothetical
earlier B initial at nu<2n*r has degree t with t*r<=nu-1. With h=7/2-r,

    7n-nu-t*h >=7n-7nu/(2r)+(7/(2r)-1)>0.              (12)

The transformed target is of order N+r because y_zeta is a unit. From
(7) and r<=j/(2L) we have

    (2m+2n-1)*r <= (m+n-1/2)*j/L < N.                 (13)

Thus the hypothetical earlier initial commutes with P, contrary to the
first Euler lemma and (12). At order2n*r, the whole W_s has degree<2n
and cannot cancel monicity of (Y²+b0)^n. The monic initials P,Q commute
by (13), and have Euler degrees 2m*h,2n*h. The e=2 lemma forces U=0.
This contradicts (11), including the equality and infinite-kappa cases.

## 6. Minimizing double line: separated roots, full two-sheet accounting

It remains that kappa<2r, necessarily finite. Put rho=sqrt(-xi), with
order kappa/2 in a finite Puiseux extension, and use z=R_s. The EXACT
two inverse sheets are

    zeta=+/-rho*sqrt(1-z/xi).

We use expansions with ord_s z=eta>kappa, to be selected, so these are
well-defined and the binomial series is s-adically convergent. Regroup
the entire F BEFORE selecting an initial:

    U(z)=sum_(i>=0)c_(2i)(z-xi)^i,
    V(z)=sum_(i>=0)c_(2i+1)(z-xi)^i,
    F_+/-=U(z)+/-rho*sqrt(1-z/xi)*V(z).                 (14)

The coefficients U_l,V_l have s-order>=j; for fixed l the defining sums
converge because xi has positive order. Indeed their summands have orders
at least j+(i-l)kappa, tending to infinity. If d=2k, U_k has order j:
its i=k summand is c_(2k), and every later summand has strictly larger
order. If d=2k+1, V_k has order j by the same argument.

The condition kappa<2r implies, for EVERY l>=0,

    ord_s c_l + l*kappa/2 > m*kappa.                   (15)

For l<=d this follows from ord c_l>=(2m-l)r and d<2m.
For l>d it follows from ord c_l>=j, j>=(2m-d)r and l>d.
Consequently, with

    q_l=min(ord_s U_l, kappa/2+ord_s V_l),

we have q_l>(m-l)kappa, allowing infinity for zero bases. Set

    eta=min_(0<=l<=m-2) q_l/(m-l).                     (16)

The anchors just established, with k<=m-2, make eta finite, and (15)
makes eta>kappa. If d=2k, so delta=k and L=m-k, then

    eta<=j/L.

If d=2k+1, so L=m-k-1/2, then

    eta<=(j+kappa/2)/(L+1/2)<j/L,

where kappa<2r<=j/L proves the strict second inequality. In both cases

    kappa<eta<=j/L<7,    eta<j.                        (17)

For the last inequality, L>=2 in the even case. In the odd case L>=3/2,
so eta<j/L<=2j/3. These cover m=2 as well as every larger m.

Call U_l z^l and +/-rho V_l z^l the BASES in (14). At z=s^eta Z,
every base with l<=m-2 has order>=m*eta, with at least one equality.
Every base with l>=m-1 is strictly later, since its coefficient has order
>=j>eta. Every positive binomial shift of an odd base is later than THAT
base by t(eta-kappa)>0. This is a comparison with its own base, not an
incorrect coefficientwise degree bound on a later shifted coefficient.

At the global earliest base order m*eta, positive shifts cannot return
from an earlier base, because no earlier base exists. The pair of sheet
coefficients has the form (u+v,u-v). It cannot vanish on BOTH sheets
unless u=v=0, in characteristic zero. Hence the A initials are

    s^(m*eta) P_+, s^(m*eta) P_-,
    P_+/-=Z^m+U_+/-, deg U_+/-<=m-2,
    at least one U_+/- is nonzero.                     (18)

Here R_s=z exactly on both sheets. All scalar terms of f_s are later
by (m-i)(7-eta)>0. Thus both P_+ and P_- are monic of degree m, even
if their correction vanishes on one sheet.

### Whole B, not the old divided remainder

Apply the SAME even/odd regrouping to W_s=B_s-R_s^n. Its original zeta
coefficients all have order>=1. If its even/odd coefficients are U^B_l,
V^B_l, then ord U^B_l>=1 and ord V^B_l>=1. Their base orders after scaling
are therefore at least1+l*eta, including the positive kappa/2 for odd
bases. In particular a global minimum of all finite base orders exists,
and at any bounded order only finitely many indices contribute.

Suppose some whole-B base has order below n*eta; choose the GLOBAL
minimum nu among both even and odd bases and all indices. Positive
binomial shifts are later than their own bases by t(eta-kappa), so none
contributes to this first order. The two-sheet tuple argument shows that
on at least one sheet B has a nonzero actual initial Q of order nu,
since R_s^n=z^n starts only at n*eta. If t=deg Q, then

    t*eta<=nu-1.                                      (19)

The source identity must be transformed with its FULL X-dependent
coordinate change. The y_X cross terms cancel in the determinant, giving
[A_tilde,B_tilde]_(z,X)=y_z[A_s,B_s]_(y,X). On either sheet,

    y_z=y_zeta/(2zeta),  ord_s y_z=-kappa/2,

because eta>kappa and y_zeta has nonzero order-zero coefficient. Passing
to Z multiplies the bracket by s^eta. Thus the exact target order is
N-kappa/2+eta, not N+eta and not an X-constant replacement target.
Equations(7),(17) give the STRICT margin

    (m+n-1)*eta+kappa/2
       < (m+n-1/2)*j/L < N.                           (20)

The first inequality holds also in the even case eta=j/L, since
kappa<j/L. Therefore the earlier Q commutes with the corresponding
monic P_+ or P_-. Its Euler factor is

    7n-nu-t*(7-eta)
       >=7n-7nu/eta+(7/eta-1)>0,

by (19), nu<n*eta and eta<7. The first Euler lemma is a contradiction.
It follows that NO whole-B base on either sheet has order<n*eta.

At order n*eta there are thus no returning binomial shifts from an
earlier base. Bases at that order have degree<n by their positive
coefficient orders. Bases at higher orders and positive shifts are later.
Consequently BOTH sheets have a monic degree-n initial Q_+/-; the
leading term z^n cannot be cancelled. Equation(20) forces
[P_+,Q_+]=[P_-,Q_-]=0. Their respective Euler degrees are m(7-eta)
and n(7-eta), with 7-eta>0. Applying the e=1 lemma on BOTH sheets forces
U_+=U_-=0, contrary to (18). This exhausts the separated case.

## 7. Exhaustion, controls, interpretation and stop boundary

The finite canonical construction gave F!=0 and a minimizing line. Such
a line is either simple or double. Section4 excludes the former;
Sections5 and6 exclude respectively every kappa>=2r and kappa<2r for
the latter. Zero coefficients, xi=0, equality, all permissible residual
multiplicities, all scalar kernels and both inverse sheets are included.
This proves (1) if the argument survives independent review.

The following are explicit hypothesis/method controls, not Keller
counterexamples or performed computations:

- If c=0, A=K^m,B=K^n is allowed. Thus F!=0 requires the NONZERO
  low-degree Jacobian; there is no claim to exclude commuting powers.
- Without the scalar removal in (4), F_j=lambda*K^t has degree7t and
  loses Delta=1 in (5). A balance at eta=7 loses the Euler force. The
  scalar correction must be removed, not merely declared irrelevant.
- The e=1 Euler conclusion requires coprimality: P=Z²+u and
  Q=(Z²+u)² commute with nonzero depressed correction for suitable
  homogeneous u. They are a control to the local inference when gcd>1,
  not a source satisfying (1).
- The e=2 correction threshold is exact for this argument. Taking
  P=(Y²+b0+t)^m, Q=(Y²+b0+t)^n with homogeneous nonzero t produces a
  degree2m-2 correction relative to (Y²+b0)^m, and does NOT force t=0.
  Our minimizing double line gives d<=2m-3, so does not invoke that
  false stronger statement.
- At an earliest separated base, u=-v can make one sheet vanish but
  the other has coefficient -2v. Dropping one sheet is not licensed.
- P=1,Q=X defeats the leading-coefficient commutation inference when
  the monic P has degree0; our P always has degree m or2m, m>=2.

No proof over arbitrary nilpotent coefficient rings, positive
characteristic, noncoprime exponents, higher-degree Jacobian targets,
arbitrary degree-seven K or arbitrary actual Keller sources is claimed.
In particular the counterexample to a proper-power low-order G estimate
is not contradicted: NO G estimate or polynomial B-reference occurs here.

The immediate different-model gate must attack the finite construction
(3)-(4), strict multiplicity budget(5), polynomial Euler initials,
coalesced equality, separated convergence/two-sheet global minima and
target chain rule, and only then the weighted-cover corollary. A GAP
preserves just the independently proved portion and forbids family
closure. No expensive computation or dependent source-family farm is
authorized by this candidate. The independent all-F9 source arrow, if
it passes its own gate, is the intended consumer; a matching numerical
degree pair or a bare Laurent standard pair is not that arrow.

## Own raised-OPEN check

Root read the complete own body in ranges1-180 and181-end, then checked
extract_raised_opens on only this private body at08:03:10UTC: result ().
No corpus traversal or mathematical subprocess was used. The report is a new unreviewed proof attempt, not an
accepted premise of the active0730 blinds or a completed strategy round.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18737`.
- Body SHA-256:
  `e10dc4122b8ffab9b003834bf79a17f11b6a8f1ad63a7a07511a6b3f913ccab6`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
