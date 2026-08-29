# Exact-pair L5 desk checker

Run from the `jc2` repository root:

```text
python3 -B cases/g2_intrinsic_exact_pair_l5_reduced_denominator_20260828/verify.py
```

The standard-library checker exhausts all support subsets modulo ambient
Kummer indices `1..12`, verifying

```text
stabilizer size = gcd(kappa, support),
orbit size = reduced denominator = kappa/gcd(kappa, support).
```

It also checks two controls used in the accompanying review: `Y^2-u` on the
oversized cover `u=t^4`, and two normalized places whose Puiseux series agree
through an arbitrarily long finite prefix.  It is not a substitute for the
local normalization proof.
