# TD12 formal cascade-rank v1 checker

This is a tiny exact-`Fraction`, standard-library control for the sealed
`TD12-FORMAL-CASCADE-RANK/v1` report.  It does not search for a Keller pair,
construct source jets, run a CAS, or consume a route realization.

It checks rational sample instances of the symbolic proof:

- the root-floor factorization of the reduced `Z` operator;
- injectivity and the nominal/sharp finite-cap cokernel dimensions;
- the B versus sibling endpoint-resonance tables; and
- one nonzero order-two binomial response in each route.

Run both modes:

```text
PYTHONDONTWRITEBYTECODE=1 python3 cases/td12_formal_cascade_rank_v1_20260829/check.py
PYTHONDONTWRITEBYTECODE=1 python3 -O cases/td12_formal_cascade_rank_v1_20260829/check.py
```

The outputs are byte-identical (`648` bytes) with SHA-256
`35f6f1719154755b82c58d13db8fdc9045152f8f780053cca59102d6b9e6f008`.

Checker SHA-256:
`ea911af2906b71802507bd02a5aab728645e823e2148d04b8a35e44fb5fca261`.
