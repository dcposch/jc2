# Max12 `(9,12)` corrected-Q8 order-128 invariant support

This case preserves the exact AWS output from eight good reductions of the
selected corrected-Q8 branch.  The pinned worker Hensel-lifts to order 128
and tests 229 rectangular monomial supports for each of four invariant pairs.
All 7,328 fit matrices have full column rank.

The local audit is intentionally lightweight and does not rerun the Hensel
lifts or matrix reductions:

```sh
python3 cases/max12_912_order3_nu_q8_order128_invariant_support_20260824/audit.py \
  | diff -u cases/max12_912_order3_nu_q8_order128_invariant_support_20260824/audit.json -
shasum -a 256 -c \
  cases/max12_912_order3_nu_q8_order128_invariant_support_20260824/MANIFEST.sha256
```

An exact recomputation uses the pinned worker and runner in
`cases/max12_912_order3_nu_q8_invariant_support_20260824/` and
`ops/aws_q8_invariant_support_run.sh`.  It should be run on a provisioned
remote host, not on the swap-constrained local machine.

The output proves only the finite-box rational-coefficient relation exclusion
stated in the report.  It does not give a global equation, normalization,
genus, projective boundary, rational trajectory, or `(9,12)` exclusion.
