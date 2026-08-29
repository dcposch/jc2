# Registration: exact-Q grade-13 collection and raw-F reduction

Date: 2026-08-26

Collect all seven grade-13 factor-DAG roots as exact sparse polynomials over
`Q`, with the raw predecessor polynomial `F` retained.  Require exact
cancellation of rows four through seven, exact independence of rows two and
three from the eight V2 correction variables, and exact affine dependence
of row one.  Cross-check the expanded polynomials against the unexpanded DAG
at primes 32003 and 65521.

Emit complete exact polynomial JSON and a deterministic Singular source.
Singular must reduce rows two and three modulo the raw principal ideal `(F)`,
factor the rows and their remainders, and compute their gcd.  Membership in
`(F)` is only a local source identity; nonmembership only says that the row
cuts the local predecessor sheet.  Neither outcome supplies Gate A or a
global finite-branch interface.

Required Python sentinels:

```text
P0_ODD_G13_EXACT_SOURCE_HASHES=PASS
P0_ODD_G13_EXACT_ROWS4_7_ZERO=PASS
P0_ODD_G13_EXACT_EXPANSION_CROSSCHECK=PASS
```

Required Singular sentinels:

```text
P0_ODD_G13_EXACT_SINGULAR_SOURCE=PASS
P0_ODD_G13_EXACT_SINGULAR_DONE=PASS
```

