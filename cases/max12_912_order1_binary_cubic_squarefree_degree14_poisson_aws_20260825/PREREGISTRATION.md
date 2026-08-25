# Preregistration — squarefree degree-14 Poisson gate

Status: frozen before execution. Every exact algebra run is restricted by the
runner to a registered AWS Linux host.

## Immutable pre-result inputs

- The first degree-14 note bytes were observed at
  `2026-08-25T19:16:34Z`, SHA-256
  `e46d3204b1c7048a56b54624ec73b3ca7c1f80ea685d01205496eb8c9e2630be`.
  They printed the dimensionally invalid term `(lambda/3)*V`, with `V=P4`,
  in a degree-seven formula.  Those bytes are a negative-control target.
- The corrected degree-14 note bytes were observed before this run at
  `2026-08-25T19:18:09Z`, SHA-256
  `c0753a6f1b29601e08a71ae7b88682bae568d489f4d4cb7b82acad2760e10eba`.
  They replace the shear term by `(lambda/3)*K*B4=(lambda/3)*P7`.

The later extension of the same note is not an input to this degree-14
checker.

## Exact target

Work over characteristic zero with `K=x*y*(x-y)` and the already displayed
degree-15 reduced family

```text
P9=K^3, P8=K^2*A, P7=K*B, P6=T, P5=U, P4=V,
```

together with its original denominator-free `Q12,...,Q8` formulas.  Put

```text
C=B-A^2/3,
W=T-A*B/3+2*A^3/27,
R=K*Q7-(4/3)K^2*V-(4/9)K*A*U-(lambda/3)K^2*B,
Z=R-(4/9)C*W.
```

Starting from the complete original homogeneous degree-14 determinant row,
the independent checker must prove the polynomial identity

```text
E14 = 3*K*[K,Z].
```

It must also verify, after clearing only the displayed `K` denominator, that

```text
Q7=(4/3)K*V+(4/9)A*U+(4/9)C*W/K+(lambda/3)K*B
```

kills the original row.  It must print the exact numerator factorization

```text
729*R = 324*C*W
```

as the consequence `Z=0`, and it must reject the old `(lambda/3)*V` formula.

The already separately checked fact that the degree-ten homogeneous
centralizer of `K` is zero turns `E14=0` into `Z=0`.  At reduced geometric
points, polynomiality is then `K | C*W`, the union of eight root-allocation
branches for squarefree `K`.  This is a radical/point-scope consequence, not
an equality of nonreduced incidence schemes.

## Refusal

No result proves lower determinant bands, any one allocation branch, a full
Keller map, a p-adic lift, a selected-Q8 landing, maximum twelve, a
counterexample, or JC2.
