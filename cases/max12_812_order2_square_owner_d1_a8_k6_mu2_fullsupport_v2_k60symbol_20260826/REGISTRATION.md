# Registration: D1 `a=8` V2 formal-`k60` ring repair

Date: 2026-08-26

Status: **PREREGISTERED DUAL-AWS SOFTWARE REPAIR.**

V1 passed the complete `D(k60)` source client over exact Q and `F_65521`,
then failed closed in the `V(k60)` client because its support-filter code
differentiated by an omitted ring symbol `k60`.  V2 pins V1 and its negative
control and performs exactly six text replacements in V1's generated
Singular input:

```text
b0,b1,k0,k61,k62,k2load
  ->
b0,b1,k0,k60,k61,k62,k2load
```

The six sites are the positive-valuation source ring, target ring, and four
maps.  The added symbol has the identity image in every map and occurs in no
equation: the load remains exactly
`k6=sigma*k61+sigma^2*k62`.  Thus this repairs source-support typing without
changing either section or any mathematical sentinel.

Frozen V1 pins:

```text
0230ca443d49e47b5d6ebae8c0f8a88d31a793d13b1df59e3698e166226d177b
  ../max12_812_order2_square_owner_d1_a8_k6_mu2_fullsupport_20260826/compile_a8.py
c18bdd9f55a108470ef166e6c0cfa243ab61b63f45742537046fdb6e583b5dc8
  ../max12_812_order2_square_owner_d1_a8_k6_mu2_fullsupport_20260826/FREEZE.sha256
be3d6843a27db31ee7e844fe1edea1e2f6fb7b65ba9b7c8f2289ff28e3441ed2
  ../max12_812_order2_square_owner_d1_a8_k6_mu2_fullsupport_20260826/RESULT_NEGATIVE_CONTROL.md
```

## Acceptance and scope

Run exact Q on Box03 and `F_65521` on r6d, each with 24-GiB virtual-memory,
600-second compiler, and 1800-second Singular caps.  Require replacement
count six, all unchanged V1 markers exactly once, no diagnostics, rc 0, and
zero swap.

A dual PASS is producer-tier evidence only for the two exhaustive `k6`
sections at fixed `ord(A)=8,ord(C)=9,ord(R)>=8` on `D(p*k10)`, after the
reviewed first-normal, half-weight, and `M=0` gates.  It says nothing about
`a>=9`, other square contacts, the whole square stratum, order two, `(8,12)`,
maximum twelve, or JC2.  It must not contradict the exact tied-load
Chebyshev/Pell survivor.

