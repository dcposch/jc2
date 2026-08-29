# Result: recursive literal-Faber source census at D1 contact `a=9`

Date: 2026-08-26

Status: **DUAL-AWS PRODUCER PASS; NAVIGATION ONLY.**

Both exact Q and `F_65521` recursively extracted every grade `0,...,31`
of all seven frozen Faber/source rows.  Every quotient identity passed, both
engines returned `0`, both validators passed, and neither host swapped.

The central diagnostic is exact: the arbitrary correction window is not
divisible by `sigma^27`.  It has 155 nonzero row/grade pairs through grade 31,
120 of them below grade 27.  Thus V1's direct division by `sigma^27` was
unlicensed, exactly as its fail-closed validator reported.  A correction-aware
`a=9` receiver must carry or solve the lower source equations first.

## Exact support census

The number of nonzero source rows at each grade is:

```text
grade:  1  2  3  6 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
count:  7  7  7  7  5  5  5  4  7  7  7  7  6  3  3  6  6  7  7  7  7  7  7  7  7
```

The earliest equations are the load-jet connection constraints.  For
example, row 1 begins

```text
g_(1,1) = 12 k0_1 + 4 k60_1 + k20_1,
g_(2,1) = 4 k60_2 + k20_2,
g_(3,1) = 4 k60_3 + k20_3,
g_(6,1) = 12 k0_2.
```

Across all rows, the higher load jets first occur at the following grades:

```text
k0_1:1, k0_2:6;
k60_1:1, k60_2:2, k60_3:3, k60_4:16;
k20_1:1, k20_2:2, k20_3:3, k20_4:24.
```

The target support is also exact within this window: `mu20,mu20_1,mu20_2,
mu20_3` first occur at grades `28,29,30,31`, respectively, while `mu4,mu6,J`
do not occur through grade 31.  All seven rows are nonzero at each grade
`24,...,31`.

The Q and `F_65521` row-status/dependency streams have the identical
normalized SHA-256
`ce2890bdd0c2e3a4c379e59a9131e298b14c712169a7ba0f3239fb1a388b27f6`.
This is a cross-characteristic support control, not a characteristic-zero
proof of any reduction modulo the lower ideal.

## AWS custody

Exact Q / Box03:

- tag `max12_812_order2_square_d1_a9_recursive_source_census_v2_q_20260826T131000Z_box03`, PID `221168`;
- compiled input SHA-256
  `aefd60602d371d57c381bc28f7eb6b329946353c23c1b5f428181521c8b78767`;
- stdout SHA-256
  `9328095190e00e626812c1a02c7b4023e940375865ad9ef806958d2a2b0d610f`;
- metadata SHA-256
  `d15d42dbdbc2131b87c0cf244e5ecc59c93f8384f145b094199f6df3158b469e`;
- wall `3.91s`, peak RSS `581296 KiB`, swaps `0`, engine `rc=0`;
- validator `PASS_A9_RECURSIVE_LITERAL_FABER_SOURCE_CENSUS`.

`F_65521` / r6d:

- tag `max12_812_order2_square_d1_a9_recursive_source_census_v2_p65521_20260826T131000Z_r6d`, PID `279963`;
- compiled input SHA-256
  `6edba0df3f7aeb5a5b05a1b6b3a782e6629f2e4a02b44d12173d5210fe46622c`;
- stdout SHA-256
  `ed7a9178e8f6418c27952bfa08b6ccc0196a4587892f86b6a6ca231e7e4bb7e9`;
- metadata SHA-256
  `4e9f4e90afef542e8e1357c03578bb4f8028e3585cbc059ac84e30a45cc5e4e5`;
- wall `2.73s`, peak RSS `412912 KiB`, swaps `0`, engine `rc=0`;
- validator `PASS_A9_RECURSIVE_LITERAL_FABER_SOURCE_CENSUS`.

## Firewall and next gate

This census does not assert that its 120 lower equations are independent,
prime, reduced, or already solved by the preceding finite-contact charts.  It
does not license reducing grades 27--31 by a guessed radical.  The next gate
is a bounded correction-aware prolongation: triangularly eliminate the early
load-connection rows, retain the full lower ideal (including nilpotents), and
only then test the `k6/mu2/AC` receiver on `D(p*k10)`.  The tied-load
Chebyshev/Pell solution is a mandatory positive control.  There is no `a=9`,
square, order-two, `(8,12)`, maximum-twelve, or JC2 conclusion here.
