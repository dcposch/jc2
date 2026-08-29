# V20 dual-AWS harvest custody

Harvested: 2026-08-27

## Frozen launch

```text
FREEZE.sha256
  9c72580ca4be922bcd746e87cb22eba713319813f9f960e8cac4cce8af0220b7

source archive, identical on both hosts
  60af95933e14e9ce04614db1b8d056c95adf9a4977d7dc11e0a7f9e715df585c
```

Both jobs started at `2026-08-27T02:43:18Z`, used a 128-GiB virtual-memory
cap, a 3,600-second compiler cap, and a 900-second Singular cap.

## Exact-Q job

```text
host       Box02 / ip-172-30-0-186
tag        max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827T024311Z_q
remote     /home/ubuntu/jobs/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827T024311Z_q/source/cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827/aws_q
local      aws_q_v20/
RESULT     b23ffacd1e4e26abccaeb94a5e83f301cd98a9918a3a84e207fc462a880fe68d
EVIDENCE   4c945846a5e6cd0a901bd44b21b2800f46ef8a3ea22dab7413f8093253a55ac4
```

Compiler: rc 0, 33.65 seconds, 35,068 KiB maximum RSS.  Singular validator:
rc 0, 0.01 seconds, 10,580 KiB maximum RSS.

## F65521 job

```text
host       r6d / ip-172-30-0-45
tag        max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827T024311Z_p65521
remote     /home/ubuntu/jobs/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827T024311Z_p65521/source/cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827/aws_p65521
local      aws_p65521_v20/
RESULT     266130872a10983724a7f9a080b36fef33981ff52192cbdf6c713a75bb7cd07a
EVIDENCE   8e6562bd78f372d4cac91ee130d60d70fae04c50d54dd70f8fe49d479c615c3b
```

Compiler: rc 0, 33.26 seconds, 35,244 KiB maximum RSS.  Singular validator:
rc 0, 0.01 seconds, 10,664 KiB maximum RSS.

## Local custody checks

All 31 entries in each remote `EVIDENCE.sha256` manifest rehashed against
the harvested local files.  The exact-Q and F65521 result summaries agree on
all term counts and section verdicts.  A separate local restricted-AST parser
checked all 14 exact-Q polynomial files coefficientwise against their
F65521 reductions and independently evaluated 56 `Q[rho]` section tests:

```text
V20_INDEPENDENT_Q_TO_F65521_MATCH=14
V20_INDEPENDENT_QRHO_ZERO_SECTION_CHECKS=56
```

These are producer/custody checks, not different-model promotion.

