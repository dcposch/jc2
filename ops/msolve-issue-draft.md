# DRAFT GitHub issue for algebraic-solving/msolve (HOLD: needs user approval to file)

Title: Silent mis-parse of parenthesized constant subexpressions (0.10.1)

Body:
msolve 0.10.1 silently mis-parses polynomial input containing parenthesized
subexpressions, producing a wrong Groebner basis with exit code 0.

Minimal reproduction (char 0, 1 variable):
  x
  0
  x-(3+1)
Expected: GB [x-4]. Actual: GB [x+1].

The parser appears to drop the parenthesized group's operator context
(related failure class to #354, silent x/2 mis-parse; PR #320's parser
hardening may cover it — unmerged as of 2026-08-10).

Impact: any pipeline emitting parenthesized .ms input gets silently wrong
verdicts. Workaround we adopted: emit fully expanded monomial sums only,
plus an input round-trip guard through an independent parser.

Found during a large verification campaign (systems with ~100 vars over Q);
happy to provide more cases.
