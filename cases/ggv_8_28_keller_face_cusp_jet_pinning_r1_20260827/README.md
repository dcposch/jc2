# `8_28` Keller-face cusp-jet pinning R1

This additive case repairs the local-versus-raw type boundary of the frozen
R0 control.  It derives the exact raw `2S/3S` coefficient slices and proves
that the rootwise fixture `U_14=X` is not itself a raw polynomial-source
coefficient.

It also verifies that both minimal normalized unit-carrier ansatzes land in

```text
M(Y)=4*(X^8-1)*Y' + 48*X^7*Y.
```

No polynomial `Y` maps to `1`; the `V_8 U_14` fixture maps to
`1+(13/12)(X^8-1)`, and the alternative `U_11^2` carrier has the same image
obstruction.  Completeness of these two normalized cases for every raw jet is
explicitly open, so no face or family exclusion is claimed.

Replay from repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_keller_face_cusp_jet_pinning_r1_20260827/verify_r1.py
```
