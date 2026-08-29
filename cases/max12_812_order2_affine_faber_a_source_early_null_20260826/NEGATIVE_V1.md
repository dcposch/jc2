# V1 deployment-negative record

Both V1 lanes reached the intended repeated-root unloaded emissions, but
the generated Singular line for the second cubic identity used an
unparenthesized exponent/divisor expression.  Singular parsed it as a
nonintegral exponent, emitted diagnostics, left `Id5` undefined, and the
wrapper correctly returned `validator=FAIL_DIAGNOSTIC`.

V1 is not mathematical evidence.  Its stdout motivated V2's
correction-complete `t^7` test: the monomial slice has
`[t^7]R1=-(3/8)v^2*x`, but a general next normal coefficient can enter at
the same order.  V2 therefore retains all four coefficients of `N4` and
the moving `p,r` tangent instead of promoting the slice obstruction.
