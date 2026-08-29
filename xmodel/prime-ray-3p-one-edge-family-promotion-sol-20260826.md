# Promotion: prime-ray `3p` one-edge arithmetic obstruction

Date: 2026-08-26

Status: **PROMOTED AT THE GLOBALLY-MINIMAL NECESSARY-CHAIN INTERFACE.**

## Theorem

For every prime `p>=7` with `p=3 mod 4`, put

```text
u=(p+1)/4,  v=(3p-1)/4,
A0=Corner(3u,1,3v).
```

The local GGV5 necessary-chain arithmetic has a starting edge of direction
`(3,-1)` from `A0` to `(1,0)`.  Its generated corners are

```text
Corner(gamma+3,3,gamma),  3<=gamma<=v,
```

where `gamma=3` is admissible but not final.  The one-edge final chains are
exactly `4<=gamma<=v`, hence number `(3p-13)/4`.  Exactly those with
`3` not dividing `gamma` carry one `MN` family, hence number `(p-3)/2`.

The Algorithm-6 control integer on this edge is

```text
Delta0=(3p-1)/4.
```

By CRT and Dirichlet, `Omega(Delta0)` is unbounded along these primes, and no
fixed divisibility shortcut `Delta0 | C(3)*p^e` can hold.  Thus neither a
uniformly finite menu of literal chain instances nor that proposed factor
bound can give a prime-uniform reduction.  Parametric templates and uniform
identities remain viable.

## Evidence and review

- repaired producer SHA-256: `8217cc3f354a5d079f110380c8303370ff2c773846cd3738bd6fb8d381d11cc1`;
- hostile review plus re-review SHA-256: `7f3fd2039930349a88700315ca9c55f2fb7df6da490390114e6f527d6701f33b`, verdict `CONFIRMED`;
- read-only controls at `p=7,11,19` agree with both exact counts.

The best exposed successor is `3P-E31`: uniformly exclude or degree-reduce
this exact `(3,-1)` family over `(p,gamma)`.  Emptiness of every correctly
covering terminal system is a sufficient route; nonemptiness of such an
over-approximating system does not construct a Keller pair and does not
falsify `3P-E31`.

## Scope firewall

This theorem concerns necessary chains for a globally minimal standard pair.
A high triangular source shear that raises a seed gcd from `D` to `D*p` is
nonminimal by construction, and the GGV5 interface cannot be applied to it
without a separate arbitrary-standard-pair bridge.  No arbitrary gcd-`3p`
Keller theorem, realized-chain-length bound, partial-y `(6,9)` closure,
counterexample, or JC2 conclusion follows.
