# V26R1 held-compiler parser erratum

Date: 2026-08-27

Status: **FAILED CLOSED BEFORE OUTPUT OR TARGET DECISION.**

The first held reconstruction invoked the unchanged corrected V26 compiler
under source freeze
`8e6d6acb948c01b81809920023e3e20c25fb0166d07686c2309f961e02fbabc0`.
It stopped after 7.98 seconds, 917,220 KiB maximum RSS, and zero swaps with
`RecursionError` while Python's AST constructor parsed the frozen V24
compatibility comparison control.  That file consists of two exact
polynomials of about 12.6 MB and roughly 110,000/83,000 top-level terms.
No compiled artifact or mathematical decision was emitted.

R1 repairs only serialization parsing.  It scans a polynomial string once,
splits at `+` or `-` occurring at parenthesis depth zero, parses each shallow
term with the original exact AST parser, and merges its sparse coefficients
in place.  Nested signs and parenthesized sums stay within their original
term.  The original V26 compiler bytes and every coefficientwise comparison
remain unchanged.

Before dispatch, the adapter must compare the old and streaming parsers on
rational, signed, nested, cancelling, powered, and aliased toy expressions;
it must also show that a sign-deletion mutation changes the result and parse
a long flat sum beyond the original recursion limit.  A malformed-parenthesis
or empty-term input must fail closed.
