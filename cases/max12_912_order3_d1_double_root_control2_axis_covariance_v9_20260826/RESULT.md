# Result: exact unit-axis transport of the V8 witness

Date: 2026-08-26 UTC

Status: **PRODUCER-TIER EXACT DUAL-AWS RESULT; HOSTILE REVIEW REQUIRED.**

## Universal coordinate identity

Put

```text
p=-3a^2,  c=2a^3+h.
```

Both exact AWS encodings verify, coefficient by coefficient and including
the fixed row-3 and row-8 targets, that

```text
E_i(a,h,Q,R,Lambda,rho,tau)
 = a^(12+i) E_i(1,h/a^3,
                 q2/a^4,q1/a^5,q0/a^6,
                 r2/a^7,r1/a^8,r0/a^9,
                 Lambda/a,rho/a,tau).
```

Here `k,mu,nu` are unchanged and specialized to the frozen loads
`k=nu=0, mu=2/3`.  All eight source rows pass this identity.  Their ordinary
source weights are exactly `12+i`.

Let `F_i` be the literal V8 multipliers, including all reviewed q2, h,
h-squared, and hQ corrections.  The smallest common denominator of the
transported multipliers `a^(8-i)F_i(hat variables)` is exactly `a^3`.
After clearing it, the dual-AWS compiler proves the polynomial identity

```text
sum_i a^(11-i) F_i(hat variables) E_i(a,h,Q,R)
     = a^23 W_V8(hat variables).
```

Both sides are one 48-term polynomial of canonical SHA

```text
53cf4b656c4415324a74862ec108b902ac8eade22733b2cb3a58cd3e447491e0.
```

Its `a=1` specialization is the frozen V8 witness SHA
`e549fd6879763d9f6804b9fcc17327e114bd54e29180246cc0b2e7c632fff38b`.
The distinguished terms are exactly coefficient-one
`a^3*Lambda^20` and coefficient-one `a^3*Lambda^20*tau`.

The same source reconstruction verifies

```text
Delta=-4p^3-27c^2=-27h(4a^3+h),
```

with canonical SHA
`e0afed585954d2dc9df4250499dd25d699e956a5e4ba990a7427ff9fd5ca726a`.

## Provisional mathematical consequence

On `D(a)`, the common factor `a^3` is a unit.  Coordinate scaling therefore
transports the full V8 initial-term theorem, not just its three filtered
grades, to every chosen unit-axis point of the smooth discriminant chart.
Equivalently, after the etale coordinate choice
`p=-3a^2,c=2a^3+h`, the reviewed V8 inequalities apply to the normalized
variables displayed above.  For an arc centered at `h=0` with `a` a unit,
`4a^3+h` is a unit and hence `v(Delta)=v(h)`.

The elementary coordinate map `(a,h)->(p,c)` has Jacobian determinant
`-6a`, so it is etale on `D(a)`.  Passing from the chosen-a chart back to the
smooth discriminant locus additionally uses faithful-flat/etale descent of
the nonexistence or unit-initial-ideal conclusion; hostile review must charge
that step before promotion.

## Dual custody

| Host | Tag | Worker PID | Order | JSON SHA | Elapsed / max RSS / swaps |
|---|---|---:|---|---|---|
| Box03 `98.80.65.144` | `max12_912_order3_d1_double_root_control2_axis_covariance_v9_20260826T044900Z_box03_forward` | 162034 | forward | `b74c8609fad7910c00766a7b7758e51cda0242c358f1d6d9cb161385ebcf42aa` | 6.12 s / 22,936 KiB / 0 |
| r6d `100.26.198.153` | `max12_912_order3_d1_double_root_control2_axis_covariance_v9_20260826T044900Z_r6d_reverse` | 229414 | reverse | `31be54bd064e652c539afb1fffa8267341e895b3a07fe506437fc995a7a1cd04` | 6.04 s / 22,504 KiB / 0 |

Both runs have rc 0, empty compiler stderr, exactly one PASS endpoint, and
successful source-closure checks.  Deleting only the preregistered `tag` and
`order` fields gives identical sorted certificates of SHA

```text
1375bd72024baefab039da3afc7d84c0ad76604df3dbc3cc60e6ed6e935d5e72.
```

## Firewall

This is a coordinate-action identity over the chosen `a` chart, with fixed
loads and frozen charged source.  Its target is `a^3*Lambda^20` before
localization.  It does not make `Lambda^20` an unlocalized initial monomial
at `a=0`, does not cover the triple-root point, moving loads, another source
chart, or a global landing theorem, and does not prove D1 or JC2.  Positive
axis valuation requires a separate weighted-cone analysis; only unit-axis
transport is claimed here.
