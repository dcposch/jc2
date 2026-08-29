# Result: K00 local-syzygy constant projection V16R1

Date: 2026-08-27

Status: **EXACT PRODUCER PASS; PROVISIONAL PENDING HOSTILE REVIEW.**

## Exact result

Put

```text
R = Q[d0,d1,d2,d3,d4,d5],  m=(d0,...,d5),
A = (r1,...,r7),
```

for the exact unloaded K00 rows at `C6=1`.  The complete frozen
87-generator polynomial module `S=syz(A)` was replayed coefficientwise.
Its origin-evaluation span in `Q^7` has exact rank one.  Every generator,
and hence the full span, has coordinates 2, 4, and 6 equal to zero.
The projection to coordinates `(6,7)` has rank one, not two.

An explicit base syzygy has origin vector

```text
(-200, 0, -960, 0, -5120, 0, -40960),
```

so its seventh coordinate is a unit in `R_m`.  A fresh second Singular
process, generated only from its seven serialized component files, replayed
the complete polynomial identity with literal residual `0`.

Consequently, for every local representation

```text
r7 = q1*r1 + ... + q6*r6  in R_m,
```

one has

```text
q2(0)=q4(0)=q6(0)=0.
```

This statement is representation-independent.  Indeed, any local syzygy
clears by a common denominator `s` with `s(0) != 0` to a polynomial
syzygy; origin evaluation is merely rescaled by the nonzero scalar `s(0)`.
Thus the complete polynomial-module evaluation controls all local
representation freedom.  The apparent unit `M6` freedom visible from the
quadratic initial relation `Q6=0` does not lift to a full local relation.

## Evidence

- Exact-Q branch: `M6_FORCED`.
- Exact evaluation rank: `1`; exact `(6,7)` projection rank: `1`.
- All 609 exact origin constants are serialized.
- Exact result JSON SHA256:
  `b6cd066a5d93fa81a4eb4217f44916969aa7b515b7e367befbe9018045a6d7ff`.
- Canonical exact 7x87 constant-matrix SHA256:
  `34640d1a2d9c2c4076b680ef5573dd8f1ceacb40c09caae918d6a0f12e32f791`.
- Fresh replay stdout SHA256:
  `3f4cfffe764b4df460100a8510b613750a3eab2e5af941fcc9e8434e4a1c21c4`.
- Literal-zero replay residual SHA256:
  `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`.
- The independent `p=65521` software control reached the same rank-one,
  coordinates-2/4/6-zero branch.  It is not evidence over Q.
- Engine time was below one second in each lane; exact peak RSS was about
  28 MiB; neither host used swap.

The original V16 run is separately preserved as a design failure: its
producer rejected the no-`M6`-freedom branch despite preregistering both
outcomes.  V16R1 used new immutable tags and a truly branch-neutral
producer.

## Firewall and successor

This is only an unloaded, order-zero, `C6=1` local-relation statement.  It
does **not** compute the first-order deformation class

```text
[b1 - phi1(q0)] in
(R/(r1,...,r6)) / im(Syz(phi0) -> R/(r1,...,r6)),
```

does not restrict that class to the honest load/`Lambda`/`Jdet` source
image, and is not a finite `Lambda<=19` reachability result, closure-first
incidence result, Taylor-realization result, order-two result, maximum-twelve
result, or JC2 result.  That representation-invariant first-order quotient
is the next mixed-lane discriminator.

