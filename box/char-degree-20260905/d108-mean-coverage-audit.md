# D108 minor-mean coverage: conditional scope of a chart exclusion

Failure of covariance alone does not prove that a chart misses every
normal-form representative of a realized datum. The present audit finds
a more precise issue: the stated normalization argument does not establish
universal coverage of the frozen D108 three-jet, even-face chart.

The charged D108 report, section8, justifies `p=pi^2-c` by a “child
generic-point reparametrisation”. Its section1 explicitly describes the
minor arc and target as transplanted from the earlier frozen engine;
it does not supply a new printed necessity theorem for a zero at-level
mean. The current engine has only `jet0,jet1,jet2`; it evaluates

    y=jet0+jet1*t+jet2*t^2+pi*t^3

and subtracts `-t^8*(pi^2-c)`. There is no coordinate for a mean at order3.

For a general quadratic face `-((pi-mu)^2-c)`, the abstract change
pi_new=pi-mu centers the quadratic. But it simultaneously changes the
physical generic-point arc to

    y=jet0+jet1*t+jet2*t^2+(pi_new+mu)*t^3.

Dropping mu from this arc is not the same reparametrisation. Therefore
centering the polynomial while retaining the engine's original arc needs
an additional necessity or coverage argument.

## Residual diagonal translation and its boundary

Under the existing diagonal translation with parameter q, the strict
coefficients and the at-level mean transform by

    jet0'=jet0-q,  u'=u,  v'=v-q*u,
    mu'=mu-2*q*v+q^2*u.

Over an algebraically closed field, a q with mu'=0 exists whenever
(u,v) is not (0,0): solve a quadratic when u is nonzero, and a linear
equation otherwise. This is a possible generic coverage argument,
provided all source equations and targets are transported. It does not
cover u=v=0, mu nonzero. On that boundary mu is invariant under diagonal
translation. Residual uniform dilation only multiplies it by a nonzero
scalar, so it does not repair the boundary either.

This observation does not exclude a different valid source theorem or
coordinate construction. It means the currently stated reparametrisation
and gauge accounting do not furnish one.

## Exact support-level control

The missing mean is not forced to zero by the h3 source floor or the
compatible major h2 block. Consider scalar mu and nonzero c, and put

    h3=(y-x)*((y*(y-x)^3+mu)^2-c).

It is monic of y-degree and total degree9, with prescribed top
`y^2*(y-x)^7`. Its normalized expression is

    K3=z^7*(1+z)^2 + 2mu*t^4*z^4*(1+z)
       +(mu^2-c)*t^8*z.

Every monomial has actual D2 weight4r+5q at least35 and belongs to the
full degree9 triangle. Along the strict-zero-jet minor arc y=pi*t^3,
its first face is exactly

    -t^8*((pi-mu)^2-c).

All lower bands vanish, while the frozen even target has pi-linear
residual2mu. The actual source `build_major_h2` map accepts this h3
with no h2-D1 residual (nine rational pivots); hence that major block
does not force mu=0 either. The full exact control and engine hash are
`d108-mean-coverage-control.py/.json`.

This control is a polynomial h3 with compatible major data. It is not
a realized Keller pair and is not asserted to satisfy every finite pole
row or the characteristic block. Consequently it establishes a missing
normalization proof, not a counterexample to printed necessity for a
realized pair.

## Consequence for the present report

The printed characteristic-attainment theorem remains valid. The cone
exclusion theorem and the conditional nondegeneracy theorem also remain
valid on their explicitly stated polynomial charts. Algebra-only
translation inside the characteristic computation remains a sound
invertible presentation of the frozen equations.

However, an exact unit for the frozen D108 three-jet even-face chart
would exclude that chart. Promoting it to exclusion of every realized
D108 datum additionally requires coverage of the missing-mean boundary,
or a full chart retaining the mean with transported incidence and pole
targets. The charged report's generic-point phrase alone does not prove
this. No new row, gauge pin, or altered engine is introduced by this
audit. The finite-chart result must therefore keep this coverage
condition explicit until the missing argument is supplied.

## Approved repair: retain the full quadratic face

The coverage issue has a direct polynomial-chart repair: keep the original
strict three-jet arc and retain mu as a new free scalar in
`-((pi-mu)^2-c)`. Any quadratic face with prescribed leader -1 can be
written uniquely in this form: for `-pi^2+L*pi+N`, take
`mu=L/2` and `c=N+L^2/4`. Conversely `L=2mu,N=c-mu^2`.
This is an invertible polynomial parameter change over Q. Distinct roots
are equivalent to c nonzero. The leader -1 at t8*pi^2 is fixed by the
source top's w^2 coefficient: any term of positive t-degree or higher
w-degree reaches the pi^2 coefficient strictly later.

Thus the repair adds -2mu to incidence row(8,1) and +mu^2 to row(8,0),
retaining the existing -c and +1 subtractions. It changes every later
leading F/G target to powers12/8 of `p_mu=(pi-mu)^2-c`. Setting mu=0
recovers the frozen system. The new mu is retained during rational graph
elimination, and no source coordinate is pinned. The source D2 floors,
major faces, front-band proofs and characteristic target are unchanged.

This formulation also matches printed Moh Definition1.3, p146, and the
following paragraph and Proposition1.2, p147: the generic point records
strictly earlier coefficients and pi at the current level; the actual
root coefficients at that level determine the face polynomial. No
zero-mean assertion is supplied there. Retaining the general quadratic
therefore repairs the identified mean omission without a new gauge.
This approval does not supply a computational verdict for the enlarged
chart; it must be run as a separately identified input variant.
