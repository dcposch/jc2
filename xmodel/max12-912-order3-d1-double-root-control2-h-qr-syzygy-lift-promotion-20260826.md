# D1 control-2 first transverse-cusp Q-R lift promotion

Date: 2026-08-26

Status: **PROMOTED EXACT FIXED-CHART WEIGHT THEOREM.**

The dual-AWS producer

```text
c9469bb0041ba34e16732e33b3944f04217009f35473275429b708fc060d680e
  cases/max12_912_order3_d1_double_root_control2_h_qr_syzygy_lift_v5_20260826/RESULT.md
```

with freeze SHA

```text
f166e2ba9aa8e2c4715f14a4f29ed7dd4296755ed5de551de94784be3e911471
  cases/max12_912_order3_d1_double_root_control2_h_qr_syzygy_lift_v5_20260826/FREEZE.sha256
```

has hostile independent review

```text
7ac62c8bd0667340aab5fcdd4d6d35b5e184536fb6e9f5c98f6c9955fdea54c7
  xmodel/max12-912-order3-d1-double-root-control2-h-qr-syzygy-lift-review-grok-20260826.md
```

with verdict `H_QR_SYZYGY_LIFT_CONFIRMED` and no load-bearing repair.

## Promoted statement

In the pinned ordinary-tail eight-row module at
`a=1, p=-3, c=2+h, k=nu=0, mu=2/3`, with full Q and R support and the
reviewed q2-corrected multipliers, the scalar correction

```text
F1 -> F1 + (11/6)h,
F2 -> F2 - (11/12)h
```

produces an exact 90-term polynomial identity whose `h=0` slice is the
reviewed q2 witness and whose complete `h`-linear Q-R component vanishes.
Normalize `wt(la)=L`, put `alpha=15/2`, `beta=5+u`, `delta=5+v`, and
`eta=wt(h)/L`.  On `u>0`, `v>0`, and `T>0`, this corrected polynomial has
unique least-weight term `la^20` for every such point if and only if
`eta>5`.

At `eta=5`, five present `h r^2` terms tie the target.  For `0<eta<5`,
those terms lie below it.  These faces are unresolved next-lift problems,
not branch survivors.

## Firewall

This promotion does not assert scalar-support completeness, an `h`-adic or
formal lift, moving axis or moving loads, another normal direction, the
whole double-root fan, D1, or JC2.  Later reviewed lifts may enlarge the
certified `eta` range, but they do not alter this exact fixed-chart theorem.
