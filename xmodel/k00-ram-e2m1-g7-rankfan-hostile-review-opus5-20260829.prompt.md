# Hostile review: corrected ramified `e=2,m=1,B11111` G7 closure

You are Opus 5, an independent hostile reviewer in the plane Jacobian-
conjecture campaign. Write only
`xmodel/k00-ram-e2m1-g7-rankfan-hostile-review-opus5-20260829.md`.

Read `COORDINATION.md` and the artifacts below. Do not inspect, list, search,
stat, build, modify, or control `jc2-lean`. Use scoped git commands excluding
it. Heavy or uncertain computation is AWS-only; seconds-scale exact stdlib
reconstruction is allowed locally. Use `apply_patch` for the deliverable.

Pinned producer artifacts:

```text
66b4f59e16f9f8f26a42e5305e5906ff495c9d00c15d96a291f91baa9efbeff4
  xmodel/k00-ram-e2m1-g7-rankfan-certificate-sol56-20260829.md
981b39f91afd4e449193077bc00d02937701618cee9bc3ae53547edaaa11dac6
  xmodel/k00-ram-e2m1-g7-rankfan-replay-sol56-20260829.py
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/compile_contracted_source_v20r2.py
98fb38535405f1cc853dd4d430e26876a84f6f97c538f862f18a0446c0c97ecf
  xmodel/k00-v20r2-valuative-comparison-v1-sol56-20260829.md
```

The claim is exact point-set emptiness of the normalized ramified cell
`Lambda=t^2`, `ord_t(d)=1`, load-order label `B11111`, on
`D(k10[0]) intersect (D(s) union D(t))`, already by G7. Review it as a
different model, not as a replay operator.

Required attacks:

1. Rebuild the relevant G3--G7 coefficients independently from all 569 frozen
   tails and the literal ramified load scale. Do not use the producer replay's
   serialized rows as an oracle.
2. Verify the erratum exactly:
   `[t^3]A10(d)=DM4(ell)[u]+A10^[3](ell)=DM4(ell)[u-mu/2]`, and the row-2
   witness `5/65536`; explain whether every earlier G3--G5 conclusion really
   survives.
3. Audit exhaustiveness and signs in both complete rank fans: G5 rank 2/1/0,
   the centered G6 cone, and its G7 rank 2/1/0 branches. Retain all seven
   labelled rows and explicitly test the reactivated row 6.
4. Check the exact unloaded surface, centering shifts, opens, algebraic-
   closure descent, field-valued versus scheme-theoretic use of the radical,
   and the implication from G7 emptiness to the full G38 cell.
5. Run ordinary and optimized producer replay only after clean-room work, then
   add independent fixtures/mutations. State precisely any discrepancy and
   the strongest verdict licensed by the evidence.

Do not infer any other ramified-cell, K00-wide, attainment, arc, polynomial
map, or JC2 conclusion. Give a crisp `CONFIRM`, `CONFIRM_WITH_CORRECTIONS`, or
`REJECT` verdict and a promotion recommendation. End with standalone
`<!-- BODY-END -->`; do not add a seal block.
