# Eta-five h-linear correction inside the Q-R kernel

Date: 2026-08-26 UTC

Status: **DUAL-AWS EXACT GRADED LIFT; hostile review pending.**

The exact scalar-correction map from eight row multipliers to the worst
h-linear Q-R piece has rank three.  Its five-dimensional kernel, in the
free-column order `(F4,F5,F6,F7,F8)`, is

```text
( 4/3,-1,0,1,0,0,0,0)
(-1,  2/3,0,0,1,0,0,0)
( 0,  0,0,0,0,1,0,0)
(10/9,-2/3,0,0,0,0,1,0)
(-4/3,7/9,0,0,0,0,0,1).
```

Its canonical SHA is

```text
ce7ba74b70b4895a639970b7acc1a2f4f0f802d4afe7df6955bc8c1eaeb9aa93.
```

After the V5 free-zero correction, the complete next h-linear closed-corner
grade consists of fourteen R-square and Q-cubic terms, canonical SHA

```text
5a8d5aba718de8396363443cd7b951c83ece5bea4707ca4cc063ae5b9dbd89ef.
```

Their image from the five kernel directions has rank three.  Exact RREF gives
the kernel-coordinate correction

```text
(1/4,-1/3,0,0,0).
```

Combining it with V5 yields the full scalar h correction

```text
(g1,...,g8)=(5/2,-25/18,0,1/4,-1/3,0,0,0).
```

For

```text
Fi''=Fi'+h*gi,
W_h''=sum_i Fi'' E_i(h),
```

the complete h-linear Q-R and R-square/Q-cubic components both vanish
exactly.  The full corrected witness has 71 terms and canonical SHA

```text
3363e67da50c953ab37b4c67dc5dfeb77d3cfdf75e31b5d6f97dd87dafc7f833.
```

Its h-linear coefficient now has 18 terms, SHA

```text
6fee8f428caa5364b3390a4c835c2a47214e91e2f8d6d6709137f3c428d0d5e3.
```

## New exact eta range

On the charged open control-2 slice

```text
alpha=15/2, beta=5+u, delta=5+v, u>0, v>0, T>0,
```

this witness has unique least term `la^20` uniformly exactly when

```text
eta >= 15/4.
```

At the endpoint `eta=15/4`, the eight new extremal terms are quadratic in h:

```text
-77/162 h^2*q2*r2 + 8/27 h^2*q2*r1 - 5/54 h^2*q2*r0,
+8/27 h^2*q1*r2 - 5/54 h^2*q1*r1 + 8/81 h^2*q1*r0,
-5/54 h^2*q0*r2 + 8/81 h^2*q0*r1.
```

Their normalized margins are `2*eta-15/2+v` for the q2 terms and
`2*eta-15/2+u` for the q1/q0 terms.  Hence the equality endpoint is strict
throughout the open u,v quadrant.  Conversely, if `eta<15/4`, choosing the
relevant positive u or v sufficiently small places an actual displayed term
below target.  The remaining 28 closed-corner threshold terms are the twenty
old q2/q corner terms plus these eight h-squared terms.

Thus the successive exact witness ranges are

```text
unchanged W':             eta >= 15/2,
V5 Q-R correction:        eta > 5,
V6 kernel grade-5 lift:   eta >= 15/4.
```

The next strict cell `0<eta<15/4` begins with the h-squared Q-R piece and
should be treated by the next filtered correction, not called a branch
survivor.

## Dual AWS custody

- Box03 forward tag
  `max12_912_order3_d1_double_root_control2_h_grade5_kernel_lift_v6_20260826T041000Z_box03_forward`,
  PID `155376`: rc 0, empty stderr, 22,420 KiB maximum RSS, zero swap;
  JSON SHA `26e540ce564877c4435b2ed2bd8a9cb7bafe8265783793e57c91471ecdb7cdd9`.
- r6d reverse tag
  `max12_912_order3_d1_double_root_control2_h_grade5_kernel_lift_v6_20260826T041000Z_r6d_reverse`,
  PID `222945`: rc 0, empty stderr, 22,636 KiB maximum RSS, zero swap;
  JSON SHA `ac4d8643682a4ddb16e6eb4c1b83042f6dff8752e1679bcdec1c03e071c39f1f`.

Deleting only the registered `tag` and `order` custody fields gives
byte-identical sorted semantic JSON, SHA

```text
d476a5dc9000ba524d6067242652b4de7c4c8372748071546b4824e67a3c778b.
```

Both ran under 4-GiB / 900-s caps after pre-GO registration and source checks.

## Firewall

This is complete only for scalar h-multiplier corrections through the two
named h-linear grades.  It does not prove general multiplier-support
completeness, classify the eta boundary or smaller eta, construct an h-adic
or formal lift, move axis or loads, cover another support/fan cell, prove D1,
or prove JC2.
