# Fable5 hostile review: r3 fixed-even `Q=X` endpoint-zero theorem

Independent desk audit (2026-08-28) of the charged frozen target

- `xmodel/ggv-upper-endpoint-deep-q1-lambda0-qx-fixed-even-endpoint-zero-r3-sol-ultra-20260828.md`
- `cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_qx_fixed_even_endpoint_zero_20260828/verify_qx_fixed_even_endpoint_zero.py`

Verdict: **PASS WITH ONE PRECISION REPAIR (theorem CONFIRMED)**.

- All producer bytes preserved; neither producer checker imported or
  executed. Frozen hashes verified at start and end (see `SOURCE.sha256`).
- Fresh standalone checker (fresh gate derivation from
  `(F/F0)^((n+2)/8)` via an ODE recurrence, `N/A^k` Laurent layer,
  windows re-extracted from `RAW_INPUT.json`):
  `xmodel/ggv-upper-endpoint-deep-q1-lambda0-qx-fixed-even-endpoint-zero-r3-hostile-review-fable5-20260828-check.py`
- Full report:
  `xmodel/ggv-upper-endpoint-deep-q1-lambda0-qx-fixed-even-endpoint-zero-r3-hostile-review-fable5-20260828.md`
- Machine summary: `RESULT.json`. Output hashes: `EVIDENCE.sha256`.

Precision repair (no verdict impact): report lines 94–95 — "modes born
after weight 10 have not entered by `G15`" is literally false for `c12`
(born at `G12`, constant load) and `c14` (born at `G14`, `A^-1` carrier);
their loads on the four audited coordinates are zero for three distinct,
now-computed reasons, which is all the theorem needs. Matching loose
producer-checker lines 252–254.

Replay:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  xmodel/ggv-upper-endpoint-deep-q1-lambda0-qx-fixed-even-endpoint-zero-r3-hostile-review-fable5-20260828-check.py
```
