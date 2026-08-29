# Hostile review: universal odd-row Laurent-to-Faber pole recurrence

You are the independent hostile reviewer. Work in
`/Users/dc/code/math/jc2`. Do not trust producer marker strings or finite
grids as proof. Do not edit any producer, prompt, ledger, or existing review.
Write only

```text
xmodel/max12-812-order2-square-d1-universal-odd-pole-recurrence-hostile-review-grok-20260826.md
```

and finish with exactly one verdict: `CONFIRMED`, `REPAIR`, or `REFUTED`.

## Frozen custody

```text
97cb6fedc22c3352b304684c0e46e768eb12ce579ba52dbf24bb38be78533263
  cases/max12_812_order2_square_owner_d1_universal_odd_pole_recurrence_20260826/RESULT.md
6ed0d583e64eecc9403f135692d0ac0b0158a3717ddd4daad84d4df76394ba87
  cases/max12_812_order2_square_owner_d1_universal_odd_pole_recurrence_20260826/EVIDENCE.sha256
9990ba104bb7d5bf4e494e5faad59545b6a6500cbdd3db571ee25429d3e13ed0
  cases/max12_812_order2_square_owner_d1_universal_odd_pole_recurrence_20260826/FREEZE.sha256
c36812e8ad47e92086f49d345abb9f89f624519adb0db38d8edf9ec372d2890f
  cases/max12_812_order2_square_owner_d1_universal_odd_pole_recurrence_20260826/AWS_LAUNCH_METADATA.md
81b0f9d772add009b1d7c6ed0caa9ef13098fc72f8921e502128ba1402901f6b
  cases/max12_812_order2_square_owner_d1_universal_odd_pole_recurrence_20260826/PRODUCER_FREEZE.sha256
d1e3218e3104651996b77d440eb0d92924369c8c380ed3ccf0330a869a170c41
  cases/max12_812_order2_square_owner_d1_universal_odd_pole_recurrence_20260826/odd_pole_recurrence_miner.py
```

Rehash every manifest row. The failed V1 wrapper launches are no-verdict and
are not evidence; V2 alone is charged.

## Charges

1. Independently derive the odd frozen Faber generating transform
   `Phi(x)=(1-sx)^(-1/2)Y(x/(1-sx))`, `s=p/2`, from the row matrix. Check the
   sign and the half exponent against rows 1,3,5,7.
2. Verify that an exact pole-`q` odd Laurent term is spanned by
   `Y_(q,e)=x^e/(1+sx)^q`, `0<=e<q`, and that the transform is exactly
   `x^e(1-sx)^(q-e-1/2)`. Look for parity, numerator-degree, polynomial-part,
   or indexing exceptions which invalidate the claimed basis coverage.
3. For arbitrary integers `1<=r<=M`, derive the functional
   `W_(M,r)=(1-sx)^(M-r-1/2)` and check the degree proof that its terminal
   coefficient annihilates every `q<=r`. Do not infer the unbounded theorem
   from the finite `M<=24` grid.
4. Check sharpness. At `q=r+1,e=r`, determine the exact surviving
   coefficient; at `q=M+1,e=M`, check it is one. State any special behavior
   on `p=0` without confusing a chart specialization with uniform sharpness.
5. Recover both row-seven vectors in powers of `p`, with signs:
   `[1,-p/4,-p^2/32,-p^3/128]` for `r=2` and
   `[1,+p/4,+3p^2/32,+5p^3/128]` for `r=3`.
6. Audit arbitrary moving `p(sigma)`: why substitution and sigma truncation
   commute, and whether convolution of rows changes the claimed terminal
   relation.
7. Inspect the miner code independently. Recompute the transform/check counts,
   exact-Q and `F_65521` lanes, all negative controls, resource metadata, and
   the composed D1 inventory SHA/pole ceiling. The finite replay is a software
   control only.
8. Enforce the firewall: the theorem generates a row syzygy after a complete
   pole ceiling and target placement are separately known. It does not prove
   any inventory, chart/fan cover, D1 theorem, order two, maximum twelve, or
   JC2.

Give the smallest failing `(M,r,q,e,row)` or smallest basis exception if one
exists.
