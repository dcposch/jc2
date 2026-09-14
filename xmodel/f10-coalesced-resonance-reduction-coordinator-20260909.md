# F10 coalesced triple contact: a fixed cubic/quintic resonance

Coordinator/root, September9,2026. NEW / UNREVIEWED pure manual proof.
This is a conditional local reduction, NOT a receiver exclusion or JC2 proof.
No mathematical subprocess of any size, CAS, coefficient emission or AWS.

## 1. Literal objects and scope

Let q>=0 be an integer, m=3q+4 and n=5q+7. Thus m>=4,
3n=5m+1 and gcd(m,n)=1. This is the INCREASING output orientation;
the printed F10 source uses the opposite order, so swapping its outputs
also negates its Jacobian scalar. No source-map theorem is assumed here.

Suppose ordinary polynomials A,B over a characteristic-zero field have
top forms K^m,K^n and bracket [A,B]_(a,b)=2c*a³,c!=0, where

    K=b(b²-a²)³,  deg K=7.

All lower coefficients are unrestricted. Extend constants algebraically
when needed. Homogenize A_s=s^(7m)A(a/s,b/s), similarly B_s. Then

    [A_s,B_s]=2c*s^N*a³, N=7(m+n)-5=56q+72.

This report proves: choose the finite normal A-reference below and a
factor of K minimizing its first-correction multiplicity divided by the
factor multiplicity. A simple minimizer is impossible. If a triple
minimizer reaches the COALESCED cubic regime defined below, its first
normal correction necessarily has

    d=2m, j=7q+9,
    F_j=lambda*b^(2q+3)*(b²-a²)^(6q+8), lambda!=0.       (A)

Its complete initial A and B then supply monic polynomials C(T),D(T)
of degrees3,5 satisfying

    (5m+1)T C'D-3m T C D'-3CD=-3c !=0,                (B)

with C(T)=T³+lambda*T²+v*T+w. There are no omitted B terms in(B).
No assertion that(B) is impossible is made. The first separated cubic
regimes are not handled by this report. Both original triple factors give
the SAME target sign; this is not a golden two-chart contradiction.

## 2. Finite canonical A-reference and the global contact budget

Choose a combined-homogeneous degree-seven reference

    R=K+sum_(i=1)^7 s^i R_(7-i),
    f_s(T)=T^m+sum_(i=0)^(m-2)alpha_i*s^[7(m-i)]*T^i,
    A_s=f_s(R)+F.

At each order1..7 remove the component in the image of multiplication by
m*K^(m-1) using a fixed homogeneous linear complement. At order7 that
image includes every scalar K^(m-1), accounting for the missing T^(m-1)
term. At later orders a nonzero homogeneous residual has degree<7(m-1)
and cannot be divisible by K^(m-1). At orders7(m-i),i=m-2,...,0, remove
any scalar K^i component by the displayed scalar term, in increasing
order; its subsequent changes occur only later. All objects stay finite.

F is nonzero: otherwise at s=1 the nonzero polynomial f_1'(R_1), with
degree7(m-1)>3, divides the nonzero degree-three bracket. Thus for
j=ord_s F>=1 its first nonzero homogeneous coefficient F_j satisfies
K^(m-1) not dividing F_j and F_j not a scalar K-power.

For the three actual factors b,b-a,b+a with multiplicities1,3,3, put
delta=min ord_L(F_j)/e_L<m-1 and L=m-delta. Counting the required
factor multiplicities gives

    delta integral:              j<=7L-1;
    delta=t+1/3,t integral>=0:  j<=7L-2/3;
    delta=t+2/3,t integral>=0:  j<=7L-1/3.             (C)

Indeed the fractional cases force multiplicities(t+1,3t+r,3t+r),
r=1 or2, of total degree7t+1+2r=7delta+(1-r/3).
The integral case has at least degree7delta, and equality would make
F_j a forbidden scalar K^delta. Denote the three losses by Delta.

For a simple minimizing factor the formal inverse z=R has nonnegative
s,z orders. If its transverse multiplicity is d=delta<=m-2, balancing
the full F against z^m gives eta<=j/(m-d)=j/L<7 and a nonzero
correction of degree<=m-2. All scalar f_s terms occur later. Whole
W=B_s-R^n has positive original coefficient orders; an earlier B initial
at nu<n*eta, with highest z-degree v, has v*eta<nu and positive
Euler factor7n-nu-v(7-eta)>7n-7nu/eta>0.
The target in the rescaled inverse has orderN+eta, and

    N-(m+n-1)j/L >= 2+(m+n-1)Delta/L >0.

Thus earlier B initials commute and contradict that positive factor.
At n*eta the full B initial is monic of degree n and commutes with
the monic A initial. Euler homogeneity and coprimality force powers of
one monic linear polynomial; its first coefficient and the depressed
A initial force the correction zero. The target is genuinely nonzero
on b=0 because a is a generic nonzero along-line coordinate. A simple
minimizer is therefore impossible. The remaining minimizer is triple,
with d=3delta<=3m-4.

## 3. Exact cubic right coordinate, not a fictitious pure cube

Fix either a=epsilon*b,epsilon=+1 or-1, put X=b, and begin with

    zeta0=X^(1/3)(X²-a²),
    a=epsilon*(X²-X^(-1/3)*zeta0)^(1/2).

The branch at zeta0=0 has a=epsilon*X. Over E=kbar(X^(1/3)) this is
an invertible formal coordinate in zeta0 with nonzero derivative.
It gives K=zeta0³ exactly. Its coefficients are formal in zeta0,
not claimed to be polynomial at every fixed s-order. Give s,X weight1,
zeta0 weight7/3; the inverse a has weight1.

An s-adic right change, identity modulo s, puts the full R exactly in
the form

    R=zeta³+alpha(s,X)*zeta+beta(s,X),
    alpha,beta in sE[[s]].                              (D)

Here is its construction, including the infinite transverse tail. At
order s^l split the remaining formal power series f_l(zeta) uniquely
as zeta²*h_l(zeta)+a_l*zeta+b_l. Replacing the old coordinate by
zeta-s^l*h_l(zeta)/3 removes exactly its zeta² multiple at that order.
The existing alpha starts in s, so changed lower deformation terms
contribute only at subsequent orders. Iterate. Each change and its
inverse are defined in the complete formal ring E[[s,zeta]], with no
negative s or zeta exponents. All weights are preserved; alpha has
weight14/3 and beta weight7. Neither lower deformation is discarded.

In this coordinate write F=sum c_l(s,X)zeta^l. Every c_l has integral
s-order>=j; ord c_d=j and all l<d have greater order. The nonlinear
initial transverse coordinate preserves vanishing multiplicity d, though
it need not preserve the degree of the entire F_j Taylor series.
The transformed W=B_s-R^n likewise has every coefficient of integral
s-order>=1. Positive transverse rescalings therefore have finite
polynomial initials despite the infinite formal transverse tails.

The exact bracket becomes

    [A_s,B_s]_(zeta,X)=2c*s^N*a(s,zeta,X)³*a_zeta.

At s=0 the original inverse derivative is
a_zeta0=-1/(2a*X^(1/3)). Hence after ANY positive transverse
rescaling the leading target is

    -c*s^N*X^(5/3),                                  (E)

independent of epsilon. Before rescaling, the pure s^N coefficient
also has the transverse term +c*X^(-2/3)*zeta0. That term is later
after positive rescaling, not identically absent from the full target.
All X-derivative cross terms cancel by the exact chain rule.

## 4. Whole-polynomial coalesced analysis

Set

    r=min_(0<=l<=d) ord(c_l)/(3m-l),
    lambda_split=min(ord alpha/2,ord beta/3).

r is finite positive and, by(C),

    r<=j/(3m-d)=j/(3L)<7/3.                           (F)

Assume COALESCENCE: lambda_split>=r, including infinity. After
zeta=s^rY the complete A initial at3mr is

    P=V(Y)^m+U(Y), V=Y³+A1Y+B1,
    U!=0, deg U<=d<=3m-4.

Higher c_l terms are later by j+(d+1)r>3mr; lower scalar terms
are later by(m-i)(7-3r)>0. Put h=7/3-r>0. P is monic degree3m
and Euler-homogeneous of weight3m*h under X*d_X+h*Y*d_Y.

If the whole B had an earlier initial Q at nu<3nr, its degree v
satisfies v*r<nu because every coefficient of W has positive order.
Its Euler degree is7n-nu. The first possible bracket order in the
(zeta,X) convention is theta=(3m-1)r+nu. For theta>N it starts
too late to equal(E); for theta<N it commutes; for theta=N the
bracket is a NONZERO constant in Y. In both latter cases its
coefficient of Y^(3m+v-1) must vanish. That coefficient is3m*q_v',
since P is monic and P_X has degree<=3m-1. Therefore q_v'=0.
But its Euler factor obeys

    7n-nu-v*h > 7n-7nu/(3r) >0,

a contradiction. No earlier B initial exists, even at target equality.

At3nr the whole B initial Q is monic degree3n; its correction has
degree<3n, so the leading term cannot cancel. The first bracket
order is(3(m+n)-1)r. If this is greater thanN the target is too
early. If less, P,Q commute. Euler then gives Q^m=P^n; coprimality
and monicity give P=W0^m,Q=W0^n for a monic cubic W0. If W0!=V,
W0^m-V^m has degree at least3(m-1), contradicting deg U<=3m-4;
if W0=V then U=0, also impossible. Consequently

    r=N/(3(m+n)-1)=(7q+9)/(3q+4)=(7m-1)/(3m).        (G)

The relevant coefficient is3(m+n)-1, NOT3(m+n)-2: only ONE
transverse derivative lowers the s-order in the bracket. A temporary
scratch estimate using the latter coefficient was rejected before
publication and is not a premise of this proof.

## 5. Complete equality supports and the cubic/quintic identity

Let k0=7q+9, so r=k0/m and gcd(k0,m)=1 since
3(7q+9)-7(3q+4)=-1. Both2r=14/3-2/(3m) and3r=7-1/m
are nonintegral for m>=4. Integral original orders and coalescence
therefore put alpha and beta strictly later, so V=Y³.

An initial F term of index l requires ord c_l=(3m-l)r to be an
integer. Hence m divides l, and l<3m. The full P has exactly the
allowed support {0,m,2m,3m}. Similarly a correction term of B at
3nr requires ord w_l=(3n-l)r a positive integer, so
l=1 mod m and l<3n=5m+1. Thus the COMPLETE Q has support contained
in {1,m+1,2m+1,3m+1,4m+1,5m+1}. This is an original-order
integrality argument, not an unjustified truncation of B.

Euler weights h=1/(3m), deg_Euler P=1 and deg_Euler Q=n/m
give, for scalar-coefficient monic polynomials C,D of degrees3,5,

    T=Y^m/X^(1/3),
    P=X*C(T), Q=X^(5/3)*Y*D(T).

The X-derivation's constants are kbar, so coefficients really are
field scalars, not unspecified functions of X. Direct differentiation
or Euler gives

    [P,Q]=X^(5/3)*(n*T*C'D-m*T*C*D'-C*D).

Equating with(E) gives(B). In particular C(0)D(0)=c!=0, and C,D
have only simple nonzero roots, since evaluating(B) at a repeated
root would make its nonzero right side vanish. No existence theorem
for these polynomials is needed for the reduction.

## 6. Normality narrows the equality to one actual contact

First the coefficient of T² in C cannot vanish. To see this, suppose
C=T³+v*T+w and reciprocate

    c0(x)=x³C(1/x)=1+v*x²+w*x³,
    d0(x)=x⁵D(1/x), d0(0)=1,
    a0=n/m=(5m+1)/(3m).

Equation(B), with a nonzero right side K0, becomes exactly

    3m*c0*d0'-(5m+1)*c0'*d0=K0*x^7.

Formal differentiation of d0*c0^(-a0) shows that d0 agrees with
c0^a0 through degree7. Since deg d0<=5, its degree6 and7
coefficients vanish. With the hypothesized absent linear term in c0,
those coefficients are

    binom(a0,3)*v³+binom(a0,2)*w²,
    a0(a0-1)(a0-2)*v²*w/2.

Here a0 is neither0,1 nor2. The second equation forces v=0 orw=0;
the first then forces both zero. Thus C=T³, contradicting C(0)!=0.
The coefficient of T² is nonzero, and deg U>=2m, so d>=2m.

On the other hand(G) and(F) force

    (3m-d)r <= j <= 7(m-d/3)-Delta,
    Delta <= 1-d/(3m).                               (H)

Integral delta has Delta=1 and hence d=0, impossible. For d=1 mod3,
Delta=2/3 gives d<=m, impossible. For d=2 mod3, Delta=1/3 gives
d<=2m. Thus d=2m, j=m*r=k0, and every inequality is an equality.
Equality in the global factor budget(C) forces exactly(A), with no
extra homogeneous factor. At either triple line the initial transverse
identity gives F_j=lambda*X^(1/3)*zeta0^(2m), so the coefficient of
T² in C is this same lambda!=0. Both actual triple charts give the
same sign and coefficient; comparing them alone adds no contradiction.

## 7. Honest controls, research meaning and read perimeter

- c=0 permits commuting powers and removes every nonzero-target step.
- A general cubic right deformation has BOTH linear and constant terms;
  only integrality at the derived resonance removes them from its initial.
- Losing the original integral order lattice would allow other P,Q
  supports, invalidating the fixed cubic/quintic reduction.
- The simple-factor target must be nonzero generically. The changed
  target2c*a*b² vanishes at b=0 and is not covered by that argument.
- The full cubic-chart target has a transverse correction after its
  constant initial. Satisfying(B) does not satisfy that later correction,
  separated regimes, the full original bracket, or a reverse-source lift.

This is a NEW exact necessary coalesced interface, pending hostile review.
It deliberately leaves the algebraic existence/classification of(B) open
within this proof. A separate Astra task solves the standalone identity
without assuming this attachment; its live report is NOT a premise and
has not been read. A positive ODE solution would be a formal leading
datum, not a polynomial receiver or counterexample.

Proof-pattern sources read WHOLE this continuation:
xmodel/triple-cubic-source-coalesced-astra-20260909.md,
SHA1620f9ef6b2edc598d35cab274cdfcc24d71353d18132d3a35ffb59fd2c46099;
xmodel/triple-one-plus-double-separated-astra-20260909.md,
SHA7709b0da88c6fa42fcbea38b9209573855edb1d6167c2cb77c1f8e374a5d1368.
Their current hashes were rechecked09:15:53 after whole reads; this is
post-read identity verification of already accepted pattern sources, not
a newly claimed pre-read custody check. The latter source's old G-based
separated argument and its later recorded corrections are NOT premises.
The root-authored finite-reference/whole-B proof e55b07e6... and reviewed
16i framework provided context; the current proof rederives every arrow.
The F10 source draft cc6edcb... was custody-first/whole-read09:05–09:07
to identify a prospective client, not to assert its still-unreviewed map.
No live Fable gate or current ODE peer report body, new literature fetch,
original high-power expansion, executable calculation or protected-tree
access occurred. The unrelated terminal F2 source review was collected
during final own-body reading; none of its mathematics is a premise here.

No new campaign OPEN token is raised here: the two bounded pending tasks
are the independent source gate and standalone ODE discriminator already
owned in LIVE STATE. Whole separated source coverage is expressly absent.
All claims remain receiver-local over fields, not nilpotent coefficient
rings. Own whole-body and own-only raised-OPEN check precede sealing.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14218`.
- Body SHA-256:
  `70f894acf008f40cea54707fcd1cf27db878df4ee24dd91cb8fb0e038c96c2da`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
