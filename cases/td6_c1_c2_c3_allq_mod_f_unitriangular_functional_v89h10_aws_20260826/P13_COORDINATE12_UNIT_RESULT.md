# TD6 H18 P13/FIRST coordinate-12 producer result

Date: 2026-08-26

Status: exact producer-tier result with agreeing dual-AWS custody; not promoted.

## Result

In the frozen literal-P13 normal form modulo original FIRST on the all-22-q,
`F=0`, `D(U*H*B3)` slice, E3 coordinate 12 has exactly one nonzero
`(parameter,q)` record and it is

```text
(3500000000/9)*(U/V).
```

It has no q dependence and no quotient-variable dependence. Since `U` is
inverted and `B3=V^4` on `F=0`, both `U` and `V` are units on the registered
open. Thus this coordinate is a unit and the frozen P13/FIRST normal-form
system has no common zero on this exact slice.

## Dual custody

The frozen source archive SHA-256 is
`a5b6f7306e4f1df434c53149d10d504332ca7266487cf0f854a83171ffc3d317`.
Its six-entry manifest passed independently on both hosts before execution.

| host | instance | remote root | rc | peak RSS | output TSV | result |
|---|---|---|---:|---:|---|---|
| Box02 | `i-010201a5da47795c4` | `/home/ubuntu/td6_v89h18_box02_20260826T223100Z` | 0 | 16560 KiB | `c5d136d9...` | `9df97904...` |
| r6d | `i-07eeaf8ba6f0bc419` | `/home/ubuntu/td6_v89h18_r6d_20260826T223100Z` | 0 | 16844 KiB | `c5d136d9...` | `9df97904...` |

The two output TSVs and two result files are byte-identical. Both resource
logs report approximately 0.05 seconds elapsed, zero swaps, and exit status
zero.

## Count erratum and firewall

`P13_FULL_NORMAL_FORM_VECTOR_RECORD_ERRATUM.md` corrects H15's description:
the TSV contains 238 vector records and 535 nonzero scalar entries, not 238
scalar terms. Coordinate 12 has exactly one nonzero record, so the correction
does not alter this result.

This result does not emit original-row/FIRST membership multipliers, lift
through independent total `F`, cover omitted source moduli, close TD6, or
resolve JC2. Independent hostile review is still required for promotion.
