# TD6 V20 raw B3 transport-factor curve

This AWS-only discriminator directly rebuilds the raw curve cut from the B3
birational chart by

```text
t^2-4t+2=0,
x=(-5t^2+20t-4)/(t-2)^2,
y=16t/(t-2)^2,
U0=w^2/y, V0=w^3/y, C0=xw^4/y^2.
```

It works over the exact degree-two field `Q(t)(w)`.  The implementation uses
an outer quadratic adapter whose direction must disappear from every raw,
first-row, remainder, and source-relation coefficient; the producer asserts
that descent.  It also asserts the B3 identity, inverse formulas, plus-one
negative control, transport/first ranks, genuine P12 reduction, every
denominator factor, and original-row source replay.  No scaling is used.

Run both deterministic first-row orders if capacity permits:

```sh
bash run_v20.sh ARCHIVE RUN_DIR PYTHON ascending b3tq EXPECTED_SHA256
bash run_v20.sh ARCHIVE RUN_DIR PYTHON reverse-first b3tq EXPECTED_SHA256
```

PASS kills only the printed localization of this raw curve.  Its `w=0`
specialization is the already separately closed origin.  No whole-B3,
three-center-family, SP2, or JC2 claim is made.
