# V32 beta-dual post-math sentinel erratum

V29 reached and passed the exact dual remainder, inverse, lambda-prime
decomposition, derivative source identity, omission negative control, and all
denominator-clearing assertions.  It then failed at a stale reporting
sentinel:

```text
assert source_multiplier_terms == 1489
```

`1489` is the support count of the beta-zero projection of the 28 source
multipliers.  Exact beta-varying multipliers can contain new derivative-only
monomials, so their union support need not remain 1489.  V32 makes no algebra
change.  It asserts the base projection count `1489`, separately requires a
nonempty beta support/coefficient count, and prints base, beta, and union
counts.  All earlier hashes and mathematical assertions are unchanged.

Run only on AWS:

```sh
python3 jc2/cases/td6_c1_c2_c3_q2_beta_dual_20260825/replay.py \
  > beta-dual-v32.stdout 2> beta-dual-v32.stderr
```

Scope remains first-order on `D(U*H*B3)`.  No finite-beta neighborhood,
four-parameter family, TD6, SP-2, or JC2 claim follows.
