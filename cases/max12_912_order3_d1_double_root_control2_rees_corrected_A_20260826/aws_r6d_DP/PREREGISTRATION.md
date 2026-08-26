# Preregistration: corrected direct-saturation A

The prior A source is invalid as an independent encoding because its rendered
factored row `E8` differs from the frozen expanded B polynomial by the nonzero
constant

```text
-25134148616192/43046721.
```

This package does not repair that formula by hand.  Its AWS-only compiler
extracts `E1,...,E8,LT` byte-for-byte from the pinned, reviewed expanded B
source and changes only the contraction algorithm from inverse-variable
elimination to direct `sat(I,<s>)`.

Pinned inputs:

```text
c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b  base_B.sing
d5317aacf229d85b7b550c40e85d2b7294cae99ba0dedf2e56c2064d4d9ec088  expected_B_certificate.stdout
```

Two outputs are emitted:

- LPDP: `(lp(1),dp(8))`, the same induced order on `(s;coordinates)` as the
  inverse-B elimination ring after removing its inverse variables;
- DP: global `dp`, an independent order replay.

Each requires:

1. direct saturation and `s=0` special fibre;
2. mutual generator reduction with the 35-generator B special-fibre ideal
   parsed from the frozen certificate stream;
3. `la^20` membership in the full special fibre;
4. `TORUS` membership, saturation exponent one, unit torus localization, and
   residue no-lift;
5. a unique encoding-specific PASS marker, rc zero, and empty CAS stderr.

Exact scope remains only the fixed-axis, fixed-load, eight-coordinate support
and weight `(4,1,1,22,22,30,30,30)`.  It is not a whole-ray/fan, D1, or JC2
claim.

AWS registrations and caps are recorded before GO.  No local compiler or CAS
execution is permitted.
