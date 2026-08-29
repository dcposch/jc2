# Preregistration: repaired total-Rees `T-rs` rho-unit certificate V13

Date: 2026-08-26

Status: **SOURCE-FROZEN REPAIR OF V12'S TOTAL-ROW VALUATION.  ACTUAL
`D_+(rs)` PREFIX ON `D(k)` ONLY; NO BROADER VERDICT.**

V13 imports the frozen V12 compiler byte-for-byte and changes only:

```text
P3 = Tg10_3/rs                         (not /rs^2),
rs*P3 = Tg10_3                         multiplication back,
8192*qcs*P3                            (not 8192*rs*qcs*P3)
```

in the certificate and both negative controls.  This follows the total-row
valuation already printed by V11.  All other V12 input pins, four-term
correction, definitions

```text
V=8*rho^2*qcs^2+3,
U=1+32*rho^2*qcs^2*V,
```

and required saturation/localization checks remain unchanged.  The repaired
identity is

```text
35*rs^2*k*U
 = 32768*P126 + 4096*P2 + 8192*qcs*P3
   + 12288*rho^2*qcs*P1.
```

Exact Q with `elim.lib` saturation and F65521 with inverse-variable
elimination must both pass, including coefficientwise source comparison,
four multiplication-back identities, two nonzero negative controls,
`35*k*U in J`, `k in J+(rho)`, an explicit inverse for rho on `D(k)`, and
the unit ideal after adjoining `(rho,1-v*k)`.

A PASS has exactly the narrow meaning stated in V12: it closes the complete
grade-12 `T-rs` Gate-T prefix on `D(k)`.  It does not cover `k=0`, any other
Rees chart or order-two component, maximum twelve, or JC2.
