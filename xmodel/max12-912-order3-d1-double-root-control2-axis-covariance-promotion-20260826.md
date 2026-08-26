# Promotion: exact unit-axis covariance of the V8 witness

Date: 2026-08-26 UTC

Status: **PROMOTED AT THE FIXED-LOAD UNIT-AXIS SCOPE BELOW.**

Pinned evidence:

```text
a061aea2bab3abcd9a8e88a3e86f18de233f46515cd2965bafa79ff1516642e2  cases/max12_912_order3_d1_double_root_control2_axis_covariance_v9_20260826/RESULT.md
003788e80c359fa715d799f3fe66a35929b105c772d139865e87f123c1a9bda2  cases/max12_912_order3_d1_double_root_control2_axis_covariance_v9_20260826/FREEZE.sha256
f81c5b054c2ff331176bd39005ad8f826b92efbfd5e16b1f7f20ae7dcbab7226  xmodel/max12-912-order3-d1-double-root-control2-axis-covariance-review-grok-20260826.md
```

The hostile review verdict is `UNIT_AXIS_COVARIANCE_CONFIRMED`.  For the
frozen ordinary-tail eight-row source and fixed loads
`k=nu=0, mu=2/3`, the literal promoted V8 multipliers satisfy all eight
coordinate-covariance identities at

```text
p=-3a^2,  c=2a^3+h.
```

Their minimal common negative axis character is exactly `-3`.  After the
minimal clearing by `a^3`, the exact identity is

```text
sum_i a^(11-i) F_i(hat variables) E_i(a,h,Q,R)
  = a^23 W_V8(hat variables),
```

with universal 48-term polynomial SHA
`53cf4b656c4415324a74862ec108b902ac8eade22733b2cb3a58cd3e447491e0`.
Its distinguished terms are coefficient-one `a^3*Lambda^20` and
coefficient-one `a^3*Lambda^20*tau`.  On `D(a)`, `a^3` is a unit, the
normalized hat-coordinate change is invertible, and the reviewed V8
unique-least-term obstruction transports to the smooth double-root
discriminant chart.  The chart has

```text
Delta=-27h(4a^3+h),       det d(p,c)/d(a,h)=-6a.
```

Firewall: this promotion requires `a` to be a unit, equivalently
`v(a)=0`, and uses the fixed loads and frozen V8 cone.  The review's phrase
“positive axis valuation is excluded” means **excluded from the licensed
scope**, not mathematically ruled out.  No claim is promoted for `v(a)>0`,
the triple-root point, moving loads, another source chart or normal
direction, the whole double-root fan, D1, or JC2.
