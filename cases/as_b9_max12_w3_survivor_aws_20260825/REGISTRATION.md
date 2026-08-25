# Registration — AS `B9` maximum-twelve `Z/27` survivor

- Registered UTC: `2026-08-25T16:04:03Z`.
- Repository basis: `d0f6edfbfcd8fbe4c77ffadcd336df349c11eb7e` plus the
  then-current dirty worktree; this case consumes no uncommitted producer.
- Execution policy: exact replay on AWS only.  Local work is source editing,
  hashing, transfer, and log inspection.

Over `F_3`, put

```text
u=x+y^3,
B9=(u,y+u^4),
G9=(u-u^3,y+u^4).
```

The registered exact integer representative modulo `27` is

```text
P=u-u^3+18*u*y,
Q=y+u^4+3*u^2*y+18*y^2.
```

The replay must independently expand every coefficient in `Z[x,y]`, verify

```text
det J(P,Q)
  = 1-81*u^4+54*y-162*u^2*y+648*y^2
  = 1 (mod 27),
```

verify reduction to `G9`, actual partial `y`-degrees `(9,12)`, the explicit
special-fibre collision `(0,0)!=(2,2)`, and the intermediate `Z/9` identity.
It must retain the mixed binomial terms in `(x+y^3)^3`; treating Frobenius as
an integer identity is a hard failure.  Omitting either new `18`-coefficient
term must fail the determinant gate.

The evidence target is only one explicit fixed-support determinant-one map
over `Z/27`.  It is not a compatible tower, a `Z_3` or characteristic-zero
map, a polynomial counterexample, a maximum-twelve theorem, a TD6 object, or
a result about every lift of `G9`.
