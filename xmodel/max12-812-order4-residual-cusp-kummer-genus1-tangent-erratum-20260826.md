# Nonmutating tangent-coordinate erratum — order-four residual cusp

Date: 2026-08-26 02:05Z

Status: **EXACT WORDING CORRECTION; NO CHANGE TO THE PROMOTED PLANE THEOREM**

The immutable producer
`xmodel/max12-812-order4-residual-cusp-kummer-genus1-gate-20260826.md`
(SHA-256
`cd6c37c145e325a48dbf382453bde4c727b98a576897d10a1f9b3752ebdd1756`)
writes the repeated top tangent as

```text
w=(1/52488) Q^3+...
```

while naming `Q=q+4/27`.  The coefficient `1/52488` belongs instead to
`l_B^3`, where `l_B=27Q`.  In the named `Q` coordinate the exact statement is

```text
w=(1/52488) l_B^3+...=(3/8) Q^3+....
```

Equivalently, if `Q=tau^2*(unit)`, the producer's displayed coefficient of
`tau^6` must absorb the cube of that unit; only its nonvanishing and order are
used.

The independent hostile review
`xmodel/max12-812-order4-residual-cusp-kummer-genus1-review-grok-20260826.md`
(SHA-256
`59fb338533ff47a25d00893684caa3076bb7bb7bc2a43ab788cabbc0eb932c6a`)
rederived this conversion and returned `CONFIRMED`.  The correction changes
none of the following: one branch of type `(2,7)`, delta three,
`ord(v)=-6`, `g(X)=0`, the complete divisor
`div_X(v)=8P_0-P_ul-P_A-6P_B`, or `g(Y)=1` for `Y:y^4=v`.

The producer remains byte-immutable so its review pin stays valid.  This file
supersedes only the two displayed tangent-coefficient sentences in producer
sections 2.3 and 2.4.
