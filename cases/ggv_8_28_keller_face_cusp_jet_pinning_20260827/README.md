# `8_28` Keller-face cusp-jet pinning control

This desk-scale case checks the exact `y`-infinity Jacobian recurrence for a
square/cube edge `F_0=H^2`, `G_0=H^3`, with `H=X^8-1` and the original
`(4,-1)` faces `B^2/B^3` retained.

It proves the bounded facts that `E_1=0` forces
`G_1=(3/2)HF_1`, `E_2=0` forces `H|F_1`, and the generic Keller fibre ODE
pins `g` finite.  It also constructs two exact formal cusp mutations through
`E_21=0`; both are rejected by the polynomial-source provenance check because
their required `G_16` terms include negative powers of `y`.

The case identifies the first rootwise cusp determinant map
`6 H'(c)V_8(c)U_14(c)=1`.  Its example leaves the explicit global remainder
`(13/12)H`, so no `E_22=1` polynomial lift is claimed.

Replay from repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/verify.py
```

Scope: one bounded formal/source-provenance control.  This is not a Keller
pair, a counterexample, a GGV-to-tree functor, or `G2-PSC`.
