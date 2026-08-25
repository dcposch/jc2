# Normalized B9 common-cubic family through modulus `3^11`

This package intersects the displayed normalized B9 coefficient family with
the integral common-cubic incidence

```text
H = y^3 + h1*x*y^2 + h2*x^2*y + h3*x^3,
P9 = P_(0,9) H^3,
Q12 = Q_(0,12) H^4,
```

where `h1,h2,h3` vanish modulo 3 and the two leading scalars are units.
All 276 determinant rows and all 23 top-form coefficient rows are retained.

The original V2 formula is quarantined in a separate frozen erratum package:
its modulus constant was reduced to zero.  V3 fixes that bug with distinct
raw and residue bit-vector constructors.  Dual-AWS V3 emitters agree at SMT
SHA-256
`5af9efbe4b138f1cb0408099c90283842b4ef0b0fef9d7d33447d51a29d53563`,
matching the independent audit formula byte-for-byte.

A source-independent compiler that does not consume the producer SMT finds
complete common-core family dimensions `55,81,99,116,133` at moduli
`3^6,...,3^10`.  At the first quadratic transition to `3^11`, the fresh
299x149 operator has rank 94 and kernel 55.  The 133 predecessor directions
split into 17 active and 116 spectators; the spectator image has rank 38 in
the 205-dimensional fresh cokernel, and the reduced nonlinear system has
zero equations.  Provisionally, this gives a `3^95` predecessor projection
and `3^150` complete displayed lift family.

The independently reconstructed witness has

```text
H = y^3 + 119880*x*y^2 + 40581*x^2*y  (mod 177147)
```

and replays all 276 determinant rows plus all 23 common-cubic rows.  Its
degree pair is exactly `(9,12)` and its leading units modulo 3 are `(2,1)`.

This is a finite-depth result over one fixed B9 mod-243 parent.  It is not an
all-depth common-core point, a characteristic-zero landing, a complete
earlier-parent cover, a maximum-twelve theorem, a counterexample, or JC2.
Heavy replay is AWS-only.
