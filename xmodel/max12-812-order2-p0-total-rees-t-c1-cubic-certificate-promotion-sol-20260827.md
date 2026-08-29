# Promotion — ordered actual-total `T-c1` cubic certificate

Date: 2026-08-27

Status: **PROMOTED FOR THE WHOLE ORDERED REGISTERED `T-c1` STRATUM.**

## Custody

- Producer:
  `xmodel/max12-812-order2-p0-total-rees-t-c1-cubic-certificate-producer-sol-20260827.md`,
  SHA-256
  `95117024a7f52dc5faaa968699bff7ff27d92c2f4ee7030c95f58d2ed02da69b`.
- Different-model hostile review:
  `xmodel/max12-812-order2-p0-total-rees-t-c1-cubic-certificate-hostile-review-grok-20260827.md`,
  SHA-256
  `40ea0ff329771620ed13b3e137c21679dd4aa47a72b3a798da92d4123671965d`.
- Literal-source rederivation of both consumed rows remains the earlier
  independent Fable5 review, SHA-256
  `139ecb673995eff3c19f72da54b7a79d0a2a4c9c01f3b8600935f855704066fb`.

## Promoted identity and theorem

For the exact actual-total V9 rows `Tg10_2,Tg10_4`, direct expansion gives

```text
c1^3
 = (32/3)c1*Tg10_2 - (128/3)a1*Tg10_4
   - rs*((5/2)rho^2 cs^2 k c1 + (5/96)rs^2 k c1)
   - c0*(4a0 c1 - 4a1 c0).                              (C1)
```

Equivalently, after multiplying by 96, this is an integral polynomial
identity.  It also reduces coefficientwise modulo 65521.

On the honest ordered fourth chart stratum for
`J1=(rs,cs,c0,c1)`, identity (C1) has reviewed staged-certificate type

```text
exceptional coordinate/power: c1^3
genuine localizer:            1
rho factor:                   1  (W=0)
source rows:                  Tg10_2,Tg10_4
ordered base equations used: rs,c0
```

The ordered stratum additionally has `cs=0`; not using that equation only
strengthens the certificate.  Kernel-as-saturation absorbs `c1^3`; `c1` is
never inverted or treated as a unit.  Thus the ordered registered
`T-c1` stratum is the zero ring for the entire total family, including
`rho != 0`, and has no localizer complement.

## Correction of the earlier residual ledger

The prior repairable Fable5 review correctly rejected the producer's claim
that `c1` itself was a chart-ring unit, but it stopped after the
`Tg10_2` relation and recorded

```text
V(c1) ∩ ordered T-c1 stratum ∩ V(rho)
```

as a residual.  That residual is withdrawn.  Its leftover
`4rho^2 a1 c1^2` is canceled exactly by the `Tg10_4` summand in (C1).
This changes neither the independently promoted `T-c0` theorem nor the
source-provenance work in that review.

## Firewall

This closes the ordered fourth `J1` stratum, not the unordered whole
standard chart as an independent object.  It proves nothing about `T-cs`,
the `k=0` siblings of other charts, either second-stage `a0/a1` chart, the
terminal receiver, the generic deck/square bridge, Gate T, order two,
maximum twelve, or JC2.
