# Mixed residue shortcut: explicit three-coordinate formation identity

MANUAL co-research, not FIRST/promotion. First action2026-09-12
23:35:48.949689244 UTC; reserve23:52/HARD23:55 unchanged. Four input pins
matched before bodies; reduction note, scalar gate and producer source freshly
WHOLE; COORD exact-pin prior WHOLE reused. No execution or extra source.

## Result and exact scope

**NEW_FORMATION_IDENTITY; ALL-r UNITNESS STILL GAP.** The root-residue route
gives an explicit polynomial 3-by-3 pairing, using only coefficients5,6,7
of each of the two degree7 truncations. It removes the inverse-series-through14
and the64-term Cauchy sum used to form B in the supplied producer. This is an
exact formation simplification, not a measured speedup, a reduction of the
septic rank, or a proved reduction of the univariate gcd degrees7/21.
It does not decide all actual integer r or license a changed source/run.

Write phi=1+u+Xu^2+Yu^3 and a_k(z)=[u^k]phi^z. Let
T_z=sum_(k=0)^7 a_k(z)u^k. For ANY parameters z,w put

    B(z,w)=[u^14](phi'/phi) T_z T_w,
    Delta=X^2-4Y-4X^3-27Y^2+18XY.

Define three explicit coordinates, requiring ONLY a5,a6,a7:

    e0(z)=(z-7)a7(z)+(2z-6)X a6(z)+(3z-5)Y a5(z),
    e1(z)=(2z-7)X a7(z)+(3z-6)Y a6(z),
    e2(z)=(3z-7)a7(z).

Set e(z)=(e0,e1,e2)^T and the symmetric matrix

    G = [ -X^2-3XY+4Y,  2X^2-6Y,       Y(-X+9Y)       ]
        [  2X^2-6Y,     -X+9Y,          Y(2-6X)        ]
        [  Y(-X+9Y),     Y(2-6X),       Y(4X^2-X-3Y)  ].

Then the following is a UNIVERSAL polynomial identity, not merely one in
the leading quotient:

    z w Delta B(z,w) = - e(z)^T G e(w).                 (1)

The actual scalar is obtained by z=2t-1, w=4-t. Its nonzero rational factors
z,w and the known-unit Delta may then be retained explicitly. There is no
real-root, positivity, reducedness or chosen leading field assumption.

## 1. Residues and the top-three-coefficient defect

For Y Delta nonzero let a range over the three simple roots of phi. The
rational differential (phi'/phi)T_z T_w du/u^15 has residue B(z,w) at0,
residue T_z(a)T_w(a)/a^15 at a, and none at infinity: its coefficient is
O(u^-2) because deg(T_z T_w)<=14. Since phi(0)=1, no root equals0. Thus

    B(z,w)=-sum_a T_z(a)T_w(a)/a^15.

The truncated power equation has the exact defect

    phi T_z' - z phi' T_z
        = -u^7 (e0(z)+e1(z)u+Y e2(z)u^2).            (2)

Coefficients below7 vanish by the defining power-series identity; the only
remaining degrees7,8,9 give precisely the three displayed e-coordinates.
At a root a and z nonzero, (2) yields

    T_z(a)=a^7 (e0(z)+e1(z)a+Y e2(z)a^2)/(z phi'(a)).

Substitution converts the residue sum into a bilinear pairing on a cubic
quotient. Equation(1) below explicitly evaluates that pairing; it is not an
unevaluated trace/resultant condition or a request to enumerate roots.

## 2. Explicit cubic trace evaluation

At every root a one has

    Delta/phi'(a)^2 = W(a),
    W(u)=X^2-4Y-2XYu-3Y^2u^2.

Indeed Delta/phi'(a)^2=Y^2(b-c)^2 for the other roots b,c; their sum and
product give (X+Ya)^2+4Y/a, and 1/a=-1-Xa-Ya^2 reduces this to W(a).
Newton sums in the cubic, without source coefficients, now give

    sum_a W(a)/a  = -X^2-3XY+4Y,
    sum_a W(a)    = 2X^2-6Y,
    sum_a a W(a)  = -X+9Y,
    sum_a a^2W(a) = 2-6X,
    sum_a a^3W(a) = (4X^2-X)/Y-3.

For example sum1/a=-1, sum a=-X/Y and sum a^2=X^2/Y^2-2/Y;
the remaining powers satisfy the cubic recurrence. Multiplying the third
basis coordinate by Y removes the lone displayed Y denominator. These five
moments are exactly the entries of G. Together with(2) and the residue theorem
they prove(1) on z w Y Delta nonzero. Both sides are polynomials in
Q[z,w,X,Y], so equality there proves the universal cleared identity, including
specializations with repeated roots or z w=0. No residue formula at a
multiple root is silently substituted for this polynomial continuation.

As an algebraic check, det(G)=-Y^3 Delta^2. This follows from its weighted
Vandermonde representation: the three weights are Delta/(a phi'(a)^2),
the basis is1,a,Ya^2, product a=-1/Y and the squared Vandermonde is
Delta/Y^4. The sign is negative. Nondegeneracy of G does NOT make a specified
mixed pairing nonzero or a unit; no such inference is used.

An independent coefficient/sign check is v^T G v=-Delta for v=(1,2X,3)^T.
The leading z^8 coefficient of e(z) is v/7!, so(1) has the required
z^8 w^8 coefficient Delta/(7!)^2 on both sides. Also e(1)=e(2)=0,
agreeing with the exact degree-based B(1,w)=B(2,w)=0 controls.

## 3. Source attachment and the proposed discriminant/Jacobian shortcut

For actual t=(5r+2)/(3r+1), z=2t-1 and w=4-t are nonzero rational units.
The accepted leading ODE reads

    phi d' - t phi' d = -(3t-5)Y d5 u^7.

At a repeated root of phi its left side vanishes and its right side does not:
3t-5, Y, d5 and the nonzero root are units at a leading residue-field point.
Thus Delta vanishes at no such point and is a unit in the whole leading
algebra. This justifies using(1) on that algebra, retaining possible
nilpotents; no new foundational squarefreeness review is intended. At the
known excluded cube t=5/3, Delta=0, so cancellation of Delta there would be
invalid. The cleared polynomial identity itself remains valid.

ROOT's separately messaged candidate B=lambda(t)*Delta*J, with
J=det(d(d6,d7)/d(X,Y)), remains **UNPROVED**, not confirmed by weights.
A short exact expression makes its remaining content explicit. Put
v_k=[u^k]phi^(t-1). Coefficient differentiation gives

    J=t^2 (v4^2-v3 v5).                              (3)

Equivalently, use the charged U,V,K,P and c3=binomial(t,3). Write
f1=d6/c3 and f2=(d7-(t-2)d6)/c3=UY-V. Then P=U^2 f1(X,V/U).
Differentiating and reducing modulo P gives

    J = c3^2 P'(X)/U                               (4)

in the leading algebra: P'=U*(f1_X f2_Y-f1_Y f2_X) there. Both U and
P' are known units at the imported actual-r squarefree-septic scope, so this
candidate WOULD close unitness if its scalar lambda had no actual-r zero
or pole. Neither that identity nor its scalar/exceptions has been derived.
Formula(1) only changes its numerator to an explicit nine-product pairing;
it does not turn the candidate into a consequence of a nonsingular matrix.

The exact untouched elimination still asks whether P and U^7 B(t,X,V/U)
are coprime at EVERY actual rational t. A generic gcd1, a unit J, or a
nonzero determinant of G individually does not answer that question.

## 4. Concrete saving, exact gap and stopping rule

The supplied source forms all a0..a7 for two powers, an inverse series
through14, its logarithmic derivative, and a64-term Cauchy sum. Identity(1)
requires only the SIX named top coefficients a5,a6,a7 for z and w and one
fixed3-by-3 polynomial matrix. These coefficients can be specified directly
by the finite multinomial formula; no lower coefficients or inverse series
are intrinsic to the new formula. This is a genuine bounded symbolic
formation reduction, not merely B rewritten as an unevaluated root sum.

The numerator in(1) has ordinary degree at most10 in X,Y; universal exact
division by z w Delta recovers the SAME degree-at-most7 B. Alternatively
one may keep Delta as an explicit known unit. Keeping it in the eliminated
polynomial may INCREASE degrees; no claim of a cheaper gcd or smaller final
certificate follows. All current accepted source and runtime remain unchanged.
Any future implementation choice is ROOT's, after the required source review;
this report creates no code, fixture, registration or execution authority.

Exact unclosed step: prove e(2t-1)^T G e(4-t) is a unit on the whole actual
rank-seven algebra, or prove/refute the specific nonvanishing scalar multiple
of Delta*J with all rational exceptions controlled. No cancellation,
positivity, generic nonzero or parameter sample has settled it here.

Cheapest independent MANUAL check of this deliverable is(2), the five cubic
moments, and the nine-product assembly, not an all-r parameter farm. A
five-minute check is an UNMEASURED planning estimate only. Stop after this
closed formation identity and precise remaining question; no derivative,
pole, norm or control-family successor is selected. Mathematical status is
GAP for unitness, not workflow failure, source zero, REG, all-F10 or JC2.

## Read scope and publication

Exactly four inputs: reduction note7b8545a6, scalar gateaa8b0148,
producer8aee305b, COORD33cfa610. Full pins/read modes are in PINS; three
fresh WHOLE reads, and disclosed same-agent COORD WHOLE reuse from the
completed20:05-20:14UTC review after its fresh current hash. ROOT's in-task
discriminant/Jacobian and truncation suggestions are recorded as advisory,
not independent evidence. No new file input, live ROOT calculation or
pending peer output was read. All computation here is manual algebra;
no source/interpreter/CAS/import/AST/test/network/worker action occurred.

Own targets were absent before begin. No canonical OPEN or shared change.
Own WHOLE readback, unchanged postpins and own-only collision check precede
the unique final marker; custody is the last authored file. Terminal metadata
gives actual ALL WRITERS IDLE and expected-manifest verification.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9214`.
- Body SHA-256:
  `69dc7179cced10c80179aa75e453aaff052f1880b471159161b4894650bce996`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
