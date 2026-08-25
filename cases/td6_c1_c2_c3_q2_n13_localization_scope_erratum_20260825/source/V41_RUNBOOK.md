# V41 compact clean generic N13 replay

Run only on AWS after verifying inherited manifests and
`V41_SOURCE.sha256`.  Launch the primary and omission control independently:

```sh
/usr/bin/time -v timeout 28800 \
  /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_n13_compact_20260825/replay.py \
  > v41-generic.stdout 2> v41-generic.stderr

/usr/bin/time -v timeout 28800 \
  /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_n13_compact_20260825/replay.py \
  --omit-direct-qprime > v41-omit.stdout 2> v41-omit.stderr
```

V41 changes no transport, row, pivot, compatibility, or source-replay
mathematics from V34.  It replaces only the enormous literal/factorized
denominator reporters with exact `(degree, term count, SHA256)` summaries and
a nonzero assertion.  This avoids a post-math formatting/factorization tail
while preserving the complete denominator polynomial by deterministic hash.

Primary PASS still proves only the generic fraction-field identity
`N13=(k/25)*beta` with staged original-row ancestry.  The omission control
must differ source-visibly and carries no positive mathematical claim.  All
denominator divisors remain charged; compact reporting is not denominator
elimination and licenses no global family conclusion.
