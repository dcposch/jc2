# V46 exact first-band incompatibility on V=0, C=-U^2

Run only on AWS with a fixed Python hash seed after verifying every inherited
manifest and `V46_SOURCE.sha256`:

```sh
PYTHONHASHSEED=0 /usr/bin/time -v timeout 28800 \
  /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_cplus1_first_incompatibility_canonical_20260825/replay.py \
  --stratum=v-cplus1-zero > v46.stdout 2> v46.stderr
```

The V45 P12 harness expected first rank 38 and therefore failed closed when
this specialization instead produced rank 37 plus a dependent row.  V46
retains that exact row ancestry, computes the polynomial-beta compatibility
ideal and its Bezout certificate, requires monic gcd one, and audits every
certificate denominator.  PASS licenses the rational line off its emitted
denominator only; combine parameter zero only with the separately frozen
all-beta U=0 theorem.
