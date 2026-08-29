# Result: typed terminal and Taylor receivers for the `p=0` odd sheet

Date: 2026-08-26

Status: **ALL THREE AWS VALIDATORS PASS; RAW/TYPED RECEIVERS ONLY.**

The exact-Q terminal lane reconstructed the complete frozen seven-tail
source after the odd-sheet normalization

```text
e1=b^2*w,       k0=(12/5)*w^2,       b*w!=0,
```

while retaining the unsolved predecessor row `F`, every primitive
correction, all three lower loads, all three constant targets, and `J`.
It emitted all `7*26=182` raw coefficients in grades `13..38` as a
487720-node commutative factor DAG.  The exact first target appearances are

```text
mu2_0 : row 2, grade 28, coefficient -1,
mu4_0 : row 4, grade 32, coefficient -1,
mu6_0 : row 6, grade 36, coefficient -1,
J0    : row 7, grade 38, coefficient -1/4.
```

This is the first complete terminal-infinity continuation of the odd sheet,
but the raw ideal has not been solved or localized.  Its endpoint is exactly
`RAW_TYPED_NOT_SOLVED`.

The two finite-branch lanes independently reconstructed the complete Faber
source and all seven frozen tails.  At each branch they emitted all nine
first-coordinate and thirteen second-coordinate Taylor expressions using
the invariant monomial formula in the frozen design.  Each manifest has 37
`P` terms and 428 `Q` terms; all character-parity and Faber-weight checks
pass.  The `x=0` lane is exact `Q`; the `x=1` lane retains the exact rational
coefficients and adds an `F_65521` control.

Both finite clients stop at `TYPED_WAITING_GATE_A`.  Gate A is still the
missing two-sided algebraization map from the coefficient-infinity odd sheet
to global rational functions `A_i(x),R0(x)` with compatible germs at
`x=0,1`.  Therefore these PASS results do not evaluate finite regularity,
prove a lift, or exclude the sheet.

Exact output hashes and remote custody paths are in `AWS_LAUNCH_METADATA.md`.
No claim about the whole square branch, order two, `(8,12)`, maximum twelve,
or JC2 follows.
