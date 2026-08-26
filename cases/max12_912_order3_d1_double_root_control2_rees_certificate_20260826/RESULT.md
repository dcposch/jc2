# Provisional exact monomial certificate

The registered r6d job completed with compiler rc zero, Singular rc zero,
empty compiler/CAS stderr, separated timing telemetry, and the two required
PASS markers.

The complete special-fibre standard basis has 35 elements.  Its last two are

```text
GH[34]=la^20
GH[35]=s
```

Thus `la^20` is a monomial in the full weighted initial ideal.  This is not a
test of the submitted generator initials: it is computed only after exact
contraction from `s!=0` and specialization `s=0`, so it includes all
S-polynomial consequences.  As an independent internal check,
`sat_with_exp(GH,<TORUS>)` is the unit ideal at exponent one and direct
reduction verifies `TORUS` itself belongs to `GH`; the original inverse-
variable torus localization independently returns the unit ideal.

Provisional consequence: no exact arc exists with the frozen axis,
`q2=k=nu=0`, `mu=2/3`, weight
`(4,1,1,22,22,30,30,30)`, and all eight displayed coordinates nonzero.
This does not exclude later moving-axis or `q2` corrections, other supports,
other weights/residues/loads, the full double-root fan, D1, or JC2.

Promotion awaits the independent factored/saturation A endpoint and hostile
source/certificate review.

AWS stdout SHA-256:

```text
d5317aacf229d85b7b550c40e85d2b7294cae99ba0dedf2e56c2064d4d9ec088
```

