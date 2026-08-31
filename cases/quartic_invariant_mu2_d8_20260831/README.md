# Quartic invariant-ring reconnaissance: `(mu,r,D)=(2,2,8)`

This is a bounded pattern-mining cell for the surviving mixed/mixed one-cusp
quartic horn. It is not a rank-four exclusion and it is not a search outside
the charged primitive single-pole invariant ring.

Put

```text
A=x^2,
U=x+x^3*y,
Z=2*y+x^2*y^2,
U^2=A+A^2*Z.
```

As a `C[A,Z]`-module the invariant ring has basis `{1,U}`. The complete
pullback-total-degree-at-most-eight vector space has the 13-element basis

```text
1,
A, A^2, A^3, A^4,
Z, A*Z, A^2*Z, Z^2,
U, A*U, A^2*U, U*Z.
```

After removing constants and applying the lossless affine target
normalization to the `(U,Z)` first jet, a generic pair has twenty parameters:

```text
H1=U+sum_(i=1)^10 a_i*B_i,
H2=Z+sum_(i=1)^10 b_i*B_i,

(B_i)=(A,A^2,A^3,A^4,A*Z,A^2*Z,Z^2,A*U,A^2*U,U*Z).
```

The constant term of `J(H1,H2)` is exactly `2`. The generator expands the
full Jacobian on AWS, requires the advertised 57 nonzero coefficient
equations for target `2`, and emits their exact parameter ideal to Singular.
It also records canonical basis and equation hashes.

## Registered reconnaissance

The first wave is modular and deliberately bounded:

- actual cell at `p=32003,65521,104729`, split across idle `r6*` workers;
- both `std` and `slimgb` represented;
- target-`3` mutation, which must return the unit ideal immediately;
- dropped-equation control, whose input hash must differ and which must never
  be mistaken for the actual cell.

Each remote lane is AWS-identity checked, source-hash and Git-basis pinned,
single-threaded, memory capped below 80% of its host, time capped, orphan-safe,
and self-hashing. Heavy generation and every Singular call are forbidden on
the local coordinator.

The stopping rule is to avoid a characteristic-zero Groebner calculation
unless at least two good primes exhibit a stable zero-dimensional component,
a repeated syzygy/leading-form obstruction, or another exact pattern worth
lifting. A positive-dimensional modular component or timeout is reusable
reconnaissance, not evidence of a Keller map. An empty modular ideal is not a
characteristic-zero theorem.

Only these outputs can change the research ledger:

- `PATTERN_IDENTITY`, followed by an exact rational certificate;
- `POSITIVE_CANDIDATE`, quarantined until independent exact field-degree and
  boundary verification;
- `NO_PATTERN_WITHIN_D8`, with basis/ideal/transcript hashes retained.

