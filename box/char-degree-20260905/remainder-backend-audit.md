# Independent audit of the remainder backend

The emitter `remainder_backend.py` at SHA-256
`c0c6f8716e09baa31f51cde41fab6ba166d9b780040354626fe980fa2adc5b6e`
correctly imposes the full characteristic total-degree and homogeneous-target
block in the audited source coordinates. The proof below also shows exact
row-ideal equivalence for its new remainder equations. This statement is
separate from the earlier front-band preprocessing, whose square-divisibility
steps were explicitly justified as radical consequences.

## Exact polynomial identity and row-ideal equality

Work over Q with physical polynomials H monic of y-degree k, and v,U of
y-degree below k. Set U=8V/3. The depressed characteristic identity is

    Q = -3 U H^3/4 + (3v^2/4+p)H^2 - 9vUH/8
        + v^3 - 9U^2/64 + pv + q.

Set Rraw=v^2-UH, and let R be the sum of its y-coefficients below k.
The backend emits the coefficients of Rraw-R as equations, followed by
those of the required total-degree and target portion of

    Qemit = (3R/4+p)H^2 - vUH/8 + vR - 9U^2/64 + pv + q.

Direct expansion proves the generic identity

    Q-Qemit = (Rraw-R)(3H^2/4+v).

Thus the original and emitted characteristic coefficient rows agree modulo
the high-remainder ideal. Conversely, the high-remainder ideal is already
contained in the ideal of the original upper-degree rows. To see this,
write Rraw=sum r_j y^j, of degree at most 2k-1. All terms of the expression
for Q in terms of Rraw except 3 Rraw H^2/4 have y-degree less than 3k.
For j=2k-1 down to k,

    [y^(j+2k)]Q = 3r_j/4
        + (3/4) sum_(ell>j) r_ell [y^(j+2k-ell)]H^2.

Since H is monic, this recursively recovers every r_j from the high Q
coefficients using the rational pivot 3/4. The required degree D is below
2k, so all these Q heights, at least 3k, are among the upper rows. Taking
all x-coefficients preserves the ideal argument over the coefficient
ring. The whole homogeneous target has degree D and does not change any
of these high rows. Both containment directions are therefore exact
polynomial row-ideal containments, without a nonzero coefficient branch.

## Normalization and implementation checks

The emitter uses normalization degrees k, 2k-1, and 3k-1 for H,v,V.
Consequently U has normalization degree 3k-2 and its normalized polynomial
is (8/3)Vn/t. The actual source floors ensure this shift is polynomial;
the script also checks the exact identity `t*Un-8Vn/3==0` at runtime.
The normalization for Qemit is 6k-2. This accounts for the t multipliers
in the vUH and vR terms and the t^2 multiplier in U^2. The scalar terms
have shifts 4k-2, 4k-1, and 6k-2. The target depths are consequently
141 and 151, exactly the same physical conditions as depths 143 and 153
with normalization 6k.

All high-y coefficients of the full Rraw are retained before any t
truncation. The Q expression is truncated only through its target depth,
which means every coefficient of physical total degree at least D is
retained. The entire leading target is subtracted. The caller's digit
face times H0 is z^40(1+z)^15 for 99, or z^49(1+z)^14 for 108. Leader
and separation localizers remain in the ideal. All five target variables
remain in the ring; the scalar e contributes below the tested positive
degree, so its absence from the high rows is correct.

The caller must supply the audited monic H and outer y-degree caps. It
would be useful defensive programming to assert these caps at runtime,
but they already follow from the retained coefficient maps of these
clients. The ring contains the two structural indeterminates z,t in
addition to coefficient variables; a raw dimension report includes their
two unconstrained dimensions and must be interpreted accordingly.

## Independent controls and scope

`remainder-independent-review.py` constructs fully generic monic H and
generic v,U for toy k=2,3,4 over Q. It verifies the displayed difference
identity and recursively recovers every high-remainder coefficient from
the Q heights. All tests pass in `remainder-independent-review.json`.
This is an algebraic identity control, not a decision on either large
source ideal.

The parent backend controls separately contain a genuine degree-55
composition with leader -1/4 and nonconstant outer v. Its correct target
produces a proper ideal, and replacing that target by 1 produces a unit.
That example has zero Jacobian through a common polynomial generator and
deliberately fails the actual D2 source faces. It is a useful positive
control for the emitter, not a necessary-chart survivor. Localizer
positive and negative controls also pass. These controls justify the row
construction; only a completed full exact-Q computation can decide the
augmented source charts.
