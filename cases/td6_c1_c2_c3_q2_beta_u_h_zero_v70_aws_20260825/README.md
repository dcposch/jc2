# TD6 q2-beta raw `u-h-zero` and origin certificates (V70)

Frozen status: **producer-exact; hostile review pending.**

V70 is the raw repair of the localization debt identified in the V33/V69
`U=0` hostile review.  It starts again from original source rows at
`C=U=0`, retains polynomial beta and direct
`q_beta'=1+2 beta t+25 t^24`, and never specializes the V33 echelon through
`C=0`.

On `C=U=0,D(V)`, dual AWS runs produce transport rank `3470/3602`, two
transport events `-V,-V`, first-source denominator `V`, first rank `36/132`,
and a beta-degree-zero unit incompatibility at original row
`('X-2',14)`.  Its 14-row original-source replay and wrong-row control pass.
The complete certificate denominator is `V^3`, so this result is deliberately
limited to `D(V)`.

On the separately rebuilt origin, dual AWS runs produce transport rank
`3468/3602` and a beta-degree-zero unit incompatibility at original
transport row 6460, key `('g','X',-19,20)`, supported by 21 source rows.
There are no nonconstant transport events; the complete denominator is one.
Original-row replay and the wrong-row control pass.

With the corrected hostile-reviewed V33 theorem on `U=0,D(C)`, the three
raw pieces form a producer-exact cover of all `U=0`.  Promotion and every
dependent whole-H/B3/A3 composition remain quarantined pending hostile
review of this package.

## Replay

The source directory contains the V69 portable archive plus the V70 wrapper
and manifest.  Extract the archive on an AWS host, add `replay_v70.py` at
`jc2/cases/td6_c1_c2_c3_q2_beta_u_h_zero_v70_20260825/`, add
`V70_RUNBOOK.md` and `V70_SOURCE.sha256` at archive root, verify all recursive
source manifests, then run:

```sh
PYTHONHASHSEED=0 /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_beta_u_h_zero_v70_20260825/replay_v70.py \
  --stratum=u-h-zero

PYTHONHASHSEED=0 /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_beta_u_h_zero_v70_20260825/replay_v70.py \
  --stratum=origin
```

Append `--omit-direct-qprime` only for the frozen source-path controls.  Run
`python3 verify.py` for the lightweight evidence/custody audit.

No whole A3, other TD6 modulus, TD6, SP-2, landing, or JC2 claim is made.
