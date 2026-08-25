# Normalized `(9,12)` order-three `nu=1` fibre probe

This bounded producer probe fixes `k=mu=0`, normalizes the nonzero invariant
`nu` to one, and asks only for the exact standard-basis dimension/degree of
the seven lower Faber equations in approximate-cubic coordinates.

```sh
python3 cases/max12_912_order3_nu1_probe_20260824/generate.py | Singular -q
```

The probe is a component-width discriminator. It is not an emptiness test,
primary decomposition, rational-trajectory classification, Taylor-boundary
reconstruction, maximum-twelve theorem, or JC2 claim.
