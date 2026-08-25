# Selected-Q8 sparse bidegree bounds

This AWS-only exact Normaliz replay computes separate origin-augmented affine
BKK bounds for the two degrees of the localized projection cycle in
`P1_w x P1_v`.

With curve class `(A,B)`, a vertical target fibre `w=alpha` has class `(1,0)`
and counts `B`; a horizontal target fibre `v=beta` has class `(0,1)` and
counts `A`.  The latter is pulled back without division as
`x3-(beta+2)*x5=0`.

For the candidate `H` of class `(21,190)`, a residual class `(a,b)` has
intersection bound `190*a+21*b`.  The computation supplies only the numerical
coordinate bounds; the cycle, localization, generic-isolated-root, and
component-subtraction arguments are stated separately in the proof report.
