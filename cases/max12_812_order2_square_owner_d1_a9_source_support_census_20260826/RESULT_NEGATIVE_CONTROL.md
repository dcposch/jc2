# Result: fail-closed `a=9` literal-Faber census

Date: 2026-08-26

Status: **NEGATIVE CONTROL; NO MATHEMATICAL VERDICT.**

Both registered AWS lanes compiled the frozen literal Faber/source client and
Singular exited `0`, but the fail-closed validator correctly rejected both
outputs:

```text
A9_SOURCE_DIVISIBLE=0
A9_SOURCE_QUOTIENT_IDENTITIES=0
A9_FAIL=SOURCE_EXTRACTION
validator=FAIL_MISSING_OR_NONUNIQUE:A9_SOURCE_DIVISIBLE=1
```

The failure is structural, not an order-two contradiction.  This V1 chart
inserted arbitrary higher jets of `p,A,C,R,k10,k6,k2,mu2` and then attempted
to divide every full source tail by `sigma^27`.  Those arbitrary jets need not
satisfy the already-earlier Faber equations.  Consequently the raw source
has nonzero grades below `27`, so the division premise is false.  Every
printed object labelled `A9_ROW_27_*` through `A9_ROW_31_*`, and the associated
dependency table, was obtained after a nonexact division and is quarantined:
none of it may be consumed as source support.

The next licensed client must extract the literal source recursively from
grade zero, preserve every nonzero lower equation, and only form a grade-27
receiver after imposing or carrying the resulting correction-aware
conormal/Kuranishi constraints.  In particular, V1 proves neither emptiness
nor existence at `a=9`, and gives no square, order-two, `(8,12)`,
maximum-twelve, or JC2 conclusion.

## Dual-AWS custody

Exact Q / Box03:

- lane `max12_812_order2_square_d1_a9_source_support_census_q_20260826T130000Z_box03`;
- engine `rc=0`, wall `1.34s`, peak RSS `111084 KiB`, swaps `0`;
- compiled input SHA-256
  `8bc7317cc088c71ad9e619869e5364a3ef1faf061d96fe3a4846fb92b2068dee`;
- stdout SHA-256
  `3c838b4197064063f0a921b422aa10fc9fc1d9edcd087d169c85253cd2393c88`;
- stderr SHA-256
  `cb11ea27efd241f76996fe4aa5f8bca26775663972e0c4e05649e5709a409d6f`;
- metadata SHA-256
  `d64fb675a2b9f2d432a909224b28b92d036e82badcff92b069109b436f741ad1`;
- validation SHA-256
  `4fa20524883426fe8624fd7777f926e1622365ecb3ec3bd6172d65e1f28a7643`.

`F_65521` / r6d:

- lane `max12_812_order2_square_d1_a9_source_support_census_p65521_20260826T130000Z_r6d`;
- engine `rc=0`, wall `0.72s`, peak RSS `81204 KiB`, swaps `0`;
- compiled input SHA-256
  `f7511d43479aaaaf7c2a86247b9dd5a795e44a7978f8f48c7e926c306e0fb65b`;
- stdout SHA-256
  `939e15f6e759e4217e1330a824e59bb9b75d78d1e46257040397b571a17ad97c`;
- stderr SHA-256
  `c4ab265786045d9b5b9a7513eaea7cb5fe61e28d09f68bb71db70408f269959d`;
- metadata SHA-256
  `476143f42a849b91f66208a283d3f6da42f3321c71bec3cc4d6adee81365d7ca`;
- validation SHA-256
  `4fa20524883426fe8624fd7777f926e1622365ecb3ec3bd6172d65e1f28a7643`.

The two fields agree on every fail-closed marker.  Agreement is only a
control on the software failure mode, not a theorem endpoint.
