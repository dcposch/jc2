# AS F-only D7 cap-boundary successor

This portable producer derives the total-degree-seven rows of the
source-corrected vertical `p=3,D=7` F-only gate from the integer Jacobian,
combines them with the reviewed D8 core, decomposes the resulting
eleven-variable/seven-row geometric support, and exhausts its literal-F3
points.

Run from this case directory:

```sh
./replay_all.sh
```

Individual commands:

```sh
python3 audit_d7_source.py
python3 audit_d7_joint.py
singular -q audit_boundary_containment.sing
singular -q audit_hzero_minass.sing
singular -q audit_hgeneric_minass.sing
```

The three direct full-ring decompositions are preregistered, optional
regressions and are intentionally excluded from `replay_all.sh`.  See
`OPTIONAL_FULL_MINASS.md` and run one at a time with
`./run_optional_full_minass.sh VARIANT OUTPUT`.

The Python source audit is symbolic over the integers before division and
reduction modulo three.  The F3 census is exhaustive, not sampled.  The
Singular computations report minimal-prime support; they do not replace the
source ideal by its radical or claim a primary decomposition.

Expected headline output:

```text
eight D7 source rows; all eight change if the divided Frobenius term is omitted
1245/6561 compatible F3 states; 3507 compatible digit points
h != 0: 8 localized minimal primes
h = 0: 6 special-fibre minimal primes
global: 13 minimal primes (8 localized closures + 5 new boundary primes)
```

This package proves only the displayed D7 successor checkpoint.  It proves
neither a next-carry survivor nor an obstruction, recurrence, all-depth
lift/no-lift statement, characteristic-zero result, counterexample, or JC2.
