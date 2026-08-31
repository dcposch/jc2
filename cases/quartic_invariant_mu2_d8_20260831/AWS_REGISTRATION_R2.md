# AWS registration R2: reconciled raw and unique counts

The verified R1 diagnostics observed `53` unique actual generators and `54`
unique target-3 generators. Independent local expansion shows that these are
the deduplications of `57` and `58` raw nonconstant monomial coefficients:
four distinct monomials carry repeated coefficient polynomials. R2 freezes
both counts rather than weakening the gate.

```text
basis      4e9c6646e91faabc0eb44498b9e30bca6a0af7e6
runner     2d26b0f1a2ca2e27d3bc055b07c7d38030fa16cb23ee1a67733dfb3d2a420545
generator  882a18964c5cd00971fb04191469241c08a6ed2064b32cb7fce8e0210cfda755
actual     raw=57 unique=53
target3    raw=58 unique=54
drop_last  raw=57 unique=52
```

Normal, `-O`, and `-OO` local replays are byte-identical for all three
profiles. The campaign is not licensing a full Gröbner launch from this
registration: Moh's degree-at-most-100 theorem already excludes every
constant-Jacobian degree-eight pair as a nonautomorphism, so a full search
cannot produce a horn counterexample. The corrected packet is retained for
reproducibility and possible structural identity mining only; any later AWS
launch requires a new explicit registration and a stated question not
already settled by that theorem.
