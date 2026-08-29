# TD6 V89H12 R1 free-count erratum

Date: 2026-08-26

Both R1 AWS lanes rebuilt literal FIRST and P12, specialized `F=0`, and then
stopped at the preregistered assertion that there were 17 nonpivot
variables.  This assertion conflated two different counts:

- the transported kernel has 132 parameter variables;
- the frozen FIRST pivot list has 38 distinct variables, hence the quotient
  has 94 nonpivot variables;
- 17 is only the number of nonzero parameter records (including the empty
  record) in the frozen pure-q14 cokernel class.

R1 performed no directional solve and computed no new P12 normal form.  It
is a fail-closed structural diagnostic, not a mathematical result.  R2
retains the same literal source, all-22-q scope, flag, pivot policy, and
`F=0` open, but enumerates and solves all 94 nonpivot directions.  The H11
empty-parameter functional remains unchanged because it sets every
nonpivot variable to zero independently of their count.
