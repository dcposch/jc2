# Selected-Q8 generic-fibre/component gate (AWS-only)

This producer input treats `w` as a coefficient-field parameter and computes
the generic fibre of the exact six-row approximate-cubic quotient on

```text
x5*(x3-2*x5) != 0.
```

The fibre is zero-dimensional over `Q(w)` (or `F_ell(w)`).  Eliminating the
six quotient coordinates and the localization inverse to `v` is potentially
much cheaper than a global two-variable elimination.  If the eliminant `H`
is squarefree and

```text
deg_v(H) = vdim(generic fibre),
```

then `v` is a primitive element: absolute factors of `H` give the geometric
dominant components.  The boundary factor that specializes to `Q8(v)` must
still be identified exactly before a one-crossing or singleton conclusion.

`scan_primes.py` finds good primes where Q8 has at least two rational roots.
At such a prime, unique smooth Q8 branches make a modular factorization a
useful merger/singleton discriminator.  Modular grouping remains support
evidence until characteristic-zero lifting/flatness is certified.

Run only on AWS.  The hardened runner records source/input hashes and uses a
24-hour / 256-GiB guard.  `--absolute` is permitted only in characteristic
zero and asks `absFactorize` to factor the generic eliminant absolutely.

