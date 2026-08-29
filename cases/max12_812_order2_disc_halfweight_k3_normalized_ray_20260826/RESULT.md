# Result: discriminant half-weight K3 normalized-ray source separator

Date: 2026-08-26

Status: **DUAL-AWS PASS.  EXACT-Q PRODUCER ENDPOINT; INDEPENDENT
CHARACTERISTIC-32003 CONTROL.**

The immutable package has `FREEZE.sha256` SHA
`13ae545507753ccc60a44c3495ce6a2afdfb3b1ac9fc60e1e838b3c7953b374a`.
The shipped source archive had SHA
`870c04fd793fdde72324995fe6626d666ada6f98b22a3b07aa64ca14b1ff01d3`.

Both registered AWS lanes completed with compiler rc zero, Singular rc zero,
and the unique fail-closed validator endpoint

```text
validator=PASS_K3_NORMALIZED_RAY_SOURCE_UNIT
```

The exact-Q Box03 lane used tag
`max12_812_order2_disc_halfweight_k3nr_q_20260826T071500Z_box03`; Singular
ran for 1:59.51 with maximum RSS 1,692,608 KiB and no swap.  The independent
characteristic-32003 r6d lane used tag
`max12_812_order2_disc_halfweight_k3nr_p32003_20260826T071500Z_r6d`;
Singular ran for 0:52.33 with maximum RSS 996,064 KiB and no swap.

The two stdout files are byte-identical at SHA
`8e03635fab8e3158f8df5ce74b6c888dbcd5640a72131004e1078c03a55bdf7f`.
They each contain exactly once:

```text
K3NR_SOURCE_HASHES=PASS
K3NR_TRUNCATED_INVERSE=1
K3NR_SIGMA12_DIVISIBLE=1
K3NR_SIGMA12_BASE_ZERO=1
K3NR_SIGMA13_KERNEL_ZERO=1
K3NR_FORBIDDEN_LOW_GRADES=1
K3NR_TANGENT_FREEZE_WEIGHT2=1
K3NR_RAW_U1_MATCH=1
K3NR_RAW_F1_ZERO=1
K3NR_RAW_F2_MATCH=1
K3NR_ROW_COMPARE_1=1
K3NR_ROW_COMPARE_2=1
K3NR_ROW_COMPARE_3=1
K3NR_ROW_COMPARE_4=1
K3NR_ROW_COMPARE_5=1
K3NR_ROW_COMPARE_6=1
K3NR_ROW_COMPARE_7=1
K3NR_C17_RECURRENCE=1
K3NR_LAST3_CERTIFICATE=1
K3NR_ANALYTIC_BT_UNIT=1
K3NR_SOURCE_BT_UNIT=1
K3NR_ENDPOINT=PASS_NORMALIZED_RAY_SOURCE_UNIT
```

Thus the complete frozen source agrees, coefficient by coefficient and
before unit saturation, with the exact unitriangular Laurent-to-Faber
transform of all seven analytic `sigma^14` rows.  The client retains the raw
`U^2` direction and proves the source ideal is unit on `D(b*t)` by the last
three rows.

Scope: this is a characteristic-zero producer endpoint for the explicitly
parametrized nonsquare discriminant normalized ray.  Exhaustive promotion
from analytic K2 support to every frozen-source discriminant K2 point still
requires the separately registered exact-Q K2 source/analytic equality
endpoint.  No square-chart, Taylor-family, order-two, `(8,12)`, maximum
twelve, or JC2 verdict is asserted here.
