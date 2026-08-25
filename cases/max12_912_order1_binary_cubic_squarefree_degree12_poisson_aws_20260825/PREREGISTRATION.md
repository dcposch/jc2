# Preregistration — squarefree degree-12 root-allocation gate

Status: frozen before execution; exact algebra is AWS-only.

The degree-12 formulas were frozen before any original-row replay in the
parent note at SHA-256
`ec187c335c7e73e50aec0bed93dc8138e55f6a908bcc5e128aedefc763986112`.
The degree-13 predecessor was preregistered at SHA-256
`ec0eb0a2a004622d742652664f9db96de8ba9999141a85b1c796b8e5a0f1acb9`.
Later edits of the parent note are not inputs here.

On the preceding collapsed family put

```text
C=K*L, W=K*M,
N=M-A*L/3,
R=9*U-A^2*L-3*A*N-3*K*L^2,
Y=P2.
```

The checker substitutes all already displayed polynomial `Q12,...,Q6`
pieces into the complete original degree-12 determinant row and checks,
after clearing only the displayed `K` denominator, the prediction

```text
Q5=(4/3)K*Y+(4/9)A*Z+(4/9)L*V-(4/243)A*L^3
   +(4/81)N*R/K+(lambda/3)U+(2*mu/3)K*A.
```

It also checks the exact pole-numerator factorization

```text
27*N*U-A*K*L^3-3*A^2*L*N-9*K*L^2*N-9*A*N^2
  =3*N*R-A*K*L^3.
```

At reduced geometric points polynomiality is `K|N*R`, yielding eight
root-allocation branches for squarefree `K`.  This is not an equality of
nonreduced ideals.  Predicted obstructed old-base dimension is 23 and fresh
`Y=P2` dimension is 3, hence full dimension 26.

No result proves later bands, a full Keller map, selected-Q8 landing,
maximum twelve, a counterexample, or JC2.
