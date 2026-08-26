# Exact LPDP `la^20` preimage witness

Status: **producer-exact, independently ordered cone replay still running,
hostile review pending**.

## Endpoint

The registered r6d LPDP V2 run completed rc `0`, with empty compiler/CAS
stderr, empty hardened stdout-diagnostic file, and every required exact
identity marker. It found one used saturation generator and checked

```text
s^96*la^20 - s^97*TAIL = sum_{i=1}^9 FINAL[i]*I[i]
```

as a literal zero-polynomial identity for the frozen expanded
`I=(E1,...,E8,LT)`. Therefore, after `s=1`, the dehomogenized ideal contains

```text
W = la^20*tau + la^20
  + (1/243)*q1*q0^3
  + (1/54)*q1*r2*r1
  + (7/108)*q1*r1^2
  + (1/54)*q1*r2*r0
  - (1/54)*q0*r1*r0
  + (1/108)*q1*r0^2.
```

Equivalently, a primitive integral witness is

```text
W_Z = 972*la^20*tau + 972*la^20
    + 4*q1*q0^3
    + 18*q1*r2*r1
    + 63*q1*r1^2
    + 18*q1*r2*r0
    - 18*q0*r1*r0
    + 9*q1*r0^2.
```

The exponent `96` is used only to lift the saturated generator back to the
original Rees equations. It disappears on dehomogenization and is not claimed
minimal. The separately registered V3 race searches for a smaller individual
exponent but is not needed for the displayed ideal-membership theorem.

## Fixed-weight consequence

At

```text
w(la,tau,rho,q1,q0,r2,r1,r0)=(4,1,1,22,22,30,30,30),
```

the eight displayed monomials have respective weights

```text
81, 80, 88, 82, 82, 82, 82, 82.
```

Thus `la^20` is the unique least-weight term of this exact witness. This
recovers the fixed-weight monomial obstruction from the earlier corrected-A
special-fibre computation by an explicit preimage in the original nine Rees
generators.

## Custody

- AWS host/tag: r6d,
  `max12_912_order3_d1_double_root_control2_la20_syzygy_v2_20260826T021500Z_r6d_LPDP`
- worker/Singular: PID `206223` / completed child `206404`
- compiled source SHA-256:
  `e9b2c1594460cc8a6053654f0fcd810522044c6b1ef89d6e92ec2fb0038fd894`
- stdout SHA-256:
  `a0611ede0e667d45f569a954fdaa73818f0ebea328212b8c46d4ccb0aa29fe08`
- stdout diagnostics and stderr: empty, SHA-256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- wall/max RSS: `13:21.79` / `13115180` KiB; no swap
- harvested directory: `aws_r6d_LPDP/`; its `result.sha256` verifies all
  compiler/solver payloads.

## Firewall

This is a fixed-source witness for

```text
a=1, h=q2=k=nu=0, mu=2/3
```

and the charged nine-generator finite Rees ideal. It does not move the axis or
loads, cover another support, prove completeness of a Newton fan, settle all
double-root directions, D1, or JC2.
