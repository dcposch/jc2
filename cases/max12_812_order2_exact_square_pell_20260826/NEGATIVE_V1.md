# V1 negative custody

The first dual-AWS attempt at `20260826T115544Z` is **NO VERDICT**.

Both engines continued after Singular rejected the separate Chebyshev
identity control: powers of the named polynomial `Delta` were parsed with a
non-integer exponent type in that expression, leaving the identity variables
undefined.  The validator failed because the mandatory identity marker was
absent.  The later radical calculation happened to print the predicted
square/Chebyshev support in both fields, but those PASS-looking lines are not
admissible evidence from this attempt.

V2 replaces named powers by explicit multiplication and removes a duplicate
library load that emitted `// ** redefining` diagnostics.  It does not change
the seven Laurent equations or the proposed support.
