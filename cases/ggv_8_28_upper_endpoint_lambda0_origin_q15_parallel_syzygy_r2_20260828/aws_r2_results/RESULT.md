# Inhomogeneous sparse syzygy r2 result

r2 replaced the false homogeneity assumption with the complete total-degree
Macaulay space: for bound `D=7`, every multiplier monomial of degree at most
`D-maxdeg(g_i)` is retained.  Desk controls and both AWS solver self-checks
passed.  Exact deduplication reproduced SHA-256
`eabe45db71777edc56f3b3d1717a6fd4f3f3c71c44fdf318d71a9babe3447a57`.

The two bounded modular systems completed exactly:

| subset | prime | columns | rows | rank | result artifact SHA-256 |
|---|---:|---:|---:|---:|---|
| G15, target-support multipliers | 65521 | 1,102 | 28,136 | 782 | `6a9316a7274141cc9b1d53182340de18d9813636c93b8714252b0d8c7d2df188` |
| full base, active-support multipliers | 65519 | 14,396 | 99,877 | 14,327 | `4fdd3d31d02c7086b7b303425704591d96fcba9fb82973f88ecbd6fb19150275` |

Both result artifacts say `NO_CERTIFICATE_IN_BOUNDED_ANSATZ`; neither contains
a coefficient certificate.  This rules out only membership representations
in the recorded degree-7 multiplier spaces.  It is not ideal nonmembership,
does not test higher degree, and is not a survivor or endpoint verdict.

Custody:

```text
256e2d9632dba36c5c406a45fe456a7915433a97fd0650dde450ce3df6f5e5e0  g15 archive, 106 files replayed
dfab446368aece730ed92b1fccba93ce999550b5b594db8f456516a4fa1e823a  full archive, 106 files replayed
a0db3c8ee95e35625328435a8bba21111b21d31ffba7669c4de6052b83cf5efe  g15 final census
12be5971e755073c8eccfbffbe177ec7e4495cd0dc3762807affcad8cb04345e  full final census
f44bad25107e57621fc3688f415a38b4ecc45203fa7760877363c74458af00c0  g15 evidence manifest
7599d893d0daf0e93ad3fed171de974dd6339f1a49bd7d1f86c0b1f90ff299ba  full evidence manifest
```

All stages exited zero, each final census contains no member and zero swap,
and no exact-Q computation ran.  No claim about the unrestricted lambda-zero
slice, branch P, JC2, HENS-CT, or `jc2-lean` is in scope.

