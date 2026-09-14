# Independent D1 face coverage, compression, and rational-point audit

This audit makes no engine edit and imposes no coordinate specialization. The
source is the frozen Moh PDF as extracted in `moh-layout.txt`; M below denotes
physical extracted lines. The executed source-face control and exact compression
control are `print-audit-d1-source-faces.py/.json` and
`print-audit-d1-compression.py/.json`. Each JSON records code custody.

## 1. Printed source and the exact differential

Def5.1(3), printed p179, M:2131–2138, gives the physical y radii 1/3 and
4/9. Def5.1(4), M:2137–2140, invokes all hypotheses of Prop4.6 at each
major disc. Prop4.6's r=1 conclusion, printed p170, M:1646–1648, is a
nonzero differential scalar for the two actual child faces. The actual
coordinate computation is independent of any prime-mark interpretation:

- x=e^-9;
- y=e^-9+e^3+Pi*e^4;
- F=e^-3 P(Pi)+higher e orders;
- G=e^-2 Q(Pi)+higher e orders.

The coordinate determinant is -9e^-6, and the chain rule gives

    J_(e^0) = (3 P Q' - 2 P' Q)/9.

The exponent of this expression is zero because -3-2+9-4=0. These are
physical orders. In the notation of `d1_jacobian_face.py`, `F_exp=-3` and
`G_exp=-2` are therefore correct. A scalar shift between G and Moh's
specialized first characteristic polynomial cannot change these negative-order
faces. `Jc` remains a free nonzero scalar with its explicit inverse. Dividing
by a fixed rational leading coefficient below is an invertible change of
coefficient coordinates, not another source dilation.

## 2. Every D1 face support is an output of the source equations

For a normalized monomial t^r z^q, substitute
`t=e^9,z=e^12(1+Pi*e)`. The coefficient of Pi^k has exponent
9r+12q+k. In particular, its exponent is congruent to k modulo3.
For physical h2,A2,A3,B1,B2 the face orders are -1,-2,-3,-1,-2 in e.
Their Pi exponents consequently belong to residue classes 2,1,0,2,1.

The K2 D2 equality face `(pi^3-1)^8` has weight96. At D1 exponent296,
its contribution is the k=8 coefficient, namely 3^8 Pi^8. Weight97
can contribute only k=5, and weight98 only k=2. Higher weights cannot
contribute because their e exponents are at least297. Thus the source
identity and the seven emitted K2 D1 rows give

    H(Pi) = Pi^2 h(Pi^3), deg h=2, leading coefficient h=3^8.

This is a consequence, not a typed pure face: both lower h coefficients
remain represented.

For each outer block, the initial D2 equality layer has q divisible by3.
Its largest possible q is30,30,21,30 for A2,A3,B1,B2 respectively. The
D1 offset0 equations require vanishing of orders16,24,8,16 at pi=1.
Because these polynomials lie in Q[pi^3], the same multiplicities occur
at all three conjugate roots of pi^3-1. A nonzero polynomial would then
have degree at least48,72,24,48, contradicting the actual degree bounds.
Hence all four outer D2 equality faces are zero by the emitted equations.
This licenses the later F/G D2 faces K2_face^3 and K2_face^2 without an
extra pin.

The remaining D1 offsets impose the same Hermite conditions at each
successive D2 weight. Computing the complete generic outer_state(7)
with every ambient coordinate present gives exactly:

| face | surviving Pi exponents | compressed form |
|---|---|---|
| H | 2,5,8 | Pi^2 h(X), deg h=2 |
| A2 | 1,4,7,10 | Pi a(X), deg a<=3 |
| A3 | 0,3,6,9 | b(X), deg b<=3 |
| B1 | 2,5 | Pi^2 c(X), deg c<=1 |
| B2 | 1,4,7,10 | Pi d(X), deg d<=3 |

Here X=Pi^3. The executable source-face control reconstructs the generic
24 inner source rows, verifies all14 rational pivots, extracts the faces,
and asserts these supports. It also checks all four outer D2 faces are
identically zero after the D1 rows. It finishes in about8 seconds.

The original P,Q therefore satisfy

    P=p(X)=X^2 h(X)^3+X a(X)h(X)+b(X),
    Q=Pi q(X), q(X)=X h(X)^2+X c(X)h(X)+d(X).

Their degrees are24 and16 in Pi, with leading coefficients3^24 and3^16.
The outer contributions have smaller degrees, so neither leader is a
new condition or normalization. The generic compression control keeps
all17 face coefficients free, including h's leader; the coefficient
identity below is valid even before the source leader is substituted.

## 3. Thirteen scalar equations, with the power cancellation done first

For P=p(Pi^3) and Q=Pi q(Pi^3), direct differentiation yields

    3 J_(e^0) = L(p,q),
    L(p,q) = p q + 3X p q' - 2X p' q.

Writing p=sum p_i X^i and q=sum q_j X^j gives the exact coefficient
formula

    [X^k] L(p,q) = sum_(i+j=k) (1+3j-2i) p_i q_j.

The nominal degree13 term vanishes because 1+3*5-2*8=0. Thus only
k=0..12 can occur, at Pi powers0,3,...,36. The constant row is
`b0*d0/3-Jc`, so both b0 and d0 must be nonzero when Jc is nonzero.
No extra localization of those coordinates is used in the helper.

Expanding full P,Q before differentiating introduces a large polynomial
which subsequently cancels. The helper instead writes

    p0=X^2 h^3, q0=X h^2, u=X a h+b, v=X c h+d.

Since L(p0,q0)=0 identically, it computes

    L(p,q)=L(p0,v)+L(u,q0)+L(u,v)

by short coefficient convolutions. This removes the identical pure-power
terms before mapping the surviving source coordinates. It does not set
u or v to zero. The independent control compares the result with direct
Pi differentiation with all17 generic coefficients free and verifies
an exact zero difference. The13 expanded rows have term counts
2,5,14,18,39,46,45,37,15,16,8,4,1. At all-zero outer faces they reduce
to the negative control -Jc, as required.

## 4. Coverage conclusions and its precise limit

The current strong driver computes the five faces from the maintained
source polynomials and uses their actual differential. The cutoff98
for K2 is safe because every omitted monomial has exponent>=297.
The four outer face thresholds are the unshifted normalized thresholds
583,879,287,583; subtracting physical normalization degrees gives the
orders used above. The extra t in F/G assembly is already accounted for
by those physical degrees. No factor of9 or extra cover shift is missing.

The minor block's C2/C3 floors and h2 target, followed by all four outer
floors and F/G targets, imply every full F/G pole row by exact polynomial
multiplication. The face-transfer licence is the refined complete-system
argument in `print-audit-derivations.md`: generic multiplicity alone would
be insufficient, while transfer of all child residue positions and
monicity is sufficient. The canonical total-degree bounds21/32 for C2/C3,
under normalizations22/33, explain why their r=0 coordinates are absent.
That absence is not inferred from a valuation floor.

Every face actually imposed by these drivers is consequently derived.
The chart remains a necessary chart for the specified branch; it does not
encode every separate characteristic-attainment or distinct-root statement
in Prop4.6 as an explicit coordinate relation. For a unit proof, the needed
claim is that every actual branch maps into this chart, which the source
and gauge audits supply. Such omitted additional conditions can weaken a
chart; they cannot make a unit on it falsely exclude an actual branch.

All positive-degree Jacobian rows plus the constant equation J=Jc and
ZJ*Jc-1 impose the full Keller equation for the represented F,G. A point
satisfying only the support and positive-Jacobian equations, with Jc=0,
is not a point of the strong chart. The existing pure-power certificates
are correctly scoped to that weaker necessary support chart. They fail
the required D1 scalar before any further zero-Jacobian band can help.

## 5. The universal D1 enlargement has no rational points

The parent driver's `universal_D1_control.py` allows every lower
coefficient of monic p of degree8 and monic q of degree5. It obtains
these monic polynomials by dividing the known rational leaders3^24 and
3^16. Its scalar is `Jnorm=3*Jc/3^40`, an invertible rational scaling.
This is an enlargement, not a specialization of the source-chart faces.

`print-audit-universal-d1-verify.py` independently regenerated all13
coefficient equations and all eight descending rational pivots, with
leaders2,4,6,8,10,12,14,16. It checked both ideal inclusions between the
remaining six original equations and the stored22-polynomial Singular
basis in the declared Q ring `(q0,q1,q2,q3,q4,Jnorm,ZJnorm)`, dp.
It also checked both inclusions with the derived three-coordinate graph,
one quartic relation, the actual scalar equation, and the inverse equation.
The dimension is1. Reduction of1 gives a nonzero remainder, the negative
unit control. There is no characteristic or finite-field inference here.

The graph is

    q2=69*q3*q4/98-39*q4^3/196,
    q1=-189*q3^2/1508+1449*q3*q4^2/6032-63*q4^4/928,
    q0=-222237*q3^2*q4/8128120
       +1877391*q3*q4^3/65024960-1431*q4^5/204160.

The remaining relation is

    153664*q3^2-117584*q3*q4^2+22789*q4^4=0.

If q4=0 then the graph gives q0=0, and the scalar equation is -Jnorm=0,
contradicting its inverse. Thus q4 is nonzero on this localized locus.
For R=q3/q4^2 the relation has discriminant -181398528. It has no real
root, hence no rational root. There are therefore no real or rational
points in this universal D1 enlargement and consequently none in the
strong source-chart locus mapping to it. The enlargement is nevertheless
nonempty over the algebraic closure, of dimension1. This is **not a unit
and not a complex branch kill**. It justifies dimension-only point
tracking after the nonzero D1 face arrives.
