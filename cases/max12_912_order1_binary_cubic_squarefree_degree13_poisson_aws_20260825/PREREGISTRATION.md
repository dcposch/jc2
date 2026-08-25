# Preregistration — squarefree degree-13 Poisson collapse gate

Status: frozen before execution; exact algebra is AWS-only.

The degree-13 formulas were frozen before any original-row replay in the
parent note at SHA-256
`ec0eb0a2a004622d742652664f9db96de8ba9999141a85b1c796b8e5a0f1acb9`.
The earlier corrected degree-14 parent was SHA-256
`c0753a6f1b29601e08a71ae7b88682bae568d489f4d4cb7b82acad2760e10eba`.
Later degree-12 edits of that note are not inputs here.

Put `C=B-A^2/3` and `W=T-A*B/3+2*A^3/27`.  Starting from the complete
original denominator-free degree-13 determinant row, this checker tests the
predicted rational expression

```text
Q6=(4/3)K*Z+(4/9)A*V+(4/9)C*U/K
   +(2/81)(9W^2-6ACW-2C^3)/K^2
   +(lambda/3)T+mu*K^2
```

by exact denominator clearing.  It separately substitutes `C=K*L` and
`W=K*M` and verifies the resulting polynomial formula directly in the same
original row.

Given the preceding reduced-point condition `K|C*W`, polynomiality forces
the rootwise condition

```text
K | 9W^2-6ACW-2C^3,
```

and hence, for squarefree `K`, both `K|C` and `K|W`.  This last implication
is a reduced geometric-point/UFD argument, not a scheme-ideal equality.
The predicted collapsed old-base dimension is 21 and the fresh
`(Z,mu)` dimension is 5, for full dimension 26.

No result proves a lower band, a full Keller map, selected-Q8 landing,
maximum twelve, a counterexample, or JC2.
