# h-squared Q-R filtered syzygy lift

Date: 2026-08-26 UTC

Status: **DUAL-AWS EXACT GRADED LIFT; hostile review pending.**

The V6 witness has exactly eight Q-R monomials in its h-squared coefficient,
canonical SHA

```text
1fbcb8047679987fba12aa681546dfd0bb27134d4e03d08efee6e5742417c275.
```

Each has pre-h closed-corner margin `-15/2`.  Exact RREF against the complete
Q-R components of all eight h=0 rows again has rank three and gives the
free-zero correction

```text
(d1,...,d8)=(5/24,-2/9,0,0,0,0,0,0).
```

Adding `h^2*d_i` to the V6 multipliers preserves the h-zero and h-linear
coefficients exactly and cancels the complete h-squared Q-R piece.  The
corrected witness has 57 terms and canonical SHA

```text
efe2ebcc234d836763a8a47f58a228f6a90cc20fd876bb48b1144a60f3e5d6a5.
```

Its residual h-squared coefficient has only two terms, SHA

```text
d5ae76fe9b6ab90e9b40f94d639869685703ce9037bb9ff0c16a4d952b26c81c.
```

## Exact eta range and next support wall

On

```text
alpha=15/2, beta=5+u, delta=5+v, u>0, v>0, T>0,
```

the new witness has unique least term `la^20` uniformly exactly for

```text
eta >= 5/2.
```

At eta `5/2`, the new eight extremal terms are h-linear but have Q-degree two
and R-degree one:

```text
 1/27 h*q1*q2*r2     +1/81 h*q1*q2*r0
+1/81 h*q1^2*r1     -1/81 h*q0*q2*r2
+1/54 h*q0*q2*r1    +5/162 h*q0*q1*r2
+1/162 h*q0*q1*r0   +1/162 h*q0^2*r1.
```

Their closed-corner pre-h margin is `-5/2`, and every one gains a positive
combination of u and v.  Therefore equality is strict in the open quadrant.
For eta below `5/2`, a sufficiently small positive u,v makes an actual
displayed term subtarget.

This is the first point at which the next correction cannot be scalar in the
h-linear multiplier: it must allow h times a linear Q multiplier.  The next
filtered system has 24 candidate columns `h*qj*E_i(0)` and the complete
Q-squared-R target above.

## Dual AWS custody

- Box03 forward tag
  `max12_912_order3_d1_double_root_control2_h2_qr_syzygy_lift_v7_20260826T041700Z_box03_forward`,
  PID `156418`: rc 0, empty stderr, 21,980 KiB maximum RSS, zero swap; JSON
  SHA `b2447171490a4b3cd4988bd0be4f603ac94d2bbb23725d7b9a1b36ec8597b296`.
- r6d reverse tag
  `max12_912_order3_d1_double_root_control2_h2_qr_syzygy_lift_v7_20260826T041700Z_r6d_reverse`,
  PID `223926`: rc 0, empty stderr, 22,104 KiB maximum RSS, zero swap; JSON
  SHA `fc80079508a69d76ebb6ca0adb2c9c7217a59eb2c0401a02123287eabe07d838`.

After deleting only tag/order custody fields, sorted semantic JSON is
identical with SHA

```text
788fa8defdca08edf0cad5f42fb85f2193dd1bc994af19e054e28395c20c8bf1.
```

Both runs used frozen source checks and 4-GiB / 900-s caps.

## Firewall

This is one scalar h-squared correction.  It does not prove completeness of
the next polynomial multiplier support, classify eta below `5/2`, give an
h-adic/formal lift, move source/load data, cover a fan, prove D1, or prove
JC2.
