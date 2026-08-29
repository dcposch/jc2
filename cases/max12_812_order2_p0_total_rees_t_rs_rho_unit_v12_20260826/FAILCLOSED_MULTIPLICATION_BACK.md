# V12 fail-closed result

Date: 2026-08-26

Both registered lanes stopped at `FAIL_MULTIPLICATION_BACK` before any
saturation, membership, or rho-unit claim.  The engine wrapper returned zero
because Singular `quit` is not an error exit, but the validator rejected the
forbidden `FAIL_` token and emitted no `RESULT.json`.

The defect is mathematical bookkeeping in the preregistered certificate,
not source data: total `Tg10_3` has chart `rs`-valuation one because its
`rho^2*a*c` terms contain only one factor of `rs`; only the frozen
specialization has valuation two.  Thus the correct definition is

```text
P3=Tg10_3/rs
```

and the divided cusp multiplier is `8192*qcs*P3`, not
`8192*rs*qcs*P3`.  V12 is no verdict.  The source-frozen successor V13 makes
only these repairs and must rerun both characteristics and both independent
saturation encodings represented by the two lanes.
