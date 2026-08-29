# D5N reviewed-local/direct-global naturality bridge

This case composes the reviewed D4R1 factor-local Morse compiler with the
reviewed D5G direct determinant, while retaining all lower-row Taylor terms
and the global `H`-quotient.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B verify_d5n.py --check RESULT.json
```

The PASS is a typed bridge and quotient-gate theorem.  It is not a gate
solution, target verdict, or face exclusion.
