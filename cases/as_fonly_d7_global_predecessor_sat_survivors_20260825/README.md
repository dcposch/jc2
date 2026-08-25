# Exact SAT survivors of the aligned global-predecessor gate

## Result

The AWS structural-base race produced three SAT models before the first
passing model triggered a clean stop of the redundant global and per-base
searches.  All three models passed the independent literal-integer replay:

| base index | structural digits | predecessor count | Q9-completion count |
|---:|:---:|---:|---:|
| 303 | `0102020` | 1 | 43,046,721 |
| 513 | `0201000` | 1 | 43,046,721 |
| 519 | `0201020` | 1 | 43,046,721 |

For each retained model, the replay reports zero in the 20 predecessor rows,
the corrected 5/12/11 top rows, the 23 Q9 rows, the 22 Q8 rows, the 19 Q7
rows, and all 46 terminal rows in degrees 12 through 9.  The recursive carry
and literal integer determinant divided by 243 agree exactly.

The first result, base `0201020`, was found on Box02 at
`/home/ubuntu/jobs/as_global_predecessor_rawq7_20260825T074543Z/base_wave1/base_0519_0201020`.
The two other results completed during the clean-stop interval.  Their exact
AWS output directories are copied byte-for-byte under `aws_results/`.

## Decoded states

The variable order is the order pinned by the parent compiler:

```text
predecessor =
 Pp,Qq,Rr,Tt,s,w,h,fua,fa,fb,fc,fd,fvb,
 d7_1,d7_4,d7_7,d6_1,d6_4,
 c5_0,c5_1,c5_2,c5_3,c5_4,c5_5,
 d5_0,d5_1,d5_2,d5_3,d5_4,d5_5.
```

Base `0201020` / index 519, the designated successor branch:

```text
predecessor = 0,2,0,1,0,2,0,0,0,2,0,0,1,0,0,1,0,0,0,0,0,0,0,2,0,0,0,0,0,1
Q9 = 1,0,0,0,0,1,0,0,0,2,2,0,1,2,1,2,0,0,0,0,2,1,1,2,0,0,0,0,1,2,2,2
Q8 = 2,0,1,2,1,2,0,1,0,1,0,0,2,2,0,1,0,2,1,0,0,2,1,1,1,2,0,0,0,2,0,0
Q7 = 0,0,0,0,0,0,0,0,0,1,1,2,0,0,0,2,0,1
```

The complete decoded vectors for bases 303 and 513 are retained in their
`direct_replay.json` files and in the producer report.

## Scope

This falsifies the proposed emptiness of the complete 79-base formula at the
displayed terminal gate.  It proves only that these three bounded source
states survive through Q7 and the degree-12-through-9 `/243` terminal rows.
The Q6/source descent, degrees 8 and 7, the next Cartier class, all-depth
continuation, algebraization, bounded support at infinite precision, and JC2
remain open.
