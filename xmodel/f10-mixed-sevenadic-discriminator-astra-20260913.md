# Seven-adic discriminator for the actual mixed scalar

MANUAL co-research; no scientific execution or source changes. First action
2026-09-13 02:34:06.662861309 UTC. Original reserve 02:47 / HARD 02:50 UTC.

This report records only the selected mixed-scalar question. The old
middle coefficient is not this scalar. Accepted generic/asymptotic unitness
does not remove the actual integer-parameter exception obligation.

## Result: two new mixed-scalar infinite families

For every actual integer r>=2 with r=1 OR2 modulo7, the SAME mixed scalar
B is a unit of the whole accepted leading algebra S_r. More precisely,
at every leading point over an algebraic closure of Q_7,

    r=1 modulo7: v_7(B)=-15/7;
    r=2 modulo7: v_7(B)=-14k-15/7, k=v_7(3r+1)>=1.

This settles two infinite families for this scalar, not merely the different
middle coefficient. It does not settle r=0,3,4,5,6 modulo7. Together with
the accepted ineffective large-r theorem, possible failures lie in a finite
but still unidentified subset of these five families. No actual scalar zero,
effective cutoff, all-r conclusion, REG or source exclusion is claimed.

## 1. Source valuations, with the normalization retained

Use tau=r/(3r+1), t=2-tau and the accepted old-to-new coordinate map:
old V is the present X and old W is the present Y. For r=1 modulo7,
tau=2 modulo7 and t=0 modulo7, with all these parameters 7-integral.
The accepted root argument gives v(X)=-2/7 at EVERY root of the degree-seven
source polynomial. This root-valuation result is imported; its conclusion
about the different middle Z is not used.

The charged reduction gives UY=V, where U,V now mean its compact quadratic
and cubic in X, not the old coordinate V. In U the leading term 3X^2 has
uniquely least valuation -4/7. In the compact V the constant

    (t-3)(t-4)(t-5)(3t-4)/420

has valuation -1; its three other terms have valuations -6/7,-4/7,-2/7.
Every displayed numerator factor is a unit modulo7. Thus v(V)=-1 and
v(Y)=-3/7. No extra component or inverse is selected: U is the accepted
whole-source unit, and here its value is also directly nonzero.

Choose pi with pi^7=7 and put x=pi^2 X, y=pi^3 Y. Both are valuation-zero
elements. The normalized source equation

    d6/binomial(t,3)=3Y^2/(t-2)+(6X+t-3)Y+K=0

has only X^3 and 3Y^2/(t-2) at valuation -6/7. Although binomial(t,3)
may be divisible by7, it is a nonzero rational for every actual r; this is
the already established rational source identity, not an integral division
claim. Multiplying it by pi^6 and reducing gives

    xbar^3=5*ybar^2.                                    (1)

The constant denominator t-2 is a 7-adic unit. Lower-weight terms vanish
under this reduction, and xbar,ybar are nonzero in the residue field.

## 2. The exact lowest-weight scalar computation

Temporarily restore the linear coefficient L in phi=1+Lu+Xu^2+Yu^3.
The scalar has weight15 for wt(L,X,Y)=(1,2,3). Therefore at L=1 its
terms of maximal X,Y weight15 are exactly its L=0 specialization.
All coefficients of the full scalar are 7-integral when t is 7-integral:
the two truncated powers use binomial(h,n), n<=7, h in Z_7, and integral
multinomial coefficients; these binomials are integral (for n=7 one of
seven consecutive numerator factors supplies the sole factor7 in 7!).
The logarithmic derivative coefficients are integral by formal inversion
of a series with constant term1. Hence every lower-weight term disappears
in the reduction of pi^15 B. No coefficient denominator can reverse this
valuation comparison.

For L=0 let q=z^3+Xz+Y and A_h=z^7 trunc_7(phi^h)(1/z). Direct polynomial
division, or the displayed powers z^3=-Xz-Y, gives

    A_h mod q=(h-1)(h-2)*[
       XY z^2+(Y^2/2+(h-3)X^3/6)z+(h-1)X^2Y/2].        (2)

This uses denominators only2,6. It follows directly by retaining the terms
z^7+hXz^5+hYz^4+binom(h,2)X^2z^3+2binom(h,2)XYz^2
+(binom(h,2)Y^2+binom(h,3)X^3)z+3binom(h,3)X^2Y.
Thus no arithmetic execution or coefficient payload was needed.

Here s=2t-1=6 modulo7 and b=4-t=4 modulo7. After (1), formula (2) reduces
in the cubic with coefficients xbar,ybar to

    A_6=6xy z^2+4y^2 z+x^2y,
    A_4=6xy z^2+ y^2 z+2x^2y.                           (3)

Bars are suppressed in (3). The Newton sums of z^3+xz+y are

    p1=0, p2=-2x, p3=-3y, p4=2x^2, p5=5xy.

Using x^3=5y^2, the four nonzero contributions to Tr(z A_6 A_4),
from z^5,z^4,z^3,z^2 respectively, are

    4y^5, 6y^5, 5y^5, y^5.

Their sum is 2y^5 modulo7. The universal reciprocal identity
B=-Tr(z A_s A_b) consequently yields

    residue(pi^15 B)=5*ybar^5 !=0.                     (4)

This explicitly includes every term of the lowest valuation, rather than
claiming one monomial was unique. Equation (4) proves v(B)=-15/7 at every
source root. The trace identity is a polynomial identity of multiplication
matrices, so does not presume separability of the auxiliary cubic. Its use
here is also independently transparent from the five Newton sums above.

## 3. The pole-parameter family r=2 modulo7

Here k=v_7(3r+1)>=1, v(t)=-k, and the accepted rescaled-septic argument
gives v(X)=-k-2/7 on every source root. Put x=X/t, y=Y/t^2 (these are
new scaled variables, not the valuation-zero variables of section1).
In U the term 3X^2 has valuation -2k-4/7, below its other terms.
In compact V the constant has valuation -4k-1; the cubic, quadratic and
linear terms have valuations -3k-6/7,-4k-4/7,-4k-2/7 respectively.
Thus v(Y)=-2k-3/7. Let xbar,ybar denote residues of pi^2 x,pi^3 y.
They are nonzero. Since V is initially t^4/140 and U initially3X^2,

    xbar^2*ybar=residue(7/420)=2.                       (5)

In the normalized d6 equation of section1, the three lowest-valued terms
are X^3,6XY,3Y^2/(t-2), with valuations -3k-6/7,-3k-5/7,
-3k-6/7 respectively. The middle one is strictly higher. Every remaining
term is higher too. Divide by t^3 and multiply by pi^6 to obtain

    xbar^3=-3ybar^2=4ybar^2.                           (6)

We now retain the factorial7 contributions exactly. After X=tx,Y=t^2y,
the full scalar is a polynomial in t of degree at most14, with rational
polynomials in x,y as coefficients. In a truncated-power coefficient of
u-degree n, a term with powers X^i Y^j uses m=n-i-2j factors and has
parameter degree at most m+i+2j=n. In a logarithmic-derivative coefficient
of u-degree n-1, the corresponding degree is at most n-1, since its log
monomial has at least one factor. Combining n1+n2+n3=15 proves degree14.

For every individual expanded term, let d be the number (0,1,2) of possible
factorial7 denominators. Such a denominator in truncation degree<=7 can
occur ONLY in the pure-linear u^7 term: in the multinomial formula the
denominator is e0!e1!e2!, and only e0=7 is possible. Each such occurrence
therefore consumes seven units of u-degree without x,y. If w=2i+3j is the
x,y weight of the entire term, w<=15-7d. Its coefficient has valuation
at least-d, so its value in x,y has valuation at least-15/7. This bound
holds coefficientwise in t. Consequently every t-degree<=13 contribution
has valuation strictly above -14k-15/7. This is a strict all-k bound, not
an approximation at a selected integer.

The degree14 coefficient uses only the first log monomial, and the leading
falling-factorial coefficients of the powers. Define, for this finite
coefficient calculation only,

    H_j(c)=[w^j]exp(c*(w+xw^2+yw^3)).

The degree14 coefficient is

    H7(2)H7(-1)
    +2x*(H7(2)H6(-1)+H6(2)H7(-1))
    +3y*(H7(2)H5(-1)+H6(2)H6(-1)+H5(2)H7(-1)).        (7)

This is a finite exact binomial leading-coefficient identity, not a new
formal-series computation or a replacement source. The residue of pi^j H_j
for j=5,6,7 is obtained directly from its finitely many monomials:

    j5: c^2*xbar*ybar;
    j6: c^3*xbar^3/6+c^2*ybar^2/2;
    j7: c^7/720+c^3*xbar^2*ybar/2.

The last line includes the pure-linear term c^7/7!, since pi^7=7.
All other terms have strictly larger valuation. By (5)-(6), these residues
are, in the order j5,j6,j7,

    c=2:  (4*xbar*ybar, 5*ybar^2, 6);
    c=-1: (  xbar*ybar,   ybar^2, 0).                   (8)

The zero in (8) is essential: the factorial term cancels the x^2y term.
The first term of (7), with two H7 factors, has valuation at least-2,
strictly above-15/7. Reducing pi^15 times the other two lines of (7) gives

    5*xbar*ybar^2 +4*xbar*ybar^2+ybar^5
      =2*xbar*ybar^2+ybar^5
      =6*xbar*ybar^2 !=0.                              (9)

For the final equality, (5)-(6) give ybar^3/xbar=4. Thus
residue(pi^15*t^-14*B) is (9), proving the claimed valuation at EVERY
source root, for every positive integer k. There is no discarded pole
order of the rational parameter and no chosen septic factor.

## 4. Whole algebra, controls and exact remaining boundary

At every actual r in the two families, all roots of the rational septic
have been covered over the algebraic closure of Q_7. Equations (4),(9)
exclude B=0 at every one. Since U is a unit, P and U^7 B(t,X,V/U) have no
common root, hence are coprime over Q. Their rational Bezout identity gives
an inverse of B in the WHOLE source algebra. This existence argument is
not a computed certificate. It does not need irreducibility of the scalar
polynomial, a selected embedding, or reducedness: the same Bezout identity
survives arbitrary base changes, including nonreduced ones.

The simplest analogous initial-form argument genuinely cancels for
r=3 modulo7. There t=1 modulo7, v(X)=-2/7, v(Y)=-3/7, and the source
initial relation is xbar^3=3ybar^2. But s=1 modulo7, and (2) gives A_s=0
at the initial level. Thus residue(pi^15 B)=0 there. This is a failure of
the first valuation test, not an actual B-zero or evidence that the old
middle scalar fails. Additional source-relative cancellation control would
be required before any nonzero next term could be claimed.

For r=0 modulo7 the old report has two X-valuation classes, -v(r) and-1/3,
and it resolves the DIFFERENT scalar using a separate Q_alpha equation.
That equation is not a mixed-B inverse. For r=4,5,6 the imported simple
root-slope hypotheses do not hold. Neither omission is repaired by field
irreducibility or by calling a perfect trace pairing nonzero on prescribed
vectors. No assertion about those five families is made here.

The exact remaining quantity is B-unitness for all actual r>=2 with
r=0,3,4,5,6 modulo7. The accepted cube theorem says failures are finite but
does not identify them. The already selected one univariate Bezout identity
with rational-parameter exception analysis remains a possible discriminator;
this manual result does not imply a smaller CPU/memory bound or justify a
new computational or residue farm. A continuation of this particular local
test would first have to determine the next nonzero source-relative term at
r=3; no such work is selected or delegated here. No new canonical OPEN.

## Read and publication scope

Fresh SHA-before-WHOLE reads: the two old seven-adic reports, the univariate
reduction, mixed-scalar FIRST, promoted cube FIRST intake, and the explicitly
optional reciprocal-trace report. COORDINATION uses the same-agent exact-pin
WHOLE read from the completed September12 20:05-20:14UTC review, with fresh
current pin before reuse. Linked reports and primary sources were not read.
The reciprocal identity has its own direct coefficient proof in the charged
text; only this finite trace identity, not its old lifecycle header or a
nonzero-pairing assertion, is used. No ROOT live file was read. A late ROOT
message independently stating the degree14 bound arrived after section3
was written and read back; it supplied no new premise or missing calculation.

The old algebra/root-valuation scopes and the new B calculations are kept
separate. All source parameters remain actual r; t=0 or1 in a residue field
is not a rational specialization at an excluded parameter. Every denominator
used in a reduction is either a proved rational source unit or its 7-adic
valuation is displayed. The pole-parameter proof covers all k>=1, including
arbitrarily divisible 3r+1. The factorial cancellation in (8) is a meaningful
negative check against discarding denominator7 terms.

Only inert text/hash/date/apply_patch and the unchanged administrative
finalizer were used. No scientific/code/interpreter/import/AST/test/CAS,
network, worker, new agent, protected-tree, source or ledger action occurred.
Own targets were absent; own WHOLE readback, input postpins and own-only
collision/quantity checks precede the unique final marker. Custody is last.
This is a new manual scalar theorem awaiting independent review, not
promotion, implementation, execution authority, REG, full-source or JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12670`.
- Body SHA-256:
  `0ad8304f611881009397b1081a2506fd499f710da44202bf4dab35648bfa1865`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
