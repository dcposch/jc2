# Preregistration — fixed-D12 `(9,12)` order-one binary-cubic bands

Status: preregistered before any CAS execution.  Every substantive run is
AWS-only.

## Exact scope

Work over an algebraically closed characteristic-zero field after licensed
constant source/target changes.  On the strict total-degree `(9,12)` stratum,
normalize the leading forms to

```text
P9=K^3,                    Q12=K^4,
```

where `K` is a nonzero homogeneous binary cubic.  The three disjoint
`PGL2` root-multiplicity types are represented by

```text
triple:      K=y^3;
double:      K=x*y^2;
squarefree:  K=x*y*(x-y).
```

The normalization is characteristic-zero only.  It does not assert an
integral `PGL2(Z_3)` transformation or preserve the B9 residue chart.

Use the original denominator-free homogeneous Jacobian bands:

```text
degree 19: [P9,Q12]=0;
degree 18: [P9,Q11]+[P8,Q12]=0;
degree 17: [P9,Q10]+[P8,Q11]+[P7,Q12]=0,
```

with `[F,G]=F_x*G_y-F_y*G_x`.  No Q8 divided row, Kummer root, Taylor row,
terminal row, or characteristic-three specialization is an input.

## Registered computation

For each cubic type independently:

1. construct `K^3,K^4` from the displayed representative and verify the
   degree-19 bracket is zero;
2. construct the complete degree-18 integer matrix on all 9 coefficients of
   `P8` and all 12 coefficients of `Q11`;
3. compute its exact rational rank and full kernel;
4. construct the complete degree-17 fresh matrix on all 8 coefficients of
   `P7` and all 11 coefficients of `Q10`;
5. project the exact quadratic source `[P8,Q11]` from the full degree-18
   kernel to the complete left cokernel of the fresh matrix;
6. emit the resulting homogeneous quadratic ideal without removing
   nilpotents or components, plus an exact Singular input and all matrices;
7. retain the zero-kernel-parameter solution as a positive source replay and
   a perturbed-top-form nonzero bracket as a negative control.

The first two bands can never by themselves yield a unit ideal because all
lower faces zero is a solution.  The accepted endpoint is exact
rank/kernel/cokernel/obstruction geometry, not an exclusion theorem.

## Finite-SAT composition control

Separately consume the frozen common-cubic witness only at SHA-256
`a39bc9185a21df92173b356c027a00650ced4b92cfc15d587a91b39c8aca299a`.
For its normalized cubic coefficients, prove the exact 3-adic valuation of
the binary-cubic discriminant and whether that valuation is stable under
arbitrary coefficient corrections divisible by `3^11`.  This may select a
root-multiplicity stratum **conditional on an exact continuation**, but it
does not provide one or compose any lower determinant band.

## Acceptance and refusal

Accept only exit-zero results with source hashes, exact matrix/basis replay,
all row/support counts, negative controls, Singular version/output, and a
second AWS execution.  Same-source dual-host agreement is custody, not
independent mathematics.

No endpoint proves survival past `3^11`, an inverse limit, a
characteristic-zero map, an order-three Q8 landing, emptiness of any full
binary-cubic stratum, maximum twelve, a counterexample, or JC2.

