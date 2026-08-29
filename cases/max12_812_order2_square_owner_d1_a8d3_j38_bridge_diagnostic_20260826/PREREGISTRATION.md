# Preregistration: `a=8,d=3` grade-38 bridge diagnostic

Date: 2026-08-26

Status: **FAILURE LOCALIZATION ONLY; NO EMPTINESS OR SURVIVAL VERDICT.**

The unchanged complete V2 producer has now returned engine rc 0 but a failed
all-seven-row bridge in both good characteristics `65519,65521`.  This
diagnostic wraps the frozen compiler, changes no source formula, and replaces
each Boolean bridge test by an explicitly retained residual modulo
`sigma^39`.  For each row it reports:

```text
bridge flag, earliest sigma valuation, number of monomials in that
coefficient, and its leading monomial.
```

It quits immediately after the seven bridge diagnostics.  First run
`F_65519` on Box03 at high memory; exact-Q replay follows only if the modular
residual does not already identify a source-emitter defect.  The input
producer remains frozen and its original failures remain immutable.

This is a diagnostic of the proposed `a=8,d=3` grade-38 order-three route,
not evidence that the source cell is nonempty.  It cannot affect the passing
`a=9` cells or any promoted theorem.
