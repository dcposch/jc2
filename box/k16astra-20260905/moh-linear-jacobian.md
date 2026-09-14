# Linear Jacobian source audit and the boundary collision scheme

Status: new conditional structural consequences, no all-t atom proof.
Work factorwise over an algebraically closed field K of characteristic
zero. All K16 identities used below come from the charged DEP and terminal
reports; the additional source search was confined to primary papers.

## 1. A linear Jacobian does not imply either elementary factorization

For an arbitrary polynomial psi in K[y], put

    F_psi(x,y)=(x-psi'(y), xy-y psi'(y)+psi(y)).

Direct differentiation gives

    det dF_psi
      = (x-y psi''(y)) + y psi''(y) = x.              (L1)

When psi=y^n, n>=2, the map is

    F_n(x,y)=(x-n y^(n-1), xy-(n-1)y^n).

Given target coordinates (a,b), its fibre is described by

    y^n+a y-b=0,  x=a+n y^(n-1).

The map is finite and proper of generic degree n. Its critical line x=0
maps nonconstantly to the parametrized (n-1,n) cusp

    y -> (-n y^(n-1), -(n-1)y^n).

Thus a nonzero linear Jacobian, even together with properness and a
noncontracted critical line, permits arbitrary generic degree. It does
not force equivalence under source and target automorphisms to
(x^2,y), which has degree two, or to (x,xy), which is birational. Nor
does it impose even degree.

The n=3 case is the standard Whitney cusp map after a source shear. A
primary source is Bisi–Polizzi, *On proper polynomial maps of C^2*,
arXiv:0903.2144, introduction and Section 1.1:
<https://arxiv.org/pdf/0903.2144>. Their cited Lamy theorem requires
properness and generic degree two. Their complete higher-degree
classification concerns Galois coverings. Neither hypothesis is
available for a general K16 cone point. The family (L1) is verified here
by its displayed determinant and monic fibre equation, independently of
any classification statement.

## 2. Every K16 chart pair is nonproper

Use the charged notation, with P0=V-gb1, L=h-b4, and x=1/pi:

    Q=U(h)+Q1(h)x+yLx^2,
    P=P0(h)+P1(h)x+P2(h)x^2+gLx^3,
    Q1=L^2 C-yb3,
    P1=LS-b3 T-gb2,  P2=LT-gb3.

For any h0 in K, the source curve

    pi=x^(-1),
    gamma=x^(-1)+b1+b2 x+b3 x^2+(b4-h0)x^3

satisfies h=h0 identically. As x tends to zero its source point tends to
infinity, whereas

    (Q,P) -> (U(h0), P0(h0)).                         (L2)

Consequently the nonproper-value locus contains the whole polynomially
parametrized curve

    B_infinity = image[h -> (U(h),P0(h))].             (L3)

This holds before imposing the terminal ideal. U is monic of degree
q=2t+1, so the curve is nonconstant. In particular no theorem whose
essential assumption is a proper polynomial map can be applied to
these chart pairs. No claim is made here that (L3) exhausts the
nonproperness locus; establishing exhaustion requires auditing every
other boundary chart.

The display can equivalently be read by the valuative criterion with
the K((x))-point above and its finite target limit; it is not a claim
that affine source infinity is a finite point.

## 3. A hypothetical tau!=0 point makes the boundary an immersion

For a cone point, the charged identity is

    J_{gamma,pi}(Q,P)=-c z+tau pi,  z=pi-gamma,
    c=-yg,

where tau denotes the homogeneous constant coefficient, i.e. the
affine terminal constant plus c. The coordinate change gives

    J_{h,x}(Q,P)
      = tau+c b1 x+c b2 x^2+c b3 x^3-cLx^4.           (L4)

In particular at the added line x=0 the determinant is the nonzero
constant tau. The extended polynomial (h,x)-map is therefore etale
along the entire added line when tau!=0. Restricting its differential
to that line proves that

    (U'(h),P0'(h)) != (0,0)  for every h in K.         (L5)

The same conclusion follows directly from the coefficient identity

    Q1 P0' - U' P1 = -tau.

Thus (L3) is a polynomial immersion under the hypothesis tau!=0.
It is not automatically an embedding. The coefficient degrees are

    deg U=q=2t+1,  deg P0=e=3t+1,
    gcd(q,e)=1,  1<q<e<2q.

In fact the following elementary complete-intersection argument shows
that such an immersion necessarily has self-identifications.

## 4. Exact all-t boundary collision length

Let U,P0 be any two monic polynomials over K of coprime degrees q,e>1.
In K[s,r], form the divided differences

    A(s,r)=(U(s)-U(r))/(s-r),
    B(s,r)=(P0(s)-P0(r))/(s-r).                       (L6)

They are polynomials; no localization or undefined division occurs.
Their total degrees are q-1,e-1 and their highest homogeneous parts
are

    A_top=(s^q-r^q)/(s-r),
    B_top=(s^e-r^e)/(s-r).

These have no common projective zero. If r=0 both are nonzero at a
projective point. If r!=0, a common zero would give a number z=s/r
different from one satisfying z^q=z^e=1, impossible since gcd(q,e)=1.
At z=1 the respective values are q,e, which are nonzero in
characteristic zero.

It follows that the homogenizations of A,B have no common zero at
infinity. They cannot have a common projective curve component since
every projective plane curve meets the line at infinity. Their affine
intersection is consequently a finite complete intersection of
scheme-theoretic length

    length K[s,r]/(A,B)=(q-1)(e-1)=6t^2.              (L7)

This is a statement about the explicit two-variable collision ring,
not a degree-only nonvanishing claim for the high-dimensional terminal
ideal.

On the diagonal s=r one has A(s,s)=U'(s) and B(s,s)=P0'(s). If tau!=0,
equation (L5) excludes every diagonal point. Therefore the entire
length 6t^2 scheme is supported off the diagonal. Every support point
is an ordered pair s!=r with

    U(s)=U(r),  P0(s)=P0(r).                          (L8)

For K16 this yields the exact conditional residual:

    tau!=0 => an off-diagonal boundary collision scheme
              of length 6t^2 in K[s,r].              (L9)

The symmetry (s,r)<->(r,s) is free on support; lengths include
tangencies and higher self-intersections and must not be identified
with a count of ordinary nodes. At t=3,4 the conditional lengths are
54 and 96, respectively. No tau!=0 cone point exists at the banked
exact t=3,4 indices; these are implications to impossible hypothetical
points, not newly found examples.

This gives a concrete next target: rule out the collisions (L8) using
the extension (L4), its marked boundary geometry, and the K16 tower.
Simply replacing immersion by embedding would erase precisely the
remaining obstruction. If injectivity of (L3) could be established,
(L7)–(L9) would already contradict tau!=0 without any use of the
Abhyankar–Moh embedding theorem.

## 5. Primary nonproperness source check

Nguyen Van Chau, *A note on singularity and non-proper value set of
polynomial maps of C^2*, Acta Math. Vietnam. 32 (2007), 287–294:
<https://arxiv.org/pdf/0710.5212>.

Theorem 1.1 constrains degrees of a dicritical parametrization below a
non-singular series. Theorem 1.2 forces a singular series in a special
configuration where one coordinate tends to a constant and the other
has a nonconstant limiting polynomial. The discussion on p.3 uses an
already-assumed affine-line image and Abhyankar–Moh. Neither statement
turns an immersive parametrization into an embedding or excludes its
self-identifications. No applicable embedding theorem for the marked
K16 boundary was found in this bounded search.

The general possibility “nonproper linear-J map with noncontracted
critical line must be impossible” was considered, but no primary
theorem establishing it was located. It is not asserted here.

No new CAS job was required for this addition; all identities and the
collision-ring argument are displayed algebraically. No job remains
running.
