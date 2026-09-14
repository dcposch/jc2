Final small-matrix scope audit
=============================

The proved bound of at most22 unknown coefficients belongs to the transported
major-face ODE. It is not currently a bound on the number of variables of the
full necessary chart, nor a matrix representation of its nilpotence decision.
This is a scope limitation of the proved reductions, not a theorem that no
further reduction can exist.

For99 the ODE solves for the17 coefficients of q of degree at most16; for108
it solves for22 coefficients of degree at most21. The unreduced coefficient
arrays have19x17 and25x22 shapes, respectively; dependent/identically zero
rows can be removed. The equation is linear because C is a scalar parameter.
Solving it determines the face as a linear function of C, and identifies
e with a fixed nonzero rational multiple of lambda. It does not determine
the remaining polynomial coefficients. In the full quotient the relation
e=kappa*lambda identifies D(separation*e) with D(separation*lambda), but
does not change the other generators of the decision ideal or show that
either localization is empty.

The normalized delta5/2 source presentation has65 G coefficients and three
centre/separation variables:68 occurring base variables. The R constant q
is an independent free factor, giving69 before localization. Factoring q
out and adjoining one Rabinowitsch variable gives69 occurring decision
variables. All74,041 retained rows in the composed source presentation
remain equations. Neither their number nor the sizes of their current-band
linear pivot matrices is a dimension calculation.

The completion-of-square/depressed-cubic target isomorphism has already
factored exactly three affine parameters. There is no second subtraction
for G's constant: its translation is one of those three actions. Recentring
the diagonal parameter u=x+h is a coordinate substitution with h carried,
not another available gauge after the jet0 slice has spent the diagonal
source translation. B being a unit on the lambda-unit locus licenses its
inverse, not B=1. The uniform scale was already spent on the major beta=1
normalization. No extra normalization of separation, lambda, or B has been
proved here.

The repaired supported-H quotient proof is accepted
-------------------------------------------------

The new h-quotient-proof.md and its checked supported Hermite lifts repair
the previously missing centre issue. They prove, over the lambda-localized
coefficient algebra and with all centres retained,

    lambda*G=H*R+S,
    deg H<=11/9, deg S<55/63,

with the required H difference valuations. They also prove the complete H
faces and the3/1/1 remaining H coefficients for delta2/delta5/2/108. The
H valuation bound is therefore NOT an outstanding gap in this lane.

The division theorem supplies a two-way coefficient map when H, R AND S
are retained. The inverse reconstructs G=lambda^(-1)*(H*R+S), and every
original characteristic, Jacobian, tower, and nodal row must be pulled back
through that formula. It is not an inverse map from H alone. For example,
the delta5/2 G/R boundary space before the characteristic relation has
65+44 coefficient coordinates over the retained scalar ring. A one-parameter
H projection does not justify deleting its R and S data or their constraints.

The scalar difference H-h3 on the completed delta5/2 and108 source charts
is likewise a proved coordinate relation, not a license to identify those
polynomials or normalize their difference. The canonical-root map and all
remainder equations still belong to the full chart.

The retained S data give a concrete obstruction to the naive last step.
Its major constant face coefficient is lambda, while its minor valuation
is strictly better than G's. The monomial lambda*x^2 has exactly that major
constant coefficient and satisfies the improved minor floor and the strict
total-degree bound. This is a non-obstruction control for that coefficient;
it is not asserted to satisfy the entire S face or the full source ideal.
The separately checked H/reverse-remainder face control also establishes
only those named face conditions, not properness of the full chart.

What a <=22-variable or <=22-matrix full decision would still require
------------------------------------------------------------------

One needs either an explicit elimination of all remaining R/S/canonical
coordinates with both ring maps and every compatibility equation retained,
or a proved finite faithful module presentation in which a small matrix
actually represents multiplication by separation*lambda. Neither structure
has been established by the face ODE or the H division theorem. The ODE's
linear operator on q coefficients is not multiplication by that element
in the full source coordinate algebra.

Consequently, a proper small H or face chart supplies no full-chart
survivor: its nonempty fibres have not been proved. A full localized unit
would exclude every actual input mapping into the necessary chart, whereas
a proper full localized ideal would give an existential necessary-chart
point. Those opposite conclusions require the full ideal or an equivalent
proved reduction, not the small projection alone.

CPU accounting: there was one evaluated full DAG run (760.15 wall seconds,
used as a CPU upper bound), one canonical addon (385.215 CPU seconds), one
all-client boundary-map run (21.794 seconds), one initial G-map control
(1.235 seconds), and subsecond rank runs. No failed or restarted heavy run
occurred.1250 CPU seconds is a conservative bound for this agent's complete
work, including all small checks and this analytic audit.
