# `8_28` Keller-face rootwise unit-carrier classification R2

This additive case proves, after root-local parametric Morse normalization,
that arbitrary higher-`u` terms in the cusp expansion do not introduce a
third constant-Jacobian carrier through weight 22.  At each simple root the
only possibilities are

```text
6*H'(c)*V8(c)*U14(c)=1       when V8(c) is nonzero;
(9/2)*H'(c)*U11(c)^2=1       when V8(c) is zero.
```

The two cases may occur on different etale/deck factors.  This is a
rootwise/formal classification only: raw polynomial provenance and the
complete global `E22` sidecar image remain open, so there is no `8_28` face
or family exclusion.

Replay from repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/verify_r2.py
```
