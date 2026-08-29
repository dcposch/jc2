# Result: correction-complete `A` repeated-root coefficient at `t^7`

Date: 2026-08-26

Status: **DUAL-AWS EXACT CANCELLATION CERTIFICATE.  THE MONOMIAL-SLICE
`t^7` OBSTRUCTION DOES NOT EXCLUDE THE SOURCE BRANCH.**

The exact-Q producer and characteristic-65521 software control both report
`PASS_A_SOURCE_EARLY_NULL`.  V1 is deployment-negative and preserved
separately; every statement below is from V2.

On the repeated-root boundary put

```text
Q0=z^2*(z^2+p),
N3=v*z*(z^2+p),
Q=Q0+t*(pp*z^2+x*z+rr)+...,
N=t^3*N3+t^4*(w3*z^3+w2*z^2+w1*z+w0)+....
```

All seven unloaded ordinary-Faber rows vanish through `t^6`.  At `t^7`
the exact complete frozen rows are

```text
R1=(-3/8)*v^2*x+(3/4)*w0*v,
R2=(-3/8)*rr*v^2,
R3=(p/4)*R1,
R4=(p/2)*R2,
R5=(p^2/32)*R1,
R6=(p^2/8)*R2,
R7=-(p^3/128)*R1.
```

Consequently

```text
w0=v*x/2,                    rr=0
```

cancels the complete seven-row coefficient.  The moving-`p` coefficient
`pp` and `w1,w2,w3` do not enter at this grade.  Thus the slice value
`R1=-(3/8)v^2*x` obtained by setting the next normal to zero is only a
regression sentinel, not a source obstruction.

The same replay independently checks the exact normalized repeated-root
cubic identities

```text
512*(B3+(p/4)*B1)=5*p^2*(x^3+5*p^2*v),
1024*(B5-(p/4)*B3+(p^2/32)*B1)=5*x^3*p^3.
```

Those identities remain correct, but they cannot be used before every
intermediate unloaded source coefficient has been recursively cleared.
Under the primitive ramification `Lambda=sigma^3,t=sigma^5`, `t^8` is
still at `sigma^40`, before the delayed loaded face at `sigma^42`.

As a separate squarefree positive control, the normalized rational witness
at `p=0,D=1,x=1,v=-1/20` has the exact predecessor rows

```text
[t^6]R2=3/3200,             [t^6]R6=3/6400.
```

This rejects that particular witness, consistently with the reviewed
squarefree first-normal theorem.  V2 does not classify the correction
recursion through `t^8`, establish a total-Rees chart, or impose terminal
or Taylor conditions.  It proves no order-two or JC2 verdict.
