# Exact rational/SNF core of the normalized B9 determinant equation

This package studies the exact integer equation

```text
E(T) = b + A*T + 243*J(T)
```

for the normalized `(P<=9,Q<=12)` coefficient box over one fixed B9
mod-243 parent.  It retains all 276 determinant rows and all 146 coefficient
variables.

Using python-flint 0.9.0 on r6d, the source-pinned `276 x 146` matrix has
exact rational rank 142, right-kernel dimension 4, and left-kernel dimension
134.  Primitive integer bases for both rational kernels are stored in
`AWS_R6D/bases.json` and were checked by exact multiplication.  The augmented
rank is 143, so the purely linear equation `A*T=-b` has no rational solution.

The complete Smith 3-adic profile is recorded in `result.json`.  In
particular, the cumulative counts at valuations below 1,2,3,4,5 are
85,115,127,129,129, matching the ranks in the frozen finite linear window.
The higher exact rank 142 is not in conflict with those finite-precision
ranks.

Projection to a primitive rational left-null basis gives a genuine nonlinear
compatibility system `C^T(b+243*J(T))`: its constant is nonzero, it has 4556
nonzero P-Q terms, and its coefficient span has rational rank 68.  The full
projected polynomial is stored deterministically as
`AWS_R6D/projected.json.gz`.

This is a structural diagnostic, not an emptiness result.  A nonzero
projected polynomial may have zeros, and solving the remaining image
coordinates is still required.  It proves no all-depth point or
nonexistence, maximum-twelve theorem, counterexample, or JC2 result.

Heavy replay is AWS-only.  Stage the transitive source closure and a
python-flint 0.9.0 environment, then run `run_aws.sh` with all five required
paths explicit.
