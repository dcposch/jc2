# AWS launch: fixed-load order-two invariant quotient probe

Status: live navigation probe; no endpoint interpreted.

```text
tag=max12_812_order2_invariant_quotient_tupleA_p32003_20260826T040200Z_box03
host=ip-172-30-0-249 / Box03 / 98.80.65.144
job=/home/ubuntu/jobs/max12_812_order2_invariant_quotient_tupleA_p32003_20260826T040200Z_box03
registered start=2026-08-26T04:03:28Z
outer/registered launcher PID=154873
aws_exact_lane PID=154890
Singular PID at first audit=154899
timeout=3600 s
virtual-memory cap=67108864 KiB
characteristic=32003
loads=2,3,5,7,11,13
emitted input SHA-256=2db7c53eaab04493e9dd15cde07c898b2d6dff3c3f3c93221c36ec4e599fc726
freeze manifest SHA-256=5d5db8e2a88fe0a1bc1082fe6a95fbf5fb16173d3adc2bbbaf02036c703437d4
```

The AWS compiler passed the exact tails/design pins, canonical all-tail
digest, weight, affine-load, and deck-parity source checks.  The engine is a
navigation experiment only: a timeout or failed projection is no theorem,
and a plane eliminant is not a normalization genus.

## Tuple B / independent prime and host

```text
tag=max12_812_order2_invariant_quotient_tupleB_p65521_20260826T040600Z_box02
host=ip-172-30-0-186 / Box02 / 34.203.207.55
job=/home/ubuntu/jobs/max12_812_order2_invariant_quotient_tupleB_p65521_20260826T040600Z_box02
registered start=2026-08-26T04:07:46Z
outer/registered launcher PID=269187
aws_exact_lane PID=269203
Singular PID at first audit=269212
timeout=3600 s
virtual-memory cap=67108864 KiB
characteristic=65521
loads=17,19,23,29,31,37
emitted input SHA-256=7d12962e2b529cf6963677ffac8a4d217403659c63a8767a7266d11473ba595e
tuple-B freeze manifest SHA-256=e453291111f1419fa2b62f965c213709eb2307fbf103b97680aca2db34a3f0a6
```

The tuple-B compiler pins the tuple-A compiler and regenerates all
load-dependent tail coefficients after changing the load dictionary.  Its
only exact source transformations are the preregistered characteristic,
load-sentinel, and even-target sites.  Comparison remains navigation only.

## Prime/load cross-controls

All four cross-controls started at `2026-08-26T04:22:02Z`.  They share the
frozen cross-control compiler and differ only by the preregistered tuple and
characteristic.  Each has a one-hour timeout and a 64-GiB virtual-memory cap.

```text
config=A65521
tag=max12_812_order2_invariant_quotient_A_p65521_20260826T042100Z_box03
host=ip-172-30-0-249 / Box03 / 98.80.65.144
job=/home/ubuntu/jobs/max12_812_order2_invariant_quotient_A_p65521_20260826T042100Z_box03
outer/registered launcher PID=156974
aws_exact_lane PID=157007
Singular PID at first audit=157016
characteristic=65521
loads=2,3,5,7,11,13
emitted input SHA-256=36a3db755ccd22c19aeb47fd26bf0652fbf6677d37d18045a37e44d23108e4a9

config=B32003
tag=max12_812_order2_invariant_quotient_B_p32003_20260826T042100Z_r6d
host=r6d / 100.26.198.153
job=/home/ubuntu/jobs/max12_812_order2_invariant_quotient_B_p32003_20260826T042100Z_r6d
outer/registered launcher PID=224475
aws_exact_lane PID=224491
Singular PID at first audit=224500
characteristic=32003
loads=17,19,23,29,31,37
emitted input SHA-256=f55a75be3363099cb277d94748da1bd107aa6739794082c7dc8b810b09f6f9f1

config=C32003
tag=max12_812_order2_invariant_quotient_C_p32003_20260826T042100Z_box03
host=ip-172-30-0-249 / Box03 / 98.80.65.144
job=/home/ubuntu/jobs/max12_812_order2_invariant_quotient_C_p32003_20260826T042100Z_box03
outer/registered launcher PID=156963
aws_exact_lane PID=156990
Singular PID at first audit=156999
characteristic=32003
loads=41,43,47,53,59,61
emitted input SHA-256=f2fced2f5a7c94f7213979228505e6065c7d6bc10f0a68fab4653f562430a36d

config=C65521
tag=max12_812_order2_invariant_quotient_C_p65521_20260826T042100Z_box02
host=ip-172-30-0-186 / Box02 / 34.203.207.55
job=/home/ubuntu/jobs/max12_812_order2_invariant_quotient_C_p65521_20260826T042100Z_box02
outer/registered launcher PID=269663
aws_exact_lane PID=269679
Singular PID at first audit=269688
characteristic=65521
loads=41,43,47,53,59,61
emitted input SHA-256=4debb5acdb2a0bec098740da2fd91dd4cde513ba1af23af889262a958240d1cc

cross-control freeze manifest SHA-256=1626d579423e2525e0362fe19ae5abdc16405fb2525dfc6ea04a82574fd412fa
```

At first audit all compilers returned their exact-source `PASS` sentinels,
all four engine processes were live, and no lane used swap.  These remain
navigation controls: agreement can guide the next discriminator but cannot
establish a characteristic-zero genus or source theorem.
