# `8_28` Keller-face rational-mode exclusion R3

This additive case works in `K(X)[[t]]` and completely classifies the
homogeneous modes below the charged weight 22.  After subtracting

```text
F^(3/2), t^4*F, t^8*F^(1/2), t^12,
t^16*F^(-1/2), t^20*F^(-1),
```

the endpoint residual must satisfy

```text
E22=-20*H*H'*d-8*H^2*d'=1, H=X^8-1.
```

Pole regularity forces `d=-Y/(2H)`, reducing the endpoint to
`4HY'+6H'Y=1`; its leading-degree formula has no polynomial solution.

The result excludes only the exact squarefree `H^2/H^3` replacement edge.
It does not exclude the original non-Keller `8_28` witness or the whole GGV
family.

Replay from repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_keller_face_rational_mode_exclusion_r3_20260827/verify_r3.py
```
