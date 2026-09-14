# Independent review of the direct printed-source engine

Scope: `engine.py`, `source_data.py`, `minor_maps.py`, and the frozen Moh
text. This is an implementation/coverage audit, not a branch verdict.
Executable controls are `minor_source-engine-checks.py` and the resulting
JSON; rational source-point checks are `minor_source-controls.py` and its
per-branch JSON. The reviewed engine hash is recorded by each control.

## Source coefficients are represented before valuation elimination

`coefficient_box` creates the full finite total-degree triangle and then
forms each strictly-below scalar row with coefficient1. Its zero map is
therefore an explicit solved system, not a declaration that unknowns never
existed. Equality coordinates remain present. At D2 the generic variable
has independent powers pi^q, so two different q values at the same total
weight cannot cancel; vanishing below the floor is exactly coefficientwise.
This is the setting in which these scalar eliminations are legitimate.

For h3, the lower degree11 triangle has66 raw coefficients,43 below the
derived weight32,2 equal,21 above. The first equality coordinate is solved
by the coefficient comparison derived in source_data; the second appears
as E82 and is eligible for further genuine equations. The original21-symbol
strict basis is unit triangular separately in every fixed-t row. Keeping
it plus the two raw equality monomials is a change of coordinates on the
full floor solution space; it does not remove a hidden support direction.
Hc_11_0 retains its literal constant meaning and is not pinned.

The exact normalized polynomial identity in `inner_state` is
K2=K3^3+U*K3+V with U=t^22*C2,V=t^33*C3. The raw C2/C3 boxes, floors,
and face equations are derived in `minor_source-bridge.md`. Their box
counts are187 and308;154 and271 scalar rows leave33 and37 coordinates.
At the K2 face, seven residual coefficient equations remain after the forced
h3 pi^5 coefficient. The h2 D1 rows impose all terms with normalized
order below296. Since each monomial has base order3W and the next generic
increment is1, only W97,k0..4 and W98,k0..1 occur beyond the fixed face.
The weight96 fixed face already vanishes through295. `inner_state` emits
its coefficient rows directly, including zeros that result from the face
identity, so there is no guessed pure D1 face.

The weight truncation in `mul_weight` is safe for these particular incidence
rows: all participating r and q are nonnegative and both weight coefficients
are positive. Omitted monomials above the largest contributing weight cannot
multiply with another retained monomial to return to that weight or below.
For the actual F/G stage construction, `build_major_h2` reconstructs the
full polynomial through the requested t-power directly from the resolved
h3,C2,C3 blocks, rather than reusing the weight-truncated incidence product.

All inner incidence eliminations use the provided QQ* pivot reducer. Its
eligible set excludes the branch localizer. It may solve any other coefficient
only when the derivative of its equation with respect to that coefficient
is a nonzero rational constant. No inference in the review relies on a
parameter being nonzero beyond the explicit rho/c localization. If a
nonlinear residue remains, `additional_rows` carries it into the stage ideal.
The h3 minor map is composed with the inner map, so earlier equations remain
valid under that composition. The stage dimension must include this residue,
as the code does, instead of declaring a free coordinate list from pivot count.

## Outer floors and degrees

The canonical h2 expansion of F has no h2^2 term by the approximate-root
definition (Moh p148, extracted lines463-468). G is expanded by ordinary
monic division. The y-degrees of each outer remainder are below33. The fixed
top identities F_top=h2_top^3 and G_top=h2_top^2 force the respective total
degree bounds65,98,32,65. As with the C2 bound, a top coefficient multiplying
h2 cannot cancel against the lower-y-degree remainder. These are consequences
of the full polynomial identity, not optional degree caps.

The two coherent systems transfer h2's orders -1 at D2 and -1/9 at D1.
Moh p149 Thm1.2, lines495-507, yields j times those orders for the j-th
outer block. Applied also to G, h2 is its square quasi-approximate root
on those systems: the distribution relations transfer its relative root
counts and accuracy. With normalized K_Q=t^D*Q the floors are cover*(D+order).
Thus the derived tuples `(D,D2floor,D1floor)` are

    A2=(65,189,583), A3=(98,285,879),
    B1=(32,93,287),  B2=(65,189,583).

`outer_state` starts each full triangle at r=0, unlike the inner remainder
normalization whose t-degree is one larger than the actual coefficient
bound and therefore starts at r=1. `outer_effective_tz` supplies exactly one
additional t to put each block into F or G's full normalization. This
one-step distinction is handled consistently by the code.

For every offset, the D1 loop solves precisely `3W+k<threshold`, generated
by the actual substitution t=e^9,z=e^12(1+Pi*e). No at-threshold coefficient
is zeroed. The last nonempty possible offset is7, computed from the largest
threshold gap. The full outer image is checked against the historical engine
only as an arithmetic control after deriving its exponents independently.

## Full minor support tags, with all centres

A direct support rule avoids relying on the inherited hard-coded shifts.
For degree D, let d be the cover denominator, g=d*(1+delta) the generic
w exponent, and L the derived normalized F/G face power. At each n in1..L,
the complete lower-coefficient tag set is exactly

    k>=0, n>=d+g*k, n-g*k divisible by d.

Necessity follows from the source monomial t^r*w^j with r>=1: k generic
picks contribute g*k, every other pick has nonnegative order divisible by d,
and the initial t^r contributes at least d. All lower and at-level centre
terms are included in this argument. Sufficiency has an explicit source
monomial witness: put r=(n-g*k)/d and take x^(D-r-k)*y^k. Its total degree
is D-r<D, its x exponent is nonnegative throughout n<=L, and its pure generic
pick gives exactly the requested tag. The audit checks every one of these
witnesses, not only the row count.

For delta2 the rule gives k<=floor((n-1)/3). For delta5/2 it gives
n>=2+7k with n congruent to k modulo2. All four sets exactly equal the old
support/counts1134,513,1316,594. The engine should use this derived emitter
(or record this complete equality certificate if retaining its old emitter).
This establishes inclusion of all lower monomial contributions with jet0,
u,minor_a2 or v, rather than assuming an unchanged centre leaves support
unchanged.

The fixed top contributes the monic highest face term at(n,k)=(L,3D/11),
which lies outside the lower-coefficient tag set. That term is automatically
correct: lower coefficients cannot reach it. All other fixed-top contributions
at or below L have at least one nongeneric pick and therefore fall in the
above tags. The full endpoint must subtract the derived P^(D/11) coefficients
on those tags; it cannot continue the strict-below zero rule through equality.
The current finite historical schedule lies strictly below those endpoints.
The refined complete-system proof giving the endpoint faces is in
`minor_source-bridge.md`; transferring only whole-disc multiplicities would
not be sufficient.

## Gauge and survivor interpretation

The two source translations survive direction placement. The major constant
uses one translation combination; jet0 remains free and leaves the diagonal
combination unspent. The at-level delta2 location minor_a2 is carried as an
independent coordinate in every expansion. On u=0 it cannot be changed by
the remaining diagonal translation, so deleting it by dividing by u would
lose a source slice. Hc_11_0 is invariant under that translation because
h3(x,x)=Hc_11_0, and is free on both branches. Uniform dilation pays only
for beta=1, and neither rho nor c is normalized inside the chart.

A zero-outer rational point has F=h2^3,G=h2^2 and therefore J identically0.
It is a valid control for positive-degree Jacobian rows. It is not a point
of a chart that additionally localizes the constant Jacobian, and it is not
a Keller pair. If it survives all chosen rows, the result must explicitly
say which constant-J condition is absent. Conversely its failure is only
failure of that point, and cannot substitute for an ideal being a unit.
The rational source-point controls in this audit set the final remaining
source coordinates to0 except jet0 and the branch localizer set to1, after
all source incidence pivots have been applied. Those are new points of the
source chart; they are not claimed to be the same coordinate assignments
as the frozen gate's unconstrained K2-output points.

## Completed exact controls and the first new point failures

`minor_source-engine-checks.json` is PASS. It checks every h3 triangular
basis determinant, all four complete lower-pole tag sets against explicit
source monomial witnesses, both full-centre emitters against an independent
native Sympy expansion, and the exact image of every outer coefficient
after all eight D1 offsets. The outer pivot ranks are41,38,33,25,19,11,6,3,
with826 remaining outer coordinates. This is image equality, not matching
names or matching dimensions.

For reproducibility during concurrent engine development,
`minor_source_engine_snapshot.py` and `minor_source_data_snapshot.py` are
immutable copies used by these final independent controls. The snapshot
changes only the source_data import to its matching snapshot name. Each
result hashes the actual snapshot file. An earlier Hc_8_3-free-coordinate
point record is explicitly labelled with an observational finish-time hash;
it is not used as custody for the snapshot run.

The snapshot uses the invertible rational exchange that retains E82 as a
free coordinate and eliminates Hc_8_3. At the new rational point with
jet0=branch-localizer=1 and every other remaining inner coordinate0, both
branches satisfy every source incidence row, the full K2 D2 face, and all
K2 D1 rows below296. Their remaining inner dimensions are64 and62.
Taking all outer free coordinates0 gives F=h2^3,G=h2^2, so every Jacobian
coefficient is0. Independent Fraction-arithmetic local composition gives:

| Branch | first K2 local order | first failed G pole power | first failed F pole power |
|---|---:|---:|---:|
| delta2 |17|34|51|
| delta5/2 on s |37|74|111|

At those first powers the G coefficient polynomial is `(400/9)*P^2` and
the F coefficient polynomial is `(8000/27)*P^3`, evaluated at rho=1 or c=1.
They are nonzero. These new points therefore satisfy every finite scheduled
row through stage8 and fail deeper pole rows. The exact assignments and
all three numeric inner coefficient blocks are serialized in
`minor_source-point-snapshot-delta2.json` and its delta52 counterpart.
No zero locus is restricted to those points for an ideal computation.

The extra deep minor remainder rows can detect these particular points
still earlier. Thm1.2 on the refined coherent minor system gives normalized
C2 floors18/42 and C3 floors27/63. The first C2 local coefficient, at local
power8 for delta2 or16 on the double cover, is `20/3-3*E82`. Its required
vanishing solves E82=20/9 by rational leader-3. This is a legitimate later
coefficient equation. It does not justify having pinned E82 before that
row was imposed, and it does not imply a branch is dead.
