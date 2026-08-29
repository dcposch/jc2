# Exact coefficient control for the nonzero-`k10` Padé lemma

Date: 2026-08-26

Status: **AWS EXACT-ARITHMETIC CONTROL PASS; COEFFICIENT IDENTITIES ONLY.**

The registered Box03 lane
`max12_812_order2_pade_coeff_verify_20260826T053600Z_box03` ran under PID
`166022`, a 300-second timeout, a 1-GiB virtual-memory cap, and zero swap.
It ended `rc=0` in 0.03 seconds with maximum RSS 12,736 KiB.  The validator
returned `PASS_EXACT_IDENTITIES`.

Starting only from the differential recurrence for

```text
(1+p*t^2+c*t^3+r*t^4)^(7/2)=sum a_n*t^n,
```

the custom rational multivariate checker verified, with
`d=p^2-4r`,

```text
a15=(7c/2048) A0,
a16=(35/32768) C0,
a17=(7c/4096) B0,

A0=-5d^3+40pc^2d-8c^4,
C0=d^4-48pc^2d^2+32c^4(d+2p^2),
B0=5pd^3-10c^2d(d+4p^2)+24pc^4.
```

It also verified the two exact reduction identities

```text
B0+p*A0=2c^2(-5d^2+8pc^2),

C0=76d^4+e1^2+4d^2*e1+16d*e2,
e1=8pc^2-5d^2,
e2=2c^4-5d^3.
```

Stdout SHA-256 is
`3bda1b3837800a4749a0ea51ae92605e16d2ba71d4f7961db3fca10da13434ba`;
stderr/time-metadata SHA-256 is
`e5ea1bb4a7a327959e02a5d3defc53b8d6e0dd8e106f7e8270f467f0e0e9bfe3`.
The frozen input manifest has SHA-256
`8e1acd1350f036a350ccd0e94bada440c360fa305c01d1a9271e824c9bd625af`.

This control verifies the finite expansions and contradiction arithmetic.
It does not by itself prove that first-tail vanishing forces these three
coefficients to vanish, classify a scheme or radical, construct/exclude a
strict arc, close order two, close `(8,12)`, prove maximum twelve, or prove
JC2.  Those logical steps belong in the separately reviewed theorem.
