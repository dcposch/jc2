# First graded transverse-cusp Q-R syzygy lift

Date: 2026-08-26 UTC

Status: **DUAL-AWS EXACT GRADED LIFT; hostile review pending.**

Starting from the reviewed q2-corrected multipliers, the first h-linear
coefficient has exactly eight worst Q-R terms, canonical SHA

```text
52bc344149c71253a551134e23b5b8f0008e2bd15b6424f13862d2742acfa27b.
```

On the closed corner `alpha=15/2,beta=delta=5`, every one has normalized
pre-h margin `-15/2`.  Exact RREF of their complete monomial coefficient
system against the Q-R components of all eight `h=0` rows has rank 3 and the
canonical free-zero solution

```text
(g1,g2,g3,g4,g5,g6,g7,g8)
  = (11/6,-11/12,0,0,0,0,0,0).
```

Thus set

```text
F1''=F1'+(11/6)h,
F2''=F2'-(11/12)h,
Fi''=Fi' for i>=3.
```

The exact corrected identity `W_h'=sum_i F_i'' E_i(h)` specializes at
`h=0` to the reviewed 37-term q2 witness, and its complete h-linear Q-R
component is zero.  Both traversals give the same 90-term corrected
polynomial, canonical SHA

```text
a4d11309d1f2195a1908c5ba0c4f36935b1c2c48170e30775b8372a4bd20621d.
```

The corrected h-linear coefficient has 37 terms and SHA

```text
c05f2603d0137a91ea8962af46064d08fdb609e7d8c61122c5036cc515119c83.
```

## New exact eta range

On

```text
alpha=15/2, beta=5+u, delta=5+v, u>0, v>0, T>0,
```

the new witness has unique least term `la^20` uniformly in the open
`u,v` quadrant exactly for

```text
eta>5.
```

The infimum is 5, but equality is not strict: at `eta=5` the following five
h-linear terms tie with the target independently of `u,v`:

```text
-17/54 h*r2^2 + 4/9 h*r1*r2 - 1/18 h*r1^2
-1/9 h*r0*r2 + 4/27 h*r0*r1.
```

Additional h-linear Q-cubic terms reach the closed `u=v=0` corner at the
same eta, but gain a positive Q-slope in the open quadrant.  For `eta<5`,
the displayed R-square terms themselves lie below target, so the same
witness cannot give a uniform exclusion there.

This exact correction improves the unchanged-witness range
`eta>=15/2` to `eta>5`.  The equality face and `0<eta<=5` require the next
graded row-module correction or a full face saturation; they are not branch
survivors.

## Dual AWS custody

- Box03 forward, tag
  `max12_912_order3_d1_double_root_control2_h_qr_syzygy_lift_v5_20260826T035900Z_box03_forward`,
  worker PID `154388`: rc 0, empty stderr, 22,544 KiB maximum RSS, zero
  swap; certificate SHA
  `2741a8e2536b7315f524747b2902be0afdc383bb4095e2d854592cc2d481667b`.
- r6d reverse, tag
  `max12_912_order3_d1_double_root_control2_h_qr_syzygy_lift_v5_20260826T035900Z_r6d_reverse`,
  worker PID `222147`: rc 0, empty stderr, 22,584 KiB maximum RSS, zero
  swap; certificate SHA
  `92573ef289aa3484e0b35019c0335ebdae48531759fe6fc7c69d40ade12c2350`.

The JSON bytes differ only in registered tag and traversal-order custody
fields.  Removing those two fields gives literally identical sorted JSON,
SHA

```text
4726e9ae886c2b9aef35ed0e48e04229e6b8b1e576fca506ef39e4e2dc49f8fe.
```

Both runs were registered before GO under 4-GiB / 900-s caps and passed the
same frozen source manifest.

## Firewall

This is one scalar h-correction of the worst Q-R graded piece.  It does not
prove an h-adic lift, classify `eta<=5`, saturate the eta=5 face, move the
axis or loads, cover another normal coordinate or support, classify the
whole double-root fan, prove D1, or prove JC2.
