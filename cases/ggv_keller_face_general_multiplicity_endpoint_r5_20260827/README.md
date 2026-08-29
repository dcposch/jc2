# General-multiplicity endpoint R5

This desk-scale case checks the arithmetic fixtures for the exact theorem in
`xmodel/ggv-keller-face-general-multiplicity-endpoint-r5-sol-20260827.md`.
Run:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B verify_r5.py
```

The verifier checks rational-mode schedules, their gcd formulation, the
degree-eight squarefree-part split, the normalized quadratic cokernel
condition, the cross-multiplied endpoint identity, and the perfect-square
positive control.  It is a regression harness, not the proof by itself.

