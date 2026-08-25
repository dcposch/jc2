# Nonmutating V77 q3 source-typing erratum

Date: 2026-08-25  
Status: **LOAD-BEARING QUARANTINE / FROZEN V77 BYTES UNCHANGED**

The frozen V77 producer source (SHA-256
`5e088d8c9b9f7f4f74de108c816f51e5f69d477572fa8b7ec0cf475efcb1ec22`)
sets, inside `configure_qd_gamma`,

```python
qd.B = EDual(0, 1)
```

while also setting the direct q3 derivative

```python
qd.Q_PRIME[2] = EDual(0, 3)
```

The imported compiler defines `B` specifically by
`q=t+B*t^2+t^25`: its source has `Q_PRIME[1]=2*B` and the q2 transport
boundary entry `{2:B}`.  Therefore a pure q3 tangent at beta=0 must set
`qd.B=EDual(0)` and vary only the original q3 transport RHS key plus
`Q_PRIME[2]`.  V77 instead injected a q2 downstream/Jacobian derivative
without the matching q2 transport-RHS derivative.  Its derivative object is
not the tangent of the claimed pure q3 source family.

Consequently every q3-specific V77 conclusion is quarantined: the first
minor derivative, raw/remainder gamma columns, lambda-prime identity,
dual-unit statement, derivative denominator audit, and the scheduling claim
drawn from them.  There is also a separate exact interpretation error:
`c0730fa1...`, printed for both the V77-gamma and V32-beta selected-minor
derivatives, is the canonical digest of the zero scalar (all 18 exact field
coordinates are `0/1`).  V77's prose statement that this derivative is
nonzero is therefore false even for its hybrid derivative calculation.

Only explicitly base-projected facts survive.  At gamma=0 the incorrect and
correct assignments both have `B=0`; hence V77's 3,470 transport rank,
38 first rank, 2,893-term base P12, base remainder `-k/50`, and exact base
source identity are unaffected.  Those facts were already inherited from
the fixed-A3 base and do not prove anything about q3.

The clean fix is a new immutable producer with `qd.B=0`, exact source key
`('g','X',0,3)`, direct term `3*gamma*t^2`, original-row replay, and omission
controls.  Frozen V77 files and its original report are not modified.

## Pinned custody

| object | SHA-256 |
|---|---|
| frozen V77 case manifest | `fdae8325583633ad9ab8571be2153a4ea9d418c50657bb61fcda8fd8f1d30bfc` |
| frozen V77 case freeze | `1d6a8f34dab858bdea5256e17fb52090b2282d50140aeab4fd6fedb671eef59b` |
| frozen V77 report | `53e590c3a22aad8333933d776aab50bed148d1918f50d124891d569437f2512d` |
| frozen V77 replay | `5e088d8c9b9f7f4f74de108c816f51e5f69d477572fa8b7ec0cf475efcb1ec22` |
| imported q2 compiler | `0ba184470dc051fad50640647c4b78ea869b8a4153219026b23abdcf0652d357` |

The zero-scalar interpretation was independently checked on AWS through the
pinned exact field serializer; no local exact-algebra computation was used.
