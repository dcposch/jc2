# Preregistered pure-N degree-ten successor

## Frozen inputs

The compiler consumes the source-hashed degree-12/11 AWS runner at

```text
cases/as_fonly_d7_vertical_next_top_carry_20260824/compile_next_top_carry.py
SHA-256 1fc18eeb80ad3ae3b8c498fe5548e9adda423df1df60237077e0df6ef5e30d44
```

and the frozen radial identity report

```text
xmodel/as-fonly-binary-top3-radial-char3-20260824.md
SHA-256 06b17cb522f8d08199f0eadc9019a3e6ea51b0e35d0587014c24839f2ad30e22
```

## Exact test

First reproduce the predecessor's exact degree-12 and degree-11 counts.
Then impose all eight nonzero coefficients of

```text
N10={C7,D5}+{C5,D7}=(c2*d0-c0*d2)'.
```

The three absent bidegrees are `x^2y^8,x^5y^5,x^8y^2`; their vanishing is
the characteristic-three derivative cokernel, not dropped equations.
Every degree-six self-bracket vanishes, so no degree-six spectator is solved
or enumerated at this row.

## Interpretation

- zero survivors is an exact obstruction for the charged vertical finite-
  depth branch represented by the frozen predecessor;
- a survivor passes only the pure quadratic top rows 12,11,10;
- degrees 9..7 still require the quotient carry and the first-/next-digit
  cross, and then another Cartier row;
- timeout, OOM, or mismatch with the predecessor counts is no verdict.

There is no recurrence, all-depth, characteristic-zero, no-lift,
counterexample, or JC2 inference.
