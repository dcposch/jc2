# V70 raw `C=U=0` q2-beta runbook

This wrapper pins V69 and adds only complete-localization display and a
wrong-row negative control.  Run from the extracted V69 payload root on AWS:

```sh
sha256sum -c SOURCE.sha256
sha256sum -c V31_SOURCE.sha256
sha256sum -c V33_SOURCE.sha256
sha256sum -c V69_SOURCE.sha256
python3 jc2/cases/td6_c1_c2_c3_q2_beta_u_h_zero_v70_20260825/replay_v70.py \
  --stratum=u-h-zero
```

Run the byte-identical source independently on Box02 and Box03 under a
12-GiB cap.  If the complete certificate has a nonconstant `V` factor, run
the separate raw `--stratum=origin` leaf; do not specialize through it.
`--omit-direct-qprime` is a source-path control and never broadens scope.
