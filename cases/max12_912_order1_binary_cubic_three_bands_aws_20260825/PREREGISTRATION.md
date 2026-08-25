# Preregistration — degree-16 lift of the binary-cubic root strata

Status: frozen before execution.  All substantive computation is AWS-only.

## Parent and exact scope

Consume the frozen first-two-band package
`cases/max12_912_order1_binary_cubic_bands_aws_20260825/` at its exact
characteristic-zero, fixed-total-D12, order-one scope.  For each representative
`K=y^3`, `K=xy^2`, and `K=xy(x-y)`, retain

```text
P9=K^3, Q12=K^4.
```

Compile the next original denominator-free homogeneous row

```text
[P9,Q9]+[P8,Q10]+[P7,Q11]+[P6,Q12]=0                  (degree 16)
```

together with the already registered degree-18 and degree-17 rows.  No
division by `K`, orbit denominator, Kummer root, Q8 divided row, Taylor row, or
terminal row is licensed.

## Scheme-theoretic parameterization

1. Parameterize the complete kernel of the degree-18 map by `s`.
2. RREF the complete degree-17 fresh map with an explicit invertible row
   transformation.  Express every pivot coefficient of `(P7,Q10)` in the
   free variables `t` and the quadratic source in `s`.
3. Retain every transformed zero-row equation as the full degree-17
   obstruction ideal.  Check its row span equals the independently computed
   left-cokernel projection from the parent compiler.
4. Construct all 17 coefficients of the degree-16 source, using independent
   bracket implementations, and project them to the complete left cokernel of
   the fresh `(P6,Q9)` map.
5. Emit the combined degree-17/degree-16 ideal in `Q[s,t]` without radical,
   saturation, component choice, or nilpotent removal.  Run exact Singular
   `std` on r6d and exact `slimgb` on Box02.

The all-zero lower faces are a mandatory positive control.  A nonunit ideal is
expected and does not establish a full Keller branch.  An exact unit would
exclude the represented root stratum only through degree 16, not globally.

## Executable placement gate

The runner must refuse Darwin and every non-Linux system, require the exact
registered AWS runtime hostname, require an exact `JC2_AWS_TAG` environment
value, require `Amazon EC2` platform identity, and verify the pinned source
manifest before invoking Python or Singular.

## Refusal

No endpoint proves compatibility below degree 16, total support/Taylor
reconstruction, an all-depth B9 lift, preservation of the mod-3 residue chart
under PGL2, selected-Q8 landing, maximum twelve, a counterexample, or JC2.

