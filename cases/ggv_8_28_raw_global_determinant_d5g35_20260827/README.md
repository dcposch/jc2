# D5G35 complete raw determinant extension

This additive case extends the frozen D5G raw determinant from weights
`0..22` through the complete source-supported range `0..35`.  It works in

```text
C = Q[400 named positive-weight D3 raw slots],
C[X,t],
H = X^8-1,
F = H^2 + sum_(n=1)^14 t^n F_n,
G = H^3 + sum_(n=1)^21 t^n G_n.
```

`DIRECT_DETERMINANT_D0_D35.json` serializes all coefficients and every
pre-cancellation contribution of

```text
E = 12 F_X G - 8 F G_X - t(F_X G_t - F_t G_X)
  = sum_(n=0)^35 D_n t^n.
```

`TARGET_GATE.json` freezes, but does not solve, the coefficient equations

```text
D0=...=D21=0, D22=1, D23=...=D35=0.
```

The complete source census sharpens the nominal top weight: `D35` has two
opposite contributions and is identically zero, while `D34` is genuinely
nonzero.  See `STRUCTURAL_D35_ADDENDUM.md`.

## Exact replay

From this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B compile_d5g35.py --check \
  ../ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json \
  DIRECT_DETERMINANT_D0_D35.json TARGET_GATE.json RESULT.json
```

The replay pins all inputs, regenerates every determinant row and target
generator, byte-compares `D0..D22` with frozen D5G, checks the unchanged D22
certificate, independently recomputes all 36 rows in dense exact
`Q[X,t]/(t^36)` after a deterministic nonzero rational specialization of
all 400 slots, and checks the `D23+1` and `D24+1` mutations.

The corrected R7R1 interface recorded in `RESULT.json` is conditional and
provisional.  No target solution, specialization, landing, finite-tower,
face, family, or JC2 claim is made.
