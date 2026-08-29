# Producer result: normalized order-two square `r=1` receiver

Date: 2026-08-26

Status: **DUAL-AWS PRODUCER PASS; HOSTILE REVIEW REQUIRED BEFORE PROMOTION.**

## Endpoint

The frozen V15 package passed independently over exact Q on Box03 and
`F_65521` on r6d.  Both engines returned `rc=0`; both validators printed
`PASS_R1_V15_VALIDATOR_TELEMETRY_REPAIR`.  The marker-only stdout is
byte-identical across fields, SHA-256
`fc6ba5c3ec390a8aebf2991920cf8e05c63f64b275e253d79d3222eeac135dff`.
It contains all twelve required markers exactly once and no Singular `?`,
`// **`, `error occurred`, or `=FAIL` token.  The validation files are also
byte-identical, SHA-256
`c3a4c8e66bdf91563cd73c2f06524ec7b70334a90f57b5442d9c86d8a1a121e2`.

The exact-Q and finite-field Singular inputs have SHA-256

```text
0b1efd2f1db5938ea18d488787d2346a9c253688719db5d673425fc76be13296
d9aafc5304ccff369815814a2cbb8b6752b9754718c435ea2e29644d2708ca7c.
```

The complete downloaded evidence is frozen by `EVIDENCE.sha256`, SHA-256
`dc26e462ff415e9d6e8fc4c228e1f3012f0490e7ecf00b695e2348b9b709441b`.

## Producer statement

On the generic-square first-normal chart `D(p*k10)`, after the reviewed
half-weight support and `M=0` gates, assume

```text
ord_sigma(A)>=1,   ord_sigma(C)>=3,   ord_sigma(R)=1.
```

At absolute sigma grade thirteen, all seven complete frozen source rows are
the exact lower-unitriangular Faber image of

```text
(5/16)*k10*R0^3/L,          L=z^2+p/2,
```

and are independent of `k6,k2,mu2,mu4,mu6,J`.  Polynomiality forces the
remainder of `R0^3` modulo `L` to vanish.  The compiler checks the exact
remainder formula

```text
b1*(3*b0^2-(p/2)*b1^2)*z
 +b0*(b0^2-(3*p/2)*b1^2),
```

standardizes the localized radical before membership reduction, and verifies
that its reduced support on `D(p*k10)` is `(b0,b1)`.  Therefore the normalized
`r=1` leading section is empty: every such arc contact-raises `R` to order at
least two.

## Firewall

This is producer-tier, arcwise/set-theoretic elimination of the normalized
`r=1` receiver only.  It awaits hostile review.  It does not consume or
repair V12's quarantined unbounded `d=1` claim, and it does not cover
`p=0`, `k10=0`, positive-order loads, the exact zero section, terminal or
Taylor conditions, fan exhaustiveness, scheme structure, the whole square
branch, order two, `(8,12)`, maximum twelve, or JC2.  Exact Q is the
characteristic-zero producer; `F_65521` is a software control.
