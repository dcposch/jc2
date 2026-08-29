# Result: corrected D1 `a=9` literal-Faber source census

Date: 2026-08-26

Status: **DUAL-AWS PRODUCER PASS; SOURCE-SUPPORT NAVIGATION ONLY.**

The parentheses-only V3 repair passed on exact Q and `F_65521`.  Compiler
sentinels found exactly `190`, `72`, and `27` fully parenthesized occurrences
of the `k10`, `k6`, and `k2` jets followed by their complete Faber weights.
All recursive quotient identities passed; both engines returned `0`; both
validators passed; neither host swapped.

The corrected result is sharply different from quarantined V2:

```text
A9V2_NONZERO_ROW_COUNT=27
A9V2_LOWER_THAN_27_ROW_COUNT=0
A9V2_RECURSIVE_QUOTIENT_IDENTITIES=1
```

Thus the full seven-row source is exactly divisible by `sigma^27` for the
registered correction window.  Nonzero row counts by grade are

```text
grade 27: 5 rows
grade 28: 5 rows
grade 29: 5 rows
grade 30: 6 rows
grade 31: 6 rows.
```

Rows 4 and 6 are zero through grade 29; row 6 is zero through grade 31.
The complete grade-27 leading block is

```text
g27_1 =  (3/4) c1 k60,
g27_2 =  (3/4) c0 k60,
g27_3 = -(3/16) p c1 k60,
g27_4 = 0,
g27_5 = -(3/128) p^2 c1 k60,
g27_6 = 0,
g27_7 = -(3/512) p^3 c1 k60.
```

At grade 28, the only new target is `mu20` in row 2 and the only new load
jet is `k60_1`; grades 29--31 introduce `mu20_1,mu20_2,mu20_3` and the
successive source/load corrections printed in the frozen outputs.  `mu4,
mu6,J` do not occur through grade 31.  `k2` first occurs at grade 31, and
`k10_1` also first occurs at grade 31.  The exact Q and `F_65521` normalized
row-status/dependency streams agree with SHA-256
`b34554fea3d1cd6dad0bd957b3c877c84de32e58ac472ac603c68438dbc01bb1`.

## AWS custody

Exact Q / Box03:

- tag `max12_812_order2_square_d1_a9_source_census_v3_parenthesized_q_20260826T132000Z_box03`, PID `222221`;
- compiled input SHA-256
  `77a0b2db497f1d2276392c1b2f862b3c05aa027c677fb66778cced1c3fad8d9f`;
- stdout SHA-256
  `ead70714b88be93b818bf7fe06403698baaaf4a710d0042a129a6e9dbc67f59c`;
- metadata SHA-256
  `d039caad4fef389b5041b1c312bc141758e6521427ae6eb9561fcab35ba232bb`;
- wall `6.00s`, peak RSS `1255356 KiB`, swaps `0`, engine `rc=0`;
- validator `PASS_A9_V3_PARENTHESIZED_LOAD_SOURCE_CENSUS`.

`F_65521` / r6d:

- tag `max12_812_order2_square_d1_a9_source_census_v3_parenthesized_p65521_20260826T132000Z_r6d`, PID `281041`;
- compiled input SHA-256
  `82ea7ddab706d0f253c4b600932d00572bee9b23d3688cc6f36b696711dfa71e`;
- stdout SHA-256
  `899d4af8125f08301967e465815f4bc58ecb11f141ee5a2f7e9c4c6b4e164ee4`;
- metadata SHA-256
  `424cb809d802d56a5c03ad77e3dfd3619f6293a5d8a00cf85c41af566ee3964d`;
- wall `3.99s`, peak RSS `889120 KiB`, swaps `0`, engine `rc=0`;
- validator `PASS_A9_V3_PARENTHESIZED_LOAD_SOURCE_CENSUS`.

## Firewall and next gate

This client certifies the finite source-support window, not the analytic
root/residue receiver or a scheme/arc conclusion.  A separate proof may use
the grade-27 block to analyze `D(k60)`.  The genuine successor is the
`V(k60)` grade-28/29 `k60_1`--`mu2`--`AC/L` collision with every displayed
correction retained.  The tied-load Chebyshev/Pell solution remains a
mandatory positive control.  There is no `a=9`, square, order-two, `(8,12)`,
maximum-twelve, or JC2 conclusion in this census alone.
