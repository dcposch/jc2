# Independent quotient and exceptional-control audit

This audit uses only the hash-verified frozen charged inputs in
`/tmp/jc2-lane.Fz7unY/inputs`. The parent mechanically verified all ten
hashes before delegation. No live ideation submission, ledger, or Lean
tree was read or changed. Its fresh exact computation is
`audit_t2.py`, with output `audit_t2.json` and `audit_t2.log`, all in
`box/k16xempty-20260905/`. The computation ran as one foreground,
line-buffered Python process, with BLAS/OMP thread counts set to one,
and exited successfully in approximately two seconds.

**Verdict:** the quotient lemma and the two pieces are correct over
arbitrary coefficient algebras, including nonreduced ones. The requested
negative assertion that the exceptional t=2 fibre should have nonempty X
is false for the specified X. Both t=2 field factors have X empty. The
correct negative control is the nonempty, positive-dimensional original
cone at d=-1, y=1/5, whose reduced support is the entire free b-axis. That
axis is excluded from U and X by the requested inverse equations. This
exclusion is exactly compatible with the weak target and (8.1).

## 1. Coefficient field and reconstruction maps

Fix t>=2, q=2t+1, and a field factor k of Q[d]/(3d^2-t-1). This polynomial
splits over Q exactly at t=3m^2-1, m>=1, with factors d=+m and d=-m.
At t=3,4,5 it is irreducible, so one exact computation in the quadratic
number field covers both embeddings after base extension. At t=2 both
rational factors must be checked separately; the driver does so.

Let S=k[c1,...,c_(t-1),b], with the displayed generator order. Here the
cj are coefficients of the *translated* monic C(x), x=h-b4, and b=b3.
They are not independent root variables or the original unshifted Cj.
The high F3 reconstruction has scalar pivots

    2*omega*(k+2t+3+6d),  k=q-1,...,1,
    -2*alpha*d          for B.

For the first pivots,

    (k+2t+3)^2-(6d)^2=(k+2t+3)^2-12(t+1)>0.

The other stated scalar factors are nonzero at each permitted factor.
Thus solving these rows is a polynomial coordinate elimination with
scalar denominators only, over every k-algebra. The rows x^0,x^1 vanish
identically, and the unsolved equations are exactly E2,...,E_(2t).

The source-to-terminal map uses the original global triangular
coordinate change proved in the frozen 8point1 report, lines 540-638,
followed by translation. A useful notational detail is

    C1(original)=gamma_t*b4,
    c1(translated)=(gamma_t+t-1)*b4
                 =-q*p_Q(t,1)/p_C(t,1)*b4.

The translated coefficient's multiplier is also a unit: p_C is the
banked scalar pivot; the explicit p_Q(t,1) numerator contains
(-4t-3)d-2(t+1). It is strictly negative at the positive embedding; at
d=-s with s>=1 it becomes (4t+3)s-2(t+1)>0. Consequently b4=0 is exactly
c1=0, and no such divisor is lost. The higher triangular diagonal
coefficients are the same nonzero -p_Q/p_C as before translation.

No map divides by b, by a root of C, by C(0), or by a discriminant. The
coefficient ring therefore retains b=0, b4=0, C(0)=0, repeated roots,
and their nonreduced intersections. Passing from the entire cone to U
does deliberately discard B*eta=0, which is precisely the zero-target
locus and is not part of the weak-radical counterexample problem.

## 2. Scheme-level quotient, including the inverse coordinate

Write R=S/J, where J=(E2,...,E_(2t)). The relevant homogeneities are

    wt(cj)=j, wt(b)=t+1,
    wt(B)=q, wt(eta)=q-1, wt(Ek)=2q-k.

The weight-zero field d is fixed by the action. The affine schemes are

    U=Spec R[z]/(1-z*B*eta),
    X=Spec R[s]/(B-eta,1-s*B).

On U, both B and eta are units because their product is a unit in a
commutative ring. Define

    v=B/eta=B^2*z,       v^-1=eta^2*z,
    aj=cj*v^-j,          bX=b*v^-(t+1),
    sX=v^q/B.

These expressions belong to the coordinate ring of U. Homogeneity
gives E_k(a,bX)=0 and

    B(a,bX)=B*v^-q,
    eta(a,bX)=eta*v^-(q-1)=B*v^-q.

Moreover sX*B(a,bX)=1. Conversely, on Gm x X put

    cj=v^j*aj,    b=v^(t+1)*bX,
    z=v^-(2q-1)*sX^2.

Since B_X=eta_X=sX^-1, their reconstructed product is
v^(2q-1)*B_X^2, and its product with z is one. The quotient B/eta
recovers v; the coefficient scaling recovers all cj,b; and

    v^-(2q-1)*(v^q/B)^2=v/B^2=1/(B*eta)=z.

Both compositions therefore recover even the inverse generator. These
are polynomial identities in the respective localized presentations,
not merely inverse maps on closed points. They prove

    U is isomorphic to Gm x X

over arbitrary k-algebras, including rings with nilpotents. No root
extraction or chosen nonzero coefficient is required.

Since adjoining a Laurent variable to a nonzero k-algebra remains
nonzero, U is empty if and only if X is empty. Also
R[(B*eta)^-1] is zero exactly when some power of B*eta is zero in R.
This establishes the direct equivalence

    X=empty  <=>  B*eta belongs to radical(J).

## 3. Main and boundary pieces, with complete maps

Write B=M+b*N and eta=rho+b*sigma, with all four coefficients in
k[c1,...,c_(t-1)]. Define

    Delta=N-sigma, A=rho-M, H=N*rho-M*sigma.

The two identities needed for all branch changes are literal identities
before taking any quotient:

    B-eta=b*Delta-A,
    H=M*Delta+N*A.

On X restricted to Delta invertible, b=A/Delta and
B=eta=H/Delta. Because B is a unit, H is a unit there too. For
d_k=deg_b(E_k), with d_k=0 for a zero row, put

    F_k=Delta^d_k*E_k(c,A/Delta).

These are polynomials and are equivalent to the original rows after
inverting Delta. The main piece is

    Spec k[c1,...,c_(t-1),u]/(F_k,1-u*Delta*H).

An explicit map back to X uses

    Delta^-1=H*u, H^-1=Delta*u,
    b=A*H*u, s=Delta^2*u.

Conversely the map from X with Delta inverted is
u=s*Delta^-2. These maps use the literal declared coefficient images.

The closed complement is the scheme defined in X by Delta=0. Since
B-eta=b*Delta-A, its ideal is exactly

    (E_k, Delta, A, 1-s*(M+b*N)).

It is important to call these an open piece and a closed piece, not an
open affine cover or an isomorphism from their disjoint union to X.
They exhaust the underlying points, which is sufficient for emptiness.
There is also an elementary ring proof that includes nilpotents. If
R_X[Delta^-1]=0, then Delta is nilpotent in R_X. If R_X/(Delta)=0, then
Delta is a unit in R_X. A nilpotent unit forces R_X=0. Thus unit ideals
for both pieces imply X is empty without any reducedness assumption.

The inverse row 1-u*Delta*H is inhomogeneous. In fact Delta itself is
the difference of weight-t and weight-(t-1) polynomials, and A is the
difference of weights 2t and 2t+1. The original positive grading is
broken by this intrinsic normalization. Therefore the original
homogeneous-projective properness argument cannot simply be applied
to a unit computation modulo one prime in this main ring.

## 4. Fresh t=2 computation and the exact exceptional family

The driver enters the full displayed F3 directly in SymPy over Q. It
solves all high coefficients through their exact scalar pivots, checks
that x^0,x^1 and every high row vanish, and then constructs B, eta and
E2,E3,E4. It independently checks exact-Q Groebner bases for U, X,
the main piece, and the boundary. Every one is the unit basis [1] on
both factors. It also checks that the original cone ideal is nonunit
and that deleting all E rows from X produces a nonunit ideal.

At d=-1, y=1/5 the output is

    B=18*c^5/125-3*c^2*b/5,
    eta=3*c^4/10+9*c*b/2,
    E2=441*c^8/2500-6*c^5*b/25-9*c^2*b^2/4,
    E3=102*c^7/25-93*c^4*b/5,
    E4=177*c^6/50-33*c^3*b/2.

It verifies the exact polynomial identity

    B*eta=(6*c/5)*E2-(72*c^2/1025)*E3
                         +(171*c^3/5125)*E4.             (* )

The reduced standard basis has the same ideal as

    59*c^6-275*c^3*b,  c^4*b,  c^2*b^2.

Its radical is (c): any geometric point with c nonzero has b=0 by
the third generator and then c=0 by the first, a contradiction. All
points with c=0 satisfy the ideal. The reduced support is thus the
whole b-axis and is positive-dimensional. Substituting c=0 in the
reconstructed W gives exactly

    C=x, W=-25*x^5/4+(5*b/2)*x^2, B=eta=0,
    b arbitrary.

The driver verifies F3 identically on this family. Every member has
1-z*B*eta=1, and every member has 1-s*B=1. Hence no member lies in U
or X. This is the demanded boundary exclusion, and it forces the
opposite of the prompt's proposed nonemptiness control.

There is more information than pointwise vanishing here: (*) puts
B*eta in J itself, so B*eta=0 in the full nonreduced cone ring. If
B*eta=sum a_k*E_k, then the following is an explicit exact unit
certificate in the unspecialized X polynomial ring:

    1=s^2*sum(a_k*E_k)
      +(1+s*B)*(1-s*B)+s^2*B*(B-eta).

For the complementary ring replace its last term by

    s^2*B*b*Delta-s^2*B*A.

Both displayed unit identities are independently expanded and checked
by the driver, on both t=2 factors. Thus the t=2 UNIT findings are
not solely claims made by an uninspected Groebner command.

On the exceptional factor specifically,

    Delta=-3*c^2/5-9*c/2,
    A=-18*c^5/125+3*c^4/10,
    H=-207*c^6/250.

The cleared E3 and E4 simplify to

    F3=9*c^8*(32*c-3325)/1250,
    F4=9*c^7*(7*c-580)/250.

On the main piece c is invertible because H is. The elementary
combination

    7*(32*c-3325)-32*(7*c-580)=-4715

therefore gives a direct localized contradiction from F3=F4=0. On
the boundary Delta=0 forces c=0 or c=-15/2 geometrically; A is nonzero
at the second alternative; and c=0 forces B=0, contradicting s*B=1.
The explicit unit identity above is the scheme-level certificate for
this elementary boundary explanation.

At d=+1, y=2/5, the output has

    B=165*b*c^2/32368-123975*c^5/74834816,
    eta=-33*b*c/119-186615*c^4/149669632.

The driver solves for an independent exact row identity. Its three
coefficients a2,a3,a4 are

    2115689453845*c/11574070520424,
    -2366259547242767*c^2/12592588726221312,
    13910882363130357*c^3/71358002781920768.

With the directly reconstructed E rows saved in JSON,
B*eta=a2*E2+a3*E3+a4*E4 checks identically. On c=0 the residual is
F=-2*b^2*x^4, so the free b-axis is absent away from zero on this factor.

As a nonunit control after dropping the E rows, the exceptional factor
has the rational point

    c=1, b=-13/425, B=eta=69/425, s=425/69.

It satisfies B-eta=1-s*B=0 and fails at least one genuine E row. The
driver checks this point exactly. This proves the normalization itself
does not make the entire coefficient space empty; the residual
equations supply the contradiction.

## 5. Weak target and the precise implication to (T)

The frozen source map identifies J with the high-eliminated positive
terminal row ideal I_+; its equation-level image is

    g*y*F(x)+3*x*(D0(x+b4)-D0(b4))=0.

Translation is triangular on nonconstant coefficients and multiplying
by x shifts the coefficient index. This is why the ideal correspondence
is available; equality of dimensions would not establish it. The target
identity modulo I_+ is

    tau=T_(t,0)-y*g=-(g*y/3)*B*eta,
    T_(t,0)=y*g+tau, wt(tau)=4t+1.

Since g*y is a scalar unit, the exact chain at each fixed t is

    X=empty
    <=> U=empty
    <=> B*eta is in radical(J)
    <=> tau is in radical(I_+)
    <=> (I_+, T_(t,0)) is the unit ideal                [(8.1)]
     => terminal normalized receiver is empty
     => the original K16 ray system at t has no solution
     => theorem (T) at t.

The last two implications consume the charged constant-spine,
normalizer, second affine spine and source-to-terminal reduction; this
audit does not independently reconstruct those upstream theorems.

For completeness, the weak radical-to-unit equivalence uses only
homogeneity, not V0. If tau^n=0 modulo I_+, then y*g+tau has the
finite inverse (y*g)^-1*sum_{j=0}^{n-1}(-tau/(y*g))^j. Conversely, if
tau is nonzero at a geometric cone point, a nonzero scalar lambda with
lambda^(4t+1)*tau=-y*g rescales that point to a common zero of I_+
and T_(t,0). That contradicts the unit ideal. Geometric points are
sufficient for radical membership over the characteristic-zero field.
Positive-dimensional cone components are allowed throughout.

At the exceptional t=2 factor (*) gives tau=0 even before taking a
radical, while the full cone has the free b-axis. Therefore (8.1) and
the banked implication to (T) are recovered there, and V0 is false.
Any test specification requiring X nonempty on this fibre would be
testing a different ideal or an incorrect negative control.

At t=3,4 the frozen exact controls have B*eta not in J but its square
in J; their lengths are 66 and 338. Thus a radical/emptiness calculation
should agree with (T) while preserving the distinction between first
and second powers. A new t=3,4 result of B*eta in J would contradict
those particular source controls and require an image or ring audit.

## 6. Scope of the audit

This audit proves no uniform emptiness statement at t>=3 and supplies
no characteristic-zero promotion of a modular main-chart computation.
It verifies the exact reduction and the exceptional controls, and it
removes the contradictory t=2 testing requirement by an explicit
polynomial certificate. Finite t computations and the requested
uniform obstruction are separate tasks owned by the parent lane.

No new exit-price assertion is made, so no charge-basis line applies.
