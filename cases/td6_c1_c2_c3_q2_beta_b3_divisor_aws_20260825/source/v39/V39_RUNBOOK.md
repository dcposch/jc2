# V39 raw H/B3 genuine-P12 / staged-N13 discriminators

Run only on AWS after verifying all inherited manifests and
`V39_SOURCE.sha256`.  The two exact raw rebuilds are independent:

```sh
/usr/bin/time -v timeout 28800 \
  /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_full_p12_n13_unit_raw_20260825/replay.py \
  --stratum=h-zero > v39-h-zero.stdout 2> v39-h-zero.stderr

/usr/bin/time -v timeout 28800 \
  /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_full_p12_n13_unit_raw_20260825/replay.py \
  --stratum=b3-param > v39-b3-param.stdout 2> v39-b3-param.stderr
```

Each lane rebuilds transport, the polynomial-beta first band, and the
genuine pre-echelon P12 after the exact raw specialization.  It lifts P12
to the raw original first rows and combines its beta tail with the matching
V34 raw staged certificate `N13=(k/25)*beta`, without beta division.

These are fraction-field discriminators, not divisor closures.  Every
denominator factor is emitted and remains a mandatory raw sub-stratum.  The
B3 lane additionally replays the exact birational-chart audit, whose omitted
base/infinity loci remain charged.  Even PASS in both lanes does not license
the full fixed-A3 beta family until the union and all recursive factor loci
are proved exactly.
