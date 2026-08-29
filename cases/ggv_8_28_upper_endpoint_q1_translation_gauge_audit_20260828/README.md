# Active-q1 translation gauge audit

The formal shear `X -> X-(3 lambda/4)t` kills the active q1 weight-one
coefficients and exactly preserves the determinant operator and target
`t^22`.  It does **not** preserve the frozen lower-X raw windows.

Replay:

```bash
python3 -B verify_translation_gauge.py --check
```

The exact counterexamples are `F8=X`, which creates forbidden
`F9[X^0]`, and independently `G12=X`, which creates forbidden `G13[X^0]`.
No theorem that determinant solutions cancel these forbidden tails is known.
