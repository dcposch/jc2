# TD6 global-compatibility report — formatting erratum

Date: 2026-08-24  
Status: **FROZEN TYPOGRAPHY CORRECTION / NO MATHEMATICAL CHANGE**

The frozen producer report
`xmodel/td6-global-compatibility-gate-20260824.md` has two LaTeX-only slips:

1. In both lines of displayed equation (8), raw `-left(` means `-\left(`.
2. The display containing equation (10) is missing its closing `\]`.

With the missing backslashes restored, equation (8) reads

```text
f6 = T^15 + (1/3)x^3 - (T + (25/27)T^9)x^6,
g6 = T + T^25 + (5/9)T^10 x^3
     - ((5/3)T^11 + (125/81)T^19)x^6.
```

These are exactly the polynomials used by
`cases/td6_global_compatibility_20260824/replay.py`. The different-model
review independently recovered the same coefficients and confirmed every
Jacobian, rectangle, valuation, and recursion claim. The byte-frozen producer
report is preserved for provenance; no mathematical statement or verdict is
changed.
