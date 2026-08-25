# V45 canonical rational raw strata for the all-beta atlas

Run only on AWS with `PYTHONHASHSEED=0` after verifying inherited manifests
and `V45_SOURCE.sha256`.  Run the same producer separately with:

```sh
--stratum=v-h-zero
--stratum=v-cplus1-zero
--stratum=v-cplus5-zero
```

The first is the residual `V=0` branch inside `H=0`.  The latter two are the
two non-`U=0` branches of the exact factorization

```text
B3|_(V=0) = 4*U^2*(C+U^2)*(C+5*U^2).
```

For each invocation use `/usr/bin/time -v timeout 28800` and the Python at
`/home/ubuntu/venvs/td6/bin/python`, retaining stdout, stderr, rc, source
checks, environment versions, and output SHA256.  A PASS is only a
fraction-field result on that rational line; recurse every emitted
denominator factor.  The already frozen global `U=0` beta theorem is a
separate dependency and is not re-proved here.
