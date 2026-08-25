# V42 q_beta N13 exceptional-curve quotient gate

Run only on AWS.  Verify `SOURCE.sha256` and `V42_SOURCE.sha256`, then launch
the three independent component lanes:

```sh
/usr/bin/time -v timeout 28800 /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_n13_curve_quotient_20260825/replay.py \
  --component=p3 > p3.stdout 2> p3.stderr

/usr/bin/time -v timeout 28800 /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_n13_curve_quotient_20260825/replay.py \
  --component=b3tq > b3tq.stdout 2> b3tq.stderr

/usr/bin/time -v timeout 28800 /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_n13_curve_quotient_20260825/replay.py \
  --component=b3half > b3half.stdout 2> b3half.stderr
```

The optional `--omit-direct-qprime` form is a negative control and carries
no positive claim.  Each primary must end in
`TD6-A3-Q2-N13-CURVE PASS`, recover ranks `3470/3602`, `38/132`, `38/94`,
and `25/56`, and certify `N13=(k/25)*beta` with exact staged original-row
ancestry.

The imported coefficient towers and center maps are the byte-pinned frozen
fixed-beta curve producers: `p3` is the exact H=B3 function field;
`b3tq` is the B3 chart fibre `t^2-4t+2=0`; `b3half` is `t=1/2`.
No scaling normalization is introduced.

Every transport norm and staged denominator factor is emitted.  PASS is a
function-field result only.  To close a component, combine it with the
separately frozen beta-zero P12 theorem and raw-rebuild every emitted
parameter-zero/norm divisor.  No fixed-A3, whole-TD6, SP-2, or JC2 claim is
licensed by this package alone.
