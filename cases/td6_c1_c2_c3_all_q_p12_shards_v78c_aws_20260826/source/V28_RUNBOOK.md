# V28 AWS runbook: generic A3 q2 `beta` dual adjoint

This archive adds one exact replay over
`E(C,V,U)[eps]/eps^2`, with `beta=eps` in
`q_beta=t+beta*t^2+t^25`.  It is a first-order discriminator on
`D(U*(C-3U^2)*B3)` only.

From the extracted archive root, first verify the full recursive closure:

```sh
sha256sum -c SOURCE.sha256
```

Then run on AWS with Python 3 and python-flint 0.9.0:

```sh
/usr/bin/time -v timeout 28800 python3 \
  jc2/cases/td6_c1_c2_c3_q2_beta_dual_20260825/replay.py \
  > beta-dual.stdout 2> beta-dual.stderr
```

The only success marker is:

```text
TD6-C1-C2-C3-Q2-BETA-DUAL-ADJOINT PASS
```

The replay must recover base ranks `3470/3602` and `38/132`, the genuine
2,893-term P12, the base remainder `-k/50`, and the 28-row/1,489-term
original-row lift.  It must retain both beta entry points: the `[t^2]g0`
transport right-hand side and `q_beta'=1+2 beta t+25t^24`.  It differentiates
the normalized first-band echelon and source multipliers, proves the full
dual original-row identity, and requires a nonzero lambda-prime omission
control.  Every base/derivative denominator radical must be contained in
`U*(C-3U^2)*B3`.

Even a nonzero sensitivity does not kill finite beta: a dual unit
`-k/50+eps*r` is only first-order rigidity.  Do not infer a neighborhood,
the four-parameter family, whole TD6, SP-2, or JC2.
