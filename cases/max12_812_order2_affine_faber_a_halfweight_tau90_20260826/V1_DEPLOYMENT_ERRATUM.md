# V1 deployment erratum

Date: 2026-08-26

The immutable V1 package with `FREEZE.sha256` SHA
`cd2f170c516133c3ecec116529aeb1e8b37468ba3f05a26df11b314c1c5d3fd6`
is deployment-negative only.  Both AWS lanes failed before any source-row
calculation because Singular parses expressions such as `cb^2/32` as a
polynomial raised to a nonintegral exponent.  The ensuing undefined
connection polynomials caused Singular 4.3.2 to terminate with signal 11.

No mathematical endpoint, source identity, or unit result was obtained
from V1.  V2 changes only these rational-coefficient spellings to
`(1/32)*cb^2` form, retains the frozen V1 design and every source variable,
and preserves the failed V1 logs as negative custody.
