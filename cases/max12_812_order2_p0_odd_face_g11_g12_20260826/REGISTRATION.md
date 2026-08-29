# Registration: p-zero odd-face grades eleven and twelve

Date: 2026-08-26

Run the complete seven-row charged source over exact `Q` on Box03 and an
independent `F_65521` control on r6d.  The registered collision cone is

```text
Lambda=sigma^2,
p=2*sigma*ell1+2*sigma^2*ell2,
R=cs0*z+sigma*(cs1*z+rs1/4)+sigma^2*(cs2*z+rs2/4),
A=A0+sigma*A1+sigma^2*A2,
C=sigma*E1+sigma^2*E2,
k10=k0+sigma*k1+sigma^2*k2c.
```

Both lanes are capped at 16 GiB.  The compiler and engine timeouts are 600
and 3600 seconds.  Exact-Q carries the characteristic-zero producer claim;
the good-prime lane is a separate software control only.

Acceptance requires exact source divisibility through grades eleven and
twelve, the moving-base Faber connection, the raw localized radical with its
last unprojected row, and the rational normalization/deck sentinels.  A
timeout, source mismatch, modular-only endpoint, missing sentinel, or
Singular diagnostic is no verdict.

Scope: one normalized collision cone on `D(cs0*k0)` only.  No terminal,
Taylor, fan-exhaustion, square-component, order-two, `(8,12)`,
maximum-twelve, or JC2 verdict.
