# V44 canonical raw H/B3 genuine-P12 / staged-N13 replay

Run only on AWS from the byte-identical archive, with a fixed Python hash
seed, after verifying inherited manifests and `V44_SOURCE.sha256`:

```sh
PYTHONHASHSEED=0 /usr/bin/time -v timeout 28800 \
  /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_full_p12_n13_unit_raw_canonical_20260825/replay.py \
  --stratum=h-zero > v44-h-zero.stdout 2> v44-h-zero.stderr

PYTHONHASHSEED=0 /usr/bin/time -v timeout 28800 \
  /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_full_p12_n13_unit_raw_canonical_20260825/replay.py \
  --stratum=b3-param > v44-b3-param.stdout 2> v44-b3-param.stderr
```

Run both lanes independently on r6d and Box03.  Promotion requires rc0 and
byte-identical canonical mathematical stdout for each matching stratum.
Compare the exact ranks, base P12 digest, beta tail, N13 multiplier, source
replay, denominator factors, and terminal canonical PASS marker.

V39's exact algebra and printed denominator-factor expressions remain useful,
but its imported digest helper hashed `repr(E3)` and thereby included process
object addresses in the first-stage pivot, beta-tail, N13-value, and
N13-multiplier SHA fields.  V44 serializes every E3 coefficient through its
18 exact rational coordinates before hashing.  Preserve V39 as a negative
custody control.

Each lane is still a fraction-field discriminator.  Every emitted raw
denominator/chart factor remains charged and must be recursively rebuilt;
neither lane alone closes its divisor or the fixed-A3 beta family.
