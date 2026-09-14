# First nonlinear modified-gap obstruction

PRODUCER RESULT / UNREVIEWED. Manual derivation only; no computation or source point.
First action 2026-09-10 22:17:09 UTC; publication reserve 22:34 UTC,
hard stop 22:37 UTC. Exactly the ROOT card and its four accepted reports
were current-pinned before fresh WHOLE reads. Old provisional headers are
superseded only by the accepted scopes named in the card.

## 1. Result and exact coefficient algebra

The first quadratic modified-band compatibility has the finite factored
determinant Delta_r in section3. It is defined over the WHOLE guarded leading
algebra, without choosing an entry of the late column or inverting p. Its
scaled form is rho² Delta_r. This is a necessary band obstruction, not a
uniform unit theorem. Section4 states the precise remaining unit certificate.

Fix r>=2 and write

    m=3r+1, n=5r+2, d=r+1, j=r-1, beta=3r,
    C=theta³+F theta²+H theta+a, D=sum_(i=0)^5 D_i theta^i,
    D5=1, D0=b, a*b invertible,
    m C D' - n C' D = -theta^7.                    (1)

All statements below hold in any commutative Q-algebra satisfying (1),
including nonreduced algebras. Use theta as a formal coefficient variable,
not an inversion of the original source S.

Here is the exact modified kernel, with the accepted17q homogeneous
read-back rho=1. Set kappa=7r+2, gamma=kappa/m, c1=H,c2=F,c3=1.
Define t0=1 and, for i=1,...,7,

    a*i*t_i=sum_(h=1)^min(3,i) ((gamma+1)h-i)c_h*t_(i-h).
    Tbase=sum_(i=0)^7 t_i theta^i,
    p=7t7/kappa, T=Tbase-(2p/7)theta^7,
    U=((m/kappa)C(T'+2p theta^6)-C'T)/theta^7,
    V=((n/kappa)D(T'+2p theta^6)-D'T)/theta^7.       (2)

The accepted modified numerator identities give POLYNOMIAL quotients
deg U<=2, deg V<=4, U2=p, V4=2p, and

    mCV'-(n-d)C'V+(m-d)UD'-nU'D+2p theta^6=0,
    maV0-nbU0=1.                                  (3)

Only the already-unit a and nonzero rational integers occur in (2).
In particular p is NOT presumed invertible or nonzero on any component.
For a scalar rho multiply U,V,p by rho; the read-back is then rho.
The literal original coefficient is u_src=-rho*p, not +rho*p.

## 2. What the zero-axis bridge actually proves

No free z is defined in the four charged accepted reports. Thus this report
does not silently identify an uncharged live presentation's z with a source
coordinate. The following independent weighted construction gives a precise
associated-graded slice where the advertised vanishing is valid.

Give S,t weights 1,r; give the actual coefficient variables weights

    wt(d_i)=r-i, wt(v_i)=2r-i, wt(k_i)=m-i,
    wt(u_src)=d, wt(ell)=m,

and give a new bookkeeping variable z weight1. Leading F,H,a,b have weight0
in this source-parameter grading. Homogenize the two fixed constants by

    Pi_z=z^(2r+1)t-u_src*t²+S*t³,
    A_z=S*t³+(S*dpoly-u_src)t²
            +(z^(2r+1)-u_src*dpoly+S*vpoly)t+kpoly,
    Delta_z=z^(7r+2)+u_src*z^(5r+1)t-ell*t*Pi_z-t*Pi_z². (4)

Every term of A_z has total weight m and every term of Delta_z has weight
7r+2. At z=1 these are exactly16r. The five coefficientwise Euler
inversions are homogeneous with fixed rational denominators, so homogenizing
their output is the same as applying them to (4). Their beta/gamma gauges
remain zero. This is a polynomial bookkeeping identity, not a localization,
source automorphism, new solution or permissible replacement of z=1 by z=0
in the complete source problem.

At z=0 take all first-r kernel coordinates zero. Accepted17q, in increasing
gap, gives all their source bands and mate bands zero: their mixed forcing
is zero because all its earlier factors are zero. At gap d take (2) times rho.
In actual source coefficients this means

    u_src=-rho*p,
    v_(r-1)=rho*(U1-Fp), k_(2r)=rho*U0,
    dpoly=F*S^r, v_(2r)=H, k_m=a.                 (5)

Keep k_(r-1)=k as the gap2d variable and set the other still-free
positive-weight coefficient parameters to zero, including ell. Formula (4)
then has A bands ONLY at gaps 0,d,2d through gap2d:

    A_z|_(z=0)=S^m C(theta)+rho*S^(m-d)U(theta)+k*S^j
               through this gap.                 (6)

The term -u_src*dpoly contributes only at gap d, and is already included
in (5). In this slice all polynomial coefficient expressions depend only on
rho,k with weights d,2d. Therefore homogeneous Euler reconstruction has no
mate bands at gaps d<h<2d. In particular the critical gap2d-1 vanishes.
Equivalently its source fixed t term and target -2S*t^5 are multiplied by
z^(2r+1); both vanish here. At z=1 that critical source band contains theta
and CANNOT be set to zero by this argument.

At gap2d the mate band has weight n-2d=3r. Its only theta³ slot is the fixed
16r coefficient B3(0)=u_src²=rho²*p²; higher theta slots are impossible.
The varying part has degree<=2. This is also read directly from the upper
row of (4) and its homogeneous reconstruction. The bracket target at this
gap is exactly -rho²*p² theta^5. All other direct target terms have larger
gap after z=ell=0. Thus (6) is a legitimate formal weighted restriction of
the accepted recurrence; it does NOT assert an actual z=1 source axis.

## 3. Full forcing and one finite factored determinant

Work first at rho=1. Write U=sum_(i=0)^2 U_i theta^i and
V=sum_(l=0)^4 V_l theta^l from (2), with out-of-range coefficients zero.
Every self-interaction term is retained by

    W=2r U V'-(4r+1)U'V,
    W_q=sum_(i+l=q+1)(2r*l-(4r+1)i)U_i V_l.       (7)

The fixed mate piece is Zfix=p² theta³. Put

    E(Z)=mCZ'-3r C'Z,
    Fcal=E(p² theta³)+W+p² theta^5.                (8)

The sign of the last term is PLUS because the actual target coefficient
is -p² theta^5. The theta5 coefficient of E(Zfix) is
3(m-3r)p²=3p². From U2=p,V4=2p, that of W is
2r*(8p²)-(4r+1)*(4p²)=-4p². Thus the full theta5
coefficient is 3p²-4p²+p²=0, and deg Fcal<=4.
This cancellation needs no p division.

For complete finite evaluation without expanding any source, define

    f4=W4+3(r+1)F p²,
    f3=W3+3(2r+1)H p²,
    f2=W2+3ma p²,
    f1=W1, f0=W0.                                (9)

These are exactly every coefficient of Fcal. For any P=sum_(q=0)^4 P_q theta^q
define three fixed-rational pivots and two linear functionals:

    x2(P)=P4/(3r-2),
    x1(P)=(P3+2F*x2(P))/(6r-1),
    x0(P)=(P2+(1-3r)F*x1(P)+(3r+2)H*x2(P))/(9r),
    pi1(P)=P1+H*x1(P)+2ma*x2(P)-6rF*x0(P),
    pi0(P)=P0+ma*x1(P)-3rH*x0(P).                (10)

Indeed the theta4,3,2 coefficients of E(x2 theta²+x1 theta+x0)+P are

    -(3r-2)x2+P4,
    -(6r-1)x1+2F*x2+P3,
    -9r*x0+(1-3r)F*x1+(3r+2)H*x2+P2.

All denominators in (10) are nonzero rational units for r>=2.
After these upper equations the FULL polynomial is
pi1(P)theta+pi0(P), not only its degree-leading term.

The promised finite factored expression is

    J(theta)=(r-1)D'(theta),
    g1=pi1(J), g0=pi0(J),
    c1=pi1(Fcal), c0=pi0(Fcal),
    Delta_r=pi1(J)*pi0(Fcal)-pi0(J)*pi1(Fcal).      (11)

Equations (2),(7),(9),(10),(11) are one exact finite rational recipe in
the whole leading algebra. They specify every coefficient by bounded sums
and rational pivots, not an unknown resultant or a claimed computed scalar.
For example J4=5j,J3=4jD4,J2=3jD3,J1=2jD2,J0=jD1.
No choice of a nonzero g entry, global Bezout coefficients, field factor,
root or extra normalization enters (11).

Restoring rho, write the degree<=2 mate part as

    Z=sum_(i=0)^2 (k*x_i(J)+rho²*x_i(Fcal))theta^i.

Then the COMPLETE gap2d mate is rho²*p² theta³+Z, and the remaining
two literal band equations are

    g1*k+rho²*c1=0,   g0*k+rho²*c0=0.             (12)

They occupy [S^(4r)]E1_res and [S^(5r)]E0_res. These positions follow from
the band weight 7r+2-2d=5r; no all-r row-count or cover theorem is used.
Eliminating k from (12) gives exactly

    rho²*Delta_r=0.                               (13)

Thus Delta_r is independent of k and the obstruction is homogeneous
quadratic in the modified-kernel scale. Equation (13) is necessary,
not in general sufficient for (12). All other residual equations, the
leading relations, inverse-boundary conditions and the top guard remain.

## 4. Unitness: exact reduction, no accepted shortcut

For j=r-1 the accepted17v theorem gives the WHOLE-IDEAL identity

    (g1,g0)=(H6(alpha),H7(alpha)),
    alpha=(n+j)/m=(6r+1)/(3r+1),
    H_i(alpha)=[theta^i](C/a)^alpha.               (14)

Consequently Delta_r belongs to this contact ideal. In particular on its
contact quotient Delta_r vanishes automatically. A proof that Delta_r is
a unit would already prove this particular late contact ideal is the unit
ideal. The charged17v result explicitly does not prove that assertion.
Its (H5,H6,H7)=B statement only makes H5 invertible ON the contact quotient;
it does not make that quotient zero. Using it to assert Delta_r invertible
would reverse the implication.

Even a future proof of (g1,g0)=B alone would not settle the issue:
the forcing pair could be a multiple of that column, giving Delta_r=0.
Thus both the homogeneous contact and the specific quadratic forcing matter.
No actual leading counterexample or uniform unit proof is established here.
The independent finite expression (11), not a claimed scalar factorization,
is the new obstruction available from these inputs.

A compact exact certificate interface can avoid keeping D as free variables.
The theta6,...,theta2 leading equations in (1), in order, give

    D4=(5r+1)F/(3r+2),
    D3=(2r*F*D4+(10r+3)H)/(6r+3),
    D2=(-(r+1)F*D3+(7r+2)H*D4+5ma)/(9r+4),
    D1=(-(4r+2)F*D2+(4r+1)H*D3+4ma*D4)/(12r+5),
    b=D0=(-(7r+3)F*D1+rH*D2+3ma*D3)/(3n).         (15)

The remaining literal leading relations are exactly

    e1=-(2r+1)H*D1+2ma*D2-2nF*b,
    e0=ma*D1-nH*b.                                (16)

To verify (15), the successive coefficients of the unknown D4,D3,D2,D1,D0
are -(3r+2),-(6r+3),-(9r+4),-(12r+5),-3n. They are rational units; all
other terms in those rows are precisely the numerators displayed. The
theta7 coefficient is 5m-3n=-1, already correct. Thus no leading component
is lost by using (15) over ANY Q-algebra. The universal guarded leading
ring is represented by Q[F,H,a,omega]/(e1,e0,omega*a*b-1), with b as (15).

Induction in (2) gives a^7*p,a^7*U_i,a^7*V_l polynomial in these leading
variables with rational coefficients. Equations (7)-(11) then show

    Delta_sharp=a^14*Delta_r

is a polynomial, after the fixed rational substitutions (15).
This is a conservative denominator bound, not an expanded coefficient
payload or measured degree. Since a is a unit, Delta_sharp is a unit
exactly when Delta_r is.

The smallest explicit next certificate requested by this report is ONE
literal polynomial identity, for the actual fixed integer r (or a genuinely
uniform family with all integer denominators justified):

    1=A*Delta_sharp+B*e1+C0*e0+E*(omega*a*b-1).     (17)

All four cofactors must be finite exact rational polynomials in F,H,a,omega,
and every coefficient of (17) must check. No such cofactors are possessed,
computed or asserted. This is a precise whole-ring unit obligation, not
generic-Q(r) evidence, a sampled-r test, a selected leading component or
an unknown resultant labelled nonzero. The missing property is (17).

## 5. Changed-object controls and exact limits

Omitting the fixed mate p² theta³ changes the theta5 coefficient of (8)
from zero to -3p². Omitting the target correction changes it to -p².
Omitting the self-bracket instead leaves 4p². These are literal changed
polynomial identities; no assertion that p is nonzero at an actual leading
point is needed. None permits dropping the corresponding term on the p=0
stratum.

Dropping the z bookkeeping at the critical gap is independently invalid:
at z=1 the fixed A term t gives a nonzero theta band at gap2d-1, and its
target contains -2S*t^5. The zero-slice argument cannot remove those from
the complete source. Identification with any separately named free-z
presentation is not imported or claimed.

Keeping only one of (12), or inverting an arbitrary g entry, loses a
necessary compatibility or a leading component. The determinant itself
does not replace the pair over a general ring. For example in
Q[epsilon]/(epsilon²), take g=(epsilon,0), c=(0,epsilon): its determinant
is zero but g*k+c=0 is impossible. This is an abstract linear-algebra
control, NOT an actual leading/source counterexample. Even if Delta_r
were a unit, (13) would give rho²=0, not rho=0 in every nonreduced algebra;
the square equation must be retained. Over a field it would exclude
nonzero rho on this formal axis only.

There is no leading nonemptiness assumption, all-r rank/cover theorem,
highest-block regularity claim, source-zero statement, actual F10 point,
Keller or JC2 conclusion. No actual coefficients, source powers, finite
matrix, CAS, arithmetic subprocess, implementation, network or worker
were used. All remaining full residuals/forcing/guards must remain in any
future source use. This report authorizes no computation or follow-on.

## OPEN(S) RAISED / own-only collision check

One unresolved mathematical quantity: unitness of Delta_r for every actual
r>=2, equivalently (17). Cheapest exact next check is a genuine finite
identity (17), not a generic nonzero-function calculation; no run is
authorized. The formal weighted-slice bridge has been proved explicitly,
but its identification with an uncharged presentation is outside scope.
No actual z=1 axis attachment is asserted.

Own report/box targets were absent initially and final-path collision is
checked before publication. No corpus or shared OPEN ledger was consulted.
All five input read modes and current pre/post pins, own WHOLE review,
transaction verification and terminal idle times accompany custody.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13713`.
- Body SHA-256:
  `445a49d1a79a2f9afb977e035a960f334c9d60525316ad688cb6f1148915d066`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
