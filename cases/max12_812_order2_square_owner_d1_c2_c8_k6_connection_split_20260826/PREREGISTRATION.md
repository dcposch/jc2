# Preregistration: D1 primary-C2 `c=8` first `k6` connection wall

Date: 2026-08-26

Status: **PREREGISTERED CHAMBERWISE MAXIMAL-POLE PRODUCER; AWS ONLY.**

## Exact scope

Work only on the unit-load generic-square primary-`C2` boundary and its
closed `A,R` tail

```text
D(p*k0), ord(C)=8, ord(A)>=8, ord(R)>=7.
```

This is the first contact excluded from the promoted target-free `3<=c<=7`
theorem.  The terminal grade is 26.  Every target begins later, but
`k6*C/L` starts in grade 25, so its first moving-connection correction must
be retained in grade 26.

## Complete source and chamber split

Independently enumerate all four binomial summands through grade 26 at the
boundary `(A,C,R)=(8,8,7)`, repeat with padded bounds, and derive all jet
maxima mechanically.  The expected primitive families are

```text
grade 25: k6*C/L;
grade 26: A*C/L, C^2/L^2, k0*R*C/L,
          plus the first correction of k6*C/L.
```

The correction must retain `k60_1`, the next `C` jet, and the moving
`p(sigma)=p+2*sigma*ell1+...` term.  In the cleared pole-two numerator its
connection contribution is preregistered as

```text
-(3/4)*ell1*k60*C.
```

No handwritten support list is authority: compile all seven literal rows
and bridge grades 25 and 26 coefficientwise to an independent analytic
source.  Sentinels must show that `k60_1`, both next-`C` coefficients, and
`ell1` actually enter.

Split scheme-theoretically on

```text
D(k60)  union  V(k60).
```

- On `D(k60)`, the complete grade-25 literal equations must contradict both
  exact-`C` charts.
- On `V(k60)`, every grade-26 moving-connection term proportional to `k60`
  vanishes.  The pole-two root pair must reduce exactly to

  ```text
  (3/8)*C(+lambda)^2, (3/8)*C(-lambda)^2,
  lambda^2=-p/2,
  ```

  while the free `k60_1*C/L` term is pole one and vanishes under root
  evaluation.

Use the disjoint exact-`C` cover

```text
D(c1)  union  (V(c1) intersect D(c0))
```

on both load branches.  All four localized ordinary-ring ideals must contain
`1` before radicals.  No leading `A` or `R` coefficient may be inverted.

## Controls and firewall

Omitting the moving-connection term must fail the full grade-26 numerator
identity before the `k60=0` split.  Omitting `C^2` must make both root
terminals zero on the closed-load branch.  Run exact Q and fresh
`F_65519`,`F_65521` controls on distinct AWS hosts, with source hashes,
ordinary polynomial rings, explicit reductions, fail-closed validators,
resource custody, and zero swap.

A PASS may close only `c=8,A>=8,R>=7` on `D(p*k0)`.  It does not extrapolate
to `c>=9`, where more connection/load jets appear, another primary/tied
face, positive-order leading load, `p=0`, `k0=0`, the exact-square zero
section, terminal/global charts, fan exhaustiveness, order two, maximum
twelve, or JC2.
