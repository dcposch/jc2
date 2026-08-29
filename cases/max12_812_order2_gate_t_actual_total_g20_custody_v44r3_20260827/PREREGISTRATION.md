# ACT-TOT-G20 V44R3 iterative-parser validation repair

Date: 2026-08-27

The V44R1 exact-Q and finite-field compilers passed every construction gate.
The original validator failed at Python's default recursion limit; frozen
V44R2 raised that limit to 50,000, but Python 3.12's AST constructor still
failed on the left-associated serialization of the largest row.

V44R3 changes only row parsing.  The producer's serialized grammar is
canonical and elementary: plus-separated monomials, star-separated factors,
one integer or parenthesized rational coefficient, and optional caret
exponents.  V44R3 parses that grammar iteratively, with duplicate-monomial
and zero-coefficient failure gates.  It pins the frozen V44R2 validators and
the same immutable V44R1 compiler results, rows, and successful resource
transcripts.  Registered AWS validators must rerun full row
custody/homogeneity/parity/canonical-hash checks and the coefficientwise
mod-65521 shadow comparison.

A pass is only the minimal `ACT-TOT-G20` custody lemma.  It proves no contact
identity, endpoint, cover, ramified result, `G2` obligation, Gate T, order
two, maximum twelve, JC2, or counterexample verdict.

