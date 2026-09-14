# Moh source audit and a uniform bare-tower Belyi identity

Status: structural partial only. No proof of the all-t radical or
nonzerodivisor atom is claimed. This note uses the frozen Moh PDF and frozen
terminal/DEP/closed-form reports whose hashes the root lane verified. The
only external primary-source lookup located Moh's 1982 paper underlying
Theorem 1.2; no new theorem from that paper is imported below.

## 1. What the frozen Moh theorem actually says

Source: `inputs/moh1983_jram340_configurations_of_roots.pdf`, printed pp.
148–149, Definitions 1.4–1.5 and Theorems 1.1–1.2. Images used for visual
verification are `moh-p149.png`, `moh-p208.png`, `moh-p209.png` in this driver
directory. `moh.txt` is an OCR extraction, useful for navigation but not a
substitute for the formulas in those images.

Let k be algebraically closed of characteristic zero and K its Puiseux
series field. A system of pi-roots sigma_i is *complete* when their discs
are disjoint and their multiplicities l_i add to the degree of the
polynomial. It is *coherent* when ord f(sigma_i)=lambda is independent of
i. Theorem 1.1 requires d dividing every l_i and says that the d-th
approximate root retains the system with multiplicities l_i/d.

Theorem 1.2 assumes an already-established coherent complete system with
accuracy lambda and a d-th quasi-approximate root h of that accuracy. In
the unique expansion

    f = h^d + sum_{j=1}^d h_j h^(d-j),  deg h_j < deg h = deg f/d,

its conclusion is

    ord h_j(sigma_i) >= j lambda/d.

It does not assert that a terminal coefficient is nonzero, that any
coefficient ideal has finite support, or that all small deformations of
the tower are trivial.

Printed p.208 applies this theorem to two chosen discs with accuracies
-1 and -3/4, obtaining the quartic h, cubic A, quadratic B tower and
restrictions on its low-degree coefficients. Printed p.209 makes a
further normalizing transformation and expands one member in fractional
powers of the other, reducing the finite computation to ten coefficients
in that particular case. The passage is a reduction to a remaining
computation; it contains no all-index nonzerodivisor conclusion.

Consequently merely recognizing the K16 h/A/B tower does not satisfy a
new theorem hypothesis that kills the residual atom. An attempted new
application must provide actual disjoint root discs, their complete
multiplicity count, equal accuracies, and divisibility by the chosen
approximate-root index; it must then extract a conclusion beyond the
coefficient bounds already encoded in the ansatz. No such stronger
conclusion was found in the charged source.

The relevant cited primary paper is T. T. Moh, *On two fundamental
theorems for the concept of approximate roots*, J. Math. Soc. Japan 34
(1982), 637–652,
<https://www.jstage.jst.go.jp/article/jmath1948/34/4/34_4_637/_article/-char/en>.
The local frozen 1983 Theorem 1.2 is sufficient for this applicability
audit; no assertion about an unread theorem in the 1982 paper is used.

## 2. A new uniform rational-map identity

All assertions in this section are proved for every integer t>=2,
factorwise in the quadratic coefficient algebra. Work over any
algebraically closed characteristic-zero field containing one root d of
3d^2=t+1. Put

    q=2t+1, e=3t+1, y=(d+t+1)/(2q),
    g1=e/q, g2=e(d+q)/(2q^2),
    g=e t(3d+2t+2)/(6q^3).

The banked bare pair (all residual variables zero) is

    h=pi^3 z,
    Q=h^q + h^(t+1)/pi + y h/pi^2,
    P=h^e + g1 h^(2t+1)/pi + g2 h^(t+1)/pi^2 + g h/pi^3.

These are polynomial expressions in (z,pi), notwithstanding the useful
Laurent presentation. On the dense torus put v=pi h^t and define

    f(v)=v^2+v+y,
    G(v)=v^3+g1 v^2+g2 v+g.

Then

    Q=h^q f(v)/v^2,
    P=h^e G(v)/v^3,
    P^q/Q^e = R(v):=G(v)^q/(v f(v)^e),

because 3q-2e=1. The normalizer implies the exact identity

    v(q f G' - e f' G) - f G = -yg.                    (B1)

This is not an asymptotic equality. For a direct hand verification,
expand its degree-five left side and substitute the displayed g1,g2,g;
each nonconstant coefficient is zero after 3d^2=t+1, while the constant
coefficient is -yg. The driver `belyi_identity.py` performs this finite
symbolic identity exactly in Q(t)[d]/(3d^2-t-1), without specializing t.

Both y and g are units factorwise. Indeed their quadratic norms are

    N(y)=(t+1)(3t+2)/(12(2t+1)^2),
    N(g)=t^2(t+1)(3t+1)^2(4t+1)/(36(2t+1)^6),

which are nonzero for t>=2. The identity (B1) now proves that f and G are
coprime and squarefree: a common root, a repeated root of f, or a repeated
root of G would make the left side zero. Neither polynomial vanishes at
v=0. For an additional exact check the driver computes

    Res_v(f,G)
      = t^2(t+1)((6t+9)d+5t+5)/(72(2t+1)^6).

Differentiating R and using (B1) gives

    R'(v)=-yg G(v)^(q-1)/(v^2 f(v)^(e+1)).             (B2)

Thus R is a degree D=3q=6t+3 rational map on the projective v-line whose
only branch values are 0, infinity, and 1. Its ramification partitions
are exactly

    over 0:        (q,q,q),
    over infinity: (e,e,1),
    over 1:        (5,1^(D-5)).                       (B3)

Proof of the last partition: the monic numerator and denominator both
have degree D, so R(infinity)=1. Equation (B2) says

    R'(v)=-yg v^(-6)+O(v^(-7)),
    R(v)=1+(yg/5)v^(-5)+O(v^(-6)).

Infinity therefore has ramification index exactly five over 1. Every
other point over 1 is finite and avoids the roots of f,G and v=0, so
(B2) makes it unramified. There are D-5 such points. The total
ramification is

    3(q-1)+2(e-1)+4 = 12t+4 = 2D-2,

which also verifies completeness of the listed branch data.

This is a structural identity with a constant-size symbolic proof for
the entire ray. It is a new description of the bare normalizer; it does
not by itself decide a residual coefficient ideal.

## 3. Exact controls and why passport rigidity is insufficient

The foreground command

    timeout 1800 stdbuf -oL python3 box/k16astra-20260905/belyi_identity.py

finished with exit code zero. Its log is `belyi_identity.log`. Besides
the uniform identity it checks both algebraic conjugates exactly at
t=2,3,4. At t=2 the two factors are rational:

    y=1/5: g=7/125,  deg(G^5-v f^7)=10, LC=7/3125;
    y=2/5: g=21/125, deg(G^5-v f^7)=10, LC=42/3125.

In both cases G^5-v f^7 is squarefree and the map has the same passport
(5,5,5), (7,7,1), (5,1^10). Yet the banked residual controls distinguish
these two factors: y=1/5 admits the positive-dimensional b3-axis, while
y=2/5 has a zero-dimensional cone. Therefore a theorem using only the
passport (B3), the degree, or the ramification count cannot decide V0.
These data are literally identical in the two control cases.

More precisely, the rational quotient R exists here because the bare
generic Q=a curve is

    h^q=a v^2/f(v),

with its cyclic automorphism h -> zeta h for zeta^q=1. P transforms by
zeta^e, so P^q descends to R. The lower residual coefficients do not
manifestly preserve this cyclic action. In particular, one may not
invoke rigidity of three-point covers for an arbitrary cone point
without first constructing an actual quotient to the projective line
and showing its three branch values persist. The generic linear
Jacobian condition alone supplies neither assertion.

A potentially useful stronger next step is a theorem on deformations
of the *marked* cyclic cover and its exact differential, including the
two pole orders e and the simple pole and the marked punctures. It must
allow the known t=2,y=1/5 family and explain its special factor. This is
substantially more information than (B3); no such theorem is proved
here.

## 4. Hyperelliptic ramification bookkeeping (shared with structural agent)

For clarity this records the independent geometric calculation that
motivates the marked-cover requirement; the structural agent treats
the exact-differential obstruction further. Write x=1/pi, L=h-b4,
V=L^2 C-yb3. Then

    Q=U+Vx+yLx^2.

The generic Q=a curve has the quadratic model

    Y=2yLx+V,
    Y^2=F_a(h):=V^2-4yL(U-a).                         (H1)

Its degree is 2t+2 with leading coefficient 1-4y, which is a unit:
the quadratic norm of 1+2d is -(4t+1)/3, and
1-4y=-(1+2d)/(2t+1). The polynomial F_a is squarefree over the rational
function field in the generic level a. A repeated root r with L(r)!=0
would satisfy L F_0'-F_0=0, a nonzero fixed polynomial, and would force
a to one of finitely many constants; generic a excludes this. At
L=0, either b3!=0 gives F_a(b4)=y^2b3^2!=0, or b3=0 gives
F_a'(b4)=-4y(U(b4)-a)!=0. Thus the smooth projective model has genus t.

On that curve P has two poles of order e at the two h-infinity points
and one simple pole above L=0; generically no cancellation occurs. At
infinity this follows from f and G being coprime, already proved by
(B1). At L=0 it follows by using x as a pole parameter in the original
Q/P expressions (the b3=0 case has L of order two and x of order -1).
The degree of P is consequently D=2e+1=6t+3.

There are q punctures x=0, given by U(h)=a. They are simple for generic
a and P is finite there. In source coordinates these are pi-infinity
points, so they must not be counted as affine points. For the bare
pair, b1=b2=b3=b4=0, the differential formula has an x^4 zero at each
of these q punctures, giving index five at each. The Riemann–Hurwitz
budget is

    total ramification = 2t-2+2D = 14t+4,
    ramification at P-poles = 2(e-1)=6t,
    remaining ramification = 8t+4=4q.

The q bare punctures of order four use all of this remaining budget.
For a cone point with homogeneous constant tau!=0 they instead become
unramified: along Q=a,

    dP = -[tau+c b1x+c b2x^2+c b3x^3-cLx^4] dh/Y,
    c=-yg.                                            (H2)

The same 4q budget can then be supplied by the finite intersections
with the linear Jacobian locus. No numerical Riemann–Hurwitz
contradiction results; the count is exactly compatible with either
configuration. Proving that this particular algebraic deformation is
impossible requires the exactness/period information of (H2), not just
the degree or divisor degree.

## 5. Valuation warning

The user-suggested phrase that a dimension-one Cohen–Macaulay curve has
a discrete valuation at each point is not valid as stated. A
one-dimensional Cohen–Macaulay local ring need not be a DVR and may
even be nonreduced. For example k[s^2,s^3] at its cusp is Cohen–Macaulay
but not regular and not a DVR. A valuation argument must pass to the
normalization of each reduced irreducible branch (and keep branch and
point distinct); any claimed nilpotency conclusion must additionally
account for the nilradical. This correction does not refute a
normalization-based strategy; it fixes the required objects.

No job from this subtask remains running.
