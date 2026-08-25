# AS F-only D7: exact global Q9 projection of the row-8 scalar

## Verdict

**PRODUCER-EXACT / PENDING DIFFERENT-MODEL REVIEW.**  Over all 79 compatible
structural bases of the corrected current Q10 source, the row-8 necessary
scalar is uniformly distributed on every nonempty Q9 affine fibre.  Hence it
is **not an obstruction at Q9 alone**.  Every one of the 11,881 nonempty Q9
predecessor fibres has `omega=0` completions.  No downstream restoration is
included.

## Source and corrected orientation

The producer consumes
`cases/as_fonly_d7_vertical_q9_state_gate_20260825/compile_shard.py` at
SHA-256
`54d05ebf86af9d75da0cc509e3094ce2e26516b84c73b8a50a36e71dbc9282b2`.
For each source-accepted Q10 state it reconstructs the complete 32-variable
Q9 affine system, projects its exact kernel to

```text
(q1,q2,q3,q4) = (c2_1,c2_2,d2_0,d2_1),
```

enumerates the image of dimension at most four, and restores the exact fibre
multiplicity `3^(kernel_dimension-projection_rank)`.

The frozen preregistration SHA-256 `1a70dbaa...` swapped the labels `rx` and
`ry`.  Since `C_x+D_y` has `x` coefficient `2*q2+q4` and `y` coefficient
`q1+2*q3`, the corrected source orientation is

```text
rx = floor((2*q2+q4)/3) mod 3,
ry = floor((q1+2*q3)/3) mod 3,
omega = ry-h*rx
      = floor((q1+2*q3)/3)+2*h*floor((2*q2+q4)/3) mod 3.
```

Nonmutating erratum SHA-256 is
`2b2fcef41a9d1b5d5dea788a50d7d288148214e28a39a4ac2d3e6da36cc4f9a5`.
Corrected V2 source SHA-256 is `8d1b070c...`; V3 source SHA-256 is
`c0951aaf...`.  On every projected tuple both reconstruct the literal
integer `E/3+M`, read its `x` and `y` coefficients, form `ry-h*rx`, and assert
equality with the displayed closed formula.  The old 13-trit canonical chart
is explicitly not reused.

The initial V1 source SHA-256 `9cca43b1...` implemented the swapped formula.
It failed closed on 15 shards and passed 12 only where the two expressions
coincided.  V1 is preserved solely as a negative control.

## Exhaustive corrected result

Both corrected runs have 27/27 rc-zero shards and the same ordered shard
stream digest
`b3fe039b359754bede4230fdcda9dfc0d3fbd260b719d99870d1c8315639f82b`.
The V2 aggregate JSON is SHA-256
`1de7a660aac89ba26e7714320afc1a2f603fe48cb6eedc7ac8b8f32d4ba1e48d`;
the control-complete V3 aggregate is
`e24c8791d06df825d9b179fb4205bd0ba6108268f38fda08ff73f48d7dc34662`.
The aggregates compute their counters from the frozen shard JSON before
checking them against the pinned corrected-parent controls; they are not
hand-entered output values.

Exact totals are:

| quantity | exact value |
|---|---:|
| Q10 source states | 33,225 |
| nonempty Q9 predecessor states | 11,881 |
| Q9 completions | 8,096,356,425,843 |
| `omega=0` completions | 2,698,785,475,281 |
| `omega=1` completions | 2,698,785,475,281 |
| `omega=2` completions | 2,698,785,475,281 |
| compatible structural bases | 79 |
| nonempty fibres classified `zero-partial` | 11,881 |

V3 independently records the source-system controls omitted from the V2
payload:

```text
rank/augmented-rank:
  (13,13):  6,615     (13,14):  4,320
  (15,15):  2,106     (16,16):  3,160
  (16,17):  5,288     (17,18): 11,736

Q9 fibre size:
  0:             21,344
  3^19:           6,615
  3^17:           2,106
  3^16:           3,160
```

The consistent rank-pair counts sum to 11,881 and their fibre sizes reproduce
the completion total.  The inconsistent counts plus consistent counts
reproduce 33,225.  Every nonempty fibre is `zero-partial`: none is killed by
`omega`, and none is forced entirely into `omega=0`.

## Consequence and exact stop

The projected scalar is a useful state coordinate, but it supplies no Q9
exclusion.  It cuts each current nonempty Q9 fibre by exactly one-third.  Any
exclusion must compose it with the actual Q8, Q7, Q6, Q5, Q4, and Q3
restoration equations, retaining their affine particulars and carry state.

This package does **not** prove that every `omega=0` completion restores, does
not classify the downstream zero locus, does not produce a complete map
modulo 243, and gives no all-depth, characteristic-zero, counterexample, or
JC2 inference.  Corrected V2 and V3 are separate executions of closely
related source rather than different implementations; hostile review is
required before promotion.

## Custody

Portable case:
`cases/as_fonly_d7_global_row8_projection_20260825/`.

AWS jobs:

- V2: `/home/ubuntu/jobs/as_global_row8_projection_20260825T1417Z_v2`;
- V3: `/home/ubuntu/jobs/as_global_row8_projection_20260825T1422Z_v3`;
- aggregate:
  `/home/ubuntu/jobs/as_global_row8_projection_aggregate_20260825T1420Z_v2`.

The V2/V3 shard archives have SHA-256 values `6b2a4a12...` and
`33094de6...`.  All 54 shard return codes are zero.  The case manifest hashes
the extracted shard payloads, both archives, source-history snapshots,
aggregate outputs, corrected source, runner, preregistration, and erratum.
