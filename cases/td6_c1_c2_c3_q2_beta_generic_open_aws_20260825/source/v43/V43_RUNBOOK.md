# V43 canonical generic P12/N13 replay

Run only on AWS, with a fixed Python hash seed, after verifying inherited
manifests and `V43_SOURCE.sha256`:

```sh
PYTHONHASHSEED=0 /usr/bin/time -v timeout 28800 \
  /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_full_p12_n13_unit_canonical_20260825/replay.py \
  > v43.stdout 2> v43.stderr
```

Run the byte-identical archive independently on r6d and Box03.  Promotion
requires both rc0, identical canonical mathematical stdout, and agreement on
the base P12, beta tail, N13 multiplier, ranks, denominators, and terminal
`TD6-A3-Q2-FULL-P12-N13-UNIT-CANONICAL PASS` marker.

V37's algebra and base P12 digest were exact, but its imported digest helper
hashed `repr(E3)` and `E3` has no custom `__repr__`; affected SHA fields thus
contained process object addresses.  V43 recursively serializes every E3
coefficient by its 18 exact `(numerator,denominator)` coordinates and
overrides the imported stage digest before any calculation.  Old V37/V39
hashes are custody-only negative controls and are not expected to match.

Scope is unchanged: the result covers only `D(U*H*B3)` and consumes the
separate staged N13 certificate.  Raw divisors and all global claims remain
excluded.
