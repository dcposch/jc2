# Registration: `p=0` odd-sheet terminal and Taylor receivers

Date: 2026-08-26

The frozen package launches three independent AWS-only lanes after the exact
grades eleven and twelve source identities have passed.

| mode | field | registered endpoint |
|---|---|---|
| `terminal` | `Q` | complete factor-DAG rows `13..38`, raw predecessor `F`, exact first target grades; no solve |
| `taylor0` | `Q` | all `P_0..P_8,Q_0..Q_12` invariant terms at `x=0`; `TYPED_WAITING_GATE_A` |
| `taylor1` | `F_65521` control | all `P_0..P_8,Q_0..Q_12` invariant terms at `x=1`; `TYPED_WAITING_GATE_A` |

The Taylor clients reconstruct the exact rational Faber source and retain
the rational coefficients even in the good-prime control.  They do not
substitute the odd-sheet variables for finite-branch germs.  Gate A is the
separate two-sided algebraization/overlap map of the design at SHA-256
`68ccd9f24318473039ce56e969915663df6bf538c5fcf72a98055f605daab4a0`.

Required terminal sentinels:

```text
P0_ODD_RECEIVER_SOURCE_HASHES=PASS
P0_ODD_RECEIVER_MODE=terminal
P0_ODD_RECEIVER_STATUS=PASS-P0-ODD-TERMINAL-RAW-DAG-TYPED
P0_ODD_RECEIVER_MATHEMATICAL_ENDPOINT=RAW_TYPED_NOT_SOLVED
```

Required Taylor sentinels replace the mode and status by the corresponding
`taylor0`/`taylor1` values and end exactly
`TYPED_WAITING_GATE_A`.  The validator rejects `PASS_TAYLOR`, `UNIT`,
`LIFT`, or `EMPTY` in either Taylor stdout.

No lane proves Gate A, finite regularity, a source lift, terminal emptiness,
the square branch, order two, `(8,12)`, maximum twelve, or JC2.
