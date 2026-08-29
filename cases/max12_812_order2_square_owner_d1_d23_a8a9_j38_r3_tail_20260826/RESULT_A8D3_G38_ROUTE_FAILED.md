# No-verdict result: a8d3 grade-38 R3-tail producer route failed

Date: 2026-08-26

Status: **FROZEN PRODUCER-ROUTE FAILURE; NO MATHEMATICAL VERDICT ON THE
`a=8,d=3` CELL.**

## Exact scope and failure

The unchanged V2 grade-38 client was run on

```text
D(p*k0*J), ord(A)=8, ord(C)=11, ord(R)>=8, d=3
```

using the mechanically derived grade-38 jet ceilings.  After the original
128-GiB attempts ended with resource-only engine rc 14, the exact same
frozen client was replayed with high-memory caps over exact `Q`, `F_65519`,
and `F_65521` on three AWS hosts.  All three engines completed rc 0 with zero
swap and produced byte-identical stdout SHA256
`90722afbc42522b2d3fca4568649fea41419dddc700808fd35d3c52b1275c761`.

The output consistently reports:

```text
PRIMITIVE_FAMILY_COUNT=17
ALL_LICENSED_SOURCE_JETS_IN_INVENTORY=1
LICENSED_SOURCE_JET_COUNT=100
LICENSED_TARGET_JET_COUNT=22
ALL_LICENSED_TARGET_JETS_RETAINED=1
ALL_MECHANICAL_JET_MAXIMA_ENTER_G38=1

ALL_SEVEN_SOURCE_ROWS_BRIDGED=0
SOURCE_R3_MOD_G39=0
ETA_RTAIL_SAFE=0
GRADE38_COEFFICIENT_MINUS_J_OVER_4=0
FULL_R3_MOD_G39=0
EXACT_DJ_UNIT=0
FAIL=SOURCE_CEILING_BRIDGE_OR_R3
```

The fail-closed validator rejects at the first missing sentinel,
`ALL_SEVEN_SOURCE_ROWS_BRIDGED=1`.  Therefore none of the downstream R3,
coefficient, or unit sentinels is accepted as an independent theorem.  The
failure falsifies this grade-38 producer/bridge route only.  It neither
proves survival nor proves emptiness of the cell.

## High-memory AWS executions

| endpoint | registered tag | rc / wall / max RSS KiB / swap | validator |
|---|---|---|---|
| exact `Q`, Box02 | `max12_812_order2_square_d1_a8a9_d23_j38_r3_tail_v2_a8d3_q_box02_highmem_20260826T1933Z` | 0 / 35:12.21 / 330806212 / 0 | FAIL missing all-seven bridge |
| `F_65519`, Box03 | `max12_812_order2_square_d1_a8a9_d23_j38_r3_tail_v2_a8d3_p65519_box03_highmem_20260826T1933Z` | 0 / 28:34.04 / 307456128 / 0 | same |
| `F_65521`, r6d | `max12_812_order2_square_d1_a8a9_d23_j38_r3_tail_v2_a8d3_p65521_r6d_highmem_20260826T1933Z` | 0 / 27:34.16 / 307455784 / 0 | same |

All three used source archive SHA256
`01cca2d13adfd6685dd628b89f7eace7344b5c778b828d29563f8b8279040f53`,
verified the frozen V2 source before execution, and used ordinary polynomial
rings rather than Singular quotient rings.

## Successor and firewall

A separately preregistered bridge diagnostic retains each of the seven row
residuals, valuations, term counts, and leading terms.  Its purpose is to
distinguish a source-emitter/analytic-bridge defect from a genuinely missing
grade-38 column before any repaired endpoint is attempted.

This artifact is not a promotion and must never be composed as an emptiness
or survival result.  It does not affect the separately reviewed `a=9,d=2,3`
promotion, the `a>=10` tail, another load chamber, `p=0`, `k0=0`, the
exact-square zero section, order two, maximum twelve, or JC2.
